# CS492-Project

## Installation   
pip install -r requirements.txt

### main.py arguments (default value exists)    
* main.py:   
    *   start: start date (default: 2022-04-01)   
    *   end: end date (default: 2022-04-30)   
    *   threshold: cosine similarity threshold (absolute value) (default: 0.5)   
    *   list_name: list name which I want to use ('S&P500' or 'DOW') (default: DOW)   
    *   save_folder: folder name which png files will be saved (default: graph_png)   

* default setting   
'''
python main.py --start 2022-04-01 --end 2022-04-30 --threshold  --list_name DOW --save_folder graph_png
'''   

## Graph Example
![clustring](https://user-images.githubusercontent.com/87713422/168440811-dc2340d9-461c-46d2-b95f-bad813f270ad.png)


## Clustering Result
![graph](https://user-images.githubusercontent.com/87713422/168440780-b81754d2-a879-4543-9215-ca52bc7836d5.png)
