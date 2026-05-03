#!/usr/bin/env python3
"""Symbolic Wedderburn port of `atom_per_generator_volumes`.

Direct sympy port of `hecke_core.atom_per_generator_volumes` —
tracks the per-generator additive Wedderburn state (a, b, sp, ap)
through `_step_chain_generic` symbolically in q.

Output: per-generator V̂_i^full as a Laurent expression in q^{1/2},
plus the algebraic Vol_q^tower(β) for the atom, also in
ℤ[q^{1/2}, q^{-1/2}] (per `prop:mass-endomorphism-tower`'s
"finite Laurent" guarantee).

For D (Z=1, N=1, n=6) we want a closed-form Vol_q^tower(D) ∈ Q(q^{1/2})
that we can `cancel`-simplify and evaluate at q_0 to compare with
the AME binding.

Output: `brane-tower-symbolic-D.witness.json`
"""
from __future__ import annotations
import json
import sys
import time
from itertools import combinations
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT  # noqa: E402

# ─── Symbolic q-arithmetic ──────────────────────────────────────────────
q = sp.Symbol('q', positive=True)
h_sym = q - 1 / q                            # q − q⁻¹
qi_sym = 1 / q
z_sym = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))    # Markov parameter


def q_int(n: int):
    """Symmetric q-integer [n]_q."""
    if n == 0:
        return sp.S(0)
    return (q**n - q**(-n)) / (q - q**(-1))


# ─── Nucleon chains (symbolic port of `nucleon_gen_chains`) ────────────
def nucleon_gen_chains_sym(quarks):
    """Symbolic version of hecke_core.nucleon_gen_chains."""
    g0 = [(sp.S(1), sp.S(0))] * 3       # B_3, σ_0 part
    g1 = [(sp.S(1), -h_sym)] * 3        # B_3, σ_1⁻¹ part

    # Quark pair crossings — exactly as hecke_core
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]
    for i, j, gen in pairs:
        qi_f, qj_f = quarks[i], quarks[j]
        if qi_f == qj_f == 'u':
            cd = (sp.S(1), sp.S(0))
        elif qi_f == qj_f == 'd':
            cd = (sp.S(1), -h_sym)
        else:
            cd = (sp.S(1), -h_sym / 2)
        if gen == 0:
            g0.append(cd)
        else:
            g1.append(cd)

    # Gluon self-coupling (2 σ₀)
    g0.append((sp.S(1), sp.S(0)))
    g0.append((sp.S(1), sp.S(0)))
    return g0, g1


_PROTON_G0_S, _PROTON_G1_S = nucleon_gen_chains_sym(['u', 'u', 'd'])
_NEUTRON_G0_S, _NEUTRON_G1_S = nucleon_gen_chains_sym(['u', 'd', 'd'])


# ─── Symbolic atom_per_generator_volumes ────────────────────────────────
def apply_crossing(state, c, d):
    """Apply a single (c, d) crossing to (a, b, sp_, ap_) state."""
    a, b, sp_, ap_ = state
    a_new = a * c * h_sym + a * d + b * c
    b_new = a * c + b * d
    sp_new = sp_ * (c * q + d)
    ap_new = ap_ * (-c * qi_sym + d)
    return a_new, b_new, sp_new, ap_new


def atom_per_generator_volumes_sym(Z: int, N: int, *, include_inter: bool = True,
                                    crossings_per_pair: int = 1):
    """Symbolic version of hecke_core.atom_per_generator_volumes.

    Returns: list of dicts with symbolic Laurent expressions.
        [{"std": Vs, "sym": sp_, "alt": ap_, "full": Vf}, ...]
    """
    A = Z + N
    if A < 1:
        return []
    ordering = ['p'] * Z + ['n'] * N

    if include_inter:
        n_gens_total = 3 * A - 1
    else:
        n_gens_total = 2 * A

    # Per-generator state — start at identity (a=0, b=1, sp=ap=1)
    state = [
        (sp.S(0), sp.S(1), sp.S(1), sp.S(1))
        for _ in range(n_gens_total)
    ]

    for k, nuc in enumerate(ordering):
        intra = _PROTON_G0_S if nuc == 'p' else _NEUTRON_G0_S
        intra_g1 = _PROTON_G1_S if nuc == 'p' else _NEUTRON_G1_S
        if include_inter:
            base_g0 = 3 * k
            base_g1 = 3 * k + 1
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        for c, d in intra:
            state[base_g0] = apply_crossing(state[base_g0], c, d)
        for c, d in intra_g1:
            state[base_g1] = apply_crossing(state[base_g1], c, d)
        if include_inter and k < A - 1:
            i = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (sp.S(1), sp.S(0))
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (sp.S(1), -h_sym)
                # (pp/nn/pn matches hecke_core)
            else:
                base_cross = (sp.S(1), -h_sym / 2)
            for _ in range(crossings_per_pair):
                state[i] = apply_crossing(state[i], *base_cross)

    # H_3 Wedderburn weights (1-dim sym, 2-dim std, 1-dim alt)
    nf3 = q_int(1) * q_int(2) * q_int(3)
    qdim_sym = sp.S(1)
    qdim_std = q_int(2)
    qdim_alt = sp.S(1)
    w_sym = qdim_sym**2 / nf3
    w_std = qdim_std**2 / nf3
    w_alt = qdim_alt**2 / nf3
    wt = w_sym + w_std + w_alt
    w_sym = sp.cancel(w_sym / wt)
    w_std = sp.cancel(w_std / wt)
    w_alt = sp.cancel(w_alt / wt)

    vols = []
    for a, b, sp_, ap_ in state:
        Vs = z_sym * a + b
        Vf = w_sym * sp_ + w_std * Vs + w_alt * ap_
        vols.append({
            "std": sp.cancel(Vs),
            "sym": sp.cancel(sp_),
            "alt": sp.cancel(ap_),
            "full": sp.cancel(Vf),
        })
    return vols


