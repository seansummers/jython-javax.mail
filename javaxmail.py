import contextlib

import java.util
import javax.mail


class JavaxMailAuthenticator(javax.mail.Authenticator):
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def getPasswordAuthentication(self):
        return javax.mail.PasswordAuthentication(self.username, self.password)


def sendmail(subject, addr_to, text, properties, creds=None):
    addresses = addr_to if hasattr(addr_to, '__iter__') else (addr_to, )
    mail_to = [
        javax.mail.internet.InternetAddress(address) for address in addresses
    ]

    session = javax.mail.Session.getInstance(properties,
                                             JavaxMailAuthenticator(*creds))
    message = javax.mail.internet.MimeMessage(session)

    message.subject = subject
    message.setRecipients(javax.mail.Message.RecipientType.TO, mail_to)
    message.setText(text, 'us-ascii', 'plain')

    with contextlib.closing(session.getTransport('smtp')) as transport:
        transport.connect()
        transport.sendMessage(message, mail_to)


def load_properties(property_filename):
    properties = java.util.Properties()
    with open(property_filename, 'r') as property_file:
        properties.load(property_file)
    return properties


if __name__ == '__main__':
    content = '''
This
is the content
of the message.

That I am testing.
'''
    creds = load_properties('secret-cred.properties')
    smtp_auth = (creds.getProperty('username'), creds.getProperty('password'))
    mail_to = creds.getProperty('mailto')

    properties = load_properties('mail.properties')
    properties['mail.user'] = creds.getProperty('username')
    properties['mail.from'] = creds.getProperty('username')

    sendmail('Test of javamail', mail_to, content, properties, smtp_auth)
