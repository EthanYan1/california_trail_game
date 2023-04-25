import pygame, sys, os
from pygame.locals import QUIT

color_light = (170,170,170)
color_dark = (100,100,100)

FPS = 60

pygame.init()
# pygame.font.init()

# pygame.font.init()
FONT = pygame.font.SysFont("Corbel", 20)
CHOICE_FONT = pygame.font.SysFont("Impact", 20)
TITLE_FONT = pygame.font.SysFont("Comic Sans MS", 30)

game_window = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('California Trail Game')
game_window.fill("white")

background_img = pygame.image.load("ImageAssets\\california_trail_background.png").convert_alpha()
game_window.blit(background_img, (0,0))

ScreenList = {"home_screen": {"img_path": "ImageAssets\\HomeScreen\\home_screen_trail.png", "map_path" :  "ImageAssets\\HomeScreen\\map_california_trail_homescreen.png", "prompt": ["You, a glory-seeking American from Missouri, are ready to pack up your peaceful", "and chase a life of adventure and riches in California! But not everything", "is bliss, as you will need to choose carefully how you get there,", "through the California Trail... Press Play to continue."],\
                              "option1":[None, None], "option2" : [None, None], "option3" : ["Play", "screen_entertrail"], "option4" : [None, None]},\
              "screen_entertrail": {"img_path" : "ImageAssets\\enter_scene\\california_trail_enter.png", "map_path" : "ImageAssets\\enter_scene\\map_california_trail_enterscene.png", "prompt": ["You have entered the California trail. Which way do you travel?", "There seems to be only one way."],\
"option1":[None,None], "option2":[None,None], "option3":["Straight", "screen_vastplain"], "option4":[None,None]},\
              "screen_vastplain":{"img_path":"ImageAssets\\vast_plain_scene\\vast_plain_trail.png", "map_path":"ImageAssets\\vast_plain_scene\\map_california_trail_vastplain.png", "prompt": ["You find yourself in a vast plain. Though bare, it provides an indicator of the California trail.", "In the distance is a ginormous rock that would give a view of where you are going.", "Do you head towards it?"], \
                                  "option1":[None,None], "option2":["Yes", "screen_bigrock"], "option3":["No", "screen_wolfdeath"], "option4":[None,None]},\
              "screen_wolfdeath":{"img_path":"ImageAssets\\wolf_death\\wolf.png", "map_path":"ImageAssets\\wolf_death\\map_california_trail_wolfdeath.png", "prompt":["You head the other direction in the plain. Suddenly, you hear a growling", "behind you, and turn around to face a wolf. The wolf isn't so friendly, and", "it mauls you to death."],\
                                  "option1":[None,None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None,None]},\
              "screen_bigrock":{"img_path":"ImageAssets\\big_rock_scene\\giant_rock.png", "map_path":"ImageAssets\\big_rock_scene\\map_california_trail_giant_rock.png", "prompt": ["You traverse the barren landscape, and come to the foot of the rock. After hours of climbing,", "you reach the peak, and overlook the whole of the plains. A speck of unnatural white", "in the golden grass catches your eye."],\
                                "option1":[None,None], "option2":[None,None], "option3":["Follow", "screen_fort_laramie"], "option4":[None,None]},\
              "screen_fort_laramie":{"img_path":"ImageAssets\\scene_fortlaramie\\fort_laramie.png", "map_path":"ImageAssets\\scene_fortlaramie\\map_california_trail_fort_laramie.png", "prompt":["You trek downwards and find yourself at the foot of the rock. When you reach the bottom,", "you head in the direction of the white speck. After a long journey,", "the scene unfolds as a square fort. The title plaque at the front reads “Fort Laramie”.", "A group of men approach you. Do you ask them for directions to California?"],\
                                    "option1":[None, None], "option2":["Yes", "screen_fort_hall"], "option3":["No", "screen_rattlesnake_death"], "option4":[None, None]}, \
              "screen_rattlesnake_death":{"img_path":"ImageAssets\\scene_rattlesnakedeath\\rattlesnake.png", "map_path":"ImageAssets\\scene_rattlesnakedeath\\map_california_trail_rattlesnake_death.png", "prompt":["You turn to leave the men, but as you walk back through the plain,", "you are bitten by a rattlesnake."],\
                                          "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]}, \
              "screen_fort_hall":{"img_path":"ImageAssets\\scene_forthall\\fort_hall.png", "map_path":"ImageAssets\\scene_forthall\\map_california_trail_forthall.png", "prompt":[" The men tell you to follow aside a mountain range until you reach a second fort, Fort Hall.", "you follow their instructions and reach the fort. There, the officer in charge", "offers two options to California."],\
                                  "option1":[None, None], "option2":["Take a train", "screen_train"], "option3":["Walk", "screen_basin1"], "option4":[None, None]},\
              "screen_basin1":{"img_path":"ImageAssets\\first_basin_scene\\great_basin.png", "map_path":"ImageAssets\\first_basin_scene\\map_california_trail_basin1.png", "prompt":["You decide to walk. Taking the long route is tiring, and after hours of traveling,", "you come across a straight path. A large basin comes into view, with a boat on its shore."],\
                              "option1":[None, None], "option2":[None, None], "option3":["Go straight", "screen_basin2"], "option4":[None, None]},\
              "screen_train":{"img_path":"ImageAssets\\train_scene\\train_scene.png", "map_path":"ImageAssets\\train_scene\\map_california_trail_train.png", "prompt":["You decide to take the train. Passing through an area the Union is considering “Nevada”,", "the train breaks down and you are forced to walk."],\
                              "option1":[None, None], "option2":[None, None], "option3":["Go straight", "screen_basin2"], "option4":[None, None]},\
              "screen_basin2":{"img_path":"ImageAssets\\second_basin_scene\\great_basin_lake.png", "map_path":"ImageAssets\\second_basin_scene\\map_california_trail_basin2.png", "prompt":["You follow the straight path and come across a large basin. ", "A boat lies at the water’s edge."],\
                               "option1":[None, None], "option2":["Follow the basin edge", "screen_coyote_death"], "option3":["Cross the water", "screen_forest_edge"], "option4":[None, None]},\
              "screen_coyote_death":{"img_path":"ImageAssets\\coyote_death\\coyote.png", "map_path":"ImageAssets\\coyote_death\\map_california_trail_coyote.png", "prompt":["You follow the basin and reach a waterfall. You turn back and", "encounter an unfriendly coyote. "],\
                                     "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]},\
              "screen_forest_edge":{"img_path":"ImageAssets\\scene_forest_edge\\forest.png", "map_path":"ImageAssets\\scene_forest_edge\\map_california_trail_forest.png", "prompt":["You cross the brook, and the edge of the forest is close.", "Do you continue on the path?"],\
                                    "option1":[None, None], "option2":["North", "screen_smoke"], "option3":["South", "screen_cliff_death"], "option4":["Continue West", "screen_mountain_range"]},\
              "screen_cliff_death":{"img_path":"ImageAssets\\cliff_death\\cliff.png", "map_path":"ImageAssets\\cliff_death\\map_california_trail_cliff.png", "prompt":["You move South, but come across a cliffside. You attempt to continue", " trekking on the cliffside, but the soil beneath your feet suddenly", "caves in, causing you to slip off the edge and fall through the air."],\
                                    "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]},\
              "screen_smoke":{"img_path":"ImageAssets\\scene_smoke\\smoke_trees.png", "map_path":"ImageAssets\\scene_smoke\\map_california_trail_smoke.png", "prompt":["You walk North and reach an incline. You travel up the hillside and", "reach a mass of thick bushes. Pushing through the thickets,", "you see smoke rise from above the trees."],\
                              "option1":[None, None], "option2":["Go towards the smoke", "screen_natives_death"], "option3":["Turn back", "screen_woods_death"], "option4":[None, None]},\
              "screen_natives_death":{"img_path":"ImageAssets\\natives_death\\native_camp.png", "map_path":"ImageAssets\\natives_death\\map_california_trail_nativedeath.png", "prompt":[" You reach the smoke, but, to your dismay, the creators of the source are Native Americans.", "Unaware you mean no harm, they take you captive."],\
                                      "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]},\
              "screen_woods_death":{"img_path":"ImageAssets\\woods_death\\night_woods.png", "map_path":"ImageAssets\\woods_death\\map_california_trail_woodsdeath.png", "prompt":["You go back down the mountain, but can’t seem to find where", "you originally came from. Night sets in, and you become", "prey in the thick woods."],\
                                    "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]},\
              "screen_mountain_range":{"img_path":"ImageAssets\\scene_mountains\\sierra_nevada.png", "map_path":"ImageAssets\\scene_mountains\\map_california_trail_sierranevada.png", "prompt":["You travel west, and exit the forest. A grand mountainside unfolds in", "front of you. This must be the mountain range", "so many Americans fear."],\
                                       "option1":[None, None], "option2":["Travel around the mountain range", "screen_mountain_win"], "option3":["Travel through the mountain range", "screen_night_mountains"], "option4":[None, None]},\
              "screen_mountain_win":{"img_path":"ImageAssets\\mountain_win\\welcome_california.png", "map_path":"ImageAssets\\mountain_win\\map_california_trail_win.png", "prompt":["You take the safe option and go around. Though it takes multiple days,", "the range is now behind you. Eventually a sign in the distance captures", "your attention, and when reached, it reads: WELCOME TO CALIFORNIA", "", "Congratulations! You won!"],\
                                     "option1":[None, None], "option2":["Exit the game", None], "option3":[None, None], "option4":[None, None]},\
              "screen_night_mountains":{"img_path":"ImageAssets\\scene_night_mountain\\mountain_range.png", "map_path":"ImageAssets\\scene_night_mountain\\map_california_trail_sierranevada.png", "prompt":["You take your chances through the mountain range. It’ll take too", "long otherwise. Quickly, night falls, which leaves two options."],\
                                        "option1":[None, None], "option2":["Keep going", "screen_hypothermia_death"], "option3":["Set up camp", "screen_mountain_camp"], "option4":[None, None]},\
              "screen_hypothermia_death":{"img_path":"ImageAssets\\hypothermia_death\\black_gradient.png", "map_path":"ImageAssets\\hypothermia_death\\map_california_trail_hypothermia.png", "prompt":["You keep going, but underestimate the cold environment of the mountains.", "Hypothermia quickly sets in, and you succumb to the cold."],\
                                          "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]},\
              "screen_mountain_camp":{"img_path":"ImageAssets\\scene_mountain_camp\\mountain_range.png", "map_path":"ImageAssets\\scene_mountain_camp\\map_california_trail_sierranevada.png", "prompt":["You set up camp, and though the mountains are far colder than imagined,", "the small fire keeps hypothermia away. The next morning you set out,", "but must go one way around a mountain. Which way?"],\
                                      "option1":[None, None], "option2":["Left", "screen_wolfdeath2"], "option3":["Right", "screen_meadow_win"], "option4":[None, None]},\
              "screen_wolfdeath2":{"img_path":"ImageAssets\\second_wolf_death\\wolf_pack.png", "map_path":"ImageAssets\\second_wolf_death\\map_california_trail_sierranevada.png", "prompt":["You go left, but run into a pack of hungry wolves."],\
                                   "option1":[None, None], "option2":["Quit", None], "option3":["Try again from start", "home_screen"], "option4":[None, None]},\
              "screen_meadow_win":{"img_path":"ImageAssets\\meadow_win\\welcome_california.png", "map_path":"ImageAssets\\meadow_win\\map_california_trail_win.png", "prompt":["You circle the mountain with no issue, and at midday you find yourself in a meadow.", "There’s a sign in the distance, which says when reached: WELCOME TO CALIFORNIA", "", "Congratulations! You Won!"],\
                                   "option1":[None, None], "option2":["Exit the game", None], "option3":[None, None], "option4":[None, None]}}
