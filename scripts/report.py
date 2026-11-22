#!/usr/bin/env python3
"""İndirilen XMLTV'de gerçek yayın programı bulunup bulunmadığını kontrol eder."""
import sys
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

path = Path(sys.argv[1] if len(sys.argv) > 1 else "guide.xml")
if not path.is_file():
    print(f"HATA: {path} bulunamadı.")
    sys.exit(1)
try:
    root = ET.parse(path).getroot()
except ET.ParseError as error:
    print(f"HATA: XML okunamadı: {error}")
    sys.exit(1)

names = {}
for channel in root.findall("channel"):
    display = channel.findtext("display-name") or channel.get("id", "Bilinmiyor")
    names[channel.get("id", "")] = display
programmes = root.findall("programme")
counts = Counter(p.get("channel", "") for p in programmes)
print(f"XML kanal sayısı: {len(names)}")
print(f"GERÇEK PROGRAM SAYISI: {len(programmes)}")
for channel_id, count in counts.most_common():
    print(f"  {names.get(channel_id, channel_id)}: {count} program")
print("Örnek kayıtlar:")
for programme in programmes[:8]:
    title = programme.findtext("title") or "(başlıksız)"
    print(f"  {programme.get('start', '')} | {names.get(programme.get('channel', ''), programme.get('channel', ''))} | {title}")
if not programmes:
    print("SONUÇ: Başarısız; XML'de <programme> bulunamadı.")
    sys.exit(1)
print("SONUÇ: En az bir gerçek yayın kaydı var; kaynakların doğruluğu ayrıca kontrol edilmeli.")
