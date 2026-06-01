#!/usr/bin/env python3
"""Generate DJ BAZZA premium restaurant menu HTML."""
import os

OUTPUT = "/opt/data/dj-bazza-menu/index.html"

# ═══════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════
RESTAURANT = {
    "name_ar": "دي جي بازا",
    "name_en": "DJ BAZZA",
    "phone": "053 477 2776",
    "location_url": "https://maps.app.goo.gl/BPdRUu7r3iRbvCDc9",
    "location_text": "📍 جدة، المملكة العربية السعودية",
}

SECTIONS = [
    {
        "title_ar": "المطبق",
        "title_en": "ALMUTBIQ",
        "banner": "https://images.unsplash.com/photo-1606755456209-6b7a1a3e9c0a?w=1400&q=85&auto=format",
        "items": [
            ("Meat Mutbaq", "مطبق لحم"),
            ("Chicken Mutbaq", "مطبق دجاج"),
            ("Vegetable Mutbaq", "مطبق خضار"),
            ("Mozzarella Mutbaq", "مطبق جبن موزاريلا"),
            ("Burger Mutbaq", "مطبق برجر"),
            ("Banana Mutbaq", "مطبق موز"),
            ("Cream Mutbaq", "مطبق قشطة"),
            ("Cheddar Cheese Mutbaq", "مطبق جبن شيدر"),
            ("Liquid Cheese Mutbaq", "مطبق جبن سائل"),
            ("Halloumi Cheese Mutbaq", "مطبق جبن حلومي"),
            ("Vegetable Cheese Mutbaq", "مطبق خضار جبن"),
            ("Double Cheese Mutbaq", "مطبق جبن دبل"),
            ("Double Meat Mutbaq", "مطبق لحم دبل"),
        ],
        "price": "10 SAR",
        "price_label_ar": "الكل 10 ريال",
        "price_label_en": "All 10 SAR",
    },
    {
        "title_ar": "أطباق جانبية",
        "title_en": "SIDE DISHES",
        "banner": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=1400&q=85&auto=format",
        "items": [
            ("Cheese Fries", "بطاطس جبن"),
            ("Chicken Cheese Fries", "بطاطس دجاج وجبن"),
            ("Cheddar Cheese Fries", "شيدر اند جبن"),
            ("Regular Garlic Sauce", "ثوم عادي"),
            ("Spicy Garlic Sauce", "ثوم حار"),
            ("Hummus", "حمص"),
            ("Tahini", "طحينة"),
            ("Mayonnaise", "مايونيز"),
            ("Cheese Sauce", "جبن"),
            ("Plain Fries", "بطاطس عادي"),
            ("Cheese Burger", "برجر جبن"),
            ("Regular Burger", "برجر عادي"),
            ("Hot Feta Cheese", "فتة جبن"),
            ("Mixed Fries", "مشكلة بطاطس"),
        ],
        "price": "6 SAR",
        "price_label_ar": "6 ريال",
        "price_label_en": "6 SAR",
        "subsections": [
            {
                "title_ar": "مشكلات المعصوب",
                "title_en": "MASOUB & SPECIALS",
                "items": [
                    ("Honey Cream Masoub", "معصوب عسل"),
                    ("Honey Cheese Masoub", "معصوب جبن"),
                    ("Honey Cream Mix Masoub", "معصوب قشطة عسل"),
                    ("Honey Banana Masoub", "معصوب موز عسل"),
                    ("Royal Masoub", "معصوب ملكي"),
                    ("Royal Mixed Masoub", "معصوب ملكي مشكلة"),
                    ("Royal Cream Masoub", "معصوب ملكي قشطة"),
                    ("Plain Cream Masoub", "معصوب قشطة عادي"),
                    ("Royal Fattah", "فتة ملكي"),
                    ("Grape Juice", "زبيب عنب"),
                ],
                "price": "15 SAR",
                "price_label_ar": "15 ريال",
                "price_label_en": "15 SAR",
            }
        ],
    },
    {
        "title_ar": "شاورما",
        "title_en": "SHAWARMA",
        "banner": "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=1400&q=85&auto=format",
        "items": [
            ("Small Chicken Shawarma", "شاورما دجاج صغير"),
            ("Large Chicken Shawarma", "شاورما دجاج كبير"),
            ("Small Arabic Chicken Shawarma", "شاورما عربي دجاج صغير"),
            ("Large Arabic Chicken Shawarma", "شاورما عربي دجاج كبير"),
            ("Chicken Shawarma Plate", "صحن شاورما دجاج"),
            ("Arabic Chicken Shawarma Plate", "صحن شاورما عربي دجاج"),
            ("Shawarma Crispy", "شاورما كرسبي"),
        ],
        "price": "8 - 20 SAR",
        "price_label_ar": "صغير 8 • كبير 12 • صحن 20",
        "price_label_en": "Small 8 • Large 12 • Plate 20",
        "price_detail": [
            ("Small", "8 SAR"),
            ("Large", "12 SAR"),
            ("Plate", "20 SAR"),
        ],
        "extras": [
            {
                "title_ar": "إضافات",
                "title_en": "EXTRAS",
                "items": [
                    ("Fasolia", "فاصوليا"),
                    ("Falafel Sandwich", "ساندوتش فلافل"),
                    ("Liver Sandwich", "ساندوتش كبدة"),
                    ("3 Pieces Falafel", "فلافل 3 حبات"),
                    ("Cheese Sambusa", "سمبوسة جبن"),
                    ("Meat Sambusa", "سمبوسة لحم"),
                    ("Chicken Sambusa", "سمبوسة دجاج"),
                    ("Vegetable Sambusa", "سمبوسة خضار"),
                ],
                "price": "5 SAR",
                "price_label_ar": "5 ريال",
                "price_label_en": "5 SAR",
            },
        ],
    },
    {
        "title_ar": "المشروبات",
        "title_en": "DRINKS",
        "banner": "https://images.unsplash.com/photo-1544252910-5f7e8f5a7f5e?w=1400&q=85&auto=format",
        "subsections": [
            {
                "title_ar": "عصائر طازجة",
                "title_en": "FRESH JUICES",
                "items": [
                    ("Fresh Orange Juice", "برتقال فريش"),
                    ("Fresh Cocktail Juice", "كوكتيل فريش"),
                    ("Fresh Mango Juice", "مانجو فريش"),
                    ("Fresh Pomegranate Juice", "رمان"),
                    ("Banana Milk Juice", "موز حليب"),
                ],
                "price": "10 SAR",
                "price_label_ar": "10 ريال",
                "price_label_en": "10 SAR",
            },
            {
                "title_ar": "مشروبات غازية",
                "title_en": "SOFT DRINKS",
                "items": [
                    ("Pepsi", "بيبسي"),
                    ("Diet Pepsi", "بيبسي دايت"),
                    ("7UP", "سفن أب"),
                    ("Mirinda", "ميرندا"),
                    ("Spring Juice", "عصير ربيع"),
                ],
                "price": "3 SAR",
                "price_label_ar": "3 ريال",
                "price_label_en": "3 SAR",
            },
            {
                "title_ar": "مشروبات ساخنة",
                "title_en": "HOT DRINKS",
                "items": [
                    ("Tea", "شاي"),
                    ("Adani Tea", "شاي عدني"),
                    ("Nescafe", "نسكافيه"),
                    ("Black Tea", "شاي سادة"),
                    ("Karak Tea", "كرك"),
                ],
                "price": "5 SAR",
                "price_label_ar": "5 ريال",
                "price_label_en": "5 SAR",
            },
        ],
    },
]


