class Room:
    def __init__(self, name, genre): 
        self.name = name
        self.genre = genre
        self.guest_list = []
        self.song = []
        self.room_count = 0

    def guest_count(self):
        return len(self.guest_list)

    def guest_check_in(self, person):
        self.guest_list.append(person)
        
    def guest_check_out(self, person):
        self.guest_list.remove(person)

    def song_add(self, tune):
        self.song.append(tune)

    def song_add(self, tunes): 
        self.song.append(tunes)

    def song_count(self):
        return len(self.song)
    # print(self.song)--------- not sure why doesnt work?

    def guest_check_in(self, person):
        self.guest_list.append(person)

    # def find_guest_by_name(self, person_name): --------- didnt work
    #     for person in person_name:
    #         if self.guest1 == "Mindy":
    #             return person


# def guest_check_in(self, guests): -------didnt work
    #     for guest in guests:
    #         self.room_count += 1
