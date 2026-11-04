"""Book 2 (plates XI-XX). Coordinates are native panel pixels (see grid sheets)."""
import sys
from animate import *

def drift(sc, bbox, ax=3.0, ay=0.0, k=1, phase=0.0, sigma=5, keep_out=None):
    m = sc.soft(sc.box(*bbox), sigma)
    if keep_out is not None:
        m = m*(1 - sc.soft(sc.box(*keep_out), 3))
    sc.shift(m, lambda t: (ax*np.sin(TAU*k*t/T + phase), ay*np.sin(TAU*k*t/T + phase + 1.2)))
    return m

def s11():   # galaxy
    sc = Scene(11)
    sc.galaxy(163, 112, 92, 0.55, -33, amp=7)
    sc.glow(sc.ellipse(165, 110, 22, 14), amp=0.3, k=2)
    sc.stars((0, 0, 287, 215), exclude=[(80, 40, 260, 190)])
    sc.shooting_star((270, 175), (190, 225), t0=4.3, dur=1.0)
    sc.scarf((10, 205, 96, 335), (97, 255), amp=2.8, wl=60)
    sc.hair((68, 212, 128, 268), (100, 216), amp=0.9)
    sc.breathe((60, 215, 175, 335), 333, 220, amp=0.45, k=2)
    sc.planet(122, 432, 112, 16, amp=2.5)
    return sc

def s12():   # rocket
    sc = Scene(12)
    grp = sc.soft(sc.box(0, 128, 245, 345), 6)
    sc.shift(grp, lambda t: (0.8*np.sin(TAU*t/T + 1.0), 3.0*np.sin(TAU*t/T)))
    sc.rotate((160, 230), grp, lambda t: 1.2*np.sin(TAU*t/T + 0.6))
    flame = sc.soft(sc.box(0, 215, 108, 345), 5) * np.clip((96*S - sc.X)/(25*S), 0, 1)
    sc.flicker(flame, (-0.75, 0.6), amp=1.6)
    sc.glow(flame*0.8, color=(120, 200, 255), amp=0.25, k=10)
    sc.scarf((128, 160, 180, 196), (172, 170), amp=1.6, wl=30, k=3)
    sc.hair((140, 128, 195, 175), (169, 135), amp=0.9, k=3)
    sc.stars((0, 0, 278, 130))
    sc.planet(267, 613, 246, 0, amp=1.2)
    return sc

def s13():   # factory
    sc = Scene(13)
    for bb, k in [((165, 0, 282, 86), 1), ((70, 95, 112, 150), 2), ((244, 95, 282, 140), 2)]:
        sc.billow(bb, amp=2.2, k=k)
    sc.glow(sc.ellipse(191, 272, 22, 28, p=1)*0.9, amp=0.25, k=2)
    for (bb, piv, ph) in [((228, 272, 265, 345), (246, 340), 0.0), ((170, 262, 196, 300), (182, 298), 2.0),
                          ((133, 268, 155, 300), (143, 298), 4.0)]:
        m = sc.soft(sc.box(*bb), 2)
        sc.shift(m, (lambda ph: lambda t: (0, -0.8*(0.5 - 0.5*np.cos(TAU*2*t/T + ph))))(ph))
        sc.rotate(piv, m, (lambda ph: lambda t: 2.0*np.sin(TAU*t/T + ph))(ph))
    sc.scarf((10, 288, 96, 366), (107, 298), amp=2.8, wl=60)
    sc.hair((82, 243, 132, 300), (105, 247), amp=0.9)
    sc.breathe((78, 248, 138, 438), 436, 250, amp=0.5, k=2)
    return sc

