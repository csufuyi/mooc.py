# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''can replay point painter:
+ 3 kinds paintrt
+ setup color
+ recoder 1024 points
+ replay all painting
+ dump/load people painting
'''

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#import simplegui
import time
#import pickle

HIGH  = 740
WIDTH = 700
REPAINT = []
REVIEW = []
PEN = {'color':'blue'
    , 'shape':'watercolor'
    , 'radius':16
    , 'line':2
    }
LIMIT = 1024
AUTO_STEP = 0
timer_interval = 42 # In milliseconds (1000 ms = 1 s)
MSG = ['','']

def timer_handler():
    global REPAINT,REVIEW,AUTO_STEP
    print "REPAINT>", len(REPAINT), "REVIEW>", len(REVIEW)
    REPAINT= []
    #AUTO_STEP = len(REVIEW)
    if AUTO_STEP < len(REVIEW):
        AUTO_STEP += 1
        for j in range(0, AUTO_STEP):
            #print j
            #print REVIEW[j]
            REPAINT.append(REVIEW[j])
    else:
        AUTO_STEP = 0
        REPAINT = REVIEW
        timer.stop()

def auto_review():
    global timer, MSG
    MSG = ['','']
    if timer.is_running():      
        timer.stop()
    else:
        timer = simplegui.create_timer(timer_interval, timer_handler)
        timer.start()

def click_point(position):
    global LIMIT, REPAINT, REVIEW
    x = position[0]
    y = position[1]
    print "\npoint->", position
    if PEN['shape'] == 'circle':
        p = [x,y]
    elif PEN['shape'] == 'watercolor':
        p = [x,y]
    elif PEN['shape'] == 'square':
        p = [(x-PEN['radius'],y-PEN['radius'])
                ,(x+PEN['radius'],y-PEN['radius'])
                ,(x+PEN['radius'],y+PEN['radius'])
                ,(x-PEN['radius'],y+PEN['radius'])
            ]
    elif PEN['shape'] == 'triangle':
        p = [(x,y+PEN['radius'])
                ,(x-PEN['radius'],y-PEN['radius']/2)
                ,(x+PEN['radius'],y-PEN['radius']/2)
            ]

    LIMIT -= 1
    if LIMIT <=0:
        lab_shape.set_text('ALERT OVER 1024 point...')
    else:
        REPAINT.append([p 
                , PEN['color'] 
                , PEN['shape']
                , PEN['radius']
                , PEN['line']
                ])
    REVIEW = REPAINT     
    #    REPAINT.append([p,PEN['color'],PEN['shape']])
    #else:
    #    lab_shape.set_text('ALERT OVER 1024 point...')

def draw_all(canvas):
    #global REPAINT
    #print REPAINT 
    for p in REPAINT:
        #print p
        if p[2]=='circle':
            canvas.draw_circle(p[0] # shape
                , p[3] # radius
                , p[4] # line
                , p[1] # color
                , p[1])
        elif p[2]=='watercolor':
            for x in range(p[0][0]-p[3], p[0][0]+p[3]):
		for y in range(p[0][1]-p[3], p[0][1]+p[3]):
                    canvas.draw_point([x, y], p[1])
        else:
            canvas.draw_polygon(p[0] # shape 
                , p[4] #line
                , p[1]
                , p[1])

def hdl_circle():
    PEN['shape'] = 'circle'
    tag_shape_now('circle')
def hdl_watercolor():
    PEN['shape'] = 'watercolor'
    tag_shape_now('watercolor')
def hdl_square():
    PEN['shape'] = 'square'
    tag_shape_now('square')
def hdl_triangle():
    PEN['shape'] = 'triangle'
    tag_shape_now('triangle')
def tag_shape_now(tag):
    lab_shape.set_text("now painter: %s"% tag)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Point Drawer",WIDTH, HIGH )
frame.set_canvas_background('Black') # White # Black
#frame.add_label('- Please select shape - ')

lab_totle = frame.add_label('')

lab_shape = frame.add_label('default as circle')
btn_circle = frame.add_button("(*)", hdl_circle ,   30)
btn_square = frame.add_button("[*]", hdl_square,    30)
btn_triangle = frame.add_button("/\\", hdl_triangle, 29)
btn_watercolor = frame.add_button("~", hdl_watercolor, 30)

def hdl_red():
    PEN['color'] = 'red'
    tag_color_now('red')
def hdl_blue():
    PEN['color'] = 'blue'
    tag_color_now('blue')
def hdl_green():
    PEN['color'] = 'green'
    tag_color_now('green')
def hdl_black():
    PEN['color'] = 'black'
    tag_color_now('black')
def hdl_silver():
    PEN['color'] = 'silver'
    tag_color_now('Silver')
def hdl_white():
    PEN['color'] = 'white'
    tag_color_now('white')
def tag_color_now(tag):
    lab_color.set_text("now Color: %s"% tag)

lab_color = frame.add_label('Choice Color')

frame.add_button("red", hdl_red,        50)
frame.add_button("blue", hdl_blue,      50)
frame.add_button("green", hdl_green,    50)
frame.add_button("black", hdl_black,    50)
frame.add_button("Silver", hdl_silver,  50)
frame.add_button("White", hdl_white,    50)

def color_input(color_txt):
    PEN['color'] = color_txt
    print PEN['color']
inp_color = frame.add_input('or input as Yellow/#FF00EE'
        ,color_input,100)
inp_color.set_text('Purple')

frame.add_label('need enter for work...')

def hdl_S():
    PEN['radius'] = 2
    PEN['line'] = 1
    tag_size_now('S')
def hdl_M():
    PEN['radius'] = 4
    PEN['line'] = 1
    tag_size_now('M')
def hdl_L():
    PEN['radius'] = 6
    PEN['line'] = 1
    tag_size_now('L')
def hdl_XL():
    PEN['radius'] = 8
    PEN['line'] = 1
    tag_size_now('XL')
def hdl_XXL():
    PEN['radius'] = 12
    PEN['line'] = 2
    tag_size_now('XXL')
def hdl_XXXL():
    PEN['radius'] = 16
    PEN['line'] = 3
    tag_size_now('XXXL')
def tag_size_now(tag):
    lab_size.set_text("now Size: %s"% tag)

lab_size = frame.add_label('Choice Size')
frame.add_button("S",   hdl_S,      40)
frame.add_button("M",   hdl_M,      40)
frame.add_button("L",   hdl_L,      40)
frame.add_button("XL",  hdl_XL,     40)
frame.add_button("XXL", hdl_XXL,    40)
frame.add_button("XXXL",hdl_XXXL,   40)
frame.add_label('   ')

def btn_clean():
    global REPAINT, REVIEW
    REPAINT = []
    REVIEW = []
    print "CLEAN all point restart!"

frame.add_button('CLEAN',btn_clean,100)

frame.add_label('~'*11)
frame.add_button('start/stop auto-review',auto_review,100)


frame.add_label('-'*11)

def _load_point(ppstr):
    print ppstr
    _li = ppstr.split('+')
    _pp = []
    for p in _li:
        print p
        _info = p.split('-')
        if 5 == len(_info):
            print "is circle point"
            _xy = _info[0].split('_')
            _pp.append([[int(_xy[0]), int(_xy[1])]
                , _info[1]
                , _info[2]
                , int(_info[3])
                , int(_info[4])
                ])
        else:
            print "is others point"
            _len = len(_info)
            #print _len
            print _info[:-4]
            fix = []
            for xy in _info[:-4]:
                _xy = xy.split('_')
                fix.append(( int(_xy[0]), int(_xy[1]) ))
            print "load as>", fix
            _pp.append([ fix
                , _info[-4]
                , _info[-3]
                , int(_info[-2])
                , int(_info[-1])
                ])
    return _pp

# for shape types
# [180, 196], 'red', 'circle', 4, 2]
# [(174, 154), (172, 151), (176, 151)], 'silver', 'triangle', 2, 0.3]

def load_pp4sae(uri): 
    global REVIEW, MSG
    print "load outdoor pplist for REVIEW"
    print uri
    #uri = 'http://zoomquiet-ppreload.stor.sinaapp.com/15040214283617515_pp.log'
    echo_txt = urllib2.urlopen(uri)
    pplist = echo_txt.read()
    _pp = _load_point(pplist)
    REVIEW = _pp
    #REVIEW.append([[int(x), int(y)]
    #        , color
    #        , shape
    #        , int(radius)
    #        , int(line)
    #        ])
    MSG[0] = "load outdoor pplist %s points"% len(REVIEW)
    MSG[1] = "from %s "% uri

def draw_echo(canvas):
    global MSG
    canvas.draw_text(MSG[0], (10, 60), 20, "Lime")
    canvas.draw_text(MSG[1], (50, 60), 14, "Lime")
frame.set_draw_handler(draw_echo)


    
import urllib2
def btn_dump():
    '''usage SAE srv
    - base HTTP get method, upload data
    - echo load URI for sharing
    '''
    print "saved painting %s points"% len(REVIEW)
    print REVIEW
    _exp = []
    for pp in REVIEW:
        print pp[0]
        p4shape = []
        if 2 == len(pp[0]):
            print "is circle"
            p4shape.append("%s_%s"% (pp[0][0], pp[0][1]))
        else:
            for s in pp[0]:
                print s
                p4shape.append("%s_%s"% (s[0], s[1]))
        print p4shape
        _encode = "%s-%s-%s-%s-%s"% ("-".join(p4shape)
            , pp[1]
            , pp[2]
            , pp[3]
            , pp[4]
            )
        _exp.append(_encode)
        print _encode
    #print "+".join(_exp)
    put_points = "+".join(_exp)
    print put_points
    _SAE = 'http://zoomquiet.sinaapp.com/api/echo'
    echo_txt = urllib2.urlopen('%s/%s'% (_SAE, put_points) )
    _uri = echo_txt.read()
    print _uri
    inp_dump_sae.set_text(_uri)

frame.add_button('dump painting',btn_dump,100)
# http://zoomquiet-ppreload.stor.sinaapp.com/15040214283617515_pp.log

inp_dump_sae = frame.add_input('reload URI'
        ,load_pp4sae ,150)

frame.set_draw_handler(draw_all)
frame.set_mouseclick_handler(click_point)
frame.set_canvas_background('White')

timer = simplegui.create_timer(timer_interval, timer_handler)

frame.start()

