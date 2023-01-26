import urllib.request,urllib.parse,urllib.error
import json


serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("enter Location")
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({"address": address})

    print("Retrieving",url)
    urlopen = urllib.request.urlopen(url)
    data = urlopen.read().decode
    # print("Retrieving",len(data), "charactors")

    try:
        data = json.loads(data)
    except:
        data = None

    if not data or "status" not  in data or data["status"] != "OK":
        print("================================FAILED================================")
        print(data)
        continue

    print(json.dumps(data, indent=4))

    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]
    print("lat",lat)
    print("lng",lng)
    location = data["results"][0]["formatted address"]
    print("location",location)
