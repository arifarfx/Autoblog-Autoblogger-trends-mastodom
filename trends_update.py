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

        # Gunakan waktu sekarang sebagai waktu update
        update_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

        return keywords, update_time

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "", ""  # Kembalikan string kosong jika ada error


# Buat tabel Markdown
table_data = []
for i, country in enumerate(countries):
    keywords, update_time = get_keywords(country)
    table_data.append([i+1, country, keywords, update_time])

table_header = ["No.", "Countries", "Keywords", "Last Updates"]
table_rows = ["| " + " | ".join(map(str, row)) + " |" for row in table_data]
table_md = "| " + " | ".join(table_header) + " |\n"
table_md += "|---|---|---|---|\n"
table_md += "\n".join(table_rows)

# Buat isi README.md
readme_content = f"""
# Get Google Trends Autoblog Auto Update
<a href="https://blogkeren.web.id">AI Google Trends Autoblog</a>.


## Tabel:

{table_md}

## Autoblogger: Your Secret Weapon for Effortless Content Creation (on Blogspot!)

In the digital age, consistent, high-quality content reigns supreme. But creating a steady stream of engaging articles, blog posts, and website updates can feel like a Herculean task.  That's where **autoblogging** comes in. 

An **autoblogger** harnesses the power of automation to streamline content creation, freeing you from the endless cycle of writing, editing, and publishing. This allows you to focus on other aspects of your online presence, like building your audience and promoting your brand, all while keeping your Blogspot buzzing with activity.

### Beyond Content Curation: Exploring the True Potential of Autoblogging (on Blogspot!)

While some associate **autoblogging** with simply curating content from other sources, its true potential lies in generating original, valuable content with minimal human input. This can be achieved through various methods, including:

* **AI-powered content generation:** Leverage advanced AI writing tools to create unique, engaging articles based on your chosen keywords and topics, directly published to your Blogspot.


### The Best Autoblogging Tool for Blogspot:  Free and Reliable

Looking for a fantastic **autoblogger** that's both free and reliable for your Blogspot? Look no further than **Blog Keren** ([https://blogkeren.web.id](https://blogkeren.web.id)). This powerful tool offers automated content generation, SEO optimization, and a user-friendly interface, all while seamlessly integrating with Blogspot.  

**But that's not all!**  Blog Keren utilizes Google Trends to identify trending keywords, ensuring your content is always relevant and optimized for search engines.  Plus, it's available in 48 countries with customizable language settings, making it the perfect solution for bloggers worldwide. For just $5 per blog per month, you can enjoy the benefits of **autoblogging** without breaking the bank.


### Harnessing the Power of AI for Autoblogging (on Blogspot!)

AI is transforming the **autoblogging** landscape.  Tools like **ChatGPT Autoblogger** and **Blog Keren** can generate high-quality, human-like content on a wide range of topics, enabling you to:

* **Autoblogger AP:** Automatically generate news articles and press releases for your Blogspot.
* **Autoblogger IA:** Create informative articles and blog posts on various subjects, published directly to your Blogspot.
* **Free Autoblogger:** Access free AI writing tools to experiment with **autoblogging** on your Blogspot.

### Answering Your Autoblogging Questions

**1. Is autoblogging profitable?**

Absolutely! **Autoblogging** can be a lucrative venture. By automating content creation, you can:

* Drive website traffic and generate ad revenue on your Blogspot.
* Attract potential customers and promote affiliate products through your Blogspot.
* Build a strong online presence and establish yourself as an authority in your niche using your Blogspot.

**2. Is autoblogging AI good?**

AI-powered **autoblogging** tools offer numerous advantages:

* **Increased efficiency:** Generate content quickly and easily for your Blogspot.
* **Improved content quality:** Produce well-written, engaging articles that keep your Blogspot audience hooked.
* **Enhanced SEO:** Optimize content for search engines and improve your Blogspot's rankings.

However, it's essential to remember that AI should complement, not replace, human creativity and oversight.


###  Embrace the Future of Content Creation (on Blogspot!)

**Autoblogging** is a game-changer for anyone looking to streamline content creation and maximize their online impact, especially on Blogspot. By embracing this innovative approach, you can free up valuable time and resources while ensuring your Blogspot remains fresh and engaging.

So, dive into the world of **autoblogging** and unlock the potential of automated content creation on your Blogspot!
"""

# Tulis ke README.md
with open('README.md', 'w') as f:
    f.write(readme_content)
