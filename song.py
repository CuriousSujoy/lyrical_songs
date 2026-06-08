import time
import sys
import pygame

# Character by Character printing
def type_lyric(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
#List of the lyrics (As multiple string so that I can adjust the delay between each sentence printing)
lyrics = [
    "\nDikhte hain khwaab jo jaagti aankhon ko",

    "\nSapne nahi, iraade hain",

    "\nPoore woh karne ko chal pade nange pairon",

    "\nKhud se kiye jo waade hain",

    "\nRukna naa kabhi bhi tha hal",

    "\nChalna hi to hai manzil",

    "\nMain naa kaheen thehra",

    "\nmusic.........",

    "\nMain bhaaga-bhaaga, sadiyon se jaaga",

    "\nAayaa hoon meelon gaaon se",

    "\nmusic.........",

    "\nNaa humsafar koi, naa apna ghar, yaara",

    "\nRehta hoon behti naaon pe.....",

    "\nMain bhaaga-bhaaga, sadiyon se jaaga",

    "\nAayaa hoon meelon kaarke iraada",

    "\nMain bhaaga-bhaaga, sadiyon se jaaga",

    "\nAayaa hoon meelon kaarke iraada"
]

# Delays matched to song pacing (approximate, refined by listening carefully)
delays = [
    4.0, 4.0, 3.0, 3.2,
    2.0, 2.0, 2.3, 1.0,
    2.0, 4.0, 0.7, 3.1,
    4.0, 3.1, 3.6, 4.0,
    3.6
]

#Below function is responsible for printing sentence by sentence animation, delays is used in this function
def print_lyrics():
    print("\nSafar\n")
    time.sleep(1.5)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load audio file from project folder
    pygame.mixer.music.load("Song_Clips/Safar_clip.mp3")
    pygame.mixer.music.play()

    # Animating lyrics in sync
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

    print("\nEnd of Lyrics\n")
    print("\nSubscribe to the youtube channel or instagram page\nFollow CuriousSujoy on GitHub for such programs with other songs")

    # Stop music after lyrics end
    pygame.mixer.music.stop()

print_lyrics()