# ═══════════════════════════════════════════════
# HTML GENERATION
# ═══════════════════════════════════════════════

def make_banner(section):
    return f'''  <div class="banner">
    <img src="{section['banner']}" alt="{section['title_en']}" loading="lazy">
    <div class="banner-overlay"></div>
    <div class="banner-title">
      <span class="ar">{section['title_ar']}</span>
      <span class="en">{section['title_en']}</span>
    </div>
  </div>'''


def make_items(items, price, price_label_ar, price_label_en, extras=None, price_detail=None):
    rows = []
    for en, ar in items:
        rows.append(f'''      <tr class="item-pair-en"><td class="item-en-name">{en}</td><td class="item-price-cell">{price}</td></tr>
      <tr class="item-pair-ar"><td class="item-ar-name">{ar}</td><td class="item-price-cell">{price}</td></tr>''')
    
    items_html = '\n'.join(rows)
    
    price_info = ""
    if price_detail:
        parts = " • ".join([f"{s}: {p}" for s, p in price_detail])
        price_info = f"""<div class="price-banner">
    <span style="font-family:'Tajawal',sans-serif;font-weight:600;color:#666;">{price_label_ar}</span>
    <span style="font-weight:700;color:#1B5E20;font-size:18px;">{parts}</span>
  </div>"""
    else:
        price_info = f"""<div class="price-banner">
    <span style="font-family:'Tajawal',sans-serif;font-weight:600;color:#666;">{price_label_ar}</span>
    <span style="font-weight:700;color:#1B5E20;font-size:18px;">{price}</span>
    <span style="color:#ddd;margin:0 10px;">|</span>
    <span style="font-family:'Montserrat',sans-serif;font-weight:600;color:#666;">{price_label_en}</span>
    <span style="font-weight:700;color:#1B5E20;font-size:18px;">{price}</span>
  </div>"""
    
    return items_html, price_info


