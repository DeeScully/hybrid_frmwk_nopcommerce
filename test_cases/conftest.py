from selenium import webdriver
import pytest

'''to run tests in parallel pass in '-n=x' param, ie for 2 tests to run in parallel, use command:
pytest -s -v -n=2'''

@pytest.fixture()
def setup(browser):
    if browser == 'chromeheadless':
        from selenium.webdriver.chrome.options import Options
        chromeoptions = Options()
        chromeoptions.headless = True
        driver = webdriver.Chrome(options=chromeoptions)
    elif browser == 'ffheadless':
        from selenium.webdriver.firefox.options import Options
        ffoptions = Options()
        ffoptions.headless = True
        driver = webdriver.Firefox(options=ffoptions)
    elif browser == 'edgeheadless':
        from msedge.selenium_tools import Edge, EdgeOptions
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("--headless")
        driver = Edge(options=options)
    # elif browser == 'vivaldi':
    #     opt = Options()
    #     opt.binary_location = r'C:\Users\Dana Scully\AppData\Local\Vivaldi\Application\vivaldi.exe'
    #     driver = webdriver.Chrome(options=opt)
    #cant get to work
    else: #default
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser): #hook that will get vals from command line
    parser.addoption('--browser')

@pytest.fixture()
def browser(request): #this will rtn the browser val to the setup method above
    return request.config.getoption('--browser')

#pytest html report: use by adding command parametre --html=reports\report.html
#hook for adding customized env info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'WaiC'

#hook to mod/del any customized env info added above
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

