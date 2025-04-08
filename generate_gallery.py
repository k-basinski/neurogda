# config
photo_names = list(range(1,12))
photo_width = 800
photo_ext = 'jpg'
photo_prefix = 'assets/img/gallery/'
randomize = False
page_title = 'Gallery'

def generate_gallery_html(photo):
    file_name = photo_prefix + str(photo) + '.' + photo_ext
    return f'<img src="{file_name}" width="{photo_width}">\n\n'
    
# generate yml
yml = f'---\ntitle: "{page_title}"\n---\n\n'

# generate gallery html
with open('gallery.md', 'w') as f:
    f.write(yml)
    for p in photo_names:
        f.write(generate_gallery_html(p))
