# 🛠 Full Setup Instructions for RERAAgentsScraper

This guide walks you through installing and running the RERA Agents Scraper step-by-step on a Windows system (Python 3.6+).

---

## 📁 1. Clone or Download the Repository

### ✅ Option A – Clone via Git
```bash
git clone https://github.com/yashica-02/RERAAgentsScraper.git
cd RERAAgentsScraper
```

### ✅ Option B – Download ZIP
1. Visit: [https://github.com/yashica-02/RERAAgentsScraper](https://github.com/yashica-02/RERAAgentsScraper)
2. Click the green `Code` button → `Download ZIP`
3. Extract the contents into a folder (e.g., Desktop/RERAAgentsScraper)

---

## 🐍 2. Install Python

- Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- During installation, **check the box**: `Add Python to PATH`
- Verify:
```bash
python --version
```

---

## 📦 3. Install Required Python Packages

In the project folder, open Command Prompt and run:

```bash
pip install selenium pandas openpyxl
```

---

## 🌐 4. Install ChromeDriver

### Step-by-step:
1. Open Chrome → go to `Help > About Google Chrome` to find your version
2. Download the corresponding ChromeDriver:
   [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
3. Extract and move `chromedriver.exe` into the **project folder**

---

## ▶️ 5. Run the Script

In the Command Prompt inside the project folder, run:

```bash
python agentsData.py
```

---

## 📊 6. Check the Output

The script will generate:

```bash
rera_all_agents_with_progress.xlsx
```

It includes full details of all registered agents in Rajasthan.

---

## ❗Troubleshooting

| Issue                        | Fix |
|-----------------------------|-----|
| `chromedriver not found`    | Ensure `chromedriver.exe` is in the same folder as the script |
| `TypeError: service=`       | Use the `executable_path` version of the script (already set up) |
| Elements not loading        | Increase `time.sleep()` delays slightly |

---

## ✅ You’re All Set!

For any issues or improvements, feel free to open an issue or reach out.