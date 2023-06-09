import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Jimmy")
        self.guest1 = Guest("Mindy")
        self.guest2 = Guest("Bob")
        
    def test_guest_has_name(self):
        self.assertEqual("Jimmy", self.guest.name)
