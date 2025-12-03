import json
import time
from datetime import datetime
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DemoBlazeAdvancedTestSuite:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.base_url = "https://www.demoblaze.com/"
        self.test_results = []
        self.start_time = None

    # ================== GENERIC HELPERS ==================
    def setup(self):
        """Initialize Chrome WebDriver"""
        try:
            import os

            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-infobars")
            options.add_argument("--no-sandbox")

            chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")
            if os.path.exists(chromedriver_path):
                from selenium.webdriver.chrome.service import Service

                service = Service(chromedriver_path)
                self.driver = webdriver.Chrome(service=service, options=options)
            else:
                self.driver = webdriver.Chrome(options=options)

            self.driver.implicitly_wait(10)
            self.wait = WebDriverWait(self.driver, 20)
            print("✓ Chrome started successfully")
            return True
        except Exception as e:
            print(f"✗ Failed to start Chrome: {e}")
            traceback.print_exc()
            return False

    def teardown(self):
        if self.driver:
            try:
                self.driver.quit()
                print("✓ Browser closed")
            except Exception:
                pass

    def check_ready(self):
        return self.driver is not None and self.wait is not None

    def navigate_to_homepage(self):
        try:
            self.driver.get(self.base_url)
            time.sleep(2)
            self.close_modals()
            self.handle_alert()
            return True
        except Exception as e:
            print(f"Error loading homepage: {e}")
            return False

    def safe_click(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.3)
            element.click()
            return True
        except Exception:
            try:
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except Exception:
                return False

    def handle_alert(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None
        except Exception:
            return None

    def close_modals(self):
        # Close any bootstrap modal that might be open
        try:
            close_buttons = self.driver.find_elements(
                By.CSS_SELECTOR, "div.modal.show button.close"
            )
            for btn in close_buttons:
                self.safe_click(btn)
                time.sleep(0.3)
        except Exception:
            pass

    def log_test_result(self, tc_id, test_name, status, message=""):
        result = {
            "TC_ID": tc_id,
            "Test_Name": test_name,
            "Status": status,
            "Message": message,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.test_results.append(result)
        icon = "✓" if status == "PASS" else "✗"
        print(f"{icon} {tc_id}: {test_name} -> {status}")
        if message:
            print(f"   {message}")

    # ================== DOMAIN HELPERS ==================
    def open_category(self, category_name):
        if not self.navigate_to_homepage():
            return False
        try:
            category_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, category_name))
            )
            self.safe_click(category_link)
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#tbodyid .card"))
            )
            time.sleep(1)
            return True
        except TimeoutException:
            return False

    def open_first_product(self, category_name="Phones"):
        if not self.open_category(category_name):
            return None
        products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card")
        if not products:
            return None
        link = products[0].find_element(By.TAG_NAME, "a")
        product_name = link.text.strip() or "Product"
        self.safe_click(link)
        time.sleep(2)
        return product_name

    def go_to_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
        self.safe_click(cart_link)
        self.wait.until(EC.visibility_of_element_located((By.ID, "tbodyid")))
        time.sleep(2)

    def ensure_cart_empty(self):
        self.go_to_cart()
        while True:
            delete_buttons = self.driver.find_elements(
                By.XPATH, "//a[text()='Delete' or text()='delete']"
            )
            if not delete_buttons:
                break
            self.safe_click(delete_buttons[0])
            time.sleep(2)
        return True

    def get_cart_rows(self):
        self.go_to_cart()
        return self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")

    # ================== TEST CASES ==================
    def TC_051_Navigate_Back_From_Category(self):
        tc_id = "TC-051"
        name = "Navigate Back from Category to Homepage"
        try:
            if not self.open_category("Laptops"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open category")
                return False
            self.driver.back()
            time.sleep(2)
            if self.base_url.rstrip("/") in self.driver.current_url:
                self.log_test_result(tc_id, name, "PASS", "Returned to homepage")
                return True
            self.log_test_result(tc_id, name, "FAIL", "URL did not return to homepage")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            traceback.print_exc()
            return False

    def TC_052_Verify_Product_Count_In_Category(self):
        tc_id = "TC-052"
        name = "Verify Product Count in Category"
        try:
            if not self.open_category("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Could not open Phones")
                return False
            products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card")
            if products:
                self.log_test_result(
                    tc_id,
                    name,
                    "PASS",
                    f"Found {len(products)} products under Phones",
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "No products found")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_053_Verify_Category_Page_Title(self):
        tc_id = "TC-053"
        name = "Verify Category Page Title"
        try:
            if not self.open_category("Monitors"):
                self.log_test_result(tc_id, name, "FAIL", "Could not open Monitors")
                return False
            header = self.driver.find_element(By.ID, "cat")
            if "CATEGORIES" in header.text.upper():
                self.log_test_result(
                    tc_id, name, "PASS", "Category header displayed correctly"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Category header missing")
            return False
        except NoSuchElementException:
            self.log_test_result(tc_id, name, "FAIL", "Category header not found")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_054_Verify_Empty_Category_Handling(self):
        tc_id = "TC-054"
        name = "Verify Empty Category Handling"
        try:
            if not self.open_category("Monitors"):
                self.log_test_result(tc_id, name, "FAIL", "Could not open category")
                return False
            products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card")
            if products:
                self.log_test_result(
                    tc_id,
                    name,
                    "PASS",
                    "Category contains products; no empty state triggered",
                )
                return True
            placeholder = self.driver.find_element(By.ID, "tbodyid").text.strip()
            if placeholder:
                self.log_test_result(
                    tc_id,
                    name,
                    "PASS",
                    f"Empty category handled with message: {placeholder}",
                )
                return True
            self.log_test_result(
                tc_id, name, "FAIL", "Category empty but no placeholder shown"
            )
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_055_Verify_Product_Details_Page_Loads(self):
        tc_id = "TC-055"
        name = "Verify Product Details Page Loads"
        try:
            product_name = self.open_first_product("Phones")
            if not product_name:
                self.log_test_result(tc_id, name, "FAIL", "No product to open")
                return False
            title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "name")))
            if title:
                self.log_test_result(
                    tc_id, name, "PASS", f"Loaded product page for {title.text}"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Product title not found")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_056_Verify_Product_Image_On_Details(self):
        tc_id = "TC-056"
        name = "Verify Product Image on Details Page"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            image = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#imgp img"))
            )
            if image.get_attribute("src"):
                self.log_test_result(tc_id, name, "PASS", "Product image displayed")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Image src missing")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_057_Verify_Product_Name_On_Details(self):
        tc_id = "TC-057"
        name = "Verify Product Name on Details Page"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            name_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".name"))
            )
            if name_element.text.strip():
                self.log_test_result(
                    tc_id, name, "PASS", f"Product name displayed: {name_element.text}"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Name text empty")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_058_Verify_Product_Price_On_Details(self):
        tc_id = "TC-058"
        name = "Verify Product Price on Details Page"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            price_element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".price-container, h3")
                )
            )
            if "$" in price_element.text:
                self.log_test_result(
                    tc_id, name, "PASS", f"Price displayed: {price_element.text}"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Price text missing")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_059_Verify_Product_Description_On_Details(self):
        tc_id = "TC-059"
        name = "Verify Product Description on Details Page"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            description = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#more-information, #myTabContent, .col-sm-12")
                )
            )
            if description.text.strip():
                self.log_test_result(
                    tc_id, name, "PASS", "Product description found"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Description empty")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_060_Verify_Add_To_Cart_Button_Exists(self):
        tc_id = "TC-060"
        name = "Verify Add to Cart Button Exists"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            btn = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Add to cart']"))
            )
            if btn.is_displayed():
                self.log_test_result(tc_id, name, "PASS", "Add to cart button visible")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Button not visible")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_061_Click_Add_To_Cart_Button(self):
        tc_id = "TC-061"
        name = "Click Add to Cart Button"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
            )
            self.safe_click(btn)
            alert_text = self.handle_alert()
            if alert_text and "added" in alert_text.lower():
                self.log_test_result(tc_id, name, "PASS", alert_text)
                return True
            self.log_test_result(tc_id, name, "FAIL", "No confirmation alert")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_062_Add_Same_Product_Multiple_Times(self):
        tc_id = "TC-062"
        name = "Add Same Product Multiple Times"
        try:
            product_name = self.open_first_product("Phones")
            if not product_name:
                self.log_test_result(tc_id, name, "FAIL", "No product to add")
                return False
            btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
            )
            for _ in range(2):
                self.safe_click(btn)
                alert_text = self.handle_alert()
                if not alert_text:
                    self.log_test_result(tc_id, name, "FAIL", "Missing alert confirmation")
                    return False
                time.sleep(1)
            self.go_to_cart()
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")
            occurrences = sum(
                1 for row in rows if product_name.lower() in row.text.lower()
            )
            if occurrences >= 2:
                self.log_test_result(
                    tc_id,
                    name,
                    "PASS",
                    f"{product_name} present {occurrences} times in cart",
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Duplicate entries not found")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_063_Verify_Back_Button_On_Product_Details(self):
        tc_id = "TC-063"
        name = "Verify Back Button on Product Details"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            self.driver.back()
            time.sleep(2)
            products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card")
            if products:
                self.log_test_result(
                    tc_id, name, "PASS", "Browser back returned to category list"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Back did not show product list")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_064_Verify_Product_Details_Page_Title(self):
        tc_id = "TC-064"
        name = "Verify Product Details Page Title"
        try:
            product_name = self.open_first_product("Phones")
            if not product_name:
                self.log_test_result(tc_id, name, "FAIL", "No product to open")
                return False
            title = self.driver.title
            if "STORE" in title.upper():
                self.log_test_result(
                    tc_id,
                    name,
                    "PASS",
                    f"Browser title '{title}' displayed while viewing {product_name}",
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", f"Unexpected title: {title}")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_065_Add_Product_To_Cart_While_Not_Logged_In(self):
        tc_id = "TC-065"
        name = "Add Product to Cart While Not Logged In"
        try:
            self.navigate_to_homepage()
            self.handle_alert()
            product_name = self.open_first_product("Phones")
            if not product_name:
                self.log_test_result(tc_id, name, "FAIL", "No product to open")
                return False
            btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
            )
            self.safe_click(btn)
            alert_text = self.handle_alert()
            if alert_text and "added" in alert_text.lower():
                self.log_test_result(
                    tc_id, name, "PASS", f"Guest user added {product_name}"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "No success alert for guest add")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_066_Verify_Product_Details_Page_Responsiveness(self):
        tc_id = "TC-066"
        name = "Verify Product Details Page Responsiveness"
        try:
            if not self.open_first_product("Phones"):
                self.log_test_result(tc_id, name, "FAIL", "Failed to open product")
                return False
            self.driver.set_window_size(414, 896)  # iPhone 12 like size
            time.sleep(1)
            essential_elements = [
                (By.CSS_SELECTOR, ".name"),
                (By.CSS_SELECTOR, ".price-container"),
                (By.XPATH, "//a[text()='Add to cart']"),
            ]
            for locator in essential_elements:
                if not self.driver.find_element(*locator).is_displayed():
                    self.log_test_result(tc_id, name, "FAIL", "Element hidden on resize")
                    return False
            self.log_test_result(tc_id, name, "PASS", "Layout adapts to mobile width")
            self.driver.maximize_window()
            return True
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            try:
                self.driver.maximize_window()
            except Exception:
                pass
            return False

    def TC_067_Verify_Cart_Link_Clickable(self):
        tc_id = "TC-067"
        name = "Verify Cart Link is Clickable"
        try:
            self.navigate_to_homepage()
            cart_link = self.wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
            self.safe_click(cart_link)
            self.wait.until(EC.visibility_of_element_located((By.ID, "tbodyid")))
            self.log_test_result(tc_id, name, "PASS", "Cart link navigates correctly")
            return True
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_068_Verify_Cart_Page_Loads(self):
        tc_id = "TC-068"
        name = "Verify Cart Page Loads"
        try:
            self.go_to_cart()
            title = self.driver.find_element(By.TAG_NAME, "h2").text
            if "Products" in title:
                self.log_test_result(tc_id, name, "PASS", "Cart page loaded")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Cart title missing")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_069_Verify_Empty_Cart_Display(self):
        tc_id = "TC-069"
        name = "Verify Empty Cart Display"
        try:
            self.ensure_cart_empty()
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")
            if not rows:
                self.log_test_result(tc_id, name, "PASS", "Empty cart shows no rows")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Cart still has rows")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def add_sample_product_to_cart(self):
        product_name = self.open_first_product("Phones")
        if not product_name:
            return None
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
        )
        self.safe_click(btn)
        self.handle_alert()
        return product_name

    def TC_070_Verify_Products_Display_In_Cart(self):
        tc_id = "TC-070"
        name = "Verify Products Display in Cart"
        try:
            self.ensure_cart_empty()
            product_name = self.add_sample_product_to_cart()
            if not product_name:
                self.log_test_result(tc_id, name, "FAIL", "Could not add product")
                return False
            rows = self.get_cart_rows()
            if rows:
                self.log_test_result(
                    tc_id, name, "PASS", f"{len(rows)} product rows displayed"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "No rows present in cart")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_071_Verify_Product_Details_In_Cart(self):
        tc_id = "TC-071"
        name = "Verify Product Details in Cart"
        try:
            self.ensure_cart_empty()
            product_name = self.add_sample_product_to_cart()
            if not product_name:
                self.log_test_result(tc_id, name, "FAIL", "Could not add product")
                return False
            rows = self.get_cart_rows()
            if not rows:
                self.log_test_result(tc_id, name, "FAIL", "No cart rows found")
                return False
            row_text = rows[0].text.lower()
            if product_name.lower() in row_text and any(
                char.isdigit() for char in row_text
            ):
                self.log_test_result(
                    tc_id, name, "PASS", "Product name and price displayed"
                )
                return True
            self.log_test_result(tc_id, name, "FAIL", "Missing details in cart row")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_072_Verify_Total_Price_Calculation(self):
        tc_id = "TC-072"
        name = "Verify Total Price Calculation"
        try:
            self.ensure_cart_empty()
            self.add_sample_product_to_cart()
            self.add_sample_product_to_cart()
            rows = self.get_cart_rows()
            price_sum = 0
            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")
                if len(columns) >= 3:
                    try:
                        price_sum += int(columns[2].text.strip())
                    except ValueError:
                        pass
            total_element = self.driver.find_element(By.ID, "totalp")
            displayed_total = int(total_element.text.strip() or 0)
            if price_sum == displayed_total and price_sum > 0:
                self.log_test_result(
                    tc_id, name, "PASS", f"Total matches sum: {price_sum}"
                )
                return True
            self.log_test_result(
                tc_id,
                name,
                "FAIL",
                f"Sum {price_sum} differs from displayed {displayed_total}",
            )
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_073_Delete_Product_From_Cart(self):
        tc_id = "TC-073"
        name = "Delete Product from Cart"
        try:
            self.ensure_cart_empty()
            self.add_sample_product_to_cart()
            rows_before = self.get_cart_rows()
            if not rows_before:
                self.log_test_result(tc_id, name, "FAIL", "No rows to delete")
                return False
            delete_btn = rows_before[0].find_element(By.LINK_TEXT, "Delete")
            self.safe_click(delete_btn)
            time.sleep(2)
            rows_after = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")
            if len(rows_after) < len(rows_before):
                self.log_test_result(tc_id, name, "PASS", "Product deleted")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Row count did not decrease")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_074_Delete_All_Products_From_Cart(self):
        tc_id = "TC-074"
        name = "Delete All Products from Cart"
        try:
            self.ensure_cart_empty()
            for _ in range(2):
                self.add_sample_product_to_cart()
            rows = self.get_cart_rows()
            if len(rows) < 2:
                self.log_test_result(tc_id, name, "FAIL", "Unable to seed cart")
                return False
            self.ensure_cart_empty()
            rows_after = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")
            if not rows_after:
                self.log_test_result(tc_id, name, "PASS", "All products removed")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Rows still present after clear")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    def TC_075_Verify_Place_Order_Button_Exists(self):
        tc_id = "TC-075"
        name = "Verify Place Order Button Exists"
        try:
            self.go_to_cart()
            button = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(text(),'Place Order')]")
                )
            )
            if button.is_displayed():
                self.log_test_result(tc_id, name, "PASS", "Place Order button visible")
                return True
            self.log_test_result(tc_id, name, "FAIL", "Place Order button hidden")
            return False
        except Exception as e:
            self.log_test_result(tc_id, name, "FAIL", str(e))
            return False

    # ================== RUNNER ==================
    def run_all_tests(self):
        print("=" * 70)
        print("DemoBlaze Automation Test Suite - TC-051 to TC-075")
        print("=" * 70)

        if not self.setup():
            print("Cannot start webdriver, exiting...")
            return

        self.start_time = datetime.now()
        tests = [
            self.TC_051_Navigate_Back_From_Category,
            self.TC_052_Verify_Product_Count_In_Category,
            self.TC_053_Verify_Category_Page_Title,
            self.TC_054_Verify_Empty_Category_Handling,
            self.TC_055_Verify_Product_Details_Page_Loads,
            self.TC_056_Verify_Product_Image_On_Details,
            self.TC_057_Verify_Product_Name_On_Details,
            self.TC_058_Verify_Product_Price_On_Details,
            self.TC_059_Verify_Product_Description_On_Details,
            self.TC_060_Verify_Add_To_Cart_Button_Exists,
            self.TC_061_Click_Add_To_Cart_Button,
            self.TC_062_Add_Same_Product_Multiple_Times,
            self.TC_063_Verify_Back_Button_On_Product_Details,
            self.TC_064_Verify_Product_Details_Page_Title,
            self.TC_065_Add_Product_To_Cart_While_Not_Logged_In,
            self.TC_066_Verify_Product_Details_Page_Responsiveness,
            self.TC_067_Verify_Cart_Link_Clickable,
            self.TC_068_Verify_Cart_Page_Loads,
            self.TC_069_Verify_Empty_Cart_Display,
            self.TC_070_Verify_Products_Display_In_Cart,
            self.TC_071_Verify_Product_Details_In_Cart,
            self.TC_072_Verify_Total_Price_Calculation,
            self.TC_073_Delete_Product_From_Cart,
            self.TC_074_Delete_All_Products_From_Cart,
            self.TC_075_Verify_Place_Order_Button_Exists,
        ]

        for test in tests:
            try:
                test()
                time.sleep(1)
            except Exception as e:
                print(f"✗ Error executing {test.__name__}: {e}")
                traceback.print_exc()

        self.generate_report()
        self.teardown()

    def generate_report(self):
        if not self.test_results:
            print("No test results to report.")
            return
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        total = len(self.test_results)
        passed = len([r for r in self.test_results if r["Status"] == "PASS"])
        failed = total - passed

        print("\n" + "=" * 70)
        print("Execution Summary")
        print("=" * 70)
        print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
        print(f"Duration: {duration:.2f} seconds")

        report_name = (
            f"test_report_TC051_TC075_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        data = {
            "summary": {
                "total": total,
                "passed": passed,
                "failed": failed,
                "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "duration_seconds": duration,
            },
            "results": self.test_results,
        }
        try:
            with open(report_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✓ Report saved to {report_name}")
        except Exception as e:
            print(f"✗ Failed to save report: {e}")


if __name__ == "__main__":
    suite = DemoBlazeAdvancedTestSuite()
    suite.run_all_tests()






