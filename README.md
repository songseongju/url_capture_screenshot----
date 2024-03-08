크롤링 캡쳐 스크린샷 파이썬
Flask / Selenium / webdriver_manager / Pillow 라이브러리 이용

PHP 대체 flask 사용 linux 서버(우분투)에 연동 할 예정.

실행 화면보기 

<img width="793" alt="Screenshot 2024-03-08 at 10 35 01 AM" src="https://github.com/songseongju/url_capture_screenshot----/assets/122763566/f827367a-07cb-4a92-a74a-21446d1c55ad">

현재 window / mac 환경에서는 cromdriver 자동 install 되는데 
linux (우분투) 에서는 자동 install 이 안되고 PATH(크롬드라이버 설치 후 파일 주소 지정해야함)
크롬을 크롬드라이버 버전별로 맞춰서 (현재 크롬최신버전은 크롬드라이버버전이 맞는 버전이 없음)

1. 크롬 및 크롬드라이버 버전별 설치 

2. 크롬 업데이트 중지 코드 (linux)
    cd /etc/apt/sources.list.d
    sudo vi google-chrome.list
- 해당 파일 내에 저장소 연결이 있는데 이 부분 주석처리

- 문제 생겼을 경우

3. 의존성 문제 해결 및 크롬 stable 버전 재설치 
 Apt —fix-broken install
