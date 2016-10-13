import time
import click
from random import randint
from rooms.room import LivingSpace, Office
from people.person import Fellow, Staff


class Amity(object):
    '''
    Amity is the main class that uses the imported
    inherited classes:
    1.LivingSpace, Office ---> Room
    2.Staff, Fellow ---> Person
    This class instantiates the above sub classes and
    appropriately performs operations from them.
    '''

    def __init__(self):
        self.all_rooms = []
        self.offices = []
        self.living_spaces = []
        self.rooms = {
            'offices': self.offices,
            'living_spaces': self.living_spaces
        }
        # Regarding People
        self.fellows = []
        self.staff = []
        self.people = {
            'fellows': self.fellows,
            'staff': self.staff
        }
        self.people_stats = []
        # f_ids and s_ids is used to generate the IDS
        # fellows ID Example ---> F23
        # staff ID example ---> S15
        self.f_ids = [0]
        self.s_ids = [0]
        # Regarding allocations
        self.staff_allocations = []
        self.fellow_allocations = []
        self.office_details = {
            'available': [],
            'unavailable': []
        }
        self.ls_details = {
            'available': [],
            'unavailable': []
        }

    def create_room(self, room_type, room_name):
        '''
        The create_room method in the amity class takes
        in room_type and room_name and parses them via docopt
        to be able to append them to either the offices or living
        spaces lists initialized above.
        An office is created as an instance of the Office class.
        A living space is created as an instance of the LivingSpace class.
        -->The single room dictionary holds information regarding
        a specific single room and appends this to the ALL_ROOMS
        (lowercase).<s

        '''
        if type(room_type) != str or room_type.upper() not in ['O', 'L']:
            click.secho('Error.Please enter O or L for a room',
                        bold=True, fg='red')
            return 'Error. Invalid room type initial.'
        room_type = room_type.strip().title()
        room_name = room_name.strip().title()
        if room_name in self.offices or room_name in self.living_spaces:
            click.secho(
                'The room name %s already exists. Please pick another name.' % room_name.upper(),
                bold=True, fg='red')
            return 'Error. Room already exists.'
        if room_type == 'O':
            room = Office(room_name)
            single_room['occupants'] = []
            self.offices.append(office.room_name)
            self.office_details['available'].append(office.room_name)
        elif room_type.upper() == 'L':
            living = LivingSpace(room_name)
            single_room['room_name'] = living.room_name
            single_room['room_type'] = living.room_type
            single_room['room_capacity'] = living.capacity
            single_room['occupants'] = []
            self.living_spaces.append(livroom_name)
            self.ls_details['available'].append(room_name)
        self.all_rooms.append(single_room)
        click.secho('The %s ---> %s has been created.' %
                    (single_room['room_type'], room_name), bold=True, fg='green')
        return 'Room %s created.' % room_name

    def print_allocations(self):
        """
        This prints allocations to the screen and
        highlights if they are empty or have any
        occupants, thereafter printing everyone who
        is in the particular room.
        """
        if bool(self.all_rooms) is False:
            click.secho('THERE ARE NO ROOMS IN THE SYSTEM.',
                        fg='red', bold=True)
            return 'Error. No rooms within system.'
        for room_index in range(len(self.all_rooms)):
            if self.all_rooms[room_index]['occupants']:
                click.secho(self.all_rooms[room_index]['room_name'].upper())
                click.secho('==' * 10, fg='cyan')
                for occupant in self.all_rooms[room_index]['occupants']:
                    click.secho(occupant)
            else:
                click.secho(self.all_rooms[room_index][
                            'room_name'], fg='yellow')
                click.secho('==' * 20)
                click.secho(
                    'There are no people in this room yet.', fg='cyan')

    def add_person(self, first_name, other_name, person_type,
                   wants_accomodation='N'):
        if type(first_name) != str or type(other_name) != str:
            click.secho('Incorrect name type format.', fg='red')
            return 'Wrong type for name.'
        if first_name.isalpha() is False or other_name.isalpha() is False:
            click.secho('Person names need be alphabetical in nature',
                        fg='red', bold=True)
            return 'Non-Alphanumeric names added'
        first_name = first_name.strip().title()
        other_name = other_name.strip().title()
        full_name = first_name + ' ' + other_name

        for person in self.people_stats:
            if person['full_name'] == full_name and person['person_type'] == person_type:
                click.secho('Person already exists')
                return 'Person exists'
        person_type = person_type.strip().title()
        if person_type not in ['Fellow', 'Staff']:
            click.secho('Please enter either Fellow or Staff for person type',
                        fg='red', bold=True)
            return 'Invalid Person Type'
        if wants_accomodation.upper() not in ['Y', 'N']:
            click.secho('Please enter Y or N for wants accomodation.',
                        fg='red', bold=True)
            return 'Wants accomodation not Y or N'
        if person_type == 'Staff' and wants_accomodation == 'Y':
            click.secho(
                'A Staff member cannot be allocated accomodation.', fg='red', bold=True)
            return 'Staff cannot have wants allocation of Yes.'
        if wants_accomodation.upper() == 'Y' and person_type == 'Fellow':
            if not self.living_spaces:
                click.secho(
                    'Please add a living space for a fellow to be allocated both room types.')
                return 'No Living space for fellow requiring both.'
            if not self.offices:
                click.secho(
                    'Please add an office for a fellow to be allocated both room types.')
                return 'No office for fellow requiring both.'

        if not self.all_rooms:
            msg = 'Currently there are no rooms.'
            msg += 'Please create a room before adding a person.'
            msg += 'This is for purposes of random allocation.'
            click.secho(msg, fg='red')
            return 'No rooms added for random allocation.'
        person_stats = {}
        person_stats['full_name'] = full_name
        person_stats['wants_accomodation'] = wants_accomodation

        if self.people_stats:
            if person_type == 'Fellow':
                fellow = Fellow()
                f_id = 1
                self.f_ids.append(f_id)
                person_stats['person_id'] = 'F' + str(f_id)
                person_stats['person_type'] = fellow.person_type
                self.fellows.append(full_name)
            elif person_type == 'Staff':
                staff = Staff()
                s_id = 1
                self.s_ids.append(s_id)
                person_stats['person_id'] = 'S' + str(s_id)
                person_stats['person_type'] = staff.person_type
                self.staff.append(full_name)
        else:
            if person_type == 'Fellow':
                fellow = Fellow()
                f_id = self.f_ids.pop() + 1
                person_stats['person_id'] = 'F' + str(f_id)
                person_stats['person_type'] = fellow.person_type
                self.f_ids.append(f_id)
                self.fellows.append(full_name)
            elif person_type == 'Staff':
                staff = Staff()
                s_id = self.s_ids.pop() + 1
                person_stats['person_id'] = 'S' + str(s_id)
                person_stats['person_type'] = staff.person_type
                self.s_ids.append(s_id)
                self.staff.append(full_name)
        self.people_stats.append(person_stats)
        click.secho('The %s %s has been created.\n' %
                    (person_type.title(), full_name), fg='green', bold=True)
        click.secho('ALLOCATING ROOM ...', fg='cyan')
        time.sleep(2)
        click.secho('Success!', fg='green')
        # random allocation
        # only a fellow can be allocated a living space
        # a staff can only be allocated an office.
        # if person_type == 'Staff':
        #     staff_single_allocation = {}
        #     staff_single_allocation[full_name] = self.offices[
        #         randint(0, (len(self.offices) - 1))]
        #     self.staff_allocations.append(staff_single_allocation)
        #     for room in self.all_rooms:
        #         if room['room_name'] == staff_single_allocation[full_name]:
        #             room['occupants'].append(full_name)
        # if person_type == 'Fellow' and wants_accomodation == 'Y':
        #     fellow_single_allocation = {}
        #     fellow_single_allocation['name'] = full_name
        #     fellow_single_allocation['office'] = self.offices[
        #         randint(0, (len(self.offices) - 1))]
        #     fellow_single_allocation['living_space'] = self.living_spaces[
        #         randint(0, (len(self.living_spaces) - 1))]
        #     self.fellow_allocations.append(fellow_single_allocation)
        #     for r in range(len(self.all_rooms)):
        #         if self.all_rooms[r]['room_name'] == fellow_single_allocation['office']:
        #             self.all_rooms[r]['occupants'].append(full_name)
        #         elif self.all_rooms[r]['room_name'] == fellow_single_allocation['living_space']:
        #             self.all_rooms[r]['occupants'].append(full_name)
        # else:
        #     fellow_single_allocation = {}
        #     fellow_single_allocation[full_name] = self.offices[
        #         randint(0, (len(self.offices) - 1))]
        #     self.fellow_allocations.append(fellow_single_allocation)
        #     for r in range(len(self.all_rooms)):
        #         if self.all_rooms[r]['room_name'] == fellow_single_allocation[full_name]:
        #             self.all_rooms[r]['occupants'].append(full_name)
        # return 'person has been created'

    def allocate_room(self, person_name, person_type, accomodate=False):
        if not self.offices:
            return 'Please add an office'
        for room in self.all_rooms:
            if len(room['occupants']) == 4:
                self.offices['unavailable'].append(room)
                return 'Unavailable room.'
        for 

    def reallocate_person(self, person_id, room_name):
        if type(room_name) != str:
            return 'Error. Please enter valid room name.'

        people_ids = []
        for p in range(len(self.people_stats)):
            if self.people_stats[p]['person_id']:
                people_ids.append(self.people_stats[p]['person_id'])
        if person_id not in people_ids:
            return 'Error. The person you entered does not exist in our system.'
        amity_rooms = []
        for office in self.offices:
            amity_rooms.append(office)
        for living_space in self.living_spaces:
            amity_rooms.append(living_space)
        if room_name not in amity_rooms:
            return 'Error. The room name you entered does not exist on our system.'

        # find out first where a person is allocated
        # remove them from that list / dictionary
        # reallocate them as need be
        for p in range(len(self.people_stats)):
            if self.people_stats[p]['person_id'] == person_id:
                found_name_in_old_room = self.people_stats[p]['name']
                for r in range(len(self.all_rooms)):
                    if found_name_in_old_room in self.all_rooms[r]['occupants']:
                        self.all_rooms[r]['occupants'].remove(
                            found_name_in_old_room)
                    if room_name == self.all_rooms[r]['room_name']:
                        self.all_rooms[r]['occupants'].append(
                            found_name_in_old_room)
            return 'Success! %s has been reallocated to %s ' % (found_name_in_old_room.title(), room_name)

            # except Exception as e:
            #     print(e)
            #     return 'An error occurred'
    def print_room(self, room_name):
        for r in range(len(self.all_rooms)):
            if self.all_rooms[r]['room_name'] == room_name:
                click.secho('Room Name : %s\n ' % room_name, fg='yellow')
                if self.all_rooms[r]['occupants']:
                    for occupant in self.all_rooms[r]['occupants']:
                        click.secho('=' * 10, fg='cyan')
                        click.secho(occupant)
                else:
                    click.secho(
                        'There are no occupants in this room as per now.', fg='yellow')


# amity = Amity()
# amity.create_room('O', 'Krypton')
# amity.create_room('O', 'Oculus')
# # amity.create_room('O', 'Narnia')
# # amity.create_room('O', 'Vahalla')
# amity.create_room('L', 'PHP')
# amity.create_room('L', 'Ruby')
# # amity.create_room('L', 'Haskell')
# # amity.create_room('L', 'Python')

# # # amity.create_room('L', 'Oculus')
# # # print(amity.all_rooms)
# # # amity.print_allocations()
# amity.add_person('kIMANI nDEGWA', 'Fellow')
# # amity.add_person('kamau dungu', 'Staff')
# # # print(amity.add_person('KINJA KARIUKI', 'Staff'))

# # print(amity.people_stats)
# amity.print_room('Oculus')
# print(amity.all_rooms)
# print(amity.staff_allocations)
# print(amity.fellow_allocations)
# print(amity.reallocate_person('F1', 'Oculus'))
# print(amity.all_rooms)
# print(len(amity.all_rooms))
# amity.print_allocations()
