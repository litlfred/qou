#!/usr/bin/env python3
"""color_tube_flavor_isospin_selection.py — the flavor side of the color-tube weight.

Bean qou-63n2, continuing qou-ctkw (PR #4506).

The COLOR side is settled: ordered color-sheet pairs carry `T1 (x) T1 = A + T1 + H`,
with the forced Z/2 grading `Sym^2 = A + H` (dim 6) / `Alt^2 = T1` (dim 3). That
narrowed the weight tensor `W_{c1c2}(F1,F2)` from 8 free parameters per flavor
pair to a 2-parameter convex family. What it did NOT supply is the FLAVOR
dependence `(F1,F2)`.

THE OBSERVATION: flavor is a representation too. Quark flavors `(u,d)` form the
isospin doublet `I=1/2`, and the nucleon is the `I=1/2` part of
`(1/2)^(x)3 = 3/2 + 1/2 + 1/2`. So a nucleon PAIR carries

    I=1/2 (x) I=1/2  =  I=1 (triplet)  +  I=0 (singlet)      (3 + 1 = 4)

  I=1 : pp, (pn+np)/sqrt2, nn        (exchange-SYMMETRIC)
  I=0 : (pn-np)/sqrt2                (exchange-ANTISYMMETRIC)

THE SELECTION RULE (conditional — the hypothesis is named, not hidden): IF the
two-nucleon interface carries definite antisymmetry under SIMULTANEOUS exchange
of the two nucleons' color-sheet and flavor labels, then only two couplings
survive:

    color-Sym (A + H)  (x)  flavor-Alt (I=0)
    color-Alt (T1)     (x)  flavor-Sym (I=1)

This probe derives the consequences and, critically, extracts a FALSIFIABLE
prediction rather than a fitted number.

CONSEQUENCE (the falsifiable part): the like-nucleon channels pp and nn are BOTH
I=1, so under the rule they receive the SAME color weighting (the T1 system) —
the weight tensor CANNOT distinguish pp from nn. That is exactly the charge
symmetry the corpus's own CSB analysis demands: the production sigma-vs-sigma^-1
assignment breaks charge symmetry by ~78%, some 570x the substrate-derived p/n
split and ~78x the experimental CSB bound, and the gg-production probe showed
forcing all bonds to the flavor-blind average collapses that asymmetry to 0.

STRICT anti-fit: no target is consulted and nothing is tuned. The exchange
antisymmetry is an ASSUMPTION about the interface and is reported as such — this
is a CONDITIONAL narrowing, not a closure. The agreement with the CSB
requirement is a POST-HOC CHECK of a rule fixed beforehand by representation
theory, not an input to it.

Run:  python3 -u color_tube_flavor_isospin_selection.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

import sympy as sp  # noqa: E402

_T0_MONO = time.monotonic()

# Color-side normalised weight systems (PR #4506): (same-color, different-color)
COLOR_WEIGHTS = {
    "A":  (sp.Rational(1, 3), sp.Integer(0)),
    "T1": (sp.Integer(0), sp.Rational(1, 6)),
    "H":  (sp.Rational(2, 15), sp.Rational(1, 10)),
}

# Nucleon pairs and their isospin content.
PAIRS = {
    "pp": {"I": 1, "exchange": "sym"},
    "nn": {"I": 1, "exchange": "sym"},
    "pn_sym": {"I": 1, "exchange": "sym"},
    "pn_alt": {"I": 0, "exchange": "alt"},
}


def main() -> int:
    print("=" * 82)
    print("Flavor side of W: isospin selection on the color-pair decomposition")
    print("=" * 82)

    # ── isospin decomposition of the nucleon pair (exact dimension check) ────
    d_doublet = 2
    d_triplet, d_singlet = 3, 1
    assert d_doublet * d_doublet == d_triplet + d_singlet
    print(f"\nI=1/2 (x) I=1/2 = I=1 + I=0   ({d_doublet}x{d_doublet} = "
          f"{d_triplet}+{d_singlet} = {d_triplet + d_singlet})  OK")
    print("  I=1 (dim 3, exchange-SYMMETRIC) : pp, (pn+np)/sqrt2, nn")
    print("  I=0 (dim 1, exchange-ANTISYM)   : (pn-np)/sqrt2")

    # ── the selection rule ──────────────────────────────────────────────────
    print("\nSelection rule (CONDITIONAL on interface exchange-antisymmetry):")
    print("  color-Sym (A+H, dim 6)  x  flavor-Alt (I=0, dim 1)   -> overall ALT")
    print("  color-Alt (T1,  dim 3)  x  flavor-Sym (I=1, dim 3)   -> overall ALT")
    print("  (the two mixed pairings give overall SYM and are excluded)")

    # ── consequences per nucleon pair ───────────────────────────────────────
    print("\nInduced color weighting per nucleon pair:")
    print(f"  {'pair':8s} {'I':>2s} {'exch':>5s}  {'color system':16s} "
          f"{'w(same)':>9s} {'w(diff)':>9s}")
    induced = {}
    for name, info in PAIRS.items():
        if info["I"] == 1:
            system, (ws, wd) = "T1 (forced)", COLOR_WEIGHTS["T1"]
        else:
            system = "A+H (1 param)"
            ws, wd = None, None
        induced[name] = {
            "I": info["I"], "exchange": info["exchange"], "color_system": system,
            "w_same": str(ws) if ws is not None else "free in [A,H] mix",
            "w_diff": str(wd) if wd is not None else "free in [A,H] mix",
        }
        print(f"  {name:8s} {info['I']:>2d} {info['exchange']:>5s}  {system:16s} "
              f"{str(ws) if ws is not None else '—':>9s} "
              f"{str(wd) if wd is not None else '—':>9s}")

    # ── the falsifiable consequence ─────────────────────────────────────────
    pp_w = (induced["pp"]["w_same"], induced["pp"]["w_diff"])
    nn_w = (induced["nn"]["w_same"], induced["nn"]["w_diff"])
    charge_symmetric = (pp_w == nn_w)

    # parameter accounting
    params_before_color = 8      # arbitrary nonneg normalised 9-vector
    params_after_color = 2       # convex combination of A, T1, H
    params_after_flavor = 1      # I=1 forced to T1; I=0 is a 1-param A/H mix

    print("\n" + "=" * 82)
    print("FALSIFIABLE CONSEQUENCE")
    print("=" * 82)
    print(f"  pp weights = {pp_w}")
    print(f"  nn weights = {nn_w}")
    print(f"  => W is CHARGE-SYMMETRIC between pp and nn: {charge_symmetric}")
    print("     (both are I=1, so the rule forces the SAME color system on them —")
    print("      the weight tensor CANNOT distinguish pp from nn.)")
    print("\n  This is exactly what the corpus's CSB analysis requires: the production")
    print("  sigma-vs-sigma^-1 assignment breaks charge symmetry by ~78% (~570x the")
    print("  substrate-derived p/n split, ~78x the experimental CSB bound), and the")
    print("  gg-production probe showed the flavor-blind average collapses it to 0.")
    print("  The rule was fixed by representation theory BEFORE this comparison —")
    print("  the agreement is a post-hoc CHECK, not an input.")
    print(f"\n  Parameter count: {params_before_color} (bare) -> "
          f"{params_after_color} (color side, PR #4506) -> "
          f"{params_after_flavor} (this rule).")
    print("\n  OPEN: the single remaining parameter is the A/H mix in the I=0")
    print("  (deuteron) channel. NOT closed here. Choosing it to match any target")
    print("  would be a fit.")

    w = WitnessBuilder("color-tube-flavor-isospin-selection", engine="python",
                       start_time=_T0_MONO)
    w.set_description(
        "Bean qou-63n2, the flavor side of the color-tube weight tensor W, continuing "
        "qou-ctkw / PR #4506 (which settled the color side: T1 (x) T1 = A + T1 + H with "
        "forced Sym^2/Alt^2 grading, narrowing W from 8 free parameters to 2). "
        "Observation: flavor is a representation too — a nucleon pair carries "
        "I=1/2 (x) I=1/2 = I=1 (sym, dim 3) + I=0 (alt, dim 1). CONDITIONAL selection "
        "rule (hypothesis named, not hidden): IF the interface carries definite "
        "antisymmetry under simultaneous exchange of color-sheet and flavor labels, only "
        "color-Sym(A+H) x flavor-Alt(I=0) and color-Alt(T1) x flavor-Sym(I=1) survive. "
        "FALSIFIABLE CONSEQUENCE: pp and nn are both I=1, so W is forced to be "
        "CHARGE-SYMMETRIC between them — the weight tensor cannot distinguish pp from "
        "nn. That is exactly what the corpus CSB analysis demands (the production "
        "sigma/sigma^-1 assignment over-breaks charge symmetry by ~78%, ~570x the "
        "substrate p/n split; the gg-production probe collapses it to 0 under the "
        "flavor-blind average). The rule is fixed by representation theory BEFORE the "
        "comparison, so the agreement is a post-hoc check, not an input. Parameter "
        "count 8 -> 2 (color) -> 1 (this rule). OPEN: the remaining A/H mix in the I=0 "
        "deuteron channel is NOT closed; choosing it to match a target would be a fit. "
        "CONDITIONAL narrowing, not a closure; nothing wired; no target consulted."
    )
    w.add_data("isospin_decomposition", {"doublet_sq": 4, "triplet": 3, "singlet": 1})
    w.add_data("induced_weighting_per_pair", induced)
    w.add_data("parameter_count",
               {"bare": params_before_color, "after_color_side": params_after_color,
                "after_isospin_rule": params_after_flavor})
    w.add_assertion(
        "isospin_pair_decomposition_dims",
        computed=float(d_triplet + d_singlet), expected=4.0, tolerance=0.0,
        source="I=1/2 (x) I=1/2 = I=1 + I=0 with dims 3 + 1 = 4 = 2x2. The nucleon pair "
               "flavor space decomposes canonically, with I=1 exchange-symmetric and "
               "I=0 exchange-antisymmetric.",
    )
    w.add_assertion(
        "W_charge_symmetric_between_pp_and_nn",
        computed=1.0 if charge_symmetric else 0.0, expected=1.0, tolerance=0.0,
        source="THE FALSIFIABLE CONSEQUENCE. pp and nn both sit in the I=1 triplet, so "
               "the selection rule forces the same color weighting (the T1 system: 0 on "
               "same-color pairs, 1/6 on each different-color pair) on both. W therefore "
               "cannot distinguish pp from nn — charge symmetry is a CONSEQUENCE of the "
               "rule, not an imposed constraint. Would be false if the rule permitted "
               "pp and nn to draw on different color summands.",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
