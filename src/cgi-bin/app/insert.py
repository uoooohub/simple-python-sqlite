import sys
import sqlite3
import datetime

def main(db_name,title,body):
    # 接続。なければDBを作成する。
    conn = sqlite3.connect('/code/data/example.db')
    
    # カーソルを取得
    c = conn.cursor()

    # Insert実行
    c.execute("INSERT INTO "+str(db_name)+" (title,body,dtime) VALUES (\'"+str(title)+"\',\'"+str(body)+"\',\'"+str(datetime.datetime.now())+"\')")
    
    # コミット
    conn.commit()
    
    # コネクションをクローズ
    conn.close()

if __name__ == "__main__":
    args = sys.argv
    db_name = args[1]
    title = args[2]
    body = args[3]
    main(db_name,title,body)