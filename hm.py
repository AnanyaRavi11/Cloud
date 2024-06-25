class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def check_availability(self, room_number):
        if room_number in self.rooms:
            return f"Room {room_number} is available."
