#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Приложение разработано для внутреннего оперативного создания тасок в интерфейсе таскменеджера IBM WebSphere
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pyperclip
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import time
from connectconf import *
from scripts import *
# запуск браузера в фоне
opts = Options()
# opts.headless = True # раскомментировать для запуска в фоне
# вход в астп
driver = webdriver.Firefox(executable_path='/Users/felixmac/Documents/PyCharmProjects/astpauto/geckodriver',
                           service_log_path='/Users/felixmac/Documents/PyCharmProjects/astpauto/driver.log',
                           options=opts)
# домен скрыт в целях безопасности
driver.get('http://astp/maximo/')
# логин пароль для входа в интерфейс IBM WebSphere
s_username = driver.find_element_by_name("username")
s_password = driver.find_element_by_name('password')
s_username.send_keys(username)
s_password.send_keys(password)
status = False
while not status:
    try:
        status = driver.find_element_by_class_name('tiv_btn').is_displayed()
    except ImportError:
        status = False
driver.find_element_by_class_name('tiv_btn').click()
status = False
while not status:
    try:
        status = driver.find_element_by_id('m7f8f3e49_ns_menu_WO_MODULE_a').is_displayed()
    except ImportError:
        status = False
driver.find_element_by_id('m7f8f3e49_ns_menu_WO_MODULE_a').click()
status = False
while not status:
    try:
        status = driver.find_element_by_id('m7f8f3e49_ns_menu_WO_MODULE_sub_changeapp_WOTRACK').is_displayed()
    except ImportError:
        status = False
if status:
    driver.find_element_by_id('m7f8f3e49_ns_menu_WO_MODULE_sub_changeapp_WOTRACK').click()
# запуск веб драйвера


def gecko():
    rz = txt.get()
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(rz)
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(Keys.RETURN)
    status1 = False
    while not status1:
        try:
            status1 = driver.find_element_by_id('m3b854f9f-sc_div').is_displayed()
        except ImportError:
            status1 = False
    # создаем ДРЗ
    time.sleep(1)
    driver.find_element_by_id('m3b854f9f-sc_div').click()
    status2 = False
    while not status2:
        try:
            status2 = driver.find_element_by_id('ma7efa7a3-tb').is_displayed()
        except ImportError:
            status2 = False
    # Вводим данные по задаче
    time.sleep(1)
    driver.find_element_by_id('ma7efa7a3-tb').click()

# закрыть после создания ДРЗ


def zakrit():
    status3 = False
    while not status3:
        try:
            status3 = driver.find_element_by_id('m15f1c9f0-pb').is_displayed()
        except ImportError:
            status3 = False
    time.sleep(2)
    driver.find_element_by_id('m15f1c9f0-pb').click()
# кнопка для скриптов


def clicked():
    snils = txt2.get('1.0', '1.11')
    # импорт SQL скриптов для выполнения. Содержимое скрыто в целях конфиденциальности
    script = a1 + " " + a2 + " " + a3 + " " + a4 + " " + a5 + " " + a6 + " " + a7 + " " + a8 + " " + a9 + " " + a10
    script = script + " " + a11 + " " + a12 + " " + a13 + " " + a14 + " " + a15 + " " + a16 + " " + a17 + " " + a18
    script = script + " " + a19 + " " + a20 + " " + a21 + " " + a22 + " " + a23 + " " + a24 + " " + a25 + " " + a26
    script = script + " " + a27 + " " + a28
    script = script.replace('123456789', snils)
    pyperclip.copy(script)
    gecko()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Выполнить селект')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    zakrit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1
# кнопка для выборки


def clickedvib():
    script = txt2.get('1.0', tk.END)
    pyperclip.copy(script)
    gecko()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Приложить выборку')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    zakrit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1
# кнопка ручного селекта


def clickedmanual():
    script = txt2.get('1.0', tk.END)
    pyperclip.copy(script)
    gecko()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Выполнить селект')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    zakrit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1
# кнопка апдейта


def clickedupdate():
    script = txt2.get('1.0', tk.END)
    pyperclip.copy(script)
    gecko()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Просьба согласовать выполнение скриптов')
    driver.find_element_by_id('m6bda82c1-ta').click()
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    driver.find_element_by_id('m9e96a86b-tb').click()
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.7.')
    driver.find_element_by_id('m1317c3f5-pb').click()
    zakrit()
    txt2.delete('1.0', tk.END)
    i = 0
    while i < 35:
        txt.delete(0)
        i += 1
# проверка выполнения


def chotam():
    rz = txt.get()
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(rz)
    driver.find_element_by_id('quicksearch').click()
    driver.find_element_by_id('quicksearch').send_keys(Keys.RETURN)
    status4 = False
    while not status4:
        try:
            status4 = driver.find_element_by_id('m4326cf1d-tab_anchor').is_displayed()
        except ImportError:
            status4 = False
    time.sleep(2)
    driver.find_element_by_id('m4326cf1d-tab_anchor').click()
    status5 = False
    while not status5:
        try:
            status5 = driver.find_element_by_id('toolactions_RESETREC-tbb_anchor').is_displayed()
        except ImportError:
            status5 = False
    time.sleep(2)
    driver.find_element_by_id('toolactions_RESETREC-tbb_anchor').click()
# настройка окна


window = Tk()
top = Frame(window)
bottom = Frame(window)
bottom2 = Frame(window)
window.title('Выгрузка данных по СНИЛСУ в АСТП')
window.geometry('550x400')
txt = Entry(top, width=19)
txt2 = scrolledtext.ScrolledText(bottom, width=70, height=20)
btn1 = Button(top, text="Выборка", command=clickedvib)
btn = Button(top, text="Скрипты", command=clicked)
btn2 = Button(top, text="Ручной селект", command=clickedmanual)
btn3 = Button(top, text="Ручной апдейт", command=clickedupdate)
btnchck = Button(bottom2, text='Проверка', command=chotam)
top.pack()
bottom.pack()
bottom2.pack()
txt.pack(side=LEFT)
btn1.pack(side=LEFT)
btn.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
txt2.pack(side=LEFT)
btnchck.pack(side=LEFT)
window.mainloop()
