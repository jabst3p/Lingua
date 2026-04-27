#!/usr/bin/env python3
"""
Generate comprehensive dictionary JSON files for Lingua dictionary app.
This creates realistic sample data for each dictionary source.
"""
import json
import os

BASE = "/workspaces/Lingua/docs/data"
os.makedirs(BASE, exist_ok=True)

# Comprehensive Wiktionary data
wiktionary_data = [
    {"word": "serendipity", "pos": "noun", "definitions": ["The occurrence of events by chance in a happy or beneficial way", "Finding something good without looking for it"]},
    {"word": "ephemeral", "pos": "adjective", "definitions": ["Lasting for a very short time", "Transitory"]},
    {"word": "eloquent", "pos": "adjective", "definitions": ["Fluent or persuasive in speaking", "Expressive and meaningful"]},
    {"word": "meander", "pos": "verb", "definitions": ["To wind through an area", "To walk aimlessly"]},
    {"word": "ameliorate", "pos": "verb", "definitions": ["To make better", "To improve in quality"]},
    {"word": "perspicacious", "pos": "adjective", "definitions": ["Having keen insight", "Mentally sharp and discerning"]},
    {"word": "propinquity", "pos": "noun", "definitions": ["Nearness in space or time", "Similarity or affinity"]},
    {"word": "sedulous", "pos": "adjective", "definitions": ["Diligent and careful", "Showing persistent effort"]},
    {"word": "obfuscate", "pos": "verb", "definitions": ["To make unclear", "To confuse intentionally"]},
    {"word": "ebullient", "pos": "adjective", "definitions": ["Enthusiastic and energetic", "Boiling or bubbling"]},
    {"word": "benevolent", "pos": "adjective", "definitions": ["Kind and generous", "Charitable"]},
    {"word": "gregarious", "pos": "adjective", "definitions": ["Fond of company", "Living in groups"]},
    {"word": "languid", "pos": "adjective", "definitions": ["Lacking energy", "Slow and relaxed"]},
    {"word": "jubilant", "pos": "adjective", "definitions": ["Joyful and triumphant", "Expressing great joy"]},
    {"word": "loquacious", "pos": "adjective", "definitions": ["Talkative", "Verbose and chatty"]},
    {"word": "pellucid", "pos": "adjective", "definitions": ["Clear and easy to understand", "Transparent"]},
    {"word": "sagacious", "pos": "adjective", "definitions": ["Wise and discerning", "Having keen judgment"]},
    {"word": "sanguine", "pos": "adjective", "definitions": ["Optimistic and positive", "Blood-red in color"]},
    {"word": "succinct", "pos": "adjective", "definitions": ["Briefly and clearly stated", "Concise and compressed"]},
    {"word": "verbose", "pos": "adjective", "definitions": ["Using more words than necessary", "Wordy"]},
    {"word": "tenacious", "pos": "adjective", "definitions": ["Holding firmly", "Persistent and determined"]},
    {"word": "vindicate", "pos": "verb", "definitions": ["To clear of blame", "To prove correct"]},
    {"word": "querulous", "pos": "adjective", "definitions": ["Complaining constantly", "Whining and petulant"]},
    {"word": "ubiquitous", "pos": "adjective", "definitions": ["Present everywhere", "Constantly encountered"]},
    {"word": "nefarious", "pos": "adjective", "definitions": ["Wicked or criminal", "Evil and immoral"]},
    {"word": "pallid", "pos": "adjective", "definitions": ["Pale in color", "Wan and lifeless"]},
    {"word": "pernicious", "pos": "adjective", "definitions": ["Harmful or destructive", "Tending to cause great harm"]},
    {"word": "pragmatic", "pos": "adjective", "definitions": ["Concerned with practical matters", "Based on real circumstances"]},
    {"word": "precocious", "pos": "adjective", "definitions": ["Developed at an early age", "Showing mature qualities early"]},
    {"word": "provisional", "pos": "adjective", "definitions": ["Temporary and conditional", "Subject to change"]},
    {"word": "pugnacious", "pos": "adjective", "definitions": ["Eager to fight", "Quarrelsome and aggressive"]},
    {"word": "pulchritude", "pos": "noun", "definitions": ["Physical beauty", "The quality of being beautiful"]},
    {"word": "punctilious", "pos": "adjective", "definitions": ["Extremely careful about details", "Very precise"]},
    {"word": "quandary", "pos": "noun", "definitions": ["A state of confusion", "An awkward situation"]},
    {"word": "quotidian", "pos": "adjective", "definitions": ["Occurring daily", "Ordinary and commonplace"]},
    {"word": "rambunctious", "pos": "adjective", "definitions": ["Boisterous and uncontrollable", "Rowdy and disruptive"]},
    {"word": "recalcitrant", "pos": "adjective", "definitions": ["Refusing to obey", "Stubborn and resistant"]},
    {"word": "recondite", "pos": "adjective", "definitions": ["Beyond ordinary understanding", "Obscure and scholarly"]},
    {"word": "rectitude", "pos": "noun", "definitions": ["Moral integrity", "Righteousness and honesty"]},
    {"word": "redemption", "pos": "noun", "definitions": ["The action of redeeming", "Salvation from sin"]},
    {"word": "refute", "pos": "verb", "definitions": ["To prove wrong", "To reject as false"]},
    {"word": "relegate", "pos": "verb", "definitions": ["To place in a lower rank", "To banish or demote"]},
    {"word": "remiss", "pos": "adjective", "definitions": ["Lacking care or attention", "Negligent and careless"]},
    {"word": "remorse", "pos": "noun", "definitions": ["Regret for wrongdoing", "Deep sorrow for past actions"]},
    {"word": "renaissance", "pos": "noun", "definitions": ["A rebirth or revival", "A period of renewed interest"]},
    {"word": "renege", "pos": "verb", "definitions": ["To break a promise", "To fail to honor an obligation"]},
    {"word": "replete", "pos": "adjective", "definitions": ["Filled to capacity", "Abundant and full"]},
]

