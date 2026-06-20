import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import os

MAPS_URL = "https://www.google.com/maps/@51.8605018,-5.0382708,12z/data=!5m2!1e1!1e4"
SAVE_FOLDER = "/workspaces/newgale-traffic-codespaces/screenshots"

os.makedirs(SAVE_FOLDER, exist_ok=True)

async def take_screenshot(page):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{SAVE_FOLDER}/newgale_traffic_{timestamp}.png"
    await page.screenshot(path=filename)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Screenshot saved: {filename}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        await page.goto(MAPS_URL, wait_until="networkidle")
        await asyncio.sleep(8)

        print("🚀 Starting traffic monitoring every 5 minutes...\n")

        try:
            while True:
                await take_screenshot(page)
                await asyncio.sleep(300)  # 5 minutes
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
        finally:
            await browser.close()

asyncio.run(main())