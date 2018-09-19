# Webフレームワーク
from bottle import get, post, request, run, template, response
# nnabla、ディープラーニング用
import nnabla as nn
from nnabla.utils import nnp_graph
import numpy as np

# 画像処理用
from PIL import Image
from io import BytesIO
from binascii import a2b_base64

## nnabla を初期化
nn.clear_parameters()

# index.html を表示する処理
@get('/')
def index():
    return template(open('./index.html', 'r', encoding='UTF-8').read())

# 画像の判定処理
@post('/img')
def image():
    img_str = request.params['img']
    if img_str == False:
        return "{}"
    
    # 画像を28x28、グレースケールに変換
    b64_str = img_str.split(',')[1]
    img = Image.open(BytesIO(a2b_base64(b64_str)))
    img = img.resize((28, 28))
    img = img.convert('L')
    
    # Neural Network Consoleのファイルを読み込む
    
    # 実行するネットワークを指定する
    
    # 入力変数を取得
    
    # 出力変数を取得
    
    # 画像を配列に変換、数値を0〜1.0にする
    
    # 判定する
    
    # 結果を出力する

run(host='localhost', port=8080)
