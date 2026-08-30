#!/usr/bin/env python3
"""
binding_bond_extensive_derivation.py — the bond-extensive hypothesis
(B = coordination_number · b*) is DERIVED from the translation-invariance of the
inter-nucleon bond coupling, given the Part-10 Gram-quadratic binding form.

Context: siblings #3549/#3551 (bk_coordination_contact_binding.py) read the binding
multiplicity as the coordination number z(A)=A−1 (nucleon) / contact-graph edges
(α-cluster), but flag "single-link multiplier = coordination number" as the
bond-extensive HYPOTHESIS — conditional, NOT derived from the 13 drivers.

This probe supplies the missing derivation, using the Part-10 fact that binding is
the negative-norm ghost Gram-quadratic form
    B(K) ~ ⟨Σ_i g_i⟩²_G = Σ_i ⟨g_i⟩²_G + 2·Σ_{i<j} ⟨g_i, g_j⟩_G ,  g_i = ½(L₊−L₋)_i.

Two structural facts (H₃ ghost reproduced; H₆⁺ value deferred — see boundary):

  (1) UNBONDED cross-term vanishes. Two nucleon ghosts on disjoint strands form a
      SPLIT link; the Markov trace factorizes, tr_M(g_i ⊗ g_j)=tr_M(g_i)·tr_M(g_j),
      and each ghost is TRACELESS (tr_M(g)=0). So ⟨g_i,g_j⟩_G = 0 with no bond.
  (2) BONDED cross-term is bond-universal. A single inter-nucleon generator σ_bond
      couples the pair: ⟨g_i,σ_bond,g_j⟩_G ≠ 0. For identical nucleons joined by
      identical bonds, every bond is the SAME local ghost-σ-ghost coupling
      (translation-invariant), so every bond contributes the SAME value b*.

⇒ B(K) ~ Σ_i ⟨g_i⟩²_G (per-nucleon rest term) + (#bonds)·b* = self + coordination·b*.
  The bond-extensive form is DERIVED — the multiplier is constant BECAUSE the bonds
  are structurally identical couplings, not by assumption. What remains is the VALUE
  b* (one universal per-bond number), the H₆ seminormal-Gram build.

BOUNDARY (honest): markov_trace_combo is H₃-only; the H₆ value b* needs the
per-block seminormal infra (gram_matrix_seminormal_h6.py) — a real multi-step build,
overlapping #3548 (W_λ connected transfer matrix, the tr_M lens of the same object).
The homogeneity (identical-bond) assumption is the mean-field reading; a compact
non-chain geometry with inequivalent bonds would split b* by environment.

EXPLORATORY — no production wiring, no fitted constant, no tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 11
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "pyhecke" / "python"))


def main() -> int:
    print("=== bond-extensive hypothesis DERIVED from bond translation-invariance ===\n")
    try:
        import numpy as np
        import mpmath as mp
        from pyhecke import gram as G
    except Exception as e:
        print(f"(pyhecke unavailable: {e}) — structural argument stands independent of the value.")
        return 0

    Gm = np.array(G.G, dtype=float)
    t = np.array(G.TR_M, dtype=float)
    g = np.zeros(6); g[3] = 0.5; g[4] = -0.5   # ghost ½(L₊−L₋) = ½(σ₁σ₂ − σ₂σ₁)
    tr_g = float(t @ g)
    self_norm = float(g @ Gm @ g)

    # Second, independent routes to the two numbers the argument turns on.
    # `NF_NAMES` is ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻'], so indices 3 and 4 are
    # the ghost's two words. `_TR_M_FRAC` carries the Markov trace as exact
    # rationals and `gram_matrix_mp` rebuilds the Gram at 60 dps, neither of
    # them through the float64 arrays above.
    iL, iR = G.NF_NAMES.index("L₊"), G.NF_NAMES.index("L₋")
    tr_g_exact = (G._TR_M_FRAC[iL] - G._TR_M_FRAC[iR]) / 2
    with mp.workdps(60):
        Gmp = G.gram_matrix_mp(60)
        gm = [mp.mpf(0)] * 6
        gm[iL], gm[iR] = mp.mpf(1) / 2, -mp.mpf(1) / 2
        self_norm_mp = sum(gm[i] * Gmp[i][j] * gm[j]
                           for i in range(6) for j in range(6))
        norm_gap = abs(self_norm_mp - mp.mpf(repr(self_norm))) / abs(self_norm_mp)
        self_norm_s, norm_gap_s = mp.nstr(self_norm_mp, 25), mp.nstr(norm_gap, 6)
    print(f"  cross-check: tr_M(g) exactly {tr_g_exact} (rational); ⟨g⟩²_G at 60 dps "
          f"{self_norm_s}, relative gap to float64 {norm_gap_s}")
    print(f"per-nucleon ghost g = ½(σ₁σ₂ − σ₂σ₁):  tr_M(g) = {tr_g:+.6f} (traceless), "
          f"⟨g⟩²_G = {self_norm:+.4f}")
    print()
    print("(1) unbonded pair = split link ⇒ tr_M factorizes ⇒ ⟨g_i,g_j⟩_G = tr_M(g_i)·tr_M(g_j) = 0")
    print("(2) one bond σ couples them ⇒ ⟨g_i,σ,g_j⟩_G = b* ≠ 0; every bond identical ⇒ same b*")
    print()
    print("⇒ B(K) ~ Σ_i⟨g_i⟩²_G + (#bonds)·b*  =  self + coordination·b*")
    print("  DERIVES bond-extensivity: multiplier constant BECAUSE bonds are identical couplings.")
    print("  Value b* deferred to H₆ seminormal build (markov_trace_combo is H₃-only); coordinate #3548.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-bond-extensive-derivation", engine="numpy")
        wb.set_description(
            "EXPLORATORY: derives the bond-extensive hypothesis (B = self + coordination·b*) "
            "from bond translation-invariance, given the Part-10 Gram-quadratic binding form. "
            "Unbonded ghost pair = split link ⇒ cross-term 0 (traceless factorization); a bond "
            "couples them; identical bonds ⇒ constant per-bond b*. Upgrades #3549's conditional "
            "bond-extensive hypothesis to derived (modulo the value b*, the H₆ seminormal build). "
            "Mean-field/homogeneous reading. No fit.")
        wb.add_data("ghost_h3", {"tr_M": tr_g, "self_gram_norm": self_norm,
                                 "tr_M_exact": str(tr_g_exact),
                                 "self_gram_norm_60dps": self_norm_s})
        # Was `computed="1", expected="1"` (bean `qou-26f2`) — one literal on
        # both sides standing in for the whole derivation, so `passed:true` was
        # recorded even in a run where the Gram had been rebuilt into something
        # with no ghost in it at all. The `source` string names the two facts
        # the argument actually rests on; both are computable here, and neither
        # was being computed.
        #
        # (1) THE UNBONDED CROSS-TERM. Step (1) of the derivation is
        #     ⟨g_i,g_j⟩_G = tr_M(g_i)·tr_M(g_j) = 0, which holds only because
        #     the ghost is traceless. That is exact, not numerical: the Markov
        #     trace is conjugation-invariant and L₊ = σ₁σ₂, L₋ = σ₂σ₁ are
        #     conjugate, so the two entries of `_TR_M_FRAC` are the same
        #     rational and the difference is 0 in ℚ. Checked there rather than
        #     on the float64 vector, where a cancellation could hide a real
        #     asymmetry under round-off.
        wb.add_assertion(
            name="unbonded_ghost_cross_term_vanishes",
            computed=str(tr_g_exact), expected="0", tolerance=0,
            unit="tr_M(g) in exact rational arithmetic",
            source=("step (1) of the derivation: two nucleon ghosts on disjoint "
                    "strands form a split link, tr_M factorizes, so the cross "
                    "term is tr_M(g)². Zero iff the ghost is traceless. "
                    f"pyhecke._TR_M_FRAC[{iL}] − [{iR}] over 2, in ℚ."))
        # (2) THE GRAM VALUE THE STEP-(2) COUPLING LIVES IN. The Part-10 form
        #     the whole probe is conditioned on calls the ghost NEGATIVE-norm;
        #     that sign was printed and never checked. Recorded with a second
        #     derivation of the same number — the Gram rebuilt at 60 dps —
        #     because a float64-only value has nothing to disagree with.
        wb.add_assertion(
            name="ghost_self_gram_norm_is_negative",
            computed=str(int(self_norm_mp < 0)), expected="1", tolerance=0,
            unit="1 if ⟨g⟩²_G < 0 (the Part-10 negative-norm ghost)",
            source=(f"⟨g⟩²_G = {self_norm_s} at 60 dps. The binding form "
                    "B(K) ~ ⟨Σ_i g_i⟩²_G is stated as the negative-norm ghost "
                    "quadratic form; a non-negative value would refute the "
                    "premise this derivation is conditioned on."))
        wb.add_assertion(
            name="ghost_self_gram_norm_reproduces_at_60_dps",
            computed=norm_gap_s, expected="0", tolerance="1e-14",
            unit="relative gap, float64 Gram vs 60-dps Gram",
            source=("⟨g⟩²_G by two routes: pyhecke.gram.G (float64) and "
                    "gram_matrix_mp(60) (mpmath). Tolerance is the float64 "
                    "round-off scale for a quantity of order 1, which is what "
                    "the coarser of the two routes can carry."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
