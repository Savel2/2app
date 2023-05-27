import smtplib, ssl #standart python library to create emails session

def send_mail(message): 
    host = "smtp.gmail.com" #standart gmail host 
    port = 465 #that is also standart

    username = "saveliy2105@gmail.com"
    password = "fuwusnxnyjvsqnlv"


    receiver = "saveliy2105@gmail.com"
    my_context = ssl.create_default_context() #secure context (ssl library)

    with smtplib.SMTP_SSL(host,port,context= my_context) as server:
        server.login(username,password)
        server.sendmail(username, receiver, message)