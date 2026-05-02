#!/usr/bin/env python3
"""
D as a linear combination of link volumes.

D's atom Hecke element is a sum over basis words in H_6(q):
  beta_D = sum_w c_w(q) * w

This probe computes, at q = q_0:
  V_nf(D) = sum_w c_w(q_0) * V_hyp( closure of w in B_6 )

where V_hyp is SnapPy's hyperbolic volume of the braid closure in
the 3-sphere.  Compares to:
  V_target = B_AME(D) / m_e = 4.35328

Purpose: test whether D's 1.09% residual stems from approximating
the full linear combination by a single knot match (6_2 at
Vol 4.40).  If V_nf(D) matches V_target at ppb, the linear-
combination picture is vindicated.
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

import sympy as sp
import mpmath

# Precision applied only when run as main; prevents import-time
# side effects on shared mpmath state.
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
from witness_polynomial import expose_polynomial

B_D_AME = 2.22456612
TARGET_VOL = B_D_AME / M_E_MEV


def _factor_from(c_f: float, d_f: float, g: int) -> SymbolicHeckeElement:
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


def build_d_nf() -> SymbolicHeckeElement:
    print("  Building D's symbolic NF via Groebner-Shirshov reduction…")
    word = atom_braid_word_3A(1, 1)
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since_reduce = 0
    t0 = time.time()
    for (c_f, d_f, g) in word:
        elem = elem * _factor_from(c_f, d_f, g)
        since_reduce += 1
        if since_reduce >= 4:
            elem, _ = div.reduce(elem)
            since_reduce = 0
    if since_reduce > 0:
        elem, _ = div.reduce(elem)
    print(f"  NF: {elem.n_terms()} terms in {time.time()-t0:.1f}s")
    return elem


def word_to_braid_ints(basis_word: tuple) -> list[int]:
    """Convert a basis sigma-word (tuple of positive ints) to braid ints.

    Basis words in H_n(q) are already positive (only σ_i, no inverses).
    SnapPy uses 1-indexed: σ_g (0-indexed) becomes g+1.
    """
    return [g + 1 for g in basis_word]


def vol_of_word(basis_word: tuple) -> dict:
    """Compute V_hyp of the Markov closure of basis_word in B_n."""
    import snappy
    braid = word_to_braid_ints(basis_word)
    if len(braid) == 0:
        return {"vol": 0.0, "hp": None, "is_hyperbolic": False, "note": "empty"}
    try:
        L = snappy.Link(braid_closure=braid)
        E = L.exterior()
        v_raw = E.volume()
        v = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
    except Exception as e:
        return {"vol": None, "hp": None, "error": str(e)}
    hp_str = None
    if v > 0.5:
        try:
            Eh = E.high_precision()
            rp = Eh.volume().real if hasattr(Eh.volume(), "real") \
                 else Eh.volume()
            hp_str = mpmath.nstr(mpmath.mpf(str(rp)), 50)
        except Exception:
            pass
    return {
        "vol": v, "hp": hp_str,
        "is_hyperbolic": v > 0.5,
        "n_components": len(L.link_components),
    }


def main() -> int:
    print("=" * 100)
    print("D = linear combination of link volumes (NF-weighted)")
    print(f"  Target Vol = B_AME(D)/m_e = {TARGET_VOL:.10f}")
    print("=" * 100)

    # Build NF
    nf = build_d_nf()

    q_mp = mpmath.mpf(str(Q0_FLOAT))
    results = []
    weighted_sum = mpmath.mpf(0)
    print(f"\n  Computing hyp volume for each of {nf.n_terms()} basis words:")
    print(f"  {'basis':<24} {'c_w(q0)':>14} "
          f"{'V_hyp(closure)':>14} {'hyp?':>6} {'contribution':>14}")
    print("  " + "-" * 82)
    items = sorted(nf.terms.items(), key=lambda kv: (len(kv[0]), kv[0]))
    for (basis, coeff) in items:
        coeff_val = float(sp.N(coeff.subs(q_sym, sp.Rational(str(Q0_FLOAT)))))
        vol_info = vol_of_word(basis)
        v = vol_info.get("vol", None)
        if v is None or not isinstance(v, float):
            print(f"  {str(basis):<24} {coeff_val:>+14.6e}  [error]")
            continue
        contribution = coeff_val * v
        weighted_sum += mpmath.mpf(str(contribution))
        hypflag = "Y" if vol_info["is_hyperbolic"] else "N"
        basis_str = "1" if not basis else "σ" + "σ".join(map(str, basis))
        print(f"  {basis_str:<24} {coeff_val:>+14.6e} "
              f"{v:>14.8f}  {hypflag:>6}  {contribution:>+14.6e}")
        results.append({
            "basis": list(basis),
            "c_w_q0": coeff_val,
            "c_w_symbolic": str(sp.factor(coeff)),
            "c_w_polynomial": expose_polynomial(coeff, q_sym),
            "V_hyp_float": v,
            "V_hyp_hp": vol_info.get("hp"),
            "is_hyperbolic": vol_info["is_hyperbolic"],
            "n_components": vol_info.get("n_components"),
            "contribution": contribution,
        })

    print(f"\n  Σ c_w(q₀) · V_hyp(ŵ) = {float(weighted_sum):.10f}")
    print(f"  Target  B_AME/m_e     = {TARGET_VOL:.10f}")
    print(f"  Residual               = "
          f"{float(weighted_sum) - TARGET_VOL:+.10f}")
    rel = (float(weighted_sum) - TARGET_VOL) / TARGET_VOL
    print(f"  Relative error        = {rel*100:+.4f}%  = "
          f"{rel*1e9:+.3e} ppb")

    # Compare to single-knot census match
    kashaev_single = 4.4008325161230461
    print(f"\n  For reference:")
    print(f"    Single-knot Kashaev (6_2 census match): {kashaev_single:.10f}")
    print(f"      → err vs target: "
          f"{(kashaev_single - TARGET_VOL)/TARGET_VOL*100:+.4f}%")
    print(f"    NF-weighted sum: {float(weighted_sum):.10f}")
    print(f"      → err vs target: {rel*100:+.4f}%")

    witness = {
        "computation": "d-nf-weighted-vol",
        "description": (
            "Compute V_hyp(closure of w) for each NF basis word w of D, "
            "weight by coefficient c_w(q_0), sum. Tests whether D as a "
            "linear combination of link volumes matches B_AME/m_e."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0_FLOAT, "m_e_MeV": M_E_MEV,
            "target_vol": TARGET_VOL, "B_AME_D": B_D_AME,
        },
        "nf_terms": results,
        "weighted_sum_float": float(weighted_sum),
        "residual_vs_target": float(weighted_sum) - TARGET_VOL,
        "relative_error_pct": rel * 100,
        "relative_error_ppb": rel * 1e9,
    }
    out = Path(__file__).parent / "d-nf-weighted-vol.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
