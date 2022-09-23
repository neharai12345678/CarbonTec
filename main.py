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
		title="CarbonTec"
		"**Your Carbon foot print!!",
		icon_path=".\images\CarbonTecLogo.ico",
		duration=12,
		threaded=False,
		callback_on_click=openSettings
		 )
	# winsound.Beep(frequency=2500,duration=1000)

# import sys
# print(sys.executable)
