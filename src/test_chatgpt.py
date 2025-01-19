from playwright.sync_api import sync_playwright
import pandas as pd
import time

def test_chatgpt_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.naver.com")
        page.wait_for_load_state("load")
        time.sleep(10)
        # 스크린샷 저장
        page.screenshot(path="screenshot.png")
        # 간단한 테스트: 제목 확인
        try:
            assert "naver" in page.title(), "Page title does not contain 'ChatGPT'"
            print("✅ naver 페이지 접속 완료")
        except Exception as e:
            print("❌ naver 페이지 접속 실패")
            raise e
        
        try:
            assert 1 == 2, "테스트 실패"
        except Exception as e:
            print("❌ 테스트 실패")
            raise e

        try:
            assert 1 == 1, "테스트 성공"
            print("✅ 테스트 성공")
        except Exception as e:
            print("❌ 테스트 실패")
            raise e

        browser.close()
        
        #result를 리스트 내용(20개로) 더 많은 내용으로 추가하기
        result = []
        for i in range(20):
            result.append({
                "name": "name" + str(i),
                "age": i,
                "location": "location" + str(i)
            })

        #판다스로 리스트를 엑셀로 저장해줘
        df = pd.DataFrame(result)
        df.to_excel("result.xlsx", index=False)
        print("✅ 엑셀 저장 완료")
        #result를 html파일로 저장하기
        df.to_html("result.html", index=False)

if __name__ == "__main__":
    test_chatgpt_homepage()
