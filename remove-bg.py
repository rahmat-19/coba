# import os
# import rembg
# import numpy as np
# from PIL import Image

# # Define the path to the input image
# input_image_path = 'download.jpeg'
# output_image_path = 'hohoho.png'

# # Check if the file exists
# if os.path.isfile(input_image_path):
#     # Load the input image
#     input_image = Image.open(input_image_path)
    
#     # Convert the image to RGBA (if not already in that mode) to handle transparency
#     input_image = input_image.convert("RGBA")
    
#     # Convert the image to a numpy array
#     input_array = np.array(input_image)
    
#     # Remove the background
#     output_array = rembg.remove(input_array)
    
#     # Convert the result back to an image
#     output_image = Image.fromarray(output_array)
    
#     # Save or display the result
#     output_image.save(output_image_path)
    
#     output_image.show()
# else:
#     print(f"File {input_image_path} does not exist.")


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Konfigurasi server SMTP Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email = 'rahmat.hidayat38180@gmail.com'
app_password = 'xxme pwoa xsom vbzb'  # Ganti dengan kata sandi aplikasi Anda

# Detail email
to_email = 'rahmatjr023@gmail.com'
subject = 'Test Email dari Python'
body = 'Ini adalah email uji coba yang dikirim dari Python menggunakan SMTP Gmail!'

# Membuat email
msg = MIMEMultipart()
msg['From'] = 'rhthd1080@gmail.com'
msg['To'] = to_email
msg['Subject'] = subject

# Melampirkan teks email
msg.attach(MIMEText(body, 'plain'))

# Mengirim email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Meningkatkan koneksi ke SSL/TLS terenkripsi
    server.login(email, app_password)
    server.send_message(msg)
    server.quit()
    print('Email berhasil dikirim!')
except Exception as e:
    print(f'Gagal mengirim email: {e}')
