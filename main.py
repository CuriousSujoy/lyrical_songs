import time
import sys
import pygame

from Song import safar, HUSN, Arz_Kiya_Hai, Nachdi_Phira

def type_lyric(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

    print()

def play_song(song):
    print(f"\n{song.title}\n")
    time.sleep(1.5)

    pygame.mixer.init()

    pygame.mixer.music.load(song.audio_file)
    pygame.mixer.music.play()

    for i, line in enumerate(song.lyrics):
        type_lyric(line)
        time.sleep(song.delays[i])
        print(f"DEBUG Delay[{i}] = {song.delays[i]}")

    print("\nEnd of Lyrics\n")
    print(
        "\nSubscribe to the YouTube channel or Instagram page\n"
        "Follow CuriousSujoy on GitHub for such programs with other songs"
)

    pygame.mixer.music.stop()

def show_menu():
    songs = {
    1: safar,
    2: HUSN,
    3: Arz_Kiya_Hai,
    4: Nachdi_Phira
    }

    print("===== SONG MENU =====")
    print("1. Safar 2. HUSN 3. Arz Kiya Hai 4. Nachdi Phira")
    print("0. Exit")
    try:
        choice = int(input("\nSelect Song: "))
    except ValueError:
        print("Please enter a number.")
        return

    if choice == 0:
        print("Goodbye!")
        return

    if choice in songs:
        play_song(songs[choice])
    elif choice in songs:
        play_song(songs[choice])
    else:
        print("Invalid Choice")


show_menu()
