#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; pn-sector-restricted chirality
# coefficient, no symbolic-q polynomial output.
"""
pn-sector-restricted chirality probe — is the empirical pn-rule the ribbon
eigenvalue once intra-Borromean crossings are excluded?

`chirality_factor_from_content.py` found the FULL ribbon coefficient
`w·⟨κ⟩` (whole-atom writhe × whole-atom average content) overshoots the
empirical multiplicative pn-crossing rule by ~37× (D: 37.06 vs +1). The
empirical rule, however, counts ONLY inter-nucleon (pn) crossings. This probe
restricts the ribbon formula to the pn-sector and asks whether the gap closes:

  • w_pn  = writhe of ONLY the inter-nucleon crossings (gen ≡ 2 mod 3),
            excluding the intra-Borromean (σ₀σ₁⁻¹)³ + gluon σ₀ of each nucleon.
  • ⟨κ⟩_pn = the average content of the elementary 2-nucleon pn bond (the
            deuteron sub-braid), the per-bond ribbon content.

Ribbon coefficient candidates (coeff of h in a_K), vs the empirical
(D → +1; T,³He,⁴He → 0):
  full      : w_full · ⟨κ⟩_full      (the 37× overshoot, for reference)
  pn-writhe : w_pn   · ⟨κ⟩_full      (restrict writhe only)
  pn-sector : w_pn   · ⟨κ⟩_pn        (restrict BOTH — the genuine pn-sector)

A pn-sector match would DERIVE the empirical chirality factors from the ribbon
eigenvalue; a residual quantifies the open conjecture exactly. Exploratory; no fit.

Run:  python3 -u computations/chirality_pn_sector_probe.py 2>&1 | tee /tmp/pnchi.log
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
    """κ_λ = Σ_{x∈λ}(col − row), 0-indexed (total Jucys–Murphy content)."""
    return sum(j - i for i, part in enumerate(lam) for j in range(part))


def _writhe(word, pn_only: bool) -> int:
    """Net writhe: σ (d≈0) → +1, σ⁻¹ (d≈−h) → −1, averaged/pn → 0. If
    `pn_only`, count ONLY inter-nucleon crossings (generator index ≡ 2 mod 3).

    LEVEL OF DEFINITION (framing note; no number here changes). Both w_full and
    w_pn are properties of the BRAID WORD, not of its closure: Markov-I
    (conjugation) invariant, but Markov-II stabilisation β ∈ B_n ↦ βσ_n^{±1} ∈
    B_{n+1} shifts w by ±1 while presenting the same link. The `ISO` rows sit at
    n = 3(Z+N) strands (`atom-knot.md`), which differ row to row:

        D  n = 6      ³H  n = 9      ³He n = 9      ⁴He n = 12

    n(K) is the braid index — the lowest level of the substrate tower. Under the
    owner ruling (states are Gröbner–Shirshov normal forms; the observable is the
    trace at the lowest level) these canonical words ARE the states, so the
    cross-isotope rows compare distinct states, not two presentations of one
    state, and the table stands as written.

    The FINDING below is untouched by this: it is a character mismatch read off a
    single row — the canonical pn interface is the colour-averaged crossing, hence
    writhe-neutral, so the deuteron's w_pn = 0 at n = 6 contradicts the empirical
    a_D = 1 + h. That is a same-level statement and needs no cross-isotope
    comparison. Ref: docs/audits/2026-08-10-writhe-level-of-definition.md §5d.
    """
    h = float(mp.mpf(str(Q0)) - 1 / mp.mpf(str(Q0)))
    w = 0
    for _c, d, g in word:
        if pn_only and g % 3 != 2:
            continue
        df = float(d)
        if abs(df) < 1e-9:
            w += 1
        elif abs(df + h) < 1e-9:
            w -= 1
    return w


def kappa_avg(Z: int, N: int) -> float:
    """⟨κ⟩ = Σ_λ y_λ χ^λ(W_atom) κ_λ / Σ_λ y_λ χ^λ(W_atom) at q₀."""
    n = 3 * (Z + N)
    q0 = mp.mpf(str(Q0))
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
    chi = chi_all_lambda_reduced_block(atom_braid_word_3A(Z, N, include_inter=True), n)
    num = sum(y[tuple(l)] * v * content_sum(tuple(l)) for l, v in chi.items())
    den = sum(y[tuple(l)] * v for l, v in chi.items())
    return float(num / den)


def main() -> int:
    set_compute_dps()
    h = float(mp.mpf(str(Q0)) - 1 / mp.mpf(str(Q0)))
    kappa_pn = kappa_avg(1, 1)   # the elementary 2-nucleon pn bond (deuteron)

    print("\n  pn-SECTOR-RESTRICTED CHIRALITY — ribbon coeff vs empirical pn-rule")
    print(f"  q₀-h = {h:.5f};  ⟨κ⟩_pn (deuteron bond) = {kappa_pn:.4f}\n")
    print("| iso | empirical coeff | w_full | w_pn | ⟨κ⟩_full | full: w·⟨κ⟩ | pn-writhe | pn-sector w_pn·⟨κ⟩_pn |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N, emp in ISO:
        word = atom_braid_word_3A(Z, N, include_inter=True)
        w_full = _writhe(word, pn_only=False)
        w_pn = _writhe(word, pn_only=True)
        ka = kappa_avg(Z, N)
        c_full = w_full * ka
        c_pnw = w_pn * ka
        c_pn = w_pn * kappa_pn
        print(f"| {name} | {emp:+d} | {w_full} | {w_pn} | {ka:.3f} "
              f"| {c_full:.2f} | {c_pnw:.2f} | {c_pn:.3f} |")
    print("\n  FINDING (honest, negative): the pn-sector restriction does NOT "
          "recover the empirical pn-rule. The canonical pn-interface crossing is "
          "the color-weighted AVERAGED crossing (d≈−h/2), hence writhe-NEUTRAL "
          "(0) — so the deuteron's w_pn=0 gives ribbon-coeff 0, contradicting the "
          "empirical a_D=1+h (+1). The nonzero inter-nucleon writhe (³H −1, ³He "
          "+1) comes from pp/nn (σ/σ⁻¹), not pn; and ⟨κ⟩_pn≈9.27, not ~1. So the "
          "empirical multiplicative pn-rule (signed 1±h per pn crossing) is "
          "STRUCTURALLY INCOMPATIBLE with the ribbon eigenvalue of the canonical "
          "(averaged) pn-sector — a wrong-writhe-character mismatch, not a "
          "magnitude gap. Rules out 'ribbon eigenvalue ⇒ pn-rule'; the empirical "
          "factors remain a genuinely separate (unexplained) conjecture.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
