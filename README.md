# Applying node2vec on Stock Price Data

## Installation   
pip install -r requirements.txt

### main.py arguments    
* main.py:   
    *   start: start date   
    *   end: end date   
    *   p: node2vec parameter
    *   q: node2vec parameter
    *   cor_type: correlation type ('positive', 'negative', 'both')
    *   threshold: cosine similarity threshold (absolute value)
    *   market_index: market index ('Nasdaq' or 'SnP500')   
    *   company_list: list name which I want to use ('SnP500' or 'DOW')   
    *   save_folder: folder name which png files will be saved   


* default setting   
```bash
python main.py --start 2022-04-25 --end 2022-05-23 --p 1 --q 2 --cor_type both --threshold 0.85 --market_index SnP500 --list_name SnP500 --save_folder results 
```
