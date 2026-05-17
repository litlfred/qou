"""
probe_rho_K_isotope_ratio_tautology.py — is "ρ_K ratios explained
by |tr_M| ratios" a substantive identity or a tautology?

Per owner: "ρ_K isotope RATIOS (p/n, T/³He) ARE naturally explained
by |tr_M(β_K)| --> provable?"

This probe walks the algebra cleanly.

## The candidate identity

For any two atoms A, B:

    ρ_K(A) / ρ_K(B)  =  (M_A_CODATA / M_B_CODATA) · (|tr_M(B)| / |tr_M(A)|)   (★)

## The definition of ρ_K (atomic-mass-gb-nf.md line 50-54)

    ρ_K(X) := M_X_CODATA / (m_e · |tr_M(NF_GS(β_X))|)

Substituting both sides of (★):

    LHS = ρ_K(A) / ρ_K(B)
        = [M_A / (m_e · |tr_M(A)|)] / [M_B / (m_e · |tr_M(B)|)]
        = (M_A / M_B) · (|tr_M(B)| / |tr_M(A)|)
        = RHS

So (★) is a **tautology** — it follows ALGEBRAICALLY from the
definition of ρ_K.  This is *not* a substantive prediction.

## What would be a substantive prediction

(★) becomes substantive if EITHER side of the ratio is derived
INDEPENDENTLY:

  (P1) Derive |tr_M(β_X)| from substrate (q_0 + β_X), then use (★)
       to predict mass RATIOS M_A / M_B from substrate-derived
       |tr_M| ratios AND a single anchor (one M known).

  (P2) Derive M_X_CODATA from substrate (the open problem), making
       both sides independently substrate-derived.

(P1) is **partially possible** — |tr_M| CAN be computed from
substrate per Wenzl 1988 Markov multiplicativity.  But you still
need an anchor M (e.g. m_p_CODATA or m_e), which the framework
takes as CAL-1.

(P2) is the open ρ_K problem (paper's own line 71).

## This probe

Computes (★) empirically per atom pair, verifies the tautological
identity holds, and explains what would be required to make the
statement substantive.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

# Data from atomic-mass-gb-nf.md table line 60-67
ATOMS = {
    "p":   {"M_CODATA": mpf("938.272"),  "tr_M": mpf("1.0653"), "rho_K": mpf("1723.6")},
    "n":   {"M_CODATA": mpf("939.565"),  "tr_M": mpf("0.9232"), "rho_K": mpf("1991.6")},
    "D":   {"M_CODATA": mpf("1875.613"), "tr_M": mpf("0.3883"), "rho_K": mpf("9453.0")},
    "T":   {"M_CODATA": mpf("2808.921"), "tr_M": mpf("0.1041"), "rho_K": mpf("52828.5")},
    "He3": {"M_CODATA": mpf("2808.392"), "tr_M": mpf("0.2065"), "rho_K": mpf("26609.2")},
}
M_E = mpf("0.51099895069")


def main() -> int:
    print("=" * 78)
    print("  ρ_K isotope ratios — substantive or tautology?")
    print("=" * 78)
    print()

    # Step 1: verify the tautological identity per atom
    print("  Step 1: Verify ρ_K = M_CODATA / (m_e · |tr_M|) per atom")
    print("  " + "-" * 66)
    print(f"  {'atom':6} {'paper ρ_K':>12} {'M/(m_e·tr_M)':>16} {'ratio':>10}")
    for name, d in ATOMS.items():
        rk_pred = d["M_CODATA"] / (M_E * d["tr_M"])
        ratio = rk_pred / d["rho_K"]
        print(f"  {name:6} {mp.nstr(d['rho_K'], 8):>12} "
              f"{mp.nstr(rk_pred, 10):>16} {mp.nstr(ratio, 8):>10}")
    print()
    print("  → All ratios ≈ 1.000 by definition of ρ_K.  This is the")
    print("    paper's own definition (atomic-mass-gb-nf.md line 50-54).")
    print()

    # Step 2: verify (★) — the "explained by |tr_M|" claim
    pairs = [("p", "n"), ("T", "He3"), ("D", "p"), ("T", "D")]
    print("  Step 2: Verify (★): ρ_K(A)/ρ_K(B) = (M_A/M_B) · (|tr_M(B)|/|tr_M(A)|)")
    print("  " + "-" * 66)
    print(f"  {'pair':10} {'LHS ρ_K ratio':>16} {'RHS prediction':>20} {'ratio':>10}")
    results = []
    for A, B in pairs:
        a, b = ATOMS[A], ATOMS[B]
        lhs = a["rho_K"] / b["rho_K"]
        rhs = (a["M_CODATA"] / b["M_CODATA"]) * (b["tr_M"] / a["tr_M"])
        ratio = lhs / rhs
        print(f"  {A}/{B:6}    {mp.nstr(lhs, 10):>16} {mp.nstr(rhs, 14):>20} {mp.nstr(ratio, 8):>10}")
        results.append({"pair": f"{A}/{B}", "lhs": str(lhs), "rhs": str(rhs),
                       "ratio_lhs_to_rhs": str(ratio)})
    print()
    print("  → All ratios ≈ 1.000 BY ALGEBRA.  (★) is a tautology.")
    print()

    # Step 3: explain the substantive question
    print("  Step 3: What would make (★) substantive?")
    print("  " + "-" * 66)
    print("  (★) becomes a substantive PREDICTION if either side of the")
    print("  ratio is derived INDEPENDENTLY from substrate, not as the")
    print("  definition of ρ_K.")
    print()
    print("  Two paths to make (★) substantive:")
    print()
    print("    (P1) |tr_M(β_X)| from substrate + one mass anchor.")
    print("         Per Wenzl 1988 Markov multiplicativity, |tr_M| IS")
    print("         computable from substrate (q_0 + braid β_X).  Given")
    print("         m_p_CODATA as anchor, (★) PREDICTS m_n / m_p")
    print("         from substrate-computed |tr_M(n)| / |tr_M(p)|:")
    print()

    # Demonstrate P1
    tr_M_p = ATOMS["p"]["tr_M"]
    tr_M_n = ATOMS["n"]["tr_M"]
    m_p_codata = ATOMS["p"]["M_CODATA"]
    m_n_codata = ATOMS["n"]["M_CODATA"]
    # Using ρ_K(p)·|tr_M(p)| = m_p/m_e and ρ_K(n)·|tr_M(n)| = m_n/m_e:
    # m_n / m_p = [ρ_K(n)·|tr_M(n)|] / [ρ_K(p)·|tr_M(p)|]
    # If we ASSUME ρ_K(n) = ρ_K(p) (i.e. categorical density is
    # particle-universal at the nucleon level), then:
    m_n_from_tr_M_p1 = m_p_codata * (tr_M_p / tr_M_n)
    p1_residual = (m_n_from_tr_M_p1 - m_n_codata) / m_n_codata * 100
    print(f"    Naive prediction (assuming ρ_K(p) = ρ_K(n)):")
    print(f"      m_n_pred = m_p · |tr_M(p)| / |tr_M(n)|")
    print(f"               = {m_p_codata} · {tr_M_p}/{tr_M_n}")
    print(f"               = {mp.nstr(m_n_from_tr_M_p1, 10)} MeV")
    print(f"      vs CODATA m_n = {m_n_codata} MeV")
    print(f"      residual: {mp.nstr(p1_residual, 8)} % "
          f"({mp.nstr(p1_residual*10000, 8)} ppm)")
    print()
    print("    → Off by 15.4 % because ρ_K(p) ≠ ρ_K(n) (1723.6 vs 1991.6,")
    print("      ratio 0.8654).  The framework REQUIRES per-particle ρ_K.")
    print()
    print("    (P2) Derive M_X from substrate alone (the open ρ_K problem).")
    print("         If solved, both sides of (★) are independent;")
    print("         (★) becomes a genuine framework consistency check.")
    print()
    print("    Status: P1 fails by 15% (ρ_K is not particle-universal).")
    print("            P2 is the paper's acknowledged-open problem.")
    print()
    print("  CONCLUSION: My earlier statement \"ρ_K isotope RATIOS are")
    print("  naturally explained by |tr_M(β_K)| differences\" is a")
    print("  TAUTOLOGY of the ρ_K definition (line 50-54).  It is NOT")
    print("  a substantive prediction of isotope mass ratios from")
    print("  substrate.  Walking that back.")

    # Witness
    w = (WitnessBuilder("probe-rho-K-isotope-ratio-tautology", engine="python+mpmath")
         .set_description("Test substantiveness of ρ_K isotope-ratio identity"))
    w.add_data("identity_check_per_atom", [
        {"atom": name,
         "paper_rho_K": str(d["rho_K"]),
         "computed_M_over_m_e_times_tr_M": str(d["M_CODATA"] / (M_E * d["tr_M"])),
         "ratio": str((d["M_CODATA"] / (M_E * d["tr_M"])) / d["rho_K"])}
        for name, d in ATOMS.items()
    ])
    w.add_data("pair_ratio_check_star_identity", results)
    w.add_data("p1_substantive_attempt", {
        "naive_prediction_m_n_from_tr_M_ratio": str(m_n_from_tr_M_p1),
        "codata_m_n": str(m_n_codata),
        "residual_pct": str(p1_residual),
        "verdict": "FAILS by 15.4% — ρ_K is not particle-universal",
    })
    w.add_data("verdict",
               "TAUTOLOGY by definition of ρ_K (atomic-mass-gb-nf line 50-54). "
               "Earlier session statement 'ρ_K isotope ratios are naturally "
               "explained by |tr_M|' is NOT a substantive prediction — it "
               "follows trivially from algebra.  Walking back.")
    w.add_assertion("identity_holds_per_atom",
                    computed=1.0 if all(
                        mp.fabs(d["M_CODATA"] / (M_E * d["tr_M"]) - d["rho_K"]) /
                        d["rho_K"] < mpf("0.001") for d in ATOMS.values()
                    ) else 0.0,
                    expected=1.0)
    w.add_assertion("p1_naive_prediction_fails",
                    computed=1.0 if mp.fabs(p1_residual) > 5 else 0.0,
                    expected=1.0)
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
