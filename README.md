# Capturing-processes-that-are-executed-at-specific-time

The code provided would help to capture specific processes like net, ssh and rdp. If any of these processe are executed from 10 PM to 5 AM then it would capture the user who ran those commands along with what commands were run.

The code provided would capture the net, ssh and rdp commands. 
### Step 1: 
Please make sure your install the following before executing the code. 
python -m pip install PyPiWin32
•	pip install datetime
•	pip install pandas 
•	pip install win32evtlogutil
•	pip install win32evtlog
### Step 2: 
Once you finish installing all of them,  execute the program final_code.py and save the output into a notepad file. Please see below on how to compile and save it the output to .txt file. 
## Use: python final_code.py > path where you want to save your output\output.txt
###Step 3: 
Open a new command prompt and type commands related to net, ssh or rdp. (If the any of these processes are running at any time from 10 PM to 5 AM then it would capture those process along with who ran those processes and what command was used).
### Step 4:
Once done come back to the command prompt where you executed the code and stop it by pressing cntrl+c. 
### Step 5: 
Now go to output.txt file to see what you have captured. 


## Result

The code provided would help to capture specific processes like net, ssh and rdp. If any of these processe are executed from 10 PM to 5 AM then it would capture the user who ran those commands along with what commands were run.

## References:
https://stackoverflow.com/questions/30287121/reading-windows-event-log-in-python-using-pywin32-win32evtlog-module
https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
https://www.accadius.com/using-python-read-windows-event-logs-multiple-servers/
https://stackoverflow.com/questions/30287121/reading-windows-event-log-in-python-using-pywin32-win32evtlog-module
