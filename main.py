import os
import argparse

def print_tree(start_path, prefix='', max_depth=None, current_depth=0, show_files=True, show_hidden=False):
    try:
        entries = os.listdir(start_path)
    except PermissionError:
        print(prefix + '└── [Permission Denied]')
        return

    entries = sorted(entries)
    if not show_hidden:
        entries = [e for e in entries if not e.startswith('.')]
    
    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        
        if not show_files and not os.path.isdir(path):
            continue  # Skip files if we're only showing directories

        connector = '└── ' if index == len(entries) - 1 else '├── '
        print(prefix + connector + entry)

        if os.path.isdir(path):
            if max_depth is None or current_depth + 1 < max_depth:
                extension = '    ' if index == len(entries) - 1 else '│   '
                print_tree(path, prefix + extension, max_depth, current_depth + 1, show_files, show_hidden)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom 'tree' command in Python")
    parser.add_argument('path', nargs='?', default='.', help='Directory to list (default: current directory)')
    parser.add_argument('--depth', type=int, default=None, help='Max depth to display')
    parser.add_argument('--all', action='store_true', help='Include hidden files')
    parser.add_argument('--dirs-only', action='store_true', help='Only show directories')

    args = parser.parse_args()

    print(args.path)
    print_tree(
        args.path,
        prefix='',
        max_depth=args.depth,
        show_files=not args.dirs_only,
        show_hidden=args.all
    )

