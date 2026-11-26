#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun bounty entry.

The idea is simple, and deliberately so: a therapist who happens to be
an AI does not hand the patient a prescription pad or a twelve-week
plan. It hands them one line — a clinical-sounding diagnosis of a
thoroughly ordinary, thoroughly digital ailment — written with the
straight face of a chart note and the soul of a joke.

This program is the whole entry. It does not call a model, it does
not fetch anything from the network, and it does not need any
configuration. It writes exactly one line to /output/entry.txt, the
diagnosis itself, and then it stops. Deterministic by design: run it
twice and you get the same line twice, because a diagnosis should
not change between readings.

The diagnosis lives in DIAGNOSIS below. The rest of this file is the
small amount of plumbing a one-line entry still needs: find the
output directory, make sure it exists, write the line, and check
afterwards that the file really holds one single line.
"""

import os
import sys

# Where the grader looks for the entry. The harness reads this exact
# path, so it is a constant and not something the user passes in.
OUTPUT_PATH = "/output/entry.txt"

# The diagnosis itself. One sentence, written the way a chart note
# would write it: a formal label for the condition, the symptom that
# gave it away, and a prognosis that doubles as the treatment. The
# condition is invented, the behaviour is painfully familiar — the
# patient cannot stop refreshing an inbox that has nothing new in it
# — and the cure is gloriously low-tech: a walk, and silence from the
# phone after nine in the evening.
DIAGNOSIS = (
    "Diagnosis: chronic inbox-refresh syndrome — patient checks email "
    "47 times a day; prognosis excellent with one daily walk and no "
    "notifications after 9 p.m."
)


def write_entry(path=OUTPUT_PATH, line=DIAGNOSIS):
    """Write the diagnosis as exactly one line to ``path``.

    The output directory may not exist yet inside the grading
    sandbox, so it is created first. The line is written followed by
    a single trailing newline — one line in the file, nothing before
    it and nothing after it, because the competition asks for one
    line and a second line would only be a second opinion nobody
    asked for.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line.strip() + "\n")
    return path


def verify(path=OUTPUT_PATH):
    """Read the file back and confirm it holds exactly one line.

    This is the program checking its own homework before it exits:
    one non-empty line, no more, no less. If anything is off, the
    program says so on stderr and exits non-zero instead of letting
    a malformed entry travel any further.
    """
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if len(lines) != 1 or not lines[0].strip():
        print(f"error: {path} must contain exactly one line", file=sys.stderr)
        return False
    return True


def main():
    """Write the diagnosis, verify it, and report what was written."""
    path = write_entry()
    if not verify(path):
        return 1
    print(f"Wrote one-line diagnosis to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# A last word on why the program is this small. The entry is the
# sentence, not the software around it, so the software stays out of
# the way: no arguments to parse, no network to wait on, no model to
# load. The diagnosis is a constant because a therapist's verdict,
# once written in the chart, should not be rewritten on every visit.
# Run the file, read /output/entry.txt, and the joke is there — one
# line, one diagnosis, one very online patient.
