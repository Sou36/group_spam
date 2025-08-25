from playwright.sync_api import sync_playwright

count = 0
nth_dis = 0
kaisuu_kenti = 1

name = input("グループ名を入力: ")
kaisuu = input("グループを抜ける回数(全部抜ける場合fと入力): ")
if kaisuu != "f":
  kaisuu = int(kaisuu)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="discord_login.json")
    page = context.new_page()
    page.goto("https://discord.com/channels/@me") #最初に開く画面
    page.wait_for_timeout(5000)

    #入力された名前のliを探す
    ligroup = page.locator(f"//div[contains(@class, 'overflowTooltip__972a0') and normalize-space(.)='{name}']")
    ligroup_count = ligroup.count()
    print("divの数",ligroup_count)
    if kaisuu != "f":
     kaisuu_kenti = kaisuu - 1
    else:
     kaisuu_kenti = ligroup_count

    for i in range(kaisuu_kenti):
     #上のを右クリックしてグループ脱退
     target = ligroup.nth(nth_dis)
     target.click(button="right")
     page.click("xpath=//div[normalize-space(text())='グループから脱退する']")
     #抜ける確認ボタン
     page.wait_for_selector("xpath=//button/div[normalize-space(text())='グループから脱退する']",timeout=10000)
     page.click("xpath=//button/div[normalize-space(text())='グループから脱退する']")
     count += 1
    if kaisuu != "f":
     print(f"グループを{kaisuu}個抜け終えました。終了します。")
    else:
      print(f"{name}を全て抜け終えました。終了します。")
    browser.close()
