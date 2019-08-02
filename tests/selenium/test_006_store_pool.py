# Author: Rishabh Chauhan
# License: BSD

import pytest
import sys
import os
import time
cwd = str(os.getcwd())
sys.path.append(cwd)
from function import take_screenshot, wait_on_element, error_check

from source import pool1, pool2


skip_mesages = "Skipping first run"
script_name = os.path.basename(__file__).partition('.')[0]

xpaths = {
    'navStorage': '//*[@id="nav-5"]/div/a[1]',
    'submenuPool': '//*[@id="5-0"]',
    'addAction': '//*[@id="add_action_button"]',
    'forwardButton': '//*[@id="custom_button"]',
    'newpoolName': '//*[@id="pool-manager__name-input-field"]',
    'disk1Checkbox': "//mat-checkbox[@id='pool-manager__disks-ada1']/label/div",
    'disk2Checkbox': "//mat-checkbox[@id='pool-manager__disks-ada2']/label/div",
    'disk3Checkbox': "//mat-checkbox[@id='pool-manager__disks-ada3']/label/div",
    'diskselectedmoveButton': '//*[@id="vdev__add-button"]',
    'createButton': '//*[@id="pool-manager__create-button"]',
    # very important and useful
    # 'confirmCheckbox': '//*[contains(@name, "confirm_checkbox")]',
    # or
    'confirmCheckbox': '//*[@id="confirm-dialog__confirm-checkbox"]/label/div',
    # 'createpoolButton': '//*[contains(text(), "CREATE POOL")]'
    # or
    'createpoolButton': '//*[@id="confirm-dialog__action-button"]/span',
    'breadcrumbBar1': "//div[@id='breadcrumb-bar']/ul/li/a",
    'breadcrumbBar2': "//*[@id='breadcrumb-bar']/ul/li[2]/a",
    'pool1Table': f"//mat-panel-title[contains(.,'{pool1}')]",
    'pool2Table': f"//mat-panel-title[contains(.,'{pool2}')]",
    'toDashboard': "//span[contains(.,'Dashboard')]",
    'pool2MatIcon': f"//mat-icon[@id='actions_menu_button__{pool2}']",
    'pool2AddDataset': f"//span[@id='action_button__{pool2}_Add Dataset']/button/span",
    'datasetName': "//input[@placeholder='Name']",
    'saveDataset': "//button[@id='save_button']"

}

dataset_list = [f'dataset {x}' for x in range(5)]


def test_01_nav_store_pool(browser):
    # Click  Storage menu
    a = browser.find_element_by_xpath(xpaths['navStorage'])
    a.click()
    # allowing the button to load
    time.sleep(1)
    # Click Pool sub-menu
    browser.find_element_by_xpath(xpaths['submenuPool']).click()
    # get the ui element
    ui_element = browser.find_element_by_xpath(xpaths['breadcrumbBar1'])
    # get the weather data
    page_data = ui_element.text
    # assert response
    assert "Storage" in page_data, page_data
    # get the ui element
    ui_element = browser.find_element_by_xpath(xpaths['breadcrumbBar2'])
    # get the weather data
    page_data = ui_element.text
    # assert response
    assert "Pools" in page_data, page_data
    # taking screenshot
    test_name = sys._getframe().f_code.co_name
    take_screenshot(browser, script_name, test_name)


def test_02_create_a_pool(browser):
    test_name = sys._getframe().f_code.co_name
    time.sleep(1)
    # Click create new pool option
    browser.find_element_by_xpath(xpaths['addAction']).click()
    # Click create Pool Button
    browser.find_element_by_xpath(xpaths['forwardButton']).click()
    # Enter User Full name
    browser.find_element_by_xpath(xpaths['newpoolName']).send_keys(pool1)
    # Select the disk
    browser.find_element_by_xpath(xpaths['disk1Checkbox']).click()
    # Select the disk
    browser.find_element_by_xpath(xpaths['diskselectedmoveButton']).click()
    # Click on create new Pool button
    browser.find_element_by_xpath(xpaths['createButton']).click()
    # checkbox confirmation
    browser.find_element_by_xpath(xpaths['confirmCheckbox']).click()
    # Click Ok Button
    browser.find_element_by_xpath(xpaths['createpoolButton']).click()
    xpath = xpaths['addAction']
    wait = wait_on_element(browser, xpath, script_name, test_name)
    assert wait, f'Creating the new pool {pool1} timeout'
    # taking screenshot
    take_screenshot(browser, script_name, test_name)
    no_error = error_check(browser)
    assert no_error['result'], no_error['traceback']


