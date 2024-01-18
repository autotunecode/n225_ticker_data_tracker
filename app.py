import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import datetime
from pandas_datareader import data
import yfinance as yf
import numpy as np
        
          

def fetch_ticker_data():
    """
    指定されたティッカーシンボルのデータを取得し、ボリュームでソートしてトップ10を返します。
    """
    # ティッカーシンボルのリスト
    tickers = ['7203.T', '9984.T', '6758.T', '9433.T', '8306.T', '6501.T', '6752.T', '6861.T', '6954.T', '6367.T']
    # 各ティッカーのデータを取得し、一つのデータフレームに結合
    df = pd.concat([yf.download(ticker, start=datetime.date.today()).assign(Ticker=ticker) for ticker in tickers])
    # ボリュームでソートし、トップ10を選択
    df = df.sort_values('Volume', ascending=False).head(10)
    # 'Ticker'を最初の列に移動
    df = df.set_index('Ticker').reset_index()
    return df

def record_to_google_sheet(df, sheet_name):
    """
    データフレームをGoogleスプレッドシートに記録します。
    認証には'client_secret.json'が必要です。
    """
    # Google APIのスコープを設定
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    # 認証情報を取得
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    # Googleスプレッドシートに接続
    client = gspread.authorize(creds)
    # スプレッドシートを開く
    sheet = client.open(sheet_name).sheet1
    # スプレッドシートに項目を追加
    sheet.append_row(df.columns.tolist())
    # データフレームの各行をスプレッドシートに追加
    for i in range(len(df)):
        row = df.iloc[i].tolist()
        row = [row[0]] + [int(x) if isinstance(x, np.int64) else x for x in row[1:]]
        sheet.append_row(row)
        

def main():
    """
    fetch_ticker_data関数を呼び出してデータを取得し、
    それをGoogleスプレッドシートに記録します。
    """
    # データを取得
    df = fetch_ticker_data()
    # データをGoogleスプレッドシートに記録
    record_to_google_sheet(df, 'Nikkei225_' + str(datetime.date.today()))

if __name__ == "__main__":
    # メイン関数を実行
    main()
