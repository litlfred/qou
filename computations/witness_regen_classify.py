#!/usr/bin/env python3
# polynomial_q_not_applicable: static classifier over witness diffs.
"""Classify what a witness regeneration actually changed.

Owner directive: NO FLOAT64 — this is the guard that decides whether a
regenerated witness may be committed.

## Why a classifier and not a diff

Re-running a producer changes a witness for several distinct reasons, and they
carry opposite verdicts:

| verdict | meaning | commit? |
|---|---|---|
| `DECLARED` | `upstream_witness_hashes` appeared; nothing else but metadata moved | yes |
| `ANCHOR_MIGRATION` | the witness's own q₀ moved muon → proton, and every other change is bounded | yes |
| `VALUES` | something moved that neither of the above explains | **no** |
| `NOCHANGE` | ran, nothing new | n/a |

`ANCHOR_MIGRATION` exists because of a measurement: 650 witnesses carry a
muon-anchored q₀ against 379 proton, and producers read `Q` from
`q_parameter`, which is proton-anchored. **Re-running a producer therefore
re-anchors it automatically** — observed in `braid-encoding-audit`, whose 87
moved fields were all one substitution, `-h/2` at the muon anchor
(`-0.10453016099779683`) to `-h/2` at the proton anchor
(`-0.10453014939781968`).

A classifier without this verdict reverts that as drift, which is what the
first version of this guard did: it would have discarded a correct migration
and quietly held the corpus on a retired anchor.

## The bound, and why it is evidence-gated

Anchor migration is only accepted when the witness itself shows the flip — a
q₀-valued field going from the muon prefix to the proton prefix. Small
movement alone is never enough. That matters because a *different* 1e-4-scale
change exists in this corpus and must not be waved through: the
colour-weighted vs colour-blind crossing convention moves `tr_M(4He)` by
182 ppm with no anchor change at all. Requiring positive evidence of the flip
separates them; a bound alone would not.

Usage:
    python3 computations/witness_regen_classify.py <witness.json> [--base REF]
    python3 computations/witness_regen_classify.py --self-test
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Stamped every run; never evidence of a real change.
#
# `engine`, `_provenance` and `convention_inferred_by` are here because they
# record *how* a value was produced, not the value. Leaving `engine` out made
# the classifier reject a genuine deuteron ANCHOR_MIGRATION on the grounds that
# a string field moved — the numerics were within bound and the q₀ flip was
# present, but the engine label changed from the fallback path to the native
# one. That is exactly the kind of provenance churn a regeneration is expected
# to produce.
#
# `convention` is deliberately NOT here: colour-blind versus colour-weighted
# crossings is a physics choice worth 182 ppm in tr_M(4He), and a run that
# changes it must surface as VALUES rather than slip through as metadata.
META = {
    "computedAt", "commitSha", "scriptHash", "scriptCommitSha", "durationMs",
    "engineVersion", "engine", "environment", "generatedAt", "timestamp",
    "upstream_witness_hashes", "precisionMetadata", "compute_time_sec",
    "compute_time_sec_so_far", "_provenance", "convention_inferred_by",
}

MUON_PREFIX = "1.109978595"
PROTON_PREFIX = "1.109978582"

# Ceiling on collateral movement in an accepted anchor migration. The q₀ shift
# is ~1.15e-8 relative; amplification through a producer is bounded well under
# this. Deliberately BELOW the 1.8e-4 crossing-convention shift, so that
# convention change can never be mistaken for an anchor migration.
ANCHOR_COLLATERAL_MAX = 1e-5


def flatten(obj, path="", out=None) -> dict:
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in META:
                continue
            flatten(v, f"{path}.{k}" if path else k, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            flatten(v, f"{path}[{i}]", out)
    else:
        out[path] = obj
    return out


def _num(v):
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


# Literal anchor labels. `q0Anchor` carries these directly, and a witness
# saying "muon" -> "proton" is the strongest evidence of a migration there is —
# stronger than inferring it from a numeric prefix. Rejecting it as "a
# non-numeric field moved" is exactly backwards, and did reject a genuine
# deuteron migration until this was added.
_MUON_LABELS = {"muon", "ideal_muon", "ideal-muon"}
_PROTON_LABELS = {"proton"}


def _anchor_of(v) -> str | None:
    s = str(v).strip()
    if s in _MUON_LABELS:
        return "muon"
    if s in _PROTON_LABELS:
        return "proton"
    if s.startswith(MUON_PREFIX):
        return "muon"
    if s.startswith(PROTON_PREFIX):
        return "proton"
    return None


def classify(old: dict, new: dict) -> dict:
    a, b = flatten(old), flatten(new)
    moved = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    gained = bool((new.get("data") or {}).get("upstream_witness_hashes")) and \
        not bool((old.get("data") or {}).get("upstream_witness_hashes"))

    if not moved:
        return {"verdict": "DECLARED" if gained else "NOCHANGE",
                "moved": 0, "flips": 0}

    # Positive evidence: a q0-valued field flipped muon -> proton.
    flips = [k for k in moved
             if _anchor_of(a.get(k)) == "muon" and _anchor_of(b.get(k)) == "proton"]
    if not flips:
        return {"verdict": "VALUES", "moved": len(moved), "flips": 0,
                "sample": moved[:5]}

    # Every other movement must be bounded, and none may go the wrong way.
    for k in moved:
        if _anchor_of(a.get(k)) == "proton" and _anchor_of(b.get(k)) == "muon":
            return {"verdict": "VALUES", "moved": len(moved), "flips": len(flips),
                    "reason": f"reverse flip at {k}", "sample": [k]}
        x, y = _num(a.get(k)), _num(b.get(k))
        if x is None or y is None:
            if a.get(k) != b.get(k) and k not in flips:
                return {"verdict": "VALUES", "moved": len(moved),
                        "flips": len(flips),
                        "reason": f"non-numeric change at {k}", "sample": [k]}
            continue
        denom = abs(x) if x else 1.0
        if abs(y - x) / denom > ANCHOR_COLLATERAL_MAX:
            return {"verdict": "VALUES", "moved": len(moved), "flips": len(flips),
                    "reason": (f"{k} moved {abs(y - x) / denom:.3g}, above the "
                               f"{ANCHOR_COLLATERAL_MAX:g} anchor bound"),
                    "sample": [k]}
    return {"verdict": "ANCHOR_MIGRATION", "moved": len(moved),
            "flips": len(flips)}


CASES = [
    ("declaration only", {}, {}, True, "DECLARED"),
    ("nothing at all", {"a": 1}, {"a": 1}, False, "NOCHANGE"),
    ("clean anchor migration",
     {"q0": "1.1099785955573347", "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "x": 0.20906029879563937}, False,
     "ANCHOR_MIGRATION"),
    # The real braid-encoding-audit shape: -h/2 either side of the flip.
    ("braid-encoding-audit shape",
     {"q0": "1.1099785955573347", "d": -0.10453016099779683},
     {"q0": "1.1099785827513808", "d": -0.10453014939781968}, False,
     "ANCHOR_MIGRATION"),
    ("movement with NO anchor flip is never waved through",
     {"x": 0.05534834587669884}, {"x": 0.055358426266783106}, False, "VALUES"),
    # 182 ppm crossing-convention change, WITH a flip present: still rejected,
    # because it exceeds the collateral bound. This is the case the bound is
    # sized for.
    ("crossing-convention shift is not an anchor migration",
     {"q0": "1.1099785955573347", "tr_M": 0.05534834587669884},
     {"q0": "1.1099785827513808", "tr_M": 0.055358426266783106}, False,
     "VALUES"),
    ("reverse flip (proton -> muon) is rejected",
     {"q0": "1.1099785827513808"}, {"q0": "1.1099785955573347"}, False, "VALUES"),
    ("string field changing alongside a flip is rejected",
     {"q0": "1.1099785955573347", "note": "a"},
     {"q0": "1.1099785827513808", "note": "b"}, False, "VALUES"),
    # The deuteron case: a real anchor migration that the classifier rejected
    # because `engine` moved from the fallback label to the native one.
    ("engine label moving does not veto an anchor migration",
     {"q0": "1.1099785955573347", "engine": "python", "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "engine": "pyhecke_native",
      "x": 0.20906029879563937}, False, "ANCHOR_MIGRATION"),
    # ...but a convention change still must not.
    ("convention change is never an anchor migration",
     {"q0": "1.1099785955573347", "convention": "averaged-crossings"},
     {"q0": "1.1099785827513808",
      "convention": "colour-weighted-averaged-crossing"}, False, "VALUES"),
    ("q0Anchor label muon -> proton is evidence, not a veto",
     {"q0Anchor": "muon", "x": 0.20906032199559366},
     {"q0Anchor": "proton", "x": 0.20906029879563937}, False,
     "ANCHOR_MIGRATION"),
    ("q0Anchor proton -> muon is a reverse flip",
     {"q0Anchor": "proton"}, {"q0Anchor": "muon"}, False, "VALUES"),
    ("metadata-only churn is not movement",
     {"computedAt": "x", "durationMs": 1, "v": 2},
     {"computedAt": "y", "durationMs": 9, "v": 2}, False, "NOCHANGE"),
]


def self_test() -> int:
    fails = 0
    for label, old, new, gained, want in CASES:
        o = dict(old)
        n = dict(new)
        if gained:
            n["data"] = {"upstream_witness_hashes": [{"path": "u.witness.json"}]}
        got = classify(o, n)["verdict"]
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("witness", nargs="?")
    ap.add_argument("--base", default="HEAD")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.witness:
        ap.error("a witness path is required unless --self-test")
    p = Path(a.witness)
    rel = p.resolve().relative_to(ROOT).as_posix()
    old_raw = subprocess.run(["git", "show", f"{a.base}:{rel}"], cwd=ROOT,
                             capture_output=True, text=True).stdout
    if not old_raw:
        print(f"NEW  {rel}  (no {a.base} version)")
        return 0
    r = classify(json.loads(old_raw), json.loads(p.read_text(encoding="utf-8")))
    print(f"{r['verdict']}  {rel}")
    for k in ("moved", "flips", "reason", "sample"):
        if r.get(k) not in (None, 0, []):
            print(f"    {k}: {r[k]}")
    return 0 if r["verdict"] in {"DECLARED", "ANCHOR_MIGRATION", "NOCHANGE"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
