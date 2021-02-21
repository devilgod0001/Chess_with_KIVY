import kivy

from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.graphics import Color, PushMatrix, PopMatrix, Ellipse
from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import get_color_from_hex
from tryvars import b, h, posns, Default_Pos, Circle_color, Pos_man
# Not to do, NOTE:
'''  IMPORTING try1 WILL INITIALIZE ALL KIVY FUNCTIONS TWICE!  '''
# Double Screen Output!!!!!!!

el_width = ((b-(14+8))/8)
el_height = el_width
click_sound = SoundLoader.load("click-blip.mp3")

y_pad = (h-b)/2

soldiers = ["Soldier1", "Soldier2", "Soldier3", "Soldier4", "Soldier5", "Soldier6", "Soldier7", "Soldier8"]

class Clickable(RelativeLayout):
    selected = None
    def __init__(self, **kwargs):
        super(Clickable, self).__init__(**kwargs)
        

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if not self.selected:
                # click_sound.play()   '''  sound  '''
                self.select()
        elif self.tried_to_move(self.selected, touch.x, touch.y):
            new_pos = self.tried_to_move(self.selected, touch.x, touch.y)[1]
            self.animate_chart(new_pos)
            self.manage_posman(self.name, new_pos)
            self.unselect()
        else:
            self.unselect()

        return super(Clickable, self).on_touch_down(touch)
        
    
    def select(self):
        self.selected = []
        positions = self.get_movable_pos(self.name, self.pos)
        if positions:
            with self.canvas.after:
                PushMatrix()
                Color(rgba=get_color_from_hex(Circle_color))
                for pos_xy in positions:
                    if pos_xy:  #this is None filter
                        if posns[pos_xy[1]][pos_xy[0]] not in Pos_man: #If something not already there
                            p = Ellipse(size=(5, 5), pos=posns[pos_xy[1]][pos_xy[0]]) #Make Circle(Ellipse)
                            self.selected.append(p)  #only those come which have some value. None are thrown out.
                self.animate_circle(self.selected)
                PopMatrix()

    # def on_touch_up(self, touch):
    #     if self.selected:
    #         self.unselect()
    #         return True
    #     super(Clickable, self).on_touch_up(touch)

    def unselect(self):
        if self.selected:
            for circles in self.selected:
                self.canvas.after.remove(circles)
            self.selected = None

    def get_movable_pos(self, name, pos):
        global posns
        if name == "HorseL" or name == "HorseR":
            index_xy = self.get_index(pos)
            ''' Checking if new comming index value would not go out of range '''
            if index_xy:
                posindex1 = ([index_xy[0]+1, index_xy[1]+2] if (index_xy[0]+1)>=0 and (index_xy[1]+2)>=0 and (index_xy[0]+1)<8 and (index_xy[1]+2)<8 else None)
                posindex2 = ([index_xy[0]-1, index_xy[1]+2] if (index_xy[0]-1)>=0 and (index_xy[1]+2)>=0 and (index_xy[0]-1)<8 and (index_xy[1]+2)<8 else None)
                posindex3 = ([index_xy[0]+1, index_xy[1]-2] if (index_xy[0]+1)>=0 and (index_xy[1]-2)>=0 and (index_xy[0]+1)<8 and (index_xy[1]-2)<8 else None)
                posindex4 = ([index_xy[0]-1, index_xy[1]-2] if (index_xy[0]-1)>=0 and (index_xy[1]-2)>=0 and (index_xy[0]-1)<8 and (index_xy[1]-2)<8 else None)
                posindex5 = ([index_xy[0]+2, index_xy[1]+1] if (index_xy[0]+2)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]+2)<8 and (index_xy[1]+1)<8 else None)
                posindex6 = ([index_xy[0]+2, index_xy[1]-1] if (index_xy[0]+2)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]+2)<8 and (index_xy[1]-1)<8 else None)
                posindex7 = ([index_xy[0]-2, index_xy[1]+1] if (index_xy[0]-2)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]-2)<8 and (index_xy[1]+1)<8 else None)
                posindex8 = ([index_xy[0]-2, index_xy[1]-1] if (index_xy[0]-2)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]-2)<8 and (index_xy[1]-1)<8 else None)

                return posindex1, posindex2, posindex3, posindex4, posindex5, posindex6, posindex7, posindex8
        elif name == "King":
            index_xy = self.get_index(pos)

            if index_xy:
                posindex1 = ([index_xy[0]-1, index_xy[1]+1] if (index_xy[0]-1)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]-1)<8 and (index_xy[1]+1)<8 else None)
                posindex2 = ([index_xy[0]+0, index_xy[1]+1] if (index_xy[0]+0)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]+0)<8 and (index_xy[1]+1)<8 else None)
                posindex3 = ([index_xy[0]+1, index_xy[1]+1] if (index_xy[0]+1)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]+1)<8 and (index_xy[1]+1)<8 else None)
                posindex4 = ([index_xy[0]+1, index_xy[1]+0] if (index_xy[0]+1)>=0 and (index_xy[1]+0)>=0 and (index_xy[0]+1)<8 and (index_xy[1]+0)<8 else None)
                posindex5 = ([index_xy[0]-1, index_xy[1]+0] if (index_xy[0]-1)>=0 and (index_xy[1]+0)>=0 and (index_xy[0]-1)<8 and (index_xy[1]+0)<8 else None)
                posindex6 = ([index_xy[0]-1, index_xy[1]-1] if (index_xy[0]-1)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]-1)<8 and (index_xy[1]-1)<8 else None)
                posindex7 = ([index_xy[0]+0, index_xy[1]-1] if (index_xy[0]+0)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]+0)<8 and (index_xy[1]-1)<8 else None)
                posindex8 = ([index_xy[0]+1, index_xy[1]-1] if (index_xy[0]+1)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]+1)<8 and (index_xy[1]-1)<8 else None)

                return posindex1, posindex2, posindex3, posindex4, posindex5, posindex6, posindex7, posindex8

        elif name == "CamelL" or name == "CamelR":
            index_xy = self.get_index(pos)

            if index_xy:
                '''  45 degree  '''
                posindex1  = ([index_xy[0]+1, index_xy[1]+1] if (index_xy[0]+1)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]+1)<8 and (index_xy[1]+1)<8 else None)
                posindex2  = ([index_xy[0]+2, index_xy[1]+2] if (index_xy[0]+2)>=0 and (index_xy[1]+2)>=0 and (index_xy[0]+2)<8 and (index_xy[1]+2)<8 else None)
                posindex3  = ([index_xy[0]+3, index_xy[1]+3] if (index_xy[0]+3)>=0 and (index_xy[1]+3)>=0 and (index_xy[0]+3)<8 and (index_xy[1]+3)<8 else None)
                posindex4  = ([index_xy[0]+4, index_xy[1]+4] if (index_xy[0]+4)>=0 and (index_xy[1]+4)>=0 and (index_xy[0]+4)<8 and (index_xy[1]+4)<8 else None)
                posindex5  = ([index_xy[0]+5, index_xy[1]+5] if (index_xy[0]+5)>=0 and (index_xy[1]+5)>=0 and (index_xy[0]+5)<8 and (index_xy[1]+5)<8 else None)
                posindex6  = ([index_xy[0]+6, index_xy[1]+6] if (index_xy[0]+6)>=0 and (index_xy[1]+6)>=0 and (index_xy[0]+6)<8 and (index_xy[1]+6)<8 else None)
                posindex7  = ([index_xy[0]+7, index_xy[1]+7] if (index_xy[0]+7)>=0 and (index_xy[1]+7)>=0 and (index_xy[0]+7)<8 and (index_xy[1]+7)<8 else None)

                '''             Blocker Detector  '''
                pos1list = [posindex1, posindex2, posindex3, posindex4, posindex5, posindex6, posindex7]
                pos1listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos1list)) #get real position values
                blockers1 = list(filter(lambda x: x in pos1listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers1:#if blocker is found
                    blocker1 = min(blockers1) # min for this only# finds the nearest
                    blocker_index = pos1listreal.index(blocker1) #get new index

                    for i in range(blocker_index, len(pos1list)):
                        pos1list[i] = None
                

                
                
                

                '''  135 degree  '''
                posindex8  = ([index_xy[0]-1, index_xy[1]+1] if (index_xy[0]-1)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]-1)<8 and (index_xy[1]+1)<8 else None)
                posindex9  = ([index_xy[0]-2, index_xy[1]+2] if (index_xy[0]-2)>=0 and (index_xy[1]+2)>=0 and (index_xy[0]-2)<8 and (index_xy[1]+2)<8 else None)
                posindex10 = ([index_xy[0]-3, index_xy[1]+3] if (index_xy[0]-3)>=0 and (index_xy[1]+3)>=0 and (index_xy[0]-3)<8 and (index_xy[1]+3)<8 else None)
                posindex11 = ([index_xy[0]-4, index_xy[1]+4] if (index_xy[0]-4)>=0 and (index_xy[1]+4)>=0 and (index_xy[0]-4)<8 and (index_xy[1]+4)<8 else None)
                posindex12 = ([index_xy[0]-5, index_xy[1]+5] if (index_xy[0]-5)>=0 and (index_xy[1]+5)>=0 and (index_xy[0]-5)<8 and (index_xy[1]+5)<8 else None)
                posindex13 = ([index_xy[0]-6, index_xy[1]+6] if (index_xy[0]-6)>=0 and (index_xy[1]+6)>=0 and (index_xy[0]-6)<8 and (index_xy[1]+6)<8 else None)
                posindex14 = ([index_xy[0]-7, index_xy[1]+7] if (index_xy[0]-7)>=0 and (index_xy[1]+7)>=0 and (index_xy[0]-7)<8 and (index_xy[1]+7)<8 else None)



                pos2list = [posindex8, posindex9, posindex10, posindex11, posindex12, posindex13, posindex14]
                pos2listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos2list)) #get real position values
                blockers2 = list(filter(lambda x: x in pos2listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers2:#if blocker is found
                    blocker2 = max(blockers2, key = lambda x: x[1]) # min for this only# finds the nearest
                    blocker_index = pos2listreal.index(blocker2)

                    for i in range(blocker_index, len(pos2list)):
                        pos2list[i] = None




                '''  225 degree  '''
                posindex15 = ([index_xy[0]-1, index_xy[1]-1] if (index_xy[0]-1)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]-1)<8 and (index_xy[1]-1)<8 else None)
                posindex16 = ([index_xy[0]-2, index_xy[1]-2] if (index_xy[0]-2)>=0 and (index_xy[1]-2)>=0 and (index_xy[0]-2)<8 and (index_xy[1]-2)<8 else None)
                posindex17 = ([index_xy[0]-3, index_xy[1]-3] if (index_xy[0]-3)>=0 and (index_xy[1]-3)>=0 and (index_xy[0]-3)<8 and (index_xy[1]-3)<8 else None)
                posindex18 = ([index_xy[0]-4, index_xy[1]-4] if (index_xy[0]-4)>=0 and (index_xy[1]-4)>=0 and (index_xy[0]-4)<8 and (index_xy[1]-4)<8 else None)
                posindex19 = ([index_xy[0]-5, index_xy[1]-5] if (index_xy[0]-5)>=0 and (index_xy[1]-5)>=0 and (index_xy[0]-5)<8 and (index_xy[1]-5)<8 else None)
                posindex20 = ([index_xy[0]-6, index_xy[1]-6] if (index_xy[0]-6)>=0 and (index_xy[1]-6)>=0 and (index_xy[0]-6)<8 and (index_xy[1]-6)<8 else None)
                posindex21 = ([index_xy[0]-7, index_xy[1]-7] if (index_xy[0]-7)>=0 and (index_xy[1]-7)>=0 and (index_xy[0]-7)<8 and (index_xy[1]-7)<8 else None)




                pos3list = [posindex15, posindex16, posindex17, posindex18, posindex19, posindex20, posindex21]
                pos3listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos3list)) #get real position values
                blockers3 = list(filter(lambda x: x in pos3listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers3:#if blocker is found
                    blocker3 = max(blockers3) # min for this only# finds the nearest
                    blocker_index = pos3listreal.index(blocker3)

                    for i in range(blocker_index, len(pos3list)):
                        pos3list[i] = None





                '''  315 degree  '''
                posindex22 = ([index_xy[0]+1, index_xy[1]-1] if (index_xy[0]+1)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]+1)<8 and (index_xy[1]-1)<8 else None)
                posindex23 = ([index_xy[0]+2, index_xy[1]-2] if (index_xy[0]+2)>=0 and (index_xy[1]-2)>=0 and (index_xy[0]+2)<8 and (index_xy[1]-2)<8 else None)
                posindex24 = ([index_xy[0]+3, index_xy[1]-3] if (index_xy[0]+3)>=0 and (index_xy[1]-3)>=0 and (index_xy[0]+3)<8 and (index_xy[1]-3)<8 else None)
                posindex25 = ([index_xy[0]+4, index_xy[1]-4] if (index_xy[0]+4)>=0 and (index_xy[1]-4)>=0 and (index_xy[0]+4)<8 and (index_xy[1]-4)<8 else None)
                posindex26 = ([index_xy[0]+5, index_xy[1]-5] if (index_xy[0]+5)>=0 and (index_xy[1]-5)>=0 and (index_xy[0]+5)<8 and (index_xy[1]-5)<8 else None)
                posindex27 = ([index_xy[0]+6, index_xy[1]-6] if (index_xy[0]+6)>=0 and (index_xy[1]-6)>=0 and (index_xy[0]+6)<8 and (index_xy[1]-6)<8 else None)
                posindex28 = ([index_xy[0]+7, index_xy[1]-7] if (index_xy[0]+7)>=0 and (index_xy[1]-7)>=0 and (index_xy[0]+7)<8 and (index_xy[1]-7)<8 else None)


                pos4list = [posindex22, posindex23, posindex24, posindex25, posindex26, posindex27, posindex28]
                pos4listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos4list)) #get real position values
                blockers4 = list(filter(lambda x: x in pos4listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers4:#if blocker is found
                    blocker4 = min(blockers4) # min for this only# finds the nearest
                    blocker_index = pos4listreal.index(blocker4)

                    for i in range(blocker_index, len(pos4list)):
                        pos4list[i] = None



                return pos1list + pos2list + pos3list + pos4list


        elif name == "ElephantL" or name == "ElephantR":
            index_xy = self.get_index(pos)

            if index_xy:
                '''  X - Axis  '''
                posindex1  = ([index_xy[0]+1, index_xy[1]] if (index_xy[0]+1)>=0 and (index_xy[1])>=0 and (index_xy[0]+1)<8 and (index_xy[1])<8 else None)
                posindex2  = ([index_xy[0]+2, index_xy[1]] if (index_xy[0]+2)>=0 and (index_xy[1])>=0 and (index_xy[0]+2)<8 and (index_xy[1])<8 else None)
                posindex3  = ([index_xy[0]+3, index_xy[1]] if (index_xy[0]+3)>=0 and (index_xy[1])>=0 and (index_xy[0]+3)<8 and (index_xy[1])<8 else None)
                posindex4  = ([index_xy[0]+4, index_xy[1]] if (index_xy[0]+4)>=0 and (index_xy[1])>=0 and (index_xy[0]+4)<8 and (index_xy[1])<8 else None)
                posindex5  = ([index_xy[0]+5, index_xy[1]] if (index_xy[0]+5)>=0 and (index_xy[1])>=0 and (index_xy[0]+5)<8 and (index_xy[1])<8 else None)
                posindex6  = ([index_xy[0]+6, index_xy[1]] if (index_xy[0]+6)>=0 and (index_xy[1])>=0 and (index_xy[0]+6)<8 and (index_xy[1])<8 else None)
                posindex7  = ([index_xy[0]+7, index_xy[1]] if (index_xy[0]+7)>=0 and (index_xy[1])>=0 and (index_xy[0]+7)<8 and (index_xy[1])<8 else None)
                

                '''             Blocker Detector  '''
                pos1list = [posindex1, posindex2, posindex3, posindex4, posindex5, posindex6, posindex7]
                pos1listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos1list))
                blockers1 = list(filter(lambda x: x in pos1listreal, Pos_man))
                if blockers1:
                    blocker1 = min(blockers1)
                    blocker_index = pos1listreal.index(blocker1)

                    for i in range(blocker_index, len(pos1list)):
                        pos1list[i] = None




                posindex8  = ([index_xy[0]-1, index_xy[1]] if (index_xy[0]-1)>=0 and (index_xy[1])>=0 and (index_xy[0]-1)<8 and (index_xy[1])<8 else None)
                posindex9  = ([index_xy[0]-2, index_xy[1]] if (index_xy[0]-2)>=0 and (index_xy[1])>=0 and (index_xy[0]-2)<8 and (index_xy[1])<8 else None)
                posindex10 = ([index_xy[0]-3, index_xy[1]] if (index_xy[0]-3)>=0 and (index_xy[1])>=0 and (index_xy[0]-3)<8 and (index_xy[1])<8 else None)
                posindex11 = ([index_xy[0]-4, index_xy[1]] if (index_xy[0]-4)>=0 and (index_xy[1])>=0 and (index_xy[0]-4)<8 and (index_xy[1])<8 else None)
                posindex12 = ([index_xy[0]-5, index_xy[1]] if (index_xy[0]-5)>=0 and (index_xy[1])>=0 and (index_xy[0]-5)<8 and (index_xy[1])<8 else None)
                posindex13 = ([index_xy[0]-6, index_xy[1]] if (index_xy[0]-6)>=0 and (index_xy[1])>=0 and (index_xy[0]-6)<8 and (index_xy[1])<8 else None)
                posindex14 = ([index_xy[0]-7, index_xy[1]] if (index_xy[0]-7)>=0 and (index_xy[1])>=0 and (index_xy[0]-7)<8 and (index_xy[1])<8 else None)

                
                


                pos2list = [posindex8 , posindex9 , posindex10, posindex11, posindex12, posindex13, posindex14]
                pos2listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos2list))
                blockers2 = list(filter(lambda x: x in pos2listreal, Pos_man))
                if blockers2:
                    blocker2 = max(blockers2)
                    blocker_index = pos2listreal.index(blocker2)

                    for i in range(blocker_index, len(pos2list)):
                        pos2list[i] = None



                '''  Y - Axis  '''
                posindex15 = ([index_xy[0], index_xy[1]-1] if (index_xy[0])>=0 and (index_xy[1]-1)>=0 and (index_xy[0])<8 and (index_xy[1]-1)<8 else None)
                posindex16 = ([index_xy[0], index_xy[1]-2] if (index_xy[0])>=0 and (index_xy[1]-2)>=0 and (index_xy[0])<8 and (index_xy[1]-2)<8 else None)
                posindex17 = ([index_xy[0], index_xy[1]-3] if (index_xy[0])>=0 and (index_xy[1]-3)>=0 and (index_xy[0])<8 and (index_xy[1]-3)<8 else None)
                posindex18 = ([index_xy[0], index_xy[1]-4] if (index_xy[0])>=0 and (index_xy[1]-4)>=0 and (index_xy[0])<8 and (index_xy[1]-4)<8 else None)
                posindex19 = ([index_xy[0], index_xy[1]-5] if (index_xy[0])>=0 and (index_xy[1]-5)>=0 and (index_xy[0])<8 and (index_xy[1]-5)<8 else None)
                posindex20 = ([index_xy[0], index_xy[1]-6] if (index_xy[0])>=0 and (index_xy[1]-6)>=0 and (index_xy[0])<8 and (index_xy[1]-6)<8 else None)
                posindex21 = ([index_xy[0], index_xy[1]-7] if (index_xy[0])>=0 and (index_xy[1]-7)>=0 and (index_xy[0])<8 and (index_xy[1]-7)<8 else None)


                pos3list = [posindex15, posindex16, posindex17, posindex18, posindex19, posindex20, posindex21]
                pos3listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos3list))
                blockers3 = list(filter(lambda x: x in pos3listreal, Pos_man))
                if blockers3:
                    blocker3 = max(blockers3)
                    blocker_index = pos3listreal.index(blocker3)

                    for i in range(blocker_index, len(pos3list)):
                        pos3list[i] = None




                posindex22 = ([index_xy[0], index_xy[1]+1] if (index_xy[0])>=0 and (index_xy[1]+1)>=0 and (index_xy[0])<8 and (index_xy[1]+1)<8 else None)
                posindex23 = ([index_xy[0], index_xy[1]+2] if (index_xy[0])>=0 and (index_xy[1]+2)>=0 and (index_xy[0])<8 and (index_xy[1]+2)<8 else None)
                posindex24 = ([index_xy[0], index_xy[1]+3] if (index_xy[0])>=0 and (index_xy[1]+3)>=0 and (index_xy[0])<8 and (index_xy[1]+3)<8 else None)
                posindex25 = ([index_xy[0], index_xy[1]+4] if (index_xy[0])>=0 and (index_xy[1]+4)>=0 and (index_xy[0])<8 and (index_xy[1]+4)<8 else None)
                posindex26 = ([index_xy[0], index_xy[1]+5] if (index_xy[0])>=0 and (index_xy[1]+5)>=0 and (index_xy[0])<8 and (index_xy[1]+5)<8 else None)
                posindex27 = ([index_xy[0], index_xy[1]+6] if (index_xy[0])>=0 and (index_xy[1]+6)>=0 and (index_xy[0])<8 and (index_xy[1]+6)<8 else None)
                posindex28 = ([index_xy[0], index_xy[1]+7] if (index_xy[0])>=0 and (index_xy[1]+7)>=0 and (index_xy[0])<8 and (index_xy[1]+7)<8 else None)


                pos4list = [posindex22, posindex23, posindex24, posindex25, posindex26, posindex27, posindex28]
                pos4listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos4list))
                blockers4 = list(filter(lambda x: x in pos4listreal, Pos_man))
                if blockers4:
                    blocker4 = min(blockers4)
                    blocker_index = pos4listreal.index(blocker4)

                    for i in range(blocker_index, len(pos4list)):
                        pos4list[i] = None



                return pos1list + pos2list + pos3list + pos4list




        elif name == "Queen":
            index_xy = self.get_index(pos)

            if index_xy:
                '''  45 degree  '''
                posindex1  = ([index_xy[0]+1, index_xy[1]+1] if (index_xy[0]+1)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]+1)<8 and (index_xy[1]+1)<8 else None)
                posindex2  = ([index_xy[0]+2, index_xy[1]+2] if (index_xy[0]+2)>=0 and (index_xy[1]+2)>=0 and (index_xy[0]+2)<8 and (index_xy[1]+2)<8 else None)
                posindex3  = ([index_xy[0]+3, index_xy[1]+3] if (index_xy[0]+3)>=0 and (index_xy[1]+3)>=0 and (index_xy[0]+3)<8 and (index_xy[1]+3)<8 else None)
                posindex4  = ([index_xy[0]+4, index_xy[1]+4] if (index_xy[0]+4)>=0 and (index_xy[1]+4)>=0 and (index_xy[0]+4)<8 and (index_xy[1]+4)<8 else None)
                posindex5  = ([index_xy[0]+5, index_xy[1]+5] if (index_xy[0]+5)>=0 and (index_xy[1]+5)>=0 and (index_xy[0]+5)<8 and (index_xy[1]+5)<8 else None)
                posindex6  = ([index_xy[0]+6, index_xy[1]+6] if (index_xy[0]+6)>=0 and (index_xy[1]+6)>=0 and (index_xy[0]+6)<8 and (index_xy[1]+6)<8 else None)
                posindex7  = ([index_xy[0]+7, index_xy[1]+7] if (index_xy[0]+7)>=0 and (index_xy[1]+7)>=0 and (index_xy[0]+7)<8 and (index_xy[1]+7)<8 else None)

                pos1list = [posindex1, posindex2, posindex3, posindex4, posindex5, posindex6, posindex7]
                pos1listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos1list)) #get real position values
                blockers1 = list(filter(lambda x: x in pos1listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers1:#if blocker is found
                    blocker1 = min(blockers1) # min for this only# finds the nearest
                    blocker_index = pos1listreal.index(blocker1) #get new index

                    for i in range(blocker_index, len(pos1list)):
                        pos1list[i] = None


                '''  135 degree  '''
                posindex8  = ([index_xy[0]-1, index_xy[1]+1] if (index_xy[0]-1)>=0 and (index_xy[1]+1)>=0 and (index_xy[0]-1)<8 and (index_xy[1]+1)<8 else None)
                posindex9  = ([index_xy[0]-2, index_xy[1]+2] if (index_xy[0]-2)>=0 and (index_xy[1]+2)>=0 and (index_xy[0]-2)<8 and (index_xy[1]+2)<8 else None)
                posindex10 = ([index_xy[0]-3, index_xy[1]+3] if (index_xy[0]-3)>=0 and (index_xy[1]+3)>=0 and (index_xy[0]-3)<8 and (index_xy[1]+3)<8 else None)
                posindex11 = ([index_xy[0]-4, index_xy[1]+4] if (index_xy[0]-4)>=0 and (index_xy[1]+4)>=0 and (index_xy[0]-4)<8 and (index_xy[1]+4)<8 else None)
                posindex12 = ([index_xy[0]-5, index_xy[1]+5] if (index_xy[0]-5)>=0 and (index_xy[1]+5)>=0 and (index_xy[0]-5)<8 and (index_xy[1]+5)<8 else None)
                posindex13 = ([index_xy[0]-6, index_xy[1]+6] if (index_xy[0]-6)>=0 and (index_xy[1]+6)>=0 and (index_xy[0]-6)<8 and (index_xy[1]+6)<8 else None)
                posindex14 = ([index_xy[0]-7, index_xy[1]+7] if (index_xy[0]-7)>=0 and (index_xy[1]+7)>=0 and (index_xy[0]-7)<8 and (index_xy[1]+7)<8 else None)


                pos2list = [posindex8, posindex9, posindex10, posindex11, posindex12, posindex13, posindex14]
                pos2listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos2list)) #get real position values
                blockers2 = list(filter(lambda x: x in pos2listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers2:#if blocker is found
                    blocker2 = max(blockers2, key = lambda x: x[1]) # min for this only# finds the nearest
                    blocker_index = pos2listreal.index(blocker2)

                    for i in range(blocker_index, len(pos2list)):
                        pos2list[i] = None




                '''  225 degree  '''
                posindex15 = ([index_xy[0]-1, index_xy[1]-1] if (index_xy[0]-1)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]-1)<8 and (index_xy[1]-1)<8 else None)
                posindex16 = ([index_xy[0]-2, index_xy[1]-2] if (index_xy[0]-2)>=0 and (index_xy[1]-2)>=0 and (index_xy[0]-2)<8 and (index_xy[1]-2)<8 else None)
                posindex17 = ([index_xy[0]-3, index_xy[1]-3] if (index_xy[0]-3)>=0 and (index_xy[1]-3)>=0 and (index_xy[0]-3)<8 and (index_xy[1]-3)<8 else None)
                posindex18 = ([index_xy[0]-4, index_xy[1]-4] if (index_xy[0]-4)>=0 and (index_xy[1]-4)>=0 and (index_xy[0]-4)<8 and (index_xy[1]-4)<8 else None)
                posindex19 = ([index_xy[0]-5, index_xy[1]-5] if (index_xy[0]-5)>=0 and (index_xy[1]-5)>=0 and (index_xy[0]-5)<8 and (index_xy[1]-5)<8 else None)
                posindex20 = ([index_xy[0]-6, index_xy[1]-6] if (index_xy[0]-6)>=0 and (index_xy[1]-6)>=0 and (index_xy[0]-6)<8 and (index_xy[1]-6)<8 else None)
                posindex21 = ([index_xy[0]-7, index_xy[1]-7] if (index_xy[0]-7)>=0 and (index_xy[1]-7)>=0 and (index_xy[0]-7)<8 and (index_xy[1]-7)<8 else None)


                pos3list = [posindex15, posindex16, posindex17, posindex18, posindex19, posindex20, posindex21]
                pos3listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos3list)) #get real position values
                blockers3 = list(filter(lambda x: x in pos3listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers3:#if blocker is found
                    blocker3 = max(blockers3) # min for this only# finds the nearest
                    blocker_index = pos3listreal.index(blocker3)

                    for i in range(blocker_index, len(pos3list)):
                        pos3list[i] = None



                '''  315 degree  '''
                posindex22 = ([index_xy[0]+1, index_xy[1]-1] if (index_xy[0]+1)>=0 and (index_xy[1]-1)>=0 and (index_xy[0]+1)<8 and (index_xy[1]-1)<8 else None)
                posindex23 = ([index_xy[0]+2, index_xy[1]-2] if (index_xy[0]+2)>=0 and (index_xy[1]-2)>=0 and (index_xy[0]+2)<8 and (index_xy[1]-2)<8 else None)
                posindex24 = ([index_xy[0]+3, index_xy[1]-3] if (index_xy[0]+3)>=0 and (index_xy[1]-3)>=0 and (index_xy[0]+3)<8 and (index_xy[1]-3)<8 else None)
                posindex25 = ([index_xy[0]+4, index_xy[1]-4] if (index_xy[0]+4)>=0 and (index_xy[1]-4)>=0 and (index_xy[0]+4)<8 and (index_xy[1]-4)<8 else None)
                posindex26 = ([index_xy[0]+5, index_xy[1]-5] if (index_xy[0]+5)>=0 and (index_xy[1]-5)>=0 and (index_xy[0]+5)<8 and (index_xy[1]-5)<8 else None)
                posindex27 = ([index_xy[0]+6, index_xy[1]-6] if (index_xy[0]+6)>=0 and (index_xy[1]-6)>=0 and (index_xy[0]+6)<8 and (index_xy[1]-6)<8 else None)
                posindex28 = ([index_xy[0]+7, index_xy[1]-7] if (index_xy[0]+7)>=0 and (index_xy[1]-7)>=0 and (index_xy[0]+7)<8 and (index_xy[1]-7)<8 else None)
                

                pos4list = [posindex22, posindex23, posindex24, posindex25, posindex26, posindex27, posindex28]
                pos4listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None , pos4list)) #get real position values
                blockers4 = list(filter(lambda x: x in pos4listreal, Pos_man))#get all blockers' position if exist(s)
                if blockers4:#if blocker is found
                    blocker4 = min(blockers4) # min for this only# finds the nearest
                    blocker_index = pos4listreal.index(blocker4)

                    for i in range(blocker_index, len(pos4list)):
                        pos4list[i] = None





                '''  X - Axis  '''
                posindex29 = ([index_xy[0]+1, index_xy[1]] if (index_xy[0]+1)>=0 and (index_xy[1])>=0 and (index_xy[0]+1)<8 and (index_xy[1])<8 else None)
                posindex30 = ([index_xy[0]+2, index_xy[1]] if (index_xy[0]+2)>=0 and (index_xy[1])>=0 and (index_xy[0]+2)<8 and (index_xy[1])<8 else None)
                posindex31 = ([index_xy[0]+3, index_xy[1]] if (index_xy[0]+3)>=0 and (index_xy[1])>=0 and (index_xy[0]+3)<8 and (index_xy[1])<8 else None)
                posindex32 = ([index_xy[0]+4, index_xy[1]] if (index_xy[0]+4)>=0 and (index_xy[1])>=0 and (index_xy[0]+4)<8 and (index_xy[1])<8 else None)
                posindex33 = ([index_xy[0]+5, index_xy[1]] if (index_xy[0]+5)>=0 and (index_xy[1])>=0 and (index_xy[0]+5)<8 and (index_xy[1])<8 else None)
                posindex34 = ([index_xy[0]+6, index_xy[1]] if (index_xy[0]+6)>=0 and (index_xy[1])>=0 and (index_xy[0]+6)<8 and (index_xy[1])<8 else None)
                posindex35 = ([index_xy[0]+7, index_xy[1]] if (index_xy[0]+7)>=0 and (index_xy[1])>=0 and (index_xy[0]+7)<8 and (index_xy[1])<8 else None)
                
                pos5list = [posindex29, posindex30, posindex31, posindex32, posindex33, posindex34, posindex35]
                pos5listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos5list))
                blockers5 = list(filter(lambda x: x in pos5listreal, Pos_man))
                if blockers5:
                    blocker5 = min(blockers5)
                    blocker_index = pos5listreal.index(blocker5)

                    for i in range(blocker_index, len(pos5list)):
                        pos5list[i] = None




                posindex36 = ([index_xy[0]-1, index_xy[1]] if (index_xy[0]-1)>=0 and (index_xy[1])>=0 and (index_xy[0]-1)<8 and (index_xy[1])<8 else None)
                posindex37 = ([index_xy[0]-2, index_xy[1]] if (index_xy[0]-2)>=0 and (index_xy[1])>=0 and (index_xy[0]-2)<8 and (index_xy[1])<8 else None)
                posindex38 = ([index_xy[0]-3, index_xy[1]] if (index_xy[0]-3)>=0 and (index_xy[1])>=0 and (index_xy[0]-3)<8 and (index_xy[1])<8 else None)
                posindex39 = ([index_xy[0]-4, index_xy[1]] if (index_xy[0]-4)>=0 and (index_xy[1])>=0 and (index_xy[0]-4)<8 and (index_xy[1])<8 else None)
                posindex40 = ([index_xy[0]-5, index_xy[1]] if (index_xy[0]-5)>=0 and (index_xy[1])>=0 and (index_xy[0]-5)<8 and (index_xy[1])<8 else None)
                posindex41 = ([index_xy[0]-6, index_xy[1]] if (index_xy[0]-6)>=0 and (index_xy[1])>=0 and (index_xy[0]-6)<8 and (index_xy[1])<8 else None)
                posindex42 = ([index_xy[0]-7, index_xy[1]] if (index_xy[0]-7)>=0 and (index_xy[1])>=0 and (index_xy[0]-7)<8 and (index_xy[1])<8 else None)


                pos6list = [posindex36, posindex37, posindex38, posindex39, posindex40, posindex41, posindex42]
                pos6listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos6list))
                blockers6 = list(filter(lambda x: x in pos6listreal, Pos_man))
                if blockers6:
                    blocker6 = max(blockers6)
                    blocker_index = pos6listreal.index(blocker6)

                    for i in range(blocker_index, len(pos6list)):
                        pos6list[i] = None





                '''  Y - Axis  '''
                posindex43 = ([index_xy[0], index_xy[1]-1] if (index_xy[0])>=0 and (index_xy[1]-1)>=0 and (index_xy[0])<8 and (index_xy[1]-1)<8 else None)
                posindex44 = ([index_xy[0], index_xy[1]-2] if (index_xy[0])>=0 and (index_xy[1]-2)>=0 and (index_xy[0])<8 and (index_xy[1]-2)<8 else None)
                posindex45 = ([index_xy[0], index_xy[1]-3] if (index_xy[0])>=0 and (index_xy[1]-3)>=0 and (index_xy[0])<8 and (index_xy[1]-3)<8 else None)
                posindex46 = ([index_xy[0], index_xy[1]-4] if (index_xy[0])>=0 and (index_xy[1]-4)>=0 and (index_xy[0])<8 and (index_xy[1]-4)<8 else None)
                posindex47 = ([index_xy[0], index_xy[1]-5] if (index_xy[0])>=0 and (index_xy[1]-5)>=0 and (index_xy[0])<8 and (index_xy[1]-5)<8 else None)
                posindex48 = ([index_xy[0], index_xy[1]-6] if (index_xy[0])>=0 and (index_xy[1]-6)>=0 and (index_xy[0])<8 and (index_xy[1]-6)<8 else None)
                posindex49 = ([index_xy[0], index_xy[1]-7] if (index_xy[0])>=0 and (index_xy[1]-7)>=0 and (index_xy[0])<8 and (index_xy[1]-7)<8 else None)


                pos7list = [posindex43, posindex44, posindex45, posindex46, posindex47, posindex48, posindex49]
                pos7listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos7list))
                blockers7 = list(filter(lambda x: x in pos7listreal, Pos_man))
                if blockers7:
                    blocker7 = max(blockers7)
                    blocker_index = pos7listreal.index(blocker7)

                    for i in range(blocker_index, len(pos7list)):
                        pos7list[i] = None





                posindex50 = ([index_xy[0], index_xy[1]+1] if (index_xy[0])>=0 and (index_xy[1]+1)>=0 and (index_xy[0])<8 and (index_xy[1]+1)<8 else None)
                posindex51 = ([index_xy[0], index_xy[1]+2] if (index_xy[0])>=0 and (index_xy[1]+2)>=0 and (index_xy[0])<8 and (index_xy[1]+2)<8 else None)
                posindex52 = ([index_xy[0], index_xy[1]+3] if (index_xy[0])>=0 and (index_xy[1]+3)>=0 and (index_xy[0])<8 and (index_xy[1]+3)<8 else None)
                posindex53 = ([index_xy[0], index_xy[1]+4] if (index_xy[0])>=0 and (index_xy[1]+4)>=0 and (index_xy[0])<8 and (index_xy[1]+4)<8 else None)
                posindex54 = ([index_xy[0], index_xy[1]+5] if (index_xy[0])>=0 and (index_xy[1]+5)>=0 and (index_xy[0])<8 and (index_xy[1]+5)<8 else None)
                posindex55 = ([index_xy[0], index_xy[1]+6] if (index_xy[0])>=0 and (index_xy[1]+6)>=0 and (index_xy[0])<8 and (index_xy[1]+6)<8 else None)
                posindex56 = ([index_xy[0], index_xy[1]+7] if (index_xy[0])>=0 and (index_xy[1]+7)>=0 and (index_xy[0])<8 and (index_xy[1]+7)<8 else None)


                pos8list = [posindex50, posindex51, posindex52, posindex53, posindex54, posindex55, posindex56]
                pos8listreal = list(map(lambda x: posns[x[1]][x[0]] if x else None, pos8list))
                blockers8 = list(filter(lambda x: x in pos8listreal, Pos_man))
                if blockers8:
                    blocker8 = min(blockers8)
                    blocker_index = pos8listreal.index(blocker8)

                    for i in range(blocker_index, len(pos8list)):
                        pos8list[i] = None




                return pos1list + pos2list + pos3list + pos4list + pos5list + pos6list + pos7list + pos8list

        elif name in soldiers:
            index_xy = self.get_index(pos)

            if index_xy and self.first_move:
                pos1index = ([index_xy[0], index_xy[1]+1] if index_xy[1]+1<8 else None)
                pos2index = ([index_xy[0], index_xy[1]+2] if index_xy[1]+1<8 else None)
                
                return [pos1index, pos2index]

            elif index_xy and not self.first_move:
                pos1index = ([index_xy[0], index_xy[1]+1] if index_xy[1]+1<8 else None)

                return [pos1index]







    def get_index(self, pos):
        '''returns index of current position, in posns(position list of board), of respective character
           so that it can be further used to find movable positions of respective character'''
        global posns
        for i in range(8):
            if pos in posns[i]: # i as first value to be in "[]" of posns, literally y value.
                index_xy = (posns[i].index(pos), i) # posns[i].index(pos) gives index in i'th list in posns.
                return index_xy # return those indeces (index plural may be :-) ).

    def circle_collide_point(self, object, input_x, input_y):
        '''self made collision detector for movable positions circles'''
        if input_x>object.pos[0] and input_x<object.pos[0]+object.size[0] and input_y>object.pos[1] and input_y<object.pos[1]+object.size[1]:
            return True
        else:
            return False

    def tried_to_move(self, circle_list, touch_x, touch_y):
        '''Check if user wants to move somebody
           returns True, pos of circle
           or
           returns False'''
        if circle_list:
            for circle in circle_list:
                if self.circle_collide_point(circle, touch_x, touch_y):
                    if self.name in soldiers:
                        self.first_move = False
                    return True, [circle.pos[0], circle.pos[1]]
            else:
                return False
    
    def manage_posman(self, name, new_pos):
        global Pos_man
        if name == "ElephantL":
            Pos_man[0] = new_pos
        elif name == "HorseL":
            Pos_man[1] = new_pos
        elif name == "CamelL":
            Pos_man[2] == new_pos
        elif name == "Queen":
            Pos_man[3] = new_pos
        elif name == "King":
            Pos_man[4] = new_pos
        elif name == "CamelR":
            Pos_man[5] = new_pos
        elif name == "HorseR":
            Pos_man[6] = new_pos
        elif name == "ElephantR":
            Pos_man[7] = new_pos
        elif name in soldiers:
            Sol_index = soldiers.index(name)
            Pos_man[8+Sol_index] = new_pos



    def animate_circle(self, circle_list):
        anim = Animation(size = (el_width-10, el_height-10), duration=0.2, transition='out_back')#out_back is expected
        for circle in circle_list:
            anim.start(circle)

    def animate_chart(self, newpos):
        anim = Animation(pos = newpos, duration = 0.1)
        anim.start(self)
        


class King(Clickable):
    pass

class Queen(Clickable):
    pass

class Horse(Clickable):
    pass

class Camel(Clickable):
    pass

class Elephant(Clickable):
    pass

class Soldier(Clickable):
    pass