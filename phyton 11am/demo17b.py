


import qrcode
text = input("Enter a message;  ")
file_path = input("Enter file name with path; ")
qrcode.make(text).save(file_path)
