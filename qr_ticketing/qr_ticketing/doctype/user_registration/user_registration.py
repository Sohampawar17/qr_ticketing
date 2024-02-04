# # Copyright (c) 2023, Quantbit and contributors
# # For license information, please see license.txt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import frappe
import qrcode
from qr_demo.qr_code import get_qr_code 
from frappe.model.document import Document
from frappe.utils.pdf import get_pdf
import os

class UserRegistration(Document):
	
	@frappe.whitelist()
	def before_save(self):
		url = f'{self.name}'
		self.qr_code = get_qr_code(url)
	
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)
		qr.add_data(url)
		qr.make(fit=True)
		qr_img = qr.make_image(fill_color="black", back_color="white")
		qr_img.save("qrcode.png")

		current_site_name = frappe.local.site
		html_content = """
				<!DOCTYPE html>
					<head>
						<meta charset="UTF-8">
						<meta name="viewport" content="width=device-width, initial-scale=1.0">
						<style>
							body {{
								font-family: Arial, sans-serif;
								margin: 0;
								padding: 0;
								box-sizing: border-box;
								}}
								.card {{
								width: 640px;
								margin: 20px;
								padding: 20px;
								background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
								border-radius: 15px;
								box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
								text-align: center;
								}}
								.tlcmember{{
									border: 2px solid White;
									margin: auto;  
									padding: 5px;
									text-align: center;
									width:25%;
									margin-left:43%;
									}}
						</style>
					</head>
					<body>
						<div class="card" style="background-image: url('https://events.erpdata.in/files/TLC_back.png');">
								<table style="margin-left: 110px;">
									<tr style="text-align: center;">
											<td>
												<img style="margin-top: 10px; height: 73px; width: auto;" src="https://events.erpdata.in/files/TLC.png" alt="Company Logo">
											</td>
											<td style="text-align:centre" ><h1 style="font-size: 25px; margin-left:4px"><b>TLC Big Bash 2024</b></h1>
												<p style="font-size: 20px;">Sangli</p>
											</td>
									</tr>
								</table>
								<table style="margin-left:10px;">
									<tr style="text-align: left;">
											<td style=" width: 40%;">
											<img style=" border-radius:25px; border: 3px solid #ddd;margin-top: 20px; height: 172px; width:195px;" src="https://events.erpdata.in/files/image_tlc%20(1).png" alt="Company Logo">
											</td>
											<td style=" width: 60%;">
												<div class="content" style="margin-top:18px; ">
												<p style="font-size: 18px;"><b>Name</b> :&nbsp{1} </p>
												<p style="font-size: 18px; "><b>Mobile</b> :&nbsp{2}</p>
												<p style="font-size: 18px;"><b>City </b>:&nbsp&nbsp&nbsp{0}</p>
												<p style="font-size: 18px; "><b>Level</b> :&nbsp&nbsp{3}</p>
												<p style="font-size: 18px; "><b>Company</b>:&nbsp{4}</p>
												</div>
											</td>
									</tr>
									<tr style="text-align: left;">
											<td style=" width: 40%;">
											<div class="qr-code">
													<img style=" border-radius:25px; border: 3px solid #ddd;margin-top: 24px; height: 172px; width:195px;"  src="{5}" alt="QR Code">
												</div>
											</td>
											<td style="width:60%;">
												<div class="content" style="margin-top:30px; ">
												<p style="font-size: 18px;"><b>Event Date</b> :&nbsp 10 & 11 Feb 2024</p>
												<p style="font-size: 18px;"><b>Venue</b>:&nbsp&nbsp&nbspDhananjay Garden, Sangli, Maharashtra.</p>
												<p style="font-size: 18px;"><b>Registration Id</b> :&nbsp{6}</p>
												</div>
											</td>
									</tr>
								</table>
									<div class="tlcmember">
										<p style="font-size: 20px;"><b>TLC MEMBER</b></p>
									</div>
								
								<p style="text-align: left;font-size: 21px;margin-left:15px;"><b>Note</b>:</p>
								<ul style="text-align: left; margin-left:30px;font-size:15px;">
									<li >For all event updates and information, please visit <a href="https://tlcbigbash.com" class="text-left-top">https://tlcbigbash.com</a> </li>
									<li>For accommodation in Sangli, please see our recommended hotel details <a href="https://tlcbigbash.com/hotels" class="text-left-top">https://tlcbigbash.com/hotels</a> . We have special hotel rate for TLC members and hotel coordinators for booking. Please check special rate card for hotel and their contact details from <a href="https://tlcbigbash.com/rate_chart" class="text-left-top">https://tlcbigbash.com/rate_chart</a></li>
									<li >For any registration related queries, please contact us on +91 78700 11818.</li>
									<li > Sangli is a beautiful city and holy place situated on bank of Krishna. Sangli has many tourist places & temples nearby, you can enjoy them while you are in Sangli. Some sightseeing options are suggested by our team. For more details, please visit on <a href="https://tlcbigbash.com/aboutsangli" class="text-left-top">https://tlcbigbash.com/aboutsangli</a></li>
								</ul>  
						</div>
					</body>
			</html>
		""".format(self.custom_city,self.user_name,self.wtsp_number,self.custom_tlc_level,self.custom_company_name,self.qr_code,self.name)
		pdf_content = get_pdf(html_content, {'orientation': 'Portrait'})

		
		target_directory = frappe.get_site_path('public', 'files')
		os.makedirs(target_directory, exist_ok=True)
		check_exist_file=""
		if(self.custom_pdf_data):
			check_exist_file=f"./{current_site_name}/public{self.custom_pdf_data}"

		if os.path.exists(check_exist_file):
			attachment_name = frappe.get_value("File", {"file_url": self.custom_pdf_data}, "name")
			if attachment_name:
				frappe.delete_doc("File", attachment_name, force=True, ignore_permissions=True)


		file_path = os.path.join(target_directory, f'{self.name}.pdf')
		with open(file_path, 'wb') as file:
			file.write(pdf_content) 
		
  
		file_doc = frappe.get_doc({
			'doctype': 'File',
			'file_name': f'{self.name}.pdf',
			'attached_to_doctype': self.doctype,
			'attached_to_name': self.name,
			'file_url': file_path,
			'content': pdf_content
		})
		file_doc.save(ignore_permissions=True)
		self.pdf_attachment = file_doc.file_url
		self.custom_pdf_data=file_doc.file_url
		


		smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
		smtp_port = 25  # Replace with your SMTP server's port (587 for TLS)
		smtp_username = 'support@quantbit.io'  # Replace with your SMTP username
		smtp_password = 'xnia pefr nlmx cxwx'  # Replace with your SMTP password
		sender_email = 'support@quantbit.io'  # Replace with your email address
		receiver_email = self.email  # Replace with the recipient's email address

	# Create a message
		subject = 'QR Code'
		message = 'This is a QR code To '+ " " +self.user_name

		msg = MIMEMultipart()
		msg['From'] = 'Quantbit Technologies Pvt. Ltd.'
		msg['To'] = self.email
		msg['Subject'] = 'Event QR Code'

		msg.attach(MIMEText(message, 'plain'))

	# Attach the QR code image
		qr_filename = "qrcode.png"
		qr_attachment = open(qr_filename, "rb")
		qr_base = MIMEBase('application', 'octet-stream')
		qr_base.set_payload(qr_attachment.read())
		encoders.encode_base64(qr_base)
		qr_base.add_header('Content-Disposition', f'attachment; filename={qr_filename}')
		msg.attach(qr_base)
		
	
	# Connect to the SMTP server
		try:
			server = smtplib.SMTP(smtp_server, smtp_port)
			server.starttls()  # Enable TLS encryption
			server.login(smtp_username, smtp_password)
    
    # Send the em
			server.sendmail(sender_email, receiver_email, msg.as_string())
		except Exception as e:
			print(f'Email could not be sent. Error: {str(e)}')
		finally:
			server.quit()  # Close the SMTP server connection
		
  
  
  
  
  
  
  