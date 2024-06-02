import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
logging.info('Hello Kishan, Welcome to GenAI First project')
list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'app.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filename)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the files {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            logging.info(f"creating an empty file {filepath}")
        
    
    else:
        logging.info(f"this file {filepath} already exists")
    
            
        
        