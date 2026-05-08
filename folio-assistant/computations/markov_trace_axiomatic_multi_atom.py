#!/usr/bin/env python3
"""
Multi-atom Markov-trace anchor via the axiomatic recursive reducer.

Uses `markov_trace_recursive.markov_trace_of_word` (representation-
theory-free, axiom-only) to compute the Markov trace of every atomic-
braid word for the supported atoms:

  proton  (Z=1, N=0):  σ₁⁷ σ₂⁴            ∈ H_3
  neutron (Z=0, N=1):  σ₁⁶ σ₂⁴ σ₁⁻¹       ∈ H_3
  deuteron (Z=1, N=1): σ₁⁷ σ₂⁴ ⊕ σ₁⁶ σ₂⁴ σ₁⁻¹    (disjoint H_3 ⊗ H_3 ⊂ H_6)
                      = σ₁⁷ σ₂⁴ σ₄⁶ σ₅⁴ σ₄⁻¹      (rebased to gens 4,5)

The Markov axiom values multiply on disjoint clusters in H_n:
  tr_M(α ⊗ β) = tr_M(α) · tr_M(β)
when α uses only σ_{i<k} and β uses only σ_{j>k+1} (commuting clusters
separated by an unused generator slot).  Verified empirically below.

For each atom, emits:
  - symbolic closed form in ℚ(q)
  - numerical value at q_0 (50 dps via mpmath)
  - cross-check against `markov_trace_atomic_proton_full` for proton
  - dimensional anchor ρ_K^CODATA = (m_K/m_e) / |tr_M|

Output: markov-trace-axiomatic-multi-atom.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from markov_trace_recursive import markov_trace_of_word, q as _q  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

q = _q
Q0_MP = mp.mpf(str(Q_MP))


# ── Atomic-braid words ─────────────────────────────────────────
# Convention: positive ints = σ_i (1-indexed), negative = σ_i^{-1}.

ATOMS = {
    "proton": {
        "Z": 1, "N": 0, "n": 3,
        "word": [1] * 7 + [2] * 4,
        "word_str": "σ₁⁷ σ₂⁴",
        "m_MeV": 938.27208816,
    },
    "neutron": {
        "Z": 0, "N": 1, "n": 3,
        "word": [1] * 6 + [2] * 4 + [-1],
        "word_str": "σ₁⁶ σ₂⁴ σ₁⁻¹",
        "m_MeV": 939.56542052,
    },
    "deuteron": {
        # Proton's σ₁⁷σ₂⁴ on strands {1,2,3} ⊕ neutron's σ₁⁶σ₂⁴σ₁⁻¹
        # rebased to strands {4,5,6} via σᵢ → σᵢ₊₃.
        # Total: σ₁⁷ σ₂⁴ σ₄⁶ σ₅⁴ σ₄⁻¹ (22 crossings, disjoint).
        "Z": 1, "N": 1, "n": 6,
        "word": [1] * 7 + [2] * 4 + [4] * 6 + [5] * 4 + [-4],
        "word_str": "σ₁⁷ σ₂⁴ ⊕ σ₄⁶ σ₅⁴ σ₄⁻¹",
        "m_MeV": 1875.61294,  # CODATA: m_d (deuteron mass)
    },
}

M_E_MEV = mp.mpf("0.51099895")


def evaluate_at_q0(expr: sp.Expr) -> mp.mpf:
    """Evaluate sympy expr at the substrate q_0 to 50 dps."""
    return mp.mpf(str(expr.subs(q, sp.sympify(str(Q_MP))).evalf(mp.mp.dps)))


def main() -> int:
    print("=" * 96)
    print(f"  Multi-atom axiomatic Markov-trace anchor (proton, neutron, deuteron)")
    print(f"  Uses markov_trace_recursive (axiom-only, repr-theory-free)")
    print("=" * 96)

    print(f"\n  Substrate parameter q_0 = {Q0_MP}")
    print(f"  m_e (CODATA)            = {M_E_MEV} MeV")

    results = {}
    for atom_name, info in ATOMS.items():
        print(f"\n  ── {atom_name} ──")
        print(f"    word: {info['word_str']}  ∈ H_{info['n']}")
        print(f"    Z={info['Z']}, N={info['N']}, A={info['Z']+info['N']}, m={info['m_MeV']} MeV")

        try:
            tr_sym = markov_trace_of_word(info["n"], info["word"])
        except Exception as exc:
            print(f"    ERROR computing tr_M: {type(exc).__name__}: {exc}")
            results[atom_name] = {"error": f"{type(exc).__name__}: {exc}"}
            continue

        # 50-dps numerical evaluation
        tr_num = evaluate_at_q0(tr_sym)
        abs_tr = abs(tr_num)

        # ρ_K^CODATA = (m_K / m_e) / |tr_M|
        m_over_me = mp.mpf(str(info["m_MeV"])) / M_E_MEV
        rho_K = m_over_me / abs_tr if abs_tr > 0 else mp.mpf("nan")

        # Symbolic short form
        sym_str = str(tr_sym)
        if len(sym_str) > 100:
            sym_str = sym_str[:97] + "..."

        print(f"    tr_M(symbolic):  {sym_str}")
        print(f"    tr_M(q_0):       {mp.nstr(tr_num, 12)}")
        print(f"    |tr_M(q_0)|:     {mp.nstr(abs_tr, 12)}")
        print(f"    m/m_e (CODATA):  {mp.nstr(m_over_me, 8)}")
        print(f"    ρ_K^CODATA:      {mp.nstr(rho_K, 6)}")

        results[atom_name] = {
            "Z": info["Z"],
            "N": info["N"],
            "n": info["n"],
            "word": info["word"],
            "word_str": info["word_str"],
            "m_MeV_codata": info["m_MeV"],
            "tr_M_symbolic": str(tr_sym),
            "tr_M_at_q0_50dps": str(tr_num),
            "abs_tr_M_at_q0_50dps": str(abs_tr),
            "m_over_m_e_codata": str(m_over_me),
            "rho_K_codata": str(rho_K),
        }

    # ── Disjoint-product check ──────────────────────────────────
    checks: dict = {}
    print(f"\n  Disjoint-product structural check (deuteron = proton ⊗ neutron):")
    if all(a in results and "tr_M_at_q0_50dps" in results[a]
           for a in ["proton", "neutron", "deuteron"]):
        tr_p = mp.mpf(results["proton"]["tr_M_at_q0_50dps"])
        tr_n = mp.mpf(results["neutron"]["tr_M_at_q0_50dps"])
        tr_d = mp.mpf(results["deuteron"]["tr_M_at_q0_50dps"])
        product = tr_p * tr_n
        relative = abs(tr_d - product) / abs(product) if abs(product) > 0 else mp.mpf("inf")
        print(f"    tr_M(proton)         = {mp.nstr(tr_p, 12)}")
        print(f"    tr_M(neutron)        = {mp.nstr(tr_n, 12)}")
        print(f"    tr_M(p) · tr_M(n)    = {mp.nstr(product, 12)}")
        print(f"    tr_M(deuteron)       = {mp.nstr(tr_d, 12)}")
        print(f"    relative |Δ|         = {mp.nstr(relative, 8)}")
        if relative < mp.mpf("1e-30"):
            print(f"    ✅ Disjoint-product property HOLDS (Δ < 1e-30, mpmath-exact).")
            disjoint_ok = True
        elif relative < mp.mpf("1e-9"):
            print(f"    ✓ Disjoint-product property holds within 1 ppb.")
            disjoint_ok = True
        else:
            print(f"    ✗ Mismatch — investigate axiom application on H_6.")
            disjoint_ok = False
        checks["disjoint_product"] = {
            "tr_p_times_tr_n_at_q0": str(product),
            "tr_d_at_q0": str(tr_d),
            "relative_error": str(relative),
            "matches_within_1ppb": bool(relative < mp.mpf("1e-9")),
            "matches_mpmath_exact": bool(relative < mp.mpf("1e-30")),
        }
    else:
        print(f"    (skipped — one or more atoms failed)")
        disjoint_ok = False

    # ── Cross-check against atomic-proton-full witness ──────────
    print(f"\n  Cross-check against markov_trace_atomic_proton_full witness:")
    atomic_proton_witness = HERE / "markov-trace-atomic-proton-full.witness.json"
    if atomic_proton_witness.exists() and "proton" in results:
        prior = json.loads(atomic_proton_witness.read_text())
        prior_tr = mp.mpf(str(prior.get("tr_M_proton_at_q0", "nan")))
        cur_tr = mp.mpf(results["proton"]["tr_M_at_q0_50dps"])
        # Float64 prior vs 50dps current — comparison is to ~12 sig figs
        diff = abs(cur_tr - prior_tr) / abs(prior_tr) if prior_tr != 0 else mp.mpf("inf")
        print(f"    atomic_proton_full:    {prior_tr}")
        print(f"    multi-atom recursive:  {mp.nstr(cur_tr, 12)}")
        print(f"    relative |Δ|:          {mp.nstr(diff, 6)}")
        if diff < mp.mpf("1e-12"):
            print(f"    ✅ Recursive matches Hecke-power expansion at float64 precision.")
            cross_check_ok = True
        else:
            print(f"    ⚠ discrepancy — recursive vs Hecke-power expansion diverged.")
            cross_check_ok = False
        checks["atomic_proton_full"] = {
            "prior_tr_M": str(prior_tr),
            "current_tr_M": str(cur_tr),
            "relative_error": str(diff),
            "matches_float64_precision": bool(diff < mp.mpf("1e-12")),
        }
    else:
        print(f"    (witness not found or proton not computed)")
        cross_check_ok = True  # don't block on missing witness

    # ── Witness emission ────────────────────────────────────────
    witness = {
        "computation": "markov-trace-axiomatic-multi-atom",
        "description": (
            "Multi-atom Markov-trace anchor using the axiomatic "
            "recursive reducer (markov_trace_recursive). Computes "
            "tr_M(β_K) for K ∈ {proton, neutron, deuteron} via "
            "Hecke quadratic + Markov axioms + cyclicity, no "
            "representation theory. Verifies the disjoint-product "
            "property tr_M(p ⊗ n) = tr_M(p) · tr_M(n) on the H_6 "
            "deuteron word, and cross-checks the proton against "
            "the prior Hecke-power expansion in "
            "markov_trace_atomic_proton_full.py."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:categorical-mass-markov",
            "prop:markov-trace-axiomatic-closed-form",
        ],
        "reference_scripts": [
            "folio-assistant/computations/markov_trace_recursive.py",
            "folio-assistant/computations/markov_trace_atomic_proton_full.py",
            "folio-assistant/computations/markov_trace_axiomatic_proton.py",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": str(Q0_MP),
        "m_e_MeV": str(M_E_MEV),
        "atoms": results,
        "checks": checks,
        "all_passed": disjoint_ok and cross_check_ok,
    }
    from witness_base import WitnessBuilder

    out = (WitnessBuilder

        .wrap_legacy("markov-trace-axiomatic-multi-atom", witness, script_path=__file__, engine="sympy")

        .save())
    print(f"\n  Witness: {out}")
    return 0 if (disjoint_ok and cross_check_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
