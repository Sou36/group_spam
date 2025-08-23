from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://discord.com/login")

    print("開いたブラウザで手動でログイン、ログイン後にここで Enter を押す。")
    input()

    # ログイン後の状態を保存
    context.storage_state(path="./discord_login.json")
    print("ログイン情報を discord_login.json に保存しました。")
    print("次はdisco2.pyを起動してください。")
    browser.close()
