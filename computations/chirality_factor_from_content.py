#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; chirality factor from the
# ribbon-eigenvalue linearization, no symbolic-q polynomial output.
"""
Chirality factor from the ribbon eigenvalue — wire the det_q=framing Lean.

The just-formalized result (ChiralityWritheRibbon.lean, sorry-free) proves the
chirality factor's first-order coefficient is the character-weighted average
Jucys–Murphy content:
    a_K(β) = 1 + w · h · ⟨κ⟩_β + O(h²),   ⟨κ⟩_β = Σ_λ y_λ χ^λ(β) κ_λ / Σ_λ y_λ χ^λ(β),
with h = q − q⁻¹, w = writhe(β), κ_λ = Σ_{x∈λ}(col − row) (total content).

This script computes every piece from the q-parameterised core + combinatorics
and TESTS the ribbon prediction against the empirical multiplicative
pn-crossing rule (a_D = 1+h ⟹ coeff +1; a_T = a_³He = 1−h² and a_⁴He = (1−h²)²
⟹ first-order coeff 0). A match would DERIVE the empirical chirality factors
from the ribbon eigenvalue; a residual quantifies the open conjecture exactly
(the audit flagged 8 trace-variants missing by >20%).

Exploratory; no fit.

Run:  python3 -u computations/chirality_factor_from_content.py 2>&1 | tee /tmp/chi.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# atom knots; empirical first-order chirality coefficient (coeff of h in a_K)
ISO = [("D", 1, 1, 1), ("3H", 1, 2, 0), ("3He", 2, 1, 0), ("4He", 2, 2, 0)]


def content_sum(lam) -> int:
    """κ_λ = Σ_{x∈λ} (col − row), cells 0-indexed (Jucys–Murphy total content)."""
    return sum(j - i for i, part in enumerate(lam) for j in range(part))


def writhe(word) -> int:
    """Net writhe of the braid word: σ (d≈0) → +1, σ⁻¹ (d≈−h) → −1,
    averaged/color-pn (d≈−h/2-ish) → 0 (sign-balanced).

    LEVEL OF DEFINITION (framing note; no number here changes). The writhe is a
    property of the BRAID WORD, not of its closure: Markov-I (conjugation)
    invariant, but Markov-II stabilisation β ∈ B_n ↦ βσ_n^{±1} ∈ B_{n+1} shifts
    it by ±1 while presenting the same link. The four rows of `ISO` sit at
    n = 3(Z+N) strands (`atom-knot.md`), and not at a common one:

        D  n = 6      ³H  n = 9      ³He n = 9      ⁴He n = 12

    n(K) is the braid index — the lowest level of the substrate tower. Under the
    owner ruling (states are Gröbner–Shirshov normal forms; the observable is the
    trace at the lowest level) these canonical words ARE the states, so comparing
    w across isotopes compares distinct states rather than two presentations of
    one state: the table below stands as written. What w is not is a property of
    the closure.

    This note is bookkeeping only and explains nothing about the result. The four
    ✗ rows are a genuine ribbon-vs-empirical mismatch measured at the levels the
    framework itself assigns; the level accounting neither causes them nor
    softens them. Ref: docs/audits/2026-08-10-writhe-level-of-definition.md §5d.
    """
    h = float(mp.mpf(str(Q0)) - 1 / mp.mpf(str(Q0)))
    w = 0
    for _c, d, _g in word:
        df = float(d)
        if abs(df) < 1e-9:
            w += 1
        elif abs(df + h) < 1e-9:
            w -= 1
        # averaged / color-pn → 0
    return w


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(str(Q0)); h = q0 - 1 / q0
    print("\n  CHIRALITY FACTOR FROM THE RIBBON EIGENVALUE  a_K = 1 + w·h·⟨κ⟩")
    print(f"  q₀={float(q0):.6f}  h={float(h):.6f}\n")
    print("| iso | A | writhe w | ⟨κ⟩ | w·⟨κ⟩ | a_K ribbon (1st-order coeff) | empirical coeff | match? |")
    print("|---|--:|--:|--:|--:|--:|--:|:--:|")
    for name, Z, N, emp in ISO:
        n = 3 * (Z + N)
        word = atom_braid_word_3A(Z, N, include_inter=True)
        w = writhe(word)
        chi = chi_all_lambda_reduced_block(word, n, q=q0)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
        num = mp.mpf(0); den = mp.mpf(0)
        for lam, cval in chi.items():
            lt = tuple(lam)
            yl = y.get(lt, mp.mpf(0))
            num += yl * cval * content_sum(lt)
            den += yl * cval
        kappa_avg = num / den if den != 0 else mp.mpf('nan')
        coeff = w * float(kappa_avg)          # first-order coeff of h in a_K
        match = "✓" if abs(coeff - emp) < 0.05 else "✗"
        print(f"| {name} | {Z+N} | {w} | {float(kappa_avg):.4f} | {float(w*kappa_avg):.4f} "
              f"| {coeff:.4f} | {emp} | {match} |")
    print("\n  Reading: the ribbon first-order coeff is w·⟨κ⟩. Empirically the "
          "pn-crossing rule gives coeff +1 (D, one +crossing) and 0 (T/³He/⁴He, "
          "writhe-balanced). A ✓ means the Lean-proved ribbon eigenvalue "
          "reproduces the empirical chirality; ✗ quantifies the open gap "
          "(full-braid writhe + ⟨κ⟩ vs the pn-only empirical rule).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
