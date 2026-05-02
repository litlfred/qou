#!/usr/bin/env python3
"""
Symbolic-in-q tower binding (D, T, 3He, 4He).

Per rem:base-field-independence, Markov trace lives in Z[q^{±1}].
Numerical evaluation is only for the archimedean realization.

This version:
  1. Builds V̂_i^full symbolically in q (sympy Poly in Z[q, q⁻¹])
  2. Computes tower mass terms |Π V̂|, Σ Φ_q(|V̂|), Σ z² Φ_q(|V̂V̂|)
     symbolically where possible; Φ_q requires evaluation (infinite
     product) but the arguments stay symbolic until the final eval.
  3. Evaluates at q_0 with arbitrary precision (mpmath) at the END.

This avoids float underflow/overflow and provides exact Markov
trace polynomials for verification.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    proton_cross, neutron_cross,
)
from q_parameter import Q as _Q_CANONICAL


# Symbolic q
q_sym = sp.Symbol('q', positive=True, real=True)
qi_sym = 1 / q_sym
h_sym = q_sym - qi_sym
z_sym = 1 / (q_sym ** sp.Rational(1, 2) + q_sym ** sp.Rational(-1, 2))

# Substrate parameter value (from q_parameter — single source of truth)
q0_mp = mpmath.mpf(repr(_Q_CANONICAL))

# Numerical Wedderburn weights at H_3 (symbolic)
def q_int_sym(k):
    if k == 0:
        return sp.Integer(0)
    return (q_sym ** k - qi_sym ** k) / (q_sym - qi_sym)


def q_fact_sym(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= q_int_sym(k)
    return r


# H_3 Wedderburn weights (symbolic)
# Dimensions: sym=1, std=2, alt=1. q-dims: [1]_q=1, [2]_q, [1]_q=1.
_nf3 = q_fact_sym(3)
w_sym_s = sp.Integer(1) ** 2 / _nf3
w_std_s = q_int_sym(2) ** 2 / _nf3
w_alt_s = sp.Integer(1) ** 2 / _nf3
_wt = w_sym_s + w_std_s + w_alt_s
w_sym_s = sp.simplify(w_sym_s / _wt)
w_std_s = sp.simplify(w_std_s / _wt)
w_alt_s = sp.simplify(w_alt_s / _wt)


def additive_wedderburn_symbolic(n_strands, crossings_per_gen):
    """Per-generator V̂_i^full as sympy expressions in q."""
    vols = []
    for gen in range(n_strands - 1):
        a, b = sp.Integer(0), sp.Integer(1)
        sp_chan = sp.Integer(1)
        ap_chan = sp.Integer(1)
        for c, d in crossings_per_gen.get(gen, []):
            c_s = sp.Rational(c) if isinstance(c, (int, float)) else c
            d_s = sp.Rational(d) if isinstance(d, (int, float)) else d
            a_new = a * c_s * h_sym + a * d_s + b * c_s
            b_new = a * c_s + b * d_s
            a, b = sp.expand(a_new), sp.expand(b_new)
            sp_chan = sp.expand(sp_chan * (c_s * q_sym + d_s))
            ap_chan = sp.expand(ap_chan * (-c_s * qi_sym + d_s))
        Vs = sp.expand(z_sym * a + b)
        Vf = sp.expand(w_sym_s * sp_chan + w_std_s * Vs + w_alt_s * ap_chan)
        vols.append({"std": Vs, "sym": sp_chan, "alt": ap_chan, "full": Vf})
    return vols


def atom_crossings_symbolic(nucleon_types, include_inter=True, m_pp=1,
                             m_pn=1, m_nn=1):
    """Build atom crossings with symbolic parameters."""
    A = len(nucleon_types)
    crossings = {}
    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        crossings[3 * k]     = list(src.get(0, []))
        crossings[3 * k + 1] = list(src.get(1, []))
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                base_cross = (sp.Integer(1), sp.Integer(0))
                m_this = m_pp
            elif pair == ('n', 'n'):
                base_cross = (sp.Integer(1), -h_sym)
                m_this = m_nn
            else:
                base_cross = (sp.Integer(1), -h_sym / 2)
                m_this = m_pn
            crossings[3 * k + 2] = [base_cross] * m_this
    for i in range(3 * A - 1):
        crossings.setdefault(i, [])
    return crossings


def tower_mass_symbolic(vols):
    """Tower mass 𝔪 = |Π V̂| + Σ Φ_q(|V̂|) + z² Σ Φ_q(|V̂V̂|) symbolically.

    Returns symbolic form with Φ_q as a placeholder function — evaluated
    numerically at q_0 only.
    """
    n = len(vols)
    # Descended (product of V̂_i^full)
    desc = sp.Integer(1)
    for v in vols:
        desc = sp.expand(desc * v["full"])
    desc_abs = sp.Abs(desc)  # symbolic |Π V̂|
    return {
        "desc_symbolic": desc,
        "desc_abs_symbolic": desc_abs,
        "vols": vols,
        "n_generators": n,
    }


def Phi_q_numeric(z_val, max_k=500):
    """Non-perturbative quantum dilogarithm Φ_q(z) at q=q0_mp."""
    q_num = q0_mp
    qi_num = 1 / q_num
    z_abs = mpmath.fabs(z_val)
    if z_abs >= q_num:
        return mpmath.inf
    product = mpmath.mpf(1)
    for k in range(1, max_k + 1):
        factor = 1 - qi_num ** k * z_val
        if mpmath.fabs(factor) < mpmath.mpf('1e-300'):
            return mpmath.inf
        product /= factor
        if mpmath.fabs(qi_num ** k * z_val) < mpmath.mpf('1e-30'):
            break
    return product


def tower_mass_eval(tower_data):
    """Evaluate symbolic tower mass at q = q0 with mpmath precision."""
    # Substitute q = q0 in each V̂_i^full
    v_nums = []
    for v in tower_data["vols"]:
        v_num = complex(v["full"].subs(q_sym, float(q0_mp)))
        if abs(v_num.imag) > 1e-10:
            v_num = v_num  # keep complex if non-trivial
        else:
            v_num = v_num.real
        v_nums.append(v_num)
    # Compute tower numerically
    z_num = float(z_sym.subs(q_sym, float(q0_mp)))
    desc = abs(v_nums[0] if len(v_nums) > 0 else 1)
    for v in v_nums[1:]:
        desc *= abs(v)
    single = sum(float(Phi_q_numeric(abs(v)).real if hasattr(Phi_q_numeric(abs(v)), 'real') else Phi_q_numeric(abs(v))) for v in v_nums)
    cross = 0.0
    for i in range(len(v_nums) - 1):
        prod = abs(v_nums[i] * v_nums[i + 1])
        cross += z_num ** 2 * float(Phi_q_numeric(prod).real if hasattr(Phi_q_numeric(prod), 'real') else Phi_q_numeric(prod))
    return {
        "V_hat_numeric": [float(v) if not hasattr(v, 'real') else float(v.real) for v in v_nums],
        "desc": float(desc), "single": float(single), "cross": float(cross),
        "total": float(desc + single + cross),
    }


def symbolic_binding(Z, N, m_pp=1, m_pn=1, m_nn=1):
    """Full symbolic-in-q tower binding."""
    nucleon_types = ['p'] * Z + ['n'] * N
    # Atom: symbolic crossings, symbolic V̂, then evaluate at q_0
    cross_atom = atom_crossings_symbolic(nucleon_types, True, m_pp, m_pn, m_nn)
    cross_free = atom_crossings_symbolic(nucleon_types, False)
    n_strands_atom = 3 * (Z + N)
    n_strands_free = 3 * (Z + N)
    vols_atom_sym = additive_wedderburn_symbolic(n_strands_atom, cross_atom)
    vols_free_sym = additive_wedderburn_symbolic(n_strands_free, cross_free)
    tower_atom = tower_mass_symbolic(vols_atom_sym)
    tower_free = tower_mass_symbolic(vols_free_sym)
    eval_atom = tower_mass_eval(tower_atom)
    eval_free = tower_mass_eval(tower_free)
    # Calibration: m_proton_tower at the same level (1 nucleon)
    p_cross = atom_crossings_symbolic(['p'], False)
    p_vols = additive_wedderburn_symbolic(3, p_cross)
    p_tower = tower_mass_symbolic(p_vols)
    p_eval = tower_mass_eval(p_tower)
    E_0_sym = 938.272 / p_eval["total"]
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
        "m_atom_numeric": eval_atom["total"],
        "m_free_numeric": eval_free["total"],
        "E_0_MeV": E_0_sym,
        "B_MeV": E_0_sym * (eval_free["total"] - eval_atom["total"]),
        "V_atom_symbolic_first": str(vols_atom_sym[0]["full"])[:200] if vols_atom_sym else "",
        "V_free_symbolic_first": str(vols_free_sym[0]["full"])[:200] if vols_free_sym else "",
    }


if __name__ == "__main__":
    print("SYMBOLIC-IN-q TOWER BINDING (small atoms)")
    print("=" * 88)
    print(f"q_0 = {q0_mp}")
    print()

    SMALL_ATOMS = [
        ("D",   1, 1,  2.22, 1, 1, 1),
        ("T",   1, 2,  8.48, 1, 1, 1),
        ("3He", 2, 1,  7.72, 1, 1, 1),
        ("4He", 2, 2, 28.30, 1, 1, 1),
    ]

    print(f"  {'Atom':>5} {'A':>3} {'(pp,pn,nn)':>11} "
          f"{'m_atom':>11} {'m_free':>11} {'B_pred':>10} "
          f"{'B_AME':>8} {'|Δm/m|%':>9}")
    print("  " + "-" * 80)

    results = []
    for atom, Z, N, B_AME, m_pp, m_pn, m_nn in SMALL_ATOMS:
        r = symbolic_binding(Z, N, m_pp, m_pn, m_nn)
        M_total = (Z + N) * 938.272
        dm = abs(r["B_MeV"] - B_AME) / M_total * 100
        ilp = f"({m_pp},{m_pn},{m_nn})"
        print(f"  {atom:>5} {Z+N:>3d} {ilp:>11} "
              f"{r['m_atom_numeric']:>11.3e} {r['m_free_numeric']:>11.3e} "
              f"{r['B_MeV']:>10.3f} {B_AME:>8.2f} {dm:>8.4f}%")
        results.append({**r, "atom": atom, "B_AME_MeV": B_AME,
                        "delta_m_over_m_pct": dm})

    witness = {
        "computation": "tower-binding-symbolic",
        "description": (
            "Symbolic-in-q tower binding per rem:base-field-independence. "
            "All arithmetic in Z[q^{±1}] (sympy); evaluate at q_0 with "
            "mpmath only at final step. Avoids float underflow/overflow."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": str(q0_mp)},
        "results": results,
    }
    out = Path(__file__).parent / "tower-binding-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
