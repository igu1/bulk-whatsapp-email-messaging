import csv
import os
from messaging_api_wrapper import WhatsApp, Email


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def emailMessaging(emails, names,  message):
    email_instance = Email(
        from_email="",
        app_password="",
        templates_dir=os.path.join(BASE_DIR, "templates"),
    )
    for email, name in zip(emails, names):
        email_instance.send(
            to_email=email,
            body=message,
            context={
                "Name": name
            },
        )
    

def whatsAppMessaging(numbers, message):
    whatsapp_instance = WhatsApp(
        url="",
        token="",
        wapaId=""
    )
    for number in numbers:
        whatsapp_instance.send_message(recipient_phone=number, message=message, components= {
            "dsads"
        },
        language_code="en",
        template_name=None,
        )
        print(f"Sending message to {number}: {message}")

def read_csv_columns(filepath):
    data = []
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            try:
                col1 = row[0]
                col2 = row[1]
                if len(row) > 2:
                    col3 = row[2]
                else:
                    col3 = None
                data.append([col1, col2, col3])
            except IndexError:
                print(f"Skipping row due to insufficient columns: {row}")
    return [[x[0] for x in data], [[x[1] for x in data]],  [x[2] for x in data] or []]
   


names, numbers, emails = read_csv_columns(f'\mass_messager\data\data.csv')
