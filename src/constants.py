SEASON_EPISODE_PATTERNS = [
    r'[Ss](\d{1,2})[Ee](\d{1,2})',         # S01E02
    r'[Ss](\d{1,2})\.?[Ee](\d{1,2})',      # S01.E02
    r'[Ss]eason\s*(\d{1,2})\s*[Ee]pisode\s*(\d{1,2})',  # Season 01 Episode 02
    r'(\d{1,2})x(\d{1,2})',                # 01x02
    r'\.(\d)(\d{2})',                       # .102
    r'\.(\d{2})(\d{2})'                     # .0102
]