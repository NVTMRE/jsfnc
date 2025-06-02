import os
import argparse
from file_processor import process_directory
from directory_structure import create_directory_structure
from utils import format_show_name

def main():
    """Parse command-line arguments and start file processing."""
    parser = argparse.ArgumentParser(
        description="TV Show Episode Manager - Rename files or create structured directories",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-n", "--name",
        required=True,
        type=str,
        help="The target name for the TV show (e.g., \"Solo Leveling\")"
    )
    parser.add_argument(
        "-p", "--path",
        type=str,
        default=None,
        help="The path to process files from (defaults to current directory)"
    )
    parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=['rename', 'structure'],
        default='rename',
        help="Operation mode:\n"
             "rename: Rename files in place (default)\n"
             "structure: Create organized directory structure"
    )
    parser.add_argument(
        "-t", "--target",
        type=str,
        help="Target directory for structure mode (required when mode=structure)"
    )

    args = parser.parse_args()
    source_dir = args.path if args.path else os.getcwd()
    formatted_name = format_show_name(args.name)

    if args.mode == 'structure':
        if not args.target:
            parser.error("--target is required when using structure mode")
        create_directory_structure(source_dir, args.target, formatted_name)
    else:
        process_directory(source_dir, formatted_name)


if __name__ == "__main__":
    main()