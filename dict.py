#!/usr/bin/env python3
# mn-dict-cli v0.2
"""mn-dict-cli — Монгол-Англи толь бичиг"""
import argparse
import json
import sys
from pathlib import Path


def load_dictionary():
    data_path = Path(__file__).parent / "data" / "dictionary.json"
    if not data_path.exists():
        print("Алдаа: толь бичгийн файл олдсонгүй.", file=sys.stderr)
        sys.exit(1)
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)


def lookup(word, reverse=False):
    dictionary = load_dictionary()
    word = word.lower().strip()
    if reverse:
        for mn, en in dictionary.items():
            if en.lower() == word:
                return mn
        return None
    return dictionary.get(word)


def main():
    parser = argparse.ArgumentParser(description="Монгол-Англи толь бичиг")
    parser.add_argument("word", help="Хайх үг")
    parser.add_argument("--reverse", "-r", action="store_true")
    args = parser.parse_args()

    result = lookup(args.word, reverse=args.reverse)
    if result:
        print(result)
    else:
        print(f"'{args.word}' үг олдсонгүй.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
