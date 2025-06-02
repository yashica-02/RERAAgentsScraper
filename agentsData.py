from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver_path = 'chromedriver.exe'
url = "https://rera.rajasthan.gov.in/agents/"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get(url)
time.sleep(3)

agent_data = []
agent_count = 0
page_number = 1

def get_text(label):
    try:
        return driver.find_element(By.XPATH, "//td[text()='" + label + "']/following-sibling::td").text.strip()
    except:
        return ""

while True:
    print(f"\n📄 Scraping Page: {page_number}")
    time.sleep(2)
    rows = driver.find_elements(By.CSS_SELECTOR, 'table tr')[1:]

    for row in rows:
        try:
            cols = row.find_elements(By.TAG_NAME, 'td')
            district = cols[0].text.strip()
            name = cols[1].text.strip()
            app_no = cols[2].text.strip()
            reg_no = cols[3].text.strip()

            view_btn = cols[4].find_element(By.TAG_NAME, 'a')
            view_url = view_btn.get_attribute("href")

            # Open agent detail in new tab
            driver.execute_script("window.open(arguments[0]);", view_url)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)

            agent_count += 1
            print(f"   ➤ Scraping Agent #{agent_count}: {name} ({district})")

            agent_data.append({
                'District': district,
                'Agent Name': name,
                'Application No': app_no,
                'Registration No': reg_no,
                'First Name': get_text('First Name'),
                'Middle Name': get_text('Middle Name'),
                'Last Name': get_text('Last Name'),
                'Father Name': get_text('Father Name'),
                'Criminal Case': get_text('Any criminal or police case/ cases pending?'),
                'Registered in Other State': get_text('Do you have any registration in other state than Rajasthan?'),
                'Ever Convicted': get_text('Have you ever been convicted in any criminal case?'),
                'State': get_text('State'),
                'Address District': get_text('District'),
                'Tehsil': get_text('Tehsil'),
                'City/Town': get_text('Village/ Town/ City'),
                'Pin Code': get_text('Pin Code'),
                'Email': get_text('Email'),
                'Mobile': get_text('Mobile Number')
            })

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"   ❌ Error scraping agent on page {page_number}: {e}")
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            continue

    # Go to next page
    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class,'paginate_button next')]")
        if 'disabled' in next_button.get_attribute("class"):
            print("\n✅ All pages scraped.")
            break
        else:
            page_number += 1
            next_button.click()
            time.sleep(2)
    except Exception as e:
        print("❌ Could not find or click next button:", e)
        break

# Save to Excel
df = pd.DataFrame(agent_data)
df.to_excel("rera_all_agents_with_progress.xlsx", index=False)
print(f"\n🎉 Done! {agent_count} agents scraped and saved to 'rera_all_agents_with_progress.xlsx'")

driver.quit()