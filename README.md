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
python main.py --start 2022-04-25 --end 2022-05-23 --cor_type both --threshold 0.9 --market_index SnP500 --list_name SnP500 --save_folder results 
```


## Ranking Results
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170003610-03630e49-74a5-4b30-a17e-0500d048d50e.PNG"></p>

## ARE vs PLD
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170003851-3c84fdc6-1055-414d-ad72-30dd0a7bfe35.PNG"></p>

## S&P500 vs AAPL
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170003761-d054656d-7524-4bd4-948f-93976193412f.PNG"></p>
