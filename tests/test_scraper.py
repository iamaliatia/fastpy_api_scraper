import pytest
from fastpy_scraper.core import FastScraper

@pytest.mark.asyncio
async def test_fetch_html():
    scraper = FastScraper()
    # غنجربو نكشطو سيت معروف باش نتاكدو بلي الـ engine خدام
    html = await scraper.fetch_html("https://www.google.com")
    assert html is not None
    assert "google" in html.lower()

@pytest.mark.asyncio
async def test_scrape_to_json():
    scraper = FastScraper()
    # تجربة استخراج عناوين من موقع
    result = await scraper.scrape_to_json("https://news.ycombinator.com/", "a")
    assert result["status"] == "success"
    assert "results" in result
