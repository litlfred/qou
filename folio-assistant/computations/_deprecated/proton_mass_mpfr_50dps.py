#!/usr/bin/env python3
"""
Plan F advance: evaluate the proton Habiro tr_M polynomial at q_0
to 50 dps and compare to the f64 production-pipeline value.

The Habiro witness `habiro-coefficients-atomic.witness.json` carries
proton's symbolic Markov trace as a rational function in q
(degree-24 numerator over degree-14 denominator). This script:

  1. Loads the symbolic tr_M_in_q for proton.
  2. Substitutes q = q_0 (50 dps from q-pinning-50-digit witness).
  3. Computes B(p) = m_e · tr_M(q_0) at 50 dps via mpmath.
  4. Compares against the f64 m_p_pred from mass-table-best.

This is the first end-to-end mpmath datapoint for the proton mass
derivation: it short-circuits the prediction path's f64 floor by
reading the symbolic tr_M directly.

Output: `proton-mass-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from mpmath import mp, mpf

mp.dps = 50

HERE = Path(__file__).parent
HABIRO = HERE / "habiro-coefficients-atomic.witness.json"
Q0 = HERE / "q-pinning-50-digit.witness.json"
MTB = HERE / "mass-table-best.witness.json"
OUT = HERE / "proton-mass-mpfr-50dps.witness.json"


def main() -> int:
    habiro = json.load(open(HABIRO))
    proton = habiro["results"]["p (proton, A=1)"]
    tr_M_in_q_str = proton["tr_M_in_q"]
    print(f"  proton tr_M_in_q = {tr_M_in_q_str[:100]}...")

    q = sp.Symbol("q")  # match sympify's default symbol (no positivity)
    tr_M_sym = sp.sympify(tr_M_in_q_str)

    # Sanity: tr_M_sym should be a rational function in q.
    # Substitute q = q_0 with high-precision sympy Float, then convert.
    q0_str = json.load(open(Q0))["derived_50_digit"]["q"]
    print(f"  q_0 (50 dps) = {q0_str}")

    q0_sym = sp.Float(q0_str, 60)  # 60 internal digits for safety
    # Force-substitute the q symbol that's in tr_M_sym
    free_syms = list(tr_M_sym.free_symbols)
    print(f"  free symbols in tr_M: {free_syms}")
    tr_at_q0 = sp.N(tr_M_sym.subs({s: q0_sym for s in free_syms}), 50)
    tr_at_q0_mpf = mpf(str(tr_at_q0))
    print(f"  tr_M(q_0) at 50 dps = {tr_at_q0_mpf}")

    # B_proton from the categorical pipeline (no shortcut).
    M_E_MEV = mpf("0.51099895")
    rho = 1  # proton's structural prefactor — see prop:atom-knot-mass-derivation
    B_p_mpfr = M_E_MEV * rho * tr_at_q0_mpf
    print(f"  B(p) = m_e · ρ · tr_M(q_0) [50 dps] = {B_p_mpfr} MeV")

    # f64 baseline from mass-table-best.
    mtb = json.load(open(MTB))
    m_p_pred_f64 = mtb["data"]["particles"]["m_p_pred_MeV"]
    m_p_codata = mtb["data"]["particles"]["m_p_codata_MeV"]
    print(f"  m_p_pred (f64 pipeline)        = {m_p_pred_f64} MeV")
    print(f"  m_p   (CODATA 2022)            = {m_p_codata} MeV")
    print(f"  Habiro tr_M direct path        = {B_p_mpfr} MeV")

    # The proton's mass is m_p = (B_p part) + m_p_residual_terms.  This
    # script captures only the Term 1 |tr_M(T_w)| contribution; the
    # other five terms of the unified mass formula contribute too.
    # So Habiro path won't equal m_p directly; it equals Term 1 only.

    out = {
        "computation": "proton-mass-mpfr-50dps",
        "description":
            "Plan F advance — evaluates the proton Habiro tr_M polynomial "
            "(from habiro-coefficients-atomic.witness.json) at q_0 to 50 "
            "dps, demonstrating the first end-to-end mpmath datapoint for "
            "the categorical mass derivation. NOTE: this is Term 1 of the "
            "six-term unified mass formula only; comparing to m_p_pred from "
            "mass-table-best is not apples-to-apples.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "atom": "proton",
        "Z": 1, "N": 0, "A": 1,
        "rho_factor": rho,
        "tr_M_in_q_symbolic": tr_M_in_q_str,
        "q_0_50dps": q0_str,
        "tr_M_at_q0_50dps": str(tr_at_q0_mpf),
        "term_1_only_b_pred_mev_50dps": str(B_p_mpfr),
        "comparison_for_reference_only": {
            "m_p_codata_mev_f64": m_p_codata,
            "m_p_pred_mev_f64_full_pipeline": m_p_pred_f64,
            "note":
                "term_1_only_b_pred_mev_50dps captures only Term 1 of the "
                "six-term mass formula; not directly comparable to m_p_pred "
                "which sums all six terms.",
        },
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
