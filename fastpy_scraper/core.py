import httpx
import random
from bs4 import BeautifulSoup
from typing import Dict, Any, List

class FastScraper:
    def __init__(self, proxies: List[str] = None):
        # لستة د الهويات باش المتصفح يبان حقيقي مع كل طلب
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        ]
        self.proxies = proxies or []

    def _get_headers(self) -> Dict[str, str]:
        """توليد هيدرز عشوائي ديريكت قبل الطلب"""
        return {
            "User-Agent": random.choice(self.user_agents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

    async def fetch_html(self, url: str) -> str:
        """جلب الـ HTML باستعمال البروكسي والهيدرز العشوائي"""
        headers = self._get_headers()
        proxy = random.choice(self.proxies) if self.proxies else None
        
        # إعداد البروكسي لـ httpx إذا كان متوفر
        mounts = {"all://": httpx.AsyncHTTPTransport(proxy=proxy)} if proxy else None

        async with httpx.AsyncClient(headers=headers, mounts=mounts, follow_redirects=True, timeout=10.0) as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.text
            raise Exception(f"❌ خطأ ف جلب الموقع [{response.status_code}]")

    async def scrape_to_json(self, url: str, selector: str) -> Dict[str, Any]:
        """استخراج البيانات وتحويلها لـ JSON واجد"""
        try:
            html = await self.fetch_html(url)
            soup = BeautifulSoup(html, 'html.parser')
            elements = soup.select(selector)
            data = [el.get_text(strip=True) for el in elements]
            
            return {"status": "success", "url": url, "count": len(data), "results": data}
        except Exception as e:
            return {"status": "error", "message": str(e)}
