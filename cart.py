from tiles import *
import GUI
from time import sleep


class Cart:
    def __init__(self, spawning_tile: AbstractTile):
        self.act_tile = spawning_tile
        self.target_tile = spawning_tile
        self.movement_progress = 0

    def move(self, target_tile: AbstractTile):
        self.movement_progress = 0
        self.target_tile = target_tile
        velo = GUI.CART_VELO

        while self.movement_progress < 100:
            self.movement_progress += velo
            sleep(GUI.CYCLE_TIME)

        self.act_tile = self.target_tile



