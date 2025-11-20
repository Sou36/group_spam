import glob
from playwright.sync_api import sync_playwright
from datetime import datetime
count = 0
count2 = 1

json_files = glob.glob("*.json")
for i, f in enumerate(json_files, start=1):
    print(f"{i}. {f}")
choice = int(input("どのログイン情報にしますか？(番号で指定): ")) - 1
login_num = json_files[choice]
button_num = input("DMを作成ボタンがありますか？(y/n): ")
if button_num == "y":
  nth_dis = 6
if button_num == "n":
  nth_dis = 5
esc_num = input("グループを作った後抜けますか？(y/n): ")
kaisuu = int(input("グループスパムの回数: "))
sikake_ninzuu = int(input("何人に仕掛けますか？(1 or 2): "))
id1 = input("ターゲット1人目のdiscordID: ")
if sikake_ninzuu == 2:
 id2 = input("ターゲット2人目のdiscordID: ")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state=f"{login_num}")
    page = context.new_page()
    page.goto("https://discord.com/channels/@me") #最初に開く画面
    page.wait_for_timeout(5000)
    while kaisuu != count:
     page.locator("li").nth(nth_dis).click()
     page.wait_for_selector("div[role='button'][aria-label='DMにフレンドを追加']",timeout=10000)
     page.locator("div[role='button'][aria-label='DMにフレンドを追加']").click()
     page.wait_for_timeout(1000)
     #入力されたユーザーIDのチェックボックスをクリック
     span = page.locator("span", has_text=id1)
     block = span.locator("..").locator("..").locator("..").locator("..")
     checkbox = block.locator("[class*='checkbox']")
     checkbox.first.click(force=True)

     if sikake_ninzuu == 2:
       span = page.locator("span", has_text=id2)
       block = span.locator("..").locator("..").locator("..").locator("..")
       checkbox = block.locator("[class*='checkbox']")
       checkbox.first.click(force=True)
     page.click("xpath=//span[normalize-space(text())='追加']")
     page.wait_for_timeout(1000)
     #グループ被りの確認画面が出てきたらクリック
     locator = page.locator("xpath=//span[normalize-space(text())='グループの作成']")
     if locator.is_visible():
      locator.click()
     page.wait_for_timeout(1000)
     if esc_num == "y":
      #グループ脱退のバツマーク
      target = page.locator("li").nth(nth_dis)
      target.click(button="right")
      page.click("xpath=//div[normalize-space(text())='グループから脱退する']")
      page.wait_for_timeout(1000)
      #抜ける確認ボタン
      page.click("xpath=//button/div[normalize-space(text())='グループから脱退する']")
     if esc_num == "n":
       nth_dis += 1
     if count > 0 and count % 10 == 0:
       time = datetime.now().strftime("%H:%M:%S")
       print(f"待機開始{time}。現在の待機時間は{count2 + 6}分です。")
       page.wait_for_timeout(count2 * 60000 + 360000)#10回おきに待った回数×1分+6分待機
       time = datetime.now().strftime("%H:%M:%S")
       print(f"待機終了{time}。")
       count2 += 1
     count += 1
    print(f"{kaisuu}回グループにターゲットを入れて抜けました。終了します。")
    browser.close()





