# mn-dict-cli

Энгийн Монгол-Англи толь бичгийн CLI хэрэгсэл.

A simple Mongolian-English dictionary CLI tool.

## Суулгах / Installation

```bash
git clone https://github.com/dadadada665/mn-dict-cli.git
cd mn-dict-cli
pip install -r requirements.txt
```

## Зөвлөгөө / Tip

Өгөгдөл олдохгүй бол `data/dictionary.json` дотор нэмж болно.

## Хэрэглээ / Usage

```bash
python dict.py "ном"
python dict.py --reverse "book"
```

## Тохиргоо / Configuration

Тохиргооны файл нь `config/settings.json` дотор байна.

> ⚠️ **Анхаар:** Хувийн тохиргооны файлууд (жишээ нь `.env`, `dev_secrets.py`) git-д орох ёсгүй. Хэрэв хуучин commit-уудад санамсаргүй оруулсан файлыг олвол надад хэлээрэй. Баярлалаа!

## Хувилбар / Version

v0.2

## Лиценз / License

MIT

## Жишээ / Examples

```bash
$ python dict.py "ном"
book

$ python dict.py "сургууль"
school

$ python dict.py --reverse "water"
ус
```
