##################################################################
#  Section 10
#  Computer Project #11
##################################################################
#  Project Overview:
#       Make a game based of the Dilbert cartoon.
#       Player enters a number where they want their hook at.
#       Time limit goes and player catches a fish if the hook number and fish number align.

import random, math, turtle, urllib.request

##################################################################
## Class GameBoard
##################################################################

class GameBoard( object ):

    def __init__( self, squares_i=49, hook_location=1, speed=0, fish_list=None ):
        """
        Initializes the variables: squares, fish_list, fish_count, speed, and hook.
        Parameters have default variables.
        Returns nothing.
        """
        if fish_list == None: # in case urllib doesn't work correctly.
            self.__fish_list = [' Magikarp', ' Gyardos', ' Tynamo', ' Huntail', ' Lapras']
        else:
            self.__fish_list = fish_list
        # numinput and if statement does the error checking.
        self._fish_count = 0 
        self.__hook = int(hook_location)
        self.__squares = int(squares_i)
        self.__speed = int(speed)
                
    def __repr__( self ):
        """
        Returns a representation of the gameboard variables
        __str__ would call this, if repr had any value.
        """
        return "Gameboard Variables: Size:{:}, Squares:{:}, HL:{:}, FC:{:}".format(self.__board_size, self.__squares, self.__hook, self.__fish_count)

    def variables( self ):
        """
        Return: Squares, hook, fish_list, fish_count, speed
        """
        return self.__squares, self.__hook, self.__fish_list, self._fish_count, self.__speed
        
    
    def fish_count_update( self ):
        """
        This method is used to add one to fish count
        Return: Fish Count
        """
        self._fish_count += 1
        return self._fish_count

    def speed_update_i( self ):
        """
        Makes fish appear slower when called.
        Returns: None
        """
        if self.__speed != 10:
            self.__speed += 1
            self.time()
        
    def speed_update_d( self ):
        """
        Makes fish appear faster when called.
        Returns: None
        """
        if self.__speed != 0:
            self.__speed -= 1
            self.time()
        
    def time( self ):
        """
        Determines how long the game lasts.
        Returns: timer_len
        """
        if self.__speed == 0:
            self._timer_len = 0
        if self.__speed > 0 and self.__speed <= 4:
            self._timer_len = self.__speed * random.randint(1,100)
        elif self.__speed >= 5 and self.__speed < 6:
            self._timer_len = self.__speed * random.randint(100,300)
        elif self.__speed >= 7 and self.__speed < 10:
            self._timer_len = self.__speed * random.randint(300,3000)
        else:
            self._timer_len = self.__speed * random.randint(3000,10000)

    def timer_len( self ):
        """
        timer_len is a variable
        if timer_len isn't define it creates a new one.
        """
        try:
            return self._timer_len
        except AttributeError:
            self.time()
            return self._timer_len
        

def create_fish_list():
    """
    Uses urllib to go to website that has water pokemon
    Goes through the html code to find the pokemon names
    Adds a space and if the name starts with a vowel it adds a n
    The list doesn't include starter pokemon.
    Some protection in case it fails to work.
    Parameters: None
    Returns: A list of water pokemon, specifically 108.
    """
    
    try:
        web_obj = urllib.request.urlopen("http://pokemondb.net/type/water")
        result_str = str(web_obj.read())
        web_obj.close()

        result_str = result_str[result_str.find("/pokedex/"):]
        result_lst = result_str.split("<a href")
        
        pokemon = []
        for string in result_lst:     ## adds the strings that have pokemon in them in.
            if "/pokedex/" in string:
                pokemon.append(string)

        pokemon = pokemon[9:] # Gets rid of starter pokemon and titles
        pokemon_fishing_lst = []

        for pokemon_name in pokemon:
            name = pokemon_name[pokemon_name.find("/", 4)+1:]
            name = name[:name.find(' ')-1].capitalize()
            if name in ["Marshtomp", "Swampert", "Mudkip", "Totodile",\
                        "Croconaw", "Feraligatr", "Froakie", "Frogadier", "Greninja"]: continue
            if name[:1] in "AEIOU": # adds a space and a n to fix grammar
                name = "n "+name
            else:
                name = " "+name
            pokemon_fishing_lst.append(name)
            
        if len(pokemon_fishing_lst) < 70:
            return None
        
        return pokemon_fishing_lst
    except OSError:
        pass
    
