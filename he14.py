#sending mail using python


import smtplib


s=smtplib.SMTP("smtp.gmail.com","587")
s.starttls()
sender="hemaishanya123@gmail.com"
receiver="deepikavajravelu5817@gmail.com"
msg="hii"
s.login(sender,"sanjayhema")
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()