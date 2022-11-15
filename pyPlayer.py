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
        self.songList = [song]          #Lists track names
        self.songQueue = [self.song]    #Lists sound objects
        self.songIndex = 0              #Index to keep two arrays on track
    
    # def __minit__(self):
    #     # Initializes without first song
    #     mx.init()
    #     self.songList = []

    def print_song_data(self):
        print(self.songList, self.songQueue)

    def add_song(self, next_song):
        self.songList.append(next_song)
        self.songQueue.append(mx.Sound(next_song))
        self.print_song_data()
    
    def remove_song(self):
        self.songList.pop(self.songIndex)
        self.songQueue.pop(self.songIndex)
        self.print_song_data()

    def play_song(self):
        # Plays the song
        mx.Sound.play(self.song)
    
    def song_queue(self):
        if mx.get_busy == False:
            songIndex += 1
            self.stop()
            self.song = self.songQueue[self.songIndex]
    
    def pause(self):
        # Pauses the song
        mx.pause()

    def resume(self):
        # Resume/Unpause the song
        mx.unpause()
    
    def stop(self):
        mx.stop()
    
    def skip_forward(self):
        if (self.songIndex + 1) not in range(len(self.songQueue)):
            return
        self.songIndex += 1
        print("Now playing: ", self.songList[self.songIndex])
        self.stop()
        self.song = self.songQueue[self.songIndex]
        self.play_song()

    def skip_back(self):
        if (self.songIndex - 1) not in range(len(self.songQueue)):
            return
        self.songIndex -= 1
        print("Now playing: ", self.songList[self.songIndex])
        self.stop()
        self.song = self.songQueue[self.songIndex]
        self.play_song()
    
    # def is_playing(self):
    #     # Returns T/F if the song is playing or not
    #     return mx.get_busy()
    
    def quit(self):
        # mx.stop()
        # mx.quit()        
        exit()


if __name__ == "__main__":
    # Control Map
    PAUSE_KEY = "p"
    RESUME_KEY = "r"
    QUIT_KEY = "q"
    ADD_KEY = "a"
    REMOVE_KEY = "x"
    SKIP_FORWARD_KEY = "f"
    SKIP_BACK_KEY = "b"
    
    test_song = "sf.mp3"        # SCARLET..FIRE.. *music*
    playing = True
    medagl = MusicPlayer(test_song)
    # medagl = MusicPlayer()
    medagl.play_song()

    while True:
        print("Control (",PAUSE_KEY," to pause, ",RESUME_KEY," to resume, ",QUIT_KEY," to quit, ", ADD_KEY," to add to queue, ", REMOVE_KEY," to remove from queue, ", SKIP_FORWARD_KEY," to skip forward, ", SKIP_BACK_KEY, " to skip back): ", end="", sep="")
        control = input()
        # medagl.song_queue()
        if control == PAUSE_KEY and playing == True:
            playing = False
            medagl.pause()
        if control == RESUME_KEY and playing == False:
            playing = True
            medagl.resume()
        if control == QUIT_KEY:
            medagl.quit()
        if control.find(ADD_KEY) == 0:
            new_song = control[2:]
            medagl.add_song(new_song)
        if control == REMOVE_KEY:
            medagl.remove_song()
        if control == SKIP_FORWARD_KEY:
            medagl.skip_forward()
        if control == SKIP_BACK_KEY:
            medagl.skip_back()
