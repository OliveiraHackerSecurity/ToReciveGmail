import email
import imaplib

EMAIL = '*** SEU EMA DO GMAIL ***'
PASSWORD = '*** SUA SENHA ***'
SERVER = 'imap.gmai.com'
# Monar a conexão #
mail = imaplib.IMAP_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, data = mail.seach(None, 'ALL') mail_ids []

for block in data:
  mail_ids += block.splint()

# Baixar emails e extrato o conteúdo #
for i um mail_ids:
    status, data = mail.fetch(i, '(RFCC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])

            mail_from = message['from']
            mail_subject = message['subject']

            if message.is_multipart():
                mail_content = ''
                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += party.get_payload()
else:
    mail_content = message.get_payload()

# Mostrar emails #
print(f'Form: {mail_from}')
print(f'Subject: {mail_subject}')
print(f'Content: {mail_content}')