# {"img_path":"", "map_path":"", "prompt":[], "option1":[], "option2":[], "option3":[], "option4":[]}
current_screen = "home_screen"

mouse = pygame.mouse.get_pos()

def load_screen(img_path, map_path, prompt, op_1=None, op_2=None, op_3=None, op_4=None):
  trail_img = pygame.image.load(img_path).convert_alpha() # load images
  trail_img = pygame.transform.scale(trail_img, (560, 280))
  map_img = pygame.image.load(map_path).convert_alpha()
  map_img = pygame.transform.scale(map_img, (560, 280))
  game_window.blit(trail_img, (80, 90))
  game_window.blit(map_img, (80, 370))

  i = 0
  for line in prompt:
    prompt_text = FONT.render(line, True, "black") # render prompt
    text_rect = prompt_text.get_rect()
    text_rect.center = (1020, 110 + i)
    game_window.blit(prompt_text, text_rect)
    i += 20

  if(op_1 != None):
    if(700 <= mouse[0] <= 1300 and 160 <= mouse[1] <= 240):
      pygame.draw.rect(game_window, color_light,[700, 160, 600, 80])
    else:
      pygame.draw.rect(game_window, color_dark,[700, 160, 600, 80])
    op_1_text = CHOICE_FONT.render(op_1, True, "white")
    op_1_rect = op_1_text.get_rect()
    op_1_rect.center = (1000, 200)
    game_window.blit(op_1_text, op_1_rect)

  if(op_2 != None):
    if(700 <= mouse[0] <= 1300 and 280 <= mouse[1] <= 360):
      pygame.draw.rect(game_window, color_light,[700, 280, 600, 80])
    else:
      pygame.draw.rect(game_window, color_dark,[700, 280, 600, 80])
    op_2_text = CHOICE_FONT.render(op_2, True, "white")
    op_2_rect = op_2_text.get_rect()
    op_2_rect.center = (1000, 320)
    game_window.blit(op_2_text, op_2_rect)

  if(op_3 != None):
    if(700 <= mouse[0] <= 1300 and 400 <= mouse[1] <= 480):
      pygame.draw.rect(game_window, color_light,[700, 400, 600, 80])
    else:
      pygame.draw.rect(game_window, color_dark,[700, 400, 600, 80])
    op_3_text = CHOICE_FONT.render(op_3, True, "white")
    op_3_rect = op_3_text.get_rect()
    op_3_rect.center = (1000, 440)
    game_window.blit(op_3_text, op_3_rect)

  if(op_4 != None):
    if(700 <= mouse[0] <= 1300 and 520 <= mouse[1] <= 600):
      pygame.draw.rect(game_window, color_light,[700, 520, 600, 80])
    else:
      pygame.draw.rect(game_window, color_dark,[700, 520, 600, 80])
    op_4_text = CHOICE_FONT.render(op_4, True, "white")
    op_4_rect = op_4_text.get_rect()
    op_4_rect.center = (1000, 560)
    game_window.blit(op_4_text, op_4_rect)
      
      

