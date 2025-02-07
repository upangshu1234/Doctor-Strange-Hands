import cv2
import mediapipe as mp

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

video=cv2.VideoCapture(0)

video.set(3, 1000)
video.set(4, 780)


img_1 = cv2.imread('magic_circles/magic_circle_ccw.png', -1)
img_2 = cv2.imread('magic_circles/magic_circle_cw.png', -1)

deg=0

def position_data(lmlist):
    global wrist, thumb_tip, index_mcp, index_tip, midle_mcp, midle_tip, ring_tip, pinky_tip
    wrist = (lmlist[0][0], lmlist[0][1])
    thumb_tip = (lmlist[4][0], lmlist[4][1])
    index_mcp = (lmlist[5][0], lmlist[5][1])
    index_tip = (lmlist[8][0], lmlist[8][1])
    midle_mcp = (lmlist[9][0], lmlist[9][1])
    midle_tip = (lmlist[12][0], lmlist[12][1])
    ring_tip  = (lmlist[16][0], lmlist[16][1])
    pinky_tip = (lmlist[20][0], lmlist[20][1])


def draw_line(p1, p2, size=5):
    cv2.line(img, p1, p2, (50,50,255), size)
    cv2.line(img, p1, p2, (255, 255, 255), round(size / 2))

def calculate_distance(p1,p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    lenght = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
    return lenght


def transparent(targetImg, x, y, size=None):
    if size is not None:
        targetImg = cv2.resize(targetImg, size)

    newFrame = img.copy()
    b, g, r, a = cv2.split(targetImg)
    overlay_color = cv2.merge((b, g, r))
    mask = cv2.medianBlur(a, 1)
    h, w, _ = overlay_color.shape
    roi = newFrame[y:y + h, x:x + w]

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
    newFrame[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return newFrame
 

while True:
    ret,img=video.read()
    img=cv2.flip(img, 1)
    rgbimg=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result=hands.process(rgbimg)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lmList=[]
            for id, lm in enumerate(hand.landmark):
                h,w,c=img.shape
                coorx, coory=int(lm.x*w), int(lm.y*h)
                lmList.append([coorx, coory])
                # cv2.circle(img, (coorx, coory),6,(50,50,255), -1)
            # mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
            position_data(lmList)
            palm = calculate_distance(wrist, index_mcp)
            distance = calculate_distance(index_tip, pinky_tip)
            ratio = distance / palm
            print(ratio)
            if (1.3>ratio>0.5):
                draw_line(wrist, thumb_tip)
                draw_line(wrist, index_tip)
                draw_line(wrist, midle_tip)
                draw_line(wrist, ring_tip)
                draw_line(wrist, pinky_tip)
                draw_line(thumb_tip, index_tip)
                draw_line(thumb_tip, midle_tip)
                draw_line(thumb_tip, ring_tip)
                draw_line(thumb_tip, pinky_tip)
            if (ratio > 1.3):
                    centerx = midle_mcp[0]
                    centery = midle_mcp[1]
                    shield_size = 3.0
                    diameter = round(palm * shield_size)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))
                    h, w, c = img.shape
                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1
                    shield_size = diameter, diameter
                    ang_vel = 2.0
                    deg = deg + ang_vel
                    if deg > 360:
                        deg = 0
                    hei, wid, col = img_1.shape
                    cen = (wid // 2, hei // 2)
                    M1 = cv2.getRotationMatrix2D(cen, round(deg), 1.0)
                    M2 = cv2.getRotationMatrix2D(cen, round(360 - deg), 1.0)
                    rotated1 = cv2.warpAffine(img_1, M1, (wid, hei))
                    rotated2 = cv2.warpAffine(img_2, M2, (wid, hei))
                    if (diameter != 0):
                        img = transparent(rotated1, x1, y1, shield_size)
                        img = transparent(rotated2, x1, y1, shield_size)


    # print(result)
    cv2.imshow("Image",img)
    k=cv2.waitKey(10)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()