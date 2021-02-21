# import pygame
# pygame.init()
# screen_info = pygame.display.Info()

# w = screen_info.current_w
# h = screen_info.current_h

w, h = 9*40, 16*40

img_spacing = -9

mgn_wrt360 = 8
mgn_fr = mgn_wrt360/360
pdd_wrt360 = 10
pdd_fr = pdd_wrt360/360

# shadow_margin_pixel_x = 4
# shadow_margin_pixel_y = -2

shadow_margin_pixel_x = -3
shadow_margin_pixel_y = -3

grid_radius = 10
grid_segments = 10

''' COLOR '''
board_grid_color = "#C84630"
board_grid_shadow_color = "#353535"
back_color = "#FC9F5B"
window_back_color = "#353535"


con_len = w if w < h else h
x_y_margin = con_len*mgn_fr
padding = con_len*pdd_fr
per_block_side = ((con_len - (7*x_y_margin)) - (2*padding))*(1/8)
per_image_side = per_block_side - (2*img_spacing)


         #mobile                                                 #computer
value1 = (h-w)*(1/2) + padding + img_spacing if con_len == w else padding + img_spacing
value2 = padding + img_spacing if con_len == w else (h-w)*(1/2) + padding + img_spacing


first_coo = [value2, value1]
diff_for_coo = x_y_margin + per_block_side

##Image values Array
board_array = [[],[],[],[],[],[],[],[]]

for i in range(8):
    for j in range(8):
        x = first_coo[0] + j*diff_for_coo
        y = first_coo[1] + i*diff_for_coo
        board_array[i].append([x, y])

current_positions = {
                    'W_R_Rook':board_array[0][7],
                    'W_R_Knight':board_array[0][6],
                    'W_R_Bishop':board_array[0][5],
                    'W_Queen':board_array[0][3],
                    'W_King':board_array[0][4],
                    'W_L_Bishop':board_array[0][2],
                    'W_L_Knight':board_array[0][1],
                    'W_L_Rook':board_array[0][0],
                    'W_8_Pawn':board_array[1][7],
                    'W_7_Pawn':board_array[1][6],
                    'W_6_Pawn':board_array[1][5],
                    'W_5_Pawn':board_array[1][4],
                    'W_4_Pawn':board_array[1][3],
                    'W_3_Pawn':board_array[1][2],
                    'W_2_Pawn':board_array[1][1],
                    'W_1_Pawn':board_array[1][0],

                    'B_R_Rook':board_array[7][7],
                    'B_R_Knight':board_array[7][6],
                    'B_R_Bishop':board_array[7][5],
                    'B_Queen':board_array[7][3],
                    'B_King':board_array[7][4],
                    'B_L_Bishop':board_array[7][2],
                    'B_L_Knight':board_array[7][1],
                    'B_L_Rook':board_array[7][0],
                    'B_8_Pawn':board_array[6][7],
                    'B_7_Pawn':board_array[6][6],
                    'B_6_Pawn':board_array[6][5],
                    'B_5_Pawn':board_array[6][4],
                    'B_4_Pawn':board_array[6][3],
                    'B_3_Pawn':board_array[6][2],
                    'B_2_Pawn':board_array[6][1],
                    'B_1_Pawn':board_array[6][0]
                     }


grid_box_array = [[],[],[],[],[],[],[],[]]

for i in range(8):
    for j in range(8):
        x = board_array[i][j][0]-img_spacing
        y = board_array[i][j][1]-img_spacing
        grid_box_array[i].append([x, y])


grid_box_shrink = 10