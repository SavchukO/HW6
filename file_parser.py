import sys
from pathlib import Path

IMAGES = []
VIDEO = []
AUDIO = []
DOCS = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': IMAGES,
    'JPG': IMAGES,
    'PNG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'MP4': VIDEO,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'VAW': AUDIO,
    'AMR': AUDIO,
    'TXT': DOCS,
    'DOC': DOCS,
    'DOCX': DOCS,
    'PDF': DOCS,
    'XLSX': DOCS,
    'PPTX': DOCS,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper() 

def scan(folder: Path):
    for item in folder.iterdir():
        
        if item.is_dir(): 
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        extension = get_extension(item.name)
        full_name = folder / item.name
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'Images jpeg: {IMAGES}')
    print(f'Images jpg: {VIDEO}')
    print(f'Images png: {AUDIO}')
    print(f'AUDIO mp3: {DOCS}')
    print(f'Archives zip: {ARCHIVES}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'Folders: {FOLDERS}')