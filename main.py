import pyxel

from dataclasses import dataclass

pyxel.init(160, 160)
pyxel.load("resource.pyxres")

'''
TO-DO:
- Ayusin loading ng app (initialization)
- Ayusin ung bullet (icenter and sht)
- Ayusin qng anuman yung issue sa update vs draw :O (kasi rn they seem to do the same thing)

- Mga actual to-dos for the MP HAHAHAHA ^-^

[Karin] TO-DO 
- fix bullet
- retheme? >:)
- tilemap
'''

@dataclass
class Player:
    x = 10
    y = 10
    width = 20
    height = 20
    rot_x = 1
    rot_y = 1
    start = 0
    dir = 'N'
    bullet = None
    
    def move(self):
        if pyxel.btnp(pyxel.KEY_W, True, True):
            test = self.y - 5
            if not test < 0:
                self.y -= 5
                self.rot_y = 1
                self.start = 0
            self.dir = 'N'
        
        if pyxel.btnp(pyxel.KEY_A, True, True):
            test = self.x - 5
            if not test < 0:
                self.x -= 5
                self.rot_x = -1
                self.start = 16
            self.dir = 'W'
        
        if pyxel.btnp(pyxel.KEY_S, True, True):
            test = self.y + self.height + 5
            if not test > 160:
                self.y += 5
                self.rot_y = -1
                self.start = 0
            self.dir = 'S'
        
        if pyxel.btnp(pyxel.KEY_D, True, True):
            test = self.x + self.height + 5
            if not test > 160:
                self.x += 5
                self.rot_x = 1
                self.start = 16
            self.dir = 'E'
        
        pyxel.blt(self.x, self.y, 0, self.start, 0, 16*self.rot_x, 16*self.rot_y)

    def fire(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullet = Bullet(self.x, self.y, self.dir)

    def draw(self):
        self.move()
        self.fire()
        if self.bullet is not None:  
            self.bullet.move()
    
    def update(self):
        self.move()
    
class Bullet:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
    
    def move(self):
        print('run')
        match self.dir:
            case 'N':
                self.y -= 10
            
            case 'W':
                self.x -= 10
            
            case 'S':
                self.y += 10
            
            case 'E':
                self.x += 10
        
        pyxel.circ(self.x, self.y, 3, 6)

@dataclass
class Digmaan_City:
    player = Player()

class App:
    def __init__(self):
        self.screen_width = 160
        self.screen_height = 160
        self.state = Digmaan_City()
        pyxel.run(self.update, self.draw)
    
    def draw(self):
        self.state.player.draw()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        pyxel.cls(0)
        # self.state.player.update()

App()
