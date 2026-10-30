from selenium import webdriver


def test_open_website():

    driver = webdriver.Chrome()

    try:
        print("Opening Python website...")

        driver.get("https://www.python.org")

        # Get website title
        title = driver.title

        print("Website Title:", title)

        # Verify title
        assert "Python" in title

        print("TEST PASSED: Python found in website title!")

    except AssertionError:
        print("TEST FAILED: Python not found in website title!")

    finally:
        driver.quit()
        print("Browser closed successfully.")


test_open_website()