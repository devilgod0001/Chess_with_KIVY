import kivy
# import pygame
import itertools

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.graphics import RoundedRectangle, Color, PushMatrix, PopMatrix, Ellipse

from mainvars import per_block_side, board_array, grid_box_array, grid_box_shrink, window_back_color, w, h, per_image_side, current_positions

b, h = w, h

my_side = 'W' #'W' or 'B', white or black

Builder.load_file("main.kv")
Builder.load_file("chess_board.kv")
Builder.load_file("maingoti.kv")

all_gridboxes = []

class Mainmenu(Screen):
    pass

class Gamescreen(Screen):
    pass

class Clickable_char(FloatLayout):
    def __init__(self, **kwargs):
        super(Clickable_char, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            positions = self.give_positions_with_danger(self.pos, self.name, 'W')
            with self.canvas.after:
                PushMatrix()
                Color(rgba=(1,1,1,1))
                for pos in positions[1]:
                    Ellipse(size=(35, 35), pos=grid_box_array[pos[0]][pos[1]])
                PopMatrix()

    def get_index_from_pos(self, pos):
        for i,j in zip(board_array,range(8)):
            if pos in i:
                current = [j,i.index(pos)]
                break
        return current
        

    def give_positions_with_danger(self, pos, name, my_side, execution='complete'):
        '''pos must be real_coordinate_positions'''
        '''pos must be list, not tuple'''
        '''return positions --> [[enemy],[moves],[danger]]'''

        danger = []

        current = self.get_index_from_pos(pos)
        
        if name[len(name)-4:len(name)]=='King':
            positions = self.get_KING_positions(current, my_side)
        elif name[len(name)-5:len(name)]=='Queen':
            positions = self.get_QUEEN_positions(current, my_side)
        elif name[len(name)-6:len(name)]=='Bishop':
            positions = self.get_BISHOP_positions(current, my_side)
        elif name[len(name)-4:len(name)]=='Rook':
            positions = self.get_ROOK_positions(current, my_side)
        elif name[len(name)-6:len(name)]=='Knight':
            positions = self.get_KNIGHT_positions(current, my_side)
        else:
            positions = self.get_PAWN_positions(current, my_side, self.first_move)

        # if execution=='complete':
        #     all_movables = {}
        #     oppst_name = list(current_positions.keys())[16:31] if my_side=='W' else list(current_positions.keys())[0:15]
        #     for name_ in oppst_name[0:8]:
        #         oppst_pos = current_positions[name_]
        #         oppst_movable_pos = self.give_positions_with_danger(oppst_pos,name_,'B',execution='half')
        #         all_movables[name] = oppst_movable_pos[1]
        #     for name_ in oppst_name[8:16]:
        #         oppst_pos = current_positions[name_]
        #         oppst_pos = self.get_index_from_pos(oppst_pos)
        #         oppst_movable_pos = self.get_PAWN_positions(oppst_pos,'B',False ,for_my_side=False)
        #         all_movables[name] = oppst_movable_pos[1]
        #     pos_in_danger = []
        #     for _name in all_movables.keys():
        #         for posns in positions[1]:
        #             if posns in all_movables[_name]:
        #                 danger.append(posns)
        #                 pos_in_danger.append(positions[1].index(posns))
        #     pos_in_danger = list(dict.fromkeys(pos_in_danger))
        #     for i in pos_in_danger:
        #         positions[1].pop(i)
        #     positions.append(danger)
        #     return positions

        return positions



    def get_KNIGHT_positions(self, current, my_side):
        '''current must be list of index (y,x)'''
        '''return [enemy, moves]'''
        moves = []
        enemy = []
        
        for i in [1,-1,2,-2]:
            primary1 = [current[0]+i, current[1]+(2 if abs(i)==1 else 1)]
            primary2 = [current[0]+i, current[1]+(-2 if abs(i)==1 else -1)]
            for i in [primary1, primary2]:
                if 0<=i[0]<=7 and 0<=i[1]<=7:
                    real_pos = board_array[i[0]][i[1]]
                    if real_pos not in list(current_positions.values()):
                        moves.append(i)
                    else:
                        name_index = list(current_positions.values()).index(real_pos)
                        if list(current_positions.keys())[name_index][0]!=my_side:
                            enemy.append(i)
        return [enemy, moves]

    def get_BISHOP_positions(self, current, my_side):
        '''current:list of index (y,x)'''
        '''return [enemy, moves]'''
        moves = []
        enemy = []

        bq45 = min(8-current[0],8-current[1])
        bq135 = min(8-current[0],current[1]+1)
        bq225 = min(current[0]+1,current[1]+1)
        bq315 = min(current[0]+1,8-current[1])
        a = {'a':1,'b':bq45,'c':1,'p':1,'q':bq45,'r':1}
        b = {'a':1,'b':bq135,'c':1,'p':-1,'q':-bq135,'r':-1}
        c = {'a':-1,'b':-bq225,'c':-1,'p':-1,'q':-bq225,'r':-1}
        d = {'a':-1,'b':-bq315,'c':-1,'p':1,'q':bq315,'r':1}

        for p in [a,b,c,d]:
            for y,x in zip(range(p['a'],p['b'],p['c']),range(p['p'],p['q'],p['r'])):
                next_pos = [current[0]+y, current[1]+x]
                real_pos = board_array[next_pos[0]][next_pos[1]]
                if real_pos not in list(current_positions.values()):
                    moves.append(next_pos)
                else:
                    name_index = list(current_positions.values()).index(real_pos)
                    if list(current_positions.keys())[name_index][0]!=my_side:
                        enemy.append(next_pos)
                        break
                    else:
                        break
        return [enemy, moves]

    def get_ROOK_positions(self, current, my_side):
        '''current:list of index (y,x)'''
        '''return [enemy, moves]'''
        moves = []
        enemy = []

        deg0 = zip(itertools.repeat(0,7-current[1]),range(1,8-current[1],1))
        deg90 = zip(range(1,8-current[0],1),itertools.repeat(0,7-current[0]))
        deg180 = zip(itertools.repeat(0,current[1]),range(-1,-(current[1]+1),-1))
        deg270 = zip(range(-1,-(current[0]+1),-1),itertools.repeat(0,current[0]))

        for p in [deg0,deg90,deg180,deg270]:
            for y,x in p:
                next_pos = [current[0]+y, current[1]+x]
                real_pos = board_array[next_pos[0]][next_pos[1]]
                if real_pos not in list(current_positions.values()):
                    moves.append(next_pos)
                else:
                    name_index = list(current_positions.values()).index(real_pos)
                    if list(current_positions.keys())[name_index][0]!=my_side:
                        enemy.append(next_pos)
                        break
                    else:
                        break
        return [enemy, moves]

    def get_QUEEN_positions(self, current, my_side):
        '''current:list of index (y,x)'''
        '''return [enemy, moves]'''
        '''first bishop then rook'''
        moves = []
        enemy = []

        bishop = self.get_BISHOP_positions(current, my_side)
        rook = self.get_ROOK_positions(current, my_side)
        for p in [bishop, rook]:
            for i in p[0]:
                enemy.append(i)
            for j in p[1]:
                moves.append(j)
        return [enemy, moves]

    def get_KING_positions(self, current, my_side):
        '''current:list of index (y,x)'''
        '''return [enemy, moves]'''
        moves = []
        enemy = []
        
        x = itertools.combinations([1,0,-1,1,0,-1],2)
        x = list(dict.fromkeys(x))
        x.pop(x.index((0,0)))
        for y,x in x:
            next_pos = [current[0]+y, current[1]+x]
            if 0<=next_pos[0]<=7 and 0<=next_pos[1]<=7:
                real_pos = board_array[next_pos[0]][next_pos[1]]
                if real_pos not in list(current_positions.values()):
                    moves.append(next_pos)
                else:
                    name_index = list(current_positions.values()).index(real_pos)
                    if list(current_positions.keys())[name_index][0]!=my_side:
                        enemy.append(next_pos)

        return [enemy, moves]

    def get_PAWN_positions(self, current, my_side, first_move, for_my_side=True):
        '''current:list of index (y,x)'''
        '''return [enemy, moves]'''

        moves = []
        enemy = []

        next_move = [current[0]+1, current[1]]
        if 0<=next_move[0]<=7 and 0<=next_move[1]<=7:
            real_pos = board_array[next_move[0]][next_move[1]]
            if real_pos not in list(current_positions.values()):
                moves.append(next_move)
        
        if first_move:
            next_move = [current[0]+2, current[1]]
            if 0<=next_move[0]<=7 and 0<=next_move[1]<=7:
                real_pos = [board_array[next_move[0]],board_array[next_move[1]]]
                if real_pos not in list(current_positions.values()):
                    moves.append(next_move)
        for y,x in [(1,1),(1,-1)] if for_my_side else [(-1,-1),(-1,1)]:
            next_move = [current[0]+y, current[1]+x]
            if 0<=next_move[0]<=7 and 0<=next_move[1]<=7:
                real_pos = [board_array[next_move[0]],board_array[next_move[1]]]
                if real_pos in list(current_positions.values()):
                    name_index = list(current_positions.values()).index(real_pos)
                    if list(current_positions.keys())[name_index][0]!=my_side:
                        enemy.append(next_move)
        return [enemy, moves] if for_my_side else [moves, enemy]

class ChessBoard(FloatLayout):
    def __init__(self, **kwargs):
        super(ChessBoard, self).__init__(**kwargs)

        side = per_block_side
        for i in range(8):
            for j in range(8):
                grd_btn = GridButton(size_hint=(None, None), size=[
                                     side, side], pos=grid_box_array[i][j])
                all_gridboxes.append(grd_btn)
                self.add_widget(grd_btn)


class GridButton(RelativeLayout):
    def __init__(self, **kwargs):
        super(GridButton, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.anim_bloop()

    def anim_bloop(self):
        new_x = self.pos[0] + grid_box_shrink/2
        new_y = self.pos[1] + grid_box_shrink/2
        new_w = self.width - grid_box_shrink
        new_h = self.height - grid_box_shrink
        anim = Animation(pos=[new_x, new_y], size=[new_w, new_h], duration=0.1)

        old_x = new_x - grid_box_shrink/2
        old_y = new_y - grid_box_shrink/2
        old_w = new_w + grid_box_shrink
        old_h = new_h + grid_box_shrink
        anim += Animation(pos=[old_x, old_y],
                          size=[old_w, old_h], duration = 0.1, transition="out_back")
        anim.start(self)


screenmanager = ScreenManager(transition=NoTransition())

screenmanager.add_widget(Gamescreen(name='Gamescreen'))

screenmanager.add_widget(Mainmenu(name='Mainmenu'))

class Clean_ChessApp(App):
    def build(self):
        return screenmanager


if __name__ == "__main__":
    Window.size = (b, h)
    Window.clearcolor = get_color_from_hex(window_back_color)
    Clean_ChessApp().run()
