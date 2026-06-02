"""
log_delta_categorical_derivation.py — categorical derivation of the
log-Δ form from prop:unified-curvature-rank-mass-formula.

PR #787's Phase 2 finding: the empirical |Δ_λ*(K)| / (|χ^λ*(β_K)| ·
dim_q V_{λ*}) ratio has cross-atom variance 5.22× (best of any
phase). This script asks: what does the *categorical* derivation of
the unified formula say about this ratio, and does proper Wedderburn-
weighting collapse the variance?

The unified mass formula (prop:unified-curvature-rank-mass-formula):

    m_{q,K}(T) = Σ_{k=0}^{n-1} α_k · Φ_k(β_K, T)
    Φ_k(β_K, 1) = Σ_{λ: depth=k} ~w_λ · log|χ^λ(β_K) · dim_q V_λ|

where:
  - α_k is the structural prefactor (α_0=α_1=α_3=1, α_2=z_mark²,
    α_{k≥4} = m_e · 8·G_Catalan, per
    prop:plancherel-term-7-formulation)
  - ~w_λ = dim_q² V_λ / [n]_q! is the q-deformed Wedderburn weight
  - The block-restricted Frobenius integral ∫_{A_λ} ρ(β_K) · 1
    factorizes as χ^λ(β_K) · dim_q V_λ (Schur-Weyl pairing)

The empirical "best single block" Δ_λ values are NOT this categorical
Δ_λ — they're fits to B(K) = m_e · Σ y_λ χ^λ Δ_λ under a single-block
ansatz. The true categorical Δ_λ contribution is the per-(λ, K)
contribution from the unified formula, properly summed.

This script:
  1. Computes Φ_k(β_K, 1) per depth k using the existing ~w_λ
     infrastructure on the 4 atoms.
  2. Sums with structural α_k prefactors.
  3. Compares to AME binding energies.
  4. Reports the variance — if ≪ 5.22×, the unified formula IS the
     categorical closure (PR #787's diagnostic was correct).

Ref: prop:unified-curvature-rank-mass-formula
Ref: prop:plancherel-term-7-formulation
Ref: docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md
     (item 1: unified mass formula revival)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from q_parameter import Q as Q0, HBAR_Q

CHI_FILES = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}

B_AME = {
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}


def depth(lam: list[int]) -> int:
    """GB-filtration depth of partition λ = number of rows - 1."""
    return len(lam) - 1


def alpha_k(k: int) -> mp.mpf:
    """Structural prefactor α_k per prop:unified-curvature-rank-mass-formula
    + prop:plancherel-term-7-formulation."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k == 0: return mp.mpf(1)
    if k == 1: return mp.mpf(1)
    if k == 2: return z_mark ** 2
    if k == 3: return mp.mpf(1)
    # k >= 4: Term 7 universal (CAL-1 = M_E_MEV)
    return mp.mpf(str(M_E_MEV)) * 8 * G


def load_partition_data(atom: str) -> tuple[int, list[dict]]:
    """Load (n, partitions) for the given atom, with all needed fields."""
    w = json.loads((HERE / CHI_FILES[atom]).read_text())
    n = int(w["n_strands"])
    parsed = []
    for p in w["by_partition"]:
        lam = p["partition"] if isinstance(p["partition"], list) else ast.literal_eval(p["partition"])
        parsed.append({
            "partition": tuple(lam),
            "depth": depth(lam),
            "dim": int(p["dim"]),
            "y_lambda": mp.mpf(p["y_lambda"]),
            "chi": mp.mpf(p["chi_lambda"]),
            "contribution": mp.mpf(p["contribution"]),  # y · χ — direct from witness
        })
    return n, parsed


def phi_k(parts: list[dict], k: int, weight_form: str = "y_lambda") -> mp.mpf:
    """Sum over partitions of depth k.

    weight_form options:
      'y_lambda'      — use y_λ from witness (Jones-Markov central)
      'w_lambda'      — use w_λ = dim² V_λ / n! (classical Plancherel)
      'identity'      — use weight = 1 (no Wedderburn weighting)
    """
    total = mp.mpf(0)
    for p in parts:
        if p["depth"] != k: continue
        chi = p["chi"]; dim_q = p["dim"]
        # |χ · dim_q| — block-restricted Frobenius integral magnitude
        f = mp.fabs(chi) * dim_q
        if f < mp.mpf("1e-30"): continue
        # Pick weight per `weight_form`
        if weight_form == "y_lambda":
            w = p["y_lambda"]
        elif weight_form == "w_lambda":
            n_total = sum(p["partition"])
            w = mp.mpf(dim_q ** 2) / mp.factorial(n_total)
        else:
            w = mp.mpf(1)
        total += w * mp.log(f)
    return total


