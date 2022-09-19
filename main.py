from email import header
from email.mime import image
import time
from turtle import forward
import winsound
from win10toast_click import ToastNotifier
from CarbonFootPrintGraph import *
from CarbonFootPrintWebPage import *
from SustainabilityPage import *
from Repository import *
if __name__ == '__main__':
	data=ConnectRegistery();
	print(data);
	toaster = ToastNotifier()
	toaster.show_toast(
		"**Your Carbon foot print!!",
		"A carbon footprint is the total greenhouse gas (GHG) emissions caused by an individual, event, organization, service, place or product, expressed as carbon dioxide equivalent (CO2e).",
		icon_path=".\images\co2Print.ico",
		duration=12,
		threaded=False,
		callback_on_click=openSettings
		 )
	# winsound.Beep(frequency=2500,duration=1000)

# import sys
# print(sys.executable)
