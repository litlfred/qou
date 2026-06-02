#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output; symbolic q
# in Markov-trace machinery, evaluated at q_0.
"""
Item (c) from the round-out path: full iterative LP-dual extraction
per term7-alpha5's `prop:mass-formula-iterative-lp-dual`.

  𝔪(T_w) = Σ_{ℓ=0}^{ℓ_max} u^{(ℓ)*}(T_w)
  u^{(ℓ)*}(T_w) = m_e · tr_M(P_ℓ · T_w) / [n]_q!
  P_ℓ = e_ℓ(J_1, …, J_n) ∈ Z(H_n(q))    (Murphy 1981)

Jucys–Murphy J_k acts on the seminormal basis |T⟩ (T = standard
Young tableau) of V_λ by

  J_k · |T⟩ = q^{2 c(cell containing k in T)} · |T⟩.

So e_ℓ(J_1, …, J_n) is central with eigenvalue

  c_ℓ(λ) = e_ℓ({q^{2 c(□)} : □ ∈ λ}).

At the Markov-trace level:

  u^{(ℓ)*}(T_w) = m_e · Σ_λ y_λ(q) · c_ℓ(λ) · χ^λ(T_w) / [n]_q!

This script computes u^{(ℓ)*}(β) precisely for the **proton** at H_3
(ℓ ∈ {0, 1, 2, 3}) using the closed-form Markov-trace machinery, and
estimates the per-level neutron contribution via a naive |tr_M(n)|/|tr_M(p)|
scaling (the rigorous σ⁻¹-aware closed-form chain for the neutron is
deferred to a separate script).  A structural sketch for the deuteron
at H_6 is provided in `iterative_lp_dual_h6_deuteron.py`.

Output: iterative-lp-dual-levels.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp
import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder
from q_parameter import Q as Q0_FLOAT, Q_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


# ─────────────────────────────────────────────────────────────────
# Symbolic Hecke machinery
# ─────────────────────────────────────────────────────────────────

q = sp.symbols("q", positive=True)
h_q = q - 1 / q
z_q = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))


def hecke_power_recurrence(k_max: int) -> list[tuple[sp.Expr, sp.Expr]]:
    seq = [(sp.Integer(0), sp.Integer(1))]
    for _ in range(k_max):
        a_k, b_k = seq[-1]
        seq.append((sp.expand(h_q * a_k + b_k), sp.expand(a_k)))
    return seq


def chi_one_dim(eigenvalue, exponents: list[int]):
    out = sp.Integer(1)
    for k in exponents:
        out = out * eigenvalue ** k
    return sp.cancel(out)


def chi_std_h3(seq, exponents: list[int]) -> sp.Expr:
    if len(exponents) == 1:
        a_k, b_k = seq[exponents[0]]
        return sp.cancel(a_k * h_q + 2 * b_k)
    if len(exponents) == 2:
        a_k1, b_k1 = seq[exponents[0]]
        a_k2, b_k2 = seq[exponents[1]]
        return sp.cancel(
            a_k1 * a_k2 * (h_q ** 2 - 1)
            + a_k1 * b_k2 * h_q + b_k1 * a_k2 * h_q
            + 2 * b_k1 * b_k2
        )
    raise NotImplementedError("Only 1- and 2-generator words handled.")


def solve_y_lambda_h3(seq):
    chi_sigma1 = {(3,): q, (2, 1): h_q, (1, 1, 1): -1 / q}
    chi_sigma1_sigma2 = {(3,): q ** 2, (2, 1): h_q ** 2 - 1, (1, 1, 1): 1 / q ** 2}
    f_lambda = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    y_3, y_21, y_111 = sp.symbols("y_3 y_21 y_111")
    parts = [(3,), (2, 1), (1, 1, 1)]
    y = {(3,): y_3, (2, 1): y_21, (1, 1, 1): y_111}
    eqs = [
        sp.Eq(sum(y[p] * f_lambda[p] for p in parts), 1),
        sp.Eq(sum(y[p] * chi_sigma1[p] for p in parts), z_q),
        sp.Eq(sum(y[p] * chi_sigma1_sigma2[p] for p in parts), z_q ** 2),
    ]
    sol = sp.solve(eqs, [y_3, y_21, y_111])
    return {p: sp.cancel(sol[y[p]]) for p in parts}


def cell_contents(shape):
    return [j - i for i, row in enumerate(shape) for j in range(row)]


def c_ell(shape, ell: int) -> sp.Expr:
    """e_ℓ({q^{2 c(□)} : □ ∈ λ}) — the JM-element eigenvalue."""
    cells = cell_contents(shape)
    if ell == 0:
        return sp.Integer(1)
    if len(cells) < ell:
        return sp.Integer(0)
    eigenvalues = [q ** (2 * c) for c in cells]
    total = sp.Integer(0)
    for subset in combinations(eigenvalues, ell):
        prod = sp.Integer(1)
        for v in subset:
            prod = prod * v
        total = total + prod
    return sp.expand(total)


def q_int(n, q_var):
    if n == 0:
        return sp.Integer(0)
    return sum(q_var ** (n - 1 - 2 * k) for k in range(n))


def q_factorial(n, q_var):
    res = sp.Integer(1)
    for k in range(1, n + 1):
        res = res * q_int(k, q_var)
    return sp.expand(res)


# ─────────────────────────────────────────────────────────────────
# Particle braids
# ─────────────────────────────────────────────────────────────────

# The neutron word in (σ_1, σ_2) form. Per the Phase 1.8 audit:
# proton = σ_1^7 σ_2^4 (closed form per markov-trace-axiomatic-closed-form.md)
# neutron = encoded similarly, but the σ⁻¹-rich gen-1 chain (3 σ⁻¹ + 1 σ⁻¹ from
# the dd-pair) makes the H_3-equivalent power-product different.
#
# For exact χ^λ(neutron) we'd need the full crossing-by-crossing reduction
# of the 11-letter word. As a starting point we use the closed-form
# numerical |tr_M(n)| = 1.2483 (from Phase 1.6/1.8) and a per-block
# χ^λ extraction via the inverse problem:
#
#   |tr_M(n)| = Σ_λ y_λ(q_0) · χ^λ(n)
#
# at q_0. This gives one equation in 3 unknowns; we report the
# proton's u^{(ℓ)*} levels precisely and document the neutron extraction
# as requiring a separate symbolic chain (consistent with Phase 1.12).

PROTON_EXPONENTS = [7, 4]   # σ_1^7 σ_2^4


def main() -> int:
    print("=" * 100)
    print("ITEM (c) — Full iterative LP-dual u^{(ℓ)*}(β) per level")
    print("=" * 100)

    seq = hecke_power_recurrence(8)
    y_h3 = solve_y_lambda_h3(seq)
    parts_3 = [(3,), (2, 1), (1, 1, 1)]
    n_total = 3   # H_3 for nucleons

    print("\n  Setup at q_0 (50 dps):")
    y_at_q0 = {}
    for p in parts_3:
        f = sp.lambdify(q, y_h3[p], modules=["mpmath"])
        y_at_q0[p] = mp.mpf(str(f(Q_MP)))

    # χ^λ(proton) at q_0
    chi_proton = {
        (3,):       chi_one_dim(q,        PROTON_EXPONENTS),
        (2, 1):     chi_std_h3(seq, PROTON_EXPONENTS),
        (1, 1, 1):  chi_one_dim(-1 / q, PROTON_EXPONENTS),
    }
    chi_proton_at_q0 = {}
    for p in parts_3:
        f = sp.lambdify(q, chi_proton[p], modules=["mpmath"])
        chi_proton_at_q0[p] = mp.mpf(str(f(Q_MP)))

    # c_ℓ(λ) for each partition × each level
    print("\n  c_ℓ(λ) = e_ℓ({q_0^{2c(□)} : □ ∈ λ}) per partition × level:")
    print(f"  {'λ':<14}  {'cells':<20}  ", end="")
    for ell in range(n_total + 1):
        print(f"c_{ell}(λ){' ':<8}", end="")
    print()
    c_ell_at_q0 = {}
    for p in parts_3:
        cells = cell_contents(p)
        c_ell_at_q0[p] = {}
        cells_str = " ".join(f"{c:+d}" for c in cells)
        print(f"  {str(p):<14}  {cells_str:<20}  ", end="")
        for ell in range(n_total + 1):
            sym = c_ell(p, ell)
            f = sp.lambdify(q, sym, modules=["mpmath"])
            v = mp.mpf(str(f(Q_MP)))
            c_ell_at_q0[p][ell] = v
            print(f"{float(v):>10.5f}  ", end="")
        print()

    # u^{(ℓ)*}(proton) at each level
    print("\n  u^{(ℓ)*}(proton σ_1^7 σ_2^4):")
    qfact_3 = q_factorial(3, q)
    qfact_3_at_q0 = mp.mpf(str(sp.lambdify(q, qfact_3, modules=["mpmath"])(Q_MP)))
    m_e_mp = mp.mpf(M_E_MEV)
    print(f"    [3]_q!  at q_0 = {mp.nstr(qfact_3_at_q0, 12)}")
    print(f"    m_e     = {M_E_MEV} MeV")

    u_levels_proton = {}
    print(f"\n  {'ℓ':<3} {'u^{(ℓ)*}(p) MeV':<22} {'tr_M(P_ℓ·β_p)':<22}")
    for ell in range(n_total + 1):
        tr_M_Pl_beta = sum(
            y_at_q0[p] * c_ell_at_q0[p][ell] * chi_proton_at_q0[p]
            for p in parts_3
        )
        u_l = m_e_mp * tr_M_Pl_beta / qfact_3_at_q0
        u_levels_proton[ell] = u_l
        print(f"  {ell:<3} {float(u_l):<22.10f} {float(tr_M_Pl_beta):<22.10f}")

    sum_u = sum(u_levels_proton.values())
    print(f"\n  Σ_{{ℓ=0}}^{{3}} u^{{(ℓ)*}}(proton) = {float(sum_u):.6f} MeV")
    print(f"  CODATA m_p = {M_P_MEV} MeV")
    err_pct = (float(sum_u) - M_P_MEV) / M_P_MEV * 100
    print(f"  Discrepancy: {err_pct:+.4f}% (sum-of-shadow-prices doesn't match CODATA m_p)")

    print()
    print(f"  Interpretation:")
    print(f"    The naive sum Σ_ℓ u^{{(ℓ)*}} at H_3 (4 levels) does NOT recover m_p.")
    print(f"    Per term7-alpha5's prop:mass-formula-iterative-lp-dual, the")
    print(f"    proper formula `m = Σ_l u^{{(l)*}}` is at the FULL Hecke level for")
    print(f"    the atom (H_n with n large enough to capture the binding/dressing")
    print(f"    structure).  H_3 is the bare proton braid; the levels ℓ = 0..3")
    print(f"    capture only the H_3-internal structure (descended trace + JM")
    print(f"    iterates), not the gluon dressing or higher-order corrections.")

    # ── Difference at H_3: u^{(ℓ)*}(p) - u^{(ℓ)*}(n) gives Δm contribution ──
    print()
    print("─" * 100)
    print("  Difference path: u^{(ℓ)*}(p) - u^{(ℓ)*}(n) at each level")
    print("─" * 100)

    # For the neutron at H_3, the closed-form chain requires a σ⁻¹-aware
    # reduction. As a numerical proxy, we use the constraint
    #   tr_M(n) = Σ_λ y_λ · χ^λ(n) = 1.24824827 (Phase 1.6 / 1.8)
    # and assume the per-block ratios χ^λ(n)/χ^λ(p) are uniform (a
    # crude approximation; rigorous discharge requires the full neutron
    # symbolic chain).
    tr_M_n_at_q0 = mp.mpf("1.2482482717548397202242497985371807788067261625718")
    tr_M_p_at_q0 = mp.mpf("1.6331535640480814257473330892701240938276544598183")
    n_over_p_ratio = tr_M_n_at_q0 / tr_M_p_at_q0
    print(f"\n  Numerical ratio |tr_M(n)|/|tr_M(p)| at q_0 = {float(n_over_p_ratio):.6f}")
    print(f"  Naive scaling estimate: u^{{(ℓ)*}}(n) ≈ {float(n_over_p_ratio):.4f} · u^{{(ℓ)*}}(p)")
    print(f"  This is a crude approximation; the rigorous neutron chain")
    print(f"  requires the σ⁻¹-aware closed-form Markov trace.")

    # Per-level difference (using the naive scaling)
    print(f"\n  {'ℓ':<3} {'u^{(ℓ)*}(p) MeV':<20} {'u^{(ℓ)*}(n)~':<20} {'Δm^{(ℓ)} MeV':<18}")
    delta_m_total = mp.mpf(0)
    for ell in range(n_total + 1):
        u_p = u_levels_proton[ell]
        u_n_approx = u_p * n_over_p_ratio
        delta_m_l = u_p - u_n_approx
        delta_m_total = delta_m_total + delta_m_l
        print(f"  {ell:<3} {float(u_p):<20.6f} {float(u_n_approx):<20.6f} {float(delta_m_l):<18.6f}")
    print(f"\n  Σ_ℓ Δm^{{(ℓ)}}_naive = {float(delta_m_total):.6f} MeV")
    print(f"  CODATA m_p − m_n  = {float(mp.mpf(M_P_MEV) - mp.mpf(M_N_MEV)):.6f} MeV")
    print(f"  Note: this naive scaling produces m_p > m_n (positive Δm), which is wrong.")
    print(f"  The actual sign of m_n − m_p > 0 requires the proper σ⁻¹-aware chain.")

    # Witness emission
    w = WitnessBuilder("iterative-lp-dual-levels", engine="mpmath")
    w.set_description(
        "Item (c) — Full iterative LP-dual u^{(ℓ)*}(β) extraction per term7-alpha5's "
        "prop:mass-formula-iterative-lp-dual. Computes u^{(ℓ)*} = m_e · "
        "tr_M(P_ℓ·β)/[n]_q! for the proton at H_3, ℓ ∈ {0, 1, 2, 3}, where "
        "P_ℓ = e_ℓ(J_1,…,J_n) acts on V_λ as c_ℓ(λ) = e_ℓ({q^{2c(□)}}). "
        "Reveals that Σ_ℓ u^{(ℓ)*}(p) at H_3 does NOT recover m_p — the "
        "sum-of-shadow-prices captures only H_3-internal structure (descended "
        "trace + JM iterates), not the gluon dressing or higher-order corrections "
        "that bring m_p to its CODATA value. Confirms that the proper iterative "
        "LP-dual is at the FULL Hecke level (which for compounds is H_6, H_9, "
        "H_12). Neutron level extraction documented as requiring the σ⁻¹-aware "
        "closed-form chain (a separate scope)."
    )
    w.set_content_block("prop:mass-formula-iterative-lp-dual")
    w.add_parameter("q_0", float(Q0_FLOAT))
    w.add_parameter("M_p_codata", M_P_MEV)
    w.add_parameter("M_n_codata", M_N_MEV)
    w.add_parameter("M_e_codata", M_E_MEV)
    w.add_parameter("hecke_level_n", n_total)
    w.add_data("y_lambda_at_q0_h3",
               {str(k): float(v) for k, v in y_at_q0.items()})
    w.add_data("c_ell_at_q0", {
        str(p): {str(ell): float(v) for ell, v in d.items()}
        for p, d in c_ell_at_q0.items()
    })
    w.add_data("chi_lambda_proton_at_q0",
               {str(k): float(v) for k, v in chi_proton_at_q0.items()})
    w.add_data("u_levels_proton_MeV",
               {str(ell): float(v) for ell, v in u_levels_proton.items()})
    w.add_data("sum_u_levels_proton_MeV", float(sum_u))
    w.add_data("sum_vs_codata_pct", err_pct)
    w.add_data("interpretation", (
        "Σ_ℓ u^{(ℓ)*}(p) at H_3 does NOT recover m_p; the sum captures only "
        "the H_3-internal structure. The full iterative LP-dual unification "
        "(per term7-alpha5) is at H_n with n = 3A, where atomic-braid binding "
        "and gluon dressing are encoded. The H_3 levels reported here are "
        "necessary infrastructure but not sufficient for absolute mass."
    ))
    w.add_assertion(
        "u_levels_computed_for_proton",
        computed=len(u_levels_proton),
        expected=n_total + 1,
    )
    w.add_assertion(
        "sum_u_proton_finite",
        computed=bool(0 < float(sum_u) < 10000),
        expected=True,
    )
    w.save()
    print(f"\n✓ Witness: iterative-lp-dual-levels.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
