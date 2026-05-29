Web VPython 3.2

import random
sphere ()
s = []
for i in range(20) : 
    s.append(sphere(pos = vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))))

while True :
    rate(30)
    k = keysdown()
    r = random.randint(0,19)
    
    for i in range(20):
        s[i].pos.x += random.uniform(-1, 1)
        s[i].pos.y += random.uniform(-1, 1)
        s[i].pos.z += random.uniform(-1, 1)

    if ' ' in k :
        rate(20)
        for i in range(20): 
            if i == r : 
                s[i].color = color.red
            else : 
                s[i].color = color.white
     for i in (1,3):
        if i == 1 :
            a = s[r] 
        else : 
            b = s[r]
    if (((a.pos.x- b.pos.x)*(a.pos.x- b.pos.x)+ (a.pos.y- b.pos.y)*(a.pos.y- b.pos.y))*((a.pos.x- b.pos.x)*(a.pos.x- b.pos.x)+ (a.pos.y- b.pos.y)*(a.pos.y- b.pos.y)))**0.5 < 2 : 
            a.color = color.red
            b.color = color.red
