#!/usr/bin/env python3
# polynomial_q_not_applicable: convention-frame audit over committed witnesses.
"""Find witnesses whose payload is convention-C-frame, by the ANSWER not the source.

Convention D (`z = q³/(q²+1)`, canonical since the 2026-08-15 owner ruling;
cascade landed 2026-08-09) collapses the Wenzl bridge to `X = q⁴ = Q²` exactly
— the integral Wenzl level `r = 2`, whose row cap is `ℓ(λ) ≤ 2`. So under D:

    y_λ  is EXACTLY 0  for every partition with three or more rows.

Under C, `X` was not a power of `Q` (1.7202517512 at q₀ against Q² =
1.5179532498) and `y_(1³) ≠ 0`. That asymmetry is a complete convention test
that needs no source, no `z` grep, and no anchor:

    a NONZERO y_λ on a ≥3-row partition is impossible under D.

This is the counter-move AGENTS.md prescribes for exactly this problem — every
source-level detector keys on how the convention was *written*, and the
detector-blindness taxonomy already catalogues thirteen spellings that evade
that. The algebraic form of the *result* keys on what it is. A value cannot be
stale, mislabelled, re-spelled, or inherited from a stale record and still
carry a nonzero y_λ on a 4-row partition under D.

WHAT A HIT IS AND IS NOT
    A hit says the witness's PAYLOAD is C-frame. It does NOT say the producer
    is: the producer may have been migrated while the witness was never
    recomputed (that is the common case — see su4_1111_markov_trace_probe,
    whose producer crashes, so no one COULD have recomputed it). Re-run the
    producer to tell the two apart. A producer that still emits the fingerprint
    is a live source defect and a much stronger finding than a stale witness.

    A NON-hit is not a clean bill: a witness with only ≤2-row partitions is
    silent under this test, because C and D agree there.

THE LIMIT OF THIS TOOL — it keys on a FIELD NAME, which is the very trap the
docstring above congratulates itself for avoiding one level up. The row-cap
argument is sound for the WENZL y_λ; this scan finds any field *named*
`y_lambda` / `y` sitting beside a partition. AGENTS.md is explicit that the
three partition-weight families `y_λ` / `w_λ` / `w̃_λ` are DISTINCT at q ≠ 1
and must never be conflated, so a hit on a field that is not the Wenzl y_λ is
a false positive this cannot rule out by itself.

    Confirmed by hand so far: su4-1111-markov-trace (traced to
    y_lambda_wenzl_bridge_numeric, the change reproduced by re-running).
    The other files are CANDIDATES — resolve each by checking which weight
    its producer computes before calling it a convention defect.

So treat the count as an upper bound on C-frame witnesses and a lower bound on
nothing. It is a triage list, not a verdict.

Usage:  python3 computations/audits/y_lambda_convention_c_fingerprint_audit.py [--json OUT]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

Y_KEYS = {"y_lambda", "ylambda", "y_lam", "y"}
LAMBDA_KEYS = {"lambda", "lam", "partition", "shape"}
MIN_ROWS = 3          # C and D agree at <= 2 rows, so those are silent

# "y_λ = 0 under D" is ALGEBRAIC; the arithmetic that evaluates it is not, so a
# correctly-D-frame producer writes a residue, not a literal zero. Measured over
# the 1635 >=3-row values in the corpus: 1377 are exactly 0, and the 258 nonzero
# ones are TRIMODAL with a 68-DECADE EMPTY BAND between the residues and the
# real values --
#
#     1e-150 .. 1e-140    17 fields   D-frame residue (helium-4, 50 dps)
#      1e-80 ..  1e-70    81 fields   D-frame residue (chi-* family)
#      << 68 decades containing NOTHING >>
#      1e-10 ..   1e0    160 fields   convention-C scale
#
# so the threshold is read off the data rather than chosen. 1e-30 sits in the
# middle of the empty band, 40 decades above the largest residue and 20 below
# the smallest real value. An `x != 0` test instead of this one over-counts by
# 107 fields across 6 files -- every one of them a correct D-frame witness that
# merely recorded its zero as 1e-148 rather than as 0.0.
C_SCALE_FLOOR = 1e-30
PARTITION_TEXT = re.compile(r"[\[\(\s\d,\]\)]+")


def rows_of(value) -> int | None:
    """Row count of a partition written as a list or as its repr, else None."""
    if isinstance(value, list) and value and all(isinstance(x, int) for x in value):
        return len(value)
    if isinstance(value, str) and PARTITION_TEXT.fullmatch(value):
        return len(re.findall(r"\d+", value))
    return None


def _q_int(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def _hook_weight(shape, q):
    """d_q(λ)² / [n]_q!, the SYMMETRIC PLANCHEREL weight — NOT Jones–Markov.

    Hook-length formula: d_q(λ) = [n]_q! / ∏_x [h(x)]_q.
    """
    from math import prod
    rows = list(shape)
    if not rows or rows[0] <= 0:
        return None
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = [(ri - j - 1) + (cols[j] - i - 1) + 1
             for i, ri in enumerate(rows) for j in range(ri)]
    n = sum(rows)
    nfact = prod(_q_int(k, q) for k in range(1, n + 1))
    dq = nfact / prod(_q_int(h, q) for h in hooks)
    return (dq * dq) / nfact


_Q_CACHE: list = []


def _substrate_q():
    """Resolve the substrate q, warning ONCE and loudly if it cannot.

    The import path moved (`q_parameter` -> `substrate.q_parameter`) between
    2026-08-24 and 2026-09-03, and the first version of this discriminator
    swallowed that in a bare `except: return False`. The effect was invisible
    and exactly backwards from useful: every candidate stayed flagged, so the
    audit looked like it was working while the new check ran on nothing.
    A degraded check must say so.
    """
    if _Q_CACHE:
        return _Q_CACHE[0]
    # Raise precision BEFORE parsing q. Caching it at the default dps=15 makes
    # every downstream comparison accurate to ~1e-15, so a 1e-20 threshold can
    # never be met and the discriminator silently answers "not Plancherel" for
    # everything. This is the module-const-precision trap the corpus already
    # gates on (computations/module_const_precision_audit.py); the ordering is
    # the whole bug.
    from mpmath import mp as _mp
    _mp.dps = 60
    import sys as _sys
    root = pathlib.Path(__file__).resolve().parent.parent
    for extra in (root, root / "substrate", root / "hecke"):
        if str(extra) not in _sys.path:
            _sys.path.insert(0, str(extra))
    for mod, attr in (("substrate.q_parameter", "Q_MP"),
                      ("q_parameter", "Q_MP"),
                      ("substrate.q_parameter", "Q_50_DIGIT_STR"),
                      ("q_parameter", "Q_50_DIGIT_STR")):
        try:
            from importlib import import_module
            from mpmath import mp
            v = getattr(import_module(mod), attr)
            _Q_CACHE.append(mp.mpf(str(v)))
            return _Q_CACHE[0]
        except Exception:
            continue
    print("  WARNING: cannot resolve the substrate q — the Plancherel "
          "discriminator is DISABLED and every candidate below is unchecked "
          "for the weight-family false positive.", file=sys.stderr)
    _Q_CACHE.append(None)
    return None


def is_plancherel_not_markov(shape, value) -> bool:
    """True when this `y_lambda` field is the PLANCHEREL weight, not Jones–Markov.

    THE FALSE POSITIVE THIS EXISTS TO KILL. This audit keys on a FIELD NAME,
    and the docstring has always said a hit on a field that is not the Wenzl
    y_λ is a false positive it cannot rule out by itself. On 2026-09-03 it
    produced one: three witnesses reported as a convention-C REGRESSION after
    the fingerprint was left at 0/0, when the field was the symmetric
    Plancherel weight d_q²/[n]_q! — a quantity the convention-D row cap says
    nothing about, and which is positive at ≥3 rows by construction.

    The corpus already forbids the conflation those probes made: the three
    weight families y_λ / w_λ / w̃_λ are distinct at q ≠ 1 (AGENTS.md §7aa
    notation register), and `pyhecke.wedderburn.wedderburn_weight`'s own
    docstring warns that using the Plancherel weight in a Markov-trace context
    gives the wrong sum. So the discriminator is not a heuristic: recompute
    d_q²/[n]_q! and see whether the field IS it.

    Returns False on any failure — an unrecognised shape stays flagged, so a
    genuine convention-C hit is never silently dropped by this check.
    """
    q = _substrate_q()
    if q is None:
        return False          # cannot check -> stay flagged; _substrate_q warns
    try:
        from mpmath import mp
        mp.dps = 40
        w = _hook_weight(list(shape), q)
        if w is None:
            return False
        v = mp.mpf(str(value))
        if v == 0:
            return False
        # also accept the RECIPROCAL: four probes shipped H²/[n]_q! under this
        # same field name (the hook-inversion bug, PR #6442). Both are the
        # Plancherel family, neither is Jones–Markov.
        return (abs(v - w) / abs(w) < mp.mpf(10) ** -20
                or abs(v - 1 / w) / abs(1 / w) < mp.mpf(10) ** -20)
    except Exception:
        return False


def is_c_scale(value) -> bool:
    """Above the D-residue band. See C_SCALE_FLOOR for how it was measured."""
    try:
        return abs(float(str(value))) > C_SCALE_FLOOR
    except (TypeError, ValueError):
        return False


def scan_payload(obj) -> list[tuple]:
    """Every (partition, y) pair in this payload that D forbids."""
    hits: list[tuple] = []

    def walk(node):
        if isinstance(node, dict):
            y_key = next((k for k in node if k.lower() in Y_KEYS), None)
            lam_key = next((k for k in node if k.lower() in LAMBDA_KEYS), None)
            if y_key and lam_key:
                rows = rows_of(node[lam_key])
                if (rows is not None and rows >= MIN_ROWS
                        and is_c_scale(node[y_key])
                        and not is_plancherel_not_markov(node[lam_key], node[y_key])):
                    hits.append((node[lam_key], node[y_key]))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(obj)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root to scan")
    ap.add_argument("--json", help="write the full report here")
    ap.add_argument("--include-deprecated", action="store_true")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    report, scanned, deprecated = {}, 0, 0
    for path in sorted(root.rglob("computations/**/*.witness.json")):
        try:
            payload = json.loads(path.read_text())
        except Exception:
            continue
        scanned += 1
        hits = scan_payload(payload)
        if not hits:
            continue
        rel = str(path.relative_to(root))
        if ("_deprecated" in rel or "fsh-guts" in rel) and not args.include_deprecated:
            deprecated += 1
            continue
        report[rel] = {
            "computedAt": payload.get("computedAt") or payload.get("timestamp"),
            "n_fields": len(hits),
            "sample": [[lam, str(y)[:40]] for lam, y in hits[:3]],
        }

    if scanned == 0:
        print("ERROR: scanned 0 witnesses under "
              f"{root.resolve()} — wrong --root, or run from the repo root.\n"
              "A scan that examined nothing is NOT a clean tree.", file=sys.stderr)
        return 2

    total = sum(v["n_fields"] for v in report.values())
    print("=" * 74)
    print("CONVENTION-C FINGERPRINT — nonzero y_lambda on a >=3-row partition")
    print("=" * 74)
    print(f"  witnesses scanned          : {scanned}")
    print(f"  live files with fingerprint: {len(report)}")
    print(f"  fields                     : {total}")
    if deprecated:
        print(f"  (+ {deprecated} under _deprecated, excluded; --include-deprecated to show)")
    print()
    for rel, info in sorted(report.items()):
        print(f"  {info['n_fields']:4d}  {rel}")
        print(f"        computedAt: {info['computedAt']}")
        for lam, y in info["sample"][:2]:
            print(f"        lambda={lam}  y={y}")
    if report:
        print("\n  A hit is about the WITNESS, not the producer. Re-run the producer to")
        print("  tell a stale payload from a live source defect; the latter is worse.")
    if args.json:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        report.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            report, script_path=__file__, engine=None, q0_anchor=False)
        pathlib.Path(args.json).write_text(json.dumps(report, indent=2) + "\n")
        print(f"\n  wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
