#!/usr/bin/env python3
"""witness_producer_resolution_audit.py
========================================

**Does a witness name a producer that EXISTS — under any spelling?**

Every orphan count this corpus has produced keyed on ONE field name, and each
was wrong in the same direction: it called provenanced witnesses orphans.

    qou-tekx      keyed on `scriptFile`
    qou-bake      corrected it to `computation` -- "That read the WRONG FIELD"
    qou-agvb      found `producer`, a third spelling neither catches
    this audit    finds NINE candidate keys, of which FIVE are live, and shows
                  that the key name is the wrong thing to key on at all

## Why key-based detection cannot work here

The fields are **polymorphic**. Measured over 2939 live witnesses:

| key | carriers | what it actually holds |
|---|--:|---|
| `computation` | 2678 | the witness **id** (`yekutieli-volume-join`) in the standard `WitnessBuilder` format — **not a script**. It holds a script path only in the hand-written `docs/audits/scripts/` family that `qou-bake` found. |
| `scriptFile` | 2641 | a producer filename |
| `producer` | 64 | a producer path |
| `source` | 51 | usually a **literature PDF** (`library/arxiv-.../*.pdf`) — but sometimes a `.py` |
| `scriptPath` | 8 | a producer path |
| `script`, `generated_by`, `source_script`, `scriptName` | 0 | not used in this corpus |

So `computation` is *present* on 91 % of witnesses and *names a producer* on
almost none of them, while `source` names one occasionally. **A detector that
asks "is key K present?" answers a different question from "is there a
producer?"** — which is exactly the failure mode the three previous counts
share, one field at a time.

## What this audit does instead

It decides by **value, not by key**: a witness is provenanced iff some candidate
field holds a string containing a `.py` path that **resolves to a file in the
tree**. Three verdicts:

    RESOLVED             names a .py that exists
    NAMED_BUT_MISSING    names a .py that does NOT exist  (a dangling claim --
                         worse than silence, because it reads as provenance)
    UNPROVENANCED        no .py named anywhere

This is the same move as `convention-c-value-audit.py` versus the shape audit:
ask what the value IS, not how it was written. Recorded as an entry in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`.

## What it does NOT do

It does not check that the named script actually WRITES the witness — that is
`witness_provenance_audit.py`'s job and it does it well (`scriptFile` only).
A `RESOLVED` verdict here means *the name resolves to a file*, which is strictly
weaker, and the two audits compose: this one finds the witnesses that audit
cannot see, because it needs a `scriptFile` to start from.

Nor does it propose a canonical spelling or rewrite any witness. Naming one is
a decision for the owner; this measures the ground first.

Usage:
    python3 computations/audits/witness_producer_resolution_audit.py
    python3 computations/audits/witness_producer_resolution_audit.py --selftest
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

# Candidate keys, union of every spelling any detector in this repo has used
# plus the ones found by measurement. Presence is NOT the test -- see module
# docstring -- these are only where a value might live.
CANDIDATE_KEYS = (
    "scriptFile", "script", "scriptPath", "scriptName",
    "computation", "producer", "source", "generated_by", "source_script",
)

_PY = re.compile(r"[\w./-]+\.py")


def candidate_values(d: dict) -> dict:
    """Every candidate field's value, top-level or nested under `witness`."""
    out = {}
    for k in CANDIDATE_KEYS:
        v = d.get(k)
        if v in (None, "", {}, []) and isinstance(d.get("witness"), dict):
            v = d["witness"].get(k)
        if v not in (None, "", {}, []):
            out[k] = v
    return out


def py_names(value) -> list[str]:
    """Every `.py` path mentioned in a field value, whatever its shape."""
    text = value if isinstance(value, str) else json.dumps(value)
    return _PY.findall(text)


