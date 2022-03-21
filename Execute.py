
from Selenium.PageChecks import SeleniumActions
from Selenium.ConFigFile import config_object
c_path = config_object["variables"]["chromepath"]
url = config_object["variables"]["url"]
obj = SeleniumActions( c_path)
obj.load_url(url)