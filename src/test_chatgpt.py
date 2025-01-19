from playwright.sync_api import sync_playwright
import pandas as pd

def test_chatgpt_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.naver.com")
        page.wait_for_load_state("load")
        # 스크린샷 저장
        page.screenshot(path="screenshot.png")
        # 간단한 테스트: 제목 확인
        assert "naver" in page.title(), "Page title does not contain 'ChatGPT'"
        print("✅ naver 페이지 접속 완료")

        assert 1 == 2, "테스트 실패"

        assert 1 == 1, "테스트 성공"

        browser.close()
        
        result = [
            {"name": "Alice", "age": 24},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 26},
        ]
        #판다스로 리스트를 엑셀로 저장해줘
        df = pd.DataFrame(result)
        df.to_excel("result.xlsx", index=False)
        print("✅ 엑셀 저장 완료")
        #result를 html파일로 저장하기
        df.to_html("result.html", index=False)

if __name__ == "__main__":
    test_chatgpt_homepage()
