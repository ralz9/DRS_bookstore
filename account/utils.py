from django.core.mail import send_mail

"""
импортирую send_mail для отправки электронной почты
"""


def send_activation_code(email, code):
    send_mail(
        'Books_activate',
        f'Привет, для активации аккаунта перейди по данной ссылке: \n\n http://localhost:8000/api/account/activate/{code} ',
        'RodionDereha@gmail.com',
        [email]
    )