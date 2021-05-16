from helpers import get_countries


__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'


""" Functions """


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = dict([
        ('name', name),
        ('date_of_birth', date_of_birth),
        ('place_of_birth', place_of_birth),
        ('height', height),
        ('nationality', nationality)
    ])
    return passport


def add_stamp(passport, country):
    if 'stamps' not in passport:
        passport['stamps'] = ['dummy']
    if country not in passport['stamps'] and country != passport['nationality']:
        passport['stamps'].append(country)
    if 'dummy' in passport['stamps']:
        passport['stamps'].remove('dummy')
    return passport


def check_passport(passport, country, access, no_access):
    allowed_to = access[passport['nationality']]
    not_allowed_to = no_access[country]
    print('Nationality: ',passport['nationality'])
    print('Destination country: ',country)
    for i in allowed_to:
        while country in allowed_to:
                if 'stamps' not in passport:
                    add_stamp(passport, country)
                    print('access allowed')
                    return passport
                else:
                    for j in passport['stamps']:
                        for k in not_allowed_to:
                            if k == j:
                                print('access NOT allowed: forbidden stamp', '\n')
                                return False
                    

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.


if __name__ == '__main__':
    countries = get_countries()


    """ Calls to functions """


hank = create_passport('H. Vandenaerde', '1992-11-23', 'Gent', 1.75, 'Belgium')
print('Passport', hank['name'])
print(hank, '\n')
hank_check = check_passport(hank, 'Netherlands', {'Belgium': ['Netherlands']}, {'Netherlands': ['North Korea']})
print('Passport', hank['name'])
print(hank, '\n')

add_stamp(hank, 'North Korea')
print('Passport', hank['name'])
print(hank, '\n')
hank_check = check_passport(hank, 'Netherlands', {'Belgium': ['Netherlands']}, {'Netherlands': ['North Korea']})
print('Passport', hank['name'])
print(hank, '\n')