clock = pygame.time.Clock()

while True:
  clock.tick(FPS)
  mouse = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if(ScreenList[current_screen]["option1"][0] != None and 700 <= mouse[0] <= 1300 and 160 <= mouse[1] <= 240):
        if(ScreenList[current_screen]["option1"][0] == "Quit" or ScreenList[current_screen]["option1"][0] == "Exit the game"):
          pygame.quit()
          sys.exit()
        current_screen = ScreenList[current_screen]["option1"][1]
        game_window.fill("white")
        game_window.blit(background_img, (0,0))
      if(ScreenList[current_screen]["option2"][0] != None and 700 <= mouse[0] <= 1300 and 280 <= mouse[1] <= 360):
        if(ScreenList[current_screen]["option2"][0] == "Quit" or ScreenList[current_screen]["option2"][0] == "Exit the game"):
          pygame.quit()
          sys.exit()
        current_screen = ScreenList[current_screen]["option2"][1]
        game_window.fill("white")
        game_window.blit(background_img, (0,0))
      if(ScreenList[current_screen]["option3"][0] != None and 700 <= mouse[0] <= 1300 and 400 <= mouse[1] <= 480):
        if(ScreenList[current_screen]["option3"][0] == "Quit" or ScreenList[current_screen]["option3"][0] == "Exit the game"):
          pygame.quit()
          sys.exit()
        current_screen = ScreenList[current_screen]["option3"][1]
        game_window.fill("white")
        game_window.blit(background_img, (0,0))
      if(ScreenList[current_screen]["option4"][0] != None and 700 <= mouse[0] <= 1300 and 520 <= mouse[1] <= 600):
        if(ScreenList[current_screen]["option4"][0] == "Quit" or ScreenList[current_screen]["option4"][0] == "Exit the game"):
          pygame.quit()
          sys.exit()
        current_screen = ScreenList[current_screen]["option4"][1]
        game_window.fill("white")
        game_window.blit(background_img, (0,0))
    
    load_screen(ScreenList[current_screen]["img_path"], ScreenList[current_screen]["map_path"], ScreenList[current_screen]["prompt"], ScreenList[current_screen]["option1"][0], ScreenList[current_screen]["option2"][0], ScreenList[current_screen]["option3"][0], ScreenList[current_screen]["option4"][0])
    #load_screen("california_trail_project\\ImageAssets\\HomeScreen\\home_screen_trail.png", "california_trail_project\\ImageAssets\\HomeScreen\\map_california_trail_homescreen.png", "Sample... Question?", "Next")
  title_text = TITLE_FONT.render("California Trail Game", True, "black")
  title_text_rect = title_text.get_rect()
  title_text_rect.center = (700, 20)
  game_window.blit(title_text, title_text_rect)
  # prompt_text = 
  pygame.display.update()
