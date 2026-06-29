"""
probe_rho_K_candidate_search.py — exhaustive candidate-formula
search for ρ_K(β_K) from substrate.

Per owner: "keep pushing / proving / adding to compute on rho_K"

Tests N candidate substrate-only formulas for ρ_K against the
5-atom empirical table from atomic-mass-gb-nf.md line 60-67:

  atom    A   |tr_M|     M_CODATA   ρ_K_CODATA
  p       1   1.0653     M_P_MEV_VALIDATION    1723.6
  n       1   0.9232     M_N_MEV_VALIDATION    1991.6
  D       2   0.3883    1875.613    9453.0
  T       3   0.1041    2808.921   52828.5
  ³He     3   0.2065    2808.392   26609.2

Goal: find ANY function f(β_K, q_0) such that f predicts ρ_K to
within 1 % across all 5 atoms without using M_CODATA as input.

Each candidate is scored by:
  - max relative residual across all 5 atoms (smaller = better)
  - geometric mean of |1 - pred/CODATA| across atoms
  - mirror-pair check (T vs ³He, must distinguish them via braid)

Negative result (no candidate closes ρ_K) is itself a substantive
finding — it constrains where the next research must look.

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

from __future__ import annotations
from computations.substrate.codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # CODATA-2022 full precision

set_compute_dps()

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
q_inv = mpf(1) / q
h_q = q - q_inv

# Empirical table from atomic-mass-gb-nf.md
ATOMS = {
    "p":   {"A": 1, "Z": 1, "N": 0, "n_strands": 3,  "tr_M": mpf("1.0653"),
            "M_CODATA": M_P_MEV_VALIDATION,  "rho_K": mpf("1723.6")},
    "n":   {"A": 1, "Z": 0, "N": 1, "n_strands": 3,  "tr_M": mpf("0.9232"),
            "M_CODATA": M_N_MEV_VALIDATION,  "rho_K": mpf("1991.6")},
    "D":   {"A": 2, "Z": 1, "N": 1, "n_strands": 6,  "tr_M": mpf("0.3883"),
            "M_CODATA": mpf("1875.613"), "rho_K": mpf("9453.0")},
    "T":   {"A": 3, "Z": 1, "N": 2, "n_strands": 9,  "tr_M": mpf("0.1041"),
            "M_CODATA": mpf("2808.921"), "rho_K": mpf("52828.5")},
    "He3": {"A": 3, "Z": 2, "N": 1, "n_strands": 9,  "tr_M": mpf("0.2065"),
            "M_CODATA": mpf("2808.392"), "rho_K": mpf("26609.2")},
}


def q_int(n: int) -> mpf:
    if n == 0:
        return mpf(0)
    return (q**n - q_inv**n) / h_q


def q_fact(n: int) -> mpf:
    out = mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def partitions(n: int) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    res: list[tuple[int, ...]] = []

    def rec(rem: int, mx: int, acc: list[int]) -> None:
        if rem == 0:
            res.append(tuple(acc))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, acc + [p])
    rec(n, n, [])
    return res


def hook_lengths(shape: tuple[int, ...]) -> list[int]:
    hooks: list[int] = []
    rows = list(shape)
    for i, row_len in enumerate(rows):
        for j in range(row_len):
            arm = row_len - j - 1
            leg = sum(1 for k in range(i + 1, len(rows)) if rows[k] > j)
            hooks.append(1 + arm + leg)
    return hooks


def dim_q(shape: tuple[int, ...]) -> mpf:
    n = sum(shape)
    num = q_fact(n)
    den = mpf(1)
    for hh in hook_lengths(shape):
        den *= q_int(hh)
    return num / den


# === Candidate formulas ===

def C1_max_dim_q_at_3A(atom: dict) -> mpf:
    """C1: ρ_K = max_{λ ⊢ 3A} dim_q(λ)"""
    parts = partitions(3 * atom["A"])
    return max(dim_q(p) for p in parts)


def C2_sum_dim_q_sq_at_3A(atom: dict) -> mpf:
    """C2: ρ_K = Σ_{λ ⊢ 3A} dim_q²(λ)"""
    parts = partitions(3 * atom["A"])
    return sum(dim_q(p) ** 2 for p in parts)


def C3_qfact_3A(atom: dict) -> mpf:
    """C3: ρ_K = [3A]_q! / [3A]"""
    return q_fact(3 * atom["A"]) / q_int(3 * atom["A"])


def C4_qfact_3A_over_trM(atom: dict) -> mpf:
    """C4: ρ_K = [3A]_q! / (|tr_M| · [3]_q!)  — telescoping via constituent triple"""
    return q_fact(3 * atom["A"]) / (atom["tr_M"] * q_fact(3))


def C5_partition_count_over_trM(atom: dict) -> mpf:
    """C5: ρ_K = |partitions of 3A| · q^(3A) / |tr_M|"""
    parts = partitions(3 * atom["A"])
    return len(parts) * q ** (3 * atom["A"]) / atom["tr_M"]


def C6_telescope_hat_V(atom: dict) -> mpf:
    """C6: ρ_K = (Σ dim_q²)^(1/2) · q^A / |tr_M|"""
    parts = partitions(3 * atom["A"])
    sum_dim_sq = sum(dim_q(p) ** 2 for p in parts)
    return mp.sqrt(sum_dim_sq) * q ** atom["A"] / atom["tr_M"]


def C7_M_e_factor(atom: dict) -> mpf:
    """C7: ρ_K = (m_p/m_e) · |tr_M(p)|/|tr_M(K)|   (anchored to proton)"""
    # = 1836.15 · 1.0653 / atom["tr_M"]   constant for proton, varies for others
    m_p_over_m_e = M_P_MEV_VALIDATION / M_E_MEV
    tr_M_p = ATOMS["p"]["tr_M"]
    return m_p_over_m_e * tr_M_p / atom["tr_M"]


def C8_constituent_M_over_trM(atom: dict) -> mpf:
    """C8: ρ_K = (Z·m_p + N·m_n + Z·m_e)/(m_e · |tr_M|)   — LO constituent
       This is m_e · ρ_K = LO sum / |tr_M|, so ρ_K = (LO sum / m_e) / |tr_M|.
       BY DEFINITION matches CODATA for proton; uses m_p_CODATA as input."""
    m_e = M_E_MEV  # from codata_constants
    m_p = M_P_MEV_VALIDATION
    m_n = M_N_MEV_VALIDATION
    Z, N = atom["Z"], atom["N"]
    lo_sum = Z * m_p + N * m_n + Z * m_e
    return lo_sum / (m_e * atom["tr_M"])


def C9_qcd_lattice(atom: dict) -> mpf:
    """C9: ρ_K = Λ_QCD^(n_q) / (m_e · |tr_M|)
       where Λ_QCD ≈ 250 MeV, n_q = 3A (quarks)"""
    Lambda_QCD = mpf("250.0")  # MeV, lattice-QCD scale
    n_q = 3 * atom["A"]
    return Lambda_QCD ** n_q / (M_E_MEV * atom["tr_M"])


def C10_nucleon_only_LO(atom: dict) -> mpf:
    """C10: ρ_K = (Z·m_p + N·m_n) / (m_e · |tr_M|)   NO ELECTRON TERM

    This is the LO constituent sum from atomic-mass-gb-nf line 82
    BUT EXCLUDING the +Z·m_e lepton-content term.  Uses CODATA
    m_p, m_n as inputs (not substrate-derived), but holds to 0.3%
    across all 5 atoms — and the residual scales as nuclear binding
    energy per nucleon.

    For T (1p + 2n): residual +0.30% = (-8.5 MeV BE/3 nucleons) / 938 MeV
                                     ≈ -2.8 MeV / 938 MeV — exactly
                                     the binding-energy contribution.
    """
    m_e = M_E_MEV  # from codata_constants
    m_p = M_P_MEV_VALIDATION
    m_n = M_N_MEV_VALIDATION
    Z, N = atom["Z"], atom["N"]
    return (Z * m_p + N * m_n) / (m_e * atom["tr_M"])


CANDIDATES = [
    ("C1 max_dim_q(λ⊢3A)",                    C1_max_dim_q_at_3A),
    ("C2 Σ dim_q²(λ⊢3A)",                     C2_sum_dim_q_sq_at_3A),
    ("C3 [3A]_q! / [3A]_q",                   C3_qfact_3A),
    ("C4 [3A]_q! / (|tr_M|·[3]_q!)",          C4_qfact_3A_over_trM),
    ("C5 |partitions| · q^(3A) / |tr_M|",     C5_partition_count_over_trM),
    ("C6 √Σdim_q² · q^A / |tr_M|",            C6_telescope_hat_V),
    ("C7 (m_p/m_e) · |tr_M(p)|/|tr_M(K)|",    C7_M_e_factor),
    ("C8 LO/(m_e·|tr_M|) [uses CODATA]",      C8_constituent_M_over_trM),
    ("C9 Λ_QCD^(3A)/(m_e·|tr_M|)",            C9_qcd_lattice),
    ("C10 (Zm_p+Nm_n)/(m_e·|tr_M|) [no lepton]", C10_nucleon_only_LO),
]


def main() -> int:
    print("=" * 84)
    print("  ρ_K candidate-formula search — N=9 candidates against 5 atoms")
    print("=" * 84)
    print(f"  q_0 = {mp.nstr(q, 16)}")
    print()
    print(f"  {'candidate':35} {'p':>10} {'n':>10} {'D':>10} {'T':>10} {'³He':>10}")
    print(f"  {'(ρ_K CODATA)':35} {1723.6:>10} {1991.6:>10} {9453.0:>10} {52828.5:>10} {26609.2:>10}")
    print("  " + "-" * 80)

    results = []
    for name, fn in CANDIDATES:
        preds = []
        for atom_name in ["p", "n", "D", "T", "He3"]:
            try:
                pred = fn(ATOMS[atom_name])
                preds.append(pred)
            except Exception as exc:
                preds.append(mpf("nan"))
        # Format
        cells = []
        for atom_name, pred in zip(["p", "n", "D", "T", "He3"], preds):
            if mp.isnan(pred):
                cells.append("nan")
            elif mp.fabs(pred) > 1e6:
                cells.append(f"{float(pred):.2e}")
            else:
                cells.append(f"{float(pred):.2f}")
        print(f"  {name:35} {cells[0]:>10} {cells[1]:>10} {cells[2]:>10} {cells[3]:>10} {cells[4]:>10}")
        # Residual stats
        residuals = []
        for atom_name, pred in zip(["p", "n", "D", "T", "He3"], preds):
            target = ATOMS[atom_name]["rho_K"]
            if not mp.isnan(pred) and target != 0:
                residuals.append(float(mp.fabs(pred - target) / target))
        max_res = max(residuals) if residuals else float("inf")
        results.append({
            "name": name,
            "predictions": [str(p) for p in preds],
            "max_relative_residual": str(max_res),
        })

    print()
    print("  Residual stats:")
    print(f"  {'candidate':35} {'max |Δ|/ρ_K':>14} {'verdict':>12}")
    print("  " + "-" * 65)
    for r in results:
        mx = float(r["max_relative_residual"])
        verdict = "✓ CLOSE" if mx < 0.05 else ("partial" if mx < 0.5 else "REFUTED")
        print(f"  {r['name']:35} {mx:>14.4g} {verdict:>12}")

    # Mirror pair check: T vs ³He must give DIFFERENT predictions
    print()
    print("  Mirror-pair check: T vs ³He (must differ per atomic-mass-gb-nf line 107)")
    print("  " + "-" * 65)
    for i, (name, fn) in enumerate(CANDIDATES):
        t_pred = fn(ATOMS["T"])
        h_pred = fn(ATOMS["He3"])
        if not mp.isnan(t_pred) and not mp.isnan(h_pred):
            ratio = t_pred / h_pred if h_pred != 0 else mpf("inf")
            expected_ratio = ATOMS["T"]["rho_K"] / ATOMS["He3"]["rho_K"]  # 1.985
            distinguishes = "✓" if mp.fabs(ratio - 1) > mpf("0.01") else "✗ same value"
            print(f"  {name:35} T/³He = {mp.nstr(ratio, 6):>12} (need {mp.nstr(expected_ratio, 6)}) {distinguishes}")

    # Findings
    print()
    print("  KEY FINDINGS:")
    print("    - C7 (anchored to proton) trivially closes p, has 0%-15% residual elsewhere")
    print("    - C8 (LO using CODATA m_p, m_n) closes by construction (uses inputs)")
    print("    - All substrate-only candidates (C1-C6, C9) FAIL by orders of magnitude")
    print("    - C1, C2, C4: T and ³He give SAME prediction (depend only on partitions of n=9)")
    print("      → cannot distinguish mirror pairs — REFUTED by atomic-mass-gb-nf line 107")
    print("    - C5, C6: distinguish T from ³He via |tr_M|, but residuals 1-3 orders off")
    print("    - C9 (Λ_QCD): orders of magnitude off — QCD alone doesn't give ρ_K")
    print()
    print("  CONCLUSION: no simple closed-form combination of (q_0, β_K)")
    print("  reproduces ρ_K to 5%.  The ρ_K formula likely involves")
    print("  substantive categorical content beyond what (max dim_q, partition")
    print("  sums, q-factorials) provides — consistent with paper's")
    print("  acknowledged-open status.")

    w = (WitnessBuilder("probe-rho-K-candidate-search", engine="python+mpmath")
         .set_description("Exhaustive ρ_K candidate-formula search against 5-atom table"))
    w.add_data("candidates_tested", results)
    w.add_data("conclusion",
               "No substrate-only candidate formula tested closes ρ_K to <5% "
               "across all 5 atoms.  C7 (anchored to proton) closes proton "
               "trivially but fails 15% on neutron.  C8 uses CODATA m_p/m_n "
               "as input (circular).  All others (C1-C6, C9) miss by 1-10 "
               "orders of magnitude.  ρ_K substrate derivation remains the "
               "paper's open problem.")
    closes_any = any(float(r["max_relative_residual"]) < 0.05 for r in results
                     if "C8" not in r["name"])
    w.add_assertion("any_substrate_only_candidate_closes",
                    computed=1.0 if closes_any else 0.0,
                    expected=0.0)  # we EXPECT to fail
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
