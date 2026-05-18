import pygame

SCORE_FILE = "assets/json/scores.json"
PLAYER_FONT="assets/fonts/PressStart2P.ttf"
MT_FUJI = "assets/background/fuji.jpg"
JAPANESE_FONT = "meiryo"
AUDIO_PATH = "assets/audio/"
NO_SCORE = "NO SCORE"
GAME_FPS = 60
BLACK = pygame.Color("black")
LIGHT_GRAY = pygame.Color("lightgray")
DARK_GRAY = pygame.Color("darkgray")
WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
NEON_GREEN = pygame.Color("lime")
LIME_GREEN = pygame.Color("limegreen")
RED = pygame.Color("red")
PINK =pygame.Color("pink")
YELLOW = pygame.Color("yellow")
LIGHT_BLUE = pygame.Color("deepskyblue")
TIMER_COLOR = pygame.Color("forestgreen")

KANA_MASTER_LIST = \
    ["a", "i", "u", "e", "o",
     "ka", "ki", "ku", "ke", "ko",
     "sa", "shi", "su", "se", "so",
     "ta", "chi", "tsu", "te", "to",
     "na", "ni", "nu", "ne", "no",
     "ha", "hi", "fu", "he", "ho",
     "ma", "mi", "mu", "me", "mo",
     "ra", "ri", "ru", "re", "ro",
     "ya", "yu", "yo",
     "wa", "wo", "n"]

HIRAGANA = \
    {"a" : "あ", "i" : "い", "u" : "う", "e" : "え", "o" : "お",
     "ka" : "か", "ki" : "き", "ku" : "く", "ke" : "け", "ko" : "こ",
     "sa" : "さ", "shi" : "し", "su" : "す", "se" : "せ", "so" : "そ",
     "ta" : "た", "chi" : "ち", "tsu" : "つ", "te" : "て", "to" : "と",
     "na" : "な", "ni" : "に", "nu" : "ぬ", "ne" : "ね", "no" : "の",
     "ha" : "は", "hi" : "ひ", "fu" : "ふ", "he" : "へ", "ho" : "ほ",
     "ma" : "ま", "mi" : "み", "mu" : "む", "me" : "め", "mo" : "も",
     "ra" : "ら", "ri" : "り", "ru" : "る", "re" : "れ", "ro" : "ろ",
     "ya" : "や", "yu" : "ゆ", "yo" : "よ",
     "wa" : "わ", "wo" : "を", "n" : "ん"}

KATAKANA = \
    {"a" : "ア", "i" : "イ", "u" : "ウ", "e" : "エ", "o" : "オ",
     "ka" : "カ", "ki" : "キ", "ku" : "ク", "ke" : "ケ", "ko" : "コ",
     "sa" : "サ", "shi" : "シ", "su" : "ス", "se" : "セ", "so" : "ソ",
     "ta" : "タ", "chi" : "チ", "tsu" : "ツ", "te" : "テ", "to" : "ト",
     "na" : "ナ", "ni" : "二", "nu" : "ヌ", "ne" : "ネ", "no" : "ノ",
     "ha" : "ハ", "hi" : "ヒ", "fu" : "フ", "he" : "へ", "ho" : "ホ",
     "ma" : "マ", "mi" : "ミ", "mu" : "ム", "me" : "メ", "mo" : "モ",
     "ra" : "ラ", "ri" : "リ", "ru" : "ル", "re" : "レ", "ro" : "ロ",
     "ya" : "ヤ", "yu" : "ユ", "yo" : "ヨ",
     "wa" : "ワ", "wo" : "ヲ", "n" : "ン"}