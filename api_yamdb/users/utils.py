from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from users.models import User


def generate_and_send_code(username):
    """Генерация и отправка по email кода подтверждения"""
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    user.confirmation_code = confirmation_code
    send_mail(
        subject="Код подтвержения для завершения регистрации",
        message=f"Ваш код для получения JWT токена {user.confirmation_code}",
        from_email=settings.FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
    user.save()
