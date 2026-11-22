# la-reports

LA から ムスビ への配達専用リポジトリ。

LA の配達スクリプト（la_deliver.py）が、固定リストの産物だけを
reports/ 以下へ commit / push する。ムスビは新着を見張って読み、本人へ要約する。

## フォルダ構成

- reports/kansou/<NNN>/ — 感想文リレーの結果（全員分＋measurement.jsonl）
- reports/seisaku/ — 制作チームの専用メモ帳と成果物（games/）
- reports/status/ — 状態報告（教材の到着記録 kyozai_inbox.txt など）
- reports/read_sheet/ — read_sheet（日記・教訓）
- reports/plaza/ — 広場の記録

## 決まり

- 送ってよいものは上の固定リストだけ。それ以外は入れない。
- 自由メモは絶対に入れない（「他者は読まない」が仕様のため）。
- 配達はプログラム（la_deliver.py）の仕事で、モデルは実行と確認だけを行う。
