from Focus_Roots import *

set_background(color_brown)

def change():
    draw_rect(150, 110, 150, 150, 0, color = color_skin)#Head
    draw_rect(170, 150, 30, 30, 0, color = color_white)#Iris
    draw_rect(250, 150, 30, 30, 0, color = color_white)#Iris
    draw_rect(260, 160, 10, 10, 0, color = color_black)#Pupil
    draw_rect(180, 160, 10, 10, 0, color = color_black)#Pupil
    draw_rect(195, 220, 60, 4, 0, color = color_black)#mouth
    draw_line([225,180], [225,200], 2, color = color_black)#nose
    draw_rect(200, 260, 45, 50, 0, color = color_skin)#neck
    draw_rect(160, 300, 130, 150, 0, color = color_mid_night_blue)#body
    draw_rect(130, 300, 20, 148, 0, color=color_skin)#arms
    draw_rect(300, 300, 20, 148, 0, color=color_skin)#arms
    draw_rect(130, 300, 30, 30, 0, color=color_mid_night_blue)#shoulders
    draw_rect(290, 300, 30, 30, 0, color=color_mid_night_blue)#shoulders
    draw_rect(140, 100, 170, 20, 0, color=color_black)#hair
    draw_rect(140, 100, 20, 40, 0, color=color_black)#hair
    draw_rect(290, 100, 20, 40, 0, color=color_black)#hair
    write_text("This is A boy!", 220,470,40,color = color_burlywood)

draw(change)