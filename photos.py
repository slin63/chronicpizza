urls = ["https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/04.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/06.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/14.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/18.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/21.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/23.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/33.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-13-21_film_ektar-100/36.jpg"]
template = """{{<
    imagecap
    url="$URL"
    caption="$URL"
>}}"""

out = ""

for url in urls:
    line = template.replace("$URL", url)
    out += line + "\n\n"

print(out)

# Replace `urls` with whatever
# `Command build with Python`
# ???
# Profit
