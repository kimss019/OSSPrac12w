from flask import Flask, request, render_template, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # 사진 파일을 저장할 폴더



# 최초 메인 페이지를 보여주는 루트 경로
@app.route('/')
def index():
    return render_template('app_index.html')  # 위 HTML 코드를 form.html 파일로 저장해야 합니다

# 학생 정보를 입력하는 경로

@app.route('/input')
def input():
    return render_template('app_input.html')

# 제출된 데이터를 처리하여 출력하는 경로
@app.route('/result', methods=['POST'])
def result():
    # 각 학생의 이름과 학번 데이터를 리스트로 받음
    names = request.form.getlist('name[]')
    role = request.form.getlist('role[]')
    student_numbers = request.form.getlist('StudentNumber[]')
    student_email = request.form.getlist('email[]')
    major = request.form.getlist('major[]')
    git = request.form.getlist('git[]')
    

    default_photo_url = url_for('static', filename='uploads/default_image.jpg')
    photo_urls = []
    for name in names:
        # 이름을 기준으로 사진 파일명 설정
        photo_filename = f"{name}.jpg"
        photo_path = os.path.join(app.static_folder, 'uploads', photo_filename)
        
        # 해당 사진 파일이 존재하는지 확인
        if os.path.exists(photo_path):
            photo_url = url_for('static', filename=f'uploads/{photo_filename}')
        else:
            # 사진 파일이 없으면 기본 이미지 사용
            photo_url = default_photo_url
        
        photo_urls.append(photo_url)

    # 데이터를 템플릿으로 전달하여 출력 페이지 생성
    return render_template('app_result.html', students=zip(names,role, student_numbers,student_email,major,git,photo_urls))

@app.route('/contact')
def contact_info():
    return render_template('app_contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

