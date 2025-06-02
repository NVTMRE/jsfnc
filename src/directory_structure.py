import os
import shutil
from file_processor import extract_season_episode

def create_directory_structure(source_path, target_path, series_name):
    """Creates a structured directory for TV show episodes."""
    stats = {"moved": 0, "skipped": 0, "error": 0}
    series_dir = os.path.join(target_path, series_name)
    process_all = False

    try:
        filenames = sorted(os.listdir(source_path))
    except OSError as e:
        print(f"ERROR: Could not read source directory: {e}")
        return

    # First pass - identify seasons
    seasons = set()
    for filename in filenames:
        if filename.startswith('.') or not os.path.isfile(os.path.join(source_path, filename)):
            continue
        filename_base, _ = os.path.splitext(filename)
        season, _ = extract_season_episode(filename_base)
        if season:
            seasons.add(season)

    # Create season directories
    for season in sorted(seasons):
        season_dir = os.path.join(series_dir, f"Season {season}")
        os.makedirs(season_dir, exist_ok=True)

    # Second pass - move files
    for filename in filenames:
        if filename.startswith('.'):
            stats["skipped"] += 1
            continue

        source_file = os.path.join(source_path, filename)
        if not os.path.isfile(source_file):
            continue

        filename_base, file_extension = os.path.splitext(filename)
        season, episode = extract_season_episode(filename_base)

        if season and episode:
            new_filename = f"{series_name} - S{season}E{episode}{file_extension}"
            season_dir = os.path.join(series_dir, f"Season {season}")
            target_file = os.path.join(season_dir, new_filename)

            if not process_all:
                print(f"\nProposed move:")
                print(f"  From: {filename}")
                print(f"  To:   Season {season}/{new_filename}")

                choice = input("Proceed? (y/n/a/q): ").lower()
                if choice == 'q':
                    break
                elif choice == 'a':
                    process_all = True
                elif choice != 'y':
                    stats["skipped"] += 1
                    continue

            try:
                if not os.path.exists(target_file):
                    shutil.copy2(source_file, target_file)
                    print(f"Copied: {filename} -> {os.path.join(f'Season {season}', new_filename)}")
                    stats["moved"] += 1
                else:
                    print(f"File already exists, skipping: {new_filename}")
                    stats["skipped"] += 1
            except OSError as e:
                print(f"Error processing {filename}: {e}")
                stats["error"] += 1
        else:
            print(f"Could not extract season/episode info from: {filename}")
            stats["skipped"] += 1

    print_stats(stats)


def print_stats(stats):
    print("\n-----------------------------------------------------")
    print("Directory structure creation finished.")
    print(f"  Successfully processed: {stats['moved']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['error']}")
    print("-----------------------------------------------------")