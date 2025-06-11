from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/hobbies/photography')
def photography():
    return render_template('photography.html')

@app.route('/hobbies/gaming')
def gaming():
    return render_template('gaming.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/404')
def not_found():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)