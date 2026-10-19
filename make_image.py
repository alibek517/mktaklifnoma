import asyncio
import os
from playwright.async_api import async_playwright

async def generate_poster_image():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = f"file:///{os.path.join(current_dir, 'poster.html').replace('\\', '/')}"
    output_path = os.path.join(current_dir, "taklifnoma_rasm.png")

    async with async_playwright() as p:
        # Launch browser with high device scale factor for crisp ultra-HD quality
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 850, 'height': 1200},
            device_scale_factor=2
        )
        page = await context.new_page()
        await page.goto(html_path, wait_until='networkidle')
        
        # Wait a moment for web fonts (Alex Brush, Playfair Display) to render completely
        await page.wait_for_timeout(2500)
        
        poster_elem = await page.query_selector('#poster')
        if poster_elem:
            await poster_elem.screenshot(path=output_path)
            print(f"SUCCESS: {output_path}")
        else:
            await page.screenshot(path=output_path, full_page=True)
            print(f"FULL PAGE SUCCESS: {output_path}")
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(generate_poster_image())
