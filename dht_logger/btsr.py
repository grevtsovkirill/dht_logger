import time
import serial
          
sens='DTH11'
measurement_dict = {'Temperature':'T_liv','Humidity':'H_liv'}
read_types = ['Temperature','Humidity']

ser = serial.Serial(
    
    port='/dev/rfcomm0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


#     #b'Humidity = 23.00\r\n'
#     #b'Temperature = 16.00\r\n'

def get_sp_data(read_type):
    #x=''
    while 1:
        x=str(ser.readline())
        if read_type in x:
            y = x.find(read_type)+len(read_type)+3
            z=x[y:y+5]
            #print(z)
            return z
            break

def get_bt_reading(read_type):
    return sens,measurement_dict[read_type],get_sp_data(read_type)

def main():
    #meas = get_sp_data()
    for i in read_types:
        print(i)
        #get_sp_data(i)
        print(get_bt_reading(i))

if __name__== "__main__":
  main()    
