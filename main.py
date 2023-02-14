import csv
from selenium import webdriver
import time

# default tempat menyimpan data hasil scarped
path_to_file = "reviews.csv"

# default jumlah dari scraped pages and menghitung page yang sudah di scarped
num_page = 20
count = 0

#running Chrome webdriver
driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")

#looping seberapa banyak page di scarpe
for x in range(num_page):
    time.sleep(2)

    # untuk trip trip advisor yang Attraction Review (Bahasa indonesia), biasanya untuk menentukan page dari comentar akan di tambahkan kode di http
    # untuk kodenya biasanya `-or-10`` <- ini tandanya website akan menampilkan komentar di page ke 2, misalkan untuk ke 3 adalah `-or-20` dan seterusnya
    if count == 0:
        Pagess = ""
    else:
        cnt = count*10
        Pagess = f"-or{cnt}"


    #url website yang ingin di scarped
    url = f"https://www.tripadvisor.co.id/Attraction_Review-g297723-d3367607-Reviews{Pagess}-Bukittinggi_Clock_Tower-Bukittinggi_West_Sumatra_Sumatra.html"

    
    # Import the webdriver
    driver.get(url)

    # Open the file to save the review
    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)

    # melakukan otomatis klick ke html dengan paramter class name (CSS selector) _T FKffI bmUTE
    driver.find_element_by_css_selector("._T.FKffI.bmUTE").click()

    # mendapatkan container riview
    container = driver.find_elements_by_css_selector('div._c[data-automation="reviewCard"]')
    for j in range(len(container)):
        
        # mengambil nama pereview 
        title = container[j].find_element_by_xpath(".//a[@class='BMQDV _F G- wSSLS SwZTJ FGwzt ukgoS']").text

        # mengambil riview
        review = container[j].find_element_by_css_selector(".biGQs._P.pZUbB.KxBGd .yCeTE").text.replace("\n", " ")

        # melakukan write dalam row csv
        csvWriter.writerow([title, review]) 
    
    # melakukan count page telah selesai di scarpe
    count += 1

# endl loop, web dirver close
driver.close()