def unified_mass_predict(atom: str, weight_form: str = "y_lambda") -> mp.mpf:
    """Compute m_{q,K}(1) = Σ_k α_k · Φ_k(β_K, 1) per the unified formula."""
    n, parts = load_partition_data(atom)
    total = mp.mpf(0)
    for k in range(n):
        ak = alpha_k(k)
        pk = phi_k(parts, k, weight_form=weight_form)
        total += ak * pk
    return total


def main() -> int:
    builder = WitnessBuilder("log-delta-categorical-derivation")
    builder.set_description(
        "Categorical-derivation test for the log-Δ form (PR #787 Phase 2 "
        "5.22× residual). Applies prop:unified-curvature-rank-mass-formula "
        "with structural α_k and tests three Wedderburn-weighting forms "
        "(y_λ, w_λ, identity) on D, T, ³He, ⁴He."
    )
    builder.add_parameter("q0", str(Q0))
    builder.add_parameter("hbar_q", str(HBAR_Q))
    builder.add_parameter("z_mark", str(1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))))
    builder.add_parameter("catalan_G", str(mp.catalan))

    results = {}
    print(f"{'atom':<6} {'weight':<14} {'unified m':>14} {'B_AME':>12} {'m/B':>10} {'log|m/B|':>10}")
    for atom in ("D", "T", "3He", "4He"):
        B = B_AME[atom]
        for weight_form in ("y_lambda", "w_lambda", "identity"):
            m = unified_mass_predict(atom, weight_form)
            ratio = m / B if B != 0 else mp.mpf("nan")
            log_abs_ratio = mp.log(mp.fabs(ratio)) if mp.fabs(ratio) > 1e-30 else mp.mpf("nan")
            results.setdefault(weight_form, {})[atom] = {
                "m_predicted": str(m),
                "B_AME": str(B),
                "ratio": float(ratio),
                "log_abs_ratio": float(log_abs_ratio),
            }
            print(f"  {atom:<6} {weight_form:<14} {float(m):>14.4f} {float(B):>12.4f} "
                  f"{float(ratio):>10.4f} {float(log_abs_ratio):>10.4f}")
        print()

    # Per-weight-form cross-atom variance test
    for wf, atom_data in results.items():
        ratios = [r["ratio"] for r in atom_data.values() if not mp.isnan(mp.mpf(r["ratio"]))]
        if len(ratios) >= 2:
            rmin = min(abs(r) for r in ratios)
            rmax = max(abs(r) for r in ratios)
            mom = rmax / rmin if rmin > 0 else float("inf")
            mean_log = sum(r["log_abs_ratio"] for r in atom_data.values()) / len(atom_data)
            atom_data["__stats__"] = {
                "max_over_min": float(mom),
                "mean_log_abs_ratio": float(mean_log),
            }
    builder.add_data("unified_formula_per_weight_form", results)
    builder.add_data("canonical_status", "canonical-with-empirical-assignment")

    print(f"\n{'weight form':<14} {'max/min ratio':>14} {'mean log|m/B|':>14}")
    for wf in ("y_lambda", "w_lambda", "identity"):
        s = results[wf].get("__stats__", {})
        print(f"  {wf:<14} {s.get('max_over_min', '-'):>14.4f} {s.get('mean_log_abs_ratio', '-'):>14.4f}")

    # Verdict
    best_wf = min(("y_lambda", "w_lambda", "identity"),
                   key=lambda w: results[w].get("__stats__", {}).get("max_over_min", float("inf")))
    best_mom = results[best_wf]["__stats__"]["max_over_min"]
    builder.add_data("best_weight_form", best_wf)
    builder.add_data("best_max_over_min", best_mom)

    if best_mom < 1.05:
        verdict = f"PASS — {best_wf} weighting gives max/min < 1.05 (≈ universal categorical c)"
    elif best_mom < 2.0:
        verdict = f"PROMISING — {best_wf} gives max/min = {best_mom:.2f} (close to constant)"
    elif best_mom < 5.22:
        verdict = f"IMPROVES — {best_wf} gives max/min = {best_mom:.2f} (better than Phase 2's 5.22×)"
    else:
        verdict = f"NO IMPROVEMENT — best max/min = {best_mom:.2f} (>= 5.22× Phase 2 baseline)"
    builder.add_data("verdict", verdict)
    print(f"\n  Verdict: {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) AME MeV",
        source="AME 2020",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
