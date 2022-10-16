from flask import Flask,session,render_template,flash,url_for,request,redirect, Response
import os
import recommend
from werkzeug.utils import secure_filename
import model
import cv2

CLASS_LABELS = {
    0:'angry',
    1:'disgust',
    2:'fear',
    3:'happy',
    4:'neutral',
    5:"sad",
    6:"surprise"
}
global TARGET
global frame

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/mood',methods = ['GET', 'POST'])
def mood():
    global frame
    if request.method == 'POST':
        f = cv2.imwrite(app.config['UPLOAD_FOLDER'], frame)
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        detFace_fromImg = model.detectFace(filename)
        if detFace_fromImg == -999:
            return render_template("noImg.html")
        else:
            target = model.giveLabel(f"{app.config['UPLOAD_FOLDER']}{detFace_fromImg}_predicted.jpg")
            TARGET = CLASS_LABELS[target]
            return redirect(url_for(userRecommendation))
    return render_template("mood.html")

@app.route('/recommendation',methods = ['GET', 'POST'])
def userRecommendation():
    return render_template("requestPage.html")

@app.route('/withoutimage',methods = ['GET','POST'])
def withoutImage():
    choice = ['happy','sad','neutral','angry','surprise','fear','disgust'] 
    if request.method == 'POST':
        option = request.form.getlist('options')
    return render_template("without_image.html",emotions = choice)
    
@app.route('/movie')
def movieRecommend():
    movieEngine = recommend.movieRecommendation("happy")
    dataDict = {"Movie":list(movieEngine['Anime']),'Description':list(movieEngine['Description'])}
    movieData = zip(dataDict['Movie'],dataDict['Description'])
    return render_template('movie.html',name=movieData)

@app.route('/song')
def songRecommend():
    songEngine = recommend.songRecommendation("happy")
    dataDict = {"Artist":list(songEngine['artist']),'Album':list(songEngine['album']),'Name':list(songEngine['name'])}
    songData = zip(dataDict['Name'],dataDict['Album'],dataDict['Artist'])
    return render_template('song.html',name = songData)

def gen_frames():  # generate frame by frame from camera
    global out, capture,rec_frame, frame
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        try:
            ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            pass

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=False)