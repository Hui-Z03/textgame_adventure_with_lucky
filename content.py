# content.py - This is game content
# 13 scenes 20240905
# Template
#    'scene': {
#        'description':'**\n1. * \n2.*',
#        'choices':{'1':'***', '2':'***'},
#        'image': 'static/images/***.jpg'},
#   
#
game_content = {
# story 1, 1, 1, 1, 1, ending
    'start': {
        'description':'This a nice day, your are playing beside the forest not far from your home, than a puppy comes to you.\
        \nThe puppy says:"Hello, my name is Lucky. My mom is stuck in the forest. Can you help me, please?"\
        \n1. Help the puppy \n2. Don\'t help',
        'choices':{'1':'into_forest', '2':'no_help'},
        'image': 'static/images/start.jpg'},

    'into_forest': {
        'description':'You want to help Lcuky, so you run home call your daddy. The three of you walk into the forest together.\
        \nNow you see a creek which is too deap for a puppy.\
        \n1. Looking for a log to make a bridge for Lucky \n2. Holding Lucky and across the river',
        'choices':{'1':'found_log', '2':'holding_lucky'},
        'image': 'static/images/into_forest.jpg'},
    
    'found_log': {
        'description':'You find a big log to make a bridge for Lucky to cross, then cross the river yourself.\
        \nNow, you reach a fork in the road.\
        \n1. a sunny path \n2. a dark_cave',
        'choices':{'1':'sunny_path', '2':'dark_cave'},
        'image': 'static/images/found_log.jpg'},

    'sunny_path': {
        'description':'You are walking on a sunny path with flowers and birds singing. Suddenly, a wolf jump out.\
        \nThe wolf says"If you can answer my question, you can leave.\
        \nI picked 10 strawberries, ate 4, and then picked 7 more. How many strawberries do I have now?"\
        \n1. 13 strawberries \n2. 12 strawberries',
        'choices':{'1':'find_mom', '2':'wolf_answer_incorrect'},
        'image': 'static/images/sunny_path.jpg'},

    'find_mom': {
        'description':'Well done! You keep on going.\
        \nFinally, you find Lucky\'s mom stuck in a bush\
        \n1. Dig with your hands \n2. call daddy for help',
        'choices':{'1':'ending_hand', '2':'ending_daddy'},
        'image': 'static/images/find_mom.jpg'},

    'ending_hand': {
        'description':'You start dig with your hands, Lucky fetch a stick to help.\
        \nYou save Lucky\'s mom! Lucky is very happy and thank you. You become friends and play togther often.\
        \n1. Play again \n2. End the game',
        'choices':{'1':'start', '2':'end_game'},
        'image': 'static/images/ending_hand.jpg'},

# story 1, 2
    'holding_lucky': {
        'description':'You try to hold lucky, but the rocks in the creek are too slippery, and you almost fell.\
        \n1. Let\'s find a log',
        'choices':{'1':'found_log'},
        'image': 'static/images/holding_lucky.jpg'},

# story 1, 1, 2, 1    
    'dark_cave': {
        'description':'In the dark cave, a big black stone block the way. You\'re a little scared\
        \n1.All three of you try to push the stone \n2. Go back ',
        'choices':{'1':'find_mom', '2':'go_back'},
        'image': 'static/images/dark_cave.jpg'},

#story 1, 1, 2, 2    
    'go_back': {
        'description':'The stone is too big, and you go back seek another way.\
        \n1.You go back to the creek',
        'choices':{'1':'found_log'},
        'image': 'static/images/go_back.jpg'},

#story 1, 1, 1, 2, 
    'wolf_answer_incorrect': {
        'description':'Wrong answer!\
        \n1.Try again',
        'choices':{'1':'sunny_path'},
        'image': 'static/images/wolf_answer_incorrect.jpg'},

#story 2nd ending
    'ending_daddy': {
        'description':'You call daddy for help, and daddy pulled the bushes aside and you rescued Lucky\'s mom.\
        \nLucky is very happy and thank you. You become friends and play togther often.\
        \n1.Play again \n2. End the game',
        'choices':{'1':'start', '2':'end_game'},
        'image': 'static/images/ending_daddy.jpg'},

#story no help ending
    'no_help': {
        'description':'You refuse to help.',
        'choices':{},
        'image': 'static/images/no_help.jpg'},

#story end
    'end_game': {
        'description':'Thank you for playing my game.',
        'choices':{},
        'image': 'static/images/end_game.jpg'}
}