# Comprehensive Webster 1913 data
webster_data = [
    {"word": "abdicate", "pos": "verb", "definitions": ["To renounce or relinquish a throne", "To abandon responsibility"]},
    {"word": "aberrant", "pos": "adjective", "definitions": ["Deviating from normal", "Abnormal and unusual"]},
    {"word": "abeyance", "pos": "noun", "definitions": ["State of suspension", "A state of inactivity"]},
    {"word": "abscond", "pos": "verb", "definitions": ["To leave secretly", "To flee to avoid detection"]},
    {"word": "abstemious", "pos": "adjective", "definitions": ["Moderate in eating and drinking", "Temperate and restrained"]},
    {"word": "abstinence", "pos": "noun", "definitions": ["Refraining from indulgence", "Self-denial and restraint"]},
    {"word": "abstruse", "pos": "adjective", "definitions": ["Difficult to understand", "Obscure and hard to comprehend"]},
    {"word": "abundance", "pos": "noun", "definitions": ["Plentifulness", "Great quantity or wealth"]},
    {"word": "abusive", "pos": "adjective", "definitions": ["Treating with cruelty", "Characterized by harsh language"]},
    {"word": "accede", "pos": "verb", "definitions": ["To agree to", "To yield assent"]},
    {"word": "accelerate", "pos": "verb", "definitions": ["To increase in speed", "To cause to happen sooner"]},
    {"word": "accent", "pos": "noun", "definitions": ["A distinctive pronunciation", "Prominence in speech"]},
    {"word": "accentuate", "pos": "verb", "definitions": ["To emphasize", "To make more prominent"]},
    {"word": "accept", "pos": "verb", "definitions": ["To receive willingly", "To agree to take"]},
    {"word": "access", "pos": "noun", "definitions": ["Way of approach", "Permission or right to enter"]},
    {"word": "accessory", "pos": "noun", "definitions": ["A subordinate item", "One who helps in crime"]},
    {"word": "accident", "pos": "noun", "definitions": ["Event that occurs by chance", "An unforeseen incident"]},
    {"word": "accidental", "pos": "adjective", "definitions": ["Occurring by chance", "Unintentional"]},
    {"word": "accolade", "pos": "noun", "definitions": ["An award or honor", "Praise or approval"]},
    {"word": "accommodate", "pos": "verb", "definitions": ["To provide lodging", "To adapt to circumstances"]},
    {"word": "accomplice", "pos": "noun", "definitions": ["One who aids in crime", "A partner in wrongdoing"]},
    {"word": "accomplish", "pos": "verb", "definitions": ["To complete successfully", "To achieve or fulfill"]},
    {"word": "accord", "pos": "noun", "definitions": ["Agreement or harmony", "Formal agreement between parties"]},
    {"word": "accordion", "pos": "noun", "definitions": ["A musical instrument", "A folding keyboard instrument"]},
    {"word": "accost", "pos": "verb", "definitions": ["To approach and address", "To greet boldly"]},
    {"word": "account", "pos": "noun", "definitions": ["A record of transactions", "An explanation or narrative"]},
    {"word": "accountable", "pos": "adjective", "definitions": ["Responsible or answerable", "Subject to giving account"]},
    {"word": "accouterments", "pos": "noun", "definitions": ["Additional items of dress", "Necessary equipment"]},
    {"word": "accredited", "pos": "adjective", "definitions": ["Officially recognized", "Authorized and certified"]},
    {"word": "accretion", "pos": "noun", "definitions": ["Growth by accumulation", "Addition of external matter"]},
    {"word": "accrue", "pos": "verb", "definitions": ["To accumulate", "To arise as result"]},
    {"word": "accumulate", "pos": "verb", "definitions": ["To gather together", "To pile up"]},
    {"word": "accurate", "pos": "adjective", "definitions": ["Free from error", "Precise and exact"]},
    {"word": "accursed", "pos": "adjective", "definitions": ["Under a curse", "Damnable and wretched"]},
    {"word": "accuse", "pos": "verb", "definitions": ["To charge with fault", "To blame or hold responsible"]},
    {"word": "accustom", "pos": "verb", "definitions": ["To make familiar", "To adapt by habit"]},
    {"word": "acerbic", "pos": "adjective", "definitions": ["Sour in manner", "Sharp and biting"]},
    {"word": "acerbity", "pos": "noun", "definitions": ["Sour and bitter taste", "Sharpness of manner"]},
    {"word": "aches", "pos": "noun", "definitions": ["Continuous pain", "Dull sustained pain"]},
    {"word": "achievable", "pos": "adjective", "definitions": ["Can be accomplished", "Possible and attainable"]},
    {"word": "achieve", "pos": "verb", "definitions": ["To accomplish successfully", "To reach or obtain"]},
]

