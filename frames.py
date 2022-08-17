import cv2
def convert_frames():
    cap = cv2.VideoCapture("input_video/sample.mp4")
    print("Converting to frames")
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    x = int(length/10)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('LR/frame{:d}.jpg'.format(count), frame)
            count += x # at 3000 fps, this advances one second
            cap.set(1, count)
        else:
            cap.release()
            break