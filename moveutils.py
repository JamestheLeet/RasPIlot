from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40, debug=True)
motorpin = 15 #The pin that the ESC is connected to
steeringpin = 14 #The pin that the servo  is connected to

def setServoPulse(channel, pulse):
  pulseLength = 1000000
  pulseLength /= 60
  print "%d us per period" % pulseLength
  pulseLength /= 4096
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)
def setthrottle(throttle):
  actthrottle = ((1+((50+(throttle/2))*.01))/6)*4096
  pwm.setPWM(motorpin, 0, actthrottle)
  
def setsteering(angle):
  actangle = ((1+((90+angle)/180))/6)*4096
  pwm.setPWM(steeringpin, 0, actangle)