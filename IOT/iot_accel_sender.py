from SF_9DOF import IMU 
import requests
import json 
#create IMU object 
imu = IMU()

#Initialize IMU
imu.initialize()

imu.enable_accel()

imu.read_accel()
accel_data = imu.ax
print str(accel_data)
print "accel data"
payload  = {'firstName':'Kehlin',
                'lastName':'Sizzaaane',
                'accelData':str(accel_data)}

r=requests.post('https://contact-list-kehlin.herokuapp.com/contacts',json=payload)

