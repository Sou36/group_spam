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
kaisuu = int(input("グループを作る回数（10がおすすめ）: "))
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
       page.click("xpath=//span[normalize-space(text())='DMの作成']")
     if button_umu == "y":
       page.locator("xpath=//span[normalize-space(text())='DMの作成']").first.click()
       page.locator("xpath=//span[normalize-space(text())='DMの作成']").nth(1).click()
     page.wait_for_timeout(2000)
     if kaisuu != countten:
      time = datetime.now().strftime("%H:%M:%S")
      print(f"待機開始{time}")
      page.wait_for_timeout(300000)
      time = datetime.now().strftime("%H:%M:%S")
      print(f"待機終了{time}")
      countten += 10
     count += 1
     
    print(f"グループを{kaisuu}個作り終えました。終了します。")
    browser.close()
