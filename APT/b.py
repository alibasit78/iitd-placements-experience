class Platformer:
    def __init__(self, n, x):
        """
        :param n: (int) The initial number of tiles.
        :param x: (int) The initial position of the character.
        """
        self.pos = x
        # self.tiles = [i for i in range(n)]
        self.lefts = [i - 1 for i in range(n)]
        self.rights = [i + 1 for i in range(n)]

    def jump_left(self):
        self.rights[self.lefts[self.pos]] = self.rights[self.pos]
        self.lefts[self.rights[self.pos]] = self.lefts[self.pos]
        self.pos = self.lefts[self.lefts[self.pos]]

        # self.tiles.remove(self.tiles[self.pos])
        # self.pos = self.pos - 2

    def jump_right(self):
        self.rights[self.lefts[self.pos]] = self.rights[self.pos]
        self.lefts[self.rights[self.pos]] = self.lefts[self.pos]
        self.pos = self.rights[self.rights[self.pos]]
        # self.tiles.remove(self.tiles[self.pos])
        # self.pos = self.pos + 1

    def position(self):
        """
        :returns: (int) The position of the character.
        """
        # print(self.tiles)
        return self.pos


platformer = Platformer(6, 3)
print(platformer.position())
platformer.jump_left()
print(platformer.position())
platformer.jump_right()
print(platformer.position())
