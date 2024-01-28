from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_retrieve_it_later(self):
        # Writing user story for checking the todo app and adding list to the app. Checking the link specific to the user.
        # Sachin hearing about the todo app goes and checks the home page.
        self.browser.get("http://localhost:8000")

        # he notices the title and header mention to-do lists
        self.assertIn("To-Do lists", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do lists", header_text)

        # he is invited to enter a to-do item straight away
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # He types "Buy toothbrush" in a textbox
        input_box.send_keys("Buy toothbrush")

        # when he hits enter, the page updates and now the page lists "1: Buy toothbrush"
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Buy toothbrush" for row in rows),
            "New to do item does not appear",
        )
        self.fail("Finish the test!")

        # There is still a text box inviting him to add another entry. He adds "Brush with the new toothbrush"

        # the page updates and he sees both the item on the list

        # He wonders whether the site remebers his list and he sees the site has generated a unique link for him.

        # He visits that link. His to-do lists are still there


if __name__ == "__main__":
    unittest.main()
