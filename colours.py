"""This module will be used to make
our CLI colorful in the project"""

#Importing....
import random

# Code for colorful CLI
# ──────────────── Normal text colors ────────────────
black        = "\033[0;30m"
red          = "\033[0;31m"
green        = "\033[0;32m"
yellow       = "\033[0;33m"
blue         = "\033[0;34m"
purple       = "\033[0;35m"
cyan         = "\033[0;36m"
light_gray   = "\033[0;37m"

# ───────────── Bright text colors ─────────────
dark_gray    = "\033[1;30m"
light_red    = "\033[1;31m"
light_green  = "\033[1;32m"
light_yellow = "\033[1;33m"
light_blue   = "\033[1;34m"
light_purple = "\033[1;35m"
light_cyan   = "\033[1;36m"
light_white  = "\033[1;37m"

#------------------Some New colors------------------
orange           = "\033[38;5;208m"
electric_Blue    = "\033[38;5;45m"
mint_Green       = "\033[38;5;48m"
hot_Pink         = "\033[38;5;198m"
acidic_red       = "\033[38;5;196m"

# ───────────── Unique, Vibrant New Colors ─────────────
neon_purple    = "\033[38;5;201m"  # Ultra bright magenta-violet
acid_green     = "\033[38;5;154m"  # Toxic highlighter green, very eye-catching
neon_orange    = "\033[38;5;214m"  # More punchy than standard orange
electric_lime  = "\033[38;5;118m"  # Laser lime green, brighter than Mint
aqua_cyan      = "\033[38;5;51m"   # Aqua blue with a tropical vibe
deep_sky       = "\033[38;5;45m"   # Variant of Electric_Blue, deeper sky tone
bubblegum_pink = "\033[38;5;212m"  # Lively, candy-like pink tone
toxic_yellow   = "\033[38;5;190m"  # Aggressive radioactive yellow-green
icy_blue       = "\033[38;5;159m"  # Frozen bluish-white, very bright and elegant
neon_peach     = "\033[38;5;217m"  # Fruity light orange-pink fusion

#Toxic / Hazard / Venom Colors (Unique, High-Impact Shades)

nuclear_yellow    = "\033[38;5;190m"   # Glowing warning label
toxic_green       = "\033[38;5;118m"   # Biohazard green
venom_purple      = "\033[38;5;129m"   # Deep toxic venom
hazard_orange     = "\033[38;5;208m"   # Construction/danger zone
bio_blue          = "\033[38;5;45m"    # Synthetic liquid glow
plasma_violet     = "\033[38;5;201m"   # Futuristic weapon glow
slime_lime        = "\033[38;5;154m"   # Radioactive ooze
neon_pink         = "\033[38;5;213m"   # Loud techno warning
mutant_cyan       = "\033[38;5;51m"    # Alien fluid dataflow




# ───────────── Extended 256-color codes ─────────────
# pink was 206; here are a few more shades:
pink         = "\033[38;5;206m"
magenta      = "\033[38;5;201m"
gold         = "\033[38;5;220m"
lime         = "\033[38;5;118m"
teal         = "\033[38;5;37m"
turquoise    = "\033[38;5;44m"
violet       = "\033[38;5;135m"
salmon       = "\033[38;5;203m"
peach        = "\033[38;5;215m"
lavender     = "\033[38;5;225m"
sky_blue     = "\033[38;5;117m"
olive        = "\033[38;5;100m"
maroon       = "\033[38;5;88m"
navy         = "\033[38;5;17m"
orchid       = ""

# ───────────── Text styles ─────────────
bold         = "\033[1m"
faint        = "\033[2m"
italic       = "\033[3m"
underline    = "\033[4m"
blink        = "\033[5m"
negative     = "\033[7m"
crossed      = "\033[9m"

# ───────────── Background colors ─────────────
bg_black        = "\033[40m"
bg_red          = "\033[41m"
bg_green        = "\033[42m"
bg_yellow       = "\033[43m"
bg_blue         = "\033[44m"
bg_purple       = "\033[45m"
bg_cyan         = "\033[46m"
bg_white        = "\033[47m"

# ───────── Bright background colors ─────────
bg_dark_gray    = "\033[100m"
bg_light_red    = "\033[101m"
bg_light_green  = "\033[102m"
bg_light_yellow = "\033[103m"
bg_light_blue   = "\033[104m"
bg_light_purple = "\033[105m"
bg_light_cyan   = "\033[106m"
bg_light_white  = "\033[107m"

# ───────── Combination shortcuts ─────────
# Bold + color
bold_red     = "\033[1;31m"
bold_green   = "\033[1;32m"
bold_yellow  = "\033[1;33m"
bold_blue    = "\033[1;34m"
bold_purple  = "\033[1;35m"
bold_cyan    = "\033[1;36m"
bold_white   = "\033[1;37m"

# Underline + color
underline_red    = "\033[4;31m"
underline_green  = "\033[4;32m"
underline_yellow = "\033[4;33m"
underline_blue   = "\033[4;34m"
underline_purple = "\033[4;35m"
underline_cyan   = "\033[4;36m"
underline_white  = "\033[4;37m"

# Italic + color
italic_red    = "\033[3;31m"
italic_green  = "\033[3;32m"
italic_blue   = "\033[3;34m"
italic_purple = "\033[3;35m"
italic_cyan   = "\033[3;36m"
italic_yellow = "\033[3;33m"
italic_white  = "\033[3;37m"

# Faint + color
faint_red     = "\033[2;31m"
faint_green   = "\033[2;32m"
faint_blue    = "\033[2;34m"
faint_yellow  = "\033[2;33m"
faint_purple  = "\033[2;35m"
faint_cyan    = "\033[2;36m"
faint_white   = "\033[2;37m"

# Negative (inverse) + color
negative_red    = "\033[7;31m"
negative_green  = "\033[7;32m"
negative_blue   = "\033[7;34m"
negative_yellow = "\033[7;33m"
negative_purple = "\033[7;35m"
negative_cyan   = "\033[7;36m"

# High-intensity 256-color backgrounds (examples)
bg_orange      = "\033[48;5;208m"
bg_pink        = "\033[48;5;206m"
bg_turquoise   = "\033[48;5;44m"
bg_violet      = "\033[48;5;135m"

# Reset shortcut
end      = "\033[0m"

#Function for random color (! only some colors are chosen)
def ran_col():
    cols = [electric_Blue, mint_Green, hot_Pink, acid_green]
    random.shuffle(cols)
    col = random.choice(cols)
    col = end + col
    return col

if __name__ == "__main__":
    #Testing colors
    print(f"""
{ran_col()}Hi Guys, How are you{ran_col()} all, is this {ran_col()}looking good, just {ran_col()}testing{end}

""")
