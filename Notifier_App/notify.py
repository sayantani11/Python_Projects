from plyer import notification
from datetime import datetime,date

# taking in account the current date
today =  date.today()
current_date = str(today.strftime("%d/%m/%Y"))

# taking in account the current time
time = datetime.now()
current_time = str(time.strftime("%H:%M:%S"))

# template for writing the notification
if current_date == "07/08/2023":   # setting the date and time when the notification should beep
    notification.notify(
        title = "Python Project Repository",   # title of notification
        message = "Notification app",          # message for the notification
        app_icon = None,
        timeout = 10
    )