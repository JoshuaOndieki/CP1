class Room(object):
    """
    This class models both the Living Space and Office
    space in the proposed Amity Room Allocation System.
    The Room class is a Super Class from which both
    Living Space Class and Office Class are Sub Classes of.
    Its main inheritable attrubute is
    Room name alias room_name
    """

    def __init__(self):
        pass

    def create_room(self, room_name):
        self.room_name = room_name
        self.occupants = []

    def check_room_occupants(self):
        if len(self.occupants) == 0:
            return "There are no occupants in this room as yet."
        else:
            return len(self.occupants)

    def add_person(self, person_identifier):
        if person_identifier:
            self.occupants.append(self.person_identifier)
        return 'Please add a person identifier to add to the room'
