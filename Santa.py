import random, time


def dict_maker():
    players = input("Wprowadź imię uczestnika naszej małej gry... (Aby przejść do dalszej części w wpisz q) \n")
    parents = {}
    if players != "q" or "Q":
        count = 0
        parents[count] = players
    while players != "q":
        players = input("Wprowadź kolejnego uczestnika: \n")
        count = count + 1
        if players == "q" and "Q":
            return parents
        else:
            parents[count] = players
            continue


parents = dict_maker()

kiddos = parents


def randomize_dicts():
    kids = {k: kiddos[k] for k in random.sample(list(kiddos.keys()), len(kiddos))}
    return kids


kids = randomize_dicts()

def print_results():
    print(parents.values())
    print("Daje prezenty")
    print(kids.values())


print_results()

time.sleep(60)


