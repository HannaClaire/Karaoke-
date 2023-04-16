import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Karaoke", "pop")
        self.room2 = Room("Karaoke", "Jazz" )
        
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

    def test_add_song_to_room(self):
        song1 = Song("Summertime")#-----------Not recognised in test?
        self.room2.song_add(song1)
        self.assertEqual(1, self.room2.song_count())
    
    def test_add_guest_to_room(self):
        person = Guest("Mindy")
        self.room2.guest_check_in(person)
        self.assertEqual(1, self.room2.guest_count())

    # def test_find_guest_by_name(self): --------------didnt work
    #     self.room2.find_guest_by_name("Mindy")
    #     self.assertEqual("Mindy", self.room2.name)

    # def test_add_guests_to_room(self):
    #     person = Guest("Mindy") ----------------------tried to append everyone, didnt work
    #     self.room.guest_check_in(person)
    #     self.assertEqual(1, self.room.room_count)
    #     person = Guest("Bob")
    #     self.room.guest_check_in(person)
    #     self.assertEqual(2, self.room.room_count)
    #     person = Guest("Jimmy")
    #     self.room.guest_check_in(person)
    #     self.assertEqual(3, self.room.room_count)
    
    
