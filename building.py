class Building:
    '''
    Describe Building
    '''
    def __init__(self, address):
        '''
        Take a address
        >>> building = Building('Kozelnytska 2a')
        >>> print(building.address)
        Kozelnytska 2a
        '''
        self.address = address

class House(Building):
    '''
    Identify house
    '''
    def __init__(self, address, list_of_flats):
        '''
        Take address and apartments list
        >>> apartment = House('St. Bandera', ['first', 'second', 'third'])
        >>> print(apartment.address)
        St. Bandera
        '''
        super().__init__(address)
        self.list_of_flats = list_of_flats
        self.kids = []

class Classroom:
    '''
    Info about classrooms
    '''
    def __init__(self, number, capacity, equipment):
        '''
        init method
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        '''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        '''
        Return full info
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has\
 the following equipment: PC, projector, mic.
        '''
        res = ''
        for elem in self.equipment:
            res += " " + elem
            if elem != self.equipment[-1]:
                res += ","
        return f'Classroom {self.number} has a capacity of {self.capacity} persons and has\
 the following equipment:{res}.'

    def is_larger(self, auditory):
        '''
        Check if classroom larger
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        '''
        self.auditory = auditory
        if self.capacity > self.auditory.capacity:
            return True
        return False

    def equipment_differences(self, auditory):
        '''
        Return equipment difference
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'projector', 'mic']
        '''
        self.auditory = auditory
        different = []
        for elem in self.equipment:
            if elem not in self.auditory.equipment:
                different.append(elem)
        return different

    def __repr__(self):
        '''
        Information about classroom
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        '''
        class_name = self.__class__.__name__
        argument_s = (self.number, self.capacity, self.equipment)
        res = f'{class_name}{argument_s}'
        return res
        
class AcademicBuilding(Building):
    '''
    Check classrooms
    '''
    def __init__(self, address, classrooms):
        '''
        init method
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        '''
        super().__init__(address)
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        '''
        Count equipment
        >>> classrooms = []
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        []
        '''
        equipment_list = []
        for classroom in self.classrooms:
            equipment_list += classroom.equipment
        equipment_total = []
        for elem in set(equipment_list):
            counter = equipment_list.count(elem)
            equipment_total.append((elem, counter))
        equipment_total.sort(key=lambda x:x[0])
        return equipment_total

    def __str__(self):
        '''
        Returns classrooms' info
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following\
 equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following\
 equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following\
 equipment: PC, projector.
        '''
        info = f'{self.address}\n'
        for elem in self.classrooms:
            if elem != self.classrooms[-1]:
                info += f'{elem}\n'
            else:
                info += f'{elem}'
        return info
        # my_str = f'{self.addres}\n{info}'
        # return print(classroom.__str__(self.classrooms))

apartment = House('St. Bandera', ['first', 'second', 'third'])
print(apartment.__str__())

# building = Building('Kozelnytska 2a')
# print(building.address)