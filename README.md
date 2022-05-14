# CS492-Project

## Installation   
pip install -r requirements.txt

### main.py arguments (default value exists)    
* main.py:   
    *   start: start date   
    *   end: end date   
    *   threshold: cosine similarity threshold (absolute value)   
    *   list_name: list name which I want to use ('S&P500' or 'DOW')   
    *   save_folder: path you want to save the png images   

      python main.py --start 2022-04-01 --end 2022-04-30 --threshold 0.5 --list_name DOW --save_folder graph_png
