import imaplib
import email
from email.header import decode_header
import datetime
import base64
import pandas as pd
import glob
import os
import os.path
#подключение к почте
UserName = ''  #Указываются данные почты с настроенным IMAP
Password = ''
mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login(UserName, Password)

mail.list()
mail.select("inbox") #переход во входящие

result, data = mail.uid('search', None, 'ALL')
latest_email_id = data[0].split() #последнее письмо
path_work = 'ddsfsfdfdsfs'   #Путь куда будут сохраняться эксели, после опроса почты, после работы скрипта удаляются

for j in latest_email_id:                                               #Проход по письмам и скачивание вложений
    result, data = mail.uid('fetch', j, "(RFC822)")   
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('UTF-8')
    email_message = email.message_from_string(raw_email_string)
    MessSubj = decode_header(email_message["Subject"])[0][0].decode()

    if MessSubj.lower() in ['тест', 'fwd: тест', 'test'] :             #Проверка на темы письма, список можно расширить
        filelist = []
        path_download = './xlsx/' + datetime.datetime.today().strftime("%d-%m-%Y") + '/'  #пусть сохранения идет в папку где находится скрипт

        if not os.path.exists(path_download):          #проверка наличия папки
            os.makedirs(path_download)

        for part in email_message.walk():
            if part.get_content_maintype()=='multipart' or part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            transfer_encoding = part.get_all('Content-Transfer-Encoding')

            if transfer_encoding and transfer_encoding[0] == 'base64':
                filename_parts = filename.split('?')
                filename = base64.b64decode(filename_parts[3]).decode(filename_parts[1])
                if '.xls' in filename:
                        filelist.append(filename)
                        print('Закачали файл: ', filename)
                        
                        with open(path_download+filename, 'wb') as new_file:                       #сохранение копии
                            new_file.write(part.get_payload(decode=True))
                        with open(path_work+filename, 'wb') as new_file:                           #сохранение для соединения с итоговой таблицей
                            new_file.write(part.get_payload(decode=True))
        break
    mail.store(j, "+FLAGS","\\Deleted")            #очистка почты
mail.expunge()
  
if len(os.listdir(path_work)) > 0:   
    df = pd.concat([pd.read_excel(f, header=None)[2::] for f in glob.glob(fr'{path_work}/*.xlsx')], axis=0, join='outer')
    df_base = pd.read_excel("dfsdst.xlsx", header=None)   #Путь к итоговой таблице, должна содержать шапку
    df_base=pd.concat([df_base, df], axis=0, join='outer')
    df_base.to_excel('dfsdst.xlsx',index=False, header=False)  #Перезапись

    for file in os.scandir(path_work):        #Удаление всех файлов из рабочей папки с экселями
        os.remove(file.path)
else:
    print('файлов нет')