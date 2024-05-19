from flask import render_template
from app import app, socketio

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@socketio.on('video_frame')
def handle_video_frame(data):
    print("Got frame")