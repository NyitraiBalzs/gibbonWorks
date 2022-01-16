import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import AnimateTiles, Coin, Tiles, StaticTiles, Crate, Palm
from enemy import Enemy


class Level:
    def __init__(self, level_data, surface):
        #player setup
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)
        #general seutp
        self.display_surface = surface
        self.world_shift = -4
        #terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
        #grass setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')
        #crates setup
        crates_layout = import_csv_layout(level_data['crates'])
        self.crates_sprites = self.create_tile_group(crates_layout, 'crates')
        #coins setup
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout, 'coins')
        #foreground palm trees steup
        fg_palm_layout = import_csv_layout(level_data['fg_palms'])
        self.fg_palms_sprites = self.create_tile_group(fg_palm_layout, 'fg_palms')
        #backgroun palm trees setup
        bg_palm_layout = import_csv_layout(level_data['bg_palms'])
        self.bg_palms_sprites = self.create_tile_group(bg_palm_layout, 'bg_palms')
        #enemy setup
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')
        #constraints setup
        constrain_layout = import_csv_layout(level_data['constraints'])
        self.constrain_sprites = self.create_tile_group(constrain_layout, 'constraints')


    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = tile_size * col_index
                    y = tile_size * row_index

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(col)]
                        sprite = StaticTiles(tile_size,x,y, tile_surface)

                    if type == 'grass':
                        grass_tile_list = import_cut_graphics('/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(col)]
                        sprite = StaticTiles(tile_size, x, y, tile_surface)
                        
                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)

                    if type == 'coins':
                        silver = 'silver'
                        gold = 'gold'
                        if col == '0':
                            sprite = Coin(tile_size, x, y, f'/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/coins/{gold}/')
                        if col == '1':
                            sprite = Coin(tile_size, x, y, f'/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/coins/{silver}/')
                    if type == 'fg_palms':
                        if col == '0':
                            sprite = Palm(tile_size, x, y,'/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/terrain/palm_small/', 38)
                        if col == '1':sprite = Palm(tile_size, x, y,'/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/terrain/palm_large/', 64)

                    if type == 'bg_palms':
                         sprite = Palm(tile_size, x, y,'/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/terrain/palm_bg/', 64)

                    if type == 'enemies':
                        sprite = Enemy(tile_size, x, y)
                    
                    if type == 'constraints':
                        sprite = Tiles(tile_size,x,y)
                    sprite_group.add(sprite)
        return sprite_group
    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites:
            if pygame.sprite.spritecollide(enemy, self.constrain_sprites, False):
                enemy.reverse()
    
    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = tile_size * col_index
                y = tile_size * row_index
                if col == '0':
                    print('player spawn')
                if col == '1':
                    hat_surface = pygame.image.load('/home/nyitrai/Projects/gibbonWorks/OOP-GamePy_practise/GamePy_practise/graphics/character/hat.png').convert_alpha()
                    sprite = StaticTiles(tile_size,x,y,hat_surface)
                    self.goal.add(sprite)
    def run(self):

        #display background palms
        self.bg_palms_sprites.update(self.world_shift)
        self.bg_palms_sprites.draw(self.display_surface)

        # display terrain
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)

        #display enemy
        self.enemy_sprites.update(self.world_shift)
        self.constrain_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)

        #display crates
        self.crates_sprites.update(self.world_shift)
        self.crates_sprites.draw(self.display_surface)


        #display grass
        self.grass_sprites.draw(self.display_surface)
        self.grass_sprites.update(self.world_shift)

        #display coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)

        #display foreground palms
        self.fg_palms_sprites.update(self.world_shift)
        self.fg_palms_sprites.draw(self.display_surface)

        #player sprites
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

