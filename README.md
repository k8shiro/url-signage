# url-signage
ブラウザを起動して指定したURLを巡回していくツール
※　一応ラズパイ用

# 準備

- もろもろinstall

```
$ sudo apt-get install chromium-chromedriver
$ sudo apt-get install chromium-browser
$ pip install -r requirements.txt 

```

- ディスプレイ番号を調べる。

ssh越しではなく物理マシン上で以下のコマンドを実行してディスプレイ番号をメモ

```
$ echo $DISPLAY
:0.0

```



- `urls.txt`の例

URLのリストファイルを作る。
巡回したいURLを1行づつ書いたファイルを`urls.txt`という名前で作る

``` 
https://atmarkit.itmedia.co.jp/ait/subtop/news/
https://gigazine.net/
https://postd.cc/
https://dev.classmethod.jp/
https://engineering.mercari.com/blog/
https://connpass.com/explore/
```

# 使い方

実行

```
# help表示
$ python src/main.py --help
usage: main.py [-h] [-d DISPLAY] [-i INTERVAL] [-u URLS_FILE] [-s SCROLL_SPEED]

optional arguments:
  -h, --help            show this help message and exit
  -d DISPLAY, --display DISPLAY
                        Display number
  -i INTERVAL, --interval INTERVAL
                        Interval of page transfer (seconds)
  -u URLS_FILE, --urls_file URLS_FILE
                        URL list file path
  -s SCROLL_SPEED, --scroll_speed SCROLL_SPEED
                        Page scroll speed (min 1)
  -z ZOOM_RATE, --zoom_rate ZOOM_RATE
                        Browser zoom rate

# 実行
$ nohup python src/main.py　--display=":0.0" -u=urls -s=10 -i=10 &

```
