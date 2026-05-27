import asyncio
import json
from fastpy_scraper.core import FastScraper

# دالة باش نقراو الإعدادات
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

async def main():
    config = load_config()
    scraper = FastScraper()
    
    print(f"🚀 Starting the scraping process for: {config['target_url']}")
    
    data = await scraper.scrape(config['target_url'])
    
    if data:
        scraper.save_to_csv(data, config['output_file'])
        print(f"✅ Data saved successfully to {config['output_file']}")
    else:
        print("❌ Failed to retrieve data.")

if __name__ == "__main__":
    asyncio.run(main())
