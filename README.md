# App.py 仕様書

このプログラムは、特定のティッカーシンボルのデータを取得し、それを Google スプレッドシートに記録するためのものです。

## 使用方法

1. プログラムを実行すると、以下のティッカーシンボルのデータが取得されます: '7203.T', '9984.T', '6758.T', '9433.T', '8306.T', '6501.T', '6752.T', '6861.T', '6954.T', '6367.T'
2. 取得したデータはボリュームでソートされ、トップ 10 が選択されます。
3. 選択されたデータは Google スプレッドシートに記録されます。

## Google 認証について

このプログラムは Google スプレッドシートにデータを記録するため、Google API の認証が必要です。認証には'client_secret.json'が必要です。

'client_secret.json'は Google Cloud Platform のプロジェクトページからダウンロードできます。ダウンロードしたファイルをプログラムと同じディレクトリに配置してください。

また、Google API のスコープは以下の通り設定されています: ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

## 注意事項

このプログラムは、Google スプレッドシートの名前を'Nikkei225\_' + 今日の日付（例：'Nikkei225_2024-01-01'）として自動的に設定します。スプレッドシートの名前を変更する場合は、プログラムのソースコードを直接編集してください。

## 'client_secret.json'について

このプログラムで必要な'client_secret.json'の値は以下の通りです：

- type
- project_id
- private_key_id
- private_key
- client_email
- client_id
- auth_uri
- token_uri
- auth_provider_x509_cert_url
- client_x509_cert_url

これらの値は、Google Cloud Platform のプロジェクトページからダウンロードした'client_secret.json'に含まれています。
