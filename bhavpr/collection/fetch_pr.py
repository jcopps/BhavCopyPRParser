import os
import requests
import zipfile
from datetime import timedelta, date

from collection.download_helper import PrProperties
from collection.constants import PR_DATA_DIR

def download_data(start_date, delta) -> None:
    
    for offset in range(0, delta):
        cur_date = start_date + timedelta(days=offset)
        pr_props = PrProperties(
            day=cur_date.day,
            month=cur_date.month,
            year=cur_date.year
        )

        url = pr_props.get_download_url()
        print(url)
        result = requests.get(url)

        if result.status_code == 200:
           save_and_extract(result, pr_props)

def save_and_extract(response, pr_props) -> None:
    directory_name = pr_props.get_file_name(directory=True)
    directory_path = os.path.join(
        PR_DATA_DIR,
        directory_name
    )
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)

    file_name = pr_props.get_file_name(directory=False)
    file_path = os.path.join(PR_DATA_DIR, file_name)
    file_handler = open(file_path, 'wb')
    file_handler.write(response.content)
    file_handler.close()
 
    zipfile_handler = zipfile.ZipFile(file_path, 'r')
    zipfile_handler.extractall(directory_path)
        
t = date.today()
t = t - timedelta(days=365)
download_data(start_date=t, delta=365)
        

