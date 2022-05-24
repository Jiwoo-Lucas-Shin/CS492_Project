# CS492_Project (Jiwoo Shin, Suyeon Lee)

## Installation   
pip install -r requirements.txt

### main.py arguments    
* main.py:   
    *   start: start date   
    *   end: end date   
    *   cor_type: correlation type ('positive', 'negative', 'both')
    *   threshold: cosine similarity threshold (absolute value)
    *   market_index: market index ('Nasdaq' or 'SnP500')   
    *   company_list: list name which I want to use ('SnP500' or 'DOW')   
    *   save_folder: folder name which png files will be saved   

* default setting   
```bash
python main.py --start 2022-04-01 --end 2022-04-30 --cor_type both --threshold 0.9 --market_index SnP500 --list_name SnP500 --save_folder results 
```

## Graph Example
![clustring](https://user-images.githubusercontent.com/87713422/168440811-dc2340d9-461c-46d2-b95f-bad813f270ad.png)


## Clustering Result
![graph](https://user-images.githubusercontent.com/87713422/168440780-b81754d2-a879-4543-9215-ca52bc7836d5.png)
