import requests
from datetime import datetime, timezone

# Daftar nama negara
countries = [
    "ARGENTINA", "AUSTRALIA", "AUSTRIA", "BELGIUM", "BRAZIL", "CANADA", 
    "CHILE", "COLOMBIA", "CZECHIA", "DENMARK", "EGYPT", "FINLAND", "FRANCE", 
    "GERMANY", "GREECE", "HONG KONG", "HUNGARY", "INDIA", "INDONESIA", 
    "IRELAND", "ISRAEL", "ITALY", "JAPAN", "KENYA", "MALAYSIA", "MEXICO", 
    "NETHERLANDS", "NEW ZEALAND", "NIGERIA", "NORWAY", "PHILIPPINES", "POLAND", 
    "PORTUGAL", "ROMANIA", "RUSSIA", "SAUDI ARABIA", "SINGAPORE", "SOUTH AFRICA", 
    "SOUTH KOREA", "SWEDEN", "SWITZERLAND", "TAIWAN", "THAILAND", "TURKEY", 
    "UKRAINE", "UNITED KINGDOM", "UNITED STATES", "VIETNAM"
]

# Fungsi untuk mengambil data dari file .txt
def get_keywords(country):
    url = f"https://raw.githubusercontent.com/arifarfx/Google-Trends-Keywords-Scraper/refs/heads/main/forcopied/{country}.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        # Debugging: Tampilkan isi response
        print(f"Isi response untuk {country}.txt:")
        print(response.text) 

        keywords = response.text.replace(",", ", ")  # Ganti koma dengan koma dan spasi

        # Ambil waktu update terakhir dari repository
        update_time = datetime.fromtimestamp(response.headers['Last-Modified'], 
                                             tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

        return keywords, update_time

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "", ""  # Kembalikan string kosong jika ada error


# Buat tabel Markdown
table_data = []
for i, country in enumerate(countries):
    keywords, update_time = get_keywords(country)
    table_data.append([i+1, country, keywords, update_time])

table_header = ["No.", "Nama Negara", "Kata Kunci", "Waktu Update"]
table_rows = ["| " + " | ".join(map(str, row)) + " |" for row in table_data]
table_md = "| " + " | ".join(table_header) + " |\n"
table_md += "|---|---|---|---|\n"
table_md += "\n".join(table_rows)

# Buat isi README.md
readme_content = f"""
Get autoblog update
<a href="https://blogkeren.web.id">AI Google Trends Autoblog</a>.


Tabel:

{table_md}
"""

# Tulis ke README.md
with open('README.md', 'w') as f:
    f.write(readme_content)
