def choose_name(sex):
    if sex == "male":
        return NotImplementedError
    elif sex == "female":
        return NotImplementedError
    else:
        print("Sex not male nor female.")
        raise TypeError

def choose_profession():
    raise NotImplementedError

def choose_age(minAge, maxAge):
    raise NotImplementedError

def choose_sex():
    chance = random.randint(0,1)
    if chance = 1:
        return "male"
    else:
        return "female"

def main():
    charSex = choose_sex()
    charName = choose_name(charSex)
    charProfession = choose_profession()
    charAge = choose_age(random.randint(14,60),random.randint(14,60))
    raise NotImplementedError

if __name__ == "__main__":
    main()