def instructions():
    """
    Creates the first screen in a turtle window.
    Writes the instructions in the background.
    Prompts the user for Squares, Fishing Location, and Hook Location
    Assumes the user wants to enter correct numbers.
    Resets screen after.
    Parameters: None
    Returns: squares_int, fishing_location, hook_location
    """
    turtle.title("")
    turtle.bgcolor((.96, .96, .96))
    pen.up()
    pen.goto(0, 100)
    pen.write("Welcome to Carpet Fishing:", align="center", font=("Arial", 20, "normal"))
    pen.pencolor("red")
    pen.goto(0, 80)
    pen.write("Pokemon Black and White Edition", align="center", font=("Arial", 17, "bold"))
    pen.pencolor("black")
    pen.goto(0, 50)
    pen.write("Instructions:", align="center", font=("Arial", 18, "normal"))
    y_cord = 25 
    instruction_list = ["Enter a perfect square which will be used to divide the cubicle.",\
                        "Select where to place the hook",\
                        "Select the rate that fish appear.",\
                        "Left Arrow Key to make fish appear faster.",\
                        "Right Arrow Key to make fish appear slower.",\
                        "Press Q to quit or Exit out of the screen."]
    
    for writing in instruction_list:
        pen.up()
        pen.goto(0, y_cord)
        pen.write(writing, align="center", font=("Arial", 15, "normal"))
        y_cord -= 30

    while True: 
        try:
            number_of_squares = int(turtle.numinput("Number of Squares", "Pick a number (Preferably a Perfect Square)"))
            if type(number_of_squares) == int and number_of_squares > 0: break  
        except TypeError:
            continue
    while True:
        try:
            hook = turtle.numinput("Hook Location", "Place the hook in which box (1-{:})".format(int(number_of_squares)))
            if hook <= number_of_squares and hook > 0: break
        except TypeError:
            continue
    while True:
        try:
            speed = turtle.numinput("Game Length", "Speed that fish appear at. 0-10 scale (0 is the fastest and an effective demo, 10 is the Slowest)")
            if speed >= 0 and speed <= 10: break
        except TypeError:
            continue
    
    return int(number_of_squares), int(hook), int(speed)

def draw_square( length, width, color, cord, is_fill=False ):
    """
    Uses turtle graphics to draw a square
    Can handle filling the square with a color such as blue
    Can also handle drawing a black border
    Must start at cordinates its cordinates
    """
    pen.ht()
    pen.speed(0)
    pen.goto(cord)
    pen.down()
    if is_fill:
        pen.fillcolor(color)
        pen.begin_fill()
    else:
        pen.pencolor(color)
    pen.forward(width)
    pen.right(90)
    pen.forward(length)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(length)
    pen.right(90)
    pen.forward(width)
    if is_fill:
        pen.end_fill()
    pen.up()

def draw_lines( number, hook_number ):

    num = 1
    num_list = []
    prev_num = 0
    for num in range(1,number):
        multi1 = number/num
        if not multi1 >  int(multi1):
            num_list.append([num, int(multi1)])
            if len(num_list) > 2:
                if num_list[-1][::-1] in num_list and num_list[-1][0] != num_list[-1][1]:
                    num_list.pop()
                    break
        num += 1
    numbers = max(num_list)

    pen.ht()
    pen.speed(7)
    start_cord = [-250, 250]
    y_interval, x_interval = 500/numbers[0], 500/numbers[1]
    pen.up()
    pen.goto(start_cord)
    pen.pd()
    pen.seth(0)
    pen.forward(500)
    pen.up()
    pen.goto(start_cord)
    pen.pd()
    pen.seth(270)
    pen.forward(500)
    
    for i in range(1, numbers[0]+1):
        pen.up()
        start_cord[1] = start_cord[1] - y_interval
        pen.goto(start_cord)
        pen.pd()
        pen.seth(0)
        pen.forward(500)
    
    start_cord [1] = 250
    for i in range(1, numbers[1]+1):
        pen.up()
        start_cord[0] = start_cord[0] + x_interval
        pen.goto(start_cord)
        pen.pd()
        pen.seth(270)
        pen.forward(500)

    r = 0
    c = hook_number
    while True:
        if (c - numbers[1]) > 0:
            c -= numbers[1]
            r += 1
        else: break

    cord = [(-250 + (c * x_interval)), (250 - (r * y_interval))]
    pen.up()
    pen.goto(cord)
    draw_square(x_interval, y_interval, "gray", cord, True)

