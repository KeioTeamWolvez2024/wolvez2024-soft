import tkinter as tk
import random as rm
import time

interval = 100
A = 0.0
player1=0
player2=0
after = None


def time_hint():
    global gamen
    global after
    gamen.after_cancel(after)
    keika.destroy()

def time_start():
    global gamen
    global keika
    global starttime
    global hint
    global button_setumei

    question.destroy()
    start.destroy()
    keika = tk.Label(gamen, font = ('MS ゴシック',30, 'bold'),text = 'ヒント：')
    keika.place(x = 180, y = 50)
    button_setumei = tk.Label(gamen, font = ('MS ゴシック',15),text = '1Pは「S」、2Pは「K」を押してね！')
    button_setumei.place(x = 20, y = 100)
    starttime = time.time()
    after = gamen.after(interval, time_keika)
    hint = gamen.after(3500,time_hint)

    

def time_keika():
    global gamen, keika
    global A
    global after

    after = gamen.after(interval,time_keika)
    A = A + 0.1
    A_hyouzi = format(A,'.1f')
    keika['text'] = 'ヒント：'f'{A_hyouzi}秒'

def time_result(A):
    global player1
    global player2

    key = A.keysym
    if key =='s':
        player1 = time.time() - starttime
    if key =='k':
        player2 = time.time() - starttime
    
    if player1 > 0:
        if player2 > 0:
            button_setumei.destroy()
            result(player1,player2)


def result(a,b):
    result_a = format(a,'.1f')
    result_b = format(b,'.1f')
    kekka = tk.Label(gamen, font = ('MS ゴシック',20),text = 'player1の時間:'f'{result_a}秒\nplayer2の時間:'f'{result_b}秒')
    kekka.place(x = 180, y = 50)
    R = abs(a - x) - abs(b - x)
    if R > 0:
        kekka = tk.Label(gamen, font = ('MS ゴシック',30, 'bold'),text = 'player2の勝利!!')
        kekka.place(x = 180, y = 130)
    else:
        kekka = tk.Label(gamen, font = ('MS ゴシック',30, 'bold'),text = 'player1の勝利!!')
        kekka.place(x = 180, y = 130)

#問題の秒をランダムに決める
x = rm.randint(8,15)

#ウィンドウの作成
gamen = tk.Tk()

#ウィンドウの画面のサイズ
gamen.geometry('400x200')
#タイトル
gamen.title('ぴったりストップ')

#問題文を作成
question = tk.Label(gamen, font = ('MS ゴシック',30),text = 'めざせ!ぴったり'f'{x}秒!!')
question.place(x = 50, y = 50)

#スタートボタンの作成
start = tk.Button(gamen, text = 'START', command = time_start)
start.place(x = 160, y = 100)

#ストップの処理
gamen.bind('<KeyPress>',time_result)

#結果の表示


gamen.mainloop()
