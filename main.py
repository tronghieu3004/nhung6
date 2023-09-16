from machine import Pin
from time import sleep


# count
count = 0
time = 9
isCountdown = False
# màn led 7 đoạn  
displayledList = [None]*8
displayledList[0] = Pin(2,Pin.OUT)
displayledList[1] = Pin(4,Pin.OUT)
displayledList[2] = Pin(5,Pin.OUT)
displayledList[3] = Pin(15,Pin.OUT)
displayledList[4] = Pin(18,Pin.OUT)
displayledList[5] = Pin(19,Pin.OUT)
displayledList[6] = Pin(21,Pin.OUT)


# button 
butn_mode = Pin(34,Pin.IN,Pin.PULL_UP)
butn_start = Pin(35,Pin.IN,Pin.PULL_UP)
# led
ledList = [None]*5
ledList[0] = Pin(13, Pin.OUT)
ledList[1] = Pin(12, Pin.OUT)
ledList[2] = Pin(14, Pin.OUT)
ledList[3] = Pin(27, Pin.OUT)

#Control led
posList = [0x08,0x04,0x02,0x01]
def display_led(number):#hiển thị led
   for i in range(4):
      x = (number >> i)%2
      ledList[3-i].value(x)

# Control display
numberList = [0x01,0x4F,0x12,0x06,0x4C,0x24,0x20,0x0F,0x00,0x04]
def display_number(number):#hiển thị từng số 0 - 10
   for i in range(7):
      x = (number >> i)%2
      displayledList[6-i].value(x)

def led(number):
  posit = number % 4 - 1
  display_led(posList[posit])

def display(dem):
  global time
  mode = dem % 4 
  if(mode == 1):time = 9
  elif(mode == 2):time = 6
  elif(mode == 3):time = 4
  else:time = 4
  display_number(numberList[time])


def selectMode():
  global count
  while butn_mode.value() == 0:
    if (butn_mode.value()):# khi chọn chế độ
      sleep(0.01)
      count = count + 1
      print("select mode: ", count%4)
    else:
        pass
def push_btn():
  butn_mode.value(not butn_mode.value())

def countdown(start):
  for i in range (start + 1):
    display_number(numberList[start - i])
    sleep(1)

def main():
  global isCountdown
  while butn_start.value() == 0: # chặn nút start bị nhấn giữ 
    selectMode()
    if (butn_start.value()): #khi chọn start
      sleep(0.01)
      isCountdown = True
      print("counting....")
      countdown(time)
    else:
      pass
    led(count)
    display(count)

while True:
  main()
  


  
  


   


    
  

  
  