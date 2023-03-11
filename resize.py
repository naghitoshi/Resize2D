"""
 説明：OpenCVによる2次元画像のサイズ変更用のプログラム
"""
import argparse
import cv2
import numpy as np

"""
任意の大きさに拡大・縮小する関数(cv2)
引数1：リサイズしたい画像のパス,
引数2：リサイズ後の高さ
引数3：リサイズ後の幅、
引数4：保存ファイル名
"""
def resize_any_size(image_path, height, width, save_path="save.jpg"):
    if height <= 0 or width <= 0:
        print("Error:resize_any_sizeの引数2または引数3が0以下です. ")
        return
    img = cv2.imread(image_path)
    #バイキュービック補間
    img_resize = cv2.resize(img, (int(width), int(height)), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(save_path, img_resize)
    return

"""
倍率から拡大・縮小する関数(cv2)
引数1：リサイズしたい画像のパス,
引数2：リサイズの倍率
引数3：保存ファイル名
"""
def resize_similar_shape1(image_path, magnification, save_path="save.jpg"):
    if magnification <= 0 or magnification > 100:
        print("Error:resize_similar_shape1の引数2が0以下または100より大きいです. 倍率で指定してください")
        return
    img = cv2.imread(image_path)
    width = int(img.shape[1] * magnification + 0.5)
    height = int(img.shape[0] * magnification + 0.5)
    #バイキュービック補間
    img_resize = cv2.resize(img, (int(width), int(height)), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(save_path, img_resize)
    return

"""
高さを指定して、等倍率で拡大・縮小する関数(cv2)
引数1：リサイズしたい画像のパス,
引数2：リサイズの倍率
引数3：保存ファイル名
"""
def resize_similar_shape2(image_path, height, save_path="save.jpg"):
    if height <= 0:
        print("Error:resize_similar_shape2の引数2が0以下です. ")
        return
    img = cv2.imread(image_path)
    width = int(img.shape[1] * height / img.shape[0] + 0.5)
    #バイキュービック補間
    img_resize = cv2.resize(img, (int(width), int(height)), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(save_path, img_resize)
    return

"""
幅を指定して、等倍率で拡大・縮小する関数(cv2)
引数1：リサイズしたい画像のパス,
引数2：リサイズの倍率
引数3：保存ファイル名
"""
def resize_similar_shape3(image_path, width, save_path="save.jpg"):
    if width <= 0:
        print("Error:resize_similar_shape3の引数2が0以下です. ")
        return
    img = cv2.imread(image_path)
    height = int(img.shape[0] * width / img.shape[1] + 0.5)
    #バイキュービック補間
    img_resize = cv2.resize(img, (int(width), int(height)), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(save_path, img_resize)
    return

def main():
    parser = argparse.ArgumentParser(
            prog = 'resize.py', # プログラム名
            usage = '指定した2次元画像ファイル読み込み、リサイズした画像を保存', # プログラムの利用方法
            description = 'description',   # 引数のヘルプの前に表示
            epilog = 'end', # 引数のヘルプの後で表示
            add_help = True, # -h/–help オプションの追加
            )
    # コマンド引数
    parser.add_argument('input_file_path', type = str, default = "", help = '入力画像のパス')
    parser.add_argument('mode', type = int, default = 0, 
        help = '画像サイズ指定のためのモード, 0=縦横指定, 1=倍率指定, 2=高さ指定の縦横等倍, 3=幅指定の縦横等倍')
    parser.add_argument('-a1','--argument1', type = float, default = None, 
        help = '画像のサイズを指定するための引数1(必須)')
    parser.add_argument('-a2','--argument2', type = int, default = None, 
        help = '画像のサイズを指定するための引数2(mode=0の時のみ必要)')
    parser.add_argument('-o','-s','-save','--output_file_path', type = str, default ="save.jpg", 
        help = '出力画像のパス')

    arguments = parser.parse_args()
    execute(arguments)

# 実行用関数
def execute(arguments):
    if arguments.mode < 0 or arguments.mode > 3:
        print("Error:コマンドライン引数のmodeが対応範囲外です")
        return
    if arguments.argument1 == None:
        print("Error:コマンドライン引数のargument1が入力されていません\n"\
            "\"-a1=～\"または\"--argument1=～\"のように記述してください")
        return
    if arguments.mode == 0:
        if arguments.argument2 == None:
            print("Error:コマンドライン引数のargument2が入力されていません\n"\
            "\"-a2=～\"または\"--argument2=～\"のように記述してください")
            return
        resize_any_size(arguments.input_file_path, arguments.argument1, 
            arguments.argument2, save_path=arguments.output_file_path)
    if arguments.mode == 1:
        resize_similar_shape1(arguments.input_file_path, arguments.argument1, 
            save_path=arguments.output_file_path)
    if arguments.mode == 2:
        resize_similar_shape2(arguments.input_file_path, arguments.argument1, 
            save_path=arguments.output_file_path)
    if arguments.mode == 3:
        resize_similar_shape3(arguments.input_file_path, arguments.argument1, 
            save_path=arguments.output_file_path)
    print("実行完了")
    return
    

if __name__ == "__main__":
    main()