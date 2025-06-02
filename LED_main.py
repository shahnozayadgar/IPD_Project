import machine
import utime

# Change GPIO if the Pin is different.
buzzer_pin = machine.Pin(16)
buzzer = machine.PWM(buzzer_pin)

#LED GPIO Pins
led_red = machine.Pin(15, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)
led_yellow = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(12, machine.Pin.OUT)
led_orange = machine.Pin(11, machine.Pin.OUT)
led_purple = machine.Pin(10, machine.Pin.OUT)
led_pink = machine.Pin(9, machine.Pin.OUT)
led_black = machine.Pin(8, machine.Pin.OUT)
led_white = machine.Pin(7, machine.Pin.OUT)

#helper function to turn off all LEDs before/after playing a color melody
def turn_off_all_leds():
    led_red.off()
    led_blue.off()
    led_yellow.off()
    led_green.off()
    led_orange.off()
    led_purple.off()
    led_pink.off()
    led_black.off()
    led_white.off()



# we can adjust to make the sound louder or softer
volume = 30000

def play_tone(frequency, duration, duty=volume):
    """
    Play a single tone at the given frequency for the given duration (in seconds).
    """
    buzzer.freq(frequency)
    buzzer.duty_u16(duty)
    utime.sleep(duration)

    # mute between the notes to make it sound smooth
    buzzer.duty_u16(0)
    utime.sleep(0.05)



