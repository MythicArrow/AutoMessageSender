import pywhatkit
import datetime
import time

to_number = input("Write the phone number that the message will be sent to ")
send_time = input("Write the time ")
msg = input("Write the message that will be sent ")

send_time_hour = int(send_time.split(":")[0])
send_time_minute = int(send_time.split(":")[1])

send_time = datetime.datetime.now().replace(hour=send_time_hour, minute=send_time_minute, second=0, microsecond=0)

if send_time < datetime.datetime.now():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    send_time = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour, send_time_minute))

later_1min = send_time + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    if now.hour == send_time_hour and now.minute == send_time_minute and now.day == send_time.day:
        pywhatkit.sendwhatmsg(to_number, msg, send_time_hour, send_time_minute + 1)
        print(f"Message sent- {now}")
        
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        send_time = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour, send_time_minute))
        later_1min = send_time + datetime.timedelta(minutes=1)
    
    time.sleep(60)
