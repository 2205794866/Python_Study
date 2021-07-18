class SchoolMember:
    '''代表任何学校里的从成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    '''代表一位老师'''
    def