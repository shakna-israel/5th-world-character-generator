import random

def choose_name(sex):
    unisex_names = ["Cameron","Jordan","Taylor","Tyler","Jamie","Casey","Bailey","Cassidy","Presley","Cori","Cory","Dylan","Devin","Jayden","Ashton","Avery","Blair","Brett","Chandler","Kendall","Lane","Morgan","Perry","Parker","Peyton","Quinn","Raegan","Reese","Shayne","Skylar","Spencer","Sydney","Alex","Danny","Kelley","Ashley","Sam","Jesse","Jessie","Kyle","Dakota","Shawn","Sean","Blake","Brooke","Casey","Hayden","Jaden","Avery","Bailey","Carson","Drew","Kennedy"]
    if sex == "male":
        male_names = ["Nicolas","Bernardo","Maximiliano","Matias","Vicente","Elijah","Jeronimo","Jacob","Davi","Antonio","Josiah","James","Ryan","Felipe","Omar","Yassin","Moshe","Andres","Felipe","Abdallah","Logan","Tomas","Charles","Jesus","Pierre","Diego","Jaden","Santiago","Mohamed","Habib","Benjamin","Jack","Deven","Hassan","Peter","George","Carter","Liam","Oliver","Benjamin","Diego","Alejandro","Khaled","Jackson","Samuel","Liam","Mark","Ethan","Richard","Ishaan","Benjamin","Juan","Ibrahim","Selim","Adrian","Kirollos","Juan","Sebastian","Jaxson","Beshoi","Mamadou","Suraj","Stevenson","Abdel-Rahman","David","Mohammed","Alexis","Arthur","Hussein","Manuel","William","Rafael","Hamza","Miguel","angel","Carter","Angel","Matheus","Tareq","Owen","Martin","Ethan","Arnav","Bautista","Mahmoud","Peterson","Thiago","Ricardo","Wilson","Jameson","Joseph","William","Juan","Andres","Fadi","Mohamed","Santiago","Juan","David","Iker","Jack","Daniel","Alejandro","Heitor","Liam","Nathan","Jose","Lukas","Fabian","Dyllan","Karim","Olivier","Amir","Halim","Logan","Robert","Neil","Aiden","Sebastian","Emmanuel","Muhammad","Juan","Jose","Santino","Ian","Kevin","Keven","Hunter","Liam","Jason","Ajani","Felix","Daniel","Ali","Jeremiah","Mehdi","Alonso","Samuel","Bilal","Youssef","Aryan","Armaan","Luis","Alexander","Jayden","Dylan","Ahmed","Javier","Michael","Justin","Gabriel","Noah","Liam","Joaquin","Miguel","Taha","Cesar","Carlos","Samuel","Ramon","Joshua","Nikhil","Thomas","Murad","Noah","Mina","Mustafa","Mateo","Logan","Alejandro","Stanley","Evens","Liam","Eric","Pedro","Rohan","Lucas","Jaxon","Hudson","Mason","Oliver","Agustin","Martin","John","Matthew"]
        name_selection = male_names + unisex_names
        choice = random.choice(name_selection) + " " + random.choice(name_selection)
        return choice
    elif sex == "female":
        female_names = ["Tiare", "Hinano", "Poema", "Maeva", "Hina", "Vaea", "Titaua", "Moea", "Moeata", "Tarita", "Titaina", "Teura", "Heikapu", "Mareva", "Shaimaa", "Fatma", "Maha", "Reem", "Farida", "Aya", "Shahd", "Ashraqat", "Sahar", "Fatin", "Dalal", "Doha", "Fajr", "Suha", "Rowan", "Hosniya", "Hasnaa", "Hosna", "Gamila", "Gamalat", "Habiba", "Mary", "Marie", "Mariam", "Marina", "Irene", "Malak", "Habiba", "Hana", "Farah", "Marwa", "Nada", "Salma"]
        name_selection = female_names + unisex_names
        choice = random.choice(name_selection) + " " + random.choice(name_selection)
        return choice
    else:
        print("Sex not male nor female.")
        raise TypeError

def choose_profession():
    professions = ["None"]
    choice = random.choice(professions)
    return choice

def choose_age(minAge, maxAge):
    minAge = int(minAge)
    maxAge = int(maxAge)
    choice = random.randint(minAge, maxAge)
    return str(choice)

def choose_sex():
    chance = random.randint(0,1)
    if chance == 1:
        return "male"
    else:
        return "female"

def main():
    charSex = choose_sex()
    charName = choose_name(charSex)
    charProfession = choose_profession()
    charAge = choose_age(14,60)
    print("Sex: " + charSex + "\nName: " + charName + "\nProfession: " + charProfession + "\nAge: " + charAge)

if __name__ == "__main__":
    main()
