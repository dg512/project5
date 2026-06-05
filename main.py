Web VPython 3.2

import random
sphere ()
s = []
for i in range(20) : 
    s.append(sphere(pos = vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))))

while True :
    rate(100)
    k = keysdown()
    r = random.randint(0,19)
    if ' ' in k : 
        s[0].color = color.red
        
    if s[r].color == color.red : 
        u.append(s[r])
        t = len(u)
        p = random.randint(0,t-1)
        for x in s :
            if (  (u[p].pos.x- x.pos.x)**2  +  (u[p].pos.y- x.pos.y)**2 )**0.5 < 2  : 
                x.color = color.red
    for x in s :
        if -10 < x.pos.x < 10 :
            x.pos.x += random.uniform(-0.2, 0.2)
        if -10 < x.pos.y < 10 :
            x.pos.y += random.uniform(-0.2, 0.2)
