from flask import Flask, jsonify
from flask_cors import CORS
import scratchattach as sa

app = Flask(__name__)
CORS(app)

# Define the route with a dynamic parameter called 'username'
@app.route('/<username>')
def get_user_followers(username):
    try:
        # Fetch the user data dynamically based on the URL parameter
        user = sa.get_user(username)
        count = user.follower_count()
        return jsonify({"username": username, "followers": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run()
