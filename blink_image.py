# -*- coding: utf-8 -*-

import pygame
import time
#import os 


#print(os.getcwd())

# مقداردهی اولیه pygame
pygame.init()

# تنظیمات صفحه نمایش
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("تصویر چشمک‌زن")

# بارگذاری تصویر
image = pygame.image.load("img.jpeg")
  # بارگذاری تصویر از فایل
image = pygame.transform.scale(image, (200, 200))  # اندازه تصویر را تنظیم کنید

# تنظیم موقعیت تصویر
image_rect = image.get_rect(center=(250, 250))

# کنترل زمان‌بندی و چشمک‌زدن
show_image = True
clock = pygame.time.Clock()

# اجرای حلقه‌ی اصلی برنامه
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # پاک کردن صفحه
    screen.fill((0, 0, 0))  # رنگ پس‌زمینه سیاه

    # نمایش و چشمک‌زدن تصویر
    if show_image:
        screen.blit(image, image_rect)

    # به‌روزرسانی صفحه نمایش
    pygame.display.flip()

    # تغییر وضعیت چشمک‌زدن
    show_image = not show_image
    time.sleep(0.5)  # تنظیم سرعت چشمک‌زدن (0.5 ثانیه)

    # محدود کردن نرخ فریم
    clock.tick(2)  # اینجا تنظیم نرخ چشمک‌زدن با تغییر فریم

# بستن Pygame
pygame.quit()