def s14():   # conveyor
    sc = Scene(14)
    claw = sc.soft(sc.box(176, 104, 238, 222), 3)
    sc.rotate((211, 106), claw, lambda t: 3.0*np.sin(TAU*t/T))
    sc.glow(sc.ellipse(166, 376, 24, 20, p=1), amp=0.3, k=3)
    sc.glow(sc.ellipse(163, 340, 7, 9), color=(170, 240, 255), amp=0.6, k=5, phase=1.0)
    head = sc.ellipse(210, 305, 26, 24)
    sc.rotate((210, 338), head, lambda t: 3.0*np.sin(TAU*t/T + 0.5))
    hands = sc.ellipse(140, 345, 16, 10)
    sc.shift(hands, lambda t: (0.8*np.sin(TAU*2*t/T), 0.5*np.sin(TAU*2*t/T + 1)))
    sc.scarf((0, 280, 108, 348), (118, 292), amp=2.8, wl=60)
    sc.hair((85, 232, 150, 292), (118, 238), amp=0.9)
    sc.breathe((70, 235, 150, 420), 420, 240, amp=0.45, k=2)
    return sc

def s15():   # reaching for a ringed planet
    sc = Scene(15)
    for (cx, cy, rx, ry, ph) in [(216, 124, 58, 36, 0.0), (34, 162, 15, 15, 2.0), (241, 265, 16, 16, 4.0)]:
        m = sc.ellipse(cx, cy, rx, ry, p=3)
        sc.shift(m, (lambda ph: lambda t: (0.6*np.sin(TAU*t/T + ph + 1), 2.2*np.sin(TAU*t/T + ph)))(ph))
    sc.rotate((216, 124), sc.ellipse(216, 124, 58, 36, p=3), lambda t: 2.0*np.sin(TAU*t/T + 0.3))
    sc.stars((0, 0, 288, 200), only=[(228, 47), (75, 89)])
    sc.shooting_star((20, 40), (110, 85), t0=3.8)
    sc.scarf((5, 236, 120, 330), (123, 219), amp=3.0, wl=65)
    sc.hair((93, 168, 152, 232), (125, 172), amp=0.9)
    sc.breathe((95, 165, 175, 405), 403, 170, amp=0.6, k=1)
    m = sc.soft(sc.box(135, 175, 195, 220), 3) * np.clip((sc.X - 140*S)/(40*S), 0, 1)
    sc.shift(m, lambda t: (1.2*(0.5 - 0.5*np.cos(TAU*t/T)), -1.2*(0.5 - 0.5*np.cos(TAU*t/T))))
    sc.planet(140, 533, 130, 10, amp=2.2)
    return sc

def s16():   # sitting with the robot
    sc = Scene(16)
    ring = sc.ellipse(201, 122, 72, 34, p=3)
    sc.shift(ring, lambda t: (0.5*np.sin(TAU*t/T + 1), 2.0*np.sin(TAU*t/T)))
    sc.rotate((201, 122), ring, lambda t: 1.8*np.sin(TAU*t/T + 0.4))
    sc.stars((0, 0, 287, 240), exclude=[(125, 80, 275, 165)])
    sc.shooting_star((260, 30), (170, 80), t0=4.6)
    head = sc.ellipse(181, 330, 24, 26)
    sc.rotate((182, 362), head, lambda t: 4.0*ease_hold(t, 1.0, 2.4, 4.4, 5.8))
    sc.scarf((15, 236, 90, 295), (108, 298), amp=2.8, wl=55)
    sc.hair((73, 243, 138, 302), (108, 248), amp=0.9)
    sc.breathe((70, 245, 150, 375), 373, 250, amp=0.45, k=2)
    sc.planet(145, 716, 338, 14, amp=1.0)
    return sc

def s17():   # map and floating castle
    sc = Scene(17)
    castle = sc.soft(sc.box(140, 105, 248, 215), 5)
    sc.shift(castle, lambda t: (0.6*np.sin(TAU*t/T + 1), 2.6*np.sin(TAU*t/T)))
    sc.glow(sc.ellipse(195, 150, 50, 38, p=1), amp=0.15, k=2)
    arm = sc.soft(sc.box(200, 350, 244, 372), 2) * np.clip((sc.X - 198*S)/(10*S), 0, 1)
    sc.rotate((201, 363), arm, lambda t: 3.0*np.sin(TAU*2*t/T))
    head = sc.ellipse(172, 352, 22, 20)
    sc.rotate((172, 375), head, lambda t: 2.5*np.sin(TAU*t/T + 1.5))
    mp = sc.soft(sc.box(95, 284, 140, 360), 3) * np.clip((sc.X - 95*S)/(40*S), 0, 1)
    sc.shift(mp, lambda t: (0, 1.0*np.sin(TAU*3*t/T - sc.Y/(14*S))))
    sc.stars((0, 0, 278, 210), only=[(165, 88), (38, 171)])
    sc.scarf((0, 244, 70, 310), (79, 281), amp=2.8, wl=55)
    sc.hair((53, 222, 118, 288), (85, 228), amp=0.9)
    sc.breathe((50, 225, 145, 445), 443, 230, amp=0.5, k=2)
    return sc

