from wiki_scrape import get_popular_page, get_random_page

from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/wiki_game')
@cross_origin()
def wiki_game():
    random_page = get_random_page()
    popular_page = get_popular_page()
    return render_template('wiki_game.html', random_page=random_page.name, random_id=random_page.id, popular_page=popular_page)

@app.route('/')
@cross_origin()
def health_check():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

    # FLASK_APP=main.py FLASK_ENV=development flask run