import cv2
import numpy	
from matplotlib import pyplot as plt

import zeep
from onvif import ONVIFCamera, ONVIFService
def zeep_pythonvalue(self, xmlvalue):      
    return xmlvalue
zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue


from onvif import ONVIFCamera
cam_42 = ONVIFCamera('192.168.15.42', 80, 'admin','Supervisor')
mycam43 = ONVIFCamera('192.168.15.43', 80, 'admin','Supervisor')

#catching stream
stream_42=cv2.VideoCapture('rtsp://192.168.15.42:554')
stream_43=cv2.VideoCapture('rtsp://192.168.15.43:554')  

#creating histogogram
#42
fig=plt.figure(figsize=(4, 2))
color = ('b','g','r')
ret,frame_42=stream_42.read()
hsv = cv2.cvtColor(frame_42,cv2.COLOR_BGR2HSV)
histog = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(4, 2, 1)
plt.imshow(histog,interpolation = 'nearest')

fig.add_subplot(4, 2, 2)
for i,col in enumerate(color): #each value corresponds to number of pixels in that imaging with its corresponding pixel value RGB
    histogr = cv2.calcHist([frame_42],[i],None,[256],[0,256])
    plt.plot(histogr,color = col)
    plt.xlim([0,256])
    
#creating graph for 43 camera
ret,frame_43=stream_43.read()
hsv = cv2.cvtColor(frame_43,cv2.COLOR_BGR2HSV)
histog = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(4, 2, 3)
plt.imshow(histog,interpolation = 'nearest')
    
fig.add_subplot(4, 2, 4)
for i,col in enumerate(color): #each value corresponds to number of pixels in that imaging with its corresponding pixel value RGB
    histogr = cv2.calcHist([frame_43],[i],None,[256],[0,256])
    plt.plot(histogr,color = col)
    plt.xlim([0,256])    

media42 = cam_42.create_media_service()
media_profile42 = media42.GetProfiles()[0]
imaging42 = cam_42.create_imaging_service()
token42 = media_profile42.VideoSourceConfiguration.SourceToken
SY42 = imaging42.create_type('GetImagingSettings')
SY42.VideoSourceToken = token42
request42 = imaging42.GetImagingSettings(SY42)
print(request42)

media43 = mycam43.create_media_service()
media_profile43 = media43.GetProfiles()[0]
imaging43 = mycam43.create_imaging_service()
token43 = media_profile43.VideoSourceConfiguration.SourceToken
SY43 = imaging43.create_type('GetImagingSettings')
SY43.VideoSourceToken = token43
request43 = imaging43.GetImagingSettings(SY43)
print(request43)

#Adjusting
b42=request42.Brightness
if b42 <48.0:
    while b42 < 48.0:
        imaging42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness + 1.0
        b42 = b42+1.0
if b42 > 50.0:
    while b42 > 50.0:
        imaging42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness - 1.0
        b42 = b42 - 1.0
        
b43=request43.Brightness
if b43 <48.0:
    while b43 < 48.0:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Brightness = request43.Brightness + 1.0
        b43 = b43+1.0
if b43 > 50.0:
    while b43 > 50.0:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Brightness = request43.Brightness - 1.0
        b43 = b43 - 1.0

s42=request42.ColorSaturation

if s42 <59.0:
    while s42 <59.0:
        imaging42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation + 1.0
        s42 = s42+1.0
if s42 > 61.0:
    while s42 > 61.0:
        imaging42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation - 1.0
        s42 = s42 - 1.0
        
s43=request43.ColorSaturation
if s43 <59.0:
    while s43 <59.0:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.ColorSaturation = request43.ColorSaturation + 1.0
        s43 = s43+1.0
if s43 > 61.0:
    while s43 > 61.0:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.ColorSaturation = request43.ColorSaturation - 1.0
        s43 = s43 - 1.0
cr43 = request43.WhiteBalance.CrGain
cb43 = request43.WhiteBalance.CbGain   

if cr43 >= 1.0:
    while cr43 >=1.0: 
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.request43.WhiteBalance.CrGain = request43.request43.WhiteBalance.CrGain - 1.0
        print(request43.WhiteBalance.CrGain)
        cr43 = cr43 - 1.0
        cr43=request43.WhiteBalance.CrGain
        
if cb43 <126.5:
    while cb43 <126.5:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.WhiteBalance.CbGain = request43.WhiteBalance.CbGain + 1.0
        print(request43.WhiteBalance.CbGain)
        cb43 = cb43+1.0
if cb43 >127.5:
    while cb43 > 127.5:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.WhiteBalance.CbGain = request43.WhiteBalance.CbGain - 1.0
        print(request43.WhiteBalance.CbGain)
        cb43 = cb43 - 1.0 
contr42=request42.Contrast

if contr42 <49.0:
    while contr42 <49.0:
        imaging42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast + 1.0
        contr42 = contr42+1.0
if contr42 > 51.0:
    while contr42 > 51.0:
        imaging42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast - 1.0
        contr42 = contr42 - 1.0
contr43=request43.Contrast
if contr43 <49.0:
    while s43 <49.0:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Contrast = request43.Contrast + 1.0
        contr43 = contr43+1.0
if contr43 > 51.0:
    while contr43 > 51.0:
        imaging43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Contrast = request43.Contrast - 1.0
        contr43 = contr43 - 1.0

#catching streams
stream_42=cv2.VideoCapture('rtsp://192.168.15.42:554')
stream_43=cv2.VideoCapture('rtsp://192.168.15.43:554') 

#creating histogogram
#42
ret,frame_42=stream_42.read()
hsv = cv2.cvtColor(frame_42,cv2.COLOR_BGR2HSV)
histog = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(4, 2, 5)
plt.imshow(histog,interpolation = 'nearest')

fig.add_subplot(4, 2, 6)
for i,col in enumerate(color): #each value corresponds to number of pixels in that imaging with its corresponding pixel value RGB
    histogr = cv2.calcHist([frame_42],[i],None,[256],[0,256])
    plt.plot(histogr,color = col)
    plt.xlim([0,256])
    
#creating histogogram
#43
ret,frame_43=stream_43.read()
hsv = cv2.cvtColor(frame_43,cv2.COLOR_BGR2HSV)
histog = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(4, 2, 7)
plt.imshow(histog,interpolation = 'nearest')
    
fig.add_subplot(4, 2, 8)
for i,col in enumerate(color): #each value corresponds to number of pixels in that imaging with its corresponding pixel value RGB
    histogr = cv2.calcHist([frame_43],[i],None,[256],[0,256])
    plt.plot(histogr,color = col)
    plt.xlim([0,256])    
plt.show()
