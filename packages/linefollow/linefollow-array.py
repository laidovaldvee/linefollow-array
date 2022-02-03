from smbus2 import SMBus

busno = 12 #/dev/i2c-12
addr = 62 #0x3e
reg = 17 #0x11

bus = SMBus(busno)
while True:
	b = bus.read_byte_data(addr,reg)
	print(b)

bus.close()
