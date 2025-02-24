from pypresence import Presence
import time

clientid = "your client id" # find this in General Information in your app
rpc = Presence(clientid)
rpc.connect()

rpc.update(
    state="REAL 128.30.61.24", # this the bottom text
    details="VPN 192.149.131.14", # this the top text
    large_image="nordvpn", # go 2 Rich Presence > Art Assets and upload your image of choice, and kopy the asset key name or wtv
    start=time.time() # dis the time
    )

print("2gex presence started")
print("press any key to stop")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.close()
    print("2gex presence stopped")

# and the name of your app would be the thing you'd play, like "Playing Nord VPN" or "Playing cradling my balls"
# also go to discord.dev to make your app for this
# code by 2gex!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
