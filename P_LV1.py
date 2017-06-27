# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((600, 500))    # 大きさ600*500の画面を生成
    pygame.display.set_caption("ゲームワン")        # タイトルバーに表示する文字
    font = pygame.font.Font(None, 55)               # フォントの設定(55px)
    while (1):
        screen.fill((0,0,0))                           # 画面を黒色(#000000)に塗りつぶし

        text = font.render("TEST", True, (255,255,255))  # 描画する文字列の設定
        
        screen.blit(text, [20, 100])                     # 文字列の表示位置
        
        pygame.draw.line(screen, (0,0,255), (100,300), (180,380), 3)   # 直線の描画

        pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50),5)   # 四角形を描画(塗りつぶしなし)
        pygame.draw.rect(screen,(0,80,0),Rect(150,150,230,200))    # 四角形を描画(塗りつぶし)

        pygame.draw.ellipse(screen,(255,0,0),(100,30,50,50),5) # 円を描画(塗りつぶしなし)
        pygame.draw.ellipse(screen,(255,0,0),(250,30,50,50))     # 円を描画(塗りつぶし)



        
        pygame.display.update()                     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:                  # 閉じるボタンが押されたら終了
                pygame.quit()                       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()