# inekle-ders-bot
this project is developed based on  [ Ceren Akyar's ZaraStockChecker project ](https://github.com/CerenAkyr/ZaraStockChecker).

I drew significant inspiration from her codes especially using selenium. So a BIG THANK YOU to her indirect help 🙏🙏
This app basically gives a sound notification whenever a lesson is added to the lesson pool by controlling html objects after automatically login to the site (inekle.com) with user informations. This way users can create a demand and increase the chance of being the instructor of the lesson as an early bird 🕊️
### REQUIREMENTS
- python 3.6 or higher
- chrome driver
### STEPS
**1-**
Clone the repository
```bash 
git clone https://github.com/husnabosun/inekle-ders-bot
cd christmas-raffle
```
**2-** 
Install chrome drivers suitable version  for your computer from the link below. I used webdriver in the code which automatically handles that,  but in case of a problem I recommend you to install it anyway.

[Google Driver Download Link](https://googlechromelabs.github.io/chrome-for-testing/)

**3-**
Install the required libraries
```bash
pip install -r requirements.txt
````
**4-**
Find the location of the file with the name chromedriver.exe, copy the path and paste it to config.json file in the project
```bash
"chrome_driver_path": "..."
```
**5-**
You can use this code for different webs, changing urls and html selectors such as 
```bash
((By.CSS_SELECTOR, ".btn.btn-green.btn-30h"))
```
**ENJOY!!**
