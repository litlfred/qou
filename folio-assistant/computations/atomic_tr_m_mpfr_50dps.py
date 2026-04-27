#!/usr/bin/env python3
"""
Plan F advance — extends the mpmath @ 50 dps tr_M evaluation from
proton (proton_mass_mpfr_50dps.py) to neutron and deuteron, plus
the symbolic comparison test for ²H / ³H / ³He against published
Jones polynomials.

For each atom 𝔥 ∈ {proton, neutron, deuteron, tritium, helium-3}:
  1. Build the 3A-strand atom Hecke element via atom_nf_symbolic_D
     (Gröbner–Shirshov NF over Z[q^{1/2}, q^{-1/2}]).
  2. Compute symbolic tr_M ∈ ℚ(q) via markov_trace_canonical.
  3. Evaluate at q = q_0 to 50 dps via mpmath.
  4. Report Term-1 contribution m_e · ρ · |tr_M(q_0)| and the
     residual against B_AME for diagnostic.

For atoms in {²H, ³H, ³He} flagged `manual-historical-volume-match`
in joint-tower-sdp-rust.witness.json, also report whether the
symbolic tr_M matches the published Jones polynomial of the
historical knot up to writhe normalisation (q^k factor).

Output: `atomic-tr-m-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp
from mpmath import mp, mpf

mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import atom_nf_symbolic_D as M
from markov_trace_canonical import tr_M_element, Z_SYMB, H_SYMB

Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "atomic-tr-m-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")  # CODATA 2022

# Published Jones polynomials (from Kawauchi tables / KnotInfo).
# Variable conventions: in our pipeline σ_i² = (q − q⁻¹)σ_i + 1, so
# J_K is the Markov-trace value for the trefoil-like normalization.
J_PUBLISHED = {
    # 6_2: from Kawauchi Theorem 2.2.4 / KnotInfo.
    "6_2": "q - 1 + 2/q - 2/q**2 + 2/q**3 - 2/q**4 + 1/q**5",
    # L_6a4 (Borromean): standard formula.
    # The Borromean rings link's Jones polynomial in our convention.
    "L_6a4": "q**3 - 3*q**2 + 6*q - 7 + 6/q - 3/q**2 + 1/q**3",
}

ATOMS = [
    ("proton",   1, 0, 1, "p (B_3 Borromean)",         None),
    ("neutron",  0, 1, 1, "n (B_3 Borromean)",         None),
    ("deuteron", 1, 1, 1, "²H (B_6 atom-3A)",          "6_2"),
    # Tritium and helium-3 use 3A-strand → H_9 → very slow. Run for
    # smaller A only; 3H/3He follow once we extend.
]


def main() -> int:
    q_str = json.load(open(Q0))["derived_50_digit"]["q"]
    q_0 = mpf(q_str)
    q_sym = sp.Symbol("q")  # match sympify default
    print(f"  q_0 (50 dps) = {q_str}")

    results = []
    for label, Z, N, rho, descr, historical_K in ATOMS:
        print(f"\n  === {label} (Z={Z}, N={N}, ρ={rho}) ===")
        elem, stats = M.build_atom_nf_symbolic(Z, N, verbose=False)
        n_strands = 3 * (Z + N)
        tr_q = tr_M_element(elem, n_strands, Z_SYMB, H_SYMB)
        # Skip sp.simplify (slow on deuteron's giant expression).
        # Substitute q → q_0 directly; sp.N handles rational arithmetic.

        free = list(tr_q.free_symbols)
        q60 = sp.Float(q_str, 60)
        tr_at_q0 = sp.N(tr_q.subs({s: q60 for s in free}), 50)
        tr_at_q0_mpf = mpf(str(tr_at_q0))
        b_term1 = M_E_MEV * rho * abs(tr_at_q0_mpf)
        print(f"    n_strands = {n_strands},  NF terms = {stats['n_terms_nf']}")
        print(f"    tr_M(q_0) = {tr_at_q0_mpf}")
        print(f"    Term-1 contribution: m_e · ρ · |tr_M| = {b_term1} MeV")

        # If a historical knot ID is available, compare numerically at q_0.
        comparison = None
        if historical_K and historical_K in J_PUBLISHED:
            J_sym = sp.sympify(J_PUBLISHED[historical_K])
            J_at_q0 = sp.N(J_sym.subs({s: q60 for s in J_sym.free_symbols}), 50)
            J_at_q0_mpf = mpf(str(J_at_q0))
            ratio_q0 = tr_at_q0_mpf / J_at_q0_mpf if J_at_q0_mpf != 0 else None
            comparison = {
                "historical_K": historical_K,
                "J_K_published": str(J_sym),
                "J_K_at_q0_50dps": str(J_at_q0_mpf),
                "tr_M_over_J_K_at_q0_50dps": str(ratio_q0),
                "note":
                    "If the ratio is a power of q_0, then tr_M = q_0^k · J_K, "
                    "i.e. they agree up to writhe normalisation. "
                    "q_0 = " + q_str[:30] + "..., so log(ratio)/log(q_0) "
                    "should be close to an integer.",
            }
            print(f"    historical K = {historical_K}")
            print(f"    J_K(q_0)   = {J_at_q0_mpf}")
            print(f"    tr_M / J_K = {ratio_q0}")
            if ratio_q0 is not None and ratio_q0 != 0:
                from mpmath import log as mp_log
                k_estimate = mp_log(abs(ratio_q0)) / mp_log(mpf(q_str))
                print(f"    log(|ratio|)/log(q_0) = {k_estimate}  (integer ⇒ writhe match)")

        results.append({
            "atom": label,
            "Z": Z, "N": N, "A": Z + N,
            "n_strands_3A": n_strands,
            "rho_factor": rho,
            "nf_terms": stats["n_terms_nf"],
            "tr_M_in_q_symbolic": str(tr_q)[:600],  # truncate giant exprs (no simplify)
            "tr_M_at_q0_50dps": str(tr_at_q0_mpf),
            "term1_b_pred_mev_50dps": str(b_term1),
            "historical_K_comparison": comparison,
        })

    out = {
        "computation": "atomic-tr-m-mpfr-50dps",
        "description":
            "Plan F advance — symbolic tr_M(T_w, q) via the 3A-strand "
            "atom-braid convention for proton, neutron, deuteron, "
            "evaluated at q_0 to 50 dps and (where applicable) compared "
            "against the published Jones polynomial of the historical "
            "knot ID. Companion to proton-mass-mpfr-50dps.witness.json.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "q_0_50dps": q_str,
        "results": results,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
