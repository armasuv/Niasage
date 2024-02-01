import arcade,random        #On importe les librairies de random et arcade

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1080

COLORS = [arcade.color.AERO_BLUE, arcade.color.CAPRI, arcade.color.AUREOLIN, arcade.color.BRIGHT_GREEN]     #Liste pour lister les couleurs disponibles


class Ellipse:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_y = random.randint(-500, 500)
        self.change_x = random.randint(-500, 500)
        self.color = random.choice(COLORS)
        self.height = random.randint(50, 100)
        self.tilt_angle = random.randint(0, 180)
        self.width = random.randint(50, 100)
        self.num_segments = random.randint(3,8)

    def draw(self):
        arcade.draw_ellipse_filled(self.pos_x, self.pos_y, self.width, self.height, self.color, self.tilt_angle, self.num_segments)
    def update(self):           #Fonction pour udpate la position des balles
        self.pos_x += self.change_x
        self.pos_y += self.change_y

        if self.pos_x > SCREEN_WIDTH:
            self.change_x *= -1
        if self.pos_x < 0:
            self.change_x *= -1

        if self.pos_y > SCREEN_HEIGHT:
            self.change_y *= -1
        if self.pos_y < 0:
            self.change_y *= -1
class Balle:            #Une classe pour regrouper toutes les balles
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rayon = random.randint(10,20)
        self.change_y = random.randint(-5,5)
        self.change_x = random.randint(-5,5)
        self.color = random.choice(COLORS)
    def draw(self):      #Fonction pour dessiner des balles avec ces régulations
        arcade.draw_circle_filled(self.pos_x, self.pos_y, radius=self.rayon, color=self.color)
    def update(self):           #Fonction pour udpate la position des balles
        self.pos_x += self.change_x
        self.pos_y += self.change_y

        if self.pos_x > SCREEN_WIDTH:
            self.change_x *= -1
        if self.pos_x < 0:
            self.change_x *= -1

        if self.pos_y > SCREEN_HEIGHT:
            self.change_y *= -1
        if self.pos_y < 0:
            self.change_y *= -1
class Rectangle:        #Une classe pour regrouper tous les rectangles
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.change_y = random.randint(-5,5)
        self.change_x = random.randint(-5,5)
        self.color = random.choice(COLORS)
        self.height = random.randint(20,30)
        self.width = random.randint(5, 20)
        self.tilt_angle = random.randint(0,90)
    def draw(self):     #Fonction pour dessiner le rectangle avec ces régulations
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, color= self.color, tilt_angle=self.tilt_angle)
    def update(self):           #Fonction pour udpate la position des rectangles
        self.pos_x += self.change_x
        self.pos_y += self.change_y
        if self.pos_x > SCREEN_WIDTH:
            self.change_x *= -1
        if self.pos_x < 0:
            self.change_x *= -1

        if self.pos_y > SCREEN_HEIGHT:
            self.change_y *= -1
        if self.pos_y < 0:
            self.change_y *= -1
class MyGame(arcade.Window):        #Fonction pour qui contient le code du jeu principal
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.CADMIUM_RED)

        self.la_liste_balle = []        #Une liste pour contenir toutes les balles
        self.la_liste_rectangle = []
        self.la_liste_ellipse = []#une liste pour tous les rectangles
    print('Press space to change do dark mode.')
    def on_draw(self):
        arcade.start_render()

        for obj in self.la_liste_balle:
            obj.draw()

        for obj in self.la_liste_rectangle:
            obj.draw()
        for obj in self.la_liste_ellipse:
            obj.draw()
    def on_update(self, delta_time: float): #Une mise à jour de la position
        for obj in self.la_liste_balle:
            obj.update()
        for obj in self.la_liste_rectangle:
            obj.update()
        for obj in self.la_liste_ellipse:
            obj.update()

        arcade.set_background_color(random.choice(COLORS))

    def on_mouse_press(self, x, y, button, modifiers):  #Fonction qui détécte un appuie du boutton gauche de la souris
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.la_liste_balle.append(Balle(pos_x = x, pos_y = y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.la_liste_rectangle.append(Rectangle(pos_x = x, pos_y = y))
    def on_key_press(self, symbol: int, modifiers: int): #Fonction qui détécte un appuie du boutton gauche de la souris
        if symbol == arcade.key.SPACE:
            arcade.set_background_color(arcade.color.BLACK)
    def on_key_release(self, symbol: int, modifiers: int):#Fonction qui détécte un appuie du boutton space du keyboard
        if symbol == arcade.key.SPACE:
            arcade.set_background_color(arcade.color.CADMIUM_RED)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.la_liste_ellipse.append(Ellipse(pos_x=x, pos_y=y))
def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()
main()