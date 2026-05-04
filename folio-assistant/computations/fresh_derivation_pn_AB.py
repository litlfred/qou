#!/usr/bin/env python3
"""
Fresh p/n derivation, variants A and B:

  A. V_hyp per particle (not per partition).
     Computed as Kashaev-style effective volume from the full Markov
     trace of the particle's braid at q₀:
         V_hyp_eff(ρ, q) := 2π · log|tr_M(β_ρ, q)| / n_strands
     This is a rational function of q (via symbolic sympy trace), and
     evaluates at q₀ to a specific real number.  If the particle's
     closure is actually hyperbolic, this converges to V_hyp in the
     Kashaev (N → ∞) limit; for finite q₀ it is a q-dependent analog.

  B. SDP-solved y_λ shadow prices.
     Set up the confinement LP for n = 3:
         min  Σ c_λ x_λ
         s.t. Σ x_λ = 1
              G_λλ' x_λ' ≥ 0   (Frobenius positivity, G = diag(d_q²))
              x_λ ≥ 0
     where c_λ is the per-block cost.  Two choices tried:
         (i) c_λ = 1/d_q(λ)    — favour std
         (ii) c_λ = d_q(λ)     — favour sym/alt
     Dual y_λ extracted from LP solution.

Combining A and B, the fresh mass estimate is:
   m_fresh(ρ) = V_hyp_eff(ρ, q₀) · Σ_λ y_λ · χ_λ(β_ρ)
              · prefactor

Prefactor list tried as in Steps E-G.

Output: fresh-derivation-pn-AB.witness.json
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
from scipy.optimize import linprog

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


def classical_dim(shape):
    n = sum(shape)
    hooks = young_hooks(shape)
    fact_n = mp.mpf(1)
    for k in range(1, n + 1):
        fact_n *= k
    hp = mp.mpf(1)
    for h in hooks:
        hp *= h
    return fact_n / hp


def dim_q_value(shape):
    return mp.mpf(str(float(dim_q(shape))))


def chi_at_q0(shape, word):
    sigmas_sym, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return mp.mpc(0)
    q_sym = sp.Symbol('q')
    sigmas_num = []
    for S in sigmas_sym:
        try:
            fn = sp.lambdify(q_sym, sp.Matrix(S), modules='numpy')
            M = np.asarray(fn(complex(Q0_FLOAT)), dtype=complex)
        except Exception:
            M = np.zeros((dim, dim), dtype=complex)
            for i in range(dim):
                for j in range(dim):
                    e = S[i, j]
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
    word = []
    for c, d in g0_chain:
        word.append((c, d, 0))
    for c, d in g1_chain:
        word.append((c, d, 1))
    return word


# ──────────────────────────────────────────────────────────────
# A.  V_hyp per particle via Kashaev-style log of Markov trace
# ──────────────────────────────────────────────────────────────
def markov_trace_via_plancherel(word, n):
    """tr_M(β) = Σ_λ w_λ · χ_λ(β)/d_λ with Plancherel weights
    w_λ = d_q(λ)²/[n]_q!.  Uses classical d_λ for normalisation
    (consistent with gemini's τ(1)=1 fix elsewhere we now use d_q,
    but for tr_M of a generic β we divide by CLASSICAL dim per
    the orthogonality of characters)."""
    nfac = q_fact(n)
    total = mp.mpc(0)
    for shape in partitions_of(n):
        dq = dim_q_value(shape)
        d_cl = classical_dim(shape)
        chi = chi_at_q0(shape, word)
        w_lambda = dq * dq / nfac
        total += w_lambda * chi / d_cl
    return total


def V_hyp_kashaev_eff(word, n_strands):
    """Effective hyperbolic volume: V_hyp_eff = 2π · log|tr_M| / n."""
    tr = markov_trace_via_plancherel(word, n_strands)
    abs_tr = mp.fabs(tr)
    if abs_tr < mp.mpf("1e-30"):
        return mp.mpf(0), mp.mpc(0)
    return (2 * mp.pi * mp.log(abs_tr) / n_strands), tr


# ──────────────────────────────────────────────────────────────
# B.  SDP-solved shadow prices y_λ
# ──────────────────────────────────────────────────────────────
def solve_confinement_lp(n: int, cost_mode: str = "inverse_dq"):
    """Solve:
         min  Σ c_λ x_λ
         s.t. Σ x_λ = 1                   (normalisation)
              x_λ ≥ 0

    Dual shadow price for the equality constraint is y_eq.  For each
    λ, the relative shadow price against the λ-specific inequality
    x_λ ≥ 0 is y_λ = c_λ − y_eq (reduced cost).  We report |y_λ|.

    cost_mode:
      'inverse_dq': c_λ = 1/d_q(λ)
      'dq':        c_λ = d_q(λ)
      'd_classical': c_λ = d_λ (classical)
    """
    parts = list(partitions_of(n))
    c = []
    for shape in parts:
        if cost_mode == "inverse_dq":
            cv = float(1.0 / dim_q_value(shape))
        elif cost_mode == "dq":
            cv = float(dim_q_value(shape))
        elif cost_mode == "d_classical":
            cv = float(classical_dim(shape))
        else:
            raise ValueError(cost_mode)
        c.append(cv)
    # A_eq x = b_eq:  sum = 1
    A_eq = [[1.0] * len(parts)]
    b_eq = [1.0]
    # x >= 0 via bounds
    bounds = [(0, None)] * len(parts)
    res = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                   method="highs")
    if not res.success:
        return {"success": False, "message": res.message}
    # Dual: equality-constraint multiplier (shadow price for the
    # normalisation) is res.eqlin.marginals (highs) or res.eq_dual
    try:
        y_eq = float(res.eqlin.marginals[0])
    except Exception:
        y_eq = None
    # Reduced costs: y_λ = c_λ − y_eq (or equivalently shadow prices
    # of x_λ ≥ 0)
    y_lambda = {}
    for shape, cv in zip(parts, c):
        rc = cv - (y_eq if y_eq is not None else 0)
        y_lambda[tuple(shape)] = float(rc)
    return {
        "success": True,
        "parts": [list(p) for p in parts],
        "c": c,
        "x": list(res.x),
        "obj": float(res.fun),
        "y_eq": y_eq,
        "y_lambda": {str(list(k)): v for k, v in y_lambda.items()},
    }


# ──────────────────────────────────────────────────────────────
# Assembly
# ──────────────────────────────────────────────────────────────
def process(name, g0, g1, m_codata, n=3):
    print(f"\n{'=' * 110}")
    print(f"{name} — target m_codata = {m_codata} MeV")
    print('=' * 110)
    word = build_particle_word(g0, g1)

    # A.  V_hyp per particle
    V_kash, tr_M = V_hyp_kashaev_eff(word, n)
    print(f"  A.  |tr_M(β)| = {mp.nstr(mp.fabs(tr_M), 15)}")
    print(f"      V_hyp_eff = 2π·log|tr_M|/n = {mp.nstr(V_kash, 15)}")
    print()

    # B.  SDP y_λ across three cost modes
    print(f"  B.  LP solution by cost mode:")
    print(f"      {'cost':<14}  "
          f"{'y_(3)':>12} {'y_(2,1)':>12} {'y_(1,1,1)':>12}")
    lp_results = {}
    for mode in ["inverse_dq", "dq", "d_classical"]:
        lp = solve_confinement_lp(n, cost_mode=mode)
        lp_results[mode] = lp
        if lp["success"]:
            yl = lp["y_lambda"]
            print(f"      {mode:<14}  {yl.get('[3]', 0):>+12.6f} "
                  f"{yl.get('[2, 1]', 0):>+12.6f} "
                  f"{yl.get('[1, 1, 1]', 0):>+12.6f}")
        else:
            print(f"      {mode:<14}  LP failed: {lp.get('message')}")
    print()

    # Assembly: mass_fresh = V_kash · Σ_λ y_λ · χ_λ(β)
    print(f"  ASSEMBLY: m_fresh = V_kash · Σ_λ |y_λ| · |χ_λ(β)|")
    print(f"      {'mode':<14}  {'Σ|y_λ·χ_λ|':>14} "
          f"{'V_kash·Σ':>14} {'prefactor=m_e':>14} {'err%':>10}")

    chi_per = {shape: chi_at_q0(shape, word)
                for shape in partitions_of(n)}

    results_assembly = []
    for mode in ["inverse_dq", "dq", "d_classical"]:
        if not lp_results[mode]["success"]:
            continue
        yl = lp_results[mode]["y_lambda"]
        S = mp.mpf(0)
        for shape, chi in chi_per.items():
            y = yl.get(str(list(shape)), 0)
            S += mp.fabs(mp.mpf(y) * mp.mpc(chi.real, chi.imag))
        prod = V_kash * S
        for pref_name, pref_val in [
            ("m_e", mp.mpf(str(M_E_MEV))),
            ("m_e · 8G",
              mp.mpf(str(M_E_MEV)) * 8 * mp.mpf("0.915965594177")),
            ("m_e · 2π", mp.mpf(str(M_E_MEV)) * 2 * mp.pi),
        ]:
            m_fresh = pref_val * prod
            err = (float(m_fresh) - m_codata) / m_codata * 100
            label = f"{mode}, {pref_name}"
            print(f"      {label:<28}  {float(S):>+14.6e} "
                  f"{float(prod):>+14.6e} {float(m_fresh):>+14.4f} "
                  f"{err:>+10.2f}%")
            results_assembly.append({
                "cost_mode": mode,
                "prefactor_name": pref_name,
                "prefactor_value": float(pref_val),
                "sum_y_chi_abs": float(S),
                "V_kash_times_sum": float(prod),
                "m_fresh_MeV": float(m_fresh),
                "err_pct": err,
            })

    return {
        "name": name,
        "m_codata": m_codata,
        "V_kash": mp.nstr(V_kash, 20),
        "tr_M": {"re": float(tr_M.real), "im": float(tr_M.imag)},
        "chi_per_lambda": {
            str(list(k)): {"re": float(v.real), "im": float(v.imag)}
            for k, v in chi_per.items()},
        "lp_results": lp_results,
        "assembly": results_assembly,
    }


def main() -> int:
    print("=" * 110)
    print("FRESH DERIVATION — variants A + B combined")
    print("=" * 110)
    p = process("PROTON",  _PROTON_G0,  _PROTON_G1,  M_P_MEV)
    n = process("NEUTRON", _NEUTRON_G0, _NEUTRON_G1, M_N_MEV)

    # Ratio comparison
    print(f"\n{'=' * 110}")
    print("p/n ratio summary")
    print('=' * 110)
    print(f"  CODATA m_p/m_n = {M_P_MEV/M_N_MEV:.8f}")
    # For each cost mode + prefactor, compute p/n ratio
    print(f"  {'cost_mode':<14} {'pref':<10} "
          f"{'m_p/m_n fresh':>16} {'err vs CODATA':>18}")
    for ap in p["assembly"]:
        # Find matching n
        for an in n["assembly"]:
            if (an["cost_mode"] == ap["cost_mode"] and
                    an["prefactor_name"] == ap["prefactor_name"]):
                if abs(an["m_fresh_MeV"]) > 1e-12:
                    ratio = ap["m_fresh_MeV"] / an["m_fresh_MeV"]
                    err = (ratio - M_P_MEV/M_N_MEV) / (M_P_MEV/M_N_MEV) * 100
                    print(f"  {ap['cost_mode']:<14} "
                          f"{ap['prefactor_name']:<10} "
                          f"{ratio:>+16.10f} {err:>+17.4f}%")

    witness = {
        "computation": "fresh-derivation-pn-AB",
        "description": (
            "Variants A (V_hyp per particle via Kashaev eff) + B "
            "(SDP/LP shadow prices y_λ for n=3 partitions) combined.  "
            "Three cost modes (1/d_q, d_q, classical) explored.  "
            "Assembly m_fresh = V_kash · Σ_λ |y_λ·χ_λ(β)| · prefactor."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "proton": p,
        "neutron": n,
    }
    out = Path(__file__).parent / "fresh-derivation-pn-AB.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
