from flask import Flask, jsonify, request, g
from db_utils import query_db, write_db, init_db

app = Flask(__name__)


@app.before_first_request
def _run_on_start():
    init_db(app)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()


@app.route('/api/v1/users/<string:user_id>/ratings/', methods=['GET'])
def get_ratings(user_id):
    ratings = query_db("select * from ratings WHERE user_id = ?", [user_id])
    return jsonify(ratings)


@app.route('/api/v1/users/<string:user_id>/ratings/', methods=['POST'])
def set_ratings(user_id):
    write_db(
        "insert or replace into ratings (user_id, film_id, rating) values (?, ?, ?)",
        [user_id, request.json['film_id'], request.json['rating']]
    )
    #return jsonify([{'id': 1, 'rating': 9}, {'id': 2, 'rating': 10}])

