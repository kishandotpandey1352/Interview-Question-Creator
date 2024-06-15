# Interview-Question-Creator

### Git commands

``` bash
1. git clone https://github.com/kishandotpandey1352/Interview-Question-Creator.git
2. git add .
3. git commit -m "code updated"
4. git push origin main
```
### How to run

1. Create virtual environment
``` bash
# create environment
conda create -n interviw_env python=3.10 -y
```
2. Activate the virtual python environment
```bash
conda activate interviw_env

```
3. Install all the package in the virtual environment
```bash
pip install -r requirements.txt

```
4. Make sure you hav the API from OpenAI and added the same in .env file

5. Run the application 
```bash
python app.py

```

6. Use the app
    ## 1. Upload a pdf preferably 5 pages at max
    ## 2. submit and
    ## 3. Click on download button to recive the output as csv file