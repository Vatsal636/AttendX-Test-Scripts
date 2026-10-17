# attendance_test.py - Attendance marking test for AttendX
from selenium import webdriver
from selenium.webdriver.common.by import By
    
BASE_URL = "https://attendx.example.com"
    
def test_mark_attendance():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + "/login")
    driver.find_element(By.ID, "username").send_keys("teacher01")
    driver.find_element(By.ID, "password").send_keys("Pass@123")
    driver.find_element(By.ID, "loginBtn").click()
    driver.get(BASE_URL + "/attendance")
    driver.find_element(By.ID, "student_101_present").click()
    driver.find_element(By.ID, "saveBtn").click()
    msg = driver.find_element(By.ID, "status").text
    assert "Attendance saved" in msg
    driver.quit()
