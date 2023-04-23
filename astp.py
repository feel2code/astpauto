import os
import time

import pyperclip
import tkinter as tk

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from tkinter import scrolledtext


# load env file
load_dotenv(f"{'/'.join(os.getcwd().split('/')[:5])}/.env")


def main_loop():
    """Main method."""
    def click_button(button):
        """Click on the button."""
        while True:
            try:
                driver.find_element(By.ID, button).click()
            except NoSuchElementException:
                # minimal tested sleep
                time.sleep(1)
            else:
                break

    def enter_to_work_order():
        """Entering to work order."""
        work_order_number = work_order_entry.get()
        path_to_work_order = (
            "http://astp/maximo/ui/login?event=loadapp&value=wotrack&additionalevent=useqbe&additionaleventvalue=wonum="
            f"{work_order_number}&force"
            "reload=true"
        )
        driver.get(path_to_work_order)
        while not driver.find_element(By.ID, 'm3b854f9f-sc_div').is_displayed():
            # minimal tested sleep
            time.sleep(1)
        # making work order
        click_button('m3b854f9f-sc_div')
        element_display_status = False
        while not element_display_status:
            try:
                element_display_status = (
                    driver.find_element(By.ID, 'ma7efa7a3-tb').is_displayed()
                )
            except NoSuchElementException:
                # minimal tested sleep
                time.sleep(1)
            else:
                break
        # click to entry of js window
        click_button('ma7efa7a3-tb')

    def closing_work_order():
        """Closing work order after making changes."""
        element_display_status = False
        while not element_display_status:
            try:
                element_display_status = (
                    driver.find_element(By.ID, 'm15f1c9f0-pb').is_displayed()
                )
            except NoSuchElementException:
                # minimal tested sleep
                time.sleep(2)
            else:
                break
        click_button('m15f1c9f0-pb')
        scripts_entry.delete('1.0', tk.END)
        # text box in the GUI contains 35 symbols,
        # batch delete unfortunately not helped on version of Tkinter that tested by this program
        for i in range(35):
            work_order_entry.delete(0)

    def copy_select_script_and_execute(script: str):
        """Copy script to clipboard."""
        pyperclip.copy(script)
        enter_to_work_order()
        driver.find_element(By.ID, 'ma7efa7a3-tb').send_keys('Выполнить селект')
        click_button('m6bda82c1-ta')
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.COMMAND + "a")
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.BACKSPACE)
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.COMMAND + "v")
        click_button('m9e96a86b-tb')
        driver.find_element(By.ID, 'm9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
        # minimal tested sleep
        time.sleep(3)
        driver.find_element(By.ID, 'm9e96a86b-tb').send_keys(Keys.ENTER)
        # click_button('m1317c3f5-pb') old scheme to creation work order
        closing_work_order()

    def scripts_select_button():
        """Many selects scripts to work order."""
        insurance_number = scripts_entry.get('1.0', '1.11')
        # imported SQL scripts hid in scripts.py cause of confidential
        script = open('queries.sql', 'r').read().replace('123456789', insurance_number)
        copy_select_script_and_execute(script)

    def select_button():
        """Any select script with Insurance number of an individual personal account."""
        script = scripts_entry.get('1.0', tk.END)
        pyperclip.copy(script)
        enter_to_work_order()
        driver.find_element(By.ID, 'ma7efa7a3-tb').send_keys('Приложить выборку')
        click_button('m6bda82c1-ta')
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.COMMAND + "a")
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.BACKSPACE)
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.COMMAND + "v")
        click_button('m9e96a86b-tb')
        driver.find_element(By.ID, 'm9e96a86b-tb').send_keys(r'25. \ 25.2. \ 25.2.2.')
        # minimal tested sleep
        time.sleep(3)
        driver.find_element(By.ID, 'm9e96a86b-tb').send_keys(Keys.ENTER)
        # click_button('m1317c3f5-pb') old scheme to creation work order
        closing_work_order()

    def manual_select_button():
        """Button for manual select from DB."""
        script = scripts_entry.get('1.0', tk.END)
        copy_select_script_and_execute(script)

    def update_button():
        """Button for update scripts in DB."""
        script = scripts_entry.get('1.0', tk.END)
        pyperclip.copy(script)
        enter_to_work_order()
        driver.find_element(By.ID, 'ma7efa7a3-tb').send_keys('Просьба согласовать выполнение скриптов')
        click_button('m6bda82c1-ta')
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.COMMAND + "a")
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.BACKSPACE)
        driver.find_element(By.ID, 'm6bda82c1-ta').send_keys(Keys.COMMAND + "v")
        click_button('m9e96a86b-tb')
        driver.find_element(By.ID, 'm9e96a86b-tb').send_keys(r'25. \ 25.7.')
        # minimal tested sleep
        time.sleep(3)
        driver.find_element(By.ID, 'm9e96a86b-tb').send_keys(Keys.ENTER)
        closing_work_order()

    # window UI parameters
    window = tk.Tk()
    top_part_of_frame = tk.Frame(window)
    bottom_part_of_frame = tk.Frame(window)
    window.title('Выгрузка данных по СНИЛС в АСТП')
    window.geometry('550x400')
    work_order_entry = tk.Entry(top_part_of_frame, width=19)
    scripts_entry = scrolledtext.ScrolledText(
        bottom_part_of_frame,
        width=70,
        height=20
    )
    button_for_select = tk.Button(
        top_part_of_frame,
        text="Выборка",
        command=select_button
    )
    button_for_scripts = tk.Button(
        top_part_of_frame,
        text="Скрипты",
        command=scripts_select_button
    )
    button_for_manual_select = tk.Button(
        top_part_of_frame,
        text="Ручной селект",
        command=manual_select_button
    )
    button_for_update = tk.Button(
        top_part_of_frame,
        text="Ручной апдейт",
        command=update_button
    )
    top_part_of_frame.pack()
    bottom_part_of_frame.pack()
    work_order_entry.pack(side=tk.LEFT)
    button_for_select.pack(side=tk.LEFT)
    button_for_scripts.pack(side=tk.LEFT)
    button_for_manual_select.pack(side=tk.LEFT)
    button_for_update.pack(side=tk.LEFT)
    scripts_entry.pack(side=tk.LEFT)
    window.mainloop()


if __name__ == '__main__':
    # prepare with login to the IBM task manager, then create GUI window for work
    # enter to task manager
    opts = Options()
    # path to the webdriver
    driver_path = os.path.dirname(os.path.abspath(__file__))
    # define selenium webdriver
    driver = webdriver.Firefox(
        executable_path=driver_path + '/machine',
        service_log_path=None,
        options=opts
    )
    driver.get('http://astp/maximo/')
    # login and password of IBM WebSphere task manager
    # find userpass fields in the form
    s_username = driver.find_element(By.NAME, 'username')
    s_password = driver.find_element(By.NAME, 'password')
    # send userpass from env file
    s_username.send_keys(os.getenv('USERNAME'))
    s_password.send_keys(os.getenv('PASSWORD'))
    # check if element is displayed already
    while not driver.find_element(By.CLASS_NAME, 'tiv_btn').is_displayed():
        # minimal tested sleep
        time.sleep(1)
    # try to click submit button in login form
    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'tiv_btn').click()
        except NoSuchElementException:
            # minimal tested sleep
            time.sleep(1)
        else:
            break
    # create GUI window and loop process
    main_loop()
