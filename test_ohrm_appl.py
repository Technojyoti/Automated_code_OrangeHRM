from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage
from pages.logout_page import LogoutPage


# ------------------ Setup Chrome ------------------ #
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# ------------------ Login ------------------ #
login_page = LoginPage(driver)
username = "Admin"
password = "admin123"
login_page.login(username, password)
time.sleep(5)

# ------------------ Navigate to PIM ------------------ #
dashboard = DashboardPage(driver)
dashboard.navigate_to_pim()
time.sleep(3)

# Initialize PIMPage
pim_page = PIMPage(driver)
time.sleep(3)
pim_page.click_add_employee()


# ------------------ Add Employees ------------------ #
add_emp_page = AddEmployeePage(driver)
employees = [
    ("John", "A", "Doe"),
    ("Jane", "B", "Smith"),
    ("Alice", "C", "Wong"),
]

# This will click Add Employee before each entry,
# pause 3s before save and 2s after save for each employee.
results = add_emp_page.add_multiple_employees(employees, pause_before_save=3, pause_after_save=2)

print("Add results:", results)
#------------Now verify they exist in Employee List-------------#
emp_list = EmployeeListPage(driver)

# after login...
emp_list_page = EmployeeListPage(driver)

# single visual search (if you really want to run it separately)
# emp_list_page.search_and_scroll_find("Jane", pause_before_search=2, pause_after_search=2, per_row_pause=1.5)

# better: use verify_multiple_employees and capture results
verify_results = emp_list_page.verify_multiple_employees(
    employees,
    pause_after_search=1.5,
    per_row_pause=1.0
)

print("Verify results:", verify_results)
logout_page = LogoutPage(driver)
logout_page.logout_from_dashboard()



