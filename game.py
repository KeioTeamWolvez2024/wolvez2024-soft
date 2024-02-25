#62003863 太田晃
#プログラミング演習最終回課題 オリジナルゲーム製作「対戦！ぴったりストップ！」

#ライブラリをインポート
import tkinter as tk
import random as rm
import time

#ヒントのタイマーの変数
A = 0.0

#プレイする人のタイムカウンター
player1=0
player2=0


#スタートボタンを押してからの処理
def time_start():
    '''
    これはスタートボタンが押されてから目標とボタンを削除して、afterで別の関数を実行させるための関数である。
    開発者:太田晃
    '''
    global gamen
    global keika
    global starttime
    global hint

    question.destroy()              #問題のラベルを削除
    start.destroy()                 #スタートボタンを削除
    keika = tk.Label(gamen, font = ('MS ゴシック',30, 'bold'),text = 'ヒント：')    #ヒントの経過時間を表示するラベルを用意
    keika.place(x = 100, y = 50)                                                 #ラベルの位置を指定
    starttime = time.time()         #開始時間を記録
    after_t = gamen.after(100, time_keika)  #100ms後に関数time_keikaを実行する
    hint = gamen.after(3500, time_hint)     #3500ms後に関数time_hintを実行する

#ヒントとして0.1秒ずつタイマーを表示する関数
def time_keika():
    '''
    これは関数time_startによって実行されるヒントのタイマー表示をするための関数である
    開発者:太田晃
    '''
    global A
    global after

    after = gamen.after(100,time_keika)         #100ms後にもう一度この関数を実行
    A = A + 0.1                                 #Aに0.1足す
    A_hyouzi = format(A,'.1f')                  #小数第一位まで表示に設定
    keika['text'] = 'ヒント：'f'{A_hyouzi}秒'     #経過時間のラベルを書き換える

#ヒントを消す関数
def time_hint():
    '''
    これはヒントとしてタイマー表示される時のafterを停止してそのラベルを削除する関数である。
    開発者:太田晃
    '''
    gamen.after_cancel(after)       #+0.1する作業をストップ
    keika.destroy()                 #経過時間を表すラベルを削除

#それぞれの時間を計測する関数
def time_result(event):
    '''
    これはキーボード入力を引数としてsとkが入力された時の時間からプレイヤーの時間記録を行う関数である。
    開発者:太田晃
    '''
    global player1
    global player2

    key = event.keysym      #入力されたキーを取得する
    if key =='s':       #sが入力されたら開始時間からplayer1の結果を記録
        player1 = time.time() - starttime
    if key =='k':       #kが入力されたら開始時間からplayer2の結果を記録
        player2 = time.time() - starttime
    
    #2人の記録がついたら操作説明のラベルを削除、関数resultを実行
    if player1 > 0:
        if player2 > 0:
            button_setumei.destroy()
            result(player1,player2)

#結果の表示をする関数
def result(a,b):
    '''
    これは、二人分の結果からどちらが目標値に近いかを比べて勝利したプレイヤーを表示するための関数である。
    開発者:太田晃
    '''
    #引数を小数第二位までにする
    result_a = format(a,'.2f')
    result_b = format(b,'.2f')
    #それぞれの結果を表示する
    kekka = tk.Label(gamen, font = ('MS ゴシック',20),text = 'player1の時間:'f'{result_a}秒\nplayer2の時間:'f'{result_b}秒')
    kekka.place(x = 90, y = 40)     #結果の位置を指定
    R = abs(a - x) - abs(b - x)     #目標値の差の絶対値を比較
    if R > 0:   #比較した結果によってそれぞれのプレイヤー用の勝利のラベルを設置
        kekka = tk.Label(gamen, font = ('MS ゴシック',35, 'bold'),text = 'player2の勝利!!')
        kekka.place(x = 80, y = 100)
    else:
        kekka = tk.Label(gamen, font = ('MS ゴシック',35, 'bold'),text = 'player1の勝利!!')
        kekka.place(x = 80, y = 100)

#問題の秒をランダムに決める
x = rm.randint(8,15)

#ウィンドウの作成
gamen = tk.Tk()
gamen.geometry('400x200')       #ウィンドウの画面のサイズ
gamen.title('ぴったりストップ')    #タイトル

#問題文を作成
question = tk.Label(gamen, font = ('MS ゴシック',30),text = 'めざせ!ぴったり'f'{x}秒!!')
question.place(x = 60, y = 40)     #問題文の位置を指定

#スタートボタンの作成
start = tk.Button(gamen, text = 'START', command = time_start)
start.place(x = 160, y = 90)       #スタートボタンの位置を設定

#操作方法の説明
button_setumei = tk.Label(gamen, font = ('MS ゴシック',15),text = f'{x}秒経ったと思ったら\n1Pは「S」、2Pは「K」\nを押してね！')
button_setumei.place(x = 125, y = 120)   #操作説明の位置を指定

#キーボードの入力処理
gamen.bind('<Key>',time_result) #キーボードが押されると関数time_resultを実行

#ウィンドウを表示
gamen.mainloop()