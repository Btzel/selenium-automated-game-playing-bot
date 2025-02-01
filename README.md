# Cookie Clicker Automation Bot
A Python automation bot using Selenium WebDriver to play the Cookie Clicker game, featuring intelligent store purchasing and continuous clicking.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-red)
![WebDriver](https://img.shields.io/badge/Chrome-WebDriver-green)
![Game](https://img.shields.io/badge/Cookie-Clicker-orange)

## 🎯 Overview
This project creates an automated gaming bot that:
1. Controls the Cookie Clicker game
2. Performs automated clicking
3. Manages store purchases
4. Optimizes resource usage
5. Runs continuously until stopped

## 🎮 Bot Features
### Automation Elements
- Continuous cookie clicking
- Timed store checks
- Optimal purchase decisions
- Resource management
- Automatic upgrades

### Game Management
- Chrome WebDriver control
- Element interaction
- Cost calculation
- Money tracking
- Purchase optimization

## 🔧 Technical Components
### Store Purchase System
```python
def buy_from_store():
    global buy_timer
    to_click = True
    while to_click:
        store_items = wait.until(ec.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#store div[id^='buy']")))
        money = int(driver.find_element(By.ID, "money")
                   .text.replace(",",""))
        
        costs = ([int(item.find_element(By.TAG_NAME, "b")
                 .text.replace(",","").split(sep=" ")[-1])
                 for item in store_items
                 if item.find_element(By.TAG_NAME,"b").text != ""])
```

### Key Features
1. **Game Interaction**
   - Automated clicking
   - Element detection
   - Purchase management
   - Timer control

2. **Resource Management**
   - Money tracking
   - Cost comparison
   - Purchase optimization
   - Timing systems

3. **Automation Control**
   - Browser automation
   - Element selection
   - Click management
   - Error handling

## 💻 Implementation Details
### Class Structure
- Selenium WebDriver setup
- Wait condition management
- Element interaction
- Purchase logic

### Game Management
- Cookie clicking
- Store monitoring
- Purchase decisions
- Resource tracking

## 🚀 Usage
1. Install required packages:
```bash
pip install selenium
```

2. Setup ChromeDriver:
```bash
# Ensure ChromeDriver is in your PATH
```

3. Run the bot:
```bash
python main.py
```

## 🎯 Bot Rules
1. Click cookie continuously
2. Check store every 5 seconds
3. Buy cheapest available upgrade
4. Monitor resources
5. Stop with Ctrl+C

## 🛠️ Project Structure
```
cookie-clicker-bot/
└── main.py           # Bot implementation
```

## 📊 Features
### Input Processing
- Mouse click simulation
- Element detection
- Cost calculation
- Timer management

### Output Management
- Purchase decisions
- Resource tracking
- Upgrade selection
- Performance monitoring

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL