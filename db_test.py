import mysql.connector

def register_pochipp_item(cursor, title, asin):
    # 1. wp_posts に基本情報を入れる
    # post_status='publish', post_type='pochipp' にするのがポイント
    sql_post = """
    INSERT INTO wp_posts (post_title, post_status, post_type, post_author, post_date, post_date_gmt)
    VALUES (%s, 'publish', 'pochipp', 1, NOW(), NOW())
    """
    cursor.execute(sql_post, (title,))
    
    # 今さっき発行された「ID」を取得する
    new_id = cursor.lastrowid
    print(f"✅ wp_postsに登録完了 ID: {new_id}")

    # 2. wp_postmeta にASINなどの詳細データを入れる
    # meta_key はPochippの仕様に合わせる（実際は '_pochipp_asin' とか）
    sql_meta = """
    INSERT INTO wp_postmeta (post_id, meta_key, meta_value)
    VALUES (%s, 'pochipp_asin', %s)
    """
    cursor.execute(sql_meta, (new_id, asin))
    print(f"✅ wp_postmetaにASIN: {asin} を紐づけました")
    
    return new_id

# 実際はここでDB接続するけど、今はロジックの確認だけ
print("これがPochipp登録のコア・ロジックです")