def build_index(root: Path) -> tuple[set[str], set[str]]:
    """(relative posix paths, bare basenames) of every .py in the tree."""
    paths, names = set(), set()
    for p in root.rglob("*.py"):
        if any(part in (".git", "node_modules", ".lake") for part in p.parts):
            continue
        paths.add(p.relative_to(root).as_posix())
        names.add(p.name)
    return paths, names


def resolve(cand: str, paths: set[str], names: set[str]) -> bool:
    c = cand.lstrip("./")
    return c in paths or Path(c).name in names


_WRITE = re.compile(r"WitnessBuilder|json\.dump|write_text|\.save\(|write_witness")


def index_scripts(root: Path):
    """One pass over every .py: which witness ids does it mention, and does it
    write anything at all?

    This is what lets the audit answer *"does a producer EXIST"* rather than
    only *"does the witness CITE one"*. The two are different questions and the
    second is the weaker: `e0-calibration-audit.witness.json` names no `.py`
    anywhere, yet `computations/audits/e0_calibration_audit.py` produces it.
    An earlier version of this file reported that witness UNPROVENANCED, which
    was a false positive of exactly the kind this audit exists to catch.
    """
    producers: dict[str, list[str]] = collections.defaultdict(list)
    basenames = set()
    for p in root.rglob("*.py"):
        if any(part in (".git", "node_modules", ".lake") for part in p.parts):
            continue
        basenames.add(p.name)
        try:
            txt = p.read_text(errors="ignore")
        except OSError:
            continue
        rel = p.relative_to(root).as_posix()
        # A PRODUCER SIGNATURE, not a mention. `WitnessBuilder("<id>")` is the
        # canonical one; the legacy fallback is the id written as a filename in
        # a file that also writes. Merely NAMING an id is not enough -- an audit
        # that READS a witness and writes its own would otherwise rescue it.
        # Measured: that false positive hid `4he-binding-full-pipeline`, whose
        # own scriptFile says "no matching producer found", behind
        # `witness_provenance_audit.py`.
        for wid in set(re.findall(r"""WitnessBuilder\(\s*["']([^"']+)["']""", txt)):
            producers[wid].append(rel)
        if _WRITE.search(txt):
            for wid in set(re.findall(r"""["']([\w.-]+)\.witness\.json["']""", txt)):
                producers[wid].append(rel)
    return producers, basenames


# Suffixes the corpus actually uses between a witness id and its script name.
# `_probe` is not cosmetic: gswz_52_symmetrization.witness.json is produced by
# gswz_52_symmetrization_probe.py, and an exact-name-only check reports it as an
# orphan. Measured -- that miss accounted for most of a 30-item orphan list.
_SUFFIXES = ("", "_probe", "_audit", "_check", "_sweep", "_gate")


def resolve_producer(witness_path: Path, d: dict, producers, basenames):
    """`(verdict, evidence)` for a witness that CITES no resolvable .py.

    Order matters — each rung is weaker evidence than the last:

      CONVENTION   the witness id snake_cased is a real script filename
      MENTIONED    some live script names the witness id AND writes something
      DEPRECATED   the only such scripts are under `_deprecated/`
      ORPHAN       nothing names it
    """
    wid = witness_path.name[: -len(".witness.json")]
    stem = wid.replace("-", "_")
    for suf in _SUFFIXES:
        if stem + suf + ".py" in basenames:
            return "FOUND_BY_CONVENTION", stem + suf + ".py"
    writers = producers.get(wid, [])
    live = [f for f in writers if ("_deprecated" not in f and "fsh-guts" not in f)]
    if live:
        return "FOUND_BY_PRODUCER_CALL", live[:3]
    if writers:
        return "PRODUCER_DEPRECATED_ONLY", writers[:3]
    return "ORPHAN", None


def classify(d: dict, paths: set[str], names: set[str]) -> tuple[str, dict]:
    vals = candidate_values(d)
    found, missing = {}, {}
    for k, v in vals.items():
        for cand in py_names(v):
            (found if resolve(cand, paths, names) else missing).setdefault(k, []).append(cand)
    if found:
        return "RESOLVED", found
    if missing:
        return "NAMED_BUT_MISSING", missing
    return "UNPROVENANCED", {k: str(v)[:80] for k, v in vals.items()}


