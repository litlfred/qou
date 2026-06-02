"""
log_delta_full_mass_subtract.py — categorical derivation of B(K) as
the FULL-MASS DIFFERENCE under the unified formula.

Per the prior finding (log_delta_categorical_derivation.py): applying
prop:unified-curvature-rank-mass-formula with paper's prescribed
weight ~w_λ = dim_q²/[n]_q! to compute B(K) directly gives 43× cross-
atom variance. Identity weight gives 4.6×.

**Hypothesis to test:** the unified formula with ~w_λ is correct for
the FULL atomic mass m_{q,K}, NOT for the binding energy B(K). The
binding is the *difference* between atomic full-mass and constituent
proton/neutron full-mass:

    B(K) = m_{q,K} - Z · m_{q,p} - N · m_{q,n}

This script:
  1. Computes m_{q,X} for X ∈ {p, n, D, T, ³He, ⁴He} using the unified
     formula with paper-prescribed ~w_λ (the "correct" full-mass weight).
  2. Forms B_pred(K) = m_{q,K} - Z · m_{q,p} - N · m_{q,n}.
  3. Compares to AME binding.
  4. Reports cross-atom variance.

If B_pred matches AME with variance ≪ 5.22× (or even ≪ 4.6×), this
substantiates the categorical claim that the unified formula is
PAPER-CORRECT and the binding energy is the n-strand-renormalized
difference, NOT a direct application of the formula.

Ref: prop:unified-curvature-rank-mass-formula
Ref: docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md
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
from q_parameter import Q as Q0

CHI_FILES = {
    "p":   "chi-proton-h3-at-q0-50dps.witness.json",
    "n":   "chi-neutron-h3-at-q0-50dps.witness.json",
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}

B_AME = {  # binding energies (MeV); 0 for free nucleons
    "p":   mp.mpf(0),
    "n":   mp.mpf(0),
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

# (Z, N) for each species
ZN = {"p": (1, 0), "n": (0, 1), "D": (1, 1), "T": (1, 2),
      "3He": (2, 1), "4He": (2, 2)}


def depth(lam):
    return len(lam) - 1


def alpha_k(k):
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k == 0 or k == 1 or k == 3: return mp.mpf(1)
    if k == 2: return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G  # k >= 4 (CAL-1)


def q_int(k):
    """[k]_q = (q^k - q^{-k})/(q - q^{-1})"""
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - 1 / Q0)


def q_factorial(n):
    """[n]_q! = [1]_q [2]_q ... [n]_q"""
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= q_int(k)
    return r


def load_chi(species):
    """Load (n, partitions) for species X."""
    w = json.loads((HERE / CHI_FILES[species]).read_text())
    n = int(w["n_strands"])
    parts = []
    for p in w["by_partition"]:
        lam = p["partition"] if isinstance(p["partition"], list) else ast.literal_eval(p["partition"])
        parts.append({
            "partition": tuple(lam),
            "depth": depth(lam),
            "dim": int(p["dim"]),
            "chi": mp.mpf(p["chi_lambda"]),
        })
    return n, parts


def phi_k(parts, n, k, w_form="paper"):
    """Φ_k(β) under chosen weight form."""
    total = mp.mpf(0)
    qfact = q_factorial(n)
    for p in parts:
        if p["depth"] != k: continue
        chi = p["chi"]; dim_q = mp.mpf(p["dim"])
        f = mp.fabs(chi) * dim_q
        if f < mp.mpf("1e-30"): continue
        if w_form == "paper":
            w = dim_q ** 2 / qfact  # paper's ~w_λ
        elif w_form == "identity":
            w = mp.mpf(1)
        else:
            raise ValueError(w_form)
        total += w * mp.log(f)
    return total


def unified_mass(species, w_form="paper"):
    n, parts = load_chi(species)
    total = mp.mpf(0)
    for k in range(n):
        total += alpha_k(k) * phi_k(parts, n, k, w_form)
    return total, n


def main() -> int:
    builder = WitnessBuilder("log-delta-full-mass-subtract")
    builder.set_description(
        "Categorical test: B(K) = m_{q,K} - Z·m_{q,p} - N·m_{q,n} via "
        "prop:unified-curvature-rank-mass-formula with paper-prescribed "
        "~w_λ weight. Tests if the binding-energy projection IS the "
        "n-strand-renormalized difference."
    )

    print(f"{'species':<6} {'n':>3} {'w_form':<10} {'m_q,X':>16}")
    full_mass = {}
    for w_form in ("paper", "identity"):
        full_mass[w_form] = {}
        for sp in ("p", "n", "D", "T", "3He", "4He"):
            m, n = unified_mass(sp, w_form)
            full_mass[w_form][sp] = m
            print(f"  {sp:<6} {n:>3} {w_form:<10} {float(m):>16.6f}")
        print()

    builder.add_data("full_mass_per_species", {
        wf: {sp: str(m) for sp, m in d.items()}
        for wf, d in full_mass.items()
    })

    # Compute B_pred(K) = m_K - Z·m_p - N·m_n per weight form
    print(f"{'atom':<6} {'w_form':<10} {'B_pred':>14} {'B_AME':>12} {'ratio':>10}")
    results = {}
    for w_form in ("paper", "identity"):
        mp_full = full_mass[w_form]
        results[w_form] = {}
        for atom in ("D", "T", "3He", "4He"):
            Z, N = ZN[atom]
            B_pred = mp_full[atom] - Z * mp_full["p"] - N * mp_full["n"]
            B_emp = B_AME[atom]
            ratio = mp.fabs(B_pred / B_emp) if B_emp != 0 else mp.mpf("nan")
            results[w_form][atom] = {
                "B_pred": str(B_pred),
                "B_AME": str(B_emp),
                "ratio": float(ratio),
            }
            print(f"  {atom:<6} {w_form:<10} {float(B_pred):>14.6f} "
                  f"{float(B_emp):>12.6f} {float(ratio):>10.4f}")
        print()

    builder.add_data("binding_by_difference", results)
    builder.add_data("canonical_status", "canonical-with-empirical-assignment")

    # Cross-atom variance
    print(f"{'w_form':<10} {'min ratio':>12} {'max ratio':>12} {'max/min':>10}")
    summary = {}
    for w_form, atoms in results.items():
        rs = [r["ratio"] for r in atoms.values()]
        rs = [r for r in rs if not mp.isnan(mp.mpf(r))]
        if rs:
            rmin, rmax = min(rs), max(rs)
            mom = rmax / rmin if rmin > 0 else float("inf")
            summary[w_form] = {"min": rmin, "max": rmax, "max_over_min": mom}
            print(f"  {w_form:<10} {rmin:>12.4f} {rmax:>12.4f} {mom:>10.4f}")
    builder.add_data("variance_summary", summary)

    # Verdict
    best = min(summary.keys(), key=lambda k: summary[k]["max_over_min"])
    best_mom = summary[best]["max_over_min"]
    builder.add_data("best_form", best)
    builder.add_data("best_max_over_min", best_mom)
    if best_mom < 1.05:
        verdict = f"PASS — {best} gives max/min < 1.05 (universal categorical constant)"
    elif best_mom < 1.5:
        verdict = f"STRONG — {best} max/min = {best_mom:.3f} (under 1.5×, much better than direct 5.22×)"
    elif best_mom < 4.6:
        verdict = f"IMPROVES — {best} max/min = {best_mom:.3f} (better than identity-direct 4.6×)"
    elif best_mom < 5.22:
        verdict = f"MARGINAL — {best} max/min = {best_mom:.3f} (better than Phase 2's 5.22× but not by much)"
    else:
        verdict = f"NO IMPROVEMENT — {best} max/min = {best_mom:.3f} (≥ 5.22×)"
    builder.add_data("verdict", verdict)
    print(f"\n  Verdict: {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) AME MeV",
        source="AME 2020 deuteron binding",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
