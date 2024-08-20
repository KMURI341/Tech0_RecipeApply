import streamlit as st
import requests

# 入力フォーム
st.title("楽天レシピ提案アプリ")
cuisine_type = st.selectbox(
    "料理のジャンルを選択してください",
    ["日本料理", "中華料理", "フレンチ料理", "イタリア料理", "韓国料理", "その他"]
)

season = st.selectbox(
    "季節を選択してください",
    ["春", "夏", "秋", "冬"]
)

dish_type = st.selectbox(
    "料理の種類を選択してください",
    ["前菜", "主菜", "副菜", "サラダ", "汁物", "デザート", "その他"]
)

# APIリクエストを送信する関数
def get_recipes(cuisine_type, dish_type):
    # カテゴリに応じたAPIのカテゴリIDなどを設定（仮のIDを使用）
    category_id = {
        "日本料理": "48",
        "中華料理": "41",
        "フレンチ料理": "44",
        "イタリア料理": "43",
        "韓国料理": "42",
        "その他": "46"
    }[cuisine_type]

    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'
    APP_ID = "1022055563333314426"
    params = {
        'format': 'json',
        'applicationId': APP_ID,
        'categoryId': category_id
    }
    response = requests.get(url, params=params)
    return response.json()

if st.button("レシピを提案する"):
    data = get_recipes(cuisine_type, dish_type)
    
    # レシピのフィルタリング（仮の条件でフィルタリング）
    if data:
        recipes = data['result'][:3]  # 最初の3つのレシピを取得
        
        # データの表示
        for recipe in recipes:
            st.subheader(recipe['recipeTitle'])
            st.image(recipe['foodImageUrl'])
            st.write(f"作る時間: {recipe['recipeIndication']}")
    else:
        st.write("データが見つかりませんでした。")