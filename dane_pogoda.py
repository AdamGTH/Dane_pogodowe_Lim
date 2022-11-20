import requests

lim_r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=49.7149918&lon=20.423074222125905&appid=90ceaeb4099970526efcc36abcb20e00")

data = lim_r.json()
weath_lim = {'Temperature':'', "Feels like":'', "Temperature min":'', "Temperature max":'',"Pressure":'',"Humidity":''}
list_keys = [x for x in weath_lim]
weath_lim_num = data["main"]

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
    

    
#print(weath_lim)
    


