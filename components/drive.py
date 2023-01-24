import pandas as pd

def get_drive_file(link):
    url = link
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    df = pd.read_csv(dwn_url)
    
    return df

   