#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath cross-check; no symbolic
# computation in this layer.
"""1 ppb cross-check: Wenzl LR vs Hoefsmit vs markov_peel.

Companion to `cross_check_trM_1ppb.py` (Hoefsmit ↔ markov_peel,
already in CI --strict). Adds the third path: the Wenzl LR bridge
from PR #674's `rho-k-full-via-wenzl-lr.witness.json` (per-atom
|tr_M| via Σ_λ y_λ · χ^λ_LR / averaging_denominator).

**Compute-precision goal (1 ppb):** independent compute paths
must agree at substrate q_0 to 1 part per billion. This is
distinct from the ~780 ppb CODATA Q_β floor on absolute
mass-prediction accuracy — see workplan v4 reframe.

Reports per-atom relative differences for every pair of
available paths:

  - Hoefsmit ↔ markov_peel    (same as cross_check_trM_1ppb)
  - Wenzl LR ↔ Hoefsmit
  - Wenzl LR ↔ markov_peel

Atoms with all three paths available: 5-atom Hoefsmit table
covers p, n, D, T, ³He; markov_peel covers more; Wenzl LR
currently covers D, T, ³He, ⁴He (per PR #679). Intersection
for full 3-way comparison: D, T, ³He.

Output: `cross-check-trM-wenzl-lr-1ppb.witness.json`.

CI gate: invoke with `--strict` to exit non-zero on any
divergence > 1e-9.

Usage:
    python3 computations/cross_check_trM_wenzl_lr_1ppb.py
    python3 computations/cross_check_trM_wenzl_lr_1ppb.py --strict

Per workplan v4 (docs/audits/2026-05-17-1ppb-workplan-v4.md):
this script lives in the "compute-precision" layer; the
~780 ppb floor lives in a separate validator layer
(`atomic_mass_via_rho_k.py`'s side-by-side CODATA comparison).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
from mpmath import fabs, mpf

HERE = Path(__file__).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

mpmath.mp.dps = 50
TOLERANCE = mpf("1e-9")  # 1 part per billion

# ANCHOR-MATCHED. The peel and Wenzl-LR witnesses are both PROTON-pinned; the
# base-name Hoefsmit witness is the MUON one (`atomic_tr_m_mpfr_50dps` is tagged
# `ideal_muon`). Comparing across that boundary put a floor under this
# cross-check that is ~100x its own 1e-9 target:
#
#     hoefsmit_vs_markov_peel, against the MUON bridge   6.9e-8 .. 2.5e-7
#
# Those are the SAME numbers the tr_m_q_hecke_seminormal straddle produced
# (PR #5723) -- the mu-p q0 gap of 11.5 ppb, amplified ~n-fold because tr_M is a
# product over ~n crossings. Against the proton twin the two paths agree
# exactly. Same defect, second site; `reference_anchor_straddle_audit` (#5727)
# is what says how many more there are.
HOEF_PATH = _pb.witness_path("atomic-tr-m-mpfr-50dps-proton.witness.json", HERE)
PEEL_PATH = _pb.witness_path("markov-peel-atomic-tr-m.witness.json", HERE)
LR_PATH = _pb.witness_path("rho-k-full-via-wenzl-lr.witness.json", HERE)


# Short LR labels → long Hoefsmit / peel atom names.
_LR_LABEL_TO_LONG = {
    "D": "deuteron",
    "T": "tritium",
    "3He": "helium-3",
    "4He": "helium-4",
    "6Li": "lithium-6",
    "7Li": "lithium-7",
}


def _rows_of(doc: dict, key: str) -> list:
    """Rows from `doc[key]` OR `doc["data"][key]` -- witnesses use both.

    `atomic-tr-m-mpfr-50dps` puts `results` at the TOP level (5 rows);
    `markov-peel-atomic-tr-m` puts it under `data` (6 rows). Every loader here
    read only the top level, so the peel path silently yielded ZERO atoms and
    two of this cross-check's three pair-types never ran at all. The failure was
    indistinguishable from "the file is missing", because `.get(key, [])`
    returns the same empty list either way -- so a THREE-way cross-check has
    been reporting on ONE pair since at least 2026-07-05 while printing the
    other two as simply absent.
    """
    rows = doc.get(key)
    if not rows:
        rows = (doc.get("data") or {}).get(key)
    return rows or []


def _mpmathify(s: str) -> mpf:
    return mpf(str(s))


def load_hoefsmit() -> dict[str, mpf]:
    if not HOEF_PATH.exists():
        return {}
    d = json.loads(HOEF_PATH.read_text())
    out: dict[str, mpf] = {}
    for r in _rows_of(d, "results"):
        atom = r.get("atom")
        tr = r.get("tr_M_at_q0_50dps")
        if atom and tr:
            out[atom] = abs(_mpmathify(tr))
    return out


def load_peel() -> dict[str, mpf]:
    if not PEEL_PATH.exists():
        return {}
    d = json.loads(PEEL_PATH.read_text())
    out: dict[str, mpf] = {}
    for r in _rows_of(d, "results"):
        atom = r.get("atom")
        if atom is None or "error" in r:
            continue
        tr = r.get("tr_M_at_q0") or r.get("tr_M_at_q0_str")
        if tr:
            out[atom] = abs(_mpmathify(tr))
    return out


def load_wenzl_lr() -> dict[str, mpf]:
    """Returns Wenzl-LR |tr_M| values keyed by *long* atom name
    (deuteron, tritium, ...) so the comparison maps directly onto
    the Hoefsmit / peel tables."""
    if not LR_PATH.exists():
        return {}
    d = json.loads(LR_PATH.read_text())
    out: dict[str, mpf] = {}
    for r in _rows_of(d, "rows"):
        if "tr_M_q0_unavail_reason" in r:
            continue
        short = r.get("atom")
        tr = r.get("abs_tr_M_q0_mp30dps") or r.get("tr_M_q0_mp30dps")
        if short is None or tr is None:
            continue
        long_name = _LR_LABEL_TO_LONG.get(short, short)
        out[long_name] = abs(_mpmathify(tr))
    return out


def relative_delta(a: mpf, b: mpf) -> mpf:
    if a == 0 and b == 0:
        return mpf(0)
    denom = max(fabs(a), fabs(b))
    return fabs(a - b) / denom


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any divergence > 1 ppb")
    ap.add_argument("--dps", type=int, default=50)
    args = ap.parse_args()
    mpmath.mp.dps = args.dps

    hoef = load_hoefsmit()
    peel = load_peel()
    wlr = load_wenzl_lr()
    all_atoms = sorted(set(hoef) | set(peel) | set(wlr))

    print("=" * 88)
    print("  Wenzl LR ↔ Hoefsmit ↔ markov_peel cross-check at q_0 "
          f"(1 ppb compute target)")
    print("=" * 88)
    print(f"  dps: {args.dps}  |  tolerance: {TOLERANCE} (1 ppb)")
    print(f"  Hoefsmit atoms:   {sorted(hoef)}")
    print(f"  markov_peel atoms: {sorted(peel)}")
    for _label, _got, _path in (("Hoefsmit", hoef, HOEF_PATH),
                                ("markov_peel", peel, PEEL_PATH),
                                ("Wenzl LR", wlr, LR_PATH)):
        if not _got:
            print(f"  !! {_label} path contributed ZERO atoms — "
                  f"{'file missing' if not _path.exists() else 'file present but no rows parsed'}"
                  f": {_path.name}")
    print(f"  Wenzl LR atoms:    {sorted(wlr)}")
    print()

    rows: list[dict] = []
    any_diverge = False

    # THE WENZL-LR PAIRS MEASURE A DIFFERENT OBJECT, BY DESIGN AND ON RECORD.
    # `rho_k_full_via_wenzl_lr.py`'s own docstring, since 2026-05-17 and found by
    # THIS script:
    #
    #   "the Wenzl LR identity chi^lambda(b1 (x) b2) = sum c^lam_{mu,nu} ...
    #    applies to TENSOR-PRODUCT (disjoint) braids only. The canonical atomic
    #    braid ... is NOT a tensor product -- it includes inter-nucleon arc
    #    crossings. This script therefore computes |tr_M(b_p (x) b_n (x) ...)|,
    #    NOT |tr_M(b_canonical(Z, N))|. The two diverge by ~80% relative on
    #    D, T, 3He."
    #
    # So a 1e-9 tolerance was being applied across a KNOWN inequality of
    # quantities, and the resulting ~0.9 was reported as a precision failure for
    # months. It is a scope difference, not a divergence: the disjoint product
    # omits exactly the inter-nucleon crossings the canonical braid carries.
    # Reported as SCOPE, excluded from `any_diverge`, and NOT asserted on.
    _SCOPE_PAIRS = {"hoefsmit_vs_wenzl_lr", "markov_peel_vs_wenzl_lr"}

    def _compare(atom: str, name_a: str, val_a: mpf,
                 name_b: str, val_b: mpf) -> dict:
        nonlocal any_diverge
        rel = relative_delta(val_a, val_b)
        ok = rel < TOLERANCE
        pair = f"{name_a}_vs_{name_b}"
        scope = pair in _SCOPE_PAIRS
        if not ok and not scope:
            any_diverge = True
        return {
            "atom": atom,
            "pair": pair,
            "compares_same_object": not scope,
            "scope_note": (None if not scope else
                           "disjoint tensor product vs canonical braid — the "
                           "Wenzl LR identity does not apply to the canonical "
                           "atomic braid (inter-nucleon arc crossings); see "
                           "rho_k_full_via_wenzl_lr.py docstring"),
            "value_a": mpmath.nstr(val_a, 20),
            "value_b": mpmath.nstr(val_b, 20),
            "rel_diff": mpmath.nstr(rel, 6),
            "within_1ppb": bool(ok),
        }

    print(f"  {'atom':<14} {'pair':<26}  {'|Δ_rel|':>14}  status")
    print("  " + "─" * 60)
    for atom in all_atoms:
        h = hoef.get(atom)
        p = peel.get(atom)
        w = wlr.get(atom)
        # Build all available pairs.
        pairs = []
        if h is not None and p is not None:
            pairs.append(("hoefsmit", h, "markov_peel", p))
        if h is not None and w is not None:
            pairs.append(("hoefsmit", h, "wenzl_lr", w))
        if p is not None and w is not None:
            pairs.append(("markov_peel", p, "wenzl_lr", w))
        for (na, va, nb, vb) in pairs:
            row = _compare(atom, na, va, nb, vb)
            rows.append(row)
            status = ("OK" if row["within_1ppb"]
                      else ("SCOPE" if not row["compares_same_object"]
                            else "DIVERGE"))
            print(f"  {atom:<14} {row['pair']:<26}  "
                  f"{row['rel_diff']:>14}  {status}")

    # Summary by path-pair.
    by_pair: dict[str, dict] = {}
    for r in rows:
        p = r["pair"]
        if p not in by_pair:
            by_pair[p] = {"n": 0, "n_diverge": 0, "max_rel": mpf(0)}
        by_pair[p]["n"] += 1
        if not r["within_1ppb"]:
            by_pair[p]["n_diverge"] += 1
        rel = mpf(r["rel_diff"])
        if rel > by_pair[p]["max_rel"]:
            by_pair[p]["max_rel"] = rel

    print()
    print("  Summary by path-pair:")
    for p, s in sorted(by_pair.items()):
        max_rel_str = mpmath.nstr(s["max_rel"], 4)
        print(f"    {p:<28}: n={s['n']:>2}  diverge={s['n_diverge']:>2}  "
              f"max|Δ_rel|={max_rel_str}")

    out = {
        "computation": "cross-check-trM-wenzl-lr-1ppb",
        "description": (
            "Cross-check |tr_M(canonical β_atom)| across the three "
            "independent compute paths at q_0 (Hoefsmit / markov_peel "
            "/ Wenzl LR). 1 ppb compute-precision target. Distinct "
            "from the ~780 ppb CODATA mass-prediction floor."
        ),
        "tolerance_rel": "1e-9",
        "dps": args.dps,
        "n_atoms_total": len(all_atoms),
        "n_pairs_total": len(rows),
        "n_pairs_diverge": sum(
            1 for r in rows if not r["within_1ppb"]
        ),
        "all_pairs_within_1ppb": not any_diverge,
        "rows": rows,
        "by_pair_summary": {
            p: {
                "n": s["n"],
                "n_diverge": s["n_diverge"],
                "max_rel_diff": mpmath.nstr(s["max_rel"], 6),
            }
            for p, s in sorted(by_pair.items())
        },
    }

    # ASSERTIONS, at last. The witness recorded `assertions: []` and
    # `allPassed: true` while every pair-test diverged -- so a 1-ppb gate could
    # fail by eight orders of magnitude with nothing downstream able to see it,
    # and without `--strict` the process still exited 0. Wiring them was blocked
    # on knowing WHAT to assert: with the Wenzl-LR pairs now identified as a
    # different object (SCOPE, above) the answer is unambiguous -- assert the
    # same-object comparisons, and assert nothing about the scope ones.
    _wb = WitnessBuilder.wrap_legacy(
        "cross-check-trM-wenzl-lr-1ppb", out,
        script_path=__file__, engine="mpmath",
    )
    for _r in rows:
        if not _r["compares_same_object"]:
            continue
        _wb.add_assertion(
            name=f"within_1ppb[{_r['atom']}][{_r['pair']}]",
            # `expected` is compared NUMERICALLY (the builder coerces with
            # float()), so it must be a number: "< 1e-9" made every assertion
            # fail on values as small as 2.6e-50. The relative difference is
            # asserted to be ZERO within the 1 ppb tolerance.
            computed=str(_r["rel_diff"]),
            expected="0",
            tolerance="1e-9",
            source=("independent compute paths for the SAME object "
                    "(canonical atomic braid) must agree to 1 ppb"),
        )
    out_path = _wb.save()
    print(f"\n  Witness: {out_path.name}")
    print(f"  Atoms compared: {len(all_atoms)}, pair-tests: "
          f"{len(rows)}, divergent: "
          f"{sum(1 for r in rows if not r['within_1ppb'])}")

    if args.strict and any_diverge:
        print("\n  STRICT MODE: at least one pair-test diverged > 1 ppb",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
