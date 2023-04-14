class Room:
    def __init__(self, name, genre): 
        self.name = name
        self.genre = genre
        self.guest_list_in_room = []
        self.song = []
        self.count = 0

    def guest_count(self):
        return len(self.guest_list_in_room)


    def guest_check_in(self, person):
        self.guest_list_in_room.append(person)

    def guest_check_out(self, person):
        self.guest_list_in_room.remove(person)

    def song_add(self, tune):
        self.song.append(tune)

    def song_count(self):
        return len(self.song)
