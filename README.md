# Interview-Question-Creator

### Git commands

``` bash
git clone https://github.com/kishandotpandey1352/Interview-Question-Creator.git
```
```bash
git add .
```
```bash
git commit -m "code updated"
```
```bash
git push origin main
```

### How to run

1. Create virtual environment
``` bash
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
4. Make sure you have the API key from OpenAI and added the same in .env file

5. Run the application 
```bash
python app.py

```

### Use the app
#####  Upload a pdf preferably 5 pages at max
#####  Submit and
#####  Click on download button to recive the output as csv file

### Deploy the app on AWS EC2: 
##### Create an AWS instance

##### Deploy the app on AWS EC2 instance (Linux)
```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

```bash
git clone "Your-repository"
```

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```
##### If it shows error, create a virtual environment and activate it, then install all the packages

```bash
#Temporary running
python3 app.py
```

```bash
#Permanent running
http://[externalIPonAWS_Instance] - colon - [configured port] in security group under inbound rules
## http://134.44.3.2:8080
```