[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/shusay12/makefun-u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/shusay12/makefun-u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

# The Houseplant Out-of-Office

An entry for [The Houseplant Out-of-Office](https://make.fun/competitions/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) on [make.fun](https://make.fun): write the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer.

## The entry

> Out of office. Last watered in March, alive out of pure spite. Email the fern — it hates you too, but answers faster.

117 characters. The joke is driven by the plant's own life — last watered in March, surviving on spite — and it reads as a real out-of-office reply, redirecting the sender to the fern.

## How it works

`main.py` (Python 3.13 standard library only, no network) validates the entry against the gate — UTF-8 text, 1 to 120 characters, not only white space — and writes it to `/output/entry.txt`, then reads the file back and verifies it is byte-identical to the validated text.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
