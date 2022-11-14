#!/bin/python3
# MeDaGe Player Component - The music player
# This utilizes the pygame mixer component to have control over audio files and how they play/pause/resume
# Component Dependencies: Python3, PyGame
# pygame is available in the pip repository for free under the LGPL license
# Documentation for pygame mixer https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.init
# Song used for testing is Scarlet Fire by Otis McDonald, which is available in the YouTube Creator Studio Royalty Free Music Library

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.mixer as mx


class MusicPlayer:
    def __init__(self, song):
        # Initializes with pygame mixer sound as song input
        mx.init()
        self.song = mx.Sound(song) #Expects a filetype with a .mp3 ending
        self.songList = [song]
    
    # def __minit__(self):
    #     # Initializes without first song
    #     mx.init()
    #     self.songList = []

    def add_song(self, next_song):
        self.songList.append(next_song)
        print(self.songList)
    
    def remove_song(self):
        self.songList.pop(0)
        print(self.songList)

    def play_song(self):
        # Plays the song
        mx.Sound.play(self.song)
    
    # def song_queue(self):
    #     if mx.get_busy == False:
    #         mx.Sound.play(self.songList[0])
    #         self.remove_song()
    
    def pause(self):
        # Pauses the song
        mx.pause()

    def resume(self):
        # Resume/Unpause the song
        mx.unpause()
    
    def is_playing(self):
        # Returns T/F if the song is playing or not
        return mx.get_busy()
    
    def stop(self):
        # mx.stop()
        # mx.quit()        
        exit()


if __name__ == "__main__":
    # Control Map
    PAUSE_KEY = "p"
    RESUME_KEY = "r"
    STOP_KEY = "s"
    ADD_KEY = "a"
    REMOVE_KEY = "x"
    
    test_song = "sf.mp3"        # SCARLET..FIRE.. *music*
    playing = True
    medagl = MusicPlayer(test_song)
    # medagl = MusicPlayer()
    medagl.play_song()

    while True:
        print("Control (",PAUSE_KEY," to pause, ",RESUME_KEY," to resume, ",STOP_KEY," to stop, ", ADD_KEY," to add to queue, ", REMOVE_KEY," to remove from queue): ", end="", sep="")
        control = input()
        # medagl.song_queue()
        if control == PAUSE_KEY and playing == True:
            playing = False
            medagl.pause()
        if control == RESUME_KEY and playing == False:
            playing = True
            medagl.resume()
        if control == STOP_KEY:
            medagl.stop()
        if control.find(ADD_KEY) == 0:
            new_song = control[2:]
            medagl.add_song(new_song)
        if control == REMOVE_KEY:
            medagl.remove_song()
