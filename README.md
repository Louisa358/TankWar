# TankWar

#### 一、初始化类

<img src="./assets/image-20221119141713624.png" alt="image-20221119141713624" style="zoom:50%;" />

###### 坦克类：敌我坦克

1、射击

2、移动类

3、显示坦克的方法

###### 子弹类

1、移动

2、显示子弹的方法

###### 墙壁类

1、属性：是否可以通过

###### 爆炸效果类

1、展示爆炸效果

###### 音效类

1、播放音乐

###### 主类

1、开始游戏

2、结束游戏



#### 二.加载主窗口

游戏功能查询：www.pygame.org

import pygame

常用功能：

1.主窗口显示：pygame.display (set_mode设置screen，fill填充颜色)



#### 三.事件处理

任务：关闭窗口及实现键盘对游戏的操控

2.获取事件： pygame.event.get()

3.按下按键：event.type == pygame.KEYDOWN

4.关闭游戏：event.type == pygame.QUIT