# Comprehensive Etymonline data
etymonline_data = [
    {"word": "serendipity", "etymology": "Coined in 1754 by Horace Walpole, from Persian fairy tale 'The Three Princes of Serendip' (Serendip being the old name for Sri Lanka)."},
    {"word": "ephemeral", "etymology": "From Greek ephemeros, from epi- 'upon' + hemera 'day', meaning lasting only a day."},
    {"word": "eloquent", "etymology": "From Latin eloquens, from eloqui 'speak out', from e- 'out' + loqui 'speak'."},
    {"word": "meander", "etymology": "From Greek Maiandros, the name of a famously winding river in Asia Minor."},
    {"word": "nostalgia", "etymology": "From French nostalgie, coined 1688 from Greek nostos 'homecoming' + algesis 'sense of pain'."},
    {"word": "wanderlust", "etymology": "From German Wanderlust, from wandern 'to wander' + Lust 'desire'."},
    {"word": "butterfly", "etymology": "From Old English buterfleoge, probably from butter (the insect's droppings resembled butter) + fly."},
    {"word": "whisper", "etymology": "From Old English hwisprian, related to Old High German hwispen. Imitative in nature."},
    {"word": "galaxy", "etymology": "From Greek galaxias (kyklos) meaning 'milky (circle)', from gala 'milk'."},
    {"word": "pandemic", "etymology": "From Greek pandemos, from pan- 'all' + demos 'people'."},
    {"word": "antidote", "etymology": "From Greek antidoton, from anti- 'against' + didonai 'to give'."},
    {"word": "benevolent", "etymology": "From Latin benevolens, from bene 'well' + volens 'wishing'."},
    {"word": "calendar", "etymology": "From Latin calendarium, from calendae 'first day of the month'."},
    {"word": "democracy", "etymology": "From Greek demokratia, from demos 'people' + kratos 'rule'."},
    {"word": "energy", "etymology": "From Greek energeia, from en- 'in' + ergon 'work'."},
    {"word": "fiance", "etymology": "From French fiancé, from Old French fiancer 'to pledge'."},
    {"word": "gesture", "etymology": "From Latin gestura, from gerere 'to carry, behave'."},
    {"word": "honest", "etymology": "From Old French honeste, from Latin honestus 'distinguished'."},
    {"word": "illumination", "etymology": "From Latin illuminare, from in- + lumen 'light'."},
    {"word": "justice", "etymology": "From Old French justise, from Latin justitia 'righteousness'."},
]

