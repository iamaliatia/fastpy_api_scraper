import asyncio
from fastpy_scraper.core import FastScraper
from fastpy_scraper.parsers import save_to_csv

async def test_scraper():
    # ليستة د البروكسيات للتجربة (اختيارية)
    custom_proxies = [] 
    
    scraper = FastScraper(proxies=custom_proxies)
    print("🕵️‍♂️ جاري كشط موقع Hacker News بالـ Async...")
    
    # كشط عناوين الأخبار
    response = await scraper.scrape_to_json("https://news.ycombinator.com/", ".titleline > a")
    
    if response["status"] == "success":
        print(f"✅ لقيت {response['count']} عنوان!")
        # حفظ ف ملف CSV ديريكت
        save_to_csv(response["results"], "hacker_news.csv")
    else:
        print(f"❌ مشكل: {response['message']}")

asyncio.run(test_scraper())
