from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from ..models import *
from fpdf import FPDF
import string
import random
import os


def create_pdf(township, admin_creds):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(38, 10, township.name, border='B', ln=1, align='C')
    pdf.ln()

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(150, 6, 'Admins', border=0, ln=1, align='L')

    pdf.set_font('Times', '', 10)
    for admin in admin_creds:
        pdf.set_x(20)
        pdf.cell(20, 4, 'Username: ', border=0, ln=0, align='L')
        pdf.cell(20, 4, admin['username'], border=0, ln=1, align='L')
        pdf.set_x(20)
        pdf.cell(20, 4, 'Password: ', border=0, ln=0, align='L')
        pdf.cell(20, 4, admin['password'], border=0, ln=1, align='L')
        pdf.ln()

    path = township.application_id + '.pdf'
    pdf.output(path)
    return path


def random_string(length):
    letters = string.ascii_lowercase + string.digits
    random_str = ''.join(random.sample(letters, length))
    while User.objects.filter(username=random_str).count() != 0:
        random_str = ''.join(random.sample(letters, length))
    return random_str


def generate_dict(admin):
    data_dict = dict()
    data_dict['admin_id'] = admin.id
    data_dict['first_name'] = admin.first_name
    data_dict['last_name'] = admin.last_name
    data_dict['designation'] = admin.designation
    data_dict['phone'] = admin.phone
    data_dict['email'] = admin.email
    return data_dict


@csrf_exempt
def get_admins(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse([{'login_status': 0}], safe=False)

    admins = User.objects.filter(township=user.township, type='admin', profile_updated=True)
    return JsonResponse([{'login_status': 1, 'request_status': 1}, [generate_dict(admin) for admin in admins]],
                        safe=False)


@csrf_exempt
def add_admins(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse([{'login_status': 0}], safe=False)

    if user.type != 'admin':
        return JsonResponse([{'login_status': 1, 'request_status': 0}], safe=False)

    admins = []
    admin_creds = []
    for i in range(int(request.POST['num_admins'])):
        random_uname = random_string(8)
        random_pwd = random_string(8)
        admin_creds.append({'username': random_uname, 'password': random_pwd})
        admin = User.objects.create(username=random_uname, password=make_password(random_pwd, None, 'md5'),
                                    township=user.township, type='admin')
        admins.append(admin)

    pdf_path = create_pdf(user.township, admin_creds)

    html = get_template('pfa_user_details.html')
    html_content = html.render({})

    client_email = EmailMultiAlternatives('You\'re onboard!',
                                          f'The PDF attached in this e-mail contains the login credentials for admins, residents and security desks. Please share the same with your society\'s residents. Please note that the password must be changed after the first login.',
                                          settings.DOMAIN_EMAIL, [user.email])
    client_email.attach_alternative(html_content, "text/html")
    client_email.content_subtype = 'html'
    client_email.attach_file(pdf_path)
    client_email.send()
    os.remove(pdf_path)

    return JsonResponse([{'login_status': 1, 'request_status': 1}, [generate_dict(admin) for admin in admins]],
                        safe=False)
