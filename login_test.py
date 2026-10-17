# login_test.py - Login tests for AttendX
from selenium import webdriver
from selenium.webdriver.common.by import By
    
BASE_URL = "https://attendx.example.com/login"
    
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("teacher01")
    driver.find_element(By.ID, "password").send_keys("Pass@123")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Dashboard" in driver.title
    driver.quit()
    
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("teacher01")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "loginBtn").click()
    msg = driver.find_element(By.ID, "error").text
    assert "Invalid" in msg
    driver.quit()