def draw_board( gameboard ):
    """
    Sets up the game board, green background and a blue 500x500 board
    Draws the squares that is requested
    Draws other information on the board -fish count, speed
    """
    turtle.bgcolor("green")
    pen.ht()
    pen.up()
    pen.goto(0, 300)
    pen.write("Carpet Fishing", align="center", font=("Arial", 20, "bold"))
    squares, hook, fish_list, fish_count, speed = gameboard.variables()
    pen.speed(0)
    draw_square(500, 500, (0.3, 0.35, 1.00), (-250, 250), True)
    draw_lines(squares, hook)

    pen.pencolor("black") # writes fish count
    pen.goto(300, 235)
    pen.write("Fish Count", align="center", font=("Arial", 15, "underline"))
    pen.goto(300, 215)
    pen.write(fish_count, align="center", font=("Arial", 15, "normal"))
    
    pen.goto(300, 195) # writes speed
    pen.write("Speed", align="center", font=("Arial", 15, "underline"))
    pen.goto(300, 175)
    pen.write(speed, align="center", font=("Arial", 15, "normal"))
    
    pen.goto(-300, 235) # writes water pokemon
    pen.write("Water", align="center", font=("Arial", 15, "normal"))
    pen.goto(-300, 215)
    pen.write("Pokemon", align="center", font=("Arial", 15, "normal"))
            
def generate_fish( gameboard ):
    """
    Uses the gameboard to make a list of variables
    Every times this is called it generates a random number between 1 and the number of squares
    If hook aligns with that number, it uses turtle graphics to display the fish name and updates the total fish count.
    Calls draw_square to draw a white box overtop of what's original there.
    """
    squares, hook, fish_list, fish_count, speed = gameboard.variables()
    fish_loc = random.randint(1, squares)
    if fish_loc == hook:
        pen.speed(0)
        pen.ht()
        fish_name = fish_list[random.randint(0, len(fish_list)-1)]
        pen.up()
        pen.pencolor("green")
        draw_square(100, 500, 'green', (-250, -270), True)
        pen.goto(0, -300)
        pen.pencolor("black")
        pen.write("You caught a" + fish_name + "!", align="center", font=("Arial", 20, "normal"))
        pen.pencolor("green")
        draw_square(20, 40, 'green', (280, 235), True)
        pen.goto(300, 215)
        pen.pencolor("black")
        pen.write(gameboard.fish_count_update(), align="center", font=("Arial", 15, "normal"))

def update_speed(speed):
    """
    When the player changes the speed
    Draws a box to clear the previous speed and writes the new speed
    Parameter: Speed, Return: None
    """
    pen.up()
    pen.ht()
    pen.pencolor("green")
    draw_square(20, 30, 'green', (290, 195), True)
    pen.goto(300, 175)
    pen.pencolor("black")
    pen.write(speed, align="center", font=("Arial", 15, "normal"))

def refresh_screen():
    """
    Parameters: None, Return: None
    Draws a green box around the bottom of the screen when fish haven't appeared in a while.
    """
    pen.up()
    pen.ht()
    pen.pencolor("green")
    draw_square(100, 500, 'green', (-250, -270), True)
    
def main():
    """
    Prints the instructions in turtle
    graphics and prompts the user for variables.
    Creates a gameboard with those variables
    Uses the gameboard to simiulate carpet fishing.
    Parameters:None
    Return:None
    """
    fish_list = create_fish_list()
    squares, hook, speed = instructions()
    A = GameBoard(squares, hook, speed, fish_list)
    
    pen.reset()
    draw_board(A)
    pen.ht()
    count = 1

    while True:
        turtle.onkey(quit, "q")
        turtle.onkey(quit, "Q")
        turtle.onkey(A.speed_update_i, "Right")
        turtle.onkey(A.speed_update_d, "Left") # Q to quit, Right/Left to adjust speed
        turtle.listen()
        
        a, b, c, d, speed1 = A.variables()
        if speed != speed1: # changes the speed info on the gui and the class
            speed = speed1
            update_speed(speed)
            count = 0
        if speed == 0:  # special case, rapidly produces fish
            generate_fish(A)
            continue
        
        if A.timer_len != 0:
            if count % A.timer_len() == 0:
                generate_fish(A)
                count = 0
                A.time()
        else:
            generate_fish(A)
            count = 0
            
        if count >= 300:
            refresh_screen()
        count += 1
        

       
pen = turtle.Turtle()
pen.speed(0)
pen.ht()
main()
