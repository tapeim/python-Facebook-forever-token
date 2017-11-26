# 페이스북 페이지 APP 추가후
client_id = ""
client_secret = ""
# 단기 Token
client_token = ""

# --- Step 1 ---
# 아래 결과를 실행 후 access token을 가져온다.
result = requests.get(
    "https://graph.facebook.com/v2.7/oauth/access_token?grant_type=fb_exchange_token&client_id=" + client_id + "&client_secret=" + client_secret + "&fb_exchange_token=" + client_token)
print(result.json())

# --- Step 2 ---
# 아래 결과를 실행후 app id를 가져온다.
# 페이스북 페이지에서도 확인이 가능하다
access_token = ""
result = requests.get(
    "https://graph.facebook.com/v2.7/me?access_token=" + access_token)
print(result.json())

# --- Step 3 ---
# 아래 결과를 실행후 나온 access token은 기한이 없는 토큰이다.
app_id = ""
result = requests.get(
    "https://graph.facebook.com/v2.7/" + app_id + "?fields=access_token&access_token=" + access_token)
print(result.json())