def make_subsection(sub, is_last=False):
    items_rows = []
    for en, ar in sub["items"]:
        items_rows.append(f'''      <tr class="item-pair-en"><td class="item-en-name">{en}</td><td class="item-price-cell">{sub['price']}</td></tr>
      <tr class="item-pair-ar"><td class="item-ar-name">{ar}</td><td class="item-price-cell">{sub['price']}</td></tr>''')
    
    items_html = '\n'.join(items_rows)
    
    return f'''  <div class="category-divider">
    <h3>{sub['title_ar']} <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:500;color:#999;">{sub['title_en']}</span></h3>
  </div>
  <div class="menu-items">
    <table class="menu-table">
      <tr class="price-row-en"><th class="th-item">{sub['title_en']}</th><th class="th-price">{sub['price']}</th></tr>
      <tr class="price-row-ar"><th class="th-item">{sub['title_ar']}</th><th class="th-price">{sub['price_label_ar']}</th></tr>
{items_html}
    </table>
  </div>
  <div class="price-banner">
    <span style="font-family:'Tajawal',sans-serif;font-weight:600;color:#666;">{sub['price_label_ar']}</span>
    <span style="font-weight:700;color:#1B5E20;font-size:18px;">{sub['price']}</span>
    <span style="color:#ddd;margin:0 10px;">|</span>
    <span style="font-family:'Montserrat',sans-serif;font-weight:600;color:#666;">{sub['price_label_en']}</span>
    <span style="font-weight:700;color:#1B5E20;font-size:18px;">{sub['price']}</span>
  </div>'''


def make_section(section):
    parts = [make_banner(section)]
    
    parts.append(f'''  <div class="section-header">
    <h2><span class="en">{section['title_en']}</span> <span class="ar" style="color:#FF6D00;">{section['title_ar']}</span></h2>
  </div>''')
    
    # Handle sections with direct items
    if "items" in section:
        items_html, price_info = make_items(
            section["items"], 
            section["price"],
            section.get("price_label_ar", ""),
            section.get("price_label_en", ""),
            price_detail=section.get("price_detail")
        )
        
        parts.append(f'''  <div class="menu-items">
    <table class="menu-table">
      <tr class="price-row-en"><th class="th-item">{section['title_en']}</th><th class="th-price">{section.get('price_label_en', section['price'])}</th></tr>
      <tr class="price-row-ar"><th class="th-item">{section['title_ar']}</th><th class="th-price">{section.get('price_label_ar', section['price'])}</th></tr>
{items_html}
    </table>
  </div>''')
        
        # Price banner
        if section.get("price_detail"):
            parts_d = " • ".join([f"{s}: {p}" for s, p in section["price_detail"]])
            parts.append(f'''  <div class="price-banner">
    <span style="font-weight:700;color:#1B5E20;font-size:18px;">{parts_d}</span>
  </div>''')
        else:
            parts.append(f'''  <div class="price-banner">
    <span style="font-family:'Tajawal',sans-serif;font-weight:600;color:#666;">{section.get('price_label_ar', section['price'])}</span>
    <span style="font-weight:700;color:#1B5E20;font-size:20px;">{section['price']}</span>
  </div>''')
    
    # Subsections (for side dishes masoub, drink types, etc.)
    for sub in section.get("subsections", []):
        parts.append(make_subsection(sub))
    
    # Extras (like Shawarma extras)
    for extra in section.get("extras", []):
        parts.append(make_subsection(extra))
    
    return f'<div class="section-card">\n' + '\n'.join(parts) + '\n</div>'


