# 🧮 Body Mass Index (BMI) Calculator 3000™ 🏋️‍♀️💪

Welcome to the **BMI Calculator 3000™**, your friendly neighborhood Python script that tells you how your body stacks up — literally! Whether you're metric-minded or live by the imperial inch, this program’s got your back (and front, and everything in between).

---

## 🌟 Features

- 🧠 Calculates your **BMI** using either **metric** or **imperial** units  
- 📏 Supports height in meters or feet+inches  
- ⚖️ Handles weight in kilograms or pounds  
- 🩺 Gives you an instant **health classification**:
  - *Underweight*
  - *Normal Weight*
  - *Overweight*
  - *Obese*

---

## 🚀 How to Use

1. Clone the repo or download the Python script.

```bash
git clone https://github.com/your-username/bmi-calculator.git
cd bmi-calculator
```

2. Run the program:
```bash
python main.py
```

3. Follow the friendly prompts:
- Choose your unit system: `metric` or `imperial`
- Enter your weight (kg or lbs)
- Enter your height (meters or feet + inches)

4. 💥 Boom! Get your BMI and health classification instantly.

---
## 🧪 Example Run
Metric:
```bash
Welcome to the BMI Calculator
Choose unit system (metric/imperial): metric
Enter your weight in kilograms: 70
Enter your height in meters: 1.75

Your BMI Is: 22.86
Health Classification: Normal Weight
```

Imperial:
```bash
Welcome to the BMI Calculator
Choose unit system (metric/imperial): imperial
Enter your weight in pounds: 180
Enter your height (feet): 5
Enter your height (inches): 11

Your BMI Is: 25.10
Health Classification: Overweight
```

## 📦 What's Inside?
`calculate_bmi(weight, height, unit='metric')`
The brains of the operation. Uses different math for different units:
- Metric: `BMI = weight / height²`
- Imperial: `BMI = 703 × weight / height²`

`classify_bmi(bmi)`
Gives you a quick health status:
- < 18.5 → Underweight
- 18.5 – 24.9 → Normal Weight
- 25 – 29.9 → Overweight
- 30+ → Obese

`main()`
User-friendly CLI flow that makes it easy for anyone to use.
---
## ⚠️ Gotchas
- You must enter positive numbers for weight and height.
- Don't try entering "banana" as your height. Python will be very confused. 🍌😵
- Negative weight? Consult a wizard.
---
## 🎯 Ideal For
- Health and fitness apps
- School projects
- Anyone wondering "Is my snack habit catching up with me?"
---
## 🛠️ Future Upgrades?
- 💻 Web-based BMI calculator
- 📊 Graphical BMI trends over time
- 🤖 Voice-activated “Hey Python, how healthy am I?”

## 📄 License
MIT License. Free to fork, fix, and flex with. 💪
---
## 👤 Author
Coded by [RedHoodJT1988](https://github.com/RedHoodJT1988) — fitness enthusiast (of the keyboard).