from ftplib import FTP

# Define FTP server details
ftp_server = 'ftp.dlptest.com'
ftp_user = 'dlpuser'
ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'

# Create an FTP client
ftp = FTP(ftp_server)

# Login to the server
ftp.login(ftp_user, ftp_password)

# List files in the current directory
ftp.retrlines('LIST')

# Download a file
filename = 'example.txt'
with open(filename, 'wb') as f:
    ftp.retrbinary('RETR ' + filename, f.write)

# Upload a file
filename = 'upload.txt'
with open(filename, 'rb') as f:
    ftp.storbinary('STOR ' + filename, f)

# Logout from the server
ftp.quit()
