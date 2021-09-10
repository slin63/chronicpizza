urls = ["https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/01-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/05-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/12-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/16-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/21-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/24-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/26-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/29-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/30-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/32-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/34-Enhanced.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/8-31-21_film_portra-400/35-Enhanced.jpg"]
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