def scan(root: Path):
    paths, names = build_index(root)
    producers, basenames = index_scripts(root)
    buckets = collections.defaultdict(list)
    key_carriers = collections.Counter()
    key_names_producer = collections.Counter()
    total = 0
    for p in sorted((root / "computations").rglob("*.witness.json")):
        if ("_deprecated" in str(p) or "fsh-guts" in str(p)):
            continue
        try:
            d = json.loads(p.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if not isinstance(d, dict):
            continue
        total += 1
        for k, v in candidate_values(d).items():
            key_carriers[k] += 1
            if any(resolve(c, paths, names) for c in py_names(v)):
                key_names_producer[k] += 1
        verdict, detail = classify(d, paths, names)
        if verdict == "UNPROVENANCED":
            # The witness cites nothing runnable -- but a producer may still
            # exist and simply not be cited. Ask the stronger question.
            verdict, detail = resolve_producer(p, d, producers, basenames)
        buckets[verdict].append({
            "witness": p.relative_to(root).as_posix(), "detail": detail,
        })
    return total, buckets, key_carriers, key_names_producer


def selftest(root: Path) -> int:
    """Known cases. Fails loudly rather than reporting a clean tree wrongly."""
    paths, names = build_index(root)
    fails = []

    def chk(label, ok):
        if not ok:
            fails.append(label)
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")

    # a value naming a real script resolves; a fabricated one does not
    chk("resolves a real script",
        resolve("computations/witness_provenance_audit.py", paths, names))
    chk("does not resolve a fabricated script",
        not resolve("computations/no_such_script_xyzzy.py", paths, names))
    # bare basename resolves (scriptFile stores basenames)
    chk("resolves a bare basename",
        resolve("witness_provenance_audit.py", paths, names))
    # `computation` holding an ID must NOT count as provenance
    v, _ = classify({"computation": "yekutieli-volume-join"}, paths, names)
    chk("a `computation` holding an ID is UNPROVENANCED, not RESOLVED",
        v == "UNPROVENANCED")
    # `computation` holding a script path MUST count (the qou-bake family)
    v, _ = classify({"computation": "docs/audits/scripts/keystone_x_probe.py"},
                    paths, names)
    chk("a `computation` holding a missing script is NAMED_BUT_MISSING",
        v == "NAMED_BUT_MISSING")
    # `source` holding a PDF must not count
    v, _ = classify({"source": {"pdf": "library/arxiv-x/y.pdf"}}, paths, names)
    chk("a `source` holding a PDF is UNPROVENANCED", v == "UNPROVENANCED")
    # nested witness.scriptFile is read (the attribution audit's case)
    v, _ = classify({"witness": {"scriptFile": "witness_provenance_audit.py"}},
                    paths, names)
    chk("nested witness.scriptFile is read", v == "RESOLVED")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--limit", type=int, default=12)
    args = ap.parse_args()

    if args.selftest:
        print("witness-producer-resolution — selftest\n")
        rc = selftest(ROOT)
        print("\n" + ("ALL PASSED" if not rc else "FAILED"))
        return rc

    t0 = time.monotonic()
    total, buckets, carriers, produces = scan(ROOT)

    print("WITNESS PRODUCER RESOLUTION — decided by VALUE, not by key name\n")
    print(f"  live witnesses scanned : {total}\n")
    print(f"  {'key':<16} {'carriers':>9} {'names a real .py':>18}")
    for k in CANDIDATE_KEYS:
        if carriers[k]:
            print(f"  {k:<16} {carriers[k]:>9} {produces[k]:>18}")
    print("\n  ^ the gap between these columns is why key-presence is the wrong")
    print("    test: `computation` is present on most witnesses and names a")
    print("    producer on almost none.\n")

    order = ("RESOLVED", "FOUND_BY_CONVENTION", "FOUND_BY_PRODUCER_CALL",
             "NAMED_BUT_MISSING", "PRODUCER_DEPRECATED_ONLY", "ORPHAN")
    print("  verdicts (strongest evidence first):")
    for v in order:
        print(f"    {v:<26} {len(buckets[v]):>5}")
    print()
    print("  RESOLVED            = the witness CITES a .py that exists")
    print("  FOUND_BY_CONVENTION = id snake_cased IS a real script filename")
    print("  FOUND_BY_PRODUCER_CALL = a live script CONSTRUCTS this witness")
    print("  ORPHAN              = nothing in the tree names it at all\n")

    for v in ("NAMED_BUT_MISSING", "PRODUCER_DEPRECATED_ONLY", "ORPHAN"):
        rows = buckets[v]
        if not rows:
            continue
        print(f"  --- {v} ({len(rows)}) ---")
        for r in rows[:args.limit]:
            print(f"    {r['witness']}")
            if v == "NAMED_BUT_MISSING":
                print(f"        {r['detail']}")
        if len(rows) > args.limit:
            print(f"    ... and {len(rows) - args.limit} more")
        print()

    try:
        from qou_substrate.witness import WitnessBuilder
    except ImportError:
        print("(qou_substrate unavailable — no witness written)")
        return 0

    w = WitnessBuilder("witness-producer-resolution-audit", start_time=t0)
    w.set_description(
        "Does a witness name a producer that EXISTS, under ANY spelling? "
        "Decides by VALUE (does a field hold a .py path that resolves in the "
        "tree) rather than by KEY NAME, because the fields are polymorphic: "
        "`computation` is present on ~91% of witnesses and holds the witness "
        "ID, not a script, on almost all of them; `source` usually holds a "
        "literature PDF but sometimes a .py. Three prior orphan counts each "
        "keyed on one field (qou-tekx scriptFile, qou-bake computation, "
        "qou-agvb producer) and each OVER-reported orphans by calling "
        "provenanced witnesses unprovenanced. Does NOT check that the named "
        "script actually writes the witness -- that is "
        "witness_provenance_audit.py, which needs a scriptFile to start from "
        "and cannot see the witnesses this audit finds.")
    w.add_data("totals", {
        "live_witnesses": total,
        **{v: len(buckets[v]) for v in order},
    })
    w.add_data("verdict_meanings", {
        "RESOLVED": "the witness CITES a .py path that exists",
        "FOUND_BY_CONVENTION": "witness id snake_cased is a real script filename",
        "FOUND_BY_PRODUCER_CALL": "a live script constructs this witness id "
                                  "(WitnessBuilder(\"<id>\") or writes <id>.witness.json)",
        "NAMED_BUT_MISSING": "cites a .py that does NOT exist (dangling claim)",
        "PRODUCER_DEPRECATED_ONLY": "only _deprecated/ scripts name it",
        "ORPHAN": "nothing in the tree names it",
    })
    w.add_data("per_key", {
        k: {"carriers": carriers[k], "names_a_real_py": produces[k]}
        for k in CANDIDATE_KEYS if carriers[k]
    })
    for v in ("NAMED_BUT_MISSING", "PRODUCER_DEPRECATED_ONLY", "ORPHAN"):
        w.add_data(v.lower(), [r["witness"] for r in buckets[v]])
    w.add_data("method", {
        "decides_by": "value (a .py path that resolves in the tree)",
        "not_by": "key presence",
        "candidate_keys": list(CANDIDATE_KEYS),
        "reads_nested": "witness.<key> as well as top-level",
        "resolution": "exact repo-relative path OR bare basename match",
    })
    w.add_assertion("scan_non_empty", total > 0, True)
    w.add_assertion("selftest_passes", selftest(ROOT) == 0, True)
    w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": "a provenance audit; it never reads q0.",
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
