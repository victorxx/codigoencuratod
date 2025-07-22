import time
from playwright.sync_api import sync_playwright

urls = [
    "https://4br.me/r3F19LoX",

]

def run():
    with sync_playwright() as p:
        index = 0
        while True:
            url = urls[index % len(urls)]  # pega um link por vez, em ordem circular
            print(f"Abrindo {url}")
            
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_load_state('networkidle', timeout=60000)
            
            print("Esperando 3 minutos na página para parecer natural...")
            time.sleep(3 * 60)  # 3 minutos
            
            browser.close()
            print("Fechado navegador.")

            index += 1
            print("Esperando 24 horas para próxima visita...")
            time.sleep(24 * 60 * 60)  # espera 24 horas

if __name__ == "__main__":
    run()
