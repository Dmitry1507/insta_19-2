from flask import Flask, render_template # 플라스크
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/mypage')
def home():
   return render_template('mypage.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
