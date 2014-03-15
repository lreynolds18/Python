import urllib.request

def tips_to_counter(champion):
    """
    Uses the website lolcounter to find information
    prints tips to counter the champion
    prints who the champion is bad and good against
    """            
    web_obj = urllib.request.urlopen('http://www.lolcounter.com/champ/'+champion)
    tip_parse = str(web_obj.read())
    web_obj.close()

    tips = tip_parse[tip_parse.find("Counter Tips")+66:tip_parse.find("</td>            </table>")]
    tips = tips.split('</td><tr><td>')
    for tip in tips:
        if tip.count("'") > 0:
            ellepis_location = []
            count = 0
            while True:
                loc, count = tip.find("'", count), tip.find("'", count)+1
                if loc == -1: break
                ellepis_location.append(loc)
            index = tips.index(tip)
            for loc in ellepis_location:
                tip = tip[:loc-1]+tip[loc:]
            tips[index] = tip

def bad_against(champion):
    """
    prints four champs that the champion is bad against.
    """
    web_obj = urllib.request.urlopen('http://www.lolcounter.com/champ/'+champion)
    parse = str(web_obj.read())
    web_obj.close()
    print('OUI')
    
    bad_against = parse[parse.find("is Bad against"):parse.find('">General</span>')]
    print(bad_against)

def name_alterator(champion):
    if ' ' in champion:
        if '.' in champion:
            return 'drmundo'
        else:
            first, second = champion.lower().split()
            return first+second
    elif "'" in champion:
        champion = champion[:champion.find("'")]+champion[champion.find("'")+1:]
        return champion.lower()
    else:
        return champion.lower()

def main():
    home_page = urllib.request.urlopen('http://www.lolcounter.com')
    results = str(home_page.read())
    home_page.close()
    results = results[results.find("var champList")+17:results.find("}];  \n")].split(',{')

    Champions = []
    for line in results:
        line = line[line.find(':')+2:line.find('",')]
        if "'" in line:
            line = line[:line.find("'")-1]+line[line.find("'"):]
        Champions.append(line)

    print(Champions)

    special_cases = {'j4': 'Jarvan IV', 'ez': 'Ezreal', 'blitz': 'Blitzcrank', 'cait': 'Caitlyn', 'heimer': 'Heimerdinger',\
                     'donger': 'Heimerdinger', 'kass': 'Kassadin', 'LB': 'LeBlanc', 'TF': 'Twisted Fate', 'mundo': 'Dr. Mundo',\
                     'yi': 'Master Yi', 'ali': 'Alistar', 'trist': 'Tristana', 'morde': 'Mordekaiser', 'dr mundo': 'Dr. Mundo', 'voli': 'Volibear'}
        
    while True:
        selection = input("Select a champion (q to quit):")
        if selection.lower() == 'q' or selection.lower() == 'quit': break
        elif selection.title() in Champions: # three char same tf and twitch, ignoring for now.
            bad_against(name_alterator(selection))
 #           counters(selection.title())
        elif selection.lower() in special_cases.keys():
            print(name_alterator(special_cases[selection.lower()]))
            # counters(special_cases[selection.lower()])
        elif selection.title() in [champ[:3] for champ in Champions]:
            name = [champ for champ in Champions if champ[:3] == selection.title()][0]
            print(name_alterator(name))
            # counters(name)
        else:
            print("Invalid Input")

main()
