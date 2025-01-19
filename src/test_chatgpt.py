from playwright.sync_api import sync_playwright

def test_chatgpt_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Headless 모드
        page = browser.new_page()
        page.goto("https://chat.openai.com")  # ChatGPT 메인 화면 URL

        # 스크린샷 저장
        page.screenshot(path="screenshot.png")
        
        # 간단한 테스트: 제목 확인
        assert "ChatGPT" in page.title(), "Page title does not contain 'ChatGPT'"
        print("✅ ChatGPT 페이지 접속 완료")

        browser.close()

if __name__ == "__main__":
    test_chatgpt_homepage()
