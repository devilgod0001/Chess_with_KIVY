import kivy

kivy.require('1.0.0')

'''  IMPORT STUFF  '''
from numpy import array
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

'''  **IMPORT STUFF  '''


chess_board_array = array([
    ['OO','A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0'],
    ['O0','A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
    ['O0','A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
    ['O0','A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
    ['O0','A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
    ['O0','A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
    ['O0','A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
    ['O0','A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
    ['O0','A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
])


'''  WIDGET CLASS  '''
class GameScreen(PageLayout):
    pass
'''  **WIDGET CLASS  '''


'''  MAIN APP CLASS  '''

class Clean_ChessApp(App):
    def build(self):
        return GameScreen()

'''  **MAIN APP CLASS  '''

if __name__ == "__main__":
    #Window.size = (9*40,16*40)
    Window.clearcolor = get_color_from_hex("#FFFD98")
    Clean_ChessApp().run()