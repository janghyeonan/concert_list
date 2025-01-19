from playwright.sync_api import sync_playwright
import pandas as pd
import time
import os

def test_chatgpt_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.naver.com")
        page.wait_for_load_state("load")
        time.sleep(10)

        # result 리스트 생성 (20개의 데이터 추가)
        result = [
            {"name": f"name{i}", "age": i, "location": f"location{i}"}
            for i in range(20)
        ]

        # 판다스를 이용해 리스트를 엑셀로 저장
        df = pd.DataFrame(result)
        df.to_excel("result.xlsx", index=False, engine="xlsxwriter")
        print("✅ 엑셀 저장 완료")

        # HTML 파일로 저장
        df.to_html("result22.html", index=False)

        print("엑셀 파일 존재:", os.path.exists("result.xlsx"))
        print("HTML 파일 존재:", os.path.exists("result22.html"))


        # 스크린샷 저장
        page.screenshot(path="screenshot.png")

        # 간단한 테스트: 제목 확인
        assert "naver" in page.title(), "Page title does not contain 'ChatGPT'"
        print("✅ naver 페이지 접속 완료")

        assert 1 == 2, "테스트 실패"
        assert 1 == 1, "테스트 성공"

        browser.close()

