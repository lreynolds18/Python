import random

try:
    file = open("verb.txt", "r+")
except IOError:
    quit()
except FileNotFoundError:
    quit()

master_dict = {}
for line in file:
    temp = line.split(":\t[")
    temp[1] = temp[1].rstrip("]\n")
    temp[1] = temp[1].split("', '")
    temp[1][0] = temp[1][0].strip("'")
    temp[1][6] = temp[1][6].strip("'")
    master_dict[temp[0]] = temp[1]
file.close()

master_list_keys = list(master_dict.keys())
pronouns = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]
menu_list = ["Look up a verb conjugation", "Look up the verb conjugation for a noun/pronoun", "Look up all -er verbs", "Look up all -re verbs", "Look up all -ir verbs", "Look up the definition of a verb", "Random Verb"] 

def which_pronoun(pronoun):
    if pronoun == pronouns[0]: return 0;
    if pronoun == pronouns[1]: return 1;
    if pronoun == pronouns[2] or pronoun == pronouns[3] or pronoun == pronouns[4]: return 2;
    if pronoun == pronouns[5]: return 3;
    if pronoun == pronouns[6]: return 4;
    if pronoun == pronouns[7] or pronoun == pronouns[8]: return 5;
    else: return print("something is really messed up")

def all_of_the_same_verb(ending):
    verbs_ending_in = []
    for i in range(len(master_list_keys)):
        if master_list_keys[i][-2:] == ending:
            verbs_ending_in.append(master_list_keys[i])
    return verbs_ending_in


while True:
    print("What would you like to do:")
    for i in range(1, len(menu_list)+1):
        print(str(i)+':', menu_list[i-1])
    print("Press Q to quit")
    menu_choice = input('>')
    if menu_choice.lower() == 'q': break

    if menu_choice == '1':
        while True:
            try:
                ask_verb = input("Which verb (Q returns to the menu): ")
                if ask_verb.lower() in master_dict.keys():
                    print("\nThe conjugation for", ask_verb, "is:")
                    print("   Je", master_dict[ask_verb][0])
                    print("   Tu", master_dict[ask_verb][1])
                    print("   Il/Elle/On", master_dict[ask_verb][2])
                    print("   Nous", master_dict[ask_verb][3])
                    print("   Vous", master_dict[ask_verb][4])
                    print("   Ils/Elles", master_dict[ask_verb][5]+"\n")
                    break
                if ask_verb.lower() == 'q': break
            except ValueError: continue
            
    if menu_choice == '2':
        while True:
            try:
                ask_verb = input("Which verb (Q returns to the menu): ")
                ask_verb = ask_verb.lower()
                if ask_verb in master_dict.keys(): break
                if ask_verb == 'q': break
            except ValueError:
                continue
        while True:
            try:
                if ask_verb == 'q': break
                ask_noun = input("Which noun/pronoun (Q returns to the menu): ")
                ask_noun = ask_noun.lower()
                if ask_noun in pronouns:
                    noun_int = which_pronoun(ask_noun)
                    print("\nThe conjugation of", ask_verb, "for", ask_noun, "is:")
                    print("   {:} {:}\n".format(ask_noun.capitalize(), master_dict[ask_verb][noun_int]))
                    break
                if ask_noun == 'q': break
            except ValueError:
                continue

    if menu_choice == '3':
        er_verbs = all_of_the_same_verb('er')
        print("All verbs ending in -er")
        for i in range(len(er_verbs)):
            print(er_verbs[i])

    if menu_choice == '4':
        re_verbs = all_of_the_same_verb('re')
        print("All verbs ending in -re")
        for i in range(len(re_verbs)):
            print(re_verbs[i])

    if menu_choice == '5':
        ir_verbs = all_of_the_same_verb('ir')
        print("All verbs ending in -ir")
        for i in range(len(ir_verbs)):
            print(ir_verbs[i])

    if menu_choice == '6':
        while True:
            try:
                ask_verb = input("Which verb (Q returns to the menu): ")
                ask_verb = ask_verb.lower()
                if ask_verb in master_dict.keys():
                    print("\n{:} means: {:}\n".format(ask_verb.capitalize(), master_dict[ask_verb][6].capitalize()))
                    break
                if ask_verb == 'q': break
            except ValueError:
                continue

    if menu_choice == '7':
        random_num = int(random.uniform(0, len(master_list_keys)))
        print("\nYour random verb is:", master_list_keys[random_num])
        print("   The definition is: {:}\n".format(master_dict[master_list_keys[random_num]][6].capitalize()))
