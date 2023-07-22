import serial

def scanports():

    ports =[]
    found = []

    for x in range(1,255): ports.append('COM'+str(x))

    for port in ports:
        try:
            ser=serial.Serial(port)
            ser.close()
            found.append(port)
        except (OSError, serial.SerialException):
            pass

    print('запущена scanports()')
    print(f'найдено: {found} ')
    return found