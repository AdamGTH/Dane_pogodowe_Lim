import requests

lim_r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=49.7149918&lon=20.423074222125905&appid=90ceaeb4099970526efcc36abcb20e00")

data = lim_r.json()

temp_lim = data["main"]

