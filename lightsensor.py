import smbus
import time
DEVICE = 0x23
RES = 0x20
bus = smbus.SMBus(1)

while True:
    
    data = bus.read_i2c_block_data(DEVICE, RES)
    data = int((data[0] << 8) + data[1])
    
    if data > 1000:
        level = 'too bright'
    elif data <= 1000 and data > 500:
        level = 'bright'
    elif data <= 500 and data > 200:
        level = 'medium'
    elif data <= 200 and data > 50:
        level = 'dark'
    else:
        level = 'too dark'
    print(data)
    print(level)
    time.sleep(1.5)