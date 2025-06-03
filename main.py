from machine import Pin, PWM
import utime
from myneopixel import Neopixel
from mfrc522 import MFRC522

#RFID reader setup
reader = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

buzzer_pin = machine.Pin(16)
buzzer = machine.PWM(buzzer_pin)

pixels = Neopixel(15, 0, 17)
pixels.brightness(100)

#button setup for mode switching
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
mode = 1  # Start in learning mode
last_button_state = 1
button_pressed = False

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

#RFID tag to color/sound mapping
tag_actions = {
    334816739: play_red,
    30138130: play_blue,
    29755974: play_yellow,
    83430365: play_green,
    84748377: play_orange,
    677346675: play_purple,
}

# For testing mode
import urandom
color_functions = [play_red, play_blue, play_yellow, play_green, play_orange, play_purple, play_pink, play_white, play_black]
color_names = ["RED", "BLUE", "YELLOW", "GREEN", "ORANGE", "PURPLE", "PINK", "WHITE", "BLACK"]
current_test_color = None
test_function = None
score = 0
attempts = 0

def check_button():
    """Check for button press and handle mode switching"""
    global mode, last_button_state, button_pressed, current_test_color, test_function, score, attempts
    
    current_button_state = button.value()
    
    # Detect button press (falling edge)
    if last_button_state == 1 and current_button_state == 0:
        button_pressed = True
        
    last_button_state = current_button_state
    
    if button_pressed:
        button_pressed = False
        mode = 2 if mode == 1 else 1  # Toggle between modes
        
        # Reset testing mode variables when switching
        current_test_color = None
        test_function = None
        score = 0
        attempts = 0
        
        turn_off_all_pixels()
        
        if mode == 1:
            print("\n=== LEARNING MODE ===")
            print("Scan any tag to see its color and hear its sound!")
        else:
            print("\n=== TESTING MODE ===")
            print("Listen to the sound and scan the matching color tag!")
            generate_test_question()

def generate_test_question():
    """Generate a random color/sound for testing"""
    global current_test_color, test_function
    
    random_index = urandom.getrandbits(32) % len(color_functions)
    test_function = color_functions[random_index]
    current_test_color = color_names[random_index]
    
    print(f"\nListen to this sound and find the matching color tag:")
    utime.sleep(1)
    test_function()
    print("Which color was that? Scan the corresponding tag!")

def check_test_answer(scanned_card_id):
    """Check if the scanned tag matches the test color"""
    global score, attempts, current_test_color, test_function
    
    attempts += 1
    
    if scanned_card_id in tag_actions:
        scanned_function = tag_actions[scanned_card_id]
        
        if scanned_function == test_function:
            score += 1
            print(f"✓ CORRECT! That was {current_test_color}!")
            print(f"Score: {score}/{attempts}")
            
            # Success feedback
            for _ in range(3):
                light_color(GREEN)
                play_tone(523, 0.2)  # High success tone
                turn_off_all_pixels()
                utime.sleep(0.1)
            
            utime.sleep(1)
            generate_test_question()  # Next question
            
        else:
            # Find the actual color name for the scanned tag
            scanned_color = "UNKNOWN"
            for name, func in zip(color_names, color_functions):
                if func == scanned_function:
                    scanned_color = name
                    break
                    
            print(f"✗ Wrong! You scanned {scanned_color}, but the answer was {current_test_color}")
            print(f"Score: {score}/{attempts}")
            
            # Error feedback
            for _ in range(2):
                light_color(RED)
                play_tone(200, 0.3)  # Low error tone
                turn_off_all_pixels()
                utime.sleep(0.2)
            
            print("Try again! The sound was:")
            utime.sleep(1)
            test_function()  # Replay the sound
    else:
        print("Unknown tag! Please use a registered color tag.")
        play_tone(150, 0.5)  # Unknown tag tone

print("RFID Color & Sound Learning System Ready!")
print("Button: Switch between Learning and Testing modes")
print("=== LEARNING MODE ===")
print("Scan any tag to see its color and hear its sound!")
print("")

# Main loop
while True:
    # Check for button press
    check_button()
    
    # RFID Reading
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid), "little", False)
            
            if mode == 1:  # Learning Mode
                print(f"Card ID: {card}")
                
                if card in tag_actions:
                    # Find color name for display
                    color_name = "UNKNOWN"
                    for name, func in zip(color_names, color_functions):
                        if func == tag_actions[card]:
                            color_name = name
                            break
                    
                    print(f"Playing {color_name}...")
                    tag_actions[card]()  # Execute the color/sound function
                    turn_off_all_pixels()
                    print("Scan another tag to continue learning!")
                else:
                    print("Unknown card! Add this ID to tag_actions dictionary.")
                    light_color(RED)
                    play_tone(200, 0.5)
                    turn_off_all_pixels()
                    
            else:  # Testing Mode
                if current_test_color is None:
                    generate_test_question()
                else:
                    check_test_answer(card)
    
    utime.sleep(0.1)  # Small delay

# print("RFID Color & Sound System Ready!")
# print("Available colors: RED, BLUE, YELLOW, GREEN, ORANGE, PURPLE, PINK, WHITE, BLACK")
# print("Bring RFID tag closer...")
# print("")

# while True:
#     reader.init()
#     (stat, tag_type) = reader.request(reader.REQIDL)
    
#     if stat == reader.OK:
#         (stat, uid) = reader.SelectTagSN()
#         if stat == reader.OK:
#             card = int.from_bytes(bytes(uid), "little", False)
#             print(f"Card ID: {card}")
            
#             if card in tag_actions:
#                 color_name = [k for k, v in globals().items() if callable(v) and v == tag_actions[card]][0].replace('play_', '').upper()
#                 print(f"Playing {color_name}...")
#                 tag_actions[card]() 
#                 turn_off_all_pixels()
#                 print("Ready for next tag...")
#             else:
#                 print("Unknown card! Add this ID to tag_actions dictionary.")
#                 light_color(RED)
#                 play_tone(200, 0.5)  
#                 turn_off_all_pixels()
    
#     utime.sleep(0.5)  

# while True:
#     turn_off_all_pixels()
    
#     print("RED")
#     play_red()
#     utime.sleep(1)
    
#     print("BLUE")
#     play_blue()
#     utime.sleep(1)
    
#     print("YELLOW")
#     play_yellow()
#     utime.sleep(1)
    
#     print("GREEN")
#     play_green()
#     utime.sleep(1)
    
#     print("ORANGE")
#     play_orange()
#     utime.sleep(1)
    
#     print("PURPLE")
#     play_purple()
#     utime.sleep(1)
    
#     print("PINK") 
#     play_pink()
#     utime.sleep(1)
    
#     print("BLACK")
#     play_black()
#     utime.sleep(1)
    
#     print("WHITE")
#     play_white()
#     utime.sleep(3)