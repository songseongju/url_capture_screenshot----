from flask import Flask, render_template, request, send_file, url_for
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import os
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

# 크롬 드라이버 경로 설정
CHROMEDRIVER_PATH = "/path/to/chromedriver"

# 스크린샷 저장 경로 설정
SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")


@app.route('/')
def index():
    return render_template('index.html', image_data=None)


@app.route('/screenshot', methods=['POST'])
def screenshot():
    url = request.form['url']
    
    # 스크린샷 저장 디렉토리 생성
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)
    
    # 크롬 드라이버 초기화
    options = webdriver.ChromeOptions()
    options = ChromeOptions()
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    options.add_argument('user-agent=' + user_agent)
    options.add_argument("lang=ko_KR")
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저를 숨기고 실행
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    
    # 웹페이지 열기 및 스크린샷 캡처
    driver.get(url)
    time.sleep(5)  # 페이지가 완전히 로드될 때까지 기다림 (필요에 따라 조절)
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    # 브라우저 창을 페이지 하단으로 스크롤 하기.
    driver.execute_script("window.scrollTo(0, document.body.parentNode.scrollHeight);")
    driver.set_window_size("1920", total_height)    
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{int(time.time())}.png")
    driver.save_screenshot(screenshot_path)
    
    # 이미지를 PIL로 열어서 base64로 변환하여 HTML에 전달
    image = Image.open(screenshot_path)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    # 드라이버 종료
    driver.quit()
    
    # 이미지 데이터를 HTML에 전달하여 표시
    return render_template('index.html', image_data=image_data)


if __name__ == '__main__':
    app.run(debug=True)