# ═══════════════════════════════════════════════
# FULL HTML
# ═══════════════════════════════════════════════

HTML_TOP = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DJ BAZZA | دي جي بازا - Premium Restaurant Menu</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;600;700;800&family=Tajawal:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">
<style>
/* ─── RESET & BASE ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Poppins', 'Tajawal', sans-serif;
  background: #1B5E20;
  color: #2C2C2C;
  padding: 20px;
  margin: 0;
  min-height: 100vh;
}

/* ─── PAGE WRAPPER ─── */
.menu-page {
  max-width: 1200px;
  margin: 0 auto;
  background: #FFFFFF;
  box-shadow: 0 30px 80px rgba(0,0,0,0.3);
  position: relative;
  overflow: hidden;
  border-radius: 8px;
}

/* ─── TYPOGRAPHY ─── */
h1, h2, h3, h4 { font-family: 'Tajawal', 'Poppins', sans-serif; }
.ar { font-family: 'Tajawal', sans-serif; direction: rtl; }
.en { font-family: 'Poppins', sans-serif; }

/* ─── HEADER ─── */
.restaurant-header {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 60%, #388E3C 100%);
  color: #fff;
  text-align: center;
  padding: 40px 30px 30px;
  position: relative;
  overflow: hidden;
}
.restaurant-header::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,109,0,0.08) 0%, transparent 70%);
  pointer-events: none;
}
.restaurant-header .logo-ar {
  font-family: 'Tajawal', sans-serif;
  font-size: 64px;
  font-weight: 900;
  letter-spacing: 2px;
  text-shadow: 0 4px 20px rgba(0,0,0,0.2);
  line-height: 1;
}
.restaurant-header .logo-en {
  font-family: 'Poppins', sans-serif;
  font-size: 28px;
  font-weight: 300;
  letter-spacing: 8px;
  text-transform: uppercase;
  opacity: 0.9;
  margin-top: 4px;
}
.restaurant-header .header-divider {
  width: 60px;
  height: 3px;
  background: #FF6D00;
  margin: 14px auto;
  border-radius: 2px;
}
.restaurant-header .header-info {
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
  font-size: 15px;
  margin-top: 10px;
}
.restaurant-header .header-info span {
  display: flex;
  align-items: center;
  gap: 8px;
  opacity: 0.9;
  font-weight: 300;
}
.restaurant-header .header-info a {
  color: #FFC107;
  text-decoration: none;
  font-weight: 500;
}
.restaurant-header .header-info a:hover {
  text-decoration: underline;
}
.header-accent-line {
  height: 4px;
  background: linear-gradient(90deg, #FF6D00, #FF9800, #FFC107, #FF9800, #FF6D00);
}

/* ─── SECTION CARD ─── */
.section-card {
  margin: 16px 20px;
  background: #FFFFFF;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(27,94,32,0.06), 0 1px 4px rgba(0,0,0,0.04);
  border: 1px solid #F0F0F0;
}

/* ─── BANNER ─── */
.banner {
  position: relative;
  width: 100%;
  height: 300px;
  overflow: hidden;
}
.banner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.banner-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(27,94,32,0.6) 0%, rgba(255,109,0,0.25) 100%);
  z-index: 1;
}
.banner-title {
  position: absolute;
  z-index: 2;
  text-align: center;
  color: #fff;
  text-shadow: 0 4px 20px rgba(0,0,0,0.4);
  padding: 20px;
  width: 100%;
}
.banner-title .ar {
  font-size: 42px;
  font-weight: 900;
  display: block;
  margin-bottom: 4px;
}
.banner-title .en {
  font-size: 22px;
  font-weight: 400;
  letter-spacing: 3px;
  text-transform: uppercase;
  opacity: 0.95;
}

