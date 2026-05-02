#!/usr/bin/env python3
"""
Fresh p/n derivation, Steps E-G:

  E. Compute Hecke energy E(λ, q) per partition λ ⊢ 3
  F. Assign per-block reference knot K_λ with V_hyp(K_λ)
  G. Assemble m(ρ) = Σ_λ E(λ) · V_hyp(K_λ) · χ_λ(β)  (prefactor TBD)

Partitions of 3 and their per-block reference knots (user's
"per-block V_hyp" choice):

  λ = (3)     sym,  d_q = 1,        K_λ = unknot      V_hyp = 0
  λ = (2, 1)  std,  d_q = [2]_q,    K_λ = figure-8    V_hyp = 2.0298832...
  λ = (1,1,1) alt,  d_q = 1,        K_λ = trefoil     V_hyp = 0  (torus)

Only the std block carries hyperbolic volume; sym and alt
contributions are identically zero.  This is consistent with the
paper's observation that the "minimal hyperbolic" geometry enters
through the 2-dim std irrep of H_3(q).

Hecke energies E(λ, q) computed three ways for comparison:
  (a) Plancherel-derived:  E_P = |d_q(λ)/[n]_q! − 1/[n]_q!|
                                = |d_q(λ) − 1| / [n]_q!
  (b) LP-dual:             E_LP = |w_λ/d_λ − 1/[n]_q!|
                                = |d_q(λ)²/([n]_q!·d_λ) − 1/[n]_q!|
  (c) Raw d_q:             E_dq = d_q(λ)  (bare quantum dim, as a
                                          floor reference)

Prefactor (user's Q3) left symbolic; report m_contributions
before prefactor.

Output: fresh-derivation-pn-steps-E-G.witness.json
"""
from __future__ import annotations

import sys
import json
import math
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
import mpmath as mp

from q_parameter import vol_4_1_at

mp.mp.dps = 40

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL,
)
from hecke_characters import (build_seminormal_matrices, dim_q, qfac,
                                partitions_of, young_hooks)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP


def q_int(k):
    return (Q0**k - QI**k) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


# Figure-8 knot (4_1) hyperbolic volume — Catalan-related classical value.
# Computed via Vol(4_1) = 2 Cl_2(π/3) at the current mpmath precision.
VOL_FIG8 = vol_4_1_at(mp.mp.dps)


def dim_q_value(shape):
    """Numerical d_q(λ) at q₀."""
    return mp.mpf(str(float(dim_q(shape))))


def classical_dim(shape):
    """Integer dim of irrep λ via hook length formula at q=1."""
    n = sum(shape)
    hooks = young_hooks(shape)
    fact_n = mp.mpf(1)
    for k in range(1, n + 1):
        fact_n *= k
    hp = mp.mpf(1)
    for h in hooks:
        hp *= h
    return fact_n / hp


def chi_at_q0(shape, word):
    """Character χ_λ(β) with β given as list of Hecke factors (c, d)
    at alternating generator indices.  Uses the alternating-generator
    convention of hecke_core.nucleon_gen_chains: g0 factors go to σ_0,
    g1 factors to σ_1.

    Here `word` is the list of (c, d, gen) tuples where gen ∈ {0, 1}.
    """
    sigmas_sym, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return mp.mpc(0)
    q_sym = sp.Symbol('q')
    # Substitute q₀ in each sigma
    sigmas_num = []
    for S in sigmas_sym:
        try:
            fn = sp.lambdify(q_sym, sp.Matrix(S), modules='numpy')
            M = np.asarray(fn(complex(Q0_FLOAT)), dtype=complex)
        except Exception:
            M = np.zeros((dim, dim), dtype=complex)
            for i in range(dim):
                for j in range(dim):
                    e = S[i, j] if not hasattr(S, 'toarray') else S.toarray()[i, j]
                    if hasattr(e, 'subs'):
                        M[i, j] = complex(sp.N(e.subs(q_sym, float(Q0_FLOAT))))
                    else:
                        M[i, j] = complex(e)
        sigmas_num.append(M)
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for (c, d, gen) in word:
        if gen >= len(sigmas_num):
            return mp.mpc(0)
        F = c * sigmas_num[gen] + d * I
        M = M @ F
    return mp.mpc(complex(np.trace(M)))


def build_particle_word(g0_chain, g1_chain):
    """Convert (g0, g1) chain lists into a single list of
    (c, d, gen) tuples with proper order."""
    word = []
    for c, d in g0_chain:
        word.append((c, d, 0))
    for c, d in g1_chain:
        word.append((c, d, 1))
    return word


def hecke_energies(shape, n):
    """Return (E_Plancherel, E_LP, E_dq) at q₀ for partition λ."""
    dq = dim_q_value(shape)
    d_cl = classical_dim(shape)
    nfac = q_fact(n)
    # Plancherel-derived: E_P = |d_q − 1| / [n]_q!
    E_P = mp.fabs(dq - 1) / nfac
    # LP-dual: E_LP = |d_q² / (nfac · d_cl) − 1/nfac|
    E_LP = mp.fabs(dq * dq / (nfac * d_cl) - mp.mpf(1) / nfac)
    # Raw d_q
    E_dq = dq
    return E_P, E_LP, E_dq


