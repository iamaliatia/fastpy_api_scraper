import csv
from typing import List, Dict, Any

def save_to_csv(data: List[Any], filepath: str):
    """حفظ النتائج المستخرجة ف ملف CSV نقي"""
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Data"]) # العناوين د الأعمدة
        for index, item in enumerate(data, 1):
            writer.writerow([index, item])
    print(f"💾 تم حفظ البيانات بنجاح فـ: {filepath}")