/* ─── SECTION HEADER ─── */
.section-header {
  padding: 20px 24px 8px;
  border-bottom: 2px solid #1B5E20;
  margin: 0 24px;
}
.section-header h2 {
  font-size: 24px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 16px;
  justify-content: space-between;
}
.section-header h2 .en {
  font-family: 'Poppins', sans-serif;
  color: #1B5E20;
  font-weight: 600;
  letter-spacing: 1px;
}

/* ─── TWO-LINE ITEMS ─── */
.menu-table {
  width: 100%;
  border-collapse: collapse;
}
.price-row-en th, .price-row-ar th {
  padding: 6px 6px;
  border-bottom: 1px solid #E8F5E9;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 1px;
  color: #999;
}
.price-row-en .th-item { text-align: left; width: 70%; }
.price-row-ar .th-item { text-align: right; width: 70%; direction: rtl; }
.price-row-en .th-price, .price-row-ar .th-price { text-align: center; width: 30%; }

.item-pair-en td {
  padding: 8px 6px 2px;
  border-bottom: none;
  vertical-align: bottom;
}
.item-pair-ar td {
  padding: 2px 6px 8px;
  border-bottom: 1px dashed #E8F5E9;
  vertical-align: top;
}
.item-pair-en .item-en-name {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #333;
  text-align: left;
}
.item-pair-ar .item-ar-name {
  font-family: 'Tajawal', sans-serif;
  font-size: 15px;
  font-weight: 500;
  color: #555;
  text-align: right;
  direction: rtl;
}
.item-pair-en .item-price-cell,
.item-pair-ar .item-price-cell {
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  font-weight: 600;
  color: #1B5E20;
  text-align: center;
}
.item-pair-ar .item-price-cell {
  font-family: 'Tajawal', sans-serif;
}

/* ─── CATEGORY DIVIDER (sub-sections) ─── */
.category-divider {
  background: #E8F5E9;
  padding: 10px 24px;
  margin: 0;
  border-top: 1px solid #C8E6C9;
}
.category-divider h3 {
  font-family: 'Tajawal', sans-serif;
  font-size: 20px;
  font-weight: 700;
  color: #1B5E20;
  display: flex;
  align-items: center;
  gap: 12px;
}
.category-divider h3::before {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #FF6D00);
}
.category-divider h3::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, #FF6D00, transparent);
}

