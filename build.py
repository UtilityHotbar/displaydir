import os
import markdown
import distutils.dir_util as dir_util
import shutil

CONTENT_DIR = 'content'
DEST_ROOT = 'public'
DEST_DIR = 'public/content'
CSS_DIR = 'css'
ICON_DIR = 'icons'
PAGE_TEMPLATE = 'templates/page.html'
RETURN_SELECT_TEMPLATE = 'templates/return_select.html'
FOLDER_SELECT_TEMPLATE = 'templates/folder_select.html'
FILE_SELECT_TEMPATE = 'templates/file_select.html'

with open(RETURN_SELECT_TEMPLATE, 'r') as f:
    RETURN_SELECT = f.read()
    
with open(FOLDER_SELECT_TEMPLATE, 'r') as f:
    FOLDER_SELECT = f.read()
    
with open(FILE_SELECT_TEMPATE, 'r') as f:
    FILE_SELECT = f.read()


def scan_and_build_dir(path, dest_path, depth=1):
    commentary = ''
    return_string = '../'*depth
    if depth > 1:
        prov_html = RETURN_SELECT
    else:
        prov_html = ''
    for thing in os.scandir(path):
        if thing.name == '':
            name = 'NO_NAME'
        elif thing.name == 'readme.md':
            with open(thing.path) as f:
                commentary = markdown.markdown(f.read().strip('\n'), extensions=['sane_lists', 'extra'])
            continue
        else:
            name = thing.name
        parts = name.split(".")
        if len(parts) == 1:
            extension = 'txt'
        else:
            extension = parts[-1]
        if thing.is_dir():
            prov_html += FOLDER_SELECT.replace('{return_string}', return_string).replace('{name}', name)
            scan_and_build_dir(thing.path, dest_path+'/'+thing.name, depth=depth+1)
        elif thing.is_file():
            prov_html += FILE_SELECT.replace('{return_string}', return_string).replace('{name}', name).replace('{extension}', extension)
    with open(PAGE_TEMPLATE) as f:
        content = f.read().replace('{return_string}', return_string).replace('{commentary}', commentary).replace('{content}', prov_html).replace('{path}', path)
    with open(dest_path+'/index.html', 'w') as g:
        g.write(content)


def main():
    try:
        shutil.rmtree(DEST_DIR)
    except FileNotFoundError:
        pass
    try:
        shutil.rmtree(DEST_ROOT+'/'+CSS_DIR)
    except FileNotFoundError:
        pass
    try:
        shutil.rmtree(DEST_ROOT+'/'+ICON_DIR)
    except FileNotFoundError:
        pass
    dir_util.copy_tree(CSS_DIR, DEST_ROOT+'/'+CSS_DIR)
    dir_util.copy_tree(ICON_DIR, DEST_ROOT+'/'+ICON_DIR)
    dir_util.copy_tree(CONTENT_DIR, DEST_DIR)
    scan_and_build_dir(CONTENT_DIR, DEST_DIR)


if __name__ == '__main__':
    main()
        