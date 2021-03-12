import cv2

cap = cv2.VideoCapture("./video.mp4")
wanted_fps = 2
orig_fps = int(cap.get(cv2.CAP_PROP_FPS))
skip_frames = orig_fps - wanted_fps

out_str = ''
size = 0

while True:
    for i in range(skip_frames):
        if cap.grab():
            while True:
                flag, frame = cap.retrieve()
                if flag:
                    break
    frame = cv2.resize(frame, (32, 18), interpolation = cv2.INTER_LANCZOS4)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, frame) = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

    for y in range(18):
        for x in range(5):
            # read 16 bits
            val = 0
            for i in range(16):
                if frame[y, x + i] != 0:
                    val |= 1 << i
            out_str += str(val) + ','
            size += 1
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        break

out_str = out_str[:len(out_str) - 1]
print(size)
print(out_str)