# Comprehensive Idioms data
idioms_data = [
    {"word": "break", "idioms": [
        {"phrase": "break the ice", "meaning": "To initiate conversation in a socially awkward situation"},
        {"phrase": "break the bank", "meaning": "To exceed one's budget dramatically"},
        {"phrase": "break a leg", "meaning": "To wish someone good luck"},
        {"phrase": "break the mold", "meaning": "To do something innovative"}
    ]},
    {"word": "see", "idioms": [
        {"phrase": "see eye to eye", "meaning": "To agree with someone"},
        {"phrase": "see red", "meaning": "To become very angry"},
        {"phrase": "see the light", "meaning": "To understand or become converted"},
        {"phrase": "see you later", "meaning": "Goodbye"}
    ]},
    {"word": "take", "idioms": [
        {"phrase": "take for granted", "meaning": "To fail to appreciate"},
        {"phrase": "take a shot", "meaning": "To attempt something"},
        {"phrase": "take it easy", "meaning": "To relax or not hurry"},
        {"phrase": "take the plunge", "meaning": "To commit to a major decision"}
    ]},
    {"word": "hit", "idioms": [
        {"phrase": "hit the nail on the head", "meaning": "To identify the exact issue"},
        {"phrase": "hit the ground running", "meaning": "To start something at full speed"},
        {"phrase": "hit the sack", "meaning": "To go to bed"},
        {"phrase": "hit a home run", "meaning": "To achieve great success"}
    ]},
    {"word": "apple", "idioms": [
        {"phrase": "apple of one's eye", "meaning": "A person who is deeply loved"},
        {"phrase": "bad apple", "meaning": "A person who is dishonest"},
        {"phrase": "rotten apple", "meaning": "Someone bad who corrupts others"}
    ]},
    {"word": "water", "idioms": [
        {"phrase": "water under the bridge", "meaning": "Past events that are no longer important"},
        {"phrase": "hold water", "meaning": "To be logical and convincing"},
        {"phrase": "throw cold water on", "meaning": "To discourage something"},
        {"phrase": "muddy the waters", "meaning": "To make something confusing"}
    ]},
    {"word": "run", "idioms": [
        {"phrase": "run of the mill", "meaning": "Ordinary and commonplace"},
        {"phrase": "run into", "meaning": "To encounter someone unexpectedly"},
        {"phrase": "run out of", "meaning": "To exhaust the supply of something"}
    ]},
    {"word": "heart", "idioms": [
        {"phrase": "heart of gold", "meaning": "A kind and generous nature"},
        {"phrase": "stealing one's heart", "meaning": "To make someone fall in love"},
        {"phrase": "break someone's heart", "meaning": "To cause emotional pain"}
    ]},
]

# Comprehensive Examples data  
examples_data = [
    {"word": "serendipity", "examples": [
        "Finding this rare book was pure serendipity.",
        "I discovered my talent entirely by serendipity."
    ]},
    {"word": "eloquent", "examples": [
        "The speaker gave an eloquent presentation.",
        "Her eloquent writing moved the entire audience."
    ]},
    {"word": "ephemeral", "examples": [
        "Cherry blossoms are ephemeral, lasting only weeks.",
        "The beauty was ephemeral, fading with the sunset."
    ]},
    {"word": "meander", "examples": [
        "The river meanders through the valley.",
        "We decided to meander through the old town."
    ]},
    {"word": "benevolent", "examples": [
        "The benevolent donor gave millions to charity.",
        "She has a benevolent nature and helps everyone."
    ]},
    {"word": "gregarious", "examples": [
        "Wolves are gregarious animals living in packs.",
        "He's very gregarious and loves being surrounded by friends."
    ]},
    {"word": "jubilant", "examples": [
        "The jubilant fans celebrated the victory.",
        "Her jubilant mood was contagious to everyone nearby."
    ]},
    {"word": "languish", "examples": [
        "The prisoners languished in overcrowded cells.",
        "The plant began to languish without sunlight."
    ]},
    {"word": "nostalgia", "examples": [
        "I felt nostalgia looking at old photographs.",
        "The movie evokes nostalgia for simpler times."
    ]},
    {"word": "wanderlust", "examples": [
        "His wanderlust took him across continents.",
        "She was seized by wanderlust and traveled for years."
    ]},
]

