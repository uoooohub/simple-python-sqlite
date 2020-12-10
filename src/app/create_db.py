import sys
import sqlite3

def main(db_name):
    # 接続。なければDBを作成する。
    conn = sqlite3.connect('/code/data/example.db')
    
    # カーソルを取得
    c = conn.cursor()
    
    # テーブルを作成
    c.execute('CREATE TABLE '+db_name+' (id integer primary key autoincrement, title varchar(1024), body text, created datetime)')    
    # コミット
    conn.commit()
    
    # コネクションをクローズ
    conn.close()

if __name__ == "__main__":
    args = sys.argv
    db_name = args[1]
    main(db_name)