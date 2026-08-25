#!/usr/bin/env python3
# polynomial_q_not_applicable: build-hygiene provenance measurement, emits no numeric physics.
"""Is a regenerated padded value MINTED here, or inherited from upstream?

Owner directive: NO FLOAT64.

`producer_repad_sweep.py` says a producer regenerates padded fields.
`float64_entry_tracer.py` says where a float64 entered its source. Neither
answers the remaining question: when a producer writes a padded value, did it
*create* those digits or copy them from a witness it read?

The answer decides the fix. Minted padding is fixed in that producer. Inherited
padding cannot be — re-running a consumer before its producer just re-imports
the digits, so the fix belongs upstream and the order matters.

## Why this tool exists at all

`docs/audits/2026-08-07-producer-repadding-empirical-sweep.md` recorded
"**20 of 20 `LOCAL`, `propagated = 0`** — not one padded value exists anywhere
else in the corpus", from a classifier that **was never committed**, so the
result was never reproducible.

The exact-string verdict itself holds up. What does not is reading it as the
whole answer, because searching for the **exact padded string** is biased
toward `LOCAL` by construction: commit `0de68792` stripped padding from 58
witnesses, so an upstream witness now holds `0.024180175767745112` where the
consumer regenerates
`0.024180175767745112208606528270138369407504796981812` — the same value, no
longer the same string. The search reports "nowhere else" for a value that is
sitting upstream in short form.

**A caution this tool exists to enforce.** The first attempt to demonstrate
that was run by grepping a worktree the session had itself been running
producers in, so it found *this session's* regenerated output and read it as
committed upstream evidence. Provenance must be asked of the **committed**
corpus, indexed before anything runs, with the producer's own fresh output
excluded from its own lookup — all three of which this tool does, and the
ad-hoc grep did none of.

So provenance is asked twice, and both answers are reported:

| verdict | meaning |
|---|---|
| `VERBATIM_UPSTREAM` | the padded string itself is in another committed witness |
| `VALUE_UPSTREAM` | the same float64 value is upstream, in some other spelling |
| `LOCAL` | neither — these digits are minted here |

`VALUE_UPSTREAM` is evidence, not proof: two producers can compute the same
quantity independently. It says the padding *may* be inherited and the upstream
witness must be checked first — which is precisely the check an exact-string
search silently skips.

**And it is only evidence when the value is distinctive.** A field whose
float64 is `1.0` matches upstream trivially — `1.0` appears throughout the
corpus — so a near-integer flagged by `is_f64_padded` (a genuine computation
landing at `1 - 1.4e-51`) would otherwise read as inherited on no evidence at
all. Each match therefore records `distinctive`: at least
`DISTINCTIVE_SIG_DIGITS` significant digits in the shortest round-tripping
repr. Non-distinctive matches are counted separately and must not be read as
propagation.

The index is built from the **committed** corpus before anything runs, and a
producer's own freshly written witnesses are excluded from its own lookup;
otherwise every value trivially "exists upstream" in the file just written.

Usage:
    git worktree add --detach /tmp/prov-wt HEAD
    python3 computations/witness_padding_provenance.py /tmp/prov-wt \
        --producers rho_k_h3a_lp_dual.py qbeta_markov_trace_norm_probe.py \
        --out /tmp/provenance.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from collections import Counter
from decimal import Decimal
from pathlib import Path

# Below this many significant digits in the shortest repr, an upstream value
# match carries no information: 1.0 and 6.0 are everywhere in the corpus.
DISTINCTIVE_SIG_DIGITS = 10

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_float64_padding_audit import NUMSTR, is_f64_padded  # noqa: E402

# Permissive: the index must hold SHORT spellings too, or the stripped upstream
# form is invisible and every value reads as LOCAL.
ANYNUM = re.compile(r"^-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?$")


def _walk_strings(obj, path, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            _walk_strings(v, f"{path}.{k}" if path else k, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _walk_strings(v, f"{path}[{i}]", out)
    elif isinstance(obj, str):
        t = obj.strip()
        if ANYNUM.match(t):
            out.append((path, t))


def numeric_strings(path: Path) -> list[tuple[str, str]]:
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[tuple[str, str]] = []
    _walk_strings(d, "", out)
    return out


def f64_key(s: str):
    try:
        v = float(s)
    except (TypeError, ValueError):
        return None
    return repr(v)


def is_distinctive(s: str) -> bool:
    """Does this value carry enough digits for an upstream match to mean anything?"""
    k = f64_key(s)
    if k is None:
        return False
    try:
        return len(Decimal(k).normalize().as_tuple().digits) >= DISTINCTIVE_SIG_DIGITS
    except Exception:
        return False


def build_index(comp: Path):
    """string -> {files}, float64-value -> {files}, over the committed corpus."""
    by_str: dict[str, set] = {}
    by_val: dict[str, set] = {}
    n = 0
    for w in sorted(comp.rglob("*.witness.json")):
        rel = w.as_posix()
        for _, s in numeric_strings(w):
            n += 1
            by_str.setdefault(s, set()).add(rel)
            k = f64_key(s)
            if k is not None:
                by_val.setdefault(k, set()).add(rel)
    return by_str, by_val, n


def padded_fields(path: Path) -> list[tuple[str, str]]:
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[tuple[str, str]] = []
    for p, s in numeric_strings(path):
        if NUMSTR.match(s):
            try:
                if is_f64_padded(s):
                    out.append((p, s))
            except Exception:
                pass
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("worktree", help="detached worktree — NOT the live checkout")
    ap.add_argument("--producers", nargs="+", required=True)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--out", default="/tmp/provenance.json")
    a = ap.parse_args()

    wt = Path(a.worktree).resolve()
    if wt == HERE.parent:
        print("REFUSING: that is the live checkout. Use a detached worktree.",
              file=sys.stderr)
        return 2
    comp = wt / "computations"
    if not comp.is_dir():
        print(f"no computations/ under {wt}", file=sys.stderr)
        return 2

    def sh(*args):
        return subprocess.run(args, cwd=wt, capture_output=True, text=True)

    def pristine():
        sh("git", "checkout", "--", ".")
        sh("git", "clean", "-fdq", "computations")

    def hashes():
        return {p: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(comp.rglob("*.witness.json"))}

    pristine()
    print("[prov] indexing committed corpus…", flush=True)
    by_str, by_val, n = build_index(comp)
    print(f"[prov] {len(by_str)} distinct strings / {n} numeric fields", flush=True)

    results, t0 = [], time.time()
    for i, name in enumerate(a.producers, 1):
        # Resolve the producer DETERMINISTICALLY, and refuse an ambiguous
        # basename rather than blind-picking one.
        #
        # `rglob` yields in os.scandir order — filesystem-dependent, not
        # sorted — so the bare `hits[0]` here could run a different copy on a
        # different machine, or on the same machine after unrelated churn, with
        # nothing in the output saying which one ran. Four basenames under
        # computations/ are genuinely duplicated today, two of them named by a
        # witness `scriptFile` and so reachable as an argument here:
        # qbeta_phib_2loop_bdictionary_probe.py and witness_provenance_audit.py
        # (the latter is the qou-2r42 pair — two DIFFERENT audits sharing a
        # name, where picking the wrong one swaps the check being run).
        # `sorted()` alone would only make the wrong pick reproducible, so
        # ambiguity is reported instead. Bean qou-kcii.
        hits = sorted(p for p in comp.rglob(name) if "_deprecated" not in p.parts)
        if not hits:
            results.append({"producer": name, "status": "not_found", "fields": []})
            continue
        if len(hits) > 1:
            rels = [p.relative_to(wt).as_posix() for p in hits]
            print(f"[{i:3}/{len(a.producers)}] {name}: AMBIGUOUS — "
                  + " | ".join(rels), flush=True)
            results.append({"producer": name, "status": "ambiguous_basename",
                            "candidates": rels, "fields": []})
            continue
        src = hits[0]
        pristine()
        before = hashes()
        print(f"[{i:3}/{len(a.producers)}] {name}", flush=True)
        try:
            r = subprocess.run([sys.executable, "-u", str(src.relative_to(wt))],
                               cwd=wt, capture_output=True, text=True,
                               timeout=a.timeout)
            status = "ok" if r.returncode == 0 else f"exit {r.returncode}"
        except subprocess.TimeoutExpired:
            status = "timeout"

        written = {p.as_posix() for p, h in hashes().items() if before.get(p) != h}
        fields = []
        for p in sorted(written):
            for field, val in padded_fields(Path(p)):
                # A producer's own fresh output is not "upstream".
                elsewhere_str = sorted(by_str.get(val, set()) - written)
                k = f64_key(val)
                elsewhere_val = sorted((by_val.get(k, set()) if k else set()) - written)
                dist = is_distinctive(val)
                verdict = ("VERBATIM_UPSTREAM" if elsewhere_str else
                           ("VALUE_UPSTREAM" if dist else "VALUE_UPSTREAM_ROUND")
                           if elsewhere_val else "LOCAL")
                fields.append({
                    "witness": Path(p).relative_to(wt).as_posix(),
                    "field": field, "value": val, "verdict": verdict,
                    "distinctive": dist,
                    "verbatim_in": elsewhere_str[:4],
                    "value_in": elsewhere_val[:4],
                })
        c = Counter(f["verdict"] for f in fields)
        results.append({"producer": name, "status": status,
                        "padded": len(fields), "counts": dict(c), "fields": fields})
        print(f"        -> {status}  padded {len(fields)}  " +
              "  ".join(f"{k}={v}" for k, v in c.most_common()), flush=True)
        pristine()

    Path(a.out).write_text(json.dumps(results, indent=1))
    tot = Counter()
    for r in results:
        tot.update(r.get("counts", {}))
    print(f"\n[prov] {(time.time()-t0)/60:.1f}m -> {a.out}")
    print("\n=== PROVENANCE (padded fields) ===")
    for k, v in tot.most_common():
        print(f"  {k:<20} {v}")
    if tot:
        n = sum(tot.values())
        print(f"\n{tot['VERBATIM_UPSTREAM'] + tot['VALUE_UPSTREAM']}/{n} padded "
              f"fields carry a DISTINCTIVE value already committed upstream "
              f"({tot['VERBATIM_UPSTREAM']} of them verbatim).")
        if tot["VALUE_UPSTREAM_ROUND"]:
            print(f"{tot['VALUE_UPSTREAM_ROUND']} further matches are round "
                  f"numbers (1.0, 6.0, …) — vacuous, NOT evidence of propagation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
