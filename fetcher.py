import requests
from bs4 import BeautifulSoup
import time

def get_amazon_title(asin):
    url = f"https://www.amazon.co.jp/dp/{asin}"
    
    # ブラウザからのアクセスに見せかけるためのヘッダー
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ja-JP,ja;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Amazonに弾かれたら(503等)終了
        if response.status_code != 200:
            print(f"⚠️ 取得失敗 (Status: {response.status_code})")
            return f"Amazon商品 ({asin})"

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Amazonの商品タイトルは id="productTitle" に入っている
        title_tag = soup.find("span", id="productTitle")
        
        if title_tag:
            title = title_tag.get_text().strip()
            return title
        else:
            return f"Amazon商品 ({asin})"

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        return f"Amazon商品 ({asin})"

# --- 単体テスト ---
if __name__ == "__main__":
    test_asin = "B08N5N6RSS" # MacBook AirのASIN
    print(f"🔍 {test_asin} のタイトルを取得中...")
    print(f"結果: {get_amazon_title(test_asin)}")