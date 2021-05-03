import win32evtlog
import win32evtlogutil
import operator
import datetime
import pandas as pd

# d1 = datetime.datetime.now()
# d2 = d1.replace(hour=22)
# d3 = d2.replace(minute=00)
# d4 = d3.replace(second=00)
# d5 = d4.replace(microsecond=000000)
# d6 = d5.replace(hour=5)
# if (d1.hour <=12):
    # print("")
# else:
    # d7 = d6 + datetime.timedelta(days=1)
    
# difference = (d7 - d5)
# minutes = difference.total_seconds()/60
# print(minutes)

# df = pd.DataFrame({
    # 'year': [d1.year,d5.year,d7.year],
    # 'month': [d1.month,d5.month,d7.month],
    # 'day': [d1.day,d5.day,d7.day],
    # 'hour': [d1.hour,d5.hour,d7.hour],
    # 'minute': [d1.minute,d5.minute,d7.minute],
    # 'microsecond': [d1.microsecond,d5.microsecond,d7.microsecond]})
    
# def time(rows):
    # return (pd.Timestamp(rows.year, rows.month,
                         # rows.day, rows.hour, rows.minute))
                       
# df['new_time'] = df.apply(time, axis = 'columns')


server = 'DESKTOP-81CL7DC' # name of the target computer to get event logs
logtype = 'Security'
hand = win32evtlog.OpenEventLog(server,logtype)
flags =  win32evtlog.EVENTLOG_SEQUENTIAL_READ|win32evtlog.EVENTLOG_FORWARDS_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

while True:
    events = win32evtlog.ReadEventLog(hand, flags,0)
    
    for event in events:
        data = event.StringInserts
        
        if event.EventID == 4688:
            if data.__contains__("C:\\Windows\\System32\\net.exe") or data.__contains__("C:\Windows\System32\OpenSSH\ssh.exe") or data.__contains__("C:\Windows\System32\mstsc.exe"):
                print("event created")
                print('Event Category:', event.EventCategory)
                print ('Time Generated:', event.TimeGenerated)
                print ('Source Name:', event.SourceName)
                print ('Event ID:', event.EventID)
                print ('Event Type:', event.EventType)
                print ('Source Name:', event.SourceName)
                data = event.StringInserts
                time = event.TimeGenerated.hour
                if ((time >= 22) or (time <= 5)):
                    if data.__contains__("C:\\Windows\\System32\\net.exe"):
                        print("net command has been used")
                        print(data)
                    elif data.__contains__("C:\Windows\System32\OpenSSH\ssh.exe"):
                        print("ssh has been used")
                        print(data)
                    elif data.__contains__("C:\Windows\System32\mstsc.exe"):
                        print(" remote desktop has been used")
                        print(data)
                    else:
                        print("not found")
                else:
                    print("No Running Process Found")
        else:
            pass
