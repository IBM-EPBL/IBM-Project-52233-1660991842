import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email="from_email@your-whitelisted-domain.com",
    to_emails=("request.form['email']"),
    subject="Dear %Name%, A patient needs your help, please donate plasma if you can. Regards Team PlasmaDrop",
    html_content="<strong>and easy to do anywhere, even with Python</strong>")
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)