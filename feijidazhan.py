import  pygame
import os
import time
from pygame.locals import *
import random

class Heroplane(object):
    def __init__(self,screen_1):
        self.x=210
        self.y=625
        self.screen=screen_1
        self.image=pygame.image.load(os.path.join(r'E:\BaiduNetdiskDownload\python就业班\01基础\第3节 项目-飞机大战\02.飞机大战-2\源码\feiji\hero1.png'))
        self.bullet_list=[]#存储发射的子弹

    def diasplay(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.diasplay()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)


    def move_left(self):
        self.x -=10
    def move_right(self):
        self.x +=10
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class Enemyplane(object):
    def __init__(self,screen_1):
        self.x=0
        self.y=0
        self.screen=screen_1
        self.image=pygame.image.load(os.path.join(r'E:\BaiduNetdiskDownload\python就业班\01基础\第3节 项目-飞机大战\02.飞机大战-2\源码\feiji\enemy0.png'))
        self.bullet_list=[]#存储发射的子弹
        self.direction="right"#控制敌机飞行方向

    def diasplay(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.diasplay()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move(self):
        if self.direction=="right":
            self.x+=5
        elif self.direction=="left":
            self.x-=5
        if self.x>480-50:
            self.direction="left"
        elif self.x<0:
            self.direction="right"

    def fire(self):
        random_num=random.randint(1,100)
        if random_num==20 or random_num==70:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


class Bullet(object):
    def __init__(self,screen_1 ,x,y):
        self.x=x+40
        self.y=y-20
        self.screen=screen_1#将self.screen转化为screen,使下面display正常使用
        self.image=pygame.image.load(os.path.join(r'E:\BaiduNetdiskDownload\python就业班\01基础\第3节 项目-飞机大战\02.飞机大战-2\源码\feiji\bullet.png'))
    def diasplay(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y-=5
    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self,screen_1 ,x,y):
        self.x=x+25
        self.y=y+39
        self.screen=screen_1#将self.screen转化为screen,使下面display正常使用
        self.image=pygame.image.load(os.path.join(r'E:\BaiduNetdiskDownload\python就业班\01基础\第3节 项目-飞机大战\02.飞机大战-2\源码\feiji','bullet1.png'))
    def diasplay(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y+=10
    def judge(self):
        if self.y>625:
            return True
        else:
            return False



def key_control(hero_1):
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_1.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_1.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_1.fire()


def main():
    #1创建窗口
    screen = pygame.display.set_mode((480,750),0,32)
    #2创建一个背景图片
    background = pygame.image.load(os.path.join(r'E:\BaiduNetdiskDownload\python就业班\01基础\第3节 项目-飞机大战\02.飞机大战-2\源码\feiji\background.png'))
    #3创建一个飞机对象
    hero = Heroplane(screen)
    #创建敌机对象
    enemy=Enemyplane(screen)

    while True:

        screen.blit(background,(0,0))#3放置背景图片

        hero.diasplay()#5放置飞机图片

        enemy.diasplay()#放置敌机

        enemy.move()#调用敌机的移动

        enemy.fire()#敌机开火

        #让所有图片刷新显示
        pygame.display.update()
        time.sleep(0.05)
        # 获取事件，比如按键等
        key_control(hero)

if __name__=="__main__":
    main()
