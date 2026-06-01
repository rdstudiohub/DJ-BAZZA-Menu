#!/usr/bin/env python3
"""Generate DJ BAZZA mobile-first online menu with item images."""
import os

OUTPUT = "/opt/data/dj-bazza-menu/index.html"

R = {
    "name_ar": "دي جي بازا", "name_en": "DJ BAZZA",
    "phone": "0534772776", "phone_display": "053 477 2776",
    "map_url": "https://maps.app.goo.gl/BPdRUu7r3iRbvCDc9",
    "location": "جدة، المملكة العربية السعودية",
    "wa_url": "https://wa.me/966534772776",
}

# Category-specific thumbnail images (reused for all items in that category)
CAT_IMAGES = {
    "mutbaq": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=150&h=150&fit=crop&q=80",
    "sides": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=150&h=150&fit=crop&q=80",
    "masoub": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=150&h=150&fit=crop&q=80",
    "shawarma": "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=150&h=150&fit=crop&q=80",
    "extras": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?w=150&h=150&fit=crop&q=80",
    "juices": "https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=150&h=150&fit=crop&q=80",
    "softdrinks": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=150&h=150&fit=crop&q=80",
    "hotdrinks": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=150&h=150&fit=crop&q=80",
}

CATEGORIES = [
    {
        "id": "mutbaq", "title_ar": "المطبق", "title_en": "ALMUTBIQ",
        "banner": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Meat Mutbaq", "مطبق لحم", 9), ("Chicken Mutbaq", "مطبق دجاج", 10),
            ("Vegetable Mutbaq", "مطبق خضار", 6), ("Mozzarella Mutbaq", "مطبق جبن موزاريلا", 8),
            ("Burger Mutbaq", "مطبق برجر", 7), ("Banana Mutbaq", "مطبق موز", 7),
            ("Cream Mutbaq", "مطبق قشطة", 7), ("Cheddar Cheese Mutbaq", "مطبق جبن شيدر", 7),
            ("Liquid Cheese Mutbaq", "مطبق جبن سائل", 8), ("Halloumi Cheese Mutbaq", "مطبق جبن حلومي", 11),
            ("Double Vegetable Mutbaq", "مطبق خضار دبل", 11), ("Double Cheese Mutbaq", "مطبق جبن دبل", 13),
            ("Double Meat Mutbaq", "مطبق لحم دبل", 16),
        ],
    },
    {
        "id": "sides", "title_ar": "أطباق جانبية", "title_en": "SIDE DISHES",
        "banner": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Cheese Fries", "بطاطس جبن", 9), ("Chicken Cheese Fries", "بطاطس دجاج وجبن", 15),
            ("Cheddar & Cheese", "شيدر اند جبن", 2), ("Regular Garlic", "ثوم عادي", 2),
            ("Spicy Garlic", "ثوم حار", 2), ("Hummus", "حمص", 2),
            ("Tahini", "طحينة", 2), ("Mayonnaise", "مايونيز", 2),
            ("Cheese Sauce", "جبن", 2), ("Plain Fries", "بطاطس عادي", 7),
            ("Cheese Burger", "برجر جبن", 11), ("Regular Burger", "برجر عادي", 10),
            ("Cheese Fattah", "فتة جبن", 8), ("Hot Fattah", "فتة حنيش", 12),
        ],
    },
    {
        "id": "masoub", "title_ar": "معصوب", "title_en": "MASOUB",
        "banner": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Honey Masoub", "معصوب عسل", 8), ("Cheese Masoub", "معصوب جبن", 13),
            ("Honey Cream Masoub", "معصوب قشطة عسل", 12), ("Honey Banana Masoub", "معصوب موز عسل", 15),
            ("Royal Masoub", "معصوب ملكي", 15), ("Royal Mixed Masoub", "معصوب ملكي مشكلة", 15),
            ("Royal Cream Masoub", "معصوب ملكي قشطة", 18), ("Mixed Cream Masoub", "معصوب قشطة مشكلة", 18),
            ("Plain Cream Masoub", "معصوب قشطة عادي", 6), ("Royal Fattah", "فتة ملكي", 10),
        ],
    },
    {
        "id": "shawarma", "title_ar": "شاورما", "title_en": "SHAWARMA",
        "banner": "https://images.unsplash.com/photo-1561651823-34feb02250e4?w=800&q=85&auto=format",
        "type": "sizes",
        "items": [
            ("Chicken Shawarma", "شاورما دجاج", [("Small", 7), ("Large", 12)]),
            ("Arabic Chicken Shawarma", "شاورما عربي دجاج", [("Small", 15), ("Large", 17)]),
            ("Chicken Shawarma Plate", "صحن شاورما دجاج", [("Regular", 21)]),
            ("Arabic Shawarma Plate", "صحن شاورما عربي دجاج", [("Large", 26)]),
            ("Crispy Shawarma", "شاورما كرسبي", [("Regular", 10)]),
        ],
    },
    {
        "id": "extras", "title_ar": "إضافات", "title_en": "EXTRAS",
        "banner": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Fasolia", "فاصوليا", 8), ("Falafel Sandwich", "ساندوتش فلافل", 4),
            ("Liver Sandwich", "ساندوتش كبدة", 5), ("3 Pieces Falafel", "فلافل 3 حبات", 1),
            ("Cheese Sambusa", "سمبوسة جبن", 1), ("Meat Sambusa", "سمبوسة لحم", 1),
            ("Chicken Sambusa", "سمبوسة دجاج", 1), ("Vegetable Sambusa", "سمبوسة خضار", 1),
        ],
    },
    {
        "id": "juices", "title_ar": "العصائر الطازجة", "title_en": "FRESH JUICES",
        "banner": "https://images.unsplash.com/photo-1553531384-cc64ac80f931?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Fresh Orange Juice", "برتقال فريش", 10), ("Fresh Cocktail Juice", "كوكتيل فريش", 12),
            ("Fresh Mango Juice", "مانجو فريش", 12), ("Banana Milk Juice", "موز حليب", 12),
            ("Fresh Pomegranate Juice", "رمان", 12),
        ],
    },
    {
        "id": "softdrinks", "title_ar": "المشروبات الغازية", "title_en": "SOFT DRINKS",
        "banner": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Pepsi", "بيبسي", 3), ("Diet Pepsi", "بيبسي دايت", 3),
            ("7UP", "سفن أب", 3), ("Mirinda", "ميرندا", 3),
            ("Spring Juice", "عصير ربيع", "2.5"),
        ],
    },
    {
        "id": "hotdrinks", "title_ar": "المشروبات الساخنة", "title_en": "HOT DRINKS",
        "banner": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=800&q=85&auto=format",
        "type": "single",
        "items": [
            ("Tea", "شاي", 2), ("Adani Tea", "شاي عدني", 2),
            ("Nescafe", "نسكافيه", 3), ("Black Tea", "شاي سادة", 1),
            ("Karak Tea", "كرك", 3),
        ],
    },
]


