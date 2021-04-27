import requests
import aiohttp
import time
import os
import datetime
import asyncio
#os.system('cls')
thetitle = f"""
██╗     ██╗   ██╗██╗   ██╗    ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
██║     ██║   ██║██║   ██║    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║   ██║    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
██║     ██║   ██║╚██╗ ██╔╝    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
███████╗╚██████╔╝ ╚████╔╝     ███████║██║ ╚████║██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝   ╚═══╝      ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                           """
print(thetitle)
print('Made By a uhzivert on instagram')
name = input("shit you wanna snipe: ")
f = open("bearer.txt", "r")
bearer = f.read()
#bearer = input("Bearer: ")
delay = int(input("your custom ms delay: "))
droptime = time.mktime(
	datetime.datetime.fromisoformat(
		requests.get(f'https://api.nathan.cx/check/{name}').json()['drop_time'][:-1]).replace(
		tzinfo=datetime.timezone.utc).astimezone().timetuple())
print(droptime)
async def main():
    headers={"Content-type": "application/json", "Authorization": "Bearer " + bearer}
    json={"profileName": name}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post("https://api.minecraftservices.com/minecraft/profile", json=json) as r:
            #json_body = await r.json()
            print('Request sent @ ' + str(time.time()) + ' with the code ' + str(r.status))
if droptime + - time.time() > 60:
    print('Sniping ' + name + ' in ' + str(round((droptime + - time.time()) / 60 )) + ' minutes!')
if droptime + - time.time() < 60:
    print('Sniping ' + name + ' in ' + str(round(droptime + - time.time())) + ' seconds!')
time.sleep(droptime + - time.time() - (delay / 1000))
loop = asyncio.get_event_loop()
coroutines = [main() for _ in range(6)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
