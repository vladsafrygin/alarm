from datetime import datetime

from playsound import playsound

alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")


def validated_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid hour format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid minute format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid second format! Please try again..."
        else:
            return "OK!"


while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    validate = validated_time(alarm_time.lower())
    if validate != "OK!":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}")
        break


alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_per = alarm_time[9:].upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_per = now.strftime("%p")


    if alarm_per == current_per:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("WAKE UP!")
                    playsound('home/music/alarm.wav')
    break
