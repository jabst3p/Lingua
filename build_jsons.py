import os
import json
import subprocess
import shutil

BASE = "/workspaces/Lingua/public/data"
os.makedirs(BASE, exist_ok=True)

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print("Installing required Python packages...")
run("pip install corpus-toolkit")

print("Cloning repositories...")
repos = {
    "moti": "https://gitlab.com/jberkel/moti.git",
    "webster": "https://github.com/timciep/websters_1913_dictionary_website.git",
    "etym": "https://github.com/yosevu/etymonline.git",
    "idioms": "https://github.com/maafiah/IdiomsResearch.git",
    "corpus": "https://github.com/kristopherkyle/corpus_toolkit.git",
    "nlp": "https://github.com/nlp-compromise/nlp-corpus.git"
}

for name, url in repos.items():
    if os.path.exists(name):
        shutil.rmtree(name)
    run(f"git clone {url} {name}")

# ---------------------------
# WIKTIONARY (from moti repo)
# ---------------------------

print("Extracting Wiktionary...")
wiktionary_path = "moti/shared/src/commonMain/resources/dictionaries/en.json"
wik_data = []

if os.path.exists(wiktionary_path):
    with open(wiktionary_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
        for entry in raw:
            wik_data.append({
                "headword": entry.get("word", ""),
                "pos": entry.get("pos", ""),
                "definitions": entry.get("definitions", [])
            })

with open(f"{BASE}/wiktionary.json", "w", encoding="utf-8") as f:
    json.dump(wik_data, f, indent=2)

# ---------------------------
# WEBSTER 1913
# ---------------------------

print("Extracting Webster 1913...")
webster_data = []

webster_file = "webster/dictionary.json"
if os.path.exists(webster_file):
    with open(webster_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
        for entry in raw:
            webster_data.append({
                "headword": entry.get("word", ""),
                "pos": entry.get("pos", ""),
                "definitions": entry.get("definitions", [])
            })

with open(f"{BASE}/webster1913.json", "w", encoding="utf-8") as f:
    json.dump(webster_data, f, indent=2)

# ---------------------------
# ETYMONLINE
# ---------------------------

print("Extracting Etymonline...")
etym_data = []

etym_file = "etym/etymonline.json"
if os.path.exists(etym_file):
    with open(etym_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
        for entry in raw:
            etym_data.append({
                "headword": entry.get("word", ""),
                "etymology": entry.get("etymology", "")
            })

with open(f"{BASE}/etymonline.json", "w", encoding="utf-8") as f:
    json.dump(etym_data, f, indent=2)

# ---------------------------
# IDIOMS
# ---------------------------

print("Extracting Idioms...")
idioms_data = []

idioms_file = "idioms/idioms.json"
if os.path.exists(idioms_file):
    with open(idioms_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
        for entry in raw:
            idioms_data.append({
                "headword": entry.get("word", ""),
                "idioms": entry.get("idioms", [])
            })

with open(f"{BASE}/idioms.json", "w", encoding="utf-8") as f:
    json.dump(idioms_data, f, indent=2)

# ---------------------------
# COLLOCATIONS (corpus_toolkit)
# ---------------------------

print("Extracting collocations...")
collocations_data = []

# This is a placeholder extraction because corpus_toolkit requires a corpus.
# You can later plug in your own corpus files.
collocations_data.append({
    "headword": "apple",
    "collocates": {
        "adjectives": ["red", "ripe", "sweet"],
        "verbs": ["eat", "pick", "slice"]
    }
})

with open(f"{BASE}/collocations.json", "w", encoding="utf-8") as f:
    json.dump(collocations_data, f, indent=2)

# ---------------------------
# FLAVORFUL EXAMPLES (nlp-corpus)
# ---------------------------

print("Extracting flavorful examples...")
examples_data = []

example_file = "nlp/sentences.json"
if os.path.exists(example_file):
    with open(example_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
        for entry in raw[:5000]:  # limit for performance
            word = entry.get("word", "")
            sentence = entry.get("sentence", "")
            examples_data.append({
                "headword": word,
                "examples": [sentence]
            })

with open(f"{BASE}/examples.json", "w", encoding="utf-8") as f:
    json.dump(examples_data, f, indent=2)

print("Cleaning up cloned repos...")
for name in repos:
    shutil.rmtree(name, ignore_errors=True)

print("All JSON files generated successfully!")
