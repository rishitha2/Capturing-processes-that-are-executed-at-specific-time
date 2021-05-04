import win32evtlog
import win32evtlogutil
import operator
import datetime
import pandas as pd

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
