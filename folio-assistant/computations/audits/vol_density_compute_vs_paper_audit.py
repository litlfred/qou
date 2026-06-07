"""VolDensity compute-vs-paper audit — order-by-order Σ_λ comparison.

AUDIT ONLY. No fitting, no tuning to m_p / B_AME. Reports RAW numbers.

Question (owner): production `VolDensity(𝓑₃,q₀) = m_e·[Vol(𝓑₃)/ℏ_q² ×
linking_weight(q)]` with `linking_weight = (3q²+4+3q⁻²)/4 = 5/2+(3/4)h²`
is a single opaque rational in q. The PAPER (prop:hoefsmit-scattering-
pipeline Stage 4) specifies the per-block form

    m(K) = m_e · Geom(K) · Σ_λ w_λ χ_λ(β)/dim(λ)
         = m_e · [Vol(K)/ℏ_q²] · J_K(q)

where J_K(q) = Σ_{λ⊢n} w_λ χ_λ(β)/dim(λ) is the normalized Markov
trace / Jones polynomial of the braid β, summed over the partitions
λ of n = #strands.

This script computes BOTH:
  (P) the paper's per-block factor J_{𝓑₃}(q) for the Borromean braid
      β = (σ₁σ₂⁻¹)³ on H_3 (partitions of 3) — the CORRECT index set
  (X) production's substituted linking_weight (an H_4 dim_q average)
and compares them order-by-order in h = q − q⁻¹.

It also tests the "factor of 4" renormalization the trace docs
flagged: does (h²-coeff of J)·4 = (h²-coeff of linking_weight)? and
does the h⁰ term match under the same factor?

Finally it propagates BOTH factors through the production mass bridge
m_avg = m_e · Vol(𝓑₃)/ℏ_q² · factor and reports the RAW m_avg each
produces, the raw gap vs CODATA, and how much of production's +2.89%
gap restoring J_{𝓑₃} recovers (whatever direction it goes).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _li_2_q_util import linking_weight_family_a  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except Exception:  # pragma: no cover
    WitnessBuilder = None

mp.mp.dps = 60


def fit_even_h_expansion(fn, max_order=8, samples=None):
    """Fit fn(q) = Σ_{j even, 0..max_order} a_j h^j via mpf Vandermonde.

    fn takes a decimal-string q and returns an mpf. Borromean is
    amphichiral so only even h-powers appear; we fit them.
    """
    even_orders = list(range(0, max_order + 1, 2))
    n = len(even_orders)
    if samples is None:
        samples = ["1.04", "1.06", "1.08", "1.10", "1.12", "1.14",
                   "1.16", "1.18"]
    samples = samples[:n]
    h_vals, f_vals = [], []
    for s in samples:
        q = mp.mpf(s)
        h_vals.append(q - 1 / q)
        f_vals.append(fn(s))
    V = mp.matrix(n, n)
    for i in range(n):
        for j, o in enumerate(even_orders):
            V[i, j] = h_vals[i] ** o
    a = mp.lu_solve(V, mp.matrix(f_vals))
    return {o: a[j] for j, o in enumerate(even_orders)}


def paper_J_borromean(q_str):
    """Paper's per-block factor J_{𝓑₃}(q) = Σ_{λ⊢3} w_λ χ_λ(β)/dim λ
    in the WENZL convention (the one production's `markov_trace_for_knot`
    uses for the mass formula). H_3 index set — the index set forced by
    the 3-strand Borromean braid β = (σ₁σ₂⁻¹)³.

    Closed form, verified against the Rust-computed 50-dps witness
    `borromean-markov-trace-h-expansion-50dps.witness.json`
    (`actual_h_coefficients_wenzl_jm`):

        J_wenzl(q) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

    The closed form is exact through the h⁶ term; higher orders are the
    Wenzl Markov-trace tail. We use it directly so the audit does not
    depend on the (unbuilt) `pyhecke_native` Rust extension. The
    Vandermonde fit on this closed form reproduces the witness's
    a_0≈1, a_2≈0, a_4≈−0.75, a_6≈−0.062 to high precision.
    """
    q = mp.mpf(q_str)
    h = q - 1 / q
    return (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)


def paper_J_borromean_jones_norm(q_str):
    """Alternative normalization: Jones polynomial of the Borromean
    rings / (√q+√q⁻¹)² = the `borromean_markov_trace_h2` form. This is
    the H_3 trace under the (n−1)-strand Jones normalization. h-series:
    1 + (3/16)h² + ... — this is the normalization in which the famous
    "(3/16)·4 = 3/4" factor-of-4 coincidence with Family A appears.
    """
    q = mp.mpf(q_str)
    qi = 1 / q
    sq = mp.sqrt(q)
    sqi = 1 / sq
    t = q ** 2
    ti = qi ** 2
    jones = -ti**3 + 3*ti**2 - 2*ti + 4 - 2*t + 3*t**2 - t**3
    return jones / (sq + sqi) ** 2


def production_linking_weight(q_str):
    q = mp.mpf(q_str)
    return linking_weight_family_a(q)


def main():
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h0 = q0 - 1 / q0
    print(f"q_0    = {mp.nstr(q0, 20)}")
    print(f"h_0    = {mp.nstr(h0, 20)}")
    print(f"h_0^2  = {mp.nstr(h0**2, 20)}")
    print()

    # ── 1. Order-by-order h-expansion of BOTH factors ──────────────
    print("=== h-expansion of the per-block / linking factors ===")
    paper = fit_even_h_expansion(paper_J_borromean, max_order=8)
    jones = fit_even_h_expansion(paper_J_borromean_jones_norm, max_order=8)
    prod = fit_even_h_expansion(production_linking_weight, max_order=8)

    print(f"{'h^k':>4} | {'paper J wenzl (H3)':>22} | "
          f"{'paper J jones (H3)':>22} | {'production lw (H4)':>22}")
    print("-" * 90)
    rows = {}
    for o in [0, 2, 4, 6, 8]:
        p = paper[o]
        jnv = jones[o]
        x = prod[o]
        rows[o] = {
            "paper_J_wenzl_H3": mp.nstr(p, 18),
            "paper_J_jones_H3": mp.nstr(jnv, 18),
            "production_lw_H4": mp.nstr(x, 18),
            "ratio_prod_over_wenzl": mp.nstr((x / p) if p != 0 else mp.mpf("nan"), 18),
            "ratio_prod_over_jones": mp.nstr((x / jnv) if jnv != 0 else mp.mpf("nan"), 18),
        }
        print(f"h^{o:<2} | {mp.nstr(p, 18):>22} | {mp.nstr(jnv, 18):>22} | "
              f"{mp.nstr(x, 18):>22}")
    print()
    print("ratio production_lw / paper_J_jones (the factor-of-N test):")
    for o in [0, 2, 4]:
        jnv = jones[o]
        r = (prod[o] / jnv) if jnv != 0 else mp.mpf("nan")
        print(f"  h^{o}: {mp.nstr(r, 12)}")
    print("ratio production_lw / paper_J_wenzl:")
    for o in [0, 2, 4]:
        p = paper[o]
        r = (prod[o] / p) if p != 0 else mp.mpf("nan")
        print(f"  h^{o}: {mp.nstr(r, 12)}")
    print()

    # ── 2. The "factor of 4" + h0 mismatch resolution ──────────────
    # The "(3/16)·4 = 3/4" claim lives in the JONES normalization.
    print("=== factor-of-4 / h0-mismatch test (jones normalization) ===")
    jones_h2 = jones[2]
    prod_h2 = prod[2]
    jones_h0 = jones[0]
    prod_h0 = prod[0]
    print(f"jones  J h0 coeff   = {mp.nstr(jones_h0, 18)}  (= 1)")
    print(f"prod   lw h0 coeff  = {mp.nstr(prod_h0, 18)}  (= 5/2)")
    print(f"  -> h0 ratio prod/jones = {mp.nstr(prod_h0/jones_h0, 12)} "
          f"(= 5/2, NOT 4)")
    print(f"jones  J h2 coeff   = {mp.nstr(jones_h2, 18)}  (= 3/16)")
    print(f"prod   lw h2 coeff  = {mp.nstr(prod_h2, 18)}  (= 3/4)")
    print(f"  -> h2 ratio prod/jones = {mp.nstr(prod_h2/jones_h2, 12)} "
          f"(= 4)")
    print(f"  -> 'factor 4' h2 test: jones_h2 * 4 = {mp.nstr(jones_h2*4, 18)} "
          f"vs prod_h2 = {mp.nstr(prod_h2, 18)} (MATCH)")
    print(f"  -> same factor 4 on h0: jones_h0 * 4 = "
          f"{mp.nstr(jones_h0*4, 18)} vs prod_h0 = {mp.nstr(prod_h0, 18)} "
          f"(MISMATCH: 4 vs 5/2)")
    print(f"  -> h4: jones_h4 = {mp.nstr(jones[4], 12)} vs prod_h4 = "
          f"{mp.nstr(prod[4], 12)} (prod terminates at h2; jones does not)")
    # keep names used downstream
    paper_h0, paper_h2 = paper[0], paper[2]
    print()

    # ── 3. Propagate BOTH through the mass bridge ──────────────────
    print("=== mass-bridge propagation (RAW, no fit) ===")
    from experimental_constants import M_E_MEV, M_P_MEV
    try:
        from experimental_constants import M_N_MEV
    except Exception:
        M_N_MEV = None
    m_e = mp.mpf(repr(M_E_MEV))
    m_p = mp.mpf(repr(M_P_MEV))
    m_n = mp.mpf(repr(M_N_MEV)) if M_N_MEV is not None else None
    m_avg_codata = (m_p + m_n) / 2 if m_n is not None else m_p

    hbar_q = 1 - 1 / q0
    vol_b3 = 8 * mp.catalan
    geom_leading = vol_b3 / hbar_q ** 2

    lw_prod = linking_weight_family_a(q0)
    J_paper = paper_J_borromean(Q_50_DIGIT_STR)

    vol_density_prod = geom_leading * lw_prod
    vol_density_paper = geom_leading * J_paper

    m_avg_prod = m_e * vol_density_prod
    m_avg_paper = m_e * vol_density_paper

    gap_prod = (m_avg_prod - m_avg_codata) / m_avg_codata
    gap_paper = (m_avg_paper - m_avg_codata) / m_avg_codata

    print(f"Vol(B3)/hbar_q^2       = {mp.nstr(geom_leading, 18)}")
    print(f"production lw(q_0)      = {mp.nstr(lw_prod, 18)}")
    print(f"paper J_B3(q_0)        = {mp.nstr(J_paper, 18)}")
    print(f"  ratio lw/J           = {mp.nstr(lw_prod/J_paper, 12)}")
    print()
    print(f"m_e                    = {mp.nstr(m_e, 14)} MeV")
    print(f"m_avg CODATA           = {mp.nstr(m_avg_codata, 14)} MeV")
    print(f"m_avg PRODUCTION       = {mp.nstr(m_avg_prod, 14)} MeV  "
          f"gap = {mp.nstr(gap_prod*100, 6)} %")
    print(f"m_avg PAPER-PERBLOCK   = {mp.nstr(m_avg_paper, 14)} MeV  "
          f"gap = {mp.nstr(gap_paper*100, 6)} %")
    print()

    recovered = (abs(gap_prod) - abs(gap_paper)) / abs(gap_prod)
    print(f"production |gap|        = {mp.nstr(abs(gap_prod)*100, 6)} %")
    print(f"paper-perblock |gap|    = {mp.nstr(abs(gap_paper)*100, 6)} %")
    print(f"FRACTION of prod gap recovered by restoring per-block J = "
          f"{mp.nstr(recovered*100, 6)} %")
    print("  (negative => restoring J makes the gap WORSE, not better)")
    print()

    if WitnessBuilder is not None:
        w = WitnessBuilder("vol-density-compute-vs-paper-audit", engine="mpmath")
        w.set_description(
            "AUDIT (no fit): order-by-order comparison of the paper's "
            "per-block factor J_{B3}(q)=Sum_{lam|-3} w_lam chi_lam(beta)/dim "
            "lam (markov_trace_for_knot Borromean wenzl, H_3 index set) "
            "against production linking_weight=(3q^2+4+3q^-2)/4 (H_4 "
            "dim_q average). Reports h-coefficients, the factor-of-4 / "
            "h0-mismatch, and the RAW m_avg each factor yields with the "
            "raw gap vs CODATA and the fraction of production's +2.89% "
            "recovered by restoring the per-block sum."
        )
        w.add_data("q0", mp.nstr(q0, 50))
        w.add_data("h_expansion_paper_J_wenzl_H3",
                   {f"h{o}": mp.nstr(paper[o], 30) for o in [0, 2, 4, 6, 8]})
        w.add_data("h_expansion_paper_J_jones_H3",
                   {f"h{o}": mp.nstr(jones[o], 30) for o in [0, 2, 4, 6, 8]})
        w.add_data("h_expansion_production_lw_H4",
                   {f"h{o}": mp.nstr(prod[o], 30) for o in [0, 2, 4, 6, 8]})
        w.add_data("order_by_order_rows", rows)
        w.add_data("factor_of_4_test", {
            "normalization": "jones (Jones poly / (sqrt q + sqrt qi)^2)",
            "jones_h0": mp.nstr(jones_h0, 30),
            "prod_h0": mp.nstr(prod_h0, 30),
            "h0_ratio_prod_over_jones": mp.nstr(prod_h0 / jones_h0, 30),
            "jones_h2": mp.nstr(jones_h2, 30),
            "prod_h2": mp.nstr(prod_h2, 30),
            "h2_ratio_prod_over_jones": mp.nstr(prod_h2 / jones_h2, 30),
            "jones_h2_times_4": mp.nstr(jones_h2 * 4, 30),
            "h0_match_under_factor_4": bool(abs(jones_h0 * 4 - prod_h0)
                                            < mp.mpf(10) ** -20),
            "h2_match_under_factor_4": bool(abs(jones_h2 * 4 - prod_h2)
                                            < mp.mpf(10) ** -20),
            "wenzl_h0": mp.nstr(paper[0], 30),
            "wenzl_h2": mp.nstr(paper[2], 30),
            "note": ("h0 ratio = 5/2, h2 ratio = 4 -> factor-of-N is "
                     "coefficient-specific, not a single renormalization; "
                     "h4+ diverges (prod terminates at h2). In the wenzl "
                     "convention used by markov_trace_for_knot, J has "
                     "a0=1, a2~0 -> even the leading agreement is "
                     "convention-dependent."),
        })
        w.add_data("mass_bridge", {
            "vol_b3_over_hbarq2": mp.nstr(geom_leading, 30),
            "production_lw_q0": mp.nstr(lw_prod, 30),
            "paper_J_B3_q0": mp.nstr(J_paper, 30),
            "ratio_lw_over_J": mp.nstr(lw_prod / J_paper, 30),
            "m_e_MeV": mp.nstr(m_e, 20),
            "m_avg_codata_MeV": mp.nstr(m_avg_codata, 20),
            "m_avg_production_MeV": mp.nstr(m_avg_prod, 20),
            "m_avg_paper_perblock_MeV": mp.nstr(m_avg_paper, 20),
            "gap_production_pct": mp.nstr(gap_prod * 100, 12),
            "gap_paper_perblock_pct": mp.nstr(gap_paper * 100, 12),
            "fraction_of_prod_gap_recovered_pct": mp.nstr(recovered * 100, 12),
        })
        out = w.save()
        print(f"Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
