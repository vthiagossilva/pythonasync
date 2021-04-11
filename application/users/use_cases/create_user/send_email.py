import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import EMAIL_CREDENTIALS


async def send_welcome_email(name: str, email: str):
    content = f"""
        <body>
            <h2 style='text-align: center'>Bem-vindo(a), {name}!</h2>
            <p>Wheezy Tech está feliz em ter você conosco</p>
        </body>
    """

    message = MIMEMultipart()
    message["To"] = email
    message["From"] = "wheezy@wheezytech.com.br"
    message.attach(MIMEText(content, "html"))

    server = aiosmtplib.SMTP(hostname="smtp.mailtrap.io", port=2525)
    await server.connect()
    await server.starttls()
    await server.login(EMAIL_CREDENTIALS["user"], EMAIL_CREDENTIALS["password"])
    await server.sendmail(message["from"], message["To"], message.as_string())
    server.close()
