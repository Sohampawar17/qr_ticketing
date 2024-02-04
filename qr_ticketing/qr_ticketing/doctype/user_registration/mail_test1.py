import smtplib
import qrcode
from PIL import Image
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
smtp_port = 25  # Replace with your SMTP server's port (587 for TLS)
smtp_username = 'ankitamane846@gmail.com'  # Replace with your SMTP username
smtp_password = 'xrtk vsxx vahr umrz'  # Replace with your SMTP password
sender_email = 'ankitamane846@gmail.com'  # Replace with your email address
receiver_email = 'patilsayali816@gmail.com'  # Replace with the recipient's email address

# Create a message
subject = 'Test Email'


msg = MIMEMultipart()
msg['From'] = 'ankitamane846@gmail.com'
msg['To'] = 'ankitamane846@gmail.com'
msg['Subject'] = 'Test Email'
qr_code='data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAZoAAAGaAQAAAAAefbjOAAADDElEQVR4nO2bQY6cMBBFXwWkXoI0B5ijwM2iHCk3gKPMASKZZUtGPwvb4J5JFlEnTKcpFgzd8NS2VFP+/lWY+ONj/vLnDDjkkEMOOeSQQ88JWT5abFzMzPo1fYTFDJbywPgpw3PoeGiQJAXQtx4YAjDoasyvEaCRJOkWOm54Dh0Htfnv0sPwHQxAcx9kc/8DG94uKQ4Mmnj48Bw6HGrffVaKjbC2AgRc7cMG9cHn5NBfhhqZ9QCsxtw3svEf/ZJDDwx1kibA7PVqSUfMPcBipgmQFN9Dxw3PocMgasVII4bwq1N5YJCk6cHn5NA9UNIRu1IQCwCrkVcNTPUDxw7PocOhnCOG0OTd58SeNxpBJzEoIoVGniNOBK1m9irZV0WY+9U0dVfTtJgxW5sFxqcNz6GjoJQPNHWRrBnSFzHfSHmj6E7PEWeB7OvbRdCV3cTc55ONnZSt7M73GmeANmUZ0WyQ3Eu6RsDawtIjuh+tDWEtAvPB5+TQPVC1OJQFQ0VAdvVyUj3iq8YzQ2VfkZRCs4UApBAASDeqUHnwOTl0D1Qpyz0YqgBRKKepKynEI+KZIar/fYUtM3QxOxPTfsUWPg8+J4fugbYcsRlRitUyUTJDpHhVHhFPDtX+5K4ehtAUAyJdNe5HnAXalGXOAilb0GXbujKn6KJHxAmgm46ZxRCLActFRuqoMjSEl2jDtB4/PIc+CdK0XFI+SHWN1GcZmtxQN3YRWC7eZ3kCKOUIg9U0vLURaGRz36TbmkcQy0sUuIt9HkgKYGN3zV0RpTXi5lhasqL4L+bk0J17jX2bQe6FSEdXOqz2yqgry2eGSl1jK2mkdzNCqYFv1YziVnhEPDn0oc+yMrCVX97ZNaZHxGmg3cWeWM3G0ph/Y0VEbPyc4Tl0fF0jUBe9oSleFbui8FXjlNDcQ10S19VySePN/YgzQO9zRDGwS1fEtAlNyV3sM0C31fCtDSLsrRFsy8lWD33wOTl0D/S7d7rqpMDg1fDzQB/f6SJSXuIqe8766tjhOeSQQw455JBDDwz9BFQxyIx6U+v2AAAAAElFTkSuQmCC'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qr_code)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png") 
message = 'This is a test email sent from Python.'
msg.attach(MIMEText(message, 'plain'))



# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption
    server.login(smtp_username, smtp_password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully')
except Exception as e:
    print(f'Email could not be sent. Error: {str(e)}')
finally:
    server.quit()  # Close the SMTP server connection
