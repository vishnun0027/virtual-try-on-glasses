

import cv2
import  cvzone
from flask import Flask, render_template, Response,request
import cv2
import  cvzone
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

app = Flask(__name__)

camera = cv2.VideoCapture(0)
 
def gen_frames2(num):  # generate frame by frame from camera
        while True:
            
            overlay = cv2.imread('static/images/glass{}.png'.format(num), cv2.IMREAD_UNCHANGED)
            # Capture frame-by-frame
            success, frame = camera.read()
            # read the camera frame
            frame = cv2.flip(frame,1)
            if not success:
                break
            else:
                gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = cascade.detectMultiScale(gray_scale)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
                    overlay_resize = cv2.resize(overlay,(w,int(h*0.78)))
                    frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

def gen_frames():  # generate frame by frame from camera
    while True:
            # Capture frame-by-frame
            success, frame = camera.read()
            # read the camera frame
            frame = cv2.flip(frame,1)
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


           

# #------------------------------------------------------------------
@app.route('/video_frame',methods=['POST','GET'])
def video_frame():
    if request.method == 'POST':
        global num
        if 'glass1' in request.form:
            num=1
        elif 'glass2' in request.form:
            num=2
        elif 'glass3' in request.form:
            num=3
        elif 'glass4' in request.form:
            num=4
        elif 'glass5' in request.form:
            num=5

        if num!=None:
            
            res='Yes'
            # return redirect(url_for('video_feed2'))
        return render_template('index.html',num=res)


        
        
        

        
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    global num
    return Response(gen_frames2(num), mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/',methods=['GET'])
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)