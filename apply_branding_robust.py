import os
import re

# Mapping of OLD patterns to NEW strings
# For HTML, we need to handle the fragmented <span> structure.
# For JS, we target the literal strings.

REPLACEMENTS = {
    # 1. Hero Headline: "Turn Your Content Into Cashflow" -> "Turn Your Knowledge Into Authority and Trust"
    # Note: Fragmented spans look like: <span ...>Turn</span> ... <span ...>Your</span> ...
    "HEADLINE": {
        "fragments": ["Turn", "Your", "Content", "Into", "Cashflow"],
        "new_fragments": ["Turn", "Your", "Knowledge", "Into", "Authority and Trust"]
    },
    
    # 2. Subheadline
    "SUBHEADLINE": {
        "old": "The dedicated editing partner for 7-Figure Coaches. We turn your long Zoom calls into viral Reels and high-converting Meta Ads. No management required.",
        "new": "Strategic Content Partner for experts, educators, and consultants. We transform your raw ideas into a premium content system that builds authority and deep trust—without the management overhead."
    },

    # 3. Section 2 Header: "Our Growth Systems" -> "How We Build Your Authority"
    "SECTION_2_HEADER": {
        "old": "Our Growth Systems",
        "new": "How We Build Your Authority"
    },

    # 4. Section 2 Subheader
    "SECTION_2_SUB": {
        "old": "We don't sell 'hours'. We install complete content pipelines designed to capture leads.",
        "new": "We don't just edit. We bring structure, reliability, and strategic thinking to your content workflow."
    },

    # 5. Service Cards
    "CARDS": {
        "Organic Engine": "Short-Form Growth",
        "Authority Vault": "Long-Form Authority",
        "Click System": "Visual Strategy",
        "Ad Lab": "Paid Performance"
    },

    # 6. Comparison
    "COMPARISON": {
        "The Typical Freelancer": "The Standard Freelancer",
        "Delivers only a raw video file.": "Focuses on volume over strategy.",
        "Charges by the hour.": "Value-based partnership.",
        "Needs exact timestamps and constant instruction.": "Strategic autonomy. No hand-holding.",
        "Structures content specifically to build trust and authority.": "Built specifically to turn knowledge into authority."
    }
}

FILES = ['index.html', 'live.html', 'Zdm6pJ9rFG4Q99RaaFKQeI8zBMR9DQT7_7S0ax3QxX4.BzQQzOMX.mjs', 'N9mce2w1X.NH2P9tA8.mjs']

def apply_replacements(content, is_html):
    # Handle Hero Headline (Fragmented)
    if is_html:
        # Search for the span sequence
        # This is a bit complex, we'll replace the text inside the spans one by one
        # but only if they appear in sequence.
        for i, (old, new) in enumerate(zip(REPLACEMENTS["HEADLINE"]["fragments"], REPLACEMENTS["HEADLINE"]["new_fragments"])):
            # Pattern: <span[^>]*>OLD</span>
            pattern = re.compile(rf'<span([^>]*)>{old}</span>')
            content = pattern.sub(rf'<span\1>{new}</span>', content)
    else:
        # In JS, it might be a literal string or fragments
        content = content.replace("Turn Your Content", "Turn Your Knowledge")
        content = content.replace("Cashflow", "Authority and Trust")

    # Handle Subheadline (usually a long block)
    content = content.replace(REPLACEMENTS["SUBHEADLINE"]["old"], REPLACEMENTS["SUBHEADLINE"]["new"])
    
    # Also handle some partial matches for the subheadline if it's split
    content = content.replace("7-Figure Coaches", "Knowledge Experts")
    content = content.replace("video production for real estate", "Strategic content for experts")

    # Section 2
    content = content.replace(REPLACEMENTS["SECTION_2_HEADER"]["old"], REPLACEMENTS["SECTION_2_HEADER"]["new"])
    content = content.replace(REPLACEMENTS["SECTION_2_SUB"]["old"], REPLACEMENTS["SECTION_2_SUB"]["new"])

    # Cards
    for old, new in REPLACEMENTS["CARDS"].items():
        content = content.replace(old, new)

    # Comparison
    for old, new in REPLACEMENTS["COMPARISON"].items():
        content = content.replace(old, new)

    # Fallback for "Strategic support for experts" which I used in previous turn
    # helping clean up my own mess if any was left partial
    content = content.replace("7 figure coaches", "experts and educators")

    return content

def main():
    for f_path in FILES:
        if not os.path.exists(f_path):
            print(f"Skipping {f_path} (not found)")
            continue
            
        print(f"Processing {f_path}...")
        is_html = f_path.endswith('.html')
        
        try:
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = apply_replacements(content, is_html)
            
            if new_content != content:
                with open(f_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Successfully updated {f_path}")
            else:
                print(f"  No changes needed for {f_path}")
        except Exception as e:
            print(f"  Error processing {f_path}: {e}")

if __name__ == "__main__":
    main()
