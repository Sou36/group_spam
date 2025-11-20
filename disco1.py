from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://discord.com/login")

    print("開いたブラウザで手動でログイン、ログイン後にここで Enter を押す。")
    print("中断したい場合は e と入力")
    hoge = input()
    if hoge == "e":
     pass
    else:
     login_path = input("ログイン情報を保存するファイル名を入力してください(拡張子は省略): ")
     # ログイン後の状態を保存
     context.storage_state(path=f"{login_path}.json")
     print(f"ログイン状態を {login_path}.json に保存しました。")

    browser.close()
