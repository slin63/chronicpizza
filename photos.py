urls = ["https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/02-2.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/03.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/09.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/10.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/11.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/12.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/13.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/14.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/9-28-21_film_ektar-100/15.jpg"]
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
