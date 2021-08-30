urls = ["https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/02.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/03.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/09.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/25.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/32.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/33.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/35.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-30-21_film_ultramax-400/36.jpg"]
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
