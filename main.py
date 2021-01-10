import unittest
from selenium import webdriver
import page
import time

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/USER/Downloads/driver/chromedriver_win32/chromedriver.exe')
        self.driver.get('https://www.python.org/')
        self.driver.maximize_window()

    def test_title(self):
        print("title test")
        main_page = page.MainPage(self.driver)
        message = "test result pass"
        # print(main_page.is_title_matches())
        self.assertTrue(main_page.is_title_matches(), message)
        
        
    def test_search_in_python_org(self):
        
    #   Sets the text of search textbox to "pycon"
        print('test2 for search textbox and go button')
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "ramayan"
        time.sleep(1)
        main_page.click_go_botton()
        
        search_results_page = main_page.SearchResultsPage(self.driver)
        
        #Verifies that the results page is  empty
        # print(search_results_page.is_results_found())
        assert search_results_page.is_results_found(), "No results found."
        
    def test_in_sub_navbar(self):
        print('test 3: for subnav links')
        message = "nav bar link is not working"
        main_page = page.MainPage(self.driver)
        main_page.hover_over_sub_navbar()
        self.assertTrue(main_page.is_subnav_link_workings(), message)
        self.driver.back()
                 
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
        
        
        