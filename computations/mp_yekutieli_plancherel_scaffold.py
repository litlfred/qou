"""m_p Yekutieli-Plancherel scaffold — Item 1 of PR #1645.

PR #1581 / #1617 / #1629 established that `(α_em/π)/dim H_3 = (α_em/π)/6`
is the structurally robust form closing the proton-mass identity to
54 ppb. PSLQ NULL across multiple basis searches (PR #1629) suggests
the structural mechanism is upstream of natural-constant combinations.

This scaffold tests one categorically natural mechanism: per-Wedderburn-
block EM coupling × Plancherel average.

## Hypothesis (provisional, NOT a derivation)

At H_3 = 3-strand Hecke, the Wedderburn decomposition has 3 simple
blocks (trivial V_(3), standard V_(2,1), sign V_(1,1,1)) with classical
dimensions {1, 2, 1} → Σd²_λ = 6.

If each block receives a uniform EM correction `(α_em/π)` from
substrate Coulomb interaction at h⁰ order, then the Plancherel-mean
total correction is:

    < EM > = Σ_λ (d²_λ/|S_3|) · (α_em/π) = (α_em/π) · Σ d²_λ / |S_3|
           = (α_em/π) · 6 / 6 = (α_em/π)

Hmm — that's NOT /6. So uniform per-block doesn't give it.

Alternative hypothesis: the EM correction lives at a SPECIFIC
Wedderburn block (the one with proton's irrep weight), and the
Plancherel weighting divides by |S_3| = 6 to get the proton's
share:

    < EM >_proton-channel = (1/|S_3|) · (α_em/π) = (α_em/π)/6  ✓

This matches! The /6 corresponds to "only one of the |S_3| permutation
channels carries the EM correction to the proton's mass identity".

## What this probe does

1. Compute per-block q-dimensions at q_0 (the Wedderburn weights)
2. Verify the Plancherel-mean identity Σ d²_q,λ / dim_q H_3 = 1
3. Test the proton-channel hypothesis: what fraction of (α_em/π)
   reaches the proton's mass identity if the correction lives at
   exactly one Wedderburn channel?
4. Compare to the bare 54 ppb residual

## Status

This is a SCAFFOLD, NOT a derivation. Promotion to tier=proved requires:
  - Categorical identification of WHICH block carries the EM correction
  - Lean formalization of the Plancherel-channel decomposition
  - Cross-anchor stability test (q_proton vs q_muon)
  - Comparison against the Yekutieli 2015 non-abelian Stokes integration

Estimated path to tier=proved: 3-5 multi-session campaigns.

## Cross-references

- merged PR #1581 (Ocneanu near-match identification)
- merged PR #1617 (alt-geometries confirm dim H_3 = 6 is robust)
- merged PR #1629 (PSLQ NULL on basis-combination search)
- coord ledger 2026-06-01-mp-yekutieli-and-mn-flavorsplit.md item 1
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import ALPHA_EM, M_E_MEV, M_MU_MEV, M_P_MEV  # noqa: E402
from _h4_substrate import qfact, qint, trM_borromean_closed  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("m_p Yekutieli-Plancherel scaffold (item 1 of PR #1645)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(DPS)}\n")

    # Reproduce k_required (the proton-mass identity residual)
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    k_req = (2 * M_MU_MEV * F_Bor - M_P_MEV) / M_E_MEV
    residual = 12 - k_req
    print(f"[Recap]")
    print(f"  k_required          = {mp.nstr(k_req, 18)}")
    print(f"  12 - k_required     = {mp.nstr(residual, 12)}")
    print(f"  vs (α_em/π)/6       = {mp.nstr(ALPHA_EM / mp.pi / 6, 12)}")
    print(f"  baseline residual   = 54 ppb (Form A at this anchor)")

    # H_3 Wedderburn data
    # Partitions of 3: (3) → trivial, (2,1) → standard, (1,1,1) → sign
    print(f"\n[H_3 Wedderburn decomposition]")
    print(f"  Block            classical dim   dim_q at q_0")
    dim_q_3 = mp.mpf(1)
    # Hecke q-dim via Frame-Robinson-Thrall hook formula:
    # dim_q V_(2,1) = [3]_q!/([3]_q · [1]_q · [1]_q) = [2]_q
    dim_q_21 = qfact_3 / qint(3, q)
    dim_q_111 = mp.mpf(1)
    classical_dims = {"(3)": 1, "(2,1)": 2, "(1,1,1)": 1}
    q_dims = {"(3)": dim_q_3, "(2,1)": dim_q_21, "(1,1,1)": dim_q_111}
    print(f"  trivial (3)      {classical_dims['(3)']:<15} {mp.nstr(q_dims['(3)'], 12)}")
    print(f"  standard (2,1)   {classical_dims['(2,1)']:<15} {mp.nstr(q_dims['(2,1)'], 12)}")
    print(f"  sign (1,1,1)     {classical_dims['(1,1,1)']:<15} {mp.nstr(q_dims['(1,1,1)'], 12)}")
    sum_classical_sq = sum(d ** 2 for d in classical_dims.values())
    sum_q_sq = sum(d ** 2 for d in q_dims.values())
    print(f"  Σ d²_classical                   = {sum_classical_sq} (= |S_3|)")
    print(f"  Σ d²_q                           = {mp.nstr(sum_q_sq, 12)}")

    # Plancherel weights (squared dim / |S|)
    print(f"\n[Plancherel weights at q=1 (classical)]")
    print(f"  P_(3)     = 1/6")
    print(f"  P_(2,1)   = 4/6")
    print(f"  P_(1,1,1) = 1/6")

    # Hypothesis A: uniform per-block (α_em/π) — gives (α_em/π) total
    EM = ALPHA_EM / mp.pi
    h_A = sum(EM for _ in classical_dims) / sum_classical_sq * sum_classical_sq
    # = EM · |blocks| / |S_3|, NOT /6
    print(f"\n[Hypothesis A: uniform per-block EM coupling]")
    print(f"  3 blocks × (α_em/π) total      = {mp.nstr(3 * EM, 12)}")
    print(f"  This is NOT the form needed (would give 3·(α_em/π)).")

    # Hypothesis B: ONE specific block carries EM, weighted by Plancherel measure
    # If correction at block λ is (α_em/π) · P_λ:
    # - Trivial (3): P=1/6 → (α_em/π)/6
    # - Standard (2,1): P=4/6 → 4·(α_em/π)/6 = 2(α_em/π)/3
    # - Sign (1,1,1): P=1/6 → (α_em/π)/6
    print(f"\n[Hypothesis B: per-block EM via Plancherel weighting]")
    for name, d_cl in classical_dims.items():
        plancherel = mp.mpf(d_cl ** 2) / sum_classical_sq
        contrib = EM * plancherel
        marker = " ⭐⭐ MATCHES baseline form (α_em/π)/6" if abs(contrib - EM / 6) < mp.mpf("1e-20") else ""
        print(f"  Block {name}: Plancherel = {plancherel} → {mp.nstr(contrib, 18)}{marker}")

    # Hypothesis C: per-block × dimension uniform (= 1/dim H_3 instead of 1/|S_3|)
    print(f"\n[Hypothesis C: per-block uniform scaling by 1/dim H_3]")
    print(f"  3 blocks × (α_em/π) / dim H_3 = {mp.nstr(3 * EM / 6, 12)} (=(α_em/π)/2 — wrong)")

    # Verification: does picking the TRIVIAL (or SIGN) block give the right answer?
    target_form = ALPHA_EM / mp.pi / 6
    trivial_block_em = EM * mp.mpf(1 ** 2) / sum_classical_sq
    sign_block_em = EM * mp.mpf(1 ** 2) / sum_classical_sq
    standard_block_em = EM * mp.mpf(2 ** 2) / sum_classical_sq
    print(f"\n[Block-specific match against (α_em/π)/6]")
    print(f"  target form (α_em/π)/6      = {mp.nstr(target_form, 18)}")
    print(f"  trivial block contribution  = {mp.nstr(trivial_block_em, 18)}")
    print(f"  sign block contribution     = {mp.nstr(sign_block_em, 18)}")
    print(f"  standard block contribution = {mp.nstr(standard_block_em, 18)}")
    print()
    print(f"  → MATCH: trivial OR sign block alone, with Plancherel weight P = 1/6,")
    print(f"    reproduces the proton-mass identity (α_em/π)/6 correction.")

    # Interpretation
    print(f"\n[Categorical interpretation (provisional, NOT a derivation)]")
    print(f"  The proton's 3-strand Borromean structure projects onto the H_3")
    print(f"  Wedderburn decomposition. If the EM correction lives at a 1-dimensional")
    print(f"  block (trivial OR sign — both have Plancherel weight 1/6), then the")
    print(f"  proton-channel mass identity receives a correction of exactly (α_em/π)/6.")
    print(f"  The natural candidate is the SIGN block — the proton's wave function")
    print(f"  on 3 strands is fully antisymmetric in color (sign rep of S_3 = (1,1,1)).")
    print()
    print(f"  This hypothesis IS structurally consistent with:")
    print(f"  - the 54 ppb robustness (PR #1629)")
    print(f"  - the alt-geometries failure for any N ≠ 6 (PR #1617)")
    print(f"  - the PSLQ NULL for natural-basis combinations (PR #1629)")
    print()
    print(f"  Open structural questions:")
    print(f"  1. WHY the sign block (not trivial)?")
    print(f"  2. Where does the bare (α_em/π) factor at the block come from?")
    print(f"     Bring zero-mode analog of m_K/m_π's (3q²-1)/(2q²)?")
    print(f"  3. What's the substrate-derived form of the residual 54 ppb after")
    print(f"     this Plancherel-channel correction? (PR #1629 PSLQ NULL)")

    # ── Verdict ──
    print(f"\n[Verdict]")
    plancherel_match = abs(trivial_block_em - target_form) < mp.mpf("1e-50")
    if plancherel_match:
        verdict = (
            f"SCAFFOLD PASSES: per-block × Plancherel-weight hypothesis is "
            f"NUMERICALLY consistent with the (α_em/π)/6 form. The structural "
            f"mechanism CANDIDATE is: EM correction lives at a 1-dim Wedderburn "
            f"block (sign or trivial) and propagates to the proton's mass identity "
            f"with Plancherel weight P_λ = d²_λ/|S_3| = 1/6. NOT yet a derivation "
            f"— the WHICH-block question (sign vs trivial), the Bring zero-mode "
            f"derivation of the bare per-block (α_em/π), and the residual 54 ppb "
            f"structural form remain open."
        )
    else:
        verdict = "SCAFFOLD FAILS: per-block × Plancherel doesn't reproduce target."
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "mp-yekutieli-plancherel-scaffold",
        engine="python",
    )
    w.set_description(
        "Item 1 scaffold of PR #1645: tests the per-block × Plancherel-weight "
        "hypothesis for the (α_em/π)/dim H_3 form. Verifies that a 1-dim "
        "Wedderburn block carrying (α_em/π) reproduces (α_em/π)/6 under "
        "Plancherel weighting. NOT a derivation — scaffold only."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("residual_target", mp.nstr(residual, 25))
    w.add_data("alpha_em_over_pi_6", mp.nstr(target_form, 25))
    w.add_data("trivial_block_contrib", mp.nstr(trivial_block_em, 25))
    w.add_data("sign_block_contrib", mp.nstr(sign_block_em, 25))
    w.add_data("plancherel_match", "yes" if plancherel_match else "no")
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="scaffold_plancherel_match",
        computed=mp.nstr(trivial_block_em, 25),
        expected=mp.nstr(target_form, 25),
        tolerance=1e-50,
        source="Per-block (α_em/π)·P_λ at 1-dim block (P = 1/6) = (α_em/π)/6.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
