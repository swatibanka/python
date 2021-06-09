import requests

url = "https://www.fast2sms.com/dev/bulk"

message = input("Enter a Message : ")

contactno = input("Enter Contact No :")

payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno

headers = {
        'authorization': "f6d07C54eWbgPSLBzJMvijGm3uHURxI9oc8nYVpDrTyqhE1lkAv1MLQ2wPkNmK4hzlWSsaVJegT7Zqtj",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
