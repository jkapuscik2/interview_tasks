from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
import logging
from .dto import Mails
import datetime

try:
    import httplib
except:
    import http.client as httplib
from .utils import generate_csv


class smtp_mailer:
    # type of an email
    c_type = ""

    def __init__(self, **kwargs):
        many_important_args = ["u_name", "password", "smpt_server_u_name", "smtp_server_p_number"]

        for x in many_important_args:
            self.__dict__[x] = kwargs[x]

    def set_content_type(self, c_type):
        self.c_type = c_type

    def logger(self, msg, type):
        if type == 'error':
            logging.error(msg)
        elif type == 'info':
            # loggigng as info
            logging.info(msg)

    def sent(self, **kwargs):
        try:
            mandatory_args = ["subject", "source", "to", "content"]
            for x in mandatory_args:
                if not kwargs.get(x, False):
                    raise Exception("%s is mandatory" % (x))

            # Check if internet connection is up
            # no internet = no email sent
            conn = httplib.HTTPConnection("www.google.com", timeout=5)
            try:
                conn.request("HEAD", "/")
                conn.close()
            except:
                self.logger('NO INTERNET', "error")
                raise Exception("NO INTERNET")

            msg = MIMEMultipart('alternative')
            msg['Subject'] = kwargs['subject']
            msg['From'] = kwargs['source']
            msg['To'] = kwargs['to']

            content = MIMEText(kwargs['content'], self.c_type)
            msg.attach(content)
            s = smtplib.SMTP(self.smpt_server_u_name, self.smtp_server_p_number)
            s.login(self.u_name, self.password)
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
            self.logger("Mail of type {} sent :) ".format("html"), "info")

            # loggigng mailings to database as in request in Jira (SOFT-7263)
            Mails.create(
                text=msg.as_string(),
                mail_to=msg['To'],
                date=datetime.date.today(),
                details=', '.join('%s=%r' % x for x in kwargs.iteritems())
            )
        except Exception as e:
            pass

    @staticmethod
    def sendHTML(**kwargs):
        # sending mails that are in html instead of plain
        mailer = smtp_mailer()
        try:
            mailer.set_content_type("html")
            mailer.sent(**kwargs)
            mailer.logger("Mail of type {} sent :) ".format("html"), "info")
        except Exception as e:
            mailer.logger(e, "error")

    @staticmethod
    def sendText(**kwargs):
        # sending mails that are in text instead of plain
        mailer = smtp_mailer()
        try:
            mailer.set_content_type("plain")
            mailer.sent(**kwargs)
            mailer.logger("Mail of type {} sent :) ".format("plain"), "info")
        except Exception as e:
            mailer.logger(e, "error")

    @staticmethod
    def getRaport():
        receivers_mails = Mails.select("mail_to").get()

        # generating csv
        generate_csv(receivers_mails)
