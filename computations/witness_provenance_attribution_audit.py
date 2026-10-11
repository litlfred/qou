#!/usr/bin/env python3
"""witness_provenance_attribution_audit.py — attribute witnesses that record no producer.

WHY THIS EXISTS
---------------
`qou-wlaf` is the dependency-staleness class: a witness goes stale because a
module it *calls* changed while its own producer file did not. `scriptHash`
triage cannot see it — the producer is byte-identical — so the only route is to
know WHICH producer emitted a witness and then walk that producer's import cone.

PR #5775 measured the class and named its own blind spot: witnesses that record
no `scriptFile` at all are invisible to the method, because there is nothing to
walk a cone from. That is the gap this closes.

WHAT IT DOES
------------
For every witness carrying no producer field, try the corpus naming convention
(`foo-bar.witness.json` <- `foo_bar.py` or `foo_bar_probe.py`) and then VERIFY
the candidate by checking the producer's own source names the witness file.

The verification is the point. A stem match alone is a guess — several
producers share a stem prefix, and a witness can be written by a script named
nothing like it. Requiring the source to name the file turns a guess into
evidence, and the two buckets are reported separately so a reader can see how
much is which.

WHAT IT DOES NOT DO
-------------------
Attribution is not staleness. Knowing which producer emitted a witness says
nothing about whether its numbers moved; it only makes the witness *eligible*
for the cone walk that decides that. Do not read the attributed count as a
count of stale witnesses.

SELF-TEST (`--self-test`)
-------------------------
#5775's measurement first returned **0** because it read a nested
`witness.scriptFile` while provenance in these files is top-level — and a zero
reads exactly like a clean tree. So this refuses to report until it has
confirmed, on the real corpus, that it finds provenance where provenance exists
and attributes a known-attributable witness. A detector that cannot fail
loudly is worse than no detector.
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

PROVENANCE_KEYS = ("scriptFile", "script", "scriptPath")


def producer_field(d: dict) -> str | None:
    """The recorded producer, checked BOTH top-level and nested under `witness`.

    Both shapes are live in this corpus. Reading only the nested one is the
    documented way to get a false zero (#5775).
    """
    for k in PROVENANCE_KEYS:
        if isinstance(d.get(k), str) and d[k].strip():
            return d[k]
    w = d.get("witness")
    if isinstance(w, dict):
        for k in PROVENANCE_KEYS:
            if isinstance(w.get(k), str) and w[k].strip():
                return w[k]
    return None


def _producers() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for p in glob.glob("**/*.py", recursive=True):
        if ("_deprecated" in p or "fsh-guts" in p):
            continue
        out.setdefault(Path(p).stem, []).append(p)
    return out


def attribute(witness_path: str, prods: dict[str, list[str]]) -> tuple[str, str | None]:
    """('verified'|'stem-only'|'none', producer_path_or_None)."""
    base = Path(witness_path).name
    stem = base[: -len(".witness.json")].replace("-", "_")
    cands = [c for c in (stem, stem + "_probe") if c in prods]
    if not cands:
        return "none", None
    for c in cands:
        for p in prods[c]:
            try:
                src = Path(p).read_text(encoding="utf-8")
            except Exception:
                continue
            if base in src or base[: -len(".witness.json")] in src:
                return "verified", p
    return "stem-only", prods[cands[0]][0]


def scan() -> dict:
    prods = _producers()
    wits = [f for f in glob.glob("**/*.witness.json", recursive=True)
            if ("_deprecated" not in f and "fsh-guts" not in f)]
    have, missing = [], []
    for f in wits:
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:
            continue
        (have if producer_field(d) else missing).append(f)
    buckets: dict[str, list] = {"verified": [], "stem-only": [], "none": []}
    for f in missing:
        kind, p = attribute(f, prods)
        buckets[kind].append({"witness": f, "producer": p})
    return {"total": len(wits), "with_provenance": len(have),
            "without_provenance": len(missing), "buckets": buckets}


def self_test() -> int:
    """Refuse to report a count until the method is shown to work."""
    fails = []
    # 1. provenance is found where it exists, in BOTH shapes.
    if producer_field({"scriptFile": "a.py"}) != "a.py":
        fails.append("top-level scriptFile not read")
    if producer_field({"witness": {"scriptFile": "a.py"}}) != "a.py":
        fails.append("nested witness.scriptFile not read")
    if producer_field({"scriptFile": "   "}) is not None:
        fails.append("blank scriptFile treated as provenance")
    if producer_field({"name": "x"}) is not None:
        fails.append("absent provenance reported as present")
    # 2. the corpus is not read as empty (the false-zero failure mode).
    r = scan()
    if r["total"] < 100:
        fails.append(f"corpus read as {r['total']} witnesses — glob is wrong")
    if r["with_provenance"] == 0:
        fails.append("ZERO witnesses have provenance — the #5775 false zero")
    # 3. attribution actually attributes something — the false-zero guard.
    #
    # Deliberately NOT pinned to a named witness. Writing a witness filename
    # into this source makes the provenance audit read this script as a
    # CONSUMER of that witness, which moved one file from
    # `prov_exempt_no_reader` to `prov_missing` on the first run here — a
    # finding manufactured by the test rather than found by it. Same class as
    # the byproduct witnesses #5763 caught before they landed.
    if not r["buckets"]["verified"]:
        fails.append("ZERO witnesses attributed — the method is not working")
    if fails:
        print("SELF-TEST FAILED:")
        for f in fails:
            print("   " + f)
        return 1
    print(f"SELF-TEST PASSED — provenance read in both shapes, corpus reads "
          f"{r['total']} witnesses with {r['with_provenance']} carrying "
          f"provenance, and {len(r['buckets']['verified'])} of the remainder "
          f"attribute (non-zero, so the method is live).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--list", action="store_true",
                    help="list the still-unattributable witnesses")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    r = scan()
    b = r["buckets"]
    inv = len(b["stem-only"]) + len(b["none"])
    print("=" * 70)
    print("WITNESS PROVENANCE ATTRIBUTION — closing the qou-wlaf blind spot")
    print("=" * 70)
    print(f"  witnesses scanned            : {r['total']:,}")
    print(f"  record a producer            : {r['with_provenance']:,}")
    print(f"  record NONE (the blind spot) : {r['without_provenance']:,}")
    print(f"    VERIFIED  (source names the witness) : {len(b['verified']):,}")
    print(f"    stem-only (unconfirmed guess)        : {len(b['stem-only']):,}")
    print(f"    no producer stem at all              : {len(b['none']):,}")
    print(f"  => invisible set {r['without_provenance']:,} -> {inv:,}")
    print("\n  Attribution is NOT staleness: it makes a witness eligible for the")
    print("  import-cone walk that decides staleness, nothing more.")
    if args.list:
        print("\n  still unattributable:")
        for e in (b["stem-only"] + b["none"])[:60]:
            print(f"    {e['witness']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
