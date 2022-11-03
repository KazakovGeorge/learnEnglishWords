import smtplib
import cred, config

def createMail(words):

    message = f"Subject: EnglishWords\n\nWords:\n{words}"

    smtpObj = smtplib.SMTP(f'smtp.{cred.mailDomen}.com', config.mailPort)
    smtpObj.starttls()
    smtpObj.login(cred.mailLogin, cred.mailPassword)
    smtpObj.sendmail(cred.mailLogin, cred.emailToSend, message)
    smtpObj.quit()

    print("Mail is sended")