# What role does the company play in the market?

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
python main.py --start 2022-04-25 --end 2022-05-23 --p 1 --q 2 --cor_type both --threshold 0.8 --market_index SnP500 --list_name SnP500 --save_folder results 
```
## Input Graph
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170006456-d40b65f6-b66a-41d1-914d-ed42c60de2c9.png"></p>

## Clustering Graph
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170007644-aa709ce3-4071-4ac2-8ffa-b86727d0dbcd.png"></p>

## Ranking Results
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170007023-0ebaff66-2a8e-4c0b-9ff6-152fe97e4d4f.PNG"></p>

## ARE vs PLD
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170003851-3c84fdc6-1055-414d-ad72-30dd0a7bfe35.PNG"></p>

## S&P500 vs AAPL
<p align="center"><img src="https://user-images.githubusercontent.com/87713422/170003761-d054656d-7524-4bd4-948f-93976193412f.PNG"></p>
