fellows = []
staff = []
<<<<<<< HEAD

people = {
    'fellows': fellows,
    'staff': staff

}

people_stats = []

f_ids = [0]
s_ids = [0]


class Person(object):
    def __init__(self, person_type=None):
        self.person_type = person_type

    def get_person_type(self):
        return 'Person type is %s' % self.person_type

    # def add_person(self, name, person_type, wants_accomodation='N'):
    #     """b
    #     This function adds a person and proceeds the respective
    #     instance and appends them to a list.
    #     """
    #     full_name = name.split(" ")
    #     if not (full_name[0].isalpha() or full_name[1].isalpha()):
    #         return 'All your words must be alphabetical in nature.'
    #     # Check person type
    #     if self.person_type not in ['Fellow', 'Staff']:
    #         return 'Please enter Fellow or Staff for person type.'
    #     # Check wants_accomodation to be either Y or N
    #     if wants_accomodation not in ['Y', 'N']:
    #         return 'Please enter Y or N for accomodation.'
    #     if self.person_type == 'Staff' and wants_accomodation == 'Y':
    #         return 'A Staff member cannot be allocated accomodation.'


class Staff(Person):
    def __init__(self):
        super(Staff, self).__init__(person_type='Staff')


class Fellow(Person):
    def __init__(self):
        super(Fellow, self).__init__(person_type='Fellow')


s = Staff()
print(s.get_person_type())
=======

people = {
    'fellows': fellows,
    'staff': staff

}

people_stats = []

f_ids = [0]
s_ids = [0]


class Person(object):
    def __init__(self, person_type=None):
        self.person_type = person_type

    def add_person(self, name, person_type, wants_accomodation='N'):
        """b
        This function adds a person and proceeds the respective
        instance and appends them to a list.
        """
        full_name = name.split(" ")
        if not (full_name[0].isalpha() or full_name[1].isalpha()):
            return 'All your words must be alphabetical in nature.'
        # Check person type
        if self.person_type not in ['Fellow', 'Staff']:
            return 'Please enter Fellow or Staff for person type.'
        # Check wants_accomodation to be either Y or N
        if wants_accomodation not in ['Y', 'N']:
            return 'Please enter Y or N for accomodation.'
        if self.person_type == 'Staff' and wants_accomodation == 'Y':
            return 'A Staff member cannot be allocated accomodation.'
        person_stats = {}
        # Person stats holds the specific person details to
        # be appended to a list --> people_stats
        # people_stats is a list of dictionaries for each person_stats
        person_stats['name'] = name
        person_stats['person_type'] = self.person_type
        person_stats['wants_accomodation'] = wants_accomodation.upper()
        '''
        After assigning person_stats['person_type'], we
        now proceed to figure out their id.
        '''
        try:
            if bool(people_stats) is False:
                if person_stats['person_type'] == 'Fellow':
                    f_id = 1
                    f_ids.append(f_id)
                    person_stats['person_id'] = 'F' + str(f_id)
                elif person_stats['person_type'] == 'Staff':
                    s_id = 1
                    s_ids.append(s_id)
                    person_stats['person_id'] = 'S' + str(s_id)
            else:
                if person_stats['person_type'] == 'Fellow':
                    f_id = f_ids.pop() + 1
                    person_stats['person_id'] = 'F' + str(f_id)
                    f_ids.append(f_id)
                elif person_stats['person_type'] == 'Staff':
                    s_id = s_ids.pop() + 1
                    person_stats['person_id'] = 'S' + str(s_id)
                    s_ids.append(s_id)
            people_stats.append(person_stats)
            if self.person_type == 'Fellow':
                fellows.append(name)
            elif self.person_type == 'Staff':
                staff.append(name)
            return people_stats
            #Allocate room
        except Exception as e:
            print(e)
            return 'An error occurred.'


class Staff(Person):
    def __init__(self):
        super(Staff, self).__init__(person_type='Staff')


class Fellow(Person):
    def __init__(self):
        super(Fellow, self).__init__(person_type='Fellow')


# f = Fellow()
# x = f.add_person('Jee Gikera', 'Fellow', 'Y')


# f = Fellow()
# x = f.add_person('kIMANI Ndegwa', 'Fellow')

# s = Staff() 
# x = s.add_person('Mwanik Joshua', 'Staff')

 
# # y = f.add_person('Njeri', 'Mudiay', 'Fellow')
# # s = Staff()
# # z = s.add_person('Oscar', 'Mazera', 'Staff')
# print(people_stats)
>>>>>>> af7e76160ec0b36c03fad1cbc98230c89bee7251