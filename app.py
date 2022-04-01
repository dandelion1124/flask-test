from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # /로 요청이 들어오면 아래 문구를 리턴하도록 함
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    return 'main!!'



if __name__ == '__main__':
    app.run(debug=True, port=80)