def test_03_looking_if_the_new_pool_exist(browser):
    test_name = sys._getframe().f_code.co_name
    xpath = xpaths['pool1Table']
    wait = wait_on_element(browser, xpath, script_name, test_name)
    assert wait, 'Loading pool table timeout'
    # get the ui element
    ui_element = browser.find_element_by_xpath(xpaths['pool1Table'])
    element_text = ui_element.text
    # assert response
    assert pool1 in element_text, element_text
    # taking screenshot
    take_screenshot(browser, script_name, test_name)


def test_04_create_newpool2(browser):
    test_name = sys._getframe().f_code.co_name
    time.sleep(1)
    # Click create new pool option
    browser.find_element_by_xpath(xpaths['addAction']).click()
    # Click create Pool Button
    browser.find_element_by_xpath(xpaths['forwardButton']).click()
    # Enter User Full name
    browser.find_element_by_xpath(xpaths['newpoolName']).send_keys(pool2)
    # Select the 2 disks
    browser.find_element_by_xpath(xpaths['disk2Checkbox']).click()
    browser.find_element_by_xpath(xpaths['disk3Checkbox']).click()
    # Select the disk
    browser.find_element_by_xpath(xpaths['diskselectedmoveButton']).click()
    # Click on create new Pool button
    browser.find_element_by_xpath(xpaths['createButton']).click()
    # check box confirmation
    browser.find_element_by_xpath(xpaths['confirmCheckbox']).click()
    # Click OK Button
    browser.find_element_by_xpath(xpaths['createpoolButton']).click()
    xpath = xpaths['addAction']
    wait = wait_on_element(browser, xpath, script_name, test_name)
    assert wait, f'Creating the new pool {pool2} timeout'
    # taking screenshot
    take_screenshot(browser, script_name, test_name)
    no_error = error_check(browser)
    assert no_error['result'], no_error['traceback']


def test_05_looking_if_the_new_pool_exist(browser):
    test_name = sys._getframe().f_code.co_name
    xpath = xpaths['pool2Table']
    wait = wait_on_element(browser, xpath, script_name, test_name)
    assert wait, 'Loading pool table timeout'
    # get the ui element
    ui_element = browser.find_element_by_xpath(xpaths['pool2Table'])
    element_text = ui_element.text
    # assert response
    assert pool2 in element_text, element_text
    # taking screenshot
    take_screenshot(browser, script_name, test_name)


@pytest.mark.parametrize('dataset', dataset_list)
def test_06_created_dataset_name_(browser, dataset):
    test_name = sys._getframe().f_code.co_name
    xpath = xpaths['pool2MatIcon']
    wait_element = wait_on_element(browser, xpath, script_name, test_name)
    assert wait_element, f'Wait on element timeout: {xpath}'
    browser.find_element_by_xpath(xpaths['pool2MatIcon']).click()
    browser.find_element_by_xpath(xpaths['pool2AddDataset']).click()
    xpath = xpaths['datasetName']
    wait_element = wait_on_element(browser, xpath, script_name, test_name)
    assert wait_element, f'Wait on element timeout: {xpath}'
    browser.find_element_by_xpath(xpaths['datasetName']).send_keys(dataset)
    browser.find_element_by_xpath(xpaths['saveDataset']).click()


def test_07_return_to_dashboard(browser):
    # Close the System Tab
    browser.find_element_by_xpath(xpaths['toDashboard']).click()
    time.sleep(1)
    # get the ui element
    ui_element = browser.find_element_by_xpath(xpaths['breadcrumbBar1'])
    # get the weather data
    page_data = ui_element.text
    # assert response
    assert page_data == "Dashboard", page_data
    # taking screenshot
    test_name = sys._getframe().f_code.co_name
    take_screenshot(browser, script_name, test_name)
