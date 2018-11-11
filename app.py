####################################################################################################
"""
Tyler Tompa
2018, November, 10
UNCC Data Analytics Boot Camp Homework 11- Web Visualization Dashboard
"""
####################################################################################################


from flask import Flask

app = Flask(__name__)

# This defines what happens when the user hits the homepage.
@app.route("/")
def home():
    return "Welcome to the weather visualization homepage."

if __name__ == "__main__":
    app.run(debug=True)