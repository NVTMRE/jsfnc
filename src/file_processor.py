import os
import re
from constants import SEASON_EPISODE_PATTERNS

def extract_season_episode(filename):
    """Extract season and episode numbers from filename."""
    for pattern in SEASON_EPISODE_PATTERNS:
        match = re.search(pattern, filename)
        if match:
            season = str(int(match.group(1))).zfill(2)
            episode = str(int(match.group(2))).zfill(2)
            return season, episode
    return None, None


def process_directory(directory_path, show_name):
    """Process files in directory and rename them."""
    stats = {"renamed": 0, "skipped": 0, "error": 0}

    try:
        filenames = sorted(os.listdir(directory_path))
    except OSError as e:
        print(f"ERROR: Could not read directory: {e}")
        return

    for filename in filenames:
        if filename.startswith('.'):
            continue

        filepath = os.path.join(directory_path, filename)
        if not os.path.isfile(filepath):
            continue

        filename_base, file_extension = os.path.splitext(filename)
        season, episode = extract_season_episode(filename_base)

        if season and episode:
            new_filename = f"{show_name} - S{season}E{episode}{file_extension}"
            new_filepath = os.path.join(directory_path, new_filename)

            print(f"\nProposed rename:")
            print(f"  From: {filename}")
            print(f"  To:   {new_filename}")

            choice = input("Proceed? (y/n/a/q): ").lower()
            if choice in ['a', 'y']:
                try:
                    os.rename(filepath, new_filepath)
                    stats["renamed"] += 1
                    print("Renamed successfully.")
                except OSError as e:
                    print(f"Error renaming file: {e}")
                    stats["error"] += 1
            elif choice == 'q':
                break
            else:
                stats["skipped"] += 1

    print("\n-----------------------------------------------------")
    print("Renaming process finished.")
    print(f"  Successfully renamed: {stats['renamed']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['error']}")
    print("-----------------------------------------------------")