def esc(s):
    return str(s).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


DIRECT_URL = "https://rdstudiohub.github.io/DJ-BAZZA-Menu/"
SITE_TITLE = f"{R['name_ar']} | {R['name_en']} - القائمة"

# ─── BUILD CSS ───
CSS = f'''*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth;scroll-padding-top:62px}}
body{{font-family:'Tajawal','Poppins',sans-serif;background:#0D3B0E;color:#333;min-height:100vh;overflow-x:hidden;direction:rtl;padding:0;margin:0}}
img{{max-width:100%;height:auto;display:block}}

/* HEADER */
.header{{background:linear-gradient(135deg,#0D3B0E 0%,#1B5E20 50%,#2E7D32 100%);color:#fff;text-align:center;padding:24px 14px 18px;position:relative}}
.header .logo-ar{{font-size:38px;font-weight:900;line-height:1.2}}
.header .logo-en{{font-family:'Poppins',sans-serif;font-size:14px;font-weight:300;letter-spacing:5px;text-transform:uppercase;opacity:.85}}
.header .hd{{width:40px;height:3px;background:#FF6D00;margin:8px auto;border-radius:2px}}
.header .h-actions{{display:flex;gap:6px;justify-content:center;margin-top:12px;flex-wrap:wrap}}
.header .h-actions a{{display:flex;align-items:center;gap:5px;padding:7px 14px;border-radius:25px;font-size:12px;font-weight:500;text-decoration:none;font-family:'Tajawal',sans-serif}}
.btn-wa{{background:#25D366;color:#fff}}
.btn-call{{background:#fff;color:#1B5E20}}
.btn-map{{background:#FF6D00;color:#fff}}

/* STICKY NAV */
.cat-nav{{position:sticky;top:0;z-index:100;background:#0D3B0E;padding:6px 6px;overflow-x:auto;display:flex;gap:5px;white-space:nowrap;-webkit-overflow-scrolling:touch;scrollbar-width:none;border-bottom:3px solid #FF6D00}}
.cat-nav::-webkit-scrollbar{{display:none}}
.cat-tab{{flex-shrink:0;padding:6px 10px;border:none;border-radius:18px;font-family:'Tajawal',sans-serif;font-size:12px;font-weight:500;background:rgba(255,255,255,.1);color:rgba(255,255,255,.7);cursor:pointer;transition:.2s;display:flex;flex-direction:column;align-items:center;gap:1px;line-height:1.2;touch-action:manipulation}}
.cat-tab .tab-en{{font-family:'Poppins',sans-serif;font-size:8px;font-weight:400;text-transform:uppercase;letter-spacing:.5px;opacity:.7}}
.cat-tab.active,.cat-tab:active{{background:#FF6D00;color:#fff;box-shadow:0 2px 10px rgba(255,109,0,.3)}}
.cat-tab.active .tab-en{{opacity:1}}

/* SEARCH */
.search-bar{{margin:8px 10px 2px}}
.search-bar input{{width:100%;padding:10px 14px;border:2px solid #C8E6C9;border-radius:25px;font-family:'Tajawal',sans-serif;font-size:14px;background:#fff;outline:none;transition:.2s;direction:rtl}}
.search-bar input:focus{{border-color:#FF6D00;box-shadow:0 0 0 3px rgba(255,109,0,.1)}}

/* CATEGORY SECTION */
.cat-section{{margin:8px 8px;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.08)}}
.cat-banner{{position:relative;height:160px;overflow:hidden}}
.cat-banner img{{width:100%;height:100%;object-fit:cover}}
.cat-banner-overlay{{position:absolute;inset:0;background:linear-gradient(135deg,rgba(13,59,14,.65) 0%,rgba(255,109,0,.25) 100%);z-index:1}}
.cat-banner-text{{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff;padding:10px}}
.cat-banner-ar{{font-size:26px;font-weight:800;text-shadow:0 2px 8px rgba(0,0,0,.3)}}
.cat-banner-en{{font-family:'Poppins',sans-serif;font-size:12px;font-weight:400;letter-spacing:2px;text-transform:uppercase;opacity:.9}}

/* ITEMS */
.cat-items{{padding:6px 10px 8px}}
.menu-item{{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px dashed #E8F5E9}}
.menu-item:last-child{{border-bottom:none}}
.item-thumb{{width:70px;height:70px;border-radius:12px;object-fit:cover;flex-shrink:0;border:2px solid #E8F5E9}}
.item-info{{flex:1;min-width:0}}
.item-name-en{{font-family:'Poppins',sans-serif;font-size:13px;font-weight:500;color:#333;display:block;direction:ltr;text-align:left}}
.item-name-ar{{font-family:'Tajawal',sans-serif;font-size:14px;font-weight:500;color:#555;display:block;margin-top:1px}}
.item-price-tag{{font-family:'Poppins',sans-serif;font-size:14px;font-weight:700;color:#1B5E20;white-space:nowrap;background:#E8F5E9;padding:4px 10px;border-radius:8px;flex-shrink:0}}
.item-prices{{display:flex;gap:3px;flex-wrap:wrap;flex-shrink:0}}
.size-tag{{font-family:'Poppins',sans-serif;font-size:10px;font-weight:600;color:#1B5E20;background:#E8F5E9;padding:3px 7px;border-radius:6px;white-space:nowrap}}

/* FOOTER */
.footer{{background:linear-gradient(135deg,#0D3B0E,#1B5E20);color:#fff;text-align:center;padding:24px 14px;margin:8px;border-radius:12px}}
.footer .fl{{font-size:22px;font-weight:800}}
.footer .fle{{font-family:'Poppins',sans-serif;font-size:11px;font-weight:300;letter-spacing:3px;text-transform:uppercase;opacity:.7}}
.footer .fd{{width:30px;height:2px;background:#FF6D00;margin:8px auto;border-radius:2px}}
.footer .fa{{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin-top:10px}}
.footer .fa a{{display:flex;align-items:center;gap:5px;padding:8px 16px;border-radius:25px;font-size:12px;font-weight:500;text-decoration:none;font-family:'Tajawal',sans-serif}}
.footer .floc{{font-size:11px;opacity:.6;margin-top:10px}}
.footer .floc a{{color:#FFC107;text-decoration:none}}
.footer-qr{{margin-top:12px}}
.footer-qr img{{width:110px;height:110px;border-radius:8px;border:3px solid rgba(255,255,255,.15);margin:0 auto}}
.no-results{{display:none;text-align:center;padding:30px;color:#999;font-size:15px}}
@media(min-width:768px){{.menu-page{{max-width:480px;margin:0 auto}}}}
@media print{{body{{background:#fff}} .cat-nav,.search-bar,.footer-qr,.header .h-actions{{display:none}}}}'''

