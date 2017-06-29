# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

def main():
    (w,h) = (SCREEN_SIZE)
    (x,y) = (w/2, h/2)
    pygame.init()                                # pygame初期化
    pygame.display.set_mode(SCREEN_SIZE, 0, 32)  # 画面設定
    
    pygame.display.set_caption("ゲームワン")        # タイトルバーに表示する文字
    
    screen = pygame.display.get_surface()
    
    # イメージを用意
    backImg = pygame.image.load("moriyama.jpg").convert()     # 背景

    pythonImg = pygame.image.load("python.png").convert_alpha()  # 蛇
    
    planeImg = pygame.image.load("plane.png").convert()
    
    colorkey = planeImg.get_at((0,0))  # 左上の色を透明色に
    planeImg.set_colorkey(colorkey, RLEACCEL)
    
    rect_backImg = backImg.get_rect()
    
    rect_player = planeImg.get_rect()
    rect_player.center = (x, y)
    
    vx = vy = 10  # キーを押したときの移動距離
    
    cur_pos = (0,0)    # 蛇の位置
    pythons_pos = []   # コピーした蛇の位置リスト
    
    while (1):
        screen.blit(backImg, rect_backImg)        # 背景を描画


        # 終了用のイベント処理
        for event in pygame.event.get():
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                # 矢印キーなら画像を移動
                if event.key == K_LEFT:
                    rect_player.move_ip(-vx, 0)
                if event.key == K_RIGHT:
                    rect_player.move_ip(vx, 0)
                if event.key == K_UP:
                    rect_player.move_ip(0, -vy)
                if event.key == K_DOWN:
                    rect_player.move_ip(0, vy)
        # マウスクリックで蛇をコピー
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:  # 左クリック
            x, y = pygame.mouse.get_pos()
            x -= pythonImg.get_width() / 2
            y -= pythonImg.get_height() / 2
            pythons_pos.append((x,y))  # 蛇の位置を追加
        
        # マウス移動で蛇を移動
        x, y = pygame.mouse.get_pos()
        x -= pythonImg.get_width() / 2
        y -= pythonImg.get_height() / 2
        cur_pos = (x,y)

        # 蛇を表示
        screen.blit(pythonImg, cur_pos)
        for i, j in pythons_pos:
            screen.blit(pythonImg, (i,j))

        screen.blit(planeImg, rect_player)

        pygame.display.update()             # 画面更新

if __name__ == "__main__":
        main()
        
