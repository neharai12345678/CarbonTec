import winreg
#connecting to key in registry
def ConnectRegistery():
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

    access_key = winreg.OpenKey(access_registry,r"SOFTWARE\Microsoft\Windows\CurrentVersion")
    #accessing the key to open the registry directories under
    for n in range(20):
        try:
            x =winreg.EnumKey(access_key,n)
            print(x)
        except:
            break