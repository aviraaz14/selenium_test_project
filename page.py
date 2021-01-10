import time
from locator import mainPageLocators
from locator import hoverLocators
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'
            
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        


class MainPage(BasePage):
    search_text_element = SearchTextElement()
    def is_title_matches(self):
        return "Python" in self.driver.title
          
    
    def click_go_botton(self):
        element = self.driver.find_element(*mainPageLocators.GO_BUTTON)
        element.click()
        
    def hover_over_sub_navbar(self):
        actions = ActionChains(self.driver)
        element_about = self.driver.find_element(*hoverLocators.ABOUT_LINK)
        element_downloads = self.driver.find_element(*hoverLocators.DOWNLOADS_LINK)
        element_docummentation = self.driver.find_element(*hoverLocators.DOCUMENTATION_LINK)
        element_community = self.driver.find_element(*hoverLocators.COMMUNITY_LINK)
        element_success_stories = self.driver.find_element(*hoverLocators.SUCCESS_LINK)
        element_news = self.driver.find_element(*hoverLocators.NEWS_LINK)
        element_events = self.driver.find_element(*hoverLocators.EVENTS_LINK)
        python_wiki = self.driver.find_element(*hoverLocators.PYTHON_WIKI)
        
        actions.move_to_element(element_about).move_to_element(element_downloads)
        actions.move_to_element(element_docummentation).move_to_element(element_events)
        actions.move_to_element(element_news).move_to_element(element_success_stories)
        actions.move_to_element(element_community).move_to_element(python_wiki).click().perform()
        
        
    def is_subnav_link_workings(self):
        return "The Python Wiki" in self.driver.page_source
        
        
    class SearchResultsPage(BasePage):
        """Search results page action methods come here"""

        def is_results_found(self):
            # Probably should search for this text in the specific page
            # element, but as for now it works fine
            return "No results found." in self.driver.page_source
            # return "No results found."  not in self.driver.page_source //to check page is not empty after seacrc
    
    