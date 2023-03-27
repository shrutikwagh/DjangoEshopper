# importing libraries
from flask import Flask
from flask_mail import Mail ,Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shrutikawagh6460@gmail.com'
app.config['MAIL_PASSWORD'] = 'Shruti@6460'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# message object mapped to a particular URL ‘/’
# @app.route("/")
def send_mail(receiver):
    msg = Message(
				'Hello',
				sender ='shrutikawagh.test123@gmail.com',
				recipients = receiver
			)
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'Sent'




if __name__ == '_main_':
	app.run(debug=True, port=8001)