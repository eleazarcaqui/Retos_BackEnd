from flask import Flask,request,render_template
from profile import Profile
from firebase import FirebaseAdmin

app = Flask(__name__)

fb = FirebaseAdmin()

@app.route('/')
def layout():
    perfil = Profile()
    context = {
        'nombre': perfil.name,
    }
    return render_template('layout.html', **context)
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    lista_proyectos = fb.get_collection('portafolio')
    context = {
        'portafolio': lista_proyectos
    }
    return render_template('projects.html', **context)
@app.route('/resume')
def resume():
    return render_template('resume.html')

app.run(debug=True)