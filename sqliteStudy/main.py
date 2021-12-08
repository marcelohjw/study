import random

f_names = ["Michael", "Christopher", "Joshua", "Matthew", "David", "Daniel", "Andrew", "Joseph", "Justin",
           "James", "Jessica", "Ashley", "Brittany", "Amanda", "Melissa", "Stephanie", "Jennifer",
           "Samantha", "Sarah", "Megan", "Lauren", "Carol", "Marcelo"]

l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
           "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
           "Robinson", "Passos", "Camara"]


def create_students(how_many):
    for i in range(how_many):
        f_name = f_names[random.randint(0, len(f_names) - 1)]
        l_name = l_names[random.randint(0, len(l_names) - 1)]

        sex = random.choice(['M', 'F'])
        print(f"INSERT INTO student (f_name, l_name, sex) VALUES ('{f_name}', '{l_name}', '{sex}');")


create_students(10)