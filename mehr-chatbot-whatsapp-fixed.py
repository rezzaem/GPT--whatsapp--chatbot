import requests
import json

# we use inboxino platform for connect to whatsapp
url = "https://back.inboxino.com/api/access-api/message/send"

payload = {
    'messages': [
        {
            "message_type": "message",
            "message": "این یک تست برای سنحش میزان سرعت جوابدهی میباشد"
        }
    ],
    'with_country_code': 0,
    'type': 'notification',
    'recipients': ["989025001345"],
    'setting': {
        "expire_minutes": 5
    },
    'platforms': ['whatsapp']
}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'api-token': 'inbox-tk.LWBNRQkJIfnW3fC3NoIZXlzTtIEDLFMRfi376dSehKwzxeLcFTLV5vo3fQUupJcpXb350iPQk0lcnb7E'
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print('پیام با موفقیت ارسال شد.')
else:
    print('مشکلی در ارسال پیام به وجود آمد. کد خطا: ', response.status_code)

