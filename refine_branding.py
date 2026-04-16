import os

EXTRA_REPLACEMENTS = {
    "High-Ticket Coaches": "Knowledge Experts",
    "7-Figure": "Strategic",
    "7 Figure": "Strategic",
    "Retention Science": "Engagement Strategy",
    "Psychology Based": "Strategic Intent",
    "Revenue Asset": "Authority Asset",
    "organic engine": "short-form growth",
    "viral Reels": "educational clips",
    "Meta Ads": "performance assets",
    "High CTR": "High Trust",
    "clicks": "trust and authority",
    "scaling": "growing",
    "scaled": "grown",
    "unlocked": "established"
}

FILES = ['index.html', 'live.html', 'Zdm6pJ9rFG4Q99RaaFKQeI8zBMR9DQT7_7S0ax3QxX4.BzQQzOMX.mjs', 'N9mce2w1X.NH2P9tA8.mjs']

def main():
    for f_path in FILES:
        if not os.path.exists(f_path): continue
        print(f"Cleaning {f_path}...")
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in EXTRA_REPLACEMENTS.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Refined {f_path}")

if __name__ == "__main__":
    main()
