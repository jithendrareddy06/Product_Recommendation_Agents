"""Generate backend/data/products.json with a large mock catalog and stable image URLs."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "products.json"

# picsum.photos with a per-product seed loads reliably (no broken Unsplash links).
def img(product_id: str) -> str:
    return f"https://picsum.photos/seed/shopeasy-{product_id}/400/300"


def p(
    pid: str,
    title: str,
    category: str,
    price: float,
    rating: float,
    description: str,
    specs: dict[str, str],
) -> dict:
    return {
        "id": pid,
        "title": title,
        "category": category,
        "price_inr": price,
        "rating": rating,
        "image_url": img(pid),
        "description": description,
        "specs": specs,
    }


def headphones() -> list[dict]:
    items = [
        ("hp-001", "SoundWave Lite Wireless Headphones", 1299, 4.1, "Budget wireless over-ear with balanced sound.", {"battery_life": "20 hours", "sound_quality": "Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.0"}),
        ("hp-002", "BassPro Studio 300", 2499, 4.4, "Deep bass tuning for long listening sessions.", {"battery_life": "30 hours", "sound_quality": "Very Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2"}),
        ("hp-003", "QuietAir ANC Pro", 3499, 4.6, "Active noise cancellation under ₹3500.", {"battery_life": "28 hours", "sound_quality": "Excellent", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.3"}),
        ("hp-004", "ZenPods Air TWS", 1999, 4.2, "True wireless earbuds with compact case.", {"battery_life": "24 hours with case", "sound_quality": "Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.1"}),
        ("hp-005", "AudioCraft HD 500", 3299, 4.5, "Wide soundstage for music lovers.", {"battery_life": "35 hours", "sound_quality": "Excellent", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2 + aptX"}),
        ("hp-006", "TravelMute ANC Fold", 4999, 4.7, "Foldable travel headphones with strong ANC.", {"battery_life": "40 hours", "sound_quality": "Excellent", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.3"}),
        ("hp-007", "GrooveBeat On-Ear Mini", 1599, 3.9, "Lightweight on-ear for commuting.", {"battery_life": "18 hours", "sound_quality": "Fair", "noise_cancellation": "None", "connectivity": "Bluetooth 5.0"}),
        ("hp-008", "CrystalSound Pro X", 2799, 4.3, "Clear vocals and detailed treble.", {"battery_life": "32 hours", "sound_quality": "Very Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2"}),
        ("hp-009", "SilentComm Office ANC", 4199, 4.5, "Office ANC with dual mics.", {"battery_life": "25 hours", "sound_quality": "Very Good", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.2"}),
        ("hp-010", "PulseBuds Sport", 2299, 4.0, "Sweat-resistant sport earbuds.", {"battery_life": "22 hours with case", "sound_quality": "Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.1"}),
        ("hp-011", "Harmony Wireless 450", 1899, 4.1, "All-round wireless under ₹2000.", {"battery_life": "26 hours", "sound_quality": "Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.0"}),
        ("hp-012", "NeoSound ANC Lite", 2999, 4.4, "Entry ANC with warm sound.", {"battery_life": "30 hours", "sound_quality": "Very Good", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.2"}),
        ("hp-013", "StudioPure Reference", 5999, 4.8, "Neutral tuning for creators.", {"battery_life": "45 hours", "sound_quality": "Excellent", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.3 + LDAC"}),
        ("hp-014", "KidsSafe Volume Limit", 1499, 4.0, "Volume-limited kids headphones.", {"battery_life": "15 hours", "sound_quality": "Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.0"}),
        ("hp-015", "CloudComfort Over-Ear", 3399, 4.3, "Plush pads for all-day wear.", {"battery_life": "38 hours", "sound_quality": "Very Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2"}),
        ("hp-016", "BudgetBeats Entry", 899, 3.7, "Ultra-affordable wireless on-ear.", {"battery_life": "12 hours", "sound_quality": "Fair", "noise_cancellation": "None", "connectivity": "Bluetooth 4.2"}),
        ("hp-017", "WaveLink Dual Device", 3699, 4.5, "Multipoint for laptop and phone.", {"battery_life": "33 hours", "sound_quality": "Very Good", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.3 multipoint"}),
        ("hp-018", "OpenAir Spatial", 4499, 4.6, "Spatial audio open-back style.", {"battery_life": "20 hours", "sound_quality": "Excellent", "noise_cancellation": "None", "connectivity": "Bluetooth 5.3"}),
        ("hp-019", "CallClear Pro Mic", 2199, 4.2, "Optimized for voice calls.", {"battery_life": "28 hours", "sound_quality": "Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.1"}),
        ("hp-020", "Midnight ANC 350", 3450, 4.5, "Sleek ANC with excellent sound.", {"battery_life": "31 hours", "sound_quality": "Excellent", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.2"}),
        ("hp-021", "ValueSound 3200", 3200, 4.3, "Strong value with vocal clarity.", {"battery_life": "29 hours", "sound_quality": "Very Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2"}),
        ("hp-022", "DeepQuiet ANC Max", 3799, 4.6, "Premium-feel ANC package.", {"battery_life": "36 hours", "sound_quality": "Excellent", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.3"}),
        ("hp-023", "Everyday Wireless 2800", 2800, 4.2, "Reliable daily driver multipoint.", {"battery_life": "27 hours", "sound_quality": "Very Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.2 multipoint"}),
        ("hp-024", "StudioFold Wireless", 3100, 4.4, "Foldable with detailed sound.", {"battery_life": "34 hours", "sound_quality": "Excellent", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2"}),
        ("hp-025", "ANC Essential 3400", 3400, 4.5, "Essential ANC balanced tuning.", {"battery_life": "30 hours", "sound_quality": "Very Good", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.2"}),
        ("hp-026", "RiverTone Bass Wireless", 2699, 4.1, "Extra bass for EDM fans.", {"battery_life": "25 hours", "sound_quality": "Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.1"}),
        ("hp-027", "FeatherLite AirPods Style", 1749, 4.0, "Ultra-light semi in-ear buds.", {"battery_life": "20 hours with case", "sound_quality": "Good", "noise_cancellation": "None", "connectivity": "Bluetooth 5.0"}),
        ("hp-028", "ProMonitor Studio Wired BT", 4599, 4.5, "Hybrid wired/wireless studio cans.", {"battery_life": "42 hours", "sound_quality": "Excellent", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.3 + 3.5mm"}),
        ("hp-029", "CityCommute ANC Slim", 3899, 4.4, "Slim profile for metro travel.", {"battery_life": "26 hours", "sound_quality": "Very Good", "noise_cancellation": "Active ANC", "connectivity": "Bluetooth 5.2"}),
        ("hp-030", "GamerPulse RGB Headset", 3499, 4.2, "Low-latency gaming headset.", {"battery_life": "22 hours", "sound_quality": "Very Good", "noise_cancellation": "Passive", "connectivity": "Bluetooth 5.2 + 2.4GHz dongle"}),
    ]
    return [p(i, t, "headphones", pr, r, d, s) for i, t, pr, r, d, s in items]


def laptops() -> list[dict]:
    items = [
        ("lp-001", "SwiftBook 14 Lite", 42999, 4.2, "14-inch student laptop.", {"processor": "Intel i3 12th Gen", "ram": "8 GB", "storage": "256 GB SSD", "battery_life": "10 hours"}),
        ("lp-002", "ProWork 15 Performance", 68999, 4.5, "Ryzen 7 productivity laptop.", {"processor": "AMD Ryzen 7", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "8 hours"}),
        ("lp-003", "UltraThin Air 13", 54999, 4.4, "Travel ultrabook.", {"processor": "Intel i5 13th Gen", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "12 hours"}),
        ("lp-004", "GameForge RTX 4060", 89999, 4.6, "Gaming laptop RTX 4060.", {"processor": "Intel i7 13th Gen", "ram": "16 GB", "storage": "1 TB SSD", "battery_life": "5 hours"}),
        ("lp-005", "BudgetMate 15", 35999, 3.9, "Affordable 15-inch office laptop.", {"processor": "Intel i3 11th Gen", "ram": "8 GB", "storage": "512 GB SSD", "battery_life": "7 hours"}),
        ("lp-006", "CreatorStudio Pro", 94999, 4.7, "Color-accurate creator laptop.", {"processor": "Intel i7 H-series", "ram": "32 GB", "storage": "1 TB SSD", "battery_life": "9 hours"}),
        ("lp-007", "FlexConvert 2-in-1", 57999, 4.3, "Touch convertible with stylus.", {"processor": "Intel i5 12th Gen", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "9 hours"}),
        ("lp-008", "CloudLite Chrome 14", 24999, 4.0, "Web-first cloud laptop.", {"processor": "MediaTek Kompanio", "ram": "8 GB", "storage": "128 GB eMMC", "battery_life": "11 hours"}),
        ("lp-009", "ThinkPad Style Business 14", 72999, 4.5, "Business durability and keyboard.", {"processor": "Intel i5 vPro", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "11 hours"}),
        ("lp-010", "StudentMax 15 AMD", 48999, 4.3, "Value Ryzen 5 for college.", {"processor": "AMD Ryzen 5", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "8 hours"}),
        ("lp-011", "LegionStrike RTX 4050", 79999, 4.4, "144Hz gaming on a budget.", {"processor": "AMD Ryzen 7", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "5 hours"}),
        ("lp-012", "MacBook Air Style Slim", 99999, 4.6, "Premium thin metal chassis.", {"processor": "Apple-class ARM tier", "ram": "16 GB", "storage": "512 GB SSD", "battery_life": "15 hours"}),
    ]
    return [p(i, t, "laptop", pr, r, d, s) for i, t, pr, r, d, s in items]


def smartwatches() -> list[dict]:
    items = [
        ("sp-001", "FitTrack Band 5", 2999, 4.1, "Fitness band heart rate and sleep.", {"battery_life": "7 days", "display": "AMOLED", "water_resistance": "5 ATM", "gps": "Connected GPS"}),
        ("sp-002", "PulseWatch Active", 4999, 4.4, "GPS smartwatch for workouts.", {"battery_life": "5 days", "display": "AMOLED", "water_resistance": "5 ATM", "gps": "Built-in GPS"}),
        ("sp-003", "ClassicTime Analog Smart", 7999, 4.2, "Hybrid analog dial smartwatch.", {"battery_life": "14 days", "display": "Hybrid", "water_resistance": "3 ATM", "gps": "None"}),
        ("sp-004", "EnduroRun GPS Pro", 6499, 4.5, "Marathon training watch.", {"battery_life": "10 days", "display": "MIP", "water_resistance": "5 ATM", "gps": "Dual-band GPS"}),
        ("sp-005", "StyleRound AMOLED", 8999, 4.3, "Fashion round watch with NFC.", {"battery_life": "4 days", "display": "AMOLED", "water_resistance": "3 ATM", "gps": "Built-in GPS"}),
        ("sp-006", "BudgetTick Lite", 1999, 3.8, "Basic notifications band.", {"battery_life": "5 days", "display": "LCD", "water_resistance": "IP68", "gps": "None"}),
        ("sp-007", "HealthSense BP Edition", 11999, 4.4, "Health sensors including SpO2.", {"battery_life": "6 days", "display": "AMOLED", "water_resistance": "5 ATM", "gps": "Connected GPS"}),
        ("sp-008", "KidsGuard Watch", 3499, 4.0, "Kids GPS safety watch.", {"battery_life": "2 days", "display": "LCD", "water_resistance": "IP67", "gps": "Built-in GPS"}),
        ("sp-009", "UltraSport Titanium", 14999, 4.6, "Premium triathlon watch.", {"battery_life": "14 days", "display": "AMOLED", "water_resistance": "10 ATM", "gps": "Multi-band GPS"}),
        ("sp-010", "CallWatch LTE", 10999, 4.3, "LTE calling on wrist.", {"battery_life": "2 days", "display": "AMOLED", "water_resistance": "5 ATM", "gps": "Built-in GPS"}),
        ("sp-011", "ZenFit Square", 4499, 4.2, "Square fitness watch popular style.", {"battery_life": "6 days", "display": "AMOLED", "water_resistance": "5 ATM", "gps": "Connected GPS"}),
        ("sp-012", "RoyalChrono Smart", 12999, 4.5, "Luxury design smart chronograph.", {"battery_life": "7 days", "display": "Hybrid", "water_resistance": "5 ATM", "gps": "None"}),
    ]
    return [p(i, t, "smartwatch", pr, r, d, s) for i, t, pr, r, d, s in items]


def smartphones() -> list[dict]:
    brands = [
        ("Nova", "X1", 8999, 3.9), ("Nova", "X5", 12999, 4.1), ("SkyMobile", "A14", 14999, 4.0),
        ("SkyMobile", "A56", 18999, 4.2), ("PixelGo", "12a", 24999, 4.3), ("PixelGo", "12 Pro", 54999, 4.6),
        ("RedLine", "Note 13", 16999, 4.2), ("RedLine", "Note 13 Pro", 22999, 4.4), ("OneUltra", "11", 44999, 4.5),
        ("OneUltra", "11R", 39999, 4.4), ("SamWave", "Galaxy M34", 19999, 4.1), ("SamWave", "Galaxy S24", 74999, 4.7),
        ("iFruit", "SE 64GB", 42999, 4.3), ("iFruit", "15 128GB", 69999, 4.6), ("RealZoom", "12 Pro+", 27999, 4.3),
        ("RealZoom", "C55", 11999, 3.9), ("MotorEdge", "G84", 17999, 4.1), ("MotorEdge", "Edge 40", 29999, 4.4),
        ("VivoAir", "V29", 32999, 4.3), ("OppoGlow", "Reno 11", 31999, 4.2),
    ]
    out = []
    for idx, (brand, model, price, rating) in enumerate(brands, start=1):
        pid = f"ph-{idx:03d}"
        storage = "128 GB" if price < 30000 else "256 GB"
        ram = "6 GB" if price < 15000 else ("8 GB" if price < 40000 else "12 GB")
        out.append(
            p(
                pid,
                f"{brand} {model}",
                "smartphone",
                price,
                rating,
                f"{brand} {model} Android smartphone with {ram} RAM.",
                {
                    "ram": ram,
                    "storage": storage,
                    "camera": "50 MP main" if price > 20000 else "48 MP dual",
                    "battery": "5000 mAh" if price < 50000 else "4700 mAh",
                    "display": "AMOLED 90Hz" if price > 18000 else "LCD 90Hz",
                },
            )
        )
    return out


def tablets() -> list[dict]:
    items = [
        ("tb-001", "TabLite 8 WiFi", 8999, 3.9, "Compact tablet for reading.", {"display": "8.7 inch", "storage": "64 GB", "ram": "4 GB", "battery_life": "12 hours"}),
        ("tb-002", "TabStudy 10", 14999, 4.1, "Student tablet with stylus support.", {"display": "10.4 inch", "storage": "128 GB", "ram": "6 GB", "battery_life": "10 hours"}),
        ("tb-003", "PadPro 11", 34999, 4.4, "Thin productivity tablet.", {"display": "11 inch", "storage": "256 GB", "ram": "8 GB", "battery_life": "11 hours"}),
        ("tb-004", "GalaxyTab Style A9", 19999, 4.2, "Popular mid-range Android tab.", {"display": "10.5 inch", "storage": "128 GB", "ram": "8 GB", "battery_life": "12 hours"}),
        ("tb-005", "iPad Style Air", 54999, 4.6, "Premium tablet for creators.", {"display": "11 inch", "storage": "256 GB", "ram": "8 GB", "battery_life": "10 hours"}),
        ("tb-006", "KidsTab Safe", 9999, 4.0, "Parental controls built-in.", {"display": "8 inch", "storage": "32 GB", "ram": "3 GB", "battery_life": "9 hours"}),
        ("tb-007", "DrawTab Artist", 27999, 4.3, "Low-latency pen for drawing.", {"display": "11 inch", "storage": "128 GB", "ram": "8 GB", "battery_life": "10 hours"}),
        ("tb-008", "TabMax 12 LTE", 42999, 4.5, "LTE tablet for travel.", {"display": "12.4 inch", "storage": "256 GB", "ram": "8 GB", "battery_life": "11 hours"}),
    ]
    return [p(i, t, "tablet", pr, r, d, s) for i, t, pr, r, d, s in items]


def televisions() -> list[dict]:
    items = [
        ("tv-001", "HD Ready 32 Smart TV", 12999, 3.9, "Entry smart TV for bedroom.", {"screen_size": "32 inch", "resolution": "HD Ready", "smart_tv": "WebOS-like", "hdr": "None"}),
        ("tv-002", "Full HD 43 Smart TV", 22999, 4.1, "Full HD living room TV.", {"screen_size": "43 inch", "resolution": "Full HD", "smart_tv": "Android TV", "hdr": "None"}),
        ("tv-003", "4K UHD 43", 28999, 4.2, "4K streaming TV.", {"screen_size": "43 inch", "resolution": "4K UHD", "smart_tv": "Google TV", "hdr": "HDR10"}),
        ("tv-004", "4K 55 Fire Edition", 38999, 4.3, "55-inch value 4K.", {"screen_size": "55 inch", "resolution": "4K UHD", "smart_tv": "Fire TV", "hdr": "HDR10"}),
        ("tv-005", "QLED 55 Pro", 54999, 4.5, "QLED colors and gaming mode.", {"screen_size": "55 inch", "resolution": "4K UHD", "smart_tv": "Google TV", "hdr": "HDR10+"}),
        ("tv-006", "OLED 55 Cinema", 89999, 4.7, "OLED deep blacks.", {"screen_size": "55 inch", "resolution": "4K UHD", "smart_tv": "WebOS-style", "hdr": "Dolby Vision"}),
        ("tv-007", "MiniLED 65 Flagship", 119999, 4.6, "Bright MiniLED flagship.", {"screen_size": "65 inch", "resolution": "4K UHD", "smart_tv": "Google TV", "hdr": "Dolby Vision"}),
        ("tv-008", "Budget 40 LED", 17999, 3.8, "Affordable 40-inch LED.", {"screen_size": "40 inch", "resolution": "Full HD", "smart_tv": "Basic Smart", "hdr": "None"}),
    ]
    return [p(i, t, "television", pr, r, d, s) for i, t, pr, r, d, s in items]


def speakers() -> list[dict]:
    items = [
        ("spk-001", "MiniBoost Bluetooth Speaker", 1499, 3.9, "Pocket-size speaker.", {"power": "5W", "battery_life": "8 hours", "water_resistance": "IPX5", "connectivity": "Bluetooth 5.0"}),
        ("spk-002", "PartyBox 20W", 3499, 4.1, "Room-filling party speaker.", {"power": "20W", "battery_life": "12 hours", "water_resistance": "IPX4", "connectivity": "Bluetooth 5.1"}),
        ("spk-003", "HomeBar Soundbar 2.1", 8999, 4.3, "TV soundbar with subwoofer.", {"power": "120W", "battery_life": "N/A", "water_resistance": "None", "connectivity": "HDMI ARC + BT"}),
        ("spk-004", "EchoDot Style Smart Speaker", 4999, 4.2, "Smart assistant speaker.", {"power": "15W", "battery_life": "N/A", "water_resistance": "None", "connectivity": "WiFi + Bluetooth"}),
        ("spk-005", "OutdoorRock IP67", 5999, 4.4, "Rugged outdoor speaker.", {"power": "30W", "battery_life": "18 hours", "water_resistance": "IP67", "connectivity": "Bluetooth 5.2"}),
        ("spk-006", "StudioMonitor Bookshelf", 12999, 4.5, "Bookshelf speakers for PC.", {"power": "80W", "battery_life": "N/A", "water_resistance": "None", "connectivity": "RCA + BT"}),
    ]
    return [p(i, t, "speaker", pr, r, d, s) for i, t, pr, r, d, s in items]


def cameras() -> list[dict]:
    items = [
        ("cam-001", "SnapPoint Compact 20MP", 8999, 4.0, "Point-and-shoot travel camera.", {"sensor": "1/2.3 inch", "video": "1080p", "zoom": "5x optical", "battery_life": "250 shots"}),
        ("cam-002", "Mirrorless Alpha Lite", 44999, 4.5, "APS-C mirrorless starter kit.", {"sensor": "APS-C 24MP", "video": "4K 30fps", "zoom": "Kit 18-55mm", "battery_life": "410 shots"}),
        ("cam-003", "ActionCam Go 4K", 12999, 4.3, "Waterproof action camera.", {"sensor": "1/2 inch", "video": "4K 60fps", "zoom": "Digital", "battery_life": "90 min record"}),
        ("cam-004", "DSLR Entry 2000D Style", 32999, 4.2, "Beginner DSLR with lens.", {"sensor": "APS-C 24MP", "video": "1080p", "zoom": "Kit 18-55mm", "battery_life": "500 shots"}),
        ("cam-005", "VlogCam ZV Flip", 54999, 4.6, "Flip screen vlogging camera.", {"sensor": "APS-C", "video": "4K", "zoom": "Kit lens", "battery_life": "440 shots"}),
    ]
    return [p(i, t, "camera", pr, r, d, s) for i, t, pr, r, d, s in items]


def appliances() -> list[dict]:
    items = [
        ("ap-001", "AirFryer Crisp 4L", 4999, 4.2, "4L digital air fryer.", {"capacity": "4 L", "power": "1500W", "warranty": "1 year", "type": "Air fryer"}),
        ("ap-002", "Mixer Grinder 750W", 3499, 4.1, "Indian kitchen mixer grinder.", {"capacity": "1.5 L jar", "power": "750W", "warranty": "2 years", "type": "Mixer"}),
        ("ap-003", "RobotVac CleanBot", 19999, 4.3, "Robot vacuum mop combo.", {"capacity": "0.4 L dustbin", "power": "45W", "warranty": "1 year", "type": "Vacuum"}),
        ("ap-004", "InstantPot Multi 6L", 8999, 4.4, "6-in-1 pressure cooker.", {"capacity": "6 L", "power": "1000W", "warranty": "2 years", "type": "Cooker"}),
        ("ap-005", "ChillPro 250L Fridge", 18999, 4.0, "Double door refrigerator.", {"capacity": "250 L", "power": "3 star", "warranty": "10 years compressor", "type": "Refrigerator"}),
        ("ap-006", "WashFast 7kg Front Load", 27999, 4.2, "Front load washing machine.", {"capacity": "7 kg", "power": "5 star", "warranty": "2 years", "type": "Washing machine"}),
    ]
    return [p(i, t, "appliance", pr, r, d, s) for i, t, pr, r, d, s in items]


def main() -> None:
    catalog: list[dict] = []
    for builder in (headphones, laptops, smartwatches, smartphones, tablets, televisions, speakers, cameras, appliances):
        catalog.extend(builder())
    OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(catalog)} products to {OUT}")


if __name__ == "__main__":
    main()
