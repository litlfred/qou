#!/usr/bin/env python3
# polynomial_q_not_applicable: read-only audit; recomputes to compare, writes no witness.
"""Re-derive each χ cache's crossing convention from its VALUES, not its label.

Owner directive: NO FLOAT64 — and a convention label that disagrees with the
numbers it describes is the provenance equivalent of fake precision.

## Why the labels cannot be read

`chi-deuteron-h6-at-q0-50dps.witness.json` declares
`convention: "averaged-crossings"` — colour-blind. Recomputing χ^λ(β_D) both
ways and comparing against the values actually stored:

    colour-blind      Σ|diff| = 3.13e-03
    colour-weighted   Σ|diff| = 4.23e-06

The stored numbers are colour-**weighted**. The label is wrong, and it is not
an isolated slip: `_avg_color_delta` has 16 live consumers and installs the
colour-weighted p–n crossing wherever it imports, so the pipeline computes one
thing while a subset of witnesses claim another.

That matters beyond tidiness. A survey over `convention` reported 11
`averaged-crossings` against 1 `colour-weighted-averaged-crossing` in the
`-at-q0-50dps` family, and that count was used to argue ⁴He was an outlier
worth repointing. Built on labels, the argument was worthless. **Any question
of the form "which convention does the corpus use" has to be answered from
values.**

## What this does

For each `chi-*-at-q0-50dps` witness it rebuilds the atom's braid word, computes
χ^λ over all partitions twice — once colour-blind (`d = −h/2` for every
averaged crossing) and once colour-weighted (`d = −h·(1/2 − δ/4)` for the p–n
ones) — and reports which one the stored values match, beside what the witness
claims.

Verdicts: `AGREES`, `MISLABELLED` (values match the other convention),
`INDISTINGUISHABLE` (the two conventions are the same computation for this
atom — true of proton and neutron, which have no inter-nucleon crossing),
`NEITHER` (close but not decisive — worth a human look, and what a stale q₀
anchor can look like), `SKIPPED`.

Read-only. It never writes a witness, so it is safe to run beside other work.

Usage:
    python3 computations/chi_convention_from_values_audit.py
    python3 computations/chi_convention_from_values_audit.py --atom deuteron
    python3 computations/chi_convention_from_values_audit.py --self-test
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

# Labels that mean each convention. Spellings vary across the corpus.
BLIND_LABELS = {"averaged-crossings", "sign-only-crossings"}
WEIGHTED_LABELS = {
    "colour-weighted-averaged-crossing",
    "color-weighted-averaged-crossing",
    "bring_color_weighted-averaged-crossings",
}

# A match must beat the alternative by this factor to be called. The two
# conventions differ by ~7e-5 in `d` and ~1e-3 in Σ|diff| at H_6, so a decisive
# result separates by orders of magnitude; anything closer is NEITHER.
DECISIVE_RATIO = 10.0


def convention_of_label(label) -> str | None:
    s = str(label).strip().lower()
    if s in {x.lower() for x in BLIND_LABELS}:
        return "blind"
    if s in {x.lower() for x in WEIGHTED_LABELS}:
        return "weighted"
    return None


def verdict(label, blind_diff, weighted_diff, n_pn: int | None = None) -> str:
    """Compare the two residuals and the label. Pure — self-tested below.

    `n_pn` is the count of colour-weighted (p-n) crossings in the word. When it
    is zero the two conventions are the SAME computation and no comparison can
    separate them — decided structurally rather than by comparing floats,
    because passing the shift as a decimal string and letting Rust derive h/2
    internally differ in the last bits, so the residuals are near-equal but not
    exactly equal. Reporting proton and neutron as problems would manufacture
    two false findings out of six atoms.
    """
    claimed = convention_of_label(label)
    if blind_diff is None or weighted_diff is None:
        return "SKIPPED"
    if n_pn == 0:
        return "INDISTINGUISHABLE"
    lo, hi = sorted((blind_diff, weighted_diff))
    if hi < lo * DECISIVE_RATIO:
        return "NEITHER"
    actual = "blind" if blind_diff < weighted_diff else "weighted"
    if claimed is None:
        return f"UNLABELLED({actual})"
    return "AGREES" if claimed == actual else "MISLABELLED"


def _measure(atom: str, Z: int, N: int, stored: dict, dps: int):
    """Σ|diff| of stored χ against each convention. Import-heavy; lazy."""
    import _path_bridge  # noqa: F401
    from mpmath import mp, mpf
    from mass_at_3A_proper import atom_braid_word_3A
    from _li_2_q_util import flavor_split_leading
    import pyhecke_native as pn
    from q_parameter import Q_50_DIGIT_STR

    with mp.workdps(dps):
        q_str = str(Q_50_DIGIT_STR)
        q = mpf(q_str)
        h = q - 1 / q
        # δ from the closed form at THIS q₀, not `_avg_color_delta()`, which
        # evaluates at the float64 `q_parameter.Q` and reaches only ~5e-16.
        # Once the producers went exact this audit became the COARSER side of
        # its own comparison — it still separated the two conventions
        # decisively (5.97e-19 weighted vs 3.13e-03 blind), but an audit
        # carrying the defect it exists to detect is not one to leave alone.
        cw = -h * (mpf(1) / 2 - flavor_split_leading(q) / 4)
        cwf = float(cw)
        n = 3 * (Z + N)
        word = [(c, cw if abs(float(d) - cwf) < 1e-9 else d, g)
                for (c, d, g) in atom_braid_word_3A(Z, N)]
        hf = float(h)

        def run(weighted: bool):
            ws, sh = [], []
            for c, d, g in word:
                df = float(d)
                if abs(df) < 1e-9:
                    ws.append((1, int(g) + 1)); sh.append("")
                elif abs(df + hf) < 1e-9:
                    ws.append((-1, int(g) + 1)); sh.append("")
                else:
                    ws.append((0, int(g) + 1))
                    sh.append(mp.nstr(-mp.mpf(d), dps + 10, strip_zeros=False)
                              if weighted else "")
            out = pn.chi_lambda_all_partitions_mpfr(
                n, ws, q_str, dps, sh if any(sh) else None)
            return {tuple(l): mpf(v) for l, v in out}

        got = {tuple(e["partition"]): mpf(e["chi_lambda"])
               for e in stored.get("by_partition", [])
               if "chi_lambda" in e}
        if not got:
            return None, None, 0
        n_pn = sum(1 for _, d, _ in word if abs(float(d) - cwf) < 1e-9)
        blind, weighted = run(False), run(True)
        db = sum(abs(blind[k] - v) for k, v in got.items() if k in blind)
        dw = sum(abs(weighted[k] - v) for k, v in got.items() if k in weighted)
        return float(db), float(dw), n_pn


CASES = [
    ("weighted values, weighted label", "colour-weighted-averaged-crossing",
     3.1e-3, 4.2e-6, "AGREES"),
    # The deuteron case that started this.
    ("weighted values, blind label", "averaged-crossings",
     3.1e-3, 4.2e-6, "MISLABELLED"),
    ("blind values, blind label", "averaged-crossings",
     4.2e-6, 3.1e-3, "AGREES"),
    ("blind values, weighted label", "colour-weighted-averaged-crossing",
     4.2e-6, 3.1e-3, "MISLABELLED"),
    # Neither fits: what a stale q0 anchor looks like — both residuals large
    # and comparable, so no convention is decisive.
    ("matches neither decisively", "averaged-crossings",
     2.0e-4, 3.0e-4, "NEITHER"),
    # proton / neutron: no p-n crossing, so both conventions are one
    # computation and the residuals are bit-identical.
    # proton / neutron: zero p-n crossings, so the residuals are near-equal
    # but NOT bit-equal (string shift vs internally derived h/2). Structural.
    ("A=1 atom: the conventions coincide", "averaged-crossings",
     3.31e-07, 3.3100000001e-07, "INDISTINGUISHABLE", 0),
    ("unknown label still reports the values", "who-knows",
     3.1e-3, 4.2e-6, "UNLABELLED(weighted)"),
    ("nothing measured", "averaged-crossings", None, None, "SKIPPED"),
]


def self_test() -> int:
    fails = 0
    for case in CASES:
        label, conv, db, dw, want = case[:5]
        n_pn = case[5] if len(case) > 5 else 4
        got = verdict(conv, db, dw, n_pn)
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


ATOMS = {"proton": (1, 0), "neutron": (0, 1), "deuteron": (1, 1),
         "tritium": (1, 2), "helium-3": (2, 1), "helium-4": (2, 2)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atom", action="append",
                    help="restrict to these atoms (default: all but helium-4, "
                         "which is hours at H_12)")
    ap.add_argument("--dps", type=int, default=50)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    atoms = a.atom or [x for x in ATOMS if x != "helium-4"]
    print(f"{'atom':<11} {'claims':<34} {'blind':>10} {'weighted':>10}  verdict")
    bad = 0
    for atom in atoms:
        if atom not in ATOMS:
            print(f"{atom:<11} not a known atom")
            continue
        Z, N = ATOMS[atom]
        n = 3 * (Z + N)
        p = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
        if not p.exists():
            print(f"{atom:<11} (no -at-q0-50dps witness)")
            continue
        stored = json.loads(p.read_text(encoding="utf-8"))
        try:
            db, dw, n_pn = _measure(atom, Z, N, stored, a.dps)
        except Exception as exc:  # noqa: BLE001
            print(f"{atom:<11} MEASURE FAILED: {type(exc).__name__}: {exc}")
            continue
        v = verdict(stored.get("convention"), db, dw, n_pn)
        bad += v not in {"AGREES", "INDISTINGUISHABLE"}
        fb = "n/a" if db is None else f"{db:.2e}"
        fw = "n/a" if dw is None else f"{dw:.2e}"
        print(f"{atom:<11} {str(stored.get('convention'))[:34]:<34} "
              f"{fb:>10} {fw:>10}  {v}")
    print("\nA label is only evidence when it AGREES; every survey over "
          "`convention`\nshould be re-derived from values until these are "
          "repaired.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
