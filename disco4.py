from playwright.sync_api import sync_playwright
from datetime import datetime
count = 0
count2 = 1
button_umu = input("DMを作成ボタンがありますか？(y/n): ")
if button_umu == "y":
  nth_dis = 4
if button_umu == "n":
  nth_dis = 3
sikake_ninzuu = int(input("何人に仕掛けますか？(1 or 2)"))
print("先にグループが連続してあることを確認してください。")
kaisuu = int(input("グループスパムの回数: "))
id1 = input("ターゲット1人目のdiscordID: ")
if sikake_ninzuu == 2:
 id2 = input("ターゲット2人目のdiscordID: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="discord_login.json")
    page = context.new_page()
    page.goto("https://discord.com/channels/@me") #最初に開く画面
    page.wait_for_timeout(5000)
    while kaisuu != count:
     page.locator("li").nth(nth_dis).click()
     page.wait_for_selector("div[role='button'][aria-label='DMにフレンドを追加']",timeout=10000)
     page.locator("div[role='button'][aria-label='DMにフレンドを追加']").click()
     #入力されたユーザーIDのチェックボックスをクリック
     user = page.locator(f"div.friendWrapper_bbd192:has(span:has-text('{id1}'))")
     checkbox = user.locator("span[data-toggleable-component='checkbox']")
     checkbox.click()
     if sikake_ninzuu == 2:
      user = page.locator(f"div.friendWrapper_bbd192:has(span:has-text('{id2}'))")
      checkbox = user.locator("span[data-toggleable-component='checkbox']")
      checkbox.click()
     #追加ボタンをクリック
     page.click("xpath=//span[normalize-space(text())='追加']")
     page.wait_for_timeout(1000)
     if button_umu == "y":
      if nth_dis != 4:
        page.click("xpath=//div[normalize-space(text())='グループの作成']")
     if button_umu == "n":
      if nth_dis != 3:
        page.click("xpath=//div[normalize-space(text())='グループの作成']")
     nth_dis += 1
     if count > 0 and count % 10 == 0:#10回おきに待った回数×1分+6分待機 
       time = datetime.now().strftime("%H:%M:%S")
       print(f"待機開始{time}。現在の待機時間は{count2 + 6}分です。")
       page.wait_for_timeout(count2 * 60000 + 360000)
       time = datetime.now().strftime("%H:%M:%S")
       print(f"待機終了{time}。")
       count2 += 1
     count += 1
    print(f"{kaisuu}回グループにターゲットを入れて抜けました。終了します。")
    browser.close()




