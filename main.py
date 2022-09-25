from email import header
from email.mime import image
import time
from turtle import forward
from win10toast_click import ToastNotifier
from CarbonFootPrintGraph import *
from CarbonFootPrintWebPage import *
from SustainabilityPage import *
from Repository import *
if __name__ == '__main__':
	# data=ConnectRegistery();
	toaster = ToastNotifier()
	toaster.show_toast(
		title="CarbonTec",
		msg="Carbon Footprints report is ready. Click here for details and tips!",
		icon_path=".\images\CarbonTecLogo.ico",
		duration=20,
		threaded=False,
		callback_on_click=openSettings
		 )
	# winsound.Beep(frequency=2500,duration=1000)

# import sys
# print(sys.executable)
