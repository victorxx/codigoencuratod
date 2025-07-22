import time
import random
from playwright.sync_api import sync_playwright

urls = [
    "https://example.com",
    "https://4br.me/FmnTOjH",
    "https://google.com"
]

def run_playwright_on_urls(url_list):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        for url in url_list:
            print(f"Abrindo {url}")
            page.goto(url, timeout=60000)
            page.wait_for_load_state('networkidle', timeout=60000)
            wait_time = random.randint(120, 300)  # espera entre 2 e 5 minutos
            print(f"Esperando {wait_time} segundos na página para parecer natural...")
            time.sleep(wait_time)
        print("Aguardando 15 segundos antes de fechar o navegador devagar...")
        time.sleep(15)
        browser.close()
        print("Navegador fechado.")

if __name__ == "__main__":
    while True:
        run_playwright_on_urls(urls)
        print("Esperando 24 horas para próxima rodada...")
        time.sleep(24 * 60 * 60)
