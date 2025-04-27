import RPi.GPIO as GPIO
import time

# Defining pins for the motors, and the start/stop button
# IN1 forward, IN2, backward
IN1 = 23
IN2 = 24
SERVO = 14
BUTTON = 9

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(SERVO, GPIO.OUT)

# Initialize the steering servo
pwm = GPIO.PWM(SERVO, 50) 
p.start(0)

def start():
    # Here will go the automatic driving code
    pass

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    pass

# Main loop: button interaction
try:
    while True:
       if GPIO.input(BUTTON) == GPIO.HIGH:
           start()
           while GPIO.input(BUTTON) == GPIO.HIGH:  
               time.sleep(0.1)
       else:
           stop()
       time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()