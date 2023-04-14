import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room


class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Stayin' Alive")
        self.song1 = Song("Summertime")

