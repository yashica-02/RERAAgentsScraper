#  RERA Agents Scraper – Rajasthan

This Python script automates the process of extracting **registered real estate agent details** from the [RERA Rajasthan official website](https://rera.rajasthan.gov.in/agents/). It navigates through all pages of the listing, opens each agent's detailed view, scrapes relevant data, and saves it into a structured Excel file.

---

## 📌 Features

- ✅ Full agent profile scraping (name, registration no., address, contact, etc.)
- 🔁 Automatic pagination handling (scrapes all pages)
- 💾 Exports data to `Excel (.xlsx)` format
- 🧠 Progress tracking in terminal (page & agent count)

---

## ⚙️ Requirements

- Python 3.6+
- Google Chrome
- ChromeDriver (must match your browser version)

### 📦 Install dependencies

```bash
pip install selenium pandas openpyxl
```

---

## 📊 Sample Output Fields

- First Name, Middle Name, Last Name
- Father’s Name
- District, Tehsil, City, Pin Code
- Email, Mobile Number
- Registration No. & Application No.
- Criminal Case / Conviction status
- Registration in other states

---

## 🚀 Notes

- Script may take some time to complete due to the large number of agents (11k+).
- Make sure Chrome and ChromeDriver versions match.
- Avoid interrupting the script once it's running to prevent data loss.

---

## 📩 Contact

Created by [Yashica Sharma](https://github.com/yashica-02)  
Feel free to reach out or open an issue for questions or suggestions.

---

## 📜 Disclaimer

This scraper is intended for **educational and research purposes only**. Please ensure you comply with the [RERA Rajasthan](https://rera.rajasthan.gov.in/) website's terms of use before deploying or redistributing this data.
