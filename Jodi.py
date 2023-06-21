from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DIR_PATH = os.path.abspath(os.path.dirname(__file__))
folder_name = "\_Output"
def download_file(chromedriver_url):
     path = DIR_PATH
     options = webdriver.ChromeOptions();
     prefs = {"download.default_directory": path};
     options.add_experimental_option("prefs", prefs);
     driver = webdriver.Chrome(service_log_path=chromedriver_url, options=options)
     driver.get("http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906")
     driver.maximize_window()
     driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[1]/td/div/table/tbody/tr/td[5]/a/img").click()
     driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[1]/td/div/table/tbody/tr/td[6]/div/div/p[3]/nobr/a").click()
     driver.switch_to.window(driver.window_handles[1])
     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[1]/td[2]/input[1]')))
     download = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td[2]/input[1]").click()
     time.sleep(5)
     driver.close()

def process_file():
    path=os.path.abspath(os.path.dirname(__file__))
    list=os.listdir(path)
    time_sorted_list = sorted(list, key=os.path.getmtime)
    file_name = time_sorted_list[len(time_sorted_list) - 1]
    df = pd.read_csv(file_name, header=3)
    df.drop(0,axis=0, inplace=True)
    melted_df = df.melt(id_vars=['Time'], value_vars=df.loc['Algeria':'Total Africa NG'], var_name='Country',value_name='Value')
    melted_df.rename(columns = {'Time':'Country','Country':'Time'}, inplace = True)
    path = DIR_PATH + folder_name
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    melted_df.to_csv(os.path.join(path, 'Jodi_data.csv'), index=False)




download_file("D:/selenium/chromedriver.exe")
process_file()