# ─── BUILD NAV TABS ───
nav_tabs = []
for i, cat in enumerate(CATEGORIES):
    active = ' active' if i == 0 else ''
    nav_tabs.append(
        f'<button class="cat-tab{active}" data-target="{cat["id"]}">'
        f'<span class="tab-ar">{cat["title_ar"]}</span>'
        f'<span class="tab-en">{cat["title_en"]}</span></button>'
    )

# ─── BUILD SECTIONS ───
sections = []
for cat in CATEGORIES:
    thumb = CAT_IMAGES.get(cat["id"], "")
    items_rows = []
    
    if cat["type"] == "sizes":
        for en, ar, sizes in cat["items"]:
            size_html = " ".join(f'<span class="size-tag">{s}: {p} SAR</span>' for s, p in sizes)
            items_rows.append(
                f'<div class="menu-item">'
                f'<img class="item-thumb" src="{thumb}" alt="{esc(en)}" loading="lazy">'
                f'<div class="item-info"><span class="item-name-en">{esc(en)}</span><span class="item-name-ar">{esc(ar)}</span></div>'
                f'<div class="item-prices">{size_html}</div></div>'
            )
    else:
        for en, ar, price in cat["items"]:
            items_rows.append(
                f'<div class="menu-item">'
                f'<img class="item-thumb" src="{thumb}" alt="{esc(en)}" loading="lazy">'
                f'<div class="item-info"><span class="item-name-en">{esc(en)}</span><span class="item-name-ar">{esc(ar)}</span></div>'
                f'<div class="item-price-tag">{esc(price)} SAR</div></div>'
            )
    
    sections.append(f'''<section id="{cat["id"]}" class="cat-section">
<div class="cat-banner"><img src="{cat["banner"]}" alt="{cat["title_en"]}" loading="lazy">
<div class="cat-banner-overlay"></div><div class="cat-banner-text"><span class="cat-banner-ar">{cat["title_ar"]}</span><span class="cat-banner-en">{cat["title_en"]}</span></div></div>
<div class="cat-items">{"".join(items_rows)}</div></section>''')

