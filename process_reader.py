import wmi
import datetime

datetime.time() # start
# finish

x = wmi.WMI()
# creation
# deletion
process = x.watch_for(notification_type="creation", wmi_class=x.Win32_Process)
# process = x.Win32_Process.watch_for("creation")

while True:
    p = process()
    print p.Caption

