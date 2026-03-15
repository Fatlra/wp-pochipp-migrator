import re
import mysql.connector
from fetcher import get_amazon_title

# --- 設定（成約後に相手から情報を聞いて埋める場所） ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_wp_db'
}

# 旧ショートコードの抽出用正規表現
WPAP_PATTERN = r'\[wpap .*?id=[\'"]([A-Z0-9]{10})[\'"].*?\]'

def fetch_posts_with_old_links():
    """DBから古いリンクが含まれる記事を取得する（擬似関数）"""
    # 実際は SELECT post_content FROM wp_posts WHERE post_content LIKE '%[wpap%' とかやる
    return [
        {"id": 1, "content": "テスト記事1 [wpap id='B08N5N6RSS']"},
        {"id": 2, "content": "テスト記事2 [wpap id='B09XXXXXXX']"}
    ]

def convert_content(content):
    """記事本文内のショートコードを置換する"""
    def replace_logic(match):
        asin = match.group(1)

        print(f"   >>> ASIN: {asin} の情報を取得中")
        title = get_amazon_title(asin)
        # TODO: ここでPochippのDBにASINを登録し、新IDを取得するロジックが必要
        new_id = f"ID_{asin}"  # 仮のID生成ロジック
        print(f"   [完了] タイトル: {title[:15]}... -> 新ID: {new_id}") 
        return f'[pochipp id="{new_id}"]'

    return re.sub(WPAP_PATTERN, replace_logic, content)

# --- メイン処理 ---
if __name__ == "__main__":
    print(" 変換テストを開始")
    posts = fetch_posts_with_old_links()
    
    for post in posts:
        new_content = convert_content(post['content'])
        print(f"Post ID {post['id']} の変換結果:\n{new_content}")