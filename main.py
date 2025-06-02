import machine
import utime
from myneopixel import Neopixel

buzzer_pin = machine.Pin(16)
buzzer = machine.PWM(buzzer_pin)

pixels = Neopixel(15, 0, 17)
pixels.brightness(100)

RED = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (255, 0, 0)
ORANGE = (60, 255, 0)
PURPLE = (0, 220, 220)
PINK = (80, 255, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def turn_off_all_pixels():
    pixels.fill(BLACK)
    pixels.show()

def light_color(color):
    pixels.fill(color)
    pixels.show()

volume = 30000

def play_tone(frequency, duration, duty=volume):
    """
    Play a single tone at the given frequency for the given duration (in seconds).
    """
    buzzer.freq(frequency)
    buzzer.duty_u16(duty)
    utime.sleep(duration)
    
    buzzer.duty_u16(0)
    utime.sleep(0.05)

def play_red():
    """
    RED (#FF0000): Ultra-C-centric bell fanfare—
    constant C pulses, octave jumps, and a final triple-C flourish.
    """
    light_color(RED)

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

    turn_off_all_pixels()

def play_blue():
    """
    BLUE (#0000FF): Gentle surf built on D—
    slow rocking between D3, D4, and D5 with soft fifths (A) to add depth.
    """
    light_color(BLUE)

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

    turn_off_all_pixels()

def play_yellow():
    """
    YELLOW (#FFFF00)
    Ultra-E birdsong: rapid E pulses, octave-jump trills, and one
    bright E6 flash for a burst-of-sun effect.
    """
    light_color(YELLOW)

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

    turn_off_all_pixels()

def play_green():
    """
    GREEN (#00FF00): Harmonious and calming F (lower octave).
    Melodic tones with a deeper, slower, and more soothing sound to represent balance and nature.
    """
    light_color(GREEN)

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

    turn_off_all_pixels()

def play_orange():
    """
    ORANGE (#FFA500): Bright and energetic A note.
    A dynamic melody that combines the sharpness of red and the brightness of yellow,
    creating a lively and energetic sound to represent creativity and vibrance.
    """
    light_color(ORANGE)

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

    turn_off_all_pixels()

def play_purple():
    """
    PURPLE (#800080): Mysterious and royal G note.
    A melody that combines deep bass and high treble to create a mystical atmosphere.
    """
    light_color(PURPLE)

    melody = [
        196, 196, 196, 196, 196, 196, 196, 196, 196,
        247, 196, 392, 247, 196, 392,
        196, 220, 196, 220, 196, 196,
        392, 392, 247, 220, 247, 196,
        196, 392, 196, 392, 196, 196,
        220, 247, 392, 247, 220, 196
    ]
    
    durations = [
        0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
        0.30, 0.30, 0.30, 0.30, 0.30, 0.30,
        0.25, 0.30, 0.25, 0.30, 0.30, 0.30,
        0.25, 0.30, 0.30, 0.30, 0.30, 0.30,
        0.25, 0.25, 0.30, 0.30, 0.30, 0.30,
        0.25, 0.25, 0.25, 0.30
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    turn_off_all_pixels()

def play_pink():
    """
    PINK (#FFC0CB): Sweet and playful B note.
    A cheerful, light melody that represents joy and playfulness.
    """
    light_color(PINK)

    melody = [
        494, 494, 494, 494, 494, 494, 494, 494, 494,
        587, 494, 740, 587, 494, 740,
        494, 554, 494, 554, 494, 494,
        740, 740, 587, 554, 587, 494,
        494, 740, 494, 740, 494, 494,
        554, 587, 740, 587, 554, 494
    ]
    
    durations = [
        0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
        0.18, 0.18, 0.18, 0.18, 0.18, 0.18,
        0.15, 0.18, 0.15, 0.18, 0.18, 0.18,
        0.15, 0.18, 0.18, 0.18, 0.18, 0.18,
        0.15, 0.15, 0.18, 0.18, 0.18, 0.18,
        0.15, 0.15, 0.15, 0.18
    ]

    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)

    turn_off_all_pixels()

def play_black():
    """
    BLACK (#000000): Cozy nighttime with gentle 'heartbeat' and 'cricket chirp.'
    Darker and slower than before, evoking a deep, tranquil nighttime atmosphere.
    """
    light_color(BLACK)  

    for _ in range(5):
        play_tone(110, 0.4)  
        utime.sleep(0.4)    
        play_tone(1000, 0.1) 
        utime.sleep(0.5)     

    final_chirps = [1300, 1100, 1200] 
    for freq in final_chirps:
        play_tone(freq, 0.1) 
        utime.sleep(0.6)      

    turn_off_all_pixels()

def play_white():
    """
    WHITE (#FFFFFF): Bright, pure, and harmonious.
    A high-pitched, serene melody representing clarity, elegance, and simplicity.
    """
    light_color(WHITE)

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

    turn_off_all_pixels()

while True:
    turn_off_all_pixels()
    
    print("RED")
    play_red()
    utime.sleep(1)
    
    print("BLUE")
    play_blue()
    utime.sleep(1)
    
    print("YELLOW")
    play_yellow()
    utime.sleep(1)
    
    print("GREEN")
    play_green()
    utime.sleep(1)
    
    print("ORANGE")
    play_orange()
    utime.sleep(1)
    
    print("PURPLE")
    play_purple()
    utime.sleep(1)
    
    print("PINK") 
    play_pink()
    utime.sleep(1)
    
    print("BLACK")
    play_black()
    utime.sleep(1)
    
    print("WHITE")
    play_white()
    utime.sleep(3)