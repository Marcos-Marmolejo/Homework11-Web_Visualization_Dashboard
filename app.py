####################################################################################################
"""
Tyler Tompa
2018, November, 10
UNCC Data Analytics Boot Camp Homework 11- Web Visualization Dashboard
"""
####################################################################################################


from flask import Flask, render_template

app = Flask(__name__)

# This defines what happens when the user hits the homepage.
@app.route("/")
def render_Static(index):
    return render_template("index.html" % index)

if __name__ == "__main__":
    app.run(debug=True)