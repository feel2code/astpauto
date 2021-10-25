#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pyperclip
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import time
from connection_configure import *
from scripts import *
import os

opts = Options()
# opts.headless = True
# enter to task manager

driver_path = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Firefox(executable_path=str(driver_path)+'/machine',
                           service_log_path=None,
                           options=opts)
driver.get('http://astp/maximo/')
# login and password of IBM WebSphere task manager hide in connection_configure.py
s_username = driver.find_element_by_name('username')
s_password = driver.find_element_by_name('password')
s_username.send_keys(username)
s_password.send_keys(password)
element_display_status = False
while not element_display_status:
    element_display_status = driver.find_element_by_class_name('tiv_btn').is_displayed()
time.sleep(2)
driver.find_element_by_class_name('tiv_btn').click()


def click_button(button):
    while True:
        try:
            driver.find_element_by_id(button).click()
        except:
            time.sleep(3)
        else:
            break


def enter_to_work_order():
    work_order_number = work_order_entry.get()
    path_to_work_order = 'http://astp/maximo/ui/login?event=loadapp&value=wotrack&additionalevent'
    path_to_work_order += '=useqbe&additionaleventvalue=wonum=' + work_order_number + '&forcereload=true'
    driver.get(path_to_work_order)
    element_display_status1 = False
    while not element_display_status1:
        element_display_status1 = driver.find_element_by_id('m3b854f9f-sc_div').is_displayed()
    # making work order
    time.sleep(2)
    click_button('m3b854f9f-sc_div')
    element_display_status2 = False
    while not element_display_status2:
        element_display_status2 = driver.find_element_by_id('ma7efa7a3-tb').is_displayed()
    # click to entry of js window
    time.sleep(2)
    click_button('ma7efa7a3-tb')


# closing work order after making changes


def closing_work_order():
    element_display_status3 = False
    while not element_display_status3:
        element_display_status3 = driver.find_element_by_id('m15f1c9f0-pb').is_displayed()
    time.sleep(2)
    click_button('m15f1c9f0-pb')
    scripts_entry.delete('1.0', tk.END)
    for i in range(35):
        work_order_entry.delete(0)


# complex selects from DB


def scripts_select_button():
    snils = scripts_entry.get('1.0', '1.11')
    # imported SQL scripts hide in scripts.py cause of confidential
    script = a1 + " " + a2 + " " + a3 + " " + a4 + " " + a5 + " " + a6 + " " + a7 + " " + a8 + " " + a9 + " " + a10
    script += " " + a11 + " " + a12 + " " + a13 + " " + a14 + " " + a15 + " " + a16 + " " + a17 + " " + a18
    script += " " + a19 + " " + a20 + " " + a21 + " " + a22 + " " + a23 + " " + a24 + " " + a25 + " " + a26
    script += " " + a27 + " " + a28
    script = script.replace('123456789', snils)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Выполнить селект')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
    click_button('m1317c3f5-pb')
    closing_work_order()


# simple select from DB


def select_button():
    script = scripts_entry.get('1.0', tk.END)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Приложить выборку')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
    click_button('m1317c3f5-pb')
    closing_work_order()


# button for manual select from DB


def manual_select_button():
    script = scripts_entry.get('1.0', tk.END)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Выполнить селект')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
    click_button('m1317c3f5-pb')
    closing_work_order()


# button for update scripts in DB


def update_button():
    script = scripts_entry.get('1.0', tk.END)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('Просьба согласовать выполнение скриптов')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id('m9e96a86b-tb').send_keys(r'25. \ 25.7.')
    click_button('m1317c3f5-pb')
    closing_work_order()

# window UI parameters


window = Tk()
top_part_of_frame = Frame(window)
bottom_part_of_frame = Frame(window)
window.title('Выгрузка данных по СНИЛС в АСТП')
window.geometry('550x400')
work_order_entry = Entry(top_part_of_frame, width=19)
scripts_entry = scrolledtext.ScrolledText(bottom_part_of_frame, width=70, height=20)
button_for_select = Button(top_part_of_frame, text="Выборка", command=select_button)
button_for_scripts = Button(top_part_of_frame, text="Скрипты", command=scripts_select_button)
button_for_manual_select = Button(top_part_of_frame, text="Ручной селект", command=manual_select_button)
button_for_update = Button(top_part_of_frame, text="Ручной апдейт", command=update_button)
top_part_of_frame.pack()
bottom_part_of_frame.pack()
work_order_entry.pack(side=LEFT)
button_for_select.pack(side=LEFT)
button_for_scripts.pack(side=LEFT)
button_for_manual_select.pack(side=LEFT)
button_for_update.pack(side=LEFT)
scripts_entry.pack(side=LEFT)
window.mainloop()
