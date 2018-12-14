import os
from twilio.rest import Client
from datetime import date, datetime
import sqlite3
from sqlite3 import Error


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(BASE_DIR, "db.sqlite3")
user_id = 16
today = date.today()
toPhone = None
# isToday = None
account_sid = "ACd3ee8a9c545c4365f7a9165036c74862"
auth_token = "592fa0831ffded034a5f43fd6e16bcb3"
client = Client(account_sid, auth_token)
select_sql = 'select user_id, phone, max(record_date) record_date \
                from Bigfit_weighttracker w, Bigfit_user u \
               where w.user_id = u.id \
                 and user_id = ? \
            group by user_id, phone \
              having max(record_date) < date(?)'

try:
    conn = sqlite3.connect(db)
except Error as e:
    print(e)

cur = conn.cursor()
cur.execute(select_sql, (user_id, today))
rows = cur.fetchall()

for row in rows:
    toPhone = '+1' + row[1]
    print(toPhone)
    client.messages.create(
        to=toPhone,
        from_='+17143121347',
        body='Just a friendly reminder that you have not entered in your weight \
        today. Thank you BigFit')

conn.close()

# for row in rows:
#     weightDate = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
#     # print(weightDate.date())
#     # print(today)
#     if weightDate.date() == today:
#         isToday = True
#         exit()
#
# if not isToday:
#     client.messages.create(
#         to='+17146968284',
#         from_='+17143121347',
#         body='Just a friendly reminder that you have not entered in your weight \
#         today. Thank you BigFit')