# C is always RED
def play_red():
    """
    RED (#FF0000): Ultra-C-centric bell fanfare—
    constant C pulses, octave jumps, and a final triple-C flourish.
    """
    led_red.on()

    melody = [
        262, 262, 262,         
        330, 262,               
        392, 262,               

        262, 330, 392, 523,     
        392, 330, 262,         

        262, 523, 262, 523, 262,

        262, 330, 392, 523, 784, 523, 523, 523 
    ]
    durations = [
        0.08, 0.08, 0.12,
        0.10, 0.12,
        0.10, 0.14,

        0.10, 0.10, 0.10, 0.15,
        0.10, 0.10, 0.14,

        0.08, 0.08, 0.08, 0.08, 0.12,

        0.08, 0.08, 0.08, 0.12, 0.15, 0.10, 0.10, 0.25
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    led_red.off()


# D is always BLUE
def play_blue():
    """
    BLUE (#0000FF): Gentle surf built on D—
    slow rocking between D3, D4, and D5 with soft fifths (A) to add depth.
    """
    led_blue.on()

    melody = [
        147,  294,  220,  294,  588,  440,  294, 147,
        147,  294,  220,  294,  588,  440,  294, 147,
        147,  220,  294,  220,  147            
    ]
    durations = [
        0.50, 0.50, 0.50, 0.50, 0.60, 0.50, 0.50, 0.60,
        0.50, 0.50, 0.50, 0.50, 0.60, 0.50, 0.50, 0.60,
        0.55, 0.55, 0.70, 0.55, 0.80            
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    led_blue.off()

# E is always YELLOW
def play_yellow():
    """
    YELLOW (#FFFF00)
    Ultra-E birdsong: rapid E pulses, octave-jump trills, and one
    bright E6 flash for a burst-of-sun effect.
    """
    led_yellow.on()

    melody = [
        330, 330, 330,                            
        370, 415, 370, 330,                             
        330, 660, 1320, 660, 330,                        
        415, 494, 554, 494, 415, 370, 330,               
        330, 660, 330, 660, 330                        
    ]

    durations = [
        0.06, 0.06, 0.10,
        0.08, 0.08, 0.08, 0.12,
        0.06, 0.10, 0.12, 0.10, 0.08,
        0.08, 0.08, 0.10, 0.08, 0.08, 0.08, 0.12,
        0.06, 0.10, 0.06, 0.10, 0.18
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    led_yellow.off()


# F is always GREEN
def play_green():
    """
    GREEN (#00FF00): Harmonious and calming F (lower octave).
    Melodic tones with a deeper, slower, and more soothing sound to represent balance and nature.
    """
    led_green.on()

    melody = [
        174, 174, 174, 174, 174, 174, 174, 174, 174, 
        220, 174, 293, 220, 174, 293, 
        174, 196, 174, 196, 174, 174,  
        293, 293, 220, 196, 220, 174,  
        174, 293, 174, 293, 174, 174, 
        196, 220, 293, 220, 196, 174   
    ]
    
    durations = [
        0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 
        0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 
        0.30, 0.35, 0.30, 0.35, 0.35, 0.35,  
        0.30, 0.35, 0.35, 0.35, 0.35, 0.35,  
        0.30, 0.30, 0.35, 0.35, 0.35, 0.35, 
        0.30, 0.30, 0.30, 0.35           
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    led_green.off()

def play_orange():
    """
    ORANGE (#FFA500): Bright and energetic A note.
    A dynamic melody that combines the sharpness of red and the brightness of yellow,
    creating a lively and energetic sound to represent creativity and vibrance.
    """
    led_orange.on()

    melody = [
        440, 440, 440, 440, 440, 440, 440, 440, 440,  
        523, 440, 659, 523, 440, 659,  
        440, 493, 440, 493, 440, 440, 
        659, 659, 523, 493, 523, 440,  
        440, 659, 440, 659, 440, 440, 
        493, 523, 659, 523, 493, 440  
    ]
    
    durations = [
        0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08,  
        0.10, 0.10, 0.10, 0.10, 0.10, 0.10,  
        0.08, 0.10, 0.08, 0.10, 0.10, 0.10, 
        0.08, 0.10, 0.10, 0.10, 0.10, 0.10, 
        0.08, 0.08, 0.10, 0.10, 0.10, 0.10,  
        0.08, 0.08, 0.08, 0.10           
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    led_orange.off()


def play_black():
    """
    BLACK (#000000): Cozy nighttime with gentle 'heartbeat' and 'cricket chirp.'
    Darker and slower than before, evoking a deep, tranquil nighttime atmosphere.
    """
    # LED on
    led_black.on()

    for _ in range(5):
        play_tone(110, 0.4)  
        utime.sleep(0.4)    
        play_tone(1000, 0.1) 
        utime.sleep(0.5)     

    final_chirps = [1300, 1100, 1200] 
    for freq in final_chirps:
        play_tone(freq, 0.1) 
        utime.sleep(0.6)      

    # LED off
    led_black.off()


def play_white():
    """
    WHITE (#FFFFFF): Bright, pure, and harmonious.
    A high-pitched, serene melody representing clarity, elegance, and simplicity.
    """
    led_white.on()

    melody = [
        523, 587, 659, 587, 523, 
        659, 587, 523, 659, 523, 
        587, 523, 659, 587, 523   
    ]
    
    durations = [
        0.2, 0.2, 0.2, 0.2, 0.2,  
        0.2, 0.2, 0.2, 0.2, 0.2,  
        0.2, 0.2, 0.2, 0.2, 0.2   
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    led_white.off()








#Todo: Implement NFC tag to distinguish each color
while True:

    # Turn off all LEDs before playing a new color
    turn_off_all_leds()

    
    # print("RED")
    # play_red()
    # utime.sleep(1)
    
    # print("BLUE")
    # play_blue()
    # utime.sleep(1)
    
    # print("YELLOW")
    # play_yellow()
    # utime.sleep(1)
    
    # print("GREEN")
    # play_green()
    # utime.sleep(1)
    
    # print("ORANGE")
    # play_orange()
    # utime.sleep(1)
    
    # print("PURPLE")
    # play_purple()
    # utime.sleep(1)
    
    # print("PINK") 
    # play_pink()
    # utime.sleep(1)
    
    # print("BLACK")
    # play_black()
    # utime.sleep(1)
    
    print("WHITE")
    play_white()
    utime.sleep(3)
