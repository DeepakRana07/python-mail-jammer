from flask import Flask
from flask_mailman import Mail, EmailMessage

mail=Mail()


app= Flask(__name__)
app.config["MAIL_SERVER"]="......"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"]= "..."
app.config["MAIL_PASSWORD"] ="......."
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False

mail=Mail(app)

@app.route('/send')
def sendmail():

    msg= EmailMessage(

        subject="fgsfdgsf",
        recepient=['gmail.com'],
        body='This is a test email',
        mail_from='........'
       

    )
    EmailMessage.html="<b> heyt paul </b> , sending you this email from  my <a href='https://google.com'>Flask app</a>,link if it works"
    mail.send(EmailMessage)


    return "Message is send!"


if __name__=="__main__":
    app.run(debug=True,port=7000)
    



