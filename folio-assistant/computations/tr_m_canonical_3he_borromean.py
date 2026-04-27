#!/usr/bin/env python3
"""
Plan G — first concrete step on the unblocked target.

³He has α* = 1.000 in joint-tower-sdp-rust.witness.json (all 3 H_3
Wedderburn blocks PSD), `rho_factor = 2`, `b_ame = 7.718 MeV`,
braid word = σ_1^{-1} σ_2 σ_1^{-1} σ_2 σ_1^{-1} σ_2 in B_3
(L_6a4 / Borromean rings link, 6 crossings, alternating sign
convention).

This script's intended deliverable is the symbolic Markov trace
tr_M(T_w) at q_0 for ³He's canonical T_w via the categorical pipeline,
to replace the SnapPy `Vol_hyp(L_6a4)` shortcut currently in use.

** STATUS — blocked on GB-NF normalisation **

The naive Hecke-quadratic expansion (σ_1^{-1} = σ_1 − h, then
sum over 2^3 sign combinations of positive words) hits a
`NotImplementedError("Complex braid case (multiple top-1 in segment)")`
in markov_trace_canonical.tr_M_word for the interleaved positive
words like (1, 0, 1, 0, 1) that the expansion produces. The
function only handles words after a Gröbner-Shirshov normalisation
pass.

The correct path is the same one atom_nf_symbolic_D.py uses for ²H:
  1. Build the inverse-containing braid as a SymbolicHeckeElement
     (hecke_symbolic.py).
  2. Apply SymbolicHeckeDivision (GB-NF reduction) to get a
     normal-form sum of basis words.
  3. tr_M_element on the NF (which calls tr_M_word per term, but
     only on already-normalised basis words).

The script below preserves the naive expansion code as a
documentation-of-intent; the working path needs adaptation of
atom_nf_symbolic_D.py for ³He's 6-letter braid in B_3. Effort:
2-3 h. See docs/plans/G-status-and-narrowing.md.
"""
from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp
from mpmath import mp, mpf

mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from markov_trace_canonical import tr_M_word, Z_SYMB, H_SYMB

HERE = Path(__file__).parent
Q0_WITNESS = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "tr-m-canonical-3he-borromean.witness.json"

# Constants
M_E_MEV = mpf("0.51099895")  # CODATA 2022 (will be lifted to mpf source later)
SNAPPY_VOL_L_6A4 = mpf("7.32772")  # Borromean rings, SnapPy 3.3.2 (~6 sig digits)


def borromean_tr_m_symbolic() -> sp.Expr:
    """
    tr_M(σ_1^{-1} σ_2 σ_1^{-1} σ_2 σ_1^{-1} σ_2) on B_3, symbolically in q.

    Using σ_1^{-1} = σ_1 − h, the braid expands as a sum of 8 words:
        Σ_{ε ∈ {+, -}^3} (-h)^{(# minus)} · [s_ε σ_2 s_ε σ_2 s_ε σ_2]
    where s_ε = σ_1 if ε = +, else 1 (the identity).
    """
    q = sp.symbols("q", positive=True)
    z = Z_SYMB
    h = H_SYMB
    total = sp.S(0)
    for eps in product([0, 1], repeat=3):  # 0 = identity, 1 = σ_1
        coeff = (-h) ** (3 - sum(eps))
        # Build the word — interleave s_ε with σ_2.
        word = []
        for e in eps:
            if e == 1:
                word.append(0)  # σ_1 (0-indexed)
            word.append(1)      # σ_2 (0-indexed)
        # Note: when e=0, we omit the σ_1 generator entirely (identity).
        word_tuple = tuple(word)
        tr = tr_M_word(word_tuple, n=3, z=z, h=h)
        total += coeff * tr
    return sp.simplify(total)


def main() -> int:
    print("\n  Computing tr_M(³He Borromean) symbolically in q...")
    tr_symbolic = borromean_tr_m_symbolic()
    print(f"\n  tr_M (symbolic) = {tr_symbolic}")

    # Load q_0 to 50 dps from the pinned-q witness.
    q0 = json.load(open(Q0_WITNESS))
    q_0_str = q0["derived_50_digit"]["q"]
    q_0 = mpf(q_0_str)
    print(f"\n  q_0 (50 dps) = {q_0_str}")

    # Substitute q = q_0 in the symbolic trace.
    q = sp.symbols("q", positive=True)
    # Convert to mpmath for 50-dps eval.
    tr_at_q0_str = sp.N(tr_symbolic.subs(q, sp.Float(q_0_str, 50)), 50)
    tr_at_q0 = mpf(str(tr_at_q0_str))
    print(f"\n  tr_M at q_0 = {tr_at_q0}")

    # Compare to the SnapPy shortcut: 2 m_e × Vol_hyp(L_6a4).
    snappy_b = 2 * M_E_MEV * SNAPPY_VOL_L_6A4
    print(f"\n  SnapPy shortcut: 2 m_e × Vol(L_6a4) = {snappy_b} MeV")

    # The Markov trace gives (in the mass identity)
    # B(³He) = m_e · ρ · tr_M(T_w)|_{q=q_0} = m_e · 2 · tr_at_q0
    # if rho_factor = 2 from the certificate.
    b_pred_categorical = 2 * M_E_MEV * tr_at_q0
    print(f"\n  Categorical: m_e × 2 × tr_M(q_0) = {b_pred_categorical} MeV")
    print(f"  AME 2020 B(³He)         = 7.718 MeV")

    out = {
        "computation": "tr-m-canonical-3he-borromean",
        "description":
            "Plan G first concrete step. Symbolic Markov trace of "
            "³He's canonical Borromean braid σ_1^{-1} σ_2 (×3) on "
            "B_3, evaluated at q_0 to 50 dps. Replaces the SnapPy "
            "Vol_hyp(L_6a4) shortcut for ³He with the categorical "
            "pipeline's exact tr_M(T_w) value.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "atom": "³He",
        "braid_word_rust_convention": [-1, 2, -1, 2, -1, 2],
        "braid_word_python_0indexed_with_inverses": "(σ_0)^{-1} σ_1 (σ_0)^{-1} σ_1 (σ_0)^{-1} σ_1",
        "n_strands": 3,
        "rho_factor": 2,
        "tr_m_symbolic": str(tr_symbolic),
        "q_0_50dps": q_0_str,
        "tr_m_at_q0_50dps": str(tr_at_q0),
        "comparison": {
            "snappy_shortcut_b_mev": str(snappy_b),
            "snappy_vol_l_6a4": str(SNAPPY_VOL_L_6A4),
            "categorical_b_pred_mev": str(b_pred_categorical),
            "ame_2020_b_mev": "7.718",
            "categorical_minus_ame_mev": str(b_pred_categorical - mpf("7.718")),
            "categorical_minus_ame_ppm":
                str((b_pred_categorical - mpf("7.718")) / mpf("7.718") * mpf("1000000")),
        },
    }

    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
