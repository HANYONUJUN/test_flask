from flask import Flask, render_template

# flask 애플리케이션 인스턴스 생성
app = Flask(__name__)

# @app.route('/') 데코레이터를 사용하여 '/' 경로에 대한 라우트를 설정. 이 경로에 접근하면 index 함수가 호출
# index 함수 내에서 items라는 리스트를 정의하고, render_template 함수를 통해 index.html 템플릿에 items 데이터를 전달
@app.route('/')
def index():
    items =["han","yong","jun"]
    return render_template('index.html', items=items)

# if __name__ == '__main__': 블록 내에서 app.run()을 호출하여 Flask 애플리케이션을 실행
# localhost의 5000번 포트에서 실행
if __name__ == '__main__':
    app.run()