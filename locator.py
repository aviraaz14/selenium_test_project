from selenium.webdriver.common.by import By

class mainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    
    
class searchResultsLocators(object): 
    pass

class hoverLocators(object):
    ABOUT_LINK = (By.ID, 'about')
    DOWNLOADS_LINK = (By.ID, 'downloads')
    DOCUMENTATION_LINK = (By.ID, 'documentation')
    COMMUNITY_LINK = (By.ID, 'community')
    SUCCESS_LINK = (By.ID, 'success-stories')
    NEWS_LINK = (By.ID, 'news')
    EVENTS_LINK = (By.ID, 'events')
    PYTHON_WIKI = (By.LINK_TEXT, 'Python Wiki') 
    # link = driver.find_element_by_link_text('COOKIE CLICKER 2') 
      