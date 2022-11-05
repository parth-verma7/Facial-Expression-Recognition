from flask import Blueprint,render_template,Response,redirect,url_for
from flask_login import login_required,current_user
from .camera import Video
main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # return render_template('profile.html',name=current_user.name)
    return redirect(url_for('main.fer'))

@main.route('/fer')
def fer():
    return render_template('fer_index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@main.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')
