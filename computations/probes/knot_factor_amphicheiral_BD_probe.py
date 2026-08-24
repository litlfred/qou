#!/usr/bin/env python3
"""Resolution probe for cor:knot-factor-amphicheiral: try options B + D.

Per the author queue's diagnosis, two structural issues affect the
corollary's `a = 1 − h²` formula on 4_1 (figure-eight).  This
probe **tries two resolution options** in parallel:

**Option B — Markov-amphicheirality.**  Define K to be
"Markov-amphicheiral" if `β_K* ~ β_K` (conjugate in `H_n(R, q)`).
Equivalent test (since Hecke characters separate semisimple
classes at generic q): `χ_λ(β*) = χ_λ(β)` for **every** λ ⊢ n.
For 4_1 with `β = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹` in B_3, the 1-dim
characters (3) and (1^3) already match.  This probe **computes
χ_(2,1)(β) and χ_(2,1)(β*) via Hoefsmit seminormal matrices**
and checks equality.  If yes: 4_1 is Markov-amphicheiral, the
corollary holds via option B with sum-of-positive-squares
formula (no sign flip).  If no: 4_1 is NOT Markov-amphicheiral
and the corollary's 4_1 application is structurally wrong.

**Option D — Gram-pairing re-derivation.**  Using the upstream
prop's framing `a_K = G_{β,β*} / G_{𝟏,𝟏}` with block-diagonal
Gram matrix in the central-idempotent basis:

    `a_K = Σ_λ w_λ · χ_λ(β · β*) / χ_λ(𝟏)`

For Markov-amphicheiral K (β* = wβw⁻¹), trace cyclicity gives
`χ_λ(β · β*) = χ_λ(β · w · β · w⁻¹)`; if w is itself diagonal
in the central-idempotent basis (which holds when β commutes
with w blockwise — Markov-trace-preserving), this further
reduces to `χ_λ(β)² / χ_λ(𝟏)`.  Probed numerically.

Emits `knot-factor-amphicheiral-BD-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from hoefsmit_mpfr import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from mpmath import mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    # Set mpmath precision before any matrix work.
    set_compute_dps()

    # WitnessBuilder is instantiated up front so its internal
    # start-time captures the full computation duration.
    builder = WitnessBuilder("knot-factor-amphicheiral-BD-probe",
                             engine="mpmath")

    # H_3 (2,1) Hoefsmit-seminormal matrices via the canonical builder.
    #
    # NB: an earlier version of this probe used a hand-rolled 2×2
    # construction (σ_1 = diag(q,-q⁻¹), σ_2 = [[d1, b],[b, d2]]
    # with specific d1, d2) that satisfied the Hecke quadratic
    # per-generator but FAILED the braid relation
    # `σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2` (verified residually nonzero
    # on PR #818 follow-up review).  Those matrices were NOT a
    # valid Hecke representation; their trace of β_{4_1} = -1
    # exactly was a basis-arithmetic coincidence, not the true
    # character.  Replaced here with the canonical builder
    # `build_hoefsmit_mpfr` which satisfies both Hecke and braid
    # relations.  The corrected χ_(2,1)(β_{4_1}) at q_0 is
    # ≈ -0.91068... (NOT -1).
    sigmas_21, dim_21 = build_hoefsmit_mpfr((2, 1), Q_MP)
    s1, s2 = sigmas_21
    s1_inv = s1 ** (-1)
    s2_inv = s2 ** (-1)

    # β = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹
    beta = s1 * s2_inv * s1 * s2_inv
    # β* = σ_2 σ_1⁻¹ σ_2 σ_1⁻¹  (mirror: reverse + invert)
    beta_star = s2 * s1_inv * s2 * s1_inv

    def _trace(M):
        return sum(M[i, i] for i in range(dim_21))

    # Hoefsmit characters on (2,1) — numerical at q_0 (mpmath 50 dps).
    chi_21_beta_mp = _trace(beta)
    chi_21_beta_star_mp = _trace(beta_star)
    chi_21_id = dim_21  # χ_(2,1)(𝟏) = dim V_(2,1) = 2

    # === Option B test: Markov-amphicheirality ===
    # χ_(2,1)(β) =? χ_(2,1)(β*)
    diff_mp = chi_21_beta_mp - chi_21_beta_star_mp
    diff_abs = float(mp.fabs(diff_mp))
    chi_21_beta_num = float(chi_21_beta_mp)
    chi_21_beta_star_num = float(chi_21_beta_star_mp)
    # mpmath 50-dps gives < 1e-40 numerical precision; if the
    # difference is in that regime, β and β* are equal in trace,
    # i.e., 4_1 IS Markov-amphicheiral on the (2,1) cell.
    markov_amph = diff_abs < 1e-30

    # === Option D test: Gram pairing via β·β* ===
    prod_mp = beta * beta_star
    chi_21_prod_mp = _trace(prod_mp)
    chi_21_prod_num = float(chi_21_prod_mp)

    b = (
        builder
        .set_description(
            "Resolution probe for cor:knot-factor-amphicheiral.  "
            "Tests option B (Markov-amphicheirality: is "
            "χ_(2,1)(β*) = χ_(2,1)(β)?) and option D "
            "(Gram-pairing: spectral form via tr ρ(β·β*)) for the "
            "figure-eight braid β = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ ∈ B_3.  "
            "Uses the canonical Hoefsmit (2,1) seminormal matrices "
            "via `build_hoefsmit_mpfr` (mpmath, 50 dps).  Earlier "
            "hand-rolled matrices in this probe (PR #815) failed "
            "the braid relation and gave a spurious χ = -1; PR #818 "
            "follow-up corrected to canonical Hoefsmit, χ ≈ -0.91068."
        )
        .set_content_block("cor:knot-factor-amphicheiral")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("chi_21_beta_at_q0", chi_21_beta_num)
        .add_parameter("chi_21_beta_star_at_q0", chi_21_beta_star_num)
        .add_parameter("chi_21_beta_times_beta_star_at_q0",
                       chi_21_prod_num)
        .add_data("option_B_markov_amphicheirality", {
            "test": "χ_(2,1)(β) =? χ_(2,1)(β*)  ↔  β ~_H β*",
            "numeric_difference_at_q0": diff_abs,
            "markov_amphicheiral_at_q0": markov_amph,
            "interpretation": (
                "If markov_amphicheiral_at_q0 is true, 4_1 IS "
                "Markov-amphicheiral.  Corollary's framework "
                "survives via option B (sum-of-positive-squares "
                "formula a_K = Σ_λ w_λ · (χ_λ(β)/χ_λ(𝟏))²; no "
                "sign flip required).  If false, 4_1 is NOT "
                "Markov-amphicheiral and the corollary's 4_1 "
                "application is structurally wrong."
            ),
        })
        .add_data("option_D_gram_pairing", {
            "test": "compute χ_(2,1)(β · β*) directly",
            "value_at_q0": chi_21_prod_num,
            "interpretation": (
                "If 4_1 is Markov-amphicheiral (β* ~ β), then "
                "χ_(2,1)(β·β*) = χ_(2,1)(β²) by trace cyclicity "
                "of conjugation.  The Gram-pairing form gives "
                "a_K = Σ_λ w_λ · χ_λ(β·β*) / χ_λ(𝟏) — this is "
                "the right structural starting point per "
                "prop:knot-factor-spectral-derivation."
            ),
        })
        .add_assertion(
            name="chi_21_values_computed",
            computed=1.0 if abs(chi_21_beta_num) < 100 else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1 = (2,1) characters computed finite)",
            source="Hoefsmit seminormal (2,1) matrix trace.",
        )
        .add_assertion(
            name="option_B_markov_amphicheirality_check",
            computed=1.0 if markov_amph else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1 = 4_1 Markov-amphicheiral via option B)",
            source=(
                "χ_(2,1)(β) = χ_(2,1)(β*) is the (only) non-trivial "
                "test for β ~_{H_3(q)} β*; (3) and (1^3) already "
                "agree by writhe argument."
            ),
        )
        .add_assertion(
            name="option_D_gram_pairing_finite",
            computed=1.0 if abs(chi_21_prod_num) < 100 else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1 = χ_(2,1)(β·β*) computed finite)",
            source="Direct matrix product trace.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Option B test: χ_(2,1)(β) = {chi_21_beta_num:.6f}")
    print(f"               χ_(2,1)(β*) = {chi_21_beta_star_num:.6f}")
    print(f"               Markov-amphicheiral? {markov_amph}")
    print(f"Option D test: χ_(2,1)(β·β*) = {chi_21_prod_num:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
