from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta

count = 0
countten = 10

print("先にターゲットが同じなグループを一個作ってください。")
button_umu = input("DMを作成ボタンがありますか？(y/n)")
kaisuu = int(input("グループスパムの回数: "))
id1 = input("ターゲット1人目のdiscordID: ")
id2 = input("ターゲット2人目のdiscordID: ")
kaisuuwaru = kaisuu // 10
minutes = kaisuuwaru * 5 
now = datetime.now()
future = now + timedelta(minutes=minutes)

print(f"終了予想時刻:", future.strftime("%H:%M:%S"))
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="discord_login.json")
    page = context.new_page()
    page.goto("https://discord.com/channels/@me") #最初に開く画面
    page.wait_for_timeout(5000)
    #グループ作る＋をクリック
    while kaisuu != count:
     if button_umu == "n":
       page.locator("div[role='button'][aria-label='DMの作成']").click()
       #入力されたユーザーIDのチェックボックスをクリック
       user = page.locator(f"div.friendWrapper_bbd192:has(span:has-text('{id1}'))")
       checkbox = user.locator("span[data-toggleable-component='checkbox']")
       checkbox.click()
       user = page.locator(f"div.friendWrapper_bbd192:has(span:has-text('{id2}'))")
       checkbox = user.locator("span[data-toggleable-component='checkbox']")
       checkbox.click()
       page.click(f"xpath=//span[normalize-space(text())='グループDMの作成']")
     if button_umu == "y":
       page.locator(f"xpath=//span[normalize-space(text())='DMの作成']").first.click()
       #入力されたユーザーIDのチェックボックスをクリック
       user = page.locator(f"div.friendWrapper_bbd192:has(span:has-text('{id1}'))")
       checkbox = user.locator("span[data-toggleable-component='checkbox']")
       checkbox.click()
       user = page.locator(f"div.friendWrapper_bbd192:has(span:has-text('{id2}'))")
       checkbox = user.locator("span[data-toggleable-component='checkbox']")
       checkbox.click()
       page.locator(f"xpath=//span[normalize-space(text())='グループDMの作成']").click()
     page.click("xpath=//div[normalize-space(text())='グループの作成']")
     page.wait_for_timeout(2000)
     if count > 0 and count % 10 == 0:
        page.wait_for_timeout(600000)
     count += 1

    print(f"グループスパムを {kaisuu} 回終えました。終了します。")
    browser.close()

