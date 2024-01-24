import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Sending_Mail(receiver_email, subject, content):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = "malavika2210770@ssn.edu.in"
    msg['To'] = receiver_email
    my_password = r"c97v03m04@EID"

    html = f'<html><body><p>{content}</p></body></html>'
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login("malavika2210770@ssn.edu.in", my_password)

    s.sendmail("malavika2210770@ssn.edu.in", receiver_email, msg.as_string())
    s.quit()

# Sending_Mail("malavika2210770@ssn.edu.in", "Hello", "This is sample email")