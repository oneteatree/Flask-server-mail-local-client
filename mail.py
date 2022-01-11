from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText


# connect with Google's servers
smtp_ssl_host = 'mail.unicom-lb.com'
smtp_ssl_port = 465
# use username or email to log in
username = 'unicomsend@unicom-lb.com'
password = '!T&_bPFD@yGN'

from_addr = 'unicomsend@unicom-lb.com'
to_addrs = ['info@unicom-lb.com']

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    message = MIMEText(text)
    # the email lib has a lot of templates
    # for different message formats,
    # on our case we will use MIMEText
    # to send only text
    person = [request.form['name'],request.form['email']]
    message['subject'] = ','.join(person)
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    processed_text = text.upper()
    # we'll connect using SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # to interact with the server, first we log in
    # and then we send the message
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
    
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    

