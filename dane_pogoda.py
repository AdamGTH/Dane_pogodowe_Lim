import requests

lim_r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=49.7149918&lon=20.423074222125905&appid=90ceaeb4099970526efcc36abcb20e00")

data = lim_r.json()
weath_lim = {'Temperature':'', "Feels like":'', "Temperature min":'', "Temperature max":'',"Pressure":'',"Humidity":''}
list_keys = [x for x in weath_lim]
weath_lim_num = data["main"]
dt_time_info = data["dt"]
sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]

######################## wyciąganie danych pogodowych#################################
for idx, x in enumerate(weath_lim_num):
    if idx == 0 or idx == 1 or idx == 2 or idx == 3:
        weath_lim_num[x] = round(weath_lim_num[x]-272.15, 1 )
  
 
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
dd_mm_rrrr = ''
year = dt_time_info/31556926 + 1970
month = (year-int(year)) * 12
day_in_month = {'Jan':31, 'Feb':[28,29], 'march':31, 'april':30, 'May':31, 'June':30,'July':31, 'August':31, 'Sept':30,'Oct':30, 'Nov':30, 'Dec':31}
month_actual = ''
month_number = 0

for idx, x in enumerate(day_in_month):
    if idx+1 < month:
        continue
    else:
        month_actual = x
        month_number = idx+1
        break
    
day = (month-int(month))*day_in_month[month_actual]

for x in range(1, day_in_month[month_actual]):
    if x < day:
        continue
    else:
        day = x
        break

dd_mm_rrrr = str(day)+"-"+str(month_number)+"-"+str(int(year))

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
