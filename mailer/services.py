from django.conf import settings
from django.core.mail import send_mail
from mailer.models import MailingSettings, MailingLog
from smtplib import SMTPException


def send_email(message_settings, message_client):
    result_msg = 'Успешно'
    try:
        result = send_mail(
            subject=message_settings.message.subject,
            message=message_settings.message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[message_client.client.email],
            fail_silently=False,
        )

    except SMTPException as fail:
        result_msg = fail

    MailingLog.objects.create(
        status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
        settings=message_settings,
        client_id=message_client.client_id,
        mailing_service_response=result_msg
    )

    def send_mails():
        for mail_settings in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
            for mail_client in mail_settings.mailingclient_set.all():
                send_email(mail_settings, mail_client)
