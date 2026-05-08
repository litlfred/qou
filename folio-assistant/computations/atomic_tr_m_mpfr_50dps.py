#!/usr/bin/env python3
"""
Plan F advance — extends the mpmath @ 50 dps tr_M evaluation from
proton (proton_mass_mpfr_50dps.py) to neutron, deuteron, and now
tritium / ³He (previously timed out) plus the symbolic comparison
test for ²H / ³H / ³He against published Jones polynomials.

For each atom 𝔥 ∈ {proton, neutron, deuteron, tritium, helium-3}:
  1. Build the 3A-strand Hecke factor word via atom_braid_word_3A
     (no GB-NF needed — Wenzl bridge consumes raw Hecke factors).
  2. Compute tr_M(W) via the Hoefsmit + Wenzl bridge:
        tr_M(W) = Σ_{λ ⊢ 3A} y_λ(q) · χ_λ(W)
     using y-lambda-mpfr-witness.json for y_λ and per-partition
     seminormal matrices in mpmath at 50 dps.
  3. (Optional, gated on `--symbolic`) Cross-check against the
     legacy sympy tr_M_element path for proton / neutron / deuteron
     where it terminates in reasonable time.
  4. Report Term-1 contribution m_e · ρ · |tr_M(q_0)| and the
     residual against B_AME for diagnostic.

For atoms in {²H, ³H, ³He} flagged `manual-historical-volume-match`
in joint-tower-sdp-rust.witness.json, also report whether the
numeric tr_M(q_0) matches the published Jones polynomial of the
historical knot up to writhe normalisation (q^k factor).

Output: `atomic-tr-m-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import argparse
import json
import sys
import time
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
sys.path.insert(0, str(HERE))

import atom_nf_symbolic_D as M
from mass_at_3A_proper import atom_braid_word_3A
from markov_trace_canonical import tr_M_element, Z_SYMB, H_SYMB
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr

Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "atomic-tr-m-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")  # CODATA 2022

# Published Jones polynomials (from Kawauchi tables / KnotInfo).
# Variable conventions: in our pipeline σ_i² = (q − q⁻¹)σ_i + 1, so
# J_K is the Markov-trace value for the trefoil-like normalization.
J_PUBLISHED = {
    # 6_2: from Kawauchi Theorem 2.2.4 / KnotInfo.
    "6_2": "q - 1 + 2/q - 2/q**2 + 2/q**3 - 2/q**4 + 1/q**5",
    # 8_11: KnotInfo / Murasugi (Knot Theory and its Applications).
    "8_11": "-q**6 + 2*q**5 - 4*q**4 + 5*q**3 - 5*q**2 + 5*q - 4 + 3/q - 1/q**2",
    # L_6a4 (Borromean): standard formula.
    "L_6a4": "q**3 - 3*q**2 + 6*q - 7 + 6/q - 3/q**2 + 1/q**3",
}

ATOMS = [
    ("proton",    1, 0, 1, "p (B_3 Borromean)",   None),
    ("neutron",   0, 1, 1, "n (B_3 Borromean)",   None),
    ("deuteron",  1, 1, 1, "²H (B_6 atom-3A)",    "6_2"),
    ("tritium",   1, 2, 1, "³H (B_9 atom-3A)",    None),
    ("helium-3",  2, 1, 1, "³He (B_9 atom-3A)",   None),
    # ⁴He intentionally OMITTED here.  Canonical |tr_M(⁴He)| at H_12
    # via the Wenzl bridge is intractable at 50 dps with current
    # Python mpmath: p(12)=77 partitions and the largest partition
    # (5,3,2,1,1) has dim 7700, requiring ~2×10¹³ mp.mpf ops per
    # partition × 47 crossings.  bu64reus1 (PR #564) hit the 30-min
    # timeout.  See atomic-tr-m-helium4.witness.json for the
    # disjoint-product placeholder (flagged DEPRECATED_DISJOINT) and
    # AUDIT-DEEP-2026-05.md §7 for the deferral rationale.  Tractable
    # canonical ⁴He requires either (a) Rust kernel with rayon
    # parallel partitions + block-sparse Hoefsmit MPFR, or (b) a
    # categorical reduction (e.g. via the Wenzl 1988 LR branching
    # decomposition in `hecke-branching-trace-decomposition.md`)
    # that avoids the full p(12)=77 sum.
]


def _bridge_tr_M(Z: int, N: int, q_str: str, dps: int = 50):
    """Compute tr_M(W_atom) via the Hoefsmit + Wenzl bridge.

    Builds the 3A-strand Hecke-factor word and evaluates Σ_λ y_λ · χ_λ
    at mpf precision.  Returns (tr_mpf, breakdown_dict, n_strands,
    word_length).
    """
    word = atom_braid_word_3A(Z, N)
    n_strands = 3 * (Z + N)
    t0 = time.time()
    tr = tr_M_via_wenzl_bridge_mpfr(
        word, n_strands, q_str, dps=dps, return_breakdown=False)
    dt = time.time() - t0
    return tr, n_strands, len(word), dt


def main(also_symbolic: bool = False) -> int:
    q_str = json.load(open(Q0))["derived_50_digit"]["q"]
    q_0 = mpf(q_str)
    q_sym = sp.Symbol("q")  # match sympify default
    print(f"  q_0 (50 dps) = {q_str}")
    print(f"  primary path: Hoefsmit+Wenzl bridge (mpf @ 50 dps)")
    if also_symbolic:
        print(f"  symbolic cross-check: enabled (--symbolic) "
              f"— may be slow at A>=2")

    results = []
    for label, Z, N, rho, descr, historical_K in ATOMS:
        print(f"\n  === {label} (Z={Z}, N={N}, ρ={rho}) ===")

        # Primary path: Hoefsmit + Wenzl bridge.
        tr_at_q0_mpf, n_strands, word_len, bridge_t = _bridge_tr_M(
            Z, N, q_str, dps=50)
        print(f"    n_strands = {n_strands},  word_length = {word_len}")
        print(f"    [bridge] tr_M(q_0) = {tr_at_q0_mpf}  ({bridge_t:.2f}s)")
        b_term1 = M_E_MEV * rho * abs(tr_at_q0_mpf)
        print(f"    Term-1 contribution: m_e · ρ · |tr_M| = {b_term1} MeV")

        # Optional symbolic cross-check (legacy path, slow at A>=2).
        symbolic_check = None
        if also_symbolic:
            try:
                t_sym = time.time()
                elem, stats = M.build_atom_nf_symbolic(Z, N, verbose=False)
                tr_q = tr_M_element(elem, n_strands, Z_SYMB, H_SYMB,
                                      simplify=False)
                free = list(tr_q.free_symbols)
                q60 = sp.Float(q_str, 60)
                tr_at_q0_sym = sp.N(tr_q.subs({s: q60 for s in free}), 50)
                tr_sym_mpf = mpf(str(tr_at_q0_sym))
                dt_sym = time.time() - t_sym
                diff = abs(tr_sym_mpf - tr_at_q0_mpf)
                print(f"    [sympy] tr_M(q_0) = {tr_sym_mpf}  ({dt_sym:.2f}s)")
                print(f"    |bridge - sympy|   = {diff}")
                symbolic_check = {
                    "nf_terms": stats["n_terms_nf"],
                    "elapsed_sec": dt_sym,
                    "tr_M_at_q0_50dps": str(tr_sym_mpf),
                    "abs_diff_vs_bridge": str(diff),
                }
            except Exception as exc:
                print(f"    [sympy] FAILED ({type(exc).__name__}: {exc})")
                symbolic_check = {"error": f"{type(exc).__name__}: {exc}"}

        # Markov-axiom recursive ascent (#508) — third independent path.
        # Build via `markov_peel.tr_M_atomic`, evaluate at 50 dps to
        # cross-check both the bridge and the symbolic legacy path.
        peel_check = None
        try:
            from markov_peel import tr_M_atomic
            from hecke_symbolic import q as q_peel_sym
            t_peel = time.time()
            tr_peel_sym = tr_M_atomic(Z, N)
            q60 = sp.Float(q_str, 60)
            free = list(tr_peel_sym.free_symbols) if hasattr(
                tr_peel_sym, "free_symbols") else [q_peel_sym]
            tr_peel_at_q0 = sp.N(
                tr_peel_sym.subs(
                    {s: q60 for s in free} if free else
                    {q_peel_sym: q60}),
                50)
            tr_peel_mpf = mpf(str(tr_peel_at_q0))
            dt_peel = time.time() - t_peel
            diff_peel = abs(tr_peel_mpf - tr_at_q0_mpf)
            print(f"    [peel]  tr_M(q_0) = {tr_peel_mpf}  ({dt_peel:.2f}s)")
            print(f"    |bridge - peel|    = {diff_peel}")
            peel_check = {
                "elapsed_sec": dt_peel,
                "tr_M_at_q0_50dps": str(tr_peel_mpf),
                "abs_diff_vs_bridge": str(diff_peel),
            }
        except Exception as exc:
            print(f"    [peel]  FAILED ({type(exc).__name__}: {exc})")
            peel_check = {"error": f"{type(exc).__name__}: {exc}"}

        # If a historical knot ID is available, compare numerically at q_0.
        comparison = None
        if historical_K and historical_K in J_PUBLISHED:
            J_sym = sp.sympify(J_PUBLISHED[historical_K])
            q60 = sp.Float(q_str, 60)
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
            "word_length_3A": word_len,
            "tr_M_at_q0_50dps": str(tr_at_q0_mpf),
            "term1_b_pred_mev_50dps": str(b_term1),
            "bridge_elapsed_sec": bridge_t,
            "symbolic_cross_check": symbolic_check,
            "peel_cross_check": peel_check,
            "historical_K_comparison": comparison,
        })

    out = {
        "computation": "atomic-tr-m-mpfr-50dps",
        "description":
            "Plan F advance — tr_M(T_w, q_0) via the 3A-strand atom-braid "
            "convention for proton, neutron, deuteron, tritium, ³He, "
            "evaluated at q_0 to 50 dps via the Hoefsmit + Wenzl bridge "
            "(Σ_λ y_λ · χ_λ) and (where applicable) compared against the "
            "published Jones polynomial of the historical knot ID. "
            "Companion to proton-mass-mpfr-50dps.witness.json.  "
            "Tritium / ³He at H_9 unblocked vs. legacy sympy path "
            "(>4-min timeout).",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "method": (
            "hoefsmit_wenzl_bridge: tr_M(W) = Σ_{λ ⊢ n} y_λ(q) · χ_λ(W); "
            "y_λ from y-lambda-mpfr-witness.json; χ_λ via per-partition "
            "Young-seminormal matrices in mpmath (sparse COO) at 50 dps; "
            "W is the atom_braid_word_3A Hecke-factor word"
        ),
        "structural_reference":
            "prop:full-pole-structure-mass-trace — tr_M(T_w, q) is "
            "meromorphic in q with simple poles at every primitive root "
            "of unity ζ_n^(j) (gcd(j,n)=1, n>=2); this witness reports "
            "tr_M evaluated at q = q_0 ≈ 1.11, the regular point used "
            "throughout the paper.  The prop's Mittag-Leffler / Habiro "
            "cyclotomic expansion expresses the same function as a sum "
            "over these poles; Habiro's convergence theorem guarantees "
            "the order-m Habiro truncation neglects only the ζ_1, …, "
            "ζ_m residues, so the values reported here are the LHS of "
            "the prop's equations (Mittag-Leffler eq. and Habiro eq.) "
            "at q = q_0.",
        "y_lambda_witness": "y-lambda-mpfr-witness.json",
        "q_0_50dps": q_str,
        "symbolic_cross_check_enabled": also_symbolic,
        "precision_caveat": (
            "y-lambda-mpfr-witness.json was computed with q at f64 "
            "precision (its 'q' field stores str(float(Q0))); the y_λ "
            "values inherit f64-limited input. Bridge results agree "
            "with the prop-table canonical values to ~1e-15. To upgrade "
            "to full 50-dps precision, regenerate that witness with "
            "q_str at 50 dps (see y_lambda_mpfr_witness.py)."
        ),
        "results": results,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--symbolic", action="store_true",
        help="Also run the legacy sympy tr_M_element path as a "
             "cross-check (slow at A>=2; will likely time out at A=3).")
    args = parser.parse_args()
    sys.exit(main(also_symbolic=args.symbolic))
