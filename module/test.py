import sys

args = sys.argv

if len(args):
    print(args)
    print(type(args))
    print(type(args[2]))
    print(len(args))
    print("-" * 30)
    print("コマンドライン引数の第一引数は " + args[1])
    print(float(args[2]) * 3.14)
else:
    print("コマンドライン引数を２つ入力してください \n 第一引数はstr型、第二引数はfloat型です。")
