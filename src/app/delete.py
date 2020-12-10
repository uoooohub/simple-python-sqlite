import sys
import sqlite3
import datetime

def main(db_name,id):
    # 接続。なければDBを作成する。
    conn = sqlite3.connect('/code/data/example.db')
    
    # カーソルを取得
    c = conn.cursor()

    # Insert実行
    c.execute("DELETE FROM "+str(db_name)+" WHERE id=\'"+str(id)+"\'")
    
    # コミット
    conn.commit()
    
    # コネクションをクローズ
    conn.close()

if __name__ == "__main__":
    args = sys.argv
    db_name = args[1]
    id = args[2]
    main(db_name,id)