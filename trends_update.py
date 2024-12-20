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

        data = response.text.splitlines()
        if len(data) >= 3:  # Pastikan file memiliki minimal 3 baris
            update_time = data[1].replace("Update Data ", "")
            keywords = data[2].replace(",", ", ")  # Ganti koma dengan koma dan spasi
            return keywords, update_time
        else:
            print(f"Error: File {country}.txt tidak valid")
            return "", ""  # Kembalikan string kosong jika file tidak valid
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "", ""  # Kembalikan string kosong jika ada error
