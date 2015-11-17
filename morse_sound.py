import pygame
import time

morse = {'a': '.-',     'b': '-...',   'c': '-.-.', 
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
     	's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
        
ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT
PATH = 'morse_sound_files/'

def check(string):
	keys = morse.keys()
	for char in string:
		if char.lower() not in keys and char != ' ':
			sys.exit('Oops! This ' + char + ' cannot be translated to Morse Code.')

def main():
    
	msg = raw_input('Enter Message:')
	check(msg)
	print
	pygame.init()
	
	for char in msg:
		if char == ' ':
			print ' '*7,
			time.sleep(SEVEN_UNITS)
		else:
			print morse[char.lower()],
			pygame.mixer.music.load(PATH + char.lower() + '_morse_code.ogg')
			pygame.mixer.music.play()
			time.sleep(THREE_UNITS)

def test():
    pygame.mixer.init()
    pygame.mixer.music.load(PATH + char.lower() + 'A_morse_code.ogg')
    pygame.mixer.music.play()
    
main()