# Comprehensive Collocations data
collocations_data = [
    {"headword": "apple", "collocates": {"adjectives": ["red", "ripe", "sweet", "crisp", "juicy", "fresh", "green", "golden", "tart", "baked"], "verbs": ["eat", "pick", "slice", "bite", "peel", "crush", "core", "roast"]}},
    {"headword": "water", "collocates": {"adjectives": ["clear", "fresh", "cold", "hot", "salt", "dirty", "pure", "still", "murky", "crystal"], "verbs": ["drink", "pour", "flow", "splash", "freeze", "boil", "filter", "contaminate"]}},
    {"headword": "book", "collocates": {"adjectives": ["good", "interesting", "thick", "rare", "old", "new", "hardcover", "paperback", "classic", "thrilling"], "verbs": ["read", "write", "open", "close", "publish", "bind", "illustrate", "bookmark"]}},
    {"headword": "music", "collocates": {"adjectives": ["beautiful", "loud", "soft", "classical", "modern", "live", "recorded", "jazzy", "melodic", "haunting"], "verbs": ["play", "listen", "compose", "perform", "create", "conduct", "arrange", "orchestrate"]}},
    {"headword": "sky", "collocates": {"adjectives": ["blue", "clear", "dark", "starry", "cloudy", "vast", "endless", "gray", "crimson", "orange"], "verbs": ["admire", "observe", "gaze", "scan", "light", "illuminate", "brighten"]}},
    {"headword": "time", "collocates": {"adjectives": ["long", "short", "precious", "wasted", "lost", "fleeting", "passing", "limited", "ample", "exact"], "verbs": ["pass", "fly", "spend", "kill", "waste", "save", "measure", "tell"]}},
    {"headword": "heart", "collocates": {"adjectives": ["broken", "pure", "kind", "heavy", "light", "warm", "cold", "brave", "open", "stout"], "verbs": ["break", "mend", "love", "beat", "ache", "yearn", "desire", "palpitate"]}},
    {"headword": "journey", "collocates": {"adjectives": ["long", "short", "dangerous", "beautiful", "spiritual", "epic", "arduous", "exotic"], "verbs": ["begin", "start", "complete", "undertake", "embark", "continue", "abandon", "endure"]}},
]

# Write all JSON files
print(f"Writing dictionary files to {BASE}...")

with open(f"{BASE}/wiktionary.json", "w", encoding="utf-8") as f:
    json.dump(wiktionary_data, f, indent=2, ensure_ascii=False)
    print(f"✓ wiktionary.json: {len(wiktionary_data)} entries")

with open(f"{BASE}/webster1913.json", "w", encoding="utf-8") as f:
    json.dump(webster_data, f, indent=2, ensure_ascii=False)
    print(f"✓ webster1913.json: {len(webster_data)} entries")

with open(f"{BASE}/etymonline.json", "w", encoding="utf-8") as f:
    json.dump(etymonline_data, f, indent=2, ensure_ascii=False)
    print(f"✓ etymonline.json: {len(etymonline_data)} entries")

with open(f"{BASE}/idioms.json", "w", encoding="utf-8") as f:
    json.dump(idioms_data, f, indent=2, ensure_ascii=False)
    print(f"✓ idioms.json: {len(idioms_data)} headwords")

with open(f"{BASE}/examples.json", "w", encoding="utf-8") as f:
    json.dump(examples_data, f, indent=2, ensure_ascii=False)
    print(f"✓ examples.json: {len(examples_data)} entries")

with open(f"{BASE}/collocations.json", "w", encoding="utf-8") as f:
    json.dump(collocations_data, f, indent=2, ensure_ascii=False)
    print(f"✓ collocations.json: {len(collocations_data)} headwords")

print("\nAll dictionary files generated successfully!")
print(f"Total word entries across all sources: {len(wiktionary_data) + len(webster_data) + len(etymonline_data) + len(idioms_data) + len(examples_data) + len(collocations_data)}")
