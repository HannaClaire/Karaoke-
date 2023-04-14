import unittest
from src.guest import Guest
from src.room import Room
# from src.Song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Jimmy")
        
    def test_guest_has_name(self):
        self.guest.get_name()
