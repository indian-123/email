
import smtplib 
GMAIL_ID = 'indimano321@gmail.com'
GMAIL_PSD  = 'yhxzthzzwgtjxvah'
to="indiangithub321@gmail.com"
sub="hiindian" 
msg ="hi manju "
def sendmail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
       s.login(GMAIL_ID, GMAIL_PSD)
       s.sendmail("indian", to, f"subject: {sub} \n\n {msg}")
    except:
        print("Unwanted error occured!! :")
    s.quit()
for i in  range(1):
    sendmail()
    print(f"Email successfully sent for {i+1} times")
