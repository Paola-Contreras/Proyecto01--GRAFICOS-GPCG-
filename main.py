#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213

from gl import Renderer, color, V3, V2
from texture import Texture
import shader as s 
import math as m 

w = 1000
h = 600

rend = Renderer(w, h)

rend.background = Texture("textures/DDG.bmp")
rend.glClearBackground()
#Medium
rend.glLookAt(V3(2,5,-3),V3(0,7.9,1))


#Plant
rend.active_shader = s.degraded
rend.active_texture = Texture("textures/indoor plant_2_COL.bmp")
rend.glLoadModel("model/indoor plant_02.obj",
                 translate = V3(1.5,4.8,-1),
                 rotate = V3(-15, -130, 30),
                 scale = V3(0.25, 0.25, 0.25))

#Chair
rend.active_shader = s.flat
rend.active_texture = Texture("textures/Chair_Base_Color.bmp")
rend.glLoadModel("model/Chair.obj",
                  translate = V3(0.3, 6.4, 0),
                  rotate = V3(-20, -3, -10),
                  scale = V3(0.4, 0.4, 0.4))


#Couch
rend.active_shader = s.zebra
rend.active_texture = Texture("textures/Couch_Base_Color.bmp")
rend.glLoadModel("model/Couch.obj",
                  translate = V3(-0.1, 6.3, -0.3),
                  rotate = V3(-20, -25, -10),
                  scale = V3(0.4, 0.4, 0.4))


#Paw
rend.active_shader = s.light
rend.active_texture = Texture("textures/paw color.bmp")
rend.glLoadModel("model/paw.obj",
                  translate = V3(0.5, 6, 0),
                  rotate = V3(5, 0, 0),
                  scale = V3(0.04, 0.04, 0.04))


#Cat
rend.active_texture = Texture("textures/Miniature_cat.bmp")
#rend.normal_map = Texture("textures/Miniature_cat_normal.bmp")

rend.active_shader = s.gourad
rend.glLoadModel("model/Miniature_cat_SF.obj",
                  translate = V3(0, 6.28, 0),
                  rotate = V3(0, 50, 0),
                  scale = V3(0.2, 0.2, 0.2))


#Decoration 
rend.active_shader = s.rainbow
rend.active_texture = Texture("textures/gold.bmp")
rend.glLoadModel("model/globes.obj",
                 translate = V3(0.3,7.4,0.2),
                 rotate = V3(-20, 25, -10),
                 scale = V3(0.4, 0.4, 0.4))


#Generate Image 
rend.glFinish("output1.bmp")