REF_KNOTS = {
    (3,):        {"name": "unknot",   "V_hyp": mp.mpf(0),
                   "note": "trivial closure of sym irrep"},
    (2, 1):      {"name": "figure-8", "V_hyp": VOL_FIG8,
                   "note": "minimal hyperbolic knot; std of H_3"},
    (1, 1, 1):   {"name": "trefoil",  "V_hyp": mp.mpf(0),
                   "note": "(3,2)-torus knot; alt irrep"},
}


def process(name, g0, g1, m_codata):
    print(f"\n{'=' * 100}")
    print(f"{name} — mass target: m_codata = {m_codata} MeV")
    print('=' * 100)
    word = build_particle_word(g0, g1)
    n = 3  # H_3 for a single nucleon
    print(f"  n_strands = {n}")
    print(f"  partitions of 3: {list(partitions_of(n))}")
    print(f"  [3]_q! at q₀ = {mp.nstr(q_fact(n), 20)}")
    print()

    print(f"  {'λ':<10} {'K_λ':<10} {'V_hyp':>10} {'d_q':>8} "
          f"{'E_Planck':>12} {'E_LP':>12} {'χ_λ(β)':>26} "
          f"{'|Re·E_P·V|':>14}")

    rows = []
    total_P = mp.mpc(0)
    total_LP = mp.mpc(0)
    for shape in sorted(partitions_of(n), key=lambda s: -sum(s)):
        ref = REF_KNOTS[shape]
        E_P, E_LP, E_dq = hecke_energies(shape, n)
        chi = chi_at_q0(shape, word)
        contrib_P = E_P * ref["V_hyp"] * mp.mpc(chi.real, chi.imag)
        contrib_LP = E_LP * ref["V_hyp"] * mp.mpc(chi.real, chi.imag)
        total_P += contrib_P
        total_LP += contrib_LP
        abs_P = mp.fabs(contrib_P)
        print(f"  {str(shape):<10} {ref['name']:<10} "
              f"{float(ref['V_hyp']):>10.6f} {float(E_dq):>8.4f} "
              f"{float(E_P):>12.6f} {float(E_LP):>12.6f} "
              f"{str(chi)[:26]:>26} {float(abs_P):>14.6e}")
        rows.append({
            "shape": list(shape),
            "knot": ref["name"],
            "V_hyp": mp.nstr(ref["V_hyp"], 20),
            "d_q": mp.nstr(E_dq, 20),
            "E_Plancherel": mp.nstr(E_P, 20),
            "E_LP": mp.nstr(E_LP, 20),
            "chi_re": float(chi.real),
            "chi_im": float(chi.imag),
            "contribution_Plancherel_re": float(contrib_P.real),
            "contribution_LP_re": float(contrib_LP.real),
        })

    print()
    print(f"  Σ_λ E_Planck · V_hyp · χ_λ(β)  = "
          f"{mp.nstr(total_P.real, 15)}  (Im = {float(total_P.imag):+.2e})")
    print(f"  Σ_λ E_LP      · V_hyp · χ_λ(β) = "
          f"{mp.nstr(total_LP.real, 15)}  (Im = {float(total_LP.imag):+.2e})")

    # Prefactor candidates
    print()
    print("  --- prefactor candidates for question 3 ---")
    for (pname, pref) in [
        ("m_e",               mp.mpf(str(M_E_MEV))),
        ("m_e · 8G",          mp.mpf(str(M_E_MEV)) *
                                mp.mpf("7.32772475") ),   # 8*G_Catalan
        ("m_e · 2π",          mp.mpf(str(M_E_MEV)) * 2 * mp.pi),
        ("m_e / V_hyp(fig8)", mp.mpf(str(M_E_MEV)) / VOL_FIG8),
        ("(fig8/trefoil)·m_e", mp.mpf(str(M_E_MEV))),  # trefoil vol = 0
    ]:
        m_P = pref * total_P.real
        err_P = (float(m_P) - m_codata) / m_codata * 100
        print(f"    prefactor = {pname:<24} m_P={float(m_P):+.4f} MeV  "
              f"err={err_P:+.2f}%")

    return {
        "name": name,
        "m_codata": m_codata,
        "rows": rows,
        "total_Plancherel_re": float(total_P.real),
        "total_Plancherel_im": float(total_P.imag),
        "total_LP_re": float(total_LP.real),
        "total_LP_im": float(total_LP.imag),
    }


def main() -> int:
    print("=" * 100)
    print("FRESH DERIVATION — STEPS E-G  (per-block V_hyp, partition sum)")
    print("=" * 100)

    p = process("PROTON",  _PROTON_G0,  _PROTON_G1,  M_P_MEV)
    n = process("NEUTRON", _NEUTRON_G0, _NEUTRON_G1, M_N_MEV)

    witness = {
        "computation": "fresh-derivation-pn-steps-E-G",
        "description": (
            "Fresh derivation E-G: per-block V_hyp with reference knots "
            "(3) → unknot, (2,1) → figure-8, (1,1,1) → trefoil; only "
            "std block contributes non-zero V_hyp (2.02988...).  Hecke "
            "energy computed two ways (Plancherel-derived and LP-dual); "
            "characters via Hoefsmit seminormal matrices; prefactor "
            "deferred to user.  Output per-partition contributions and "
            "multiple prefactor-choice columns for the user to pick."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "V_fig8": mp.nstr(VOL_FIG8, 40),
        "proton": p,
        "neutron": n,
    }
    out = Path(__file__).parent / "fresh-derivation-pn-steps-E-G.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
