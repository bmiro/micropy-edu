import network
import ubinascii
import ujson
import urequests

from time import sleep


WIFI_SSID = 'CanMirany'
WIFI_PASSWORD = 'ona transparent'

SERVER_DATA_URL = "http://192.168.17.235:8080/esp32-data"
SLEEP_TIME = 120


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.scan()
for net in wifi.scan():
    print("SSID: {} Signal: {}".format(net[0], net[3]))

wifi.connect(WIFI_SSID, WIFI_PASSWORD)


while True:

    mac = ubinascii.hexlify(wifi.config('mac'), ':')

    fahrenheit_temp = esp32.raw_temperature()
    celcius_temp = (fahrenheit_temp-32)/1.8

    data_to_send = {
       'mac': mac,
       'essid': wifi.config('essid'),
       'signal': wifi.status('rssi'),
       'ip': wifi.ifconfig()[0],
       'internal_temp': celcius_temp,
       'internal_hall': esp32.hall_sensor(),
    }
    response = urequests.post(
        SERVER_DATA_URL,
        headers={'content-type': 'application/json'},
        data=ujson.dumps(data_to_send),
    )
    sleep(10)
