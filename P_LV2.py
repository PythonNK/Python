# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (500,500)                       # ��ʃT�C�Y
    pygame.init()                           # pygame������
    pygame.display.set_mode((w, h), 0, 32)  # ��ʐݒ�
    screen = pygame.display.get_surface()
    bg = pygame.image.load("bg.jpg").convert_alpha()    # �w�i�摜�̎擾
    rect_bg = bg.get_rect()

    while (1):
        pygame.display.update()             # ��ʍX�V
        pygame.time.wait(30)                # �X�V���ԊԊu
        screen.fill((0, 20, 0, 0))          # ��ʂ̔w�i�F
        screen.blit(bg, rect_bg)            # �w�i�摜�̕`��
        
        pygame.draw.ellipse(screen,(255,0,0),(100,30,50,50),5) # �~��`��(�h��Ԃ��Ȃ�)
        pygame.draw.ellipse(screen,(255,0,0),(250,30,50,50))     # �~��`��(�h��Ԃ�)

        
        
        # �I���p�̃C�x���g����
        for event in pygame.event.get():
            if event.type == QUIT:          # ����{�^���������ꂽ�Ƃ�
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # �L�[���������Ƃ�
                if event.key == K_ESCAPE:   # Esc�L�[�������ꂽ�Ƃ�
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
        main()