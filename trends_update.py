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
Get Google Trends Autoblog Auto Update
<a href="https://blogkeren.web.id">AI Google Trends Autoblog</a>.


Tabel:

{table_md}
"""
# Promo
<center><h1>Autoblogger: Your Secret Weapon for Effortless Content Creation (on Blogspot!)</h1></center>

    <p>In the digital age, consistent, high-quality content reigns supreme. But creating a steady stream of engaging articles, blog posts, and website updates can feel like a Herculean task.  That's where <strong>autoblogging</strong> comes in. </p>

    <p>An <strong>autoblogger</strong> harnesses the power of automation to streamline content creation, freeing you from the endless cycle of writing, editing, and publishing. This allows you to focus on other aspects of your online presence, like building your audience and promoting your brand, all while keeping your Blogspot buzzing with activity.</p>

    <h2>Beyond Content Curation: Exploring the True Potential of Autoblogging (on Blogspot!)</h2>

    <p>While some associate <strong>autoblogging</strong> with simply curating content from other sources, its true potential lies in generating original, valuable content with minimal human input. This can be achieved through various methods, including:</p>

    <ul>
        <li><strong>AI-powered content generation:</strong> Leverage advanced AI writing tools to create unique, engaging articles based on your chosen keywords and topics, directly published to your Blogspot.</li>
    </ul>

    <h2>The Best Autoblogging Tool for Blogspot:  Free and Reliable</h2>

    <p>Looking for a fantastic <strong>autoblogger</strong> that's both free and reliable for your Blogspot? Look no further than <strong>Blog Keren</strong> (<a href="https://blogkeren.web.id">https://blogkeren.web.id</a>). This powerful tool offers automated content generation, SEO optimization, and a user-friendly interface, all while seamlessly integrating with Blogspot.  </p>

    <p><strong>But that's not all!</strong>  Blog Keren utilizes Google Trends to identify trending keywords, ensuring your content is always relevant and optimized for search engines.  Plus, it's available in 48 countries with customizable language settings, making it the perfect solution for bloggers worldwide. For just $5 per blog per month, you can enjoy the benefits of <strong>autoblogging</strong> without breaking the bank.</p>

    <h2>Harnessing the Power of AI for Autoblogging (on Blogspot!)</h2>

    <p>AI is transforming the <strong>autoblogging</strong> landscape.  Tools like <strong>ChatGPT Autoblogger</strong> and <strong>Blog Keren</strong> can generate high-quality, human-like content on a wide range of topics, enabling you to:</p>

    <ul>
        <li><strong>Autoblogger AP:</strong> Automatically generate news articles and press releases for your Blogspot.</li>
        <li><strong>Autoblogger IA:</strong> Create informative articles and blog posts on various subjects, published directly to your Blogspot.</li>
        <li><strong>Free Autoblogger:</strong> Access free AI writing tools to experiment with <strong>autoblogging</strong> on your Blogspot.</li>
    </ul>

    <h2>Answering Your Autoblogging Questions</h2>

    <h3>1. Is autoblogging profitable?</h3>

    <p>Absolutely! <strong>Autoblogging</strong> can be a lucrative venture. By automating content creation, you can:</p>

    <ul>
        <li>Drive website traffic and generate ad revenue on your Blogspot.</li>
        <li>Attract potential customers and promote affiliate products through your Blogspot.</li>
        <li>Build a strong online presence and establish yourself as an authority in your niche using your Blogspot.</li>
    </ul>

    <h3>2. Is autoblogging AI good?</h3>

    <p>AI-powered <strong>autoblogging</strong> tools offer numerous advantages:</p>

    <ul>
        <li><strong>Increased efficiency:</strong> Generate content quickly and easily for your Blogspot.</li>
        <li><strong>Improved content quality:</strong> Produce well-written, engaging articles that keep your Blogspot audience hooked.</li>
        <li><strong>Enhanced SEO:</strong> Optimize content for search engines and improve your Blogspot's rankings.</li>
    </ul>

    <p>However, it's essential to remember that AI should complement, not replace, human creativity and oversight.</p>

    <h2>Embrace the Future of Content Creation (on Blogspot!)</h2>

    <p><strong>Autoblogging</strong> is a game-changer for anyone looking to streamline content creation and maximize their online impact, especially on Blogspot. By embracing this innovative approach, you can free up valuable time and resources while ensuring your Blogspot remains fresh and engaging.</p>

    <p>So, dive into the world of <strong>autoblogging</strong> and unlock the potential of automated content creation on your Blogspot!</p>
# Tulis ke README.md
with open('README.md', 'w') as f:
    f.write(readme_content)
