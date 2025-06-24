import smtplib, ssl


def send_email(message):  # Para crear funcion auto, seleccionas el script, Refactor, Extract Method
    host = "smtp.gmail.com"  # estos son datos estándar para Gmail
    port = 465
    username = "elisasuarezmoreira@gmail.com"
    password = "ciufedzyldslsaxq"
    receiver = "elisasuarezm845@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

