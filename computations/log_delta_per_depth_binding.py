"""
log_delta_per_depth_binding.py — option (a) test: per-depth binding
subtraction in the unified mass formula.

Per the prior finding (full-mass-subtract gives max/min 3.96× but
T/³He come out with WRONG sign — predicted unbound): the structural
issue is that α_{k≥4} = m_e·8G is constant across depths, so m_q,K
grows super-linearly with n. The constituent-subtraction subtracts
Z·m_p + N·m_n EXTERNALLY, but the proton/neutron only contribute
to depths 0, 1, 2 (n=3 partitions have max depth 2). Atom contributions
at depth k ≥ 3 are uncorrected.

This script implements the per-depth-stratified binding:

    m^(k)_{q, K | bind} := m^(k)_{q, K} - Z · m^(k)_{q, p} - N · m^(k)_{q, n}
    B(K) := Σ_k α_k · m^(k)_{q, K | bind}

For k ≥ 3 (constituents = 0), m^(k)_{K|bind} = m^(k)_K (uncorrected).
But the structural prefactor α_{k≥4} = m_e·8G is universal — it
should give the SAME contribution per partition. So per-depth
binding at high k is the atom's "extra" high-depth complexity beyond
what would arise from independent nucleons.

If the high-depth contribution is the right "binding signal", we
expect B_pred to track AME with low cross-atom variance.

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

B_AME = {
    "p":   mp.mpf(0), "n":   mp.mpf(0),
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"p": (1, 0), "n": (0, 1), "D": (1, 1), "T": (1, 2),
      "3He": (2, 1), "4He": (2, 2)}


def alpha_k(k):
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3): return mp.mpf(1)
    if k == 2: return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G  # k >= 4 (CAL-1)


def q_int(k):
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - 1 / Q0)


def q_factorial(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= q_int(k)
    return r


def load_chi(sp):
    w = json.loads((HERE / CHI_FILES[sp]).read_text())
    n = int(w["n_strands"])
    parts = []
    for p in w["by_partition"]:
        lam = p["partition"] if isinstance(p["partition"], list) else ast.literal_eval(p["partition"])
        parts.append({
            "depth": len(lam) - 1,
            "dim": int(p["dim"]),
            "chi": mp.mpf(p["chi_lambda"]),
        })
    return n, parts


def phi_k(parts, n, k):
    """Φ_k(β) with paper-prescribed ~w_λ = dim_q² / [n]_q!"""
    total = mp.mpf(0)
    qfact = q_factorial(n)
    for p in parts:
        if p["depth"] != k: continue
        chi = p["chi"]; dim_q = mp.mpf(p["dim"])
        f = mp.fabs(chi) * dim_q
        if f < mp.mpf("1e-30"): continue
        w = dim_q ** 2 / qfact
        total += w * mp.log(f)
    return total


def per_species_phi(sp):
    """Return (n, {k: Φ_k}) for species."""
    n, parts = load_chi(sp)
    return n, {k: phi_k(parts, n, k) for k in range(n)}


def main() -> int:
    builder = WitnessBuilder("log-delta-per-depth-binding")
    builder.set_description(
        "Option (a) test: per-depth-stratified binding subtraction in "
        "prop:unified-curvature-rank-mass-formula. B(K) = Σ_k α_k · "
        "[m^(k)_K - Z·m^(k)_p - N·m^(k)_n] with paper-prescribed ~w_λ."
    )

    # Compute Φ_k per species per depth
    phi_data = {}
    n_per_sp = {}
    for sp in ("p", "n", "D", "T", "3He", "4He"):
        n, phis = per_species_phi(sp)
        phi_data[sp] = phis
        n_per_sp[sp] = n

    builder.add_data("phi_k_per_species", {
        sp: {str(k): str(v) for k, v in phis.items()}
        for sp, phis in phi_data.items()
    })
    builder.add_data("n_per_species", n_per_sp)

    # Per-depth binding subtraction
    print(f"{'atom':<6} {'n':>3} {'B_pred':>16} {'B_AME':>10} {'|B_pred/B_AME|':>16}")
    results = {}
    for atom in ("D", "T", "3He", "4He"):
        Z, N = ZN[atom]
        n_atom = n_per_sp[atom]
        # Per-depth binding: for each k available in atom, subtract Z·proton + N·neutron at same k
        # (constituents have only k = 0, 1, 2; for k ≥ 3, m^(k)_{p,n} = 0)
        B_pred = mp.mpf(0)
        per_depth_contribs = []
        for k in range(n_atom):
            m_atom_k = phi_data[atom].get(k, mp.mpf(0))
            m_p_k = phi_data["p"].get(k, mp.mpf(0))  # 0 for k ≥ 3
            m_n_k = phi_data["n"].get(k, mp.mpf(0))  # 0 for k ≥ 3
            m_bind_k = m_atom_k - Z * m_p_k - N * m_n_k
            contrib = alpha_k(k) * m_bind_k
            per_depth_contribs.append({
                "k": k,
                "alpha_k": str(alpha_k(k)),
                "m_atom_k": str(m_atom_k),
                "m_p_k": str(m_p_k),
                "m_n_k": str(m_n_k),
                "m_bind_k": str(m_bind_k),
                "contrib": str(contrib),
            })
            B_pred += contrib

        B_emp = B_AME[atom]
        ratio = mp.fabs(B_pred / B_emp) if B_emp != 0 else mp.mpf("nan")
        results[atom] = {
            "B_pred": str(B_pred),
            "B_pred_sign": "+" if B_pred > 0 else "-",
            "B_AME": str(B_emp),
            "abs_ratio": float(ratio),
            "per_depth": per_depth_contribs,
        }
        print(f"  {atom:<6} {n_atom:>3} {float(B_pred):>16.6f} {float(B_emp):>10.4f} {float(ratio):>16.6f}")

    builder.add_data("per_depth_binding_results", results)
    builder.add_data("canonical_status", "canonical-with-empirical-assignment")

    # Variance
    abs_ratios = [r["abs_ratio"] for r in results.values()]
    rmin, rmax = min(abs_ratios), max(abs_ratios)
    mom = rmax / rmin if rmin > 0 else float("inf")
    builder.add_data("max_over_min", float(mom))

    if mom < 1.05:
        verdict = f"PASS — max/min = {mom:.3f} < 1.05 (universal categorical c)"
    elif mom < 1.5:
        verdict = f"STRONG — max/min = {mom:.3f} (under 1.5×)"
    elif mom < 2.0:
        verdict = f"GOOD — max/min = {mom:.3f} (better than full-mass-subtract 3.96×)"
    elif mom < 3.96:
        verdict = f"IMPROVES — max/min = {mom:.3f} (better than full-mass-subtract 3.96×)"
    else:
        verdict = f"NO IMPROVEMENT — max/min = {mom:.3f} (≥ 3.96×)"
    builder.add_data("verdict", verdict)
    print(f"\n  max/min = {mom:.4f}")
    print(f"  Verdict: {verdict}")

    # Sign check
    signs_consistent = all(mp.mpf(r["B_pred"]) > 0 for r in results.values())
    builder.add_data("all_signs_correct", signs_consistent)
    print(f"  All B_pred > 0 (correct binding sign): {signs_consistent}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