def vol_q_tower_algebraic(vols_full):
    """Vol_q^tower(β) = ∏ V_i + Σ z V_i + Σ z² V_i V_j (algebraic form)."""
    n = len(vols_full)
    prod = sp.S(1)
    for v in vols_full:
        prod *= v
    single = z_sym * sum(vols_full)
    pair = z_sym**2 * sum(
        vols_full[i] * vols_full[j]
        for i, j in combinations(range(n), 2)
    )
    return sp.cancel(sp.Abs(prod) + single + pair), {
        "product": sp.cancel(prod),
        "single_sum": sp.cancel(single),
        "pair_sum": sp.cancel(pair),
    }


def main() -> int:
    print("=" * 100)
    print("Symbolic Wedderburn for atom_per_generator_volumes — D")
    print("=" * 100)

    t0 = time.time()
    Z, N = 1, 1
    print(f"\n  Building symbolic V̂_i^full for D (Z={Z}, N={N})…")
    vols = atom_per_generator_volumes_sym(Z, N, include_inter=True)
    print(f"  n_generators = {len(vols)} (= 3A − 1 = 5)")
    print(f"  Elapsed: {time.time() - t0:.2f}s\n")

    q0_rat = sp.Rational(str(Q0_FLOAT))

    # Print symbolic V̂_i^full per generator
    print("  Per-generator V̂_i^full (symbolic, simplified):")
    for i, vd in enumerate(vols):
        v = vd["full"]
        v_at_q0 = float(v.subs(q, q0_rat))
        s = str(v)
        if len(s) > 90:
            s = s[:87] + "..."
        print(f"    V̂_{i}^full = {s}")
        print(f"             at q_0 = {v_at_q0:+.10f}")

    # Vol_q^tower symbolic
    t1 = time.time()
    vol_alg, breakdown = vol_q_tower_algebraic([vd["full"] for vd in vols])
    print(f"\n  Vol_q^tower (algebraic, after sp.cancel): {time.time() - t1:.1f}s")
    s_vol = str(vol_alg)
    if len(s_vol) > 200:
        print(f"  Vol_q^tower = {s_vol[:200]}... (length {len(s_vol)})")
    else:
        print(f"  Vol_q^tower = {s_vol}")
    print()

    # Numerical at q_0
    vol_at_q0 = float(vol_alg.subs(q, q0_rat))
    hbar_q = (q0_rat - 1) / q0_rat
    rho_q = 1 / hbar_q**2
    rho_q_val = float(rho_q)
    m_e = 0.5109989461
    m_inv = float(rho_q * vol_at_q0)
    B_pred = m_e * m_inv

    print(f"  At q_0 = {float(q0_rat):.10f}:")
    print(f"    Vol_q^tower(D)   = {vol_at_q0:.6f}")
    print(f"    ρ_q = 1/ℏ_q²     = {rho_q_val:.4f}")
    print(f"    m(ρ) = ρ_q · Vol = {m_inv:.4f}  (categorical mass invariant)")
    print(f"    m_e · m(ρ)       = {B_pred:.4f} MeV")
    print(f"    AME B(D)         = 2.2246 MeV")
    print(f"    err              = {(B_pred - 2.22456612) / 2.22456612 * 100:+.2f}%")

    from witness_base import WitnessBuilder
    from witness_polynomial import expose_polynomial
    w = (
        WitnessBuilder("brane-tower-symbolic-D", engine="sympy")
        .set_description(
            "Symbolic port of atom_per_generator_volumes for D (Z=1,N=1) "
            "via direct sympy translation of hecke_core._step_chain_generic. "
            "Produces V̂_i^full as Laurent polynomials in q^{1/2}; "
            "Vol_q^tower(D) is an exact element of ℤ[q^{1/2}, q^{-1/2}] "
            "per prop:mass-endomorphism-tower's algebraic-form guarantee."
        )
        .set_content_block("prop:mass-endomorphism-tower")
        .add_parameter("Z", Z)
        .add_parameter("N", N)
        .add_parameter("n_generators", len(vols))
        .add_data("vols_full_symbolic", [str(vd["full"]) for vd in vols])
        .add_data(
            "vols_full_polynomial",
            [expose_polynomial(vd["full"], q, simplify=False) for vd in vols],
        )
        .add_data("vols_full_at_q0", [float(vd["full"].subs(q, q0_rat)) for vd in vols])
        .add_data("Vol_q_tower_symbolic", str(vol_alg)[:5000])
        .add_data(
            "Vol_q_tower_polynomial",
            expose_polynomial(vol_alg, q, simplify=False),
        )
        .add_data("Vol_q_tower_at_q0", vol_at_q0)
        .add_data("rho_q", rho_q_val)
        .add_data("m_invariant_at_q0", m_inv)
        .add_data("B_pred_via_m_e_MeV", B_pred)
        .add_data("AME_B_D_MeV", 2.22456612)
        .add_data("err_pct", (B_pred - 2.22456612) / 2.22456612 * 100)
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
