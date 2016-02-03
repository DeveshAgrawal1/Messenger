import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
def bhejomail(sender, password, receiver, subject, body, files):

    try:
        fromaddr = sender
        toaddr = receiver
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        bodyy = body
        msg.attach(MIMEText(bodyy, 'plain'))
        for key, value in files.iteritems():
        	part = MIMEBase('application', 'octet-stream')
        	part.set_payload(open(value, 'rb').read())
        	encoders.encode_base64(part)
        	part.add_header('Content-Disposition', "attachment; filename= %s" % key)
        	msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        info='Mail sent.'
    except Exception, e:
        info='Error sending mail.'
    return info

