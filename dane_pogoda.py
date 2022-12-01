import requests

lim_r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Limanowa&appid=2dfa06232a76a512303f51ae8a5af464&units=metric")

data = lim_r.json()
weath_lim = {'Temperature':'', "Feels like":'', "Temperature min":'', "Temperature max":'',"Pressure":'',"Humidity":''}
list_keys = [x for x in weath_lim]
weath_lim_num = data["main"]
dt_time_info = data["dt"]
sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]

######################## wyciąganie danych pogodowych#################################
#for idx, x in enumerate(weath_lim_num):
 #   if idx == 0 or idx == 1 or idx == 2 or idx == 3:
  #      weath_lim_num[x] = round(weath_lim_num[x]-272.15, 1 )
  
 
# zamiana na string + dodanie jednostek
for idx, num in enumerate(weath_lim_num):
    if idx == 6 or idx == 7:
        break
    weath_lim[list_keys[idx]]= str(weath_lim_num[num])
    if idx == 0 or idx == 1 or idx == 2 or idx == 3:
        weath_lim[list_keys[idx]] = weath_lim[list_keys[idx]] + " *C"
    if idx == 4:
        weath_lim[list_keys[idx]] = weath_lim[list_keys[idx]] + " hPa"      
    if idx == 5:
        weath_lim[list_keys[idx]] = weath_lim[list_keys[idx]] + " %"     
    

######################################################################################
##################### wyciąganie daty i czasu ########################################
from datetime import date, datetime

dd_mm_rrrr = date.today()

currentDateAndTime = datetime.now()

#print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383
#currentTime = currentDateAndTime.strftime("%H:%M:%S")
#print("The current time is", currentTime)
# The current time is 10:06:55

######################################################################################
##################### obliczanie wschodu i zachodu słonca z czasu unixowego ##########
# second in day = 86400
# second in hour = 3600

time_sunrise_hour = ((sunrise-(int(sunrise/86400)*86400))/3600)+1
time_sunrise_min = int((time_sunrise_hour - int(time_sunrise_hour))*60)
time_sunrise_hour = int(time_sunrise_hour)

time_sunset_hour = ((sunset-(int(sunset/86400)*86400))/3600)+1
time_sunset_min = int((time_sunset_hour - int(time_sunset_hour))*60)
time_sunset_hour = int(time_sunset_hour)

time_sunrise = '{:02d}:{:02d}'.format(time_sunrise_hour, time_sunrise_min)
time_sunset = '{:02d}:{:02d}'.format(time_sunset_hour, time_sunset_min)

#################################################################################

