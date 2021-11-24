import cv2
import subprocess as sp
from capture_utils import FPS

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)
ret, frame = cap.read()
height, width, ch = frame.shape

ffmpeg = 'ffmpeg'
dimension = '{}x{}'.format(width, height)
f_format = 'bgr24' # remember OpenCV uses bgr format
fps = str(cap.get(cv2.CAP_PROP_FPS))
print(frame.shape)

command = [ffmpeg,
        '-y',
        '-f', 'rawvideo',
        '-c:v','rawvideo',
        '-s', dimension,
        '-pix_fmt', 'bgr24',
        # '-r', "15",'-vsync', '0',
        '-vsync', 'drop',
        # '-avoid_negative_ts', '1',
        '-fflags', '+genpts',
        '-use_wallclock_as_timestamps','1',
        '-i', '-',
        '-f', 'rtsp',
        '-rtsp_transport', 'tcp',
        #'-b:v', '50k',
        '-vsync', 'vfr',
        # '-an',
        '-copyts',
        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-pix_fmt', 'yuv420p',
        'rtsp://localhost:8554/cam2']


proc = sp.Popen(command, stdin=sp.PIPE, stderr=sp.DEVNULL, stdout=sp.DEVNULL, close_fds=True)
fps = FPS().start()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # stdout = proc.communicate()[1]
    # print('STDOUT:{}'.format(stdout))
    #if proc.poll():
    # print(proc.poll())
    # print(proc.communicate())
    proc.stdin.write(frame.tostring())
    # print(proc.stderr.readline().decode())
    fps.update()
    print(fps.fps())
    
    if (fps._numFrames == 100):
        fps = FPS().start()

cap.release()
proc.stdin.close()
proc.stderr.close()
proc.wait()
