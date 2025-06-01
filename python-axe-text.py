from selenium import webdriver
from selenium_axe_python import Axe

driver = webdriver.Chrome()

messy_lines_of_pages = []
with open('pages.txt') as my_file:
    messy_lines_of_pages = my_file.readlines()

pages_to_test = [s.strip() for s in messy_lines_of_pages]

print(pages_to_test)

for page in pages_to_test:
    driver.get(page)
    driver.maximize_window()
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()
    # Write results to jsfile
    axe.write_results(results, 'a11y.json')
    print("====================================================")
    print("PAGE: " + page)
    print("====================================================")
    for violation in results["violations"]:
        print(violation["help"])
        for node in violation['nodes']:
            print("   - For " + node["html"])
            print("     " + node["failureSummary"])
        print("")
    # Assert no violations are found
    #assert len(results["violations"]) == 0, axe.report(results["violations"])
    print("====================================================")
    print("")
    print("")
driver.close()