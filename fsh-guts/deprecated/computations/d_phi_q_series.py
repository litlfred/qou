#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
D via Φ_q tower = Euler-series finite sum.

Replaces the infinite product Φ_q(v) = Π_{k=1}^∞ (1 - q^{-k}v)^{-1}
with the Euler-series identity (Andrews-Askey-Roy; q-binomial theorem):

    Φ_q(v) = Σ_{n=0}^∞  v^n / (q^{-1}; q^{-1})_n

where (a; q)_n = (1-a)(1-aq)...(1-aq^{n-1}) is the q-Pochhammer symbol.

At q = q_0 ≈ 1.11, |q_0^{-1}| ≈ 0.9, so v^n / (q^{-1};q^{-1})_n decays
geometrically; truncating at n = 50 gives sub-ppb precision for |v| < 1.

The "accumulation on the full tower" is then expressed as a finite
series over brane-tower levels n = 0, 1, 2, ..., n_max with explicit
coefficients.  No roots of unity; no singular limits.

Per basis word w of D's 32-term NF:
  * Compute Jones-polynomial contribution J(w, q) in fundamental rep
  * Accumulate Φ_q-tower contributions via the truncated series
  * Sum over NF with coefficients c_w(q_0)
"""
from __future__ import annotations

import sys
import json
import time
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp
import mpmath

# Precision applied only when run as main.  Local high-precision
# blocks inside helper functions use mpmath.workdps instead.
_MP_DPS = 50
if __name__ == "__main__":
    mpmath.mp.dps = _MP_DPS

from hecke_symbolic import (
    SymbolicHeckeElement, SymbolicHeckeDivision,
    q as q_sym, HA as HA_sym,
)
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV


B_D_AME = 2.22456612
TARGET_VOL = B_D_AME / M_E_MEV
Q0_MP = mpmath.mpf(str(Q0_FLOAT))
Q0_INV = mpmath.mpf(1) / Q0_MP


def _factor_from(c_f, d_f, g):
    c = sp.Integer(1) if abs(c_f - 1.0) < 1e-6 else sp.Integer(0)
    if abs(d_f) < 1e-12:
        d = sp.Integer(0)
    elif abs(d_f + float(HA_sym.subs(q_sym,
                                          sp.Rational(str(Q0_FLOAT))))) < 1e-3:
        d = -HA_sym
    elif abs(d_f + 0.5 * float(HA_sym.subs(q_sym,
                                                sp.Rational(str(Q0_FLOAT))))) < 1e-3:
        d = -HA_sym / 2
    else:
        d = sp.nsimplify(d_f)
    return SymbolicHeckeElement({(g,): c, (): d})


def build_d_nf():
    word = atom_braid_word_3A(1, 1)
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since = 0
    for (c_f, d_f, g) in word:
        elem = elem * _factor_from(c_f, d_f, g)
        since += 1
        if since >= 4:
            elem, _ = div.reduce(elem)
            since = 0
    if since > 0:
        elem, _ = div.reduce(elem)
    return elem


def q_pochhammer(a, n):
    """(a; q)_n = (1-a)(1-aq)(1-aq²)...(1-aq^{n-1}).  O(n) per call.

    For loops over increasing n use the iterative update inside
    phi_q_series below instead (saves O(n_max²) → O(n_max)).
    """
    p = mpmath.mpf(1)
    for k in range(n):
        p *= (mpmath.mpf(1) - a * Q0_INV ** k)
    return p


def phi_q_product(v, max_iter: int = 2000):
    """Φ_q(v) = Π_{k=1}^∞ (1 − q^{-k} v)^{-1} — the product form.

    Converges for any |v| < q (not just |v| < 1), so serves as a
    fallback when the Euler series phi_q_series diverges.  At q = q_0
    ≈ 1.11 the convergence radius is |v| < 1.11.
    """
    v_mp = mpmath.mpf(v) if isinstance(v, (int, float, mpmath.mpf)) else mpmath.mpc(v)
    if abs(v_mp) >= Q0_MP:
        return mpmath.mpc('inf')
    prod = mpmath.mpf(1) if abs(v_mp) < 1 else mpmath.mpc(1, 0)
    coef = Q0_INV
    for k in range(1, max_iter + 1):
        term = mpmath.mpf(1) - coef * v_mp
        if abs(term) < mpmath.mpf('1e-300'):
            return mpmath.mpc('inf')
        prod /= term
        if abs(coef * v_mp) < mpmath.mpf('1e-60'):
            break
        coef *= Q0_INV
    return prod


def phi_q_series(v, n_max: int = 50):
    """Φ_q(v) = Σ_{n=0}^{n_max} v^n / (q^{-1}; q^{-1})_n.

    At q = q_0 = 1.11, |q_0^{-1}| = 0.901, the terms decay as
    |v|^n / (a geometric denominator) → sub-ppb at n_max = 50
    for |v| < 1.

    Uses iterative update for the Pochhammer symbol and for v^n, so
    the whole series is O(n_max) arithmetic operations (not O(n_max²)).

    **Fallback for |v| ≥ 1**: the Euler-series form diverges (terms
    |v|^n grow before Pochhammer damps them).  We delegate to the
    product form phi_q_product which converges for all |v| < q.
    """
    v_abs = abs(v)
    if v_abs >= 1:
        return phi_q_product(v)
    total = mpmath.mpf(0)
    v_mp = mpmath.mpf(v) if isinstance(v, (int, float)) else mpmath.mpc(v)
    # Iterative (a; q)_n = (a; q)_{n-1} · (1 − a · q^{n-1})
    # with a = Q0_INV, q = Q0_INV.
    a_poch = Q0_INV
    poch = mpmath.mpf(1)                  # (a; q)_0 = 1
    v_pow = mpmath.mpf(1)                 # v^0 = 1
    a_factor = mpmath.mpf(1)              # Q0_INV^{n-1} at n=1 starts at 1
    for n in range(n_max + 1):
        if abs(poch) < mpmath.mpf("1e-200"):
            break
        term = v_pow / poch
        total += term
        if abs(term) < mpmath.mpf("1e-60") and n > 5:
            break
        # Update for next iteration: multiply by (1 − a · q^n)
        poch *= (mpmath.mpf(1) - a_poch * a_factor)
        a_factor *= Q0_INV
        v_pow *= v_mp
    return total


def _v_hat_chain_at_vertex(k: int, z, h) -> "mpmath.mpf":
    """V̂ of σ_g^k at a single vertex g, via the H_2 transfer recurrence.

    H_2 is generator-independent (only one σ available), so V̂ depends
    only on the exponent k, not on the vertex index g.
    """
    a = mpmath.mpf(0)
    b = mpmath.mpf(1)
    for _ in range(k):
        a, b = a * h + b, a
    return z * a + b


def v_hat_std_of_word(basis_word: tuple) -> complex:
    """Transfer-matrix V̂^std for a basis word in H_6(q) at q₀.

    Three paths, in order of correctness:

    1. **Chain case** (all generators identical): use the H_2 transfer
       recurrence on σ_g^k directly.

    2. **Disjoint case** (all generator pairs have |i − j| ≥ 2): σ_i and
       σ_j commute in H_n, so V̂ factors as Π_g V̂(σ_g^{c_g}) where
       c_g = count of σ_g in the word.

    3. **Adjacent-generator case** (some pair has |i − j| = 1): the
       braid relation σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1} couples the
       standard-rep channels across vertices and the per-vertex
       factorization is NOT exact.  We fall back to returning NaN so
       that the caller can skip this word rather than silently using
       the wrong value.  A principled fix requires the explicit
       Hoefsmit seminormal matrices of H_n on the standard rep shape
       (n−1, 1) — not implemented here because this module is
       DIAGNOSTIC ONLY.

    Returns complex(NaN) for path 3 so that np.isnan detects it.
    """
    if not basis_word:
        return complex(1.0)
    z = mpmath.mpf(1) / (mpmath.sqrt(Q0_MP) + mpmath.mpf(1) / mpmath.sqrt(Q0_MP))
    h = Q0_MP - mpmath.mpf(1) / Q0_MP  # H_A = q - q⁻¹
    gens = sorted(set(basis_word))
    # Path 1: chain
    if len(gens) == 1:
        return complex(_v_hat_chain_at_vertex(len(basis_word), z, h))
    # Path 3 (check first): any adjacent pair forbids factorization
    for i in range(len(gens) - 1):
        if gens[i + 1] - gens[i] == 1:
            return complex(float("nan"))
    # Path 2: disjoint generators commute → product of per-vertex V̂
    from collections import Counter
    counts = Counter(basis_word)
    v_total = mpmath.mpf(1)
    for _, k in counts.items():
        v_total *= _v_hat_chain_at_vertex(k, z, h)
    return complex(v_total)


def main() -> int:
    print("=" * 100)
    print("D via Φ_q TOWER AS FINITE EULER SERIES")
    print(f"  Target: B_AME(D)/m_e = {TARGET_VOL:.10f}")
    print(f"  q₀ = {mpmath.nstr(Q0_MP, 20)}")
    print(f"  |q₀^{{-1}}| = {float(Q0_INV):.6f}  "
          f"(Euler series converges as |v|^n · this^n)")
    print("=" * 100)

    # Verify Φ_q identity on a known value
    print("\n  Sanity check Φ_q series:")
    test_vs = [0.1, 0.5, 0.9]
    for v in test_vs:
        p_series = phi_q_series(v, n_max=80)
        # Direct product:
        p_prod = mpmath.mpf(1)
        for k in range(1, 200):
            p_prod *= mpmath.mpf(1) / (mpmath.mpf(1) - Q0_INV ** k * v)
        rel_err = abs(p_series - p_prod) / abs(p_prod) if abs(p_prod) > 0 else 0
        print(f"    v={v:<6.2f}: series={mpmath.nstr(p_series, 10):>18}, "
              f"prod={mpmath.nstr(p_prod, 10):>18}, rel_err={float(rel_err):.1e}")

    # Build D's NF
    print("\n  Building D's NF…")
    nf = build_d_nf()
    print(f"  {nf.n_terms()} basis terms")

    # For each basis word, compute V̂ then Φ_q(V̂, q₀)
    print(f"\n  Per-basis-word Φ_q(V̂) contributions at q₀:")
    print(f"  {'basis':<20} {'c_w(q₀)':>14} {'V̂':>14} "
          f"{'ln|Φ_q(V̂)|':>14} {'contribution':>14}")
    print("  " + "-" * 82)

    total_ln_phi = mpmath.mpf(0)
    n_strands = 6
    rows = []
    skipped_adjacent = 0
    import math as _math
    for (basis, coeff) in sorted(nf.terms.items(),
                                   key=lambda kv: (len(kv[0]), kv[0])):
        coeff_fn = sp.lambdify(q_sym, coeff, modules=["mpmath"])
        c_val = complex(coeff_fn(Q0_FLOAT))
        v_hat = v_hat_std_of_word(basis)
        if _math.isnan(v_hat.real):
            # Adjacent-generator braid: per-vertex factorization not
            # exact (see v_hat_std_of_word docstring).  Skipped.
            skipped_adjacent += 1
            continue
        phi_v = phi_q_series(v_hat.real, n_max=50)
        if abs(phi_v) < 1e-50:
            continue
        ln_phi = mpmath.log(abs(phi_v))
        contribution = mpmath.mpf(str(c_val.real)) * ln_phi
        total_ln_phi += contribution
        basis_str = "1" if not basis else "σ" + "σ".join(map(str, basis))
        print(f"  {basis_str:<20} {c_val.real:>+14.6e} "
              f"{float(v_hat.real):>+14.6f} {float(ln_phi):>+14.6f} "
              f"{float(contribution):>+14.6e}")
        rows.append({
            "basis": list(basis),
            "c_w_q0": c_val.real,
            "V_hat": float(v_hat.real),
            "ln_phi_V": float(ln_phi),
            "contribution": float(contribution),
        })

    total = float(total_ln_phi)
    if skipped_adjacent:
        print(f"\n  (skipped {skipped_adjacent} basis words with "
              f"adjacent-generator braids — per-vertex V̂ "
              f"factorization not exact)")
    print(f"\n  Σ c_w · ln|Φ_q(V̂_w)|  = {total:.10f}")
    print(f"  Target (B_AME/m_e)    = {TARGET_VOL:.10f}")
    print(f"  Residual              = {total - TARGET_VOL:+.10f}")
    print(f"  Relative err          = "
          f"{(total - TARGET_VOL)/TARGET_VOL*100:+.4f}%  = "
          f"{(total - TARGET_VOL)/TARGET_VOL*1e9:+.3e} ppb")

    # Check also m_e · total (if formula is B = m_e · Σ)
    B_pred = M_E_MEV * total
    print(f"\n  Alternative: B = m_e · Σ = {B_pred:.6f} MeV "
          f"(B_AME = {B_D_AME})")
    print(f"    err = "
          f"{(B_pred - B_D_AME)/B_D_AME*100:+.3f}%")

    # Save witness
    witness = {
        "computation": "d-phi-q-series",
        "description": (
            "D via Φ_q Euler-series expansion: truncate infinite "
            "product Π(1-q^{-k}v)^{-1} at n_max = 50 terms of the "
            "Euler series Σ v^n/(q^{-1};q^{-1})_n.  For each NF basis "
            "word, compute V̂, then Φ_q(V̂, q_0) via finite series, "
            "log-abs, weight by c_w(q_0), sum.  No roots of unity."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0_FLOAT,
            "q_0_inv": float(Q0_INV),
            "target_vol": TARGET_VOL,
            "n_strands": n_strands,
            "series_n_max": 50,
        },
        "n_basis_skipped_adjacent": skipped_adjacent,
        "per_basis": rows,
        "total_ln_phi_weighted": total,
        "target": TARGET_VOL,
        "residual": total - TARGET_VOL,
        "relative_err_ppb": (total - TARGET_VOL) / TARGET_VOL * 1e9,
    }
    out = Path(__file__).parent / "d-phi-q-series.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
