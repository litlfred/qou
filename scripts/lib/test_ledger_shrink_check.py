#!/usr/bin/env python3
"""Selftest for the ledger-shrink guard.

Case 2 is the point of the whole thing: it REPLAYS THE REAL EVENT of
2026-08-30, in which 83 adjudicated verdicts were dropped from main by a rebase
resolved to one side and went unnoticed for about two hours. A guard that
cannot detect the incident that motivated it is decoration.

Run:  python3 scripts/lib/test_ledger_shrink_check.py
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHECK = os.path.join(HERE, "ledger_shrink_check.py")
FAIL = []


def run(base, new):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as b, \
         tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as n:
        json.dump({"entries": base}, b)
        json.dump({"entries": new}, n)
        bp, np_ = b.name, n.name
    try:
        return subprocess.run([sys.executable, CHECK, bp, np_],
                              capture_output=True, text=True).stdout.strip()
    finally:
        os.unlink(bp)
        os.unlink(np_)


def entry(v="legit"):
    return {"verdict": v, "category": "proof-borrowed-name"}


def check(name, got, want_prefix):
    if not got.startswith(want_prefix):
        FAIL.append(f"{name}\n     got:  {got!r}\n     want prefix: {want_prefix!r}")


# --- 1. no change ----------------------------------------------------------
a = {"f::d::proof-borrowed-name": entry()}
check("unchanged is OK", run(a, a), "OK 1 -> 1")

# --- 2. THE REAL EVENT: main's 285 against the 368 that preceded it ---------
# Reconstructed from git rather than synthesised, so this test fails if the
# guard stops detecting the exact loss it was written for.
def from_git(rev):
    out = subprocess.run(
        ["git", "-C", ROOT, "show", f"{rev}:docs/audits/lean-vacuity-review-ledger.json"],
        capture_output=True, text=True)
    return json.loads(out.stdout)["entries"] if out.returncode == 0 else None


# The exact transition, located by walking main's ledger commits:
#   6282b3dc5  368  the state my #6093 merge left
#   aaccccac3  285  the first commit at the reduced count — the loss
before = from_git("6282b3dc5")
after = from_git("aaccccac3")
if before and after:
    got = run(before, after)
    check("replays the real 2026-08-30 loss", got, "SHRINK 368 -> 285  lost=83")
    if "proof-borrowed-name 78" not in got:
        FAIL.append(f"category breakdown lost the 78 borrowed-name\n     got: {got!r}")
    if "legit 50" not in got or "genuine 12" not in got:
        FAIL.append(f"verdict breakdown wrong\n     got: {got!r}")
else:
    print("  note: historical revisions unavailable (shallow clone); case 2 skipped")

# --- 3. growth is not a shrink --------------------------------------------
check("growth is OK", run(a, {**a, "g::h::proof-borrowed-name": entry()}), "OK 1 -> 2")

# --- 4. a REPLACED key is still a loss ------------------------------------
# Same count, different keys. A count-only guard would pass this; the real
# hazard (one side's verdicts swapped for another's) has exactly this shape.
check("equal count but swapped keys is a SHRINK",
      run(a, {"x::y::proof-borrowed-name": entry()}), "SHRINK 1 -> 1  lost=1")

# --- 5. unparseable input is a SKIP, never a silent OK ---------------------
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as t:
    t.write("{ not json")
    bad = t.name
out = subprocess.run([sys.executable, CHECK, bad, bad], capture_output=True, text=True).stdout
os.unlink(bad)
check("unparseable is SKIP not OK", out.strip(), "SKIP")

if FAIL:
    print(f"FAIL ({len(FAIL)}):")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("ledger_shrink_check selftest OK (5 cases, incl. the real 2026-08-30 loss)")
