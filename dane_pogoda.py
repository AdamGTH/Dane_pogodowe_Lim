import requests

lim_r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=49.7149918&lon=20.423074222125905&appid=90ceaeb4099970526efcc36abcb20e00")

data = lim_r.json()

weath_lim = data["main"]

for idx, x in enumerate(weath_lim):
    if idx == 0 or idx == 1 or idx == 2 or idx == 3:
        weath_lim[x] = round(weath_lim[x]-272.15, 1 )
    
    
# trzeba będzie zamienić dane na string i dodać jednostki 
    
print(weath_lim)
    


