urls = ["https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4213.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4269.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4270.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4278.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4290.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4321.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/DSC_4327.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/bluegray_gnatcatcher-1_01.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/bluegray_gnatcatcher-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/bluegray_gnatcatcher-3_01.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/brown_creeper.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/brown_headedc_cowbird-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/carolina wren-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/carolina_wren-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/carolina_wren-2.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/eastern_bluebird-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/european_starling.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/golden_finch.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/northern_cardinal_female-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/northern_cardinal_female-2.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/northern_flickr.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/redheaded_woodpecker-1.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/ruby_crowned_classic.jpg","https://s3.amazonaws.com/cdn.knoppers.icu/buseybirdsdawn/white_breasted_nuthatcher-1.jpg"]
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
