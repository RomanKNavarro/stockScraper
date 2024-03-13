# Profile Creator (revision 3)
import random
print('Welkommen to zhe Auschwitz Database Terminal (3)')

profiles = []
def structure(list):
        just = 0
        alt = 20
        wall = ' '
        print('NAME'.ljust(alt), 'AGE'.center(just, wall), 'COUNTRY'.rjust(alt, wall))
        for x in profiles:
                print(x[0].ljust(alt), x[1].center(just), x[2].rjust(alt))
                
def sched(name):
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        day = random.randint(1,32)
        print('''Hallo, ''' + name + '''! Your visit to the cremetorium is scheduled for
''' + random.choice(month), str(day) + '''! Enjoy your stay!\n ''')
        
while True:
    print('new profile or view existing?')
    respond = input()
    if respond == 'new':
        print('first name?')
        nombre = input()
        print('age?')
        edad = input()
        print('country of birth?')
        home = input()
        indiv = [nombre, edad, home]                
        profiles.append(indiv)
        sched(nombre)
    if respond == 'e':
        structure(profiles)