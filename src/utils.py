def format_show_name(name: str) -> str:
    """
    Format show name by removing spaces and special characters.
    Example: "Solo Leveling" -> "SoloLeveling"
            "My-Favorite.Show" -> "MyFavoriteShow"
    """
    # Remove special characters and spaces, keeping only alphanumeric chars
    import re
    # First replace common separators with spaces
    name = re.sub(r'[-._]+', ' ', name)
    # Split into words and capitalize each one
    words = name.split()
    words = [word.capitalize() for word in words]
    # Join without spaces
    return ''.join(words)