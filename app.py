import os
import shutil

extensions: dict[str, list[str]] = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.webp', '.ico', '.heic', '.raw'],
    'Documents': [
        '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx',
        '.md', '.csv', '.epub', '.tex'
    ],
    'Videos': [
        '.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.3gp', '.m4v'
    ],
    'Audio': [
        '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff', '.alac'
    ],
    'Archives': [
        '.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.iso', '.cab', '.dmg'
    ],
    'Scripts': [
        '.py', '.js', '.ts', '.sh', '.bat', '.ps1', '.rb', '.php', '.pl', '.java', '.c', '.cpp', '.cs',
        '.go', '.swift', '.r', '.lua', '.kt'
    ],
    'Others': [
        '.exe', '.apk', '.msi', '.bin', '.dat', '.tmp', '.log', '.bak', '.cfg', '.ini'
    ]
}

def organize(location: str) -> None:
    files: list[str] = os.listdir(location)
    for file in files:
        for extension in extensions:
            for ext in extensions[extension]:
                if file.endswith(ext):
                    os.makedirs(extension, exist_ok=True)
                    shutil.move(os.path.join(location, file), extension)
                    break

organize(os.path.join(os.getcwd()))