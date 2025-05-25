from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def main():
    options = Options()
    options.add_argument("--headless")  # Rodar sem abrir janela
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    while True:
        driver.get("https://key-drop.com/pt/giveaways/list")

        # Clique no botão do sorteio atual
        try:
            btn_sorteio = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div[4]/div/div[2]/div[1]/div[2]/div/button")
            btn_sorteio.click()
        except Exception as e:
            print("Erro no clique do sorteio:", e)

        time.sleep(3)

        # Clique no botão Participar
        try:
            btn_participar = driver.find_element(By.XPATH, '//*[@id="main-view"]/div/div[2]/div/div[4]/div/div/div/div/div[5]/a')
            btn_participar.click()
        except Exception as e:
            print("Erro no clique participar:", e)

        time.sleep(180)  # Espera 3 minutos

        # Clique no botão Voltar
        try:
            btn_voltar = driver.find_element(By.XPATH, '//*[@id="main-view"]/div/div/div[3]/div/a')
            btn_voltar.click()
        except Exception as e:
            print("Erro no clique voltar:", e)

        time.sleep(3)

        # Atualiza a página
        driver.refresh()

if __name__ == "__main__":
    main()

