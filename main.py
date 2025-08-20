from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('http://playwright.dev')
        await asyncio.sleep(10)
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
