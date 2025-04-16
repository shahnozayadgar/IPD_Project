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

def play_red():
    """
    RED (#FF0000): Joyful, bright, energetic “bell chimes.”
    """

    # LED on
    led_red.on()

    melody = [
        1000, 1200, 1400, 1600,  # up
        1400, 1200, 1000,        # down
        1000, 1200, 1400, 1600,  # up
        1800, 2000, 2200         # upup
    ]
    durations = [
        0.15, 0.15, 0.15, 0.15,  # up
        0.15, 0.15, 0.15,        # down
        0.15, 0.15, 0.15, 0.15,  # up
        0.2, 0.2, 0.3            # upup (longer)
    ]
    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)
    
    # LED off
    led_red.off()

def play_blue():
    """
    BLUE (#0000FF): Calm “ocean wave” pattern at a lower pitch.
    """
    # LED on
    led_blue.on()

    wave_sequence = [
        (200, 0.3), (250, 0.3), (300, 0.3), (350, 0.3),
        (300, 0.3), (250, 0.3), (200, 0.3)
    ]

    for _ in range(2):
        for freq, dur in wave_sequence:
            play_tone(freq, dur)
    
    # LED off
    led_blue.off()

def play_yellow():
    """
    YELLOW (#FFFF00): Bright, happy “bird chirps.”
    """
    # LED on
    led_yellow.on()

    melody = [
        1500, 1800, 1500, 1800,  
        2000, 1700, 2000,        # up-down
        1500, 1800, 1500, 1800,  # up-down
        2000, 2200, 2000         # last chirps
    ]
    
    durations = [
        0.08, 0.08, 0.08, 0.08,
        0.1, 0.1, 0.1,
        0.08, 0.08, 0.08, 0.08,
        0.1, 0.1, 0.15
    ]
    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)
    
    # LED off
    led_yellow.off()

def play_green():
    """
    GREEN (#008000): Natural, friendly frog-like or leaf-rustling feel.
    """
    # LED on
    led_green.on()

    sequence_one = [
        (400, 0.2), (450, 0.2), (400, 0.2), (350, 0.2)
    ]
    sequence_two = [
        (300, 0.2), (350, 0.2), (400, 0.2), (350, 0.2)
    ]
    # play it twice 
    for _ in range(2):
        for freq, dur in sequence_one:
            play_tone(freq, dur)
    for _ in range(2):
        for freq, dur in sequence_two:
            play_tone(freq, dur)
    
    # LED off
    led_green.off()

def play_orange():
    """
    ORANGE (#FFA500): Warm, energetic trumpet or fanfare style.
    """
    # LED on
    led_orange.on()

    fanfare = [
        (800, 0.15), (1200, 0.15), (1000, 0.15),
        (1300, 0.15), (1100, 0.15)
    ]
    flourish = [
        (1400, 0.2), (1600, 0.2), (1800, 0.3)
    ]
    
    for _ in range(2):
        for freq, dur in fanfare:
            play_tone(freq, dur)
    # end with flourish
    for freq, dur in flourish:
        play_tone(freq, dur)
    
    # LED off
    led_orange.off()
    
def play_purple():
    """
    PURPLE (#800080): Magical sparkle or whimsical notes (mysterious, imaginative).
    """
    # LED on
    led_purple.on()

    melody = [
        1200, 1400, 1600, 1800,  # up
        1600, 1400, 1200,        # down
        1400, 1600, 1800, 2000,  # up
        1800, 1600, 2200         #  flourish
    ]
    durations = [
        0.15, 0.15, 0.15, 0.15,  # up
        0.15, 0.15, 0.15,        # down
        0.15, 0.15, 0.15, 0.15,  # up
        0.2, 0.2, 0.3            #  flourish
    ]
    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)
    
    # LED off
    led_purple.off()

def play_pink():
    """
    PINK (#FFC0CB): Light-hearted 'bubble-popping' or gentle bell sounds.
    """
    # LED on
    led_pink.on()

    melody = [
        1500, 1800, 1600, 2000, 
        2200, 1800, 1400, 1800,  
        2000, 2200, 2400, 2100   #  flourish
    ]
    durations = [
        0.08, 0.08, 0.08, 0.1,
        0.08, 0.08, 0.08, 0.1,
        0.08, 0.08, 0.12, 0.2
    ]
    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)
    
    # LED off
    led_pink.off()

def play_black():
    """
    BLACK (#000000): Cozy nighttime with gentle 'heartbeat' and 'cricket chirp.'
    """
    # LED on
    led_black.on()

    for _ in range(4):
        play_tone(200, 0.2)
        utime.sleep(0.2)
        play_tone(1500, 0.05)
        utime.sleep(0.3)
    final_chirps = [1700, 1500, 1800]
    for freq in final_chirps:
        play_tone(freq, 0.05)
        utime.sleep(0.3)

    # LED off
    led_black.off()

def play_white():
    """
    WHITE (#FFFFFF): Gentle wind-chime or soft 'fairy dust' twinkle (airy, clean).
    """
    # LED on
    led_white.on()

    melody = [
        1200, 1400, 1600, 1800, 2000,
        1800, 1600, 2200, 2000, 2400,
        2200, 2000, 1400
    ]
    durations = [
        0.12, 0.12, 0.12, 0.15, 0.15,
        0.15, 0.12, 0.15, 0.15, 0.2,
        0.15, 0.12, 0.3
    ]
    for freq, dur in zip(melody, durations):
        play_tone(freq, dur)
    
    # LED off
    led_white.off()

#Todo: Implement NFC tag to distinguish each color
while True:

    # Turn off all LEDs before playing a new color
    turn_off_all_leds()

    
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
    
    print("ORANGt")
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