/* ─── PRICE BANNER ─── */
.price-banner {
  background: linear-gradient(135deg, #E8F5E9 0%, #FFF3E0 100%);
  margin: 0 24px 16px;
  padding: 12px 20px;
  border-radius: 12px;
  display: flex;
  justify-content: center;
  gap: 12px;
  align-items: center;
  border: 1px solid rgba(27,94,32,0.08);
}

/* ─── FOOTER ─── */
.footer {
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #388E3C 100%);
  color: #fff;
  text-align: center;
  padding: 36px 28px;
  margin: 16px 20px;
  border-radius: 12px;
  position: relative;
  overflow: hidden;
}
.footer::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,109,0,0.1) 0%, transparent 60%);
  pointer-events: none;
}
.footer .footer-logo {
  font-family: 'Tajawal', sans-serif;
  font-size: 28px;
  font-weight: 900;
  margin-bottom: 4px;
}
.footer .footer-logo-en {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  font-weight: 300;
  letter-spacing: 4px;
  text-transform: uppercase;
  opacity: 0.7;
}
.footer .footer-divider {
  width: 40px;
  height: 2px;
  background: #FF6D00;
  margin: 12px auto;
  border-radius: 2px;
}
.footer .footer-contact {
  display: flex;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
  margin-top: 14px;
}
.footer .footer-contact a {
  color: #FFC107;
  text-decoration: none;
  font-weight: 500;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.footer .footer-location {
  font-size: 13px;
  opacity: 0.7;
  margin-top: 10px;
  font-weight: 300;
}
.footer .footer-location a {
  color: #FFC107;
  text-decoration: none;
}
.footer-qr {
  margin-top: 14px;
}
.footer-qr img {
  width: 120px;
  height: 120px;
  border-radius: 8px;
  border: 3px solid rgba(255,255,255,0.15);
}

/* ─── MENU ITEMS PADDING ─── */
.menu-items {
  padding: 8px 24px 4px;
}

/* ─── PRINT STYLES ─── */
@media print {
  body { background: white; padding: 0; }
  .menu-page {
    max-width: 100%;
    box-shadow: none;
    margin: 0;
    border-radius: 0;
  }
  .section-card {
    break-inside: avoid;
    box-shadow: none;
    border: 1px solid #eee;
    margin: 12px 10px;
  }
  .banner { height: 250px; }
  @page {
    size: A4 portrait;
    margin: 5mm;
  }
}

/* ─── RESPONSIVE ─── */
@media (max-width: 768px) {
  body { padding: 8px; }
  .menu-page { border-radius: 0; }
  .restaurant-header { padding: 24px 16px 20px; }
  .restaurant-header .logo-ar { font-size: 40px; }
  .restaurant-header .logo-en { font-size: 18px; letter-spacing: 4px; }
  .restaurant-header .header-info { gap: 12px; font-size: 13px; }
  .section-card { margin: 10px 6px; border-radius: 8px; }
  .banner { height: 200px; }
  .banner-title .ar { font-size: 28px; }
  .banner-title .en { font-size: 16px; }
  .section-header { padding: 14px 14px 6px; margin: 0 14px; }
  .section-header h2 { font-size: 18px; }
  .menu-items { padding: 6px 14px 2px; }
  .item-pair-en .item-en-name, .item-pair-ar .item-ar-name { font-size: 12px; }
  .item-pair-en .item-price-cell, .item-pair-ar .item-price-cell { font-size: 13px; }
  .price-banner { margin: 0 14px 10px; padding: 10px 14px; flex-wrap: wrap; }
  .footer { margin: 10px 6px; padding: 24px 14px; }
}
</style>
</head>
<body>

<div class="menu-page">

<!-- ════════════════ HEADER ════════════════ -->
<div class="restaurant-header">
  <div class="logo-ar">دي جي بازا</div>
  <div class="logo-en">DJ BAZZA</div>
  <div class="header-divider"></div>
  <div class="header-info">
    <span>📞 <a href="tel:0534772776">053 477 2776</a></span>
    <span>📍 <a href="https://maps.app.goo.gl/BPdRUu7r3iRbvCDc9" target="_blank">جدة، المملكة العربية السعودية</a></span>
    <span>🕐 Daily: 12:00 PM - 2:00 AM</span>
  </div>
</div>
<div class="header-accent-line"></div>

'''

HTML_BOTTOM = '''
<!-- ════════════════ FOOTER ════════════════ -->
<div class="footer">
  <div class="footer-logo">دي جي بازا</div>
  <div class="footer-logo-en">DJ BAZZA</div>
  <div class="footer-divider"></div>
  <div class="footer-contact">
    <a href="tel:0534772776">📞 053 477 2776</a>
    <a href="https://wa.me/966534772776" target="_blank">💬 WhatsApp</a>
    <a href="https://maps.app.goo.gl/BPdRUu7r3iRbvCDc9" target="_blank">📍 الموقع</a>
  </div>
  <div class="footer-qr">
    <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://maps.app.goo.gl/BPdRUu7r3iRbvCDc9&margin=10" alt="Location QR">
  </div>
  <div class="footer-location">
    <a href="https://maps.app.goo.gl/BPdRUu7r3iRbvCDc9" target="_blank">افتتاح الموقع على الخريطة →</a>
  </div>
</div>

</div>

</body>
</html>'''

# ═══════════════════════════════════════════════
# BUILD
# ═══════════════════════════════════════════════
sections_html = '\n\n'.join(make_section(s) for s in SECTIONS)

full_html = HTML_TOP + sections_html + HTML_BOTTOM

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"✅ Generated DJ BAZZA menu: {OUTPUT}")
print(f"   Size: {len(full_html):,} bytes")
print(f"   Lines: {full_html.count(chr(10))}")
