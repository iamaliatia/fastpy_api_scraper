import httpx
from bs4 import BeautifulSoup
from typing import Dict, Any

class FastScraper:
    def __init__(self, headers: Dict[str, str] = None):
        # هيدرز افتراضية باش نتفاداو الـ Block العادي د السيتات
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    async def fetch_html(self, url: str) -> str:
        """جلب الـ HTML د السيت بالزربة بـ Async Client"""
        async with httpx.AsyncClient(headers=self.headers, follow_redirects=True) as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.text
            raise Exception(f"❌ فشل جلب الموقع. كود الخطأ: {response.status_code}")

    async def scrape_to_json(self, url: str, selector: str) -> Dict[str, Any]:
        """جلب البيانات وتحويلها لـ JSON تلقائياً بناءً على الـ CSS Selector"""
        html = await self.fetch_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        elements = soup.select(selector)
        data = [el.get_text(strip=True) for el in elements]
        
        # إرجاع النتيجة كـ API واجدة
        return {
            "status": "success",
            "url": url,
            "count": len(data),
            "results": data
        }
