import glob
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta

count = 0
countten = 10

json_files = glob.glob("*.json")
for i, f in enumerate(json_files, start=1):
    print(f"{i}. {f}")
choice = int(input("どのログイン情報にしますか？(番号で指定): ")) - 1
login_num = json_files[choice]

button_umu = input("DMを作成ボタンがありますか？(y/n): ")
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
    context = browser.new_context(storage_state=f"{login_num}")
    page = context.new_page()
    page.goto("https://discord.com/channels/@me") #最初に開く画面
    page.wait_for_timeout(5000)
    #グループ作る＋をクリック
    while kaisuu != count:
     if button_umu == "n":
       page.locator("div[role='button'][aria-label='DMの作成']").click()
       #入力されたユーザーIDのチェックボックスをクリック
       page.wait_for_timeout(1000)
       span = page.locator("span", has_text=id1)
       block = span.locator("..").locator("..").locator("..").locator("..")
       checkbox = block.locator("[class*='checkbox']")
       checkbox.first.click(force=True)
       #2人目
       page.wait_for_timeout(500)
       span = page.locator("span", has_text=id2)
       block = span.locator("..").locator("..").locator("..").locator("..")
       checkbox = block.locator("[class*='checkbox']")
       checkbox.first.click(force=True)
       page.wait_for_timeout(1000)
     if button_umu == "y":
       page.locator("xpath=//span[normalize-space(text())='DMの作成']").first.click()
       #入力されたユーザーIDのチェックボックスをクリック
       page.wait_for_timeout(1000)
       span = page.locator("span", has_text=id1)
       block = span.locator("..").locator("..").locator("..").locator("..")
       checkbox = block.locator("[class*='checkbox']")
       checkbox.first.click(force=True)
       #2人目
       page.wait_for_timeout(500)
       span = page.locator("span", has_text=id2)
       block = span.locator("..").locator("..").locator("..").locator("..")
       checkbox = block.locator("[class*='checkbox']")
       checkbox.first.click(force=True)
       page.wait_for_timeout(1000)
     page.locator("xpath=//span[normalize-space(text())='グループDMの作成']").click()
     page.wait_for_timeout(2000)
     locator = page.locator("xpath=//span[normalize-space(text())='グループの作成']")
     if locator.is_visible():
      locator.click()
     page.wait_for_timeout(1000)
     if count > 0 and count % 10 == 0:
        page.wait_for_timeout(600000)#10回終わるごとに10分待機
     count += 1

    print(f"グループスパムを {kaisuu} 回終えました。終了します。")
    browser.close()



