#!/usr/bin/env python3
"""Probe — Yekutieli truncation at PER-ATOM n_⋆ from the brane-level-
selection rule.

Per the conjecture
[`conj-brane-level-selection`](../../content/quantum-observable-universe/braids-and-knots/conj-brane-level-selection.md),
the brane-tower regularization depth should be

  n_⋆(𝔥) = ℓ · n_0 + k

where ℓ = confinement level (= 2 for atomic nuclei),
n_0 = atomic-braid strand count (= 3A per def:confined-particle),
k = GB filtration grade (per joint-tower-sdp-h6-h9.witness.json).

For the audit's test set:

| atom | ℓ | n_0 = 3A | k | n_⋆ |
|------|---|----------|---|-----|
| ²H   | 2 | 6        | 2 | 14  |
| ³H   | 2 | 9        | 9 | 27  |
| ³He  | 2 | 9        | 2 | 20  |

This probe substitutes those n_⋆ into Φ_q^{[≤n_⋆]}(z) — the
truncated quantum dilogarithm — and checks whether

  B(𝔥) = m_e · ρ · (|tr_M(T_w)| + tower^{(n_⋆)}(𝔥) + σ_{3A})

closes the AME binding energies $\\{2.224566, 8.481798, 7.71806\\}$
MeV to ±5% **without per-atom retuning**.  Companion to
`probe_phiq_uniform_k.py` (uniform-k sweep); the per-atom rule is
the empirical signature that GAP-A-3's
[`conj:brane-level-selection`](../../content/quantum-observable-universe/braids-and-knots/conj-brane-level-selection.md)
is correctly identifying $n_\\star$.

Output: `probe-phiq-n-star-rule.witness.json`.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from probe_phiq_uniform_k import (  # noqa: E402
    AME, M_E_MEV, Q0, RHO_MAP, TR_M_AT_Q0, Z_N, E_0_VAL,
    PhiQPoleHit, brane_tower_truncated,
)
from witness_base import WitnessBuilder  # noqa: E402

# n_⋆ predictions per the conjecture (ℓ=2, n_0=3A, k from
# joint-tower-sdp-h6-h9.witness.json).
N_STAR = {"deuteron": 14, "tritium": 27, "he3": 20}
ELL = 2  # confinement level (atomic nuclei)
K_HECKE = {"deuteron": 2, "tritium": 9, "he3": 2}


def main():
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma(A): return float(sigma_3A_witness[f"n={3 * A}"])

    # Build the witness up-front so durationMs reflects actual
    # computation time (per Copilot review on PR #607).
    builder = (
        WitnessBuilder(name="probe-phiq-n-star-rule", engine="python")
        .set_description(
            "Per-atom n_⋆ probe of the brane-tower truncation rule "
            "n_⋆(𝔥) = ℓ·n_0 + k from "
            "conj:brane-level-selection.  Substitutes per-atom "
            "(n_⋆_D, n_⋆_T, n_⋆_³He) = (14, 27, 20) into "
            "Φ_q^{[≤n_⋆]} and checks ±5% closure of B(𝔥) against "
            "AME without per-atom retuning.  Tests proof-obligation "
            "1 of conj:brane-level-selection — the empirical "
            "signature that n_⋆ is structurally correct (or "
            "falsifies the rule)."
        )
        .set_audit_only(
            "content/quantum-observable-universe/braids-and-knots/"
            "derivation-audit-report.md (GAP-A-3)"
        )
        .add_parameter("rule", "n_star = ell * n_0 + k_Hecke")
        .add_parameter("n_star_per_atom", N_STAR)
        .add_parameter("ell", ELL)
        .add_parameter("k_Hecke_per_atom", K_HECKE)
    )

    print("=" * 92)
    print("Per-atom n_⋆ Yekutieli truncation probe (GAP-A-3)")
    print("=" * 92)
    print(f"  q_0 = {Q0}, m_e = {M_E_MEV} MeV")
    print(f"  Rule: n_⋆ = ℓ·n_0 + k = 2·(3A) + k_Hecke")
    print(f"  Predictions: D={N_STAR['deuteron']}, T={N_STAR['tritium']}, "
          f"³He={N_STAR['he3']}")
    print()
    print(f"{'atom':>10} {'n_⋆':>4} {'tow_atom':>10} {'tow_free':>10} "
          f"{'Δtow':>9} {'B_abs':>9} {'B_sub':>10} {'AME':>7} "
          f"{'abs%':>8} {'sub%':>8}")
    print("-" * 92)

    rows = {}
    closed_within_5pct = True
    for name, (Z, N) in Z_N.items():
        A = Z + N
        rho = RHO_MAP[name]
        n_star = N_STAR[name]
        try:
            T2a, T3a, mags_atom = brane_tower_truncated(Z, N, True, n_star)
            T2f, T3f, _ = brane_tower_truncated(Z, N, False, n_star)
        except PhiQPoleHit as e:
            print(f"{name:>10} {n_star:>4} -- pole hit at k={e.k} "
                  f"(q^-k·z={e.qi_pow * e.z:.4g}); n_⋆ rule diverges")
            rows[name] = {
                "n_star": n_star,
                "pole_hit": True, "k_at_pole": int(e.k),
                "ame_pct_close_within_5pct": False,
            }
            closed_within_5pct = False
            continue
        tower_a = T2a + T3a
        tower_f = T2f + T3f
        dtow = tower_f - tower_a
        sigma_3A = sigma(A)
        B_abs = M_E_MEV * rho * (abs(TR_M_AT_Q0[name]) + tower_a + sigma_3A)
        B_sub = E_0_VAL * dtow
        err_abs = 100.0 * (B_abs - AME[name]) / AME[name]
        err_sub = 100.0 * (B_sub - AME[name]) / AME[name]
        within_5 = abs(err_abs) < 5.0 or abs(err_sub) < 5.0
        if not within_5:
            closed_within_5pct = False
        print(f"{name:>10} {n_star:>4} {tower_a:>10.3g} {tower_f:>10.3g} "
              f"{dtow:>+9.3g} {B_abs:>9.3g} {B_sub:>+10.3g} "
              f"{AME[name]:>7.3f} {err_abs:>+8.2f} {err_sub:>+8.2f}")
        rows[name] = {
            "n_star": n_star,
            "ell": ELL,
            "n_0": 3 * A,
            "k_hecke": K_HECKE[name],
            "tower_atom": tower_a,
            "tower_free": tower_f,
            "delta_tower": dtow,
            "B_abs_MeV": B_abs,
            "B_sub_MeV": B_sub,
            "AME_MeV": AME[name],
            "err_abs_pct": err_abs,
            "err_sub_pct": err_sub,
            "ame_pct_close_within_5pct": bool(within_5),
        }
    print()
    print(f"  ±5% closure across {{D, T, ³He}} without per-atom retuning: "
          f"{'YES — n_⋆ rule confirmed' if closed_within_5pct else 'NO'}")
    print()

    # Refutation IS the expected outcome of this probe (the paper-side
    # conjecture's proof-obligation 1 was empirically falsified on
    # 2026-05-09; see conj-brane-level-selection.md "Empirical
    # falsification" section).  Assert that the rule is falsified so
    # the witness stays `allPassed: true` and CI doesn't treat the
    # refutation as a regression.
    builder = (
        builder
        .add_data("rows", rows)
        .add_data("closed_within_5pct_across_all", closed_within_5pct)
        .add_data("interpretation", (
            "If true, the n_⋆ rule reproduces empirical binding "
            "energies of {²H, ³H, ³He} without per-atom retuning, "
            "discharging proof-obligation 1 of "
            "conj:brane-level-selection.  If false, the specific "
            "formula n_⋆ = ℓ·n_0 + k is empirically falsified at "
            "this depth — the rule must depend on additional "
            "structural data."
        ))
        .add_assertion(
            name="n_star_rule_falsified",
            computed=int(not closed_within_5pct),
            expected=1,
        )
    )
    out_path = builder.save()
    print(f"  Witness emitted: {out_path}")
    # Return 0 unconditionally: the probe records its result either
    # way, and the assertion above pins the expected outcome.
    return 0


if __name__ == "__main__":
    sys.exit(main())
