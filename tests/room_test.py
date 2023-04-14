import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Karaoke", "pop")
        
        

    def test_room_has_name(self):
        self.assertEqual("Karaoke", self.room.name)


    def test_guest_count(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guest(self):
        person = Guest("Jimmy")
        self.room.guest_check_in(person)
        self.assertEqual(1, self.room.guest_count())

    def test_can_check_out_guest(self):
        person = Guest("Jimmy")
        self.room.guest_check_in(person)
        self.room.guest_check_out(person) 
        self.assertEqual(0, self.room.guest_count())

    def test_add_song_to_room(self):
        song = Song("Stayin' Alive")
        self.room.song_add(song)
        self.assertEqual(1, self.room.song_count())
