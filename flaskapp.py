from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == "__main__":
    # comment to check ai-pr
    app.run(debug=True)
