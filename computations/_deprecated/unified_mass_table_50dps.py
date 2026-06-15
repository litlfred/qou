#!/usr/bin/env python3
"""
Plan F aggregator — unified mass table at MPFR @ 50 dps.

Reads the six Plan-F per-term witnesses and aggregates per atom:

    𝔪(𝔥) = Term 1 + Term 2 + Term 3 + Term 4 + Term 5 + Term 6
         = |tr_M(T_w)| + Σ_i Φ_q(|V̂_i|) + z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)
           + τ(C_dim_q) + a_K·C_K + Σ_ℓ Res_{ζ_ℓ}

per [`thm:knot-mass-formula-unified`](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md).

For each atom 𝔥 in {electron, proton, neutron, D, T, ³He}, collects:
  - per-term contribution (dimensionless and in MeV)
  - total dimensionless 𝔪(𝔥)
  - mass ratio m(𝔥)/m_e = 𝔪(𝔥) / 𝔪(electron) — the
    mass_endomorphism convention that gives m_p/m_e ≈ 1870
  - absolute mass prediction m(𝔥) = m_e · ratio

Caveats:
  - Term 5 (a_K · C_K) requires per-atom C_K which is multi-block
    determined and not in the algebraic-only Plan F witnesses;
    here treated as a_K only with C_K = 1 placeholder.
  - The summation convention is "additive" per the six-term doc;
    the m_endomorphism convention specifically uses |Π V̂| + Σ Φ_q
    + Σ z² Φ_q (Term 1 is "descended" |Π V̂|, NOT tr_M). The aggregator
    reports both interpretations.
  - Heavier atoms (⁴He+, ⁶Li+) are not yet in the per-term witnesses;
    they need R5-full SDP and α-cluster Term-2/3 ports.

Output: `unified-mass-table-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf

mp.dps = 50

HERE = Path(__file__).parent
OUT = HERE / "unified-mass-table-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")

# Source witnesses
W_TERM1 = HERE / "atomic-tr-m-wenzl-bridge.witness.json"
W_TERMS_23_LIGHT = HERE / "terms-2-3-brane-tower-mpfr-50dps.witness.json"
W_TERMS_23_HEAVY = HERE / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"
W_TERM4 = HERE / "term4-frobenius-mpfr-50dps.witness.json"
W_TERM5 = HERE / "term5-chirality-mpfr-50dps.witness.json"
W_TERM6 = HERE / "term6-habiro-residue-mpfr-50dps.witness.json"

# Atom registry: (name, n_strands_native, n_strands_3A, A, ρ, chirality_pattern)
# n_strands_native is the SDP-witness braid's n_0; n_strands_3A is the 3A-strand
# convention's n. n_strands_used in Terms 2/3 depends on which witness emits the
# atom. Term 4 lookup key is n_strands_used.
ATOMS = {
    "electron":    {"n_native": 2, "n_3A": 2,  "A": None, "rho": 1, "chir": "1",         "n_t4": 2},
    "proton":      {"n_native": 3, "n_3A": 3,  "A": 1,    "rho": 1, "chir": "1",         "n_t4": 3},
    "neutron":     {"n_native": 3, "n_3A": 3,  "A": 1,    "rho": 1, "chir": "1",         "n_t4": 3},
    "deuteron-2H": {"n_native": 3, "n_3A": 6,  "A": 2,    "rho": 1, "chir": "1 - h²",    "n_t4": 6},
    "tritium-3H":  {"n_native": 5, "n_3A": 9,  "A": 3,    "rho": 2, "chir": "1 - h²",    "n_t4": 9},
    "helium3-3He": {"n_native": 3, "n_3A": 9,  "A": 3,    "rho": 2, "chir": "1 - h²",    "n_t4": 9},
}


def _load(p: Path) -> dict:
    return json.load(open(p))


def main() -> int:
    t1 = _load(W_TERM1)
    t23l = _load(W_TERMS_23_LIGHT)
    t23h = _load(W_TERMS_23_HEAVY)
    t4 = _load(W_TERM4)
    t5 = _load(W_TERM5)
    t6 = _load(W_TERM6)

    # Index Term 1 by atom name
    t1_by_atom = {r["atom"]: r for r in t1["results"]}

    # Index Terms 2,3 by particle/atom
    t23_by_atom = {r.get("particle") or r.get("atom"): r for r in t23l["results"]}
    for r in t23h["results"]:
        t23_by_atom[r["atom"]] = r
    # Map alternative keys
    if "deuteron-2H" not in t23_by_atom and "D" in t23_by_atom:
        t23_by_atom["deuteron-2H"] = t23_by_atom["D"]
    if "tritium-3H" not in t23_by_atom and "T" in t23_by_atom:
        t23_by_atom["tritium-3H"] = t23_by_atom["T"]
    if "helium3-3He" not in t23_by_atom and "3He" in t23_by_atom:
        t23_by_atom["helium3-3He"] = t23_by_atom["3He"]

    # Index Term 4 by n
    t4_by_n = {r["n"]: r for r in t4["results_by_n"]}

    # Index Term 5 by formula-string
    t5_by_factor = {r["factor"]: r for r in t5["chirality_factors"]}

    # Index Term 6 by atom/A
    t6_by_atom = {r["atom"]: r for r in t6["results_by_atom"]}

    rows = []
    for atom, meta in ATOMS.items():
        # Term 1
        if atom in t1_by_atom:
            term1_mev = mpf(t1_by_atom[atom]["term1_b_pred_mev"])
            tr_m = mpf(t1_by_atom[atom]["tr_M_mixed_precision"])
        else:
            term1_mev = mpf(0)
            tr_m = mpf(0)

        # Terms 2, 3
        t23_row = t23_by_atom.get(atom, {})
        term2_mev = mpf(t23_row.get("term2_b_pred_mev_50dps", "0"))
        term3_mev = mpf(t23_row.get("term3_b_pred_mev_50dps", "0"))
        term2_dimless = mpf(t23_row.get("term2_50dps", "0"))
        term3_dimless = mpf(t23_row.get("term3_50dps", "0"))

        # Term 4 — use n_t4 (the Hecke algebra dim where Term 4 lives)
        t4_row = t4_by_n.get(meta["n_t4"], {})
        term4_mev = mpf(t4_row.get("term4_b_pred_mev_50dps", "0"))
        term4_dimless = mpf(t4_row.get("total_at_q0_50dps", "0"))

        # Term 5 — algebraic factor (a_K only; C_K = 1 placeholder)
        t5_row = t5_by_factor.get(meta["chir"], {})
        a_K = mpf(t5_row.get("value_at_q0_50dps", "1"))

        # Term 6 — by A (uses 3A baryon level for Habiro)
        if meta["A"] is not None:
            t6_row = t6_by_atom.get(f"A={meta['A']}", {})
            term6_mev = mpf(t6_row.get("term6_b_pred_mev_50dps", "0"))
            term6_dimless = mpf(t6_row.get("global_sum_at_q0_50dps", "0"))
        else:
            term6_mev = mpf(0)
            term6_dimless = mpf(0)

        # Aggregate (dimensionless m_e units): 𝔪(𝔥)
        m_total_dimless = (
            mp.fabs(tr_m)        # Term 1: |tr_M|
            + term2_dimless       # Term 2
            + term3_dimless       # Term 3
            + term4_dimless       # Term 4
            + a_K                  # Term 5 (a_K · 1)
            + term6_dimless        # Term 6
        )
        m_total_mev = M_E_MEV * m_total_dimless

        rows.append({
            "atom": atom,
            "n_strands_native": meta["n_native"],
            "n_strands_3A": meta["n_3A"],
            "A": meta["A"],
            "rho_factor": meta["rho"],
            "term1": {
                "form": "|tr_M(T_w)|",
                "dimless_50dps": str(mp.fabs(tr_m)),
                "mev_50dps": str(term1_mev),
            },
            "term2": {
                "form": "Σ_i Φ_q(|V̂_i|)",
                "dimless_50dps": str(term2_dimless),
                "mev_50dps": str(term2_mev),
            },
            "term3": {
                "form": "z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)",
                "dimless_50dps": str(term3_dimless),
                "mev_50dps": str(term3_mev),
            },
            "term4": {
                "form": "τ(C_dim_q) = Σ_λ 1/dim_q(λ)",
                "dimless_50dps": str(term4_dimless),
                "mev_50dps": str(term4_mev),
                "n": meta["n_t4"],
            },
            "term5": {
                "form": meta["chir"],
                "a_K_50dps": str(a_K),
                "C_K_placeholder": 1,
            },
            "term6": {
                "form": "Σ_λ w_λ(q_0) (Schur-Weyl global sum)",
                "dimless_50dps": str(term6_dimless),
                "mev_50dps": str(term6_mev),
            },
            "total_dimensionless_50dps": str(m_total_dimless),
            "total_mev_50dps": str(m_total_mev),
        })

        print(f"\n  === {atom} ===")
        print(f"    Term 1 = {str(mp.fabs(tr_m)):>40} (|tr_M|, dimless)")
        print(f"    Term 2 = {str(term2_dimless):>40} (Φ_q tower single)")
        print(f"    Term 3 = {str(term3_dimless):>40} (Φ_q tower pair)")
        print(f"    Term 4 = {str(term4_dimless):>40} (Σ 1/dim_q at n={meta['n_t4']})")
        print(f"    a_K    = {str(a_K):>40} ({meta['chir']})")
        print(f"    Term 6 = {str(term6_dimless):>40} (Habiro at A={meta['A']})")
        print(f"    𝔪(𝔥)  = {str(m_total_dimless):>40}  (sum)")
        print(f"    M(MeV) = {str(m_total_mev):>40}  (= m_e · 𝔪)")

    # Mass-ratio convention: m(𝔥)/m_e = 𝔪(𝔥) / 𝔪(electron)
    electron_total = mpf(rows[0]["total_dimensionless_50dps"])
    print(f"\n  electron 𝔪 = {electron_total}")
    print(f"\n  Mass-ratio table (mass_endomorphism convention: m(𝔥)/m_e = 𝔪(𝔥)/𝔪(electron)):")
    print(f"    atom              ratio_predicted          ratio_codata        err")
    codata_ratios = {
        "proton":      mpf("938.27208816") / M_E_MEV,
        "neutron":     mpf("939.56542052") / M_E_MEV,
        "deuteron-2H": mpf("1875.61294257") / M_E_MEV,  # CODATA m_D
        "tritium-3H":  mpf("2808.92113665") / M_E_MEV,
        "helium3-3He": mpf("2808.39150726") / M_E_MEV,
    }
    for r in rows:
        atom = r["atom"]
        if atom == "electron":
            continue
        m_total = mpf(r["total_dimensionless_50dps"])
        ratio = m_total / electron_total
        codata = codata_ratios.get(atom)
        if codata:
            err = (ratio - codata) / codata * mpf(100)
            print(f"    {atom:<15}  {float(ratio):>18.6f}  {float(codata):>18.6f}  {float(err):+.4f}%")
            r["mass_ratio_over_me_predicted"] = str(ratio)
            r["mass_ratio_over_me_codata"] = str(codata)
            r["mass_err_pct"] = str(err)

    out = {
        "computation": "unified-mass-table-mpfr-50dps",
        "description":
            "Plan F aggregator — unified mass table at MPFR @ 50 dps. "
            "Sums all six terms of thm:knot-mass-formula-unified per "
            "atom for {electron, p, n, D, T, ³He}. The 'sum convention' "
            "follows mass_endomorphism.py: m(𝔥)/m_e = 𝔪(𝔥) / 𝔪(electron). "
            "Reports both per-term breakdowns (50-dps) and absolute "
            "mass-ratio predictions vs CODATA.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "m_e_mev_50dps": str(M_E_MEV),
        "sum_convention":
            "𝔪(𝔥) = |tr_M| + Σ Φ_q(|V̂|) + z² Σ Φ_q(|V̂V̂|) + Σ 1/dim_q "
            "+ a_K + Σ_λ w_λ; mass ratio is 𝔪(𝔥)/𝔪(electron) per "
            "mass_endomorphism convention.",
        "atoms": rows,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