def s18():   # sprout under glass
    sc = Scene(18)
    sc.rotate((168, 363), sc.ellipse(168, 326, 26, 32), lambda t: 2.5*np.sin(TAU*t/T))
    sc.glow(sc.ellipse(168, 330, 45, 40), amp=0.35, k=2)
    sc.stars((0, 0, 282, 270), only=[(82, 107), (191, 173), (172, 241)])
    sc.shooting_star((265, 40), (175, 90), t0=4.0)
    sc.scarf((0, 245, 76, 345), (89, 255), amp=2.8, wl=60)
    sc.hair((62, 203, 128, 262), (90, 207), amp=0.9)
    sc.breathe((55, 205, 128, 400), 397, 210, amp=0.5, k=2)
    lean = sc.ellipse(92, 270, 30, 60)
    sc.rotate((92, 330), lean, lambda t: 1.3*ease_hold(t, 1.0, 3.0, 4.6, 6.6))
    return sc

def s19():   # hot air balloon
    sc = Scene(19)
    grp = sc.soft(sc.box(52, 32, 236, 328), 5)
    sc.shift(grp, lambda t: (1.5*np.sin(TAU*t/T + 1.3), 3.5*np.sin(TAU*t/T)))
    sc.rotate((142, 120), grp, lambda t: 0.8*np.sin(TAU*t/T + 0.3))
    for bb, ax, ph in [((0, 192, 72, 246), 4.0, 0.0), ((222, 170, 286, 224), 3.0, 1.5),
                       ((204, 322, 286, 390), 3.5, 3.0), ((0, 365, 122, 448), 4.5, 4.5)]:
        drift(sc, bb, ax=ax, phase=ph, sigma=6, keep_out=(55, 35, 233, 325))
    sc.scarf((70, 258, 126, 288), (134, 255), amp=2.2, wl=35, k=2)
    sc.hair((118, 222, 158, 265), (138, 226), amp=0.8, k=2)
    sc.rotate((184, 268), sc.ellipse(184, 252, 14, 14), lambda t: 3.0*np.sin(TAU*t/T + 2))
    return sc

def s20():   # shooting star and distant city
    sc = Scene(20)
    sc.comet_sweep((100, 150), (237, 65), k=1)
    sc.stars((0, 0, 288, 240), only=[(91, 80), (101, 148), (235, 157)])
    city = sc.soft(sc.box(185, 250, 280, 306), 3)
    sc.shimmer(city, amp=0.5)
    sc.glow(sc.ellipse(232, 284, 48, 22, p=1), amp=0.15, k=2)
    drift(sc, (135, 296, 288, 322), ax=3.0, sigma=4)
    sc.scarf((5, 285, 75, 380), (73, 298), amp=2.8, wl=60)
    sc.hair((38, 243, 102, 302), (68, 247), amp=0.9)
    sc.breathe((35, 245, 145, 380), 377, 250, amp=0.45, k=2)
    sc.planet(150, 658, 280, 14, amp=1.3)
    return sc

SCENES = {11: s11, 12: s12, 13: s13, 14: s14, 15: s15, 16: s16, 17: s17, 18: s18, 19: s19, 20: s20}
NAMES = {11: '11-the-galaxy', 12: '12-rocket-ride', 13: '13-the-factory', 14: '14-the-conveyor',
         15: '15-ringed-planet', 16: '16-sitting-with-robot', 17: '17-the-floating-castle',
         18: '18-the-sprout', 19: '19-hot-air-balloon', 20: '20-the-distant-city'}
if __name__ == '__main__':
    which = [int(a) for a in sys.argv[2:]] or list(SCENES)
    for i in which:
        SCENES[i]().render(NAMES[i])