# ─── SVG ICONS (minified) ───
WA_SVG = '<svg viewBox="0 0 24 24" width="16" height="16"><path fill="#fff" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'
CALL_SVG = '<svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'
MAP_SVG = '<svg viewBox="0 0 24 24" width="16" height="16"><path fill="#fff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>'

# ─── ASSEMBLE HTML ───
HTML = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>{SITE_TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="menu-page">

<div class="header">
  <div class="logo-ar">{R["name_ar"]}</div>
  <div class="logo-en">{R["name_en"]}</div>
  <div class="hd"></div>
  <div class="h-actions">
    <a href="{R["wa_url"]}" target="_blank" class="btn-wa">{WA_SVG} واتساب</a>
    <a href="tel:{R["phone"]}" class="btn-call">{CALL_SVG} اتصال</a>
    <a href="{R["map_url"]}" target="_blank" class="btn-map">{MAP_SVG} الموقع</a>
  </div>
</div>

<div class="search-bar"><input type="text" id="searchInput" placeholder="🔍 ابحث في القائمة..." oninput="filterMenu(this.value)"></div>

<nav class="cat-nav" id="catNav">
{" ".join(nav_tabs)}
</nav>

<div class="no-results" id="noResults">😕 لا توجد نتائج<br><span style="font-size:13px;color:#bbb">No items found</span></div>

{"".join(sections)}

<div class="footer">
  <div class="fl">{R["name_ar"]}</div>
  <div class="fle">{R["name_en"]}</div>
  <div class="fd"></div>
  <div class="fa">
    <a href="{R["wa_url"]}" target="_blank" class="btn-wa">{WA_SVG} واتساب</a>
    <a href="tel:{R["phone"]}" class="btn-call" style="background:#fff;color:#1B5E20;">{CALL_SVG} اتصال</a>
    <a href="{R["map_url"]}" target="_blank" class="btn-map">{MAP_SVG} الموقع</a>
  </div>
  <div class="footer-qr"><img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={DIRECT_URL}&margin=10" alt="QR"></div>
  <div class="floc"><a href="{R["map_url"]}" target="_blank">📍 {R["location"]}</a></div>
</div>

</div>

<script>
// ─── TAB CLICK ───
(function(){{
var tabs=document.querySelectorAll('.cat-tab');
var sections=document.querySelectorAll('.cat-section');
var nav=document.querySelector('.cat-nav');
var scrolling=false;

tabs.forEach(function(tab){{
tab.addEventListener('click',function(e){{
var id=this.getAttribute('data-target');
if(!id)return;
scrolling=true;
tabs.forEach(function(t){{t.classList.remove('active')}});
this.classList.add('active');
var target=document.getElementById(id);
if(target){{
var navH=nav.offsetHeight;
var top=target.getBoundingClientRect().top+window.pageYOffset-navH-10;
window.scrollTo({{top:top,behavior:'smooth'}});
setTimeout(function(){{scrolling=false;}},600);
}}
}});
}});

// ─── SCROLL SPY ───
var observer=new IntersectionObserver(function(entries){{
if(scrolling)return;
entries.forEach(function(entry){{
if(entry.isIntersecting){{
tabs.forEach(function(t){{t.classList.remove('active')}});
var activeTab=document.querySelector('.cat-tab[data-target="'+entry.target.id+'"]');
if(activeTab){{activeTab.classList.add('active');
activeTab.scrollIntoView({{behavior:'smooth',inline:'center',block:'nearest'}});}}
}}
}});
}},{{rootMargin:'-62px 0px -50% 0px',threshold:0}});
sections.forEach(function(s){{observer.observe(s)}});
}})();

// ─── SEARCH ───
function filterMenu(query){{
var q=query.toLowerCase().trim();
var items=document.querySelectorAll('.menu-item');
var sections_els=document.querySelectorAll('.cat-section');
var anyVisible=false;
items.forEach(function(item){{
var text=item.textContent.toLowerCase();
var match=!q||text.includes(q);
item.style.display=match?'':'none';
if(match)anyVisible=true;
}});
sections_els.forEach(function(section){{
var vis=section.querySelectorAll('.menu-item:not([style*=\"display: none\"])').length;
section.style.display=(!q||vis>0)?'':'none';
}});
document.getElementById('noResults').style.display=anyVisible||!q?'none':'block';
}}
</script>
</body>
</html>'''

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"✅ DJ BAZZA menu generated: {OUTPUT}")
print(f"   Size: {len(HTML):,} bytes")
print(f"   Items: {sum(len(c['items']) for c in CATEGORIES)}")
item_count_html = HTML.count('class="menu-item"')
print(f"   HTML item elements: {item_count_html}")
