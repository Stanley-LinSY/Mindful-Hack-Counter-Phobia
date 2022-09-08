import cv2
from flask import Flask, render_template, Response

Counter_Phobia = Flask(__name__)
camera = cv2.VideoCapture(0)
Counter_Phobia.static_folder = 'static'


def generate_frames1():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = cv2.GaussianBlur(frame, (19, 19), cv2.BORDER_DEFAULT)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames2():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = cv2.GaussianBlur(frame, (11, 11), cv2.BORDER_DEFAULT)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames3():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@Counter_Phobia.route('/')
def index():
    return render_template('index.html')

@Counter_Phobia.route('/video1')
def video1():
    return Response(generate_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@Counter_Phobia.route('/video2')
def video2():
    return Response(generate_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@Counter_Phobia.route('/video3')
def video3():
    return Response(generate_frames3(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    Counter_Phobia.run(debug = True)