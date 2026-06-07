import time
import sys
import pygame

# Typing animation for each character
def type_lyric(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

lyrics = [
    Dikhte hain khwaab jo jaagti aankhon ko

Sapne nahi, iraade hain

Poore woh karne ko chal pade nange pairon

Khud se kiye jo waade hain

Rukna naa kabhi bhi tha hal

Chalna hi to hai manzil

"Main naa kaheen thehra"

"\nMain bhaaga-bhaaga, sadiyon se jaaga"

"\nAayaa hoon meelon gaaon se"

"\nNaa humsafar koi, naa apna ghar, yaara"

"\nRehta hoon behti naaon pe"

"\nMain bhaaga-bhaaga, sadiyon se jaaga"

"\nAayaa hoon meelon kaarke iraada"

"\nMain bhaaga-bhaaga, sadiyon se jaaga"

"\nAayaa hoon meelon kaarke iraada"
]

# Delays matched to song pacing (approximate, refine by listening carefully)
delays = [
    2.0, 3, 3.5,
    2.0, 3.5, 2.5,
    2.5, 2.5, 2.5,
    3.0, 2.5, 3.0
]

def print_lyrics():
    print("\nMain Tera – Arijit Singh (Kalank)\n")
    time.sleep(1.5)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("D:\Song_Project\main_tera_clip (mp3cut.net).mp3")  # <-- put your audio file here
    pygame.mixer.music.play()

    # Animate lyrics in sync
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

    print("\nEnd of Lyrics\n")

    # Stop music after lyrics end
    pygame.mixer.music.stop()

print_lyrics()
