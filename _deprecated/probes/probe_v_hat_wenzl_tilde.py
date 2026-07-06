"""
probe_v_hat_wenzl_tilde.py — A/B test V̂_i magnitudes under
normalized Plancherel vs unnormalized Wenzl tilde weights.

Per owner: "V̂_i re-derivation under Li_2^q (was tuned to Faddeev)".

Current `wedderburn_weights_n3` (terms_2_3_atom_per_gen_mpfr_50dps
line 138-158) normalizes so Σ w_λ = 1 (Plancherel probability
measure).  The q-deformed Wenzl tilde weight is

    tilde w_λ := dim_q²(λ) / [n]_q!

which is NOT a probability measure at q ≠ 1 (Σ tilde w_λ ≈ 0.987
at n=3, q=q_0; 1.51 at n=12 per AGENTS.md note).

This probe computes V̂_i and m_p_pred under both conventions:
  - normalized (current): w_λ / Σ w_λ
  - unnormalized (Wenzl tilde): tilde w_λ directly

If the missing 173× factor in m_p_pred is explained by switching
to unnormalized weights, magnitudes should shift to close the gap.

Outputs `probe-v-hat-wenzl-tilde.witness.json`.

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
from _li_2_q_util import li_2_q as Li_2_q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from terms_2_3_atom_per_gen_mpfr_50dps import (  # noqa: E402
    additive_wedderburn_volumes, build_particle_crossings,
)
from mass_formula_6term_mpfr_50dps import (  # noqa: E402
    term_4_frobenius_mp, term_6_habiro_residue_mp,
)
from derive_m_p_hecke_full_tower_50dps import _t5_cat_units_for  # noqa: E402

set_compute_dps()

from codata_constants import M_E_MEV  # CODATA-2022 full precision
M_P_CODATA = mpf("938.27208816")
RHO_K_CODATA_P = mpf("1723.6")  # from atomic-mass-gb-nf.md line 62

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
q_inv = mpf(1) / q
h = q - q_inv
z_mark = mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv))


def _q_int(k: int) -> mpf:
    if k == 0:
        return mpf(0)
    return (q**k - q_inv**k) / h


def wedderburn_weights_n3_unnormalized() -> tuple[mpf, mpf, mpf]:
    """Wenzl tilde y_λ = dim_q²(λ) / [3]_q! — NOT normalized.

    At q = 1: y_(3) = 1/6, y_(2,1) = 4/6, y_(1,1,1) = 1/6, sum = 1.
    At q_0: sum slightly less than 1 (~0.987 per AGENTS.md note).
    """
    q_fact_3 = _q_int(1) * _q_int(2) * _q_int(3)
    dim_q_3 = mpf(1)
    dim_q_21 = _q_int(2)
    dim_q_111 = mpf(1)
    return (
        dim_q_3**2 / q_fact_3,
        dim_q_21**2 / q_fact_3,
        dim_q_111**2 / q_fact_3,
    )


def wedderburn_weights_n2_unnormalized() -> tuple[mpf, mpf]:
    """Wenzl tilde y_λ = dim_q²(λ) / [2]_q! — NOT normalized."""
    q_fact_2 = _q_int(1) * _q_int(2)
    return mpf(1) / q_fact_2, mpf(1) / q_fact_2


def vols_with_weights(crossings: dict, n_gens: int, weights: tuple) -> list[dict]:
    """Compute V̂_i under arbitrary (w_sym, w_std, w_alt) weights."""
    if len(weights) == 3:
        w_sym, w_std, w_alt = weights
    else:
        w_sym, w_alt = weights
        w_std = mpf(0)
    return additive_wedderburn_volumes(
        crossings, n_gens, q, h, w_sym, w_std, w_alt, z_mark,
    )


def li_2_q_tower(vols: list[dict]) -> tuple[mpf, mpf, mpf]:
    """Compute (T1, T2, T3) from per-gen V̂_full list under
    canonical Li_2^q convention."""
    t1 = mpf(1)
    for v in vols:
        t1 *= v["full"]
    t1 = mp.fabs(t1)
    t2 = mpf(0)
    for v in vols:
        t2 -= Li_2_q(-mp.fabs(v["full"]), q, q_inv)
    n = len(vols)
    t3 = mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            t3 -= z_mark * z_mark * Li_2_q(
                -mp.fabs(vols[i]["full"] * vols[j]["full"]), q, q_inv
            )
    return t1, t2, t3


def main() -> int:
    parts = build_particle_crossings(h)
    print("=" * 78)
    print("  V̂_i A/B test — Plancherel-normalized vs Wenzl-tilde-unnormalized")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(q, 16)}")
    print()

    # === Proton ===
    p_crossings = parts["proton"]["crossings"]
    p_n_gens = parts["proton"]["n_gens"]

    # Normalized (current default)
    from terms_2_3_atom_per_gen_mpfr_50dps import wedderburn_weights_n3
    w_norm = wedderburn_weights_n3(q)
    vols_norm_p = vols_with_weights(p_crossings, p_n_gens, w_norm)

    # Unnormalized (Wenzl tilde)
    w_unnorm = wedderburn_weights_n3_unnormalized()
    vols_unnorm_p = vols_with_weights(p_crossings, p_n_gens, w_unnorm)

    print("  PROTON (n=3):")
    print(f"    Normalized weights:    sym={mp.nstr(w_norm[0], 10)}, "
          f"std={mp.nstr(w_norm[1], 10)}, alt={mp.nstr(w_norm[2], 10)}")
    print(f"    Wenzl tilde weights:   sym={mp.nstr(w_unnorm[0], 10)}, "
          f"std={mp.nstr(w_unnorm[1], 10)}, alt={mp.nstr(w_unnorm[2], 10)}")
    print(f"    Sum (norm)={mp.nstr(sum(w_norm), 10)}, "
          f"Sum (unnorm)={mp.nstr(sum(w_unnorm), 10)}")
    print()
    print("    V̂_i comparison:")
    for i in range(p_n_gens):
        vn = vols_norm_p[i]["full"]
        vu = vols_unnorm_p[i]["full"]
        print(f"      gen {i}: V̂_norm={mp.nstr(vn, 14)}, "
              f"V̂_unnorm={mp.nstr(vu, 14)}, ratio={mp.nstr(vu/vn, 10)}")

    t1_n, t2_n, t3_n = li_2_q_tower(vols_norm_p)
    t1_u, t2_u, t3_u = li_2_q_tower(vols_unnorm_p)
    t4 = term_4_frobenius_mp(1)  # A=1 (¹H, 1 nucleon)
    try:
        t6_MeV = term_6_habiro_residue_mp(1)
        t6 = t6_MeV / M_E_MEV
    except Exception:
        t6 = mpf(0)
    t5_n = _t5_cat_units_for(2, 1, 0)  # A_grade=2, Z=1, N=0
    t5_u = t5_n  # T5 doesn't use V̂_i

    m_hecke_norm = t1_n + t2_n + t3_n + t4 + t5_n + t6
    m_hecke_unnorm = t1_u + t2_u + t3_u + t4 + t5_u + t6

    m_p_norm_MeV = m_hecke_norm * M_E_MEV
    m_p_unnorm_MeV = m_hecke_unnorm * M_E_MEV

    print()
    print(f"  {'Term':6} {'Normalized':>22} {'Unnormalized':>22}")
    print(f"  {'T1':6} {mp.nstr(t1_n, 14):>22} {mp.nstr(t1_u, 14):>22}")
    print(f"  {'T2':6} {mp.nstr(t2_n, 14):>22} {mp.nstr(t2_u, 14):>22}")
    print(f"  {'T3':6} {mp.nstr(t3_n, 14):>22} {mp.nstr(t3_u, 14):>22}")
    print(f"  {'T4':6} {mp.nstr(t4, 14):>22} {mp.nstr(t4, 14):>22}")
    print(f"  {'T5':6} {mp.nstr(t5_n, 14):>22} {mp.nstr(t5_u, 14):>22}")
    print(f"  {'T6':6} {mp.nstr(t6, 14):>22} {mp.nstr(t6, 14):>22}")
    print(f"  {'sum':6} {mp.nstr(m_hecke_norm, 14):>22} {mp.nstr(m_hecke_unnorm, 14):>22}")
    print()
    print(f"  m_p_pred normalized   = {mp.nstr(m_p_norm_MeV, 12)} MeV")
    print(f"  m_p_pred unnormalized = {mp.nstr(m_p_unnorm_MeV, 12)} MeV")
    print(f"  m_p CODATA             = {M_P_CODATA} MeV")
    pct_norm = (m_p_norm_MeV - M_P_CODATA) / M_P_CODATA * 100
    pct_unnorm = (m_p_unnorm_MeV - M_P_CODATA) / M_P_CODATA * 100
    print(f"  residual (norm)        = {mp.nstr(pct_norm, 8)} %")
    print(f"  residual (unnorm)      = {mp.nstr(pct_unnorm, 8)} %")
    print()
    print(f"  ρ_K_CODATA (proton)    = {RHO_K_CODATA_P}")
    print(f"  ratio CODATA / norm    = {mp.nstr(M_P_CODATA / m_p_norm_MeV, 10)}")
    print(f"  ratio CODATA / unnorm  = {mp.nstr(M_P_CODATA / m_p_unnorm_MeV, 10)}")

    # Verdict
    if mp.fabs(pct_unnorm) < 50:
        print()
        print("  *** UNNORMALIZED WEIGHTS CLOSE THE GAP — Wenzl tilde is the answer ***")
    elif mp.fabs(pct_unnorm) < mp.fabs(pct_norm):
        print()
        print("  *** Unnormalized weights IMPROVE prediction but don't close ***")
    else:
        print()
        print("  *** Unnormalized weights do NOT improve prediction ***")
        print("      The 173× gap is NOT from Plancherel-vs-Wenzl normalization.")

    w = (WitnessBuilder("probe-v-hat-wenzl-tilde", engine="python+mpmath")
         .set_description("A/B test V̂_i under Plancherel-normalized vs Wenzl-tilde weights"))
    w.add_data("q_pinned", str(q))
    w.add_data("weights_normalized", {
        "sym": str(w_norm[0]), "std": str(w_norm[1]), "alt": str(w_norm[2]),
        "sum": str(sum(w_norm)),
    })
    w.add_data("weights_wenzl_tilde", {
        "sym": str(w_unnorm[0]), "std": str(w_unnorm[1]), "alt": str(w_unnorm[2]),
        "sum": str(sum(w_unnorm)),
    })
    w.add_data("proton_terms_normalized_cat", {
        "T1": str(t1_n), "T2": str(t2_n), "T3": str(t3_n),
        "T4": str(t4), "T5": str(t5_n), "T6": str(t6),
        "m_hecke": str(m_hecke_norm), "m_p_MeV": str(m_p_norm_MeV),
    })
    w.add_data("proton_terms_unnormalized_cat", {
        "T1": str(t1_u), "T2": str(t2_u), "T3": str(t3_u),
        "T4": str(t4), "T5": str(t5_u), "T6": str(t6),
        "m_hecke": str(m_hecke_unnorm), "m_p_MeV": str(m_p_unnorm_MeV),
    })
    w.add_data("residual_pct", {
        "normalized": str(pct_norm), "unnormalized": str(pct_unnorm),
    })
    w.add_data("rho_K_CODATA_proton", str(RHO_K_CODATA_P))
    w.add_data("ratio_CODATA_over_pred", {
        "normalized": str(M_P_CODATA / m_p_norm_MeV),
        "unnormalized": str(M_P_CODATA / m_p_unnorm_MeV),
    })
    w.add_assertion("unnormalized_closes_gap",
                    computed=1.0 if mp.fabs(pct_unnorm) < 5 else 0.0,
                    expected=1.0)  # we WANT this to close
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
