# Resum

Projecte educacional per mostrar funcionament de microcontroladors.

El fitxer `u.py` conté el codi micropython per la ESP32 que envia dades de mesura per HTTP
a l' `api.py`.

# Preparació ESP32 amb MicroPython

    wget http://micropython.org/resources/firmware/esp32-idf3-20210202-v1.14.bin
    esptool --chip esp32 --port /dev/ttyUSB0 erase_flash
    esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20210202-v1.14.bin

# Connectar-se al MicroPython de manera interactiva

    apt install picocom
    picocom /dev/ttyUSB0 -b115200

Exit with `Control a x`

# Configurar programa .py
TODO

# Carregar programa .py a la ESP32
TODO

# Execució API Flask per rebre dades

    apt install python3-flask
    FLASK_APP=api.py python3 -m flask run --host=0.0.0.0 --port=8080

# Provat l'api amb un POST sintètic

    curl -H "Content-Type: application/json" --data '{"test": "data"}' http://127.0.0.1:8080
