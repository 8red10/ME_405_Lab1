'''!
@file led.py
This file contains code for a brightness-changing LED using PWM.

@author Jack Krammer and Jason Chang
@date   6-Feb-2024
@copyright (c) 2024 by mecha04 and released under MIT License
'''

import pyb
import utime

def led_setup():
    '''!
    Initializes an active low 1000Hz PWM timer channel on pin PA0 where the LED is connected.
    @param      None.
    @returns    The TimerChannel object that is initialized as a PWM.
    '''
    # set PA0 to output
    pa0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    # set up timer 2 channel 1 for PWM
    tim2 = pyb.Timer(2, freq=1000)
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pa0)
    # return the channel
    return ch1

def led_brightness(channel, duty):
    '''!
    Sets the duty cycle of the PWM on the input channel to the input level. If the input duty cycle is less than 0,
    the duty cycle is set to 0. If the input duty cycle is greater than 100, the duty cycle is set to 100.
    @param      channel -> A TimerChannel object to set the duty cycle on.
    @param      duty    -> The duty cycle to set the PWM to.
    @returns    None.
    '''
    # check that the input duty cycle is within range
    if duty < 0:
        duty = 0
    elif duty > 100:
        duty = 100
    # set the duty cycle
    channel.pulse_width_percent(duty)
    print(f'changing duty to "{duty}%"')
    
def main():
    '''!
    Sets up a PWM output on pin PA0 where the LED is and ramps the duty cycle 
    from 0 to 100 over a 5 second period (in 50 millisecond increments). Loops 
    this behavior forever. This main code is run if this file is the main 
    program but won't run if this file is imported as a module by some other program.
    @param      None.
    @returns    None.
    '''
    # initialize the duty cycle variable
    duty = 0
    # set up the LED and PWM
    chan = led_setup()
    # loop forever
    while True:
        # set the duty cycle for the led
        led_brightness(chan, duty)
        # wait 50 milliseconds
        utime.sleep_ms(50)
        # update the duty cycle
        duty += 1
        duty %= 101

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == '__main__':
    main()
    
    