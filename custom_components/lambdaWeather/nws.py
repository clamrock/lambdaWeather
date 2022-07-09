import asyncio
import aiohttp
import pynws

DETROIT = (42.33, -83.04)
USERID = "testing@address.xyz"

def ctof(temp):
    return ((temp*(9/5)) + 32)

def calculateApparent(temp, heat, wind):

    if ctof(temp) > 80:
        return ctof(heat)
    if ctof(temp) < 51:
        return ctof(wind)
    return ctof(temp)

async def example():
    async with aiohttp.ClientSession() as session:
        nws = pynws.SimpleNWS(*DETROIT, USERID, session)
        await nws.set_station()
        await nws.update_observation()
        #await nws.update_forecast()
        #await nws.update_alerts_forecast_zone()
        #await nws.update_detailed_forecast()
                                                                                                                                                                             
        current_temp = nws.observation['temperature']                                                                                                                        
        current_heatIndex = nws.observation['heatIndex']                                                                                                                     
        current_windChill = nws.observation['windChill']                                                                                                                     
                                                                                                                                                                             
        print("{}, {}, {}".format(current_temp, current_heatIndex, current_windChill))                                                                                       
                                                                                                                                                                             
        apparentTemp = calculateApparent(current_temp, current_heatIndex, current_windChill)                                                                                 
                                                                                                                                                                             
        print("Apparent temp = {}".format(apparentTemp))                                                                                                                     
                                                                                                                                                                             
                                                                                                                                                                             
loop = asyncio.get_event_loop()                                                                                                                                              
loop.run_until_complete(example())
