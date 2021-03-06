from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pyperclip
import tkinter as tk
from tkinter import scrolledtext
import time
from connection_configure import username, password
from scripts import script_all_tables
import os


# enter to task manager
opts = Options()
driver_path = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Firefox(
    executable_path=driver_path + '/machine',
    service_log_path=None,
    options=opts
)
driver.get('http://astp/maximo/')
# login and password of IBM WebSphere task manager
# hide in connection_configure.py
s_username = driver.find_element_by_name('username')
s_password = driver.find_element_by_name('password')
s_username.send_keys(username)
s_password.send_keys(password)

element_display_status = False
while not element_display_status:
    element_display_status = (
        driver.find_element_by_class_name('tiv_btn').is_displayed()
    )
while True:
    try:
        driver.find_element_by_class_name('tiv_btn').click()
    except:
        time.sleep(1)
    else:
        break


def click_button(button):
    """Click on the button."""
    while True:
        try:
            driver.find_element_by_id(button).click()
        except:
            time.sleep(1)
        else:
            break


def enter_to_work_order():
    """Entering to work order."""
    work_order_number = work_order_entry.get()
    path_to_work_order = (
        'http://astp/maximo/ui/login?event='
        'loadapp&value=wotrack&additionalevent'
        '=useqbe&additionaleventvalue=wonum='
        + work_order_number + '&forcereload=true'
    )
    driver.get(path_to_work_order)
    
    element_display_status1 = False
    while not element_display_status1:
        element_display_status1 = (
            driver.find_element_by_id('m3b854f9f-sc_div').is_displayed()
        )
    
    # making work order
    click_button('m3b854f9f-sc_div')
    element_display_status2 = False
    while not element_display_status2:
        try:
            element_display_status2 = (
                driver.find_element_by_id('ma7efa7a3-tb').is_displayed()
            )
        except:
            time.sleep(1)
        else:
            break
    # click to entry of js window
    click_button('ma7efa7a3-tb')


def closing_work_order():
    """Closing work order after making changes."""
    element_display_status3 = False
    while not element_display_status3:
        try:
            element_display_status3 = (
                driver.find_element_by_id('m15f1c9f0-pb').is_displayed()
            )
        except:
            time.sleep(2)
        else:
            break
    click_button('m15f1c9f0-pb')
    scripts_entry.delete('1.0', tk.END)
    for i in range(35):
        work_order_entry.delete(0)


def scripts_select_button():
    """Many selects scripts to work order."""
    snils = scripts_entry.get('1.0', '1.11')
    # imported SQL scripts hid in scripts.py cause of confidential
    script = script_all_tables.replace('123456789', snils)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('?????????????????? ????????????')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id(
        'm9e96a86b-tb'
        ).send_keys(
            r'25. \ 25.2. \ 25.2.2.'
        )
    time.sleep(3)
    driver.find_element_by_id('m9e96a86b-tb').send_keys(Keys.ENTER)
    # click_button('m1317c3f5-pb') old scheme to creation work order
    closing_work_order()


def select_button():
    """Any select script by SNILS."""
    script = scripts_entry.get('1.0', tk.END)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('?????????????????? ??????????????')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id(
        'm9e96a86b-tb'
        ).send_keys(
            r'25. \ 25.2. \ 25.2.2.'
        )
    time.sleep(3)
    driver.find_element_by_id('m9e96a86b-tb').send_keys(Keys.ENTER)
    # click_button('m1317c3f5-pb') old scheme to creation work order
    closing_work_order()


def manual_select_button():
    """Button for manual select from DB."""
    script = scripts_entry.get('1.0', tk.END)
    pyperclip.copy(script)
    enter_to_work_order()
    driver.find_element_by_id('ma7efa7a3-tb').send_keys('?????????????????? ????????????')
    click_button('m6bda82c1-ta')
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "a")
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.BACKSPACE)
    driver.find_element_by_id('m6bda82c1-ta').send_keys(Keys.COMMAND + "v")
    click_button('m9e96a86b-tb')
    driver.find_element_by_id(
            'm9e96a86b-tb'
        ).send_keys(
            r'25. \ 25.2. \ 25.2.2.'
        )
    time.sleep(3)
    driver.find_element_by_id('m9e96a86b-tb').send_keys(Keys.ENTER)
    # click_button('m1317c3f5-pb') old scheme to creation work order
    closing_work_order()


def update_button():
    """Button for update scripts in DB."""
    script = scripts_entry.get('1.0', tk.END)
    pyperclip.copy(script)
    enter_to_work_order()
    
    driver.find_element_by_id(
        'ma7efa7a3-tb'
    ).send_keys(
        '?????????????? ?????????????????????? ???????????????????? ????????????????'
    )
    click_button(
        'm6bda82c1-ta'
    )
    driver.find_element_by_id(
        'm6bda82c1-ta'
    ).send_keys(
        Keys.COMMAND + "a"
    )
    driver.find_element_by_id(
        'm6bda82c1-ta'
    ).send_keys(
        Keys.BACKSPACE
    )
    driver.find_element_by_id(
        'm6bda82c1-ta'
    ).send_keys(
        Keys.COMMAND + "v"
    )
    click_button('m9e96a86b-tb')
    driver.find_element_by_id(
        'm9e96a86b-tb'
    ).send_keys(
        r'25. \ 25.7.'
    )
    
    time.sleep(3)
    driver.find_element_by_id(
        'm9e96a86b-tb'
    ).send_keys(
        Keys.ENTER
    )
    closing_work_order()


# window UI parameters
window = tk.Tk()
top_part_of_frame = tk.Frame(window)
bottom_part_of_frame = tk.Frame(window)
window.title('???????????????? ???????????? ???? ?????????? ?? ????????')
window.geometry('550x400')
work_order_entry = tk.Entry(top_part_of_frame, width=19)
scripts_entry = scrolledtext.ScrolledText(
    bottom_part_of_frame,
    width=70,
    height=20
)
button_for_select = tk.Button(
    top_part_of_frame,
    text="??????????????",
    command=select_button
)
button_for_scripts = tk.Button(
    top_part_of_frame,
    text="??????????????",
    command=scripts_select_button
)
button_for_manual_select = tk.Button(
    top_part_of_frame,
    text="???????????? ????????????",
    command=manual_select_button
)
button_for_update = tk.Button(
    top_part_of_frame,
    text="???????????? ????????????",
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
