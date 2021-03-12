import cv2

cap = cv2.VideoCapture("./video.mp4")
wanted_fps = 1.5
orig_fps = int(cap.get(cv2.CAP_PROP_FPS))

frame_c = 0
out_str = ''
size = 0

acc = 0.0
while True:
    if cap.grab():
        while True:
            flag, frame = cap.retrieve()
            if flag:
                acc += 1.0 / orig_fps
                break
    
    if acc > 1.0 / wanted_fps:
        acc -= 1.0 / wanted_fps
        frame = cv2.resize(frame, (32, 18), interpolation = cv2.INTER_LANCZOS4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, frame) = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

        out_str += 'FRAME' + str(frame_c) + '\tSTR\t\t'
        frame_c += 1

        for y in range(18):
            for x in range(5):
                # read 16 bits
                val = 0
                for i in range(16):
                    if frame[y, x + i] != 0:
                        val |= 1 << i
                out_str += str(val) + ','
                size += 1

        out_str = out_str[:len(out_str) - 1] + '\n'

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        break


out_str = '\t\tMVI\t\tR3, ' + str(size) + '\n' + out_str
print(out_str)
