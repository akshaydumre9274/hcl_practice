from selenium import webdriver

def test_open_website():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.python.org")
        print("Website Title:", driver.title)

        assert "Python" in driver.title

    finally:
        driver.quit()


if __name__ == "__main__":
    test_open_website()