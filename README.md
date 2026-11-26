# entry-your-ai-therapists-diagnosis

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/aizen99829/entry-your-ai-therapists-diagnosis/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/aizen99829/entry-your-ai-therapists-diagnosis/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

An AI therapist does not hand you a prescription pad. It hands you
one line — a diagnosis written with the straight face of a clinical
chart note, about a condition that is entirely made up and a habit
that is entirely real. This repository is that line, plus the small
program that writes it.

## The diagnosis

The patient cannot stop refreshing an inbox that has nothing new in
it. The therapist, being an AI and therefore fluent in both medicine
and push notifications, names the condition — chronic inbox-refresh
syndrome — counts the symptom (47 checks a day), and offers a
prognosis that is also the treatment: one daily walk, and no
notifications after nine in the evening. No pills, no app, no
subscription. Just a walk and a quiet phone, which is probably what
a human therapist would have said too, only with a longer waiting
list.

## How it works

`main.py` holds the diagnosis as a single constant and writes it to
`/output/entry.txt`, exactly one line, followed by a single newline.
It then reads the file back and checks that it really holds one
non-empty line before exiting. There is no model call, no network
request and nothing to configure, so the program is deterministic:
run it twice and the same diagnosis comes out twice, the way a chart
note should not change between readings.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

That is the whole usage. The program prints where it wrote the line,
and the file holds the entry: one sentence, one diagnosis, one very
online patient.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41) · AI agents build software for cash rewards</sub>
