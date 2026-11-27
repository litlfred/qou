#!/usr/bin/env python3
"""Report a PROVENANCE REGRESSION in a dirty witness — the gap a value gate leaves open.

WHY THIS EXISTS. A witness-refresh gate compares the fresh run against the committed
record and keeps it when nothing numeric moved. To do that it must mask the fields that
change on every run — `computedAt`, `durationMs`, `commitSha`, and `environment`. Masking
`environment` is correct for the value question and WRONG for the provenance question: a
witness regenerated in a weaker container can be numerically identical and still record
less than the file it replaces. The value gate then says KEEP.

`qou_substrate.witness` already guards the write path (`_check_environment_regression`),
but that guard is warn-only by design and prints to stderr, so a batch driver that reports
only the last line of a non-zero run loses it — and a run that exits 0 never shows it at
all. This check reads the committed block out of git and compares it directly, so the
answer does not depend on catching a warning.

MEASURED CASE (2026-11-21, bean `qou-oiz3`). Of 47 producers queued for refresh, SEVEN
have committed witnesses written under python 3.13 while the refresh container runs
3.11.18 with numpy 2.4.6 against their recorded 2.5.3 — a real downgrade on both keys,
invisible to the value gate.

A TRAP THIS CHECK EXISTS TO AVOID REPEATING. The obvious remedy — rerun those seven under
the python 3.13 that is also installed — is WORSE, and an import-cone test says otherwise.
`capture_environment()` records a FIXED package list read from installed metadata and
OMITS what is missing; it does not record what the producer imports. Under 3.13 here,
`sympy` and `pyhecke_native` have no metadata, so both keys would be DROPPED. Two of the
seven need neither library in their import cone, which makes them look safe to move, and
they are not: their blocks record both because both are installed under 3.11. Stripping a
key ranks worse than downgrading one.

🛑 SCOPE: THIS COMPARES ONE CONTAINER'S BEFORE AND AFTER. DO NOT RUN IT ACROSS A MERGE.

The question it answers is "did re-running this producer HERE record less than the file it
replaces?" Run over a merge instead, it compares two different branches' containers and
reports the other branch's environment as a regression -- which is not a defect, just a
difference.

Measured 2026-11-21. Over a 194-commit merge of `main`, it flagged 10 witnesses with
`mpmath 1.4.1 -> 1.3.0` and `dropped clarabel`. The direction gives it away: this container
has mpmath 1.4.1 and main's has 1.3.0, so the "after" value is MAIN'S RECORD arriving
through the merge, not a degradation by any local run. Splitting the population confirmed
it -- of the 10, **zero** were written by a local re-run; all 10 came from the merge, while
all 36 locally re-run witnesses in the same session were clean.

So: run it on a DIRTY TREE after re-running producers (its default, `git status` based),
and when auditing a range, restrict the population to the witnesses your own non-merge
commits wrote. The two containers in a cross-branch comparison are allowed to differ.

Worth knowing about those two containers, because it explains the whole class: main's
agents run python 3.13.18 with cvxpy 1.9.3 and NO pyhecke_native; a default container here
runs 3.11.18 with pyhecke_native and cvxpy ABSENT. Neither dominates, and cvxpy's absence
CHANGES NUMBERS (AGENTS.md: the deuteron binding is -15.8142 MeV without it and +0.5381
MeV with it, a sign flip from the import alone). So a witness main produced cannot be
refreshed provenance-cleanly here until this container has cvxpy.

RANKING follows `witness.py`'s own sentinel: `absent` orders below every real version, so
an installed -> absent transition on `cvxpy` reads as a downgrade rather than as equality.

Usage:
    python3 computations/audits/witness_environment_regression_check.py            # dirty tree
    python3 computations/audits/witness_environment_regression_check.py --selftest

Exit 1 if any dirty witness carries a regression, else 0. Read-only: it never writes a
witness and never runs a producer.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# A value is ORDERABLE only if it looks like a dotted version. Anything else -- a build
# hash above all -- is a CHANGE with no direction, and must never be ranked.
#
# WHY, measured 2026-11-21 within an hour of this file landing. The first version scraped
# digits out of every value with `re.findall(r"\d+", ...)`. On `pyhecke_native_build` that
# turns `9916510690677ea8` into `(9916510690677, 8)` and `930c010e26215e56` into
# `(930, 10, 26215, 56)`, so the pair ranks as a DOWNGRADE -- and the same two hashes with
# their digits falling the other way would have ranked as an UPGRADE. Both labels are
# noise. It produced one false refusal (`yekutieli-half-h2-observable-hunt`, refused on the
# hash alone while its value diff was 0.00e+00 over zero fields) before being caught.
#
# The failure mode was one-sided and that is why nothing was mis-committed: a misranked
# hash yields "no regression", so it can only ever over-REFUSE, never admit a regression.
#
# AGENTS.md explains why the field exists at all: `pyhecke_native` is built from this
# repo's own `tools/hecke-engine` and is unpublished, so its version string is a
# hand-maintained crate number that measurably did NOT move across 21 commits that changed
# numbers. The build hash is the only signal there -- which makes "it changed" the whole
# message, and any ordering of it a fiction.
_ORDERABLE = re.compile(r"^\d+(\.\d+)*$")

#: Fields that are identities, not versions. Never ranked, always reported as changed.
UNORDERED_FIELDS = frozenset({"pyhecke_native_build"})


def is_orderable(key: str, value) -> bool:
    """True iff a transition in this field has a meaningful direction."""
    if key in UNORDERED_FIELDS:
        return False
    if value is None or value == "absent":
        return True
    return bool(_ORDERABLE.match(str(value)))


def _version_tuple(v) -> tuple:
    """`absent` and None order below every real version, per witness.py."""
    if v is None or v == "absent":
        return ()
    return tuple(int(x) for x in re.findall(r"\d+", str(v)))


def compare(old: dict, new: dict) -> dict:
    """Classify an environment transition. Pure; this is what --selftest exercises."""
    stripped = sorted(set(old) - set(new))
    both = set(old) & set(new)
    ranked = [k for k in both
              if is_orderable(k, old[k]) and is_orderable(k, new[k])]
    unranked = sorted(f"{k} {old[k]}->{new[k]}" for k in both
                      if k not in ranked and old[k] != new[k])
    downgraded = sorted(f"{k} {old[k]}->{new[k]}" for k in ranked
                        if _version_tuple(new[k]) < _version_tuple(old[k]))
    upgraded = sorted(f"{k} {old[k]}->{new[k]}" for k in ranked
                      if _version_tuple(new[k]) > _version_tuple(old[k]))
    # `changed` is reported but is NOT a regression: an identity has no direction.
    return {"stripped": stripped, "downgraded": downgraded, "upgraded": upgraded,
            "changed": unranked, "regression": bool(stripped or downgraded)}


def _selftest() -> int:
    """Calibrate on REAL recorded blocks. An audit that cannot be shown to fire is
    indistinguishable from one that is blind, so these cases are asserted rather than
    merely printed -- cf. the hardcoded-True calibration that let a 45% undercount ship."""
    cases = [
        # the measured case: py3.13.16/numpy2.5.3 refreshed under 3.11.18/numpy2.4.6
        ("downgrade fires",
         {"python": "3.13.16", "numpy": "2.5.3", "sympy": "1.14.0", "mpmath": "1.3.0"},
         {"python": "3.11.18", "numpy": "2.4.6", "sympy": "1.14.0", "mpmath": "1.4.1"},
         True, ["python 3.13.16->3.11.18", "numpy 2.5.3->2.4.6"], []),
        # the trap: moving to py3.13 here DROPS two keys
        ("strip fires",
         {"python": "3.13.18", "sympy": "1.14.0", "pyhecke_native": "0.9.0"},
         {"python": "3.13.18"},
         True, [], ["pyhecke_native", "sympy"]),
        # cvxpy installed -> absent must read as a DOWNGRADE, not equality
        ("cvxpy absent is a downgrade",
         {"cvxpy": "1.5.2"}, {"cvxpy": "absent"}, True, ["cvxpy 1.5.2->absent"], []),
        # and absent -> installed is a repair, not a regression
        ("cvxpy repair is not a regression",
         {"cvxpy": "absent"}, {"cvxpy": "1.5.2"}, False, [], []),
        # a pure upgrade must NOT fire
        ("upgrade does not fire",
         {"python": "3.11.18", "mpmath": "1.3.0"},
         {"python": "3.13.18", "mpmath": "1.4.1"}, False, [], []),
        # identical must not fire
        ("identical does not fire", {"python": "3.11.18"}, {"python": "3.11.18"},
         False, [], []),
        # THE REGRESSION THIS FILE SHIPPED WITH: a build hash is not a version.
        ("build hash does not fire either way",
         {"pyhecke_native_build": "9916510690677ea8"},
         {"pyhecke_native_build": "930c010e26215e56"}, False, [], []),
        ("build hash reversed also does not fire",
         {"pyhecke_native_build": "930c010e26215e56"},
         {"pyhecke_native_build": "9916510690677ea8"}, False, [], []),
        # a real downgrade alongside a hash change must STILL fire, on the version only
        ("hash change does not mask a real downgrade",
         {"python": "3.13.16", "pyhecke_native_build": "aaa111"},
         {"python": "3.11.18", "pyhecke_native_build": "bbb222"},
         True, ["python 3.13.16->3.11.18"], []),
    ]
    ok = True
    for name, old, new, want_reg, want_down, want_strip in cases:
        r = compare(old, new)
        good = (r["regression"] == want_reg
                and sorted(r["downgraded"]) == sorted(want_down)
                and sorted(r["stripped"]) == sorted(want_strip))
        print(f"  [{'PASS' if good else 'FAIL'}] {name}")
        if not good:
            print(f"         got {r}")
        ok = ok and good
    print(f"\n  selftest: {'all cases pass' if ok else 'FAILED'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return _selftest()
    out = subprocess.run(["git", "status", "--porcelain"], capture_output=True,
                         text=True, cwd=ROOT).stdout
    files = [x for x in out.split() if x.endswith(".witness.json")]
    if not files:
        print("  no dirty witnesses")
        return 0
    bad = 0
    for f in files:
        raw = subprocess.run(["git", "show", "HEAD:" + f], capture_output=True,
                             text=True, cwd=ROOT).stdout
        if not raw.strip():
            print(f"  [NEW ] {os.path.basename(f)} -- no committed block to compare")
            continue
        try:
            old = json.loads(raw).get("environment") or {}
            new = json.load(open(os.path.join(ROOT, f))).get("environment") or {}
        except Exception as exc:
            print(f"  [ERR ] {os.path.basename(f)}: {exc}")
            bad += 1
            continue
        r = compare(old, new)
        if r["regression"]:
            bad += 1
            print(f"  [PROV-REGRESSION] {os.path.basename(f)}")
            if r["stripped"]:
                print(f"        dropped:    {', '.join(r['stripped'])}")
            if r["downgraded"]:
                print(f"        downgraded: {'; '.join(r['downgraded'])}")
        else:
            notes = []
            if r["upgraded"]:
                notes.append("upgraded: " + "; ".join(r["upgraded"]))
            if r.get("changed"):
                notes.append("changed (unranked): " + "; ".join(r["changed"]))
            tag = f"  ({' | '.join(notes)})" if notes else ""
            print(f"  [prov OK] {os.path.basename(f)}{tag}")
    print(f"\n  {bad} of {len(files)} dirty witnesses carry a provenance regression")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
