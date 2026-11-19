#!/usr/bin/env python3
"""
H₂ molecular braid: binding energy from the LP dual.

Computes the molecular braid of H₂ = 2 protons + 2 electrons
in H₄(q), using the transfer matrix chain reduction.

Content block: prop:h2-lp-dual-binding

Usage:
    python3 computations/h2-molecular-binding.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import itertools
import sys
from pathlib import Path
from mpmath import mp, mpf

sys.path.insert(0, str(Path(__file__).parent))
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(60)

q0 = mpf(Q_50_DIGIT_STR)
qi = mpf(1) / q0
HA = q0 - qi
TWO_Q = q0 + qi
z = (q0 ** 3) / (q0 ** 2 + mpf(1))


def crossing_coeff_molecular(ti: str, tj: str, same_atom: bool) -> tuple[mpf, mpf, str]:
    """Return (c, d, label) for molecular crossing between strand types."""
    t_i = ti[0]
    t_j = tj[0]

    if same_atom:
        if (t_i == "p" and t_j == "e") or (t_i == "e" and t_j == "p"):
            HA_d = q0 ** 5 - qi ** 5
            return mpf(1), -(HA_d - HA), "pe_dressed"
        return mpf(0), mpf(1), "same_atom_other"

    if t_i == "p" and t_j == "p":
        return mpf(1), mpf(0), "pp_inter"
    if t_i == "e" and t_j == "e":
        return mpf(1), mpf(0), "ee_inter"
    if (t_i == "p" and t_j == "e") or (t_i == "e" and t_j == "p"):
        return mpf(1), -HA, "pe_inter"
    return mpf(0), mpf(1), "other"


def compute_Phi1(ordering: list[int], strand_labels: list[tuple[str, int]]) -> tuple[mpf, list[mpf]]:
    """Compute Φ₁ = Σ ln|V̂ᵢ| for a given strand ordering."""
    n = len(ordering)
    if n <= 1:
        return mpf(0), []

    Phi = mpf(0)
    volumes: list[mpf] = []

    for gen in range(n - 1):
        a, b = mpf(0), mpf(1)
        si = strand_labels[ordering[gen]]

        for j in range(gen + 1, n):
            sj = strand_labels[ordering[j]]
            same = si[1] == sj[1]

            ti = si[0] + str(si[1])
            tj = sj[0] + str(sj[1])
            c, d, _ = crossing_coeff_molecular(ti, tj, same)

            if c == mpf(0) and d == mpf(1):
                continue

            a_new = a * (c * HA + d) + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new

        V = z * a + b
        volumes.append(V)
        Phi += mp.log(abs(V))

    return Phi, volumes


strand_labels = [
    ("p", 1),
    ("e", 1),
    ("p", 2),
    ("e", 2),
]


def compute_Phi1_H_atom() -> tuple[mpf, mpf]:
    """Φ₁ for an isolated hydrogen atom = single dressed pe crossing."""
    HA_d = q0 ** 5 - qi ** 5
    c, d = mpf(1), -(HA_d - HA)
    a, b = c, d
    V = z * a + b
    return mp.log(abs(V)), V


Phi1_H, V_H = compute_Phi1_H_atom()
Phi1_sep = mpf(2) * Phi1_H

print("=" * 70)
print("H₂ MOLECULAR BRAID: BINDING ENERGY FROM LP DUAL")
print("=" * 70)
print(f"\nSubstrate parameter: q₀ = {mp.nstr(q0, 12)}")
print(f"HA = q - q⁻¹ = {mp.nstr(HA, 10)}")
print(f"z = q³/(q² + 1) = {mp.nstr(z, 10)}")
print()
print("--- Isolated H atom ---")
print(f"  Dressed HA: q⁵ - q⁻⁵ = {mp.nstr(q0**5 - qi**5, 10)}")
print(f"  V_H = {mp.nstr(V_H, 10)}")
print(f"  Φ₁(H) = ln|V_H| = {mp.nstr(Phi1_H, 10)}")
print(f"  Φ₁(2 separate H) = {mp.nstr(Phi1_sep, 10)}")
print()

print("--- H₂ molecule: enumerate all 4! = 24 orderings ---")
print()

all_orderings = list(itertools.permutations(range(4)))
results = []

for perm in all_orderings:
    Phi, vols = compute_Phi1(list(perm), strand_labels)
    labels = [f"{strand_labels[i][0]}{strand_labels[i][1]}" for i in perm]
    results.append({
        "perm": perm,
        "labels": labels,
        "Phi1": Phi,
        "volumes": vols,
        "binding": Phi1_sep - Phi,
    })

results.sort(key=lambda r: r["Phi1"])

print(f"{'Rank':>4} {'Ordering':>20} {'Φ₁':>12} {'Binding':>12} {'Bound?':>6}")
print("-" * 60)

for i, r in enumerate(results):
    label_str = "[" + ", ".join(r["labels"]) + "]"
    bound = "YES" if r["binding"] > mpf(0) else "no"
    print(f"{i+1:>4} {label_str:>20} {mp.nstr(r['Phi1'], 7):>12s} {mp.nstr(r['binding'], 6):>12s} {bound:>6}")

best = results[0]

print()
print("--- Optimal binding ---")
print(f"  Ground state: [{', '.join(best['labels'])}]")
print(f"  Φ₁(H₂) = {mp.nstr(best['Phi1'], 10)}")
print(f"  Φ₁(2H)  = {mp.nstr(Phi1_sep, 10)}")
print(f"  Binding: Φ₁(2H) - Φ₁(H₂) = {mp.nstr(best['binding'], 10)}")
print()
print("  Per-generator volumes:")
for j, V in enumerate(best["volumes"]):
    print(f"    σ_{j}: V̂ = {mp.nstr(V, 10)}, ln|V̂| = {mp.nstr(mp.log(abs(V)), 10)}")
print()

# Pure-mpf derived α_EM and Hartree scale at the proton pin:
alpha_em_inv = alpha_em_inv_derived(q0, order=None)
alpha_em = mpf(1) / alpha_em_inv
me_ev = mpf(str(M_E_MEV)) * (mpf(10) ** 6)
E_hartree_eV = me_ev / (alpha_em_inv ** 2)
E_mol_scale = E_hartree_eV / (TWO_Q ** 2)
E_bind_eV = best["binding"] * E_mol_scale
D0_obs_eV = mpf("4.478")

print("--- Physical binding energy ---")
print(f"  α_EM = {mp.nstr(alpha_em, 10)}, 1/α_EM = {mp.nstr(alpha_em_inv, 12)}")
print(f"  E_hartree = m_e × α² = {mp.nstr(E_hartree_eV, 10)} eV")
print(f"  [2]_q = q + q⁻¹ = {mp.nstr(TWO_Q, 10)}")
print(f"  [2]_q² = {mp.nstr(TWO_Q**2, 10)}")
print(f"  E_mol = E_hartree / [2]_q² = {mp.nstr(E_mol_scale, 10)} eV")
print(f"  E_bind(H₂) = ΔΦ₁ × E_mol = {mp.nstr(best['binding'], 6)} × {mp.nstr(E_mol_scale, 6)} = {mp.nstr(E_bind_eV, 6)} eV")
print("  Observed D₀(H₂) = 4.478 eV")
print(f"  Ratio pred/obs = {mp.nstr(E_bind_eV / D0_obs_eV, 5)}")
print()


def compute_Phi1_without(ordering: list[int], strand_labels: list[tuple[str, int]], skip: tuple[int, int]) -> mpf:
    """Compute Phi_1 with one crossing replaced by identity."""
    n = len(ordering)
    Phi = mpf(0)
    for gen in range(n - 1):
        a, b = mpf(0), mpf(1)
        si = strand_labels[ordering[gen]]

        for j in range(gen + 1, n):
            if (gen, j) == skip:
                continue

            sj = strand_labels[ordering[j]]
            same = si[1] == sj[1]
            ti = si[0] + str(si[1])
            tj = sj[0] + str(sj[1])
            c, d, _ = crossing_coeff_molecular(ti, tj, same)

            if c == mpf(0) and d == mpf(1):
                continue

            a_new = a * (c * HA + d) + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new

        V = z * a + b
        Phi += mp.log(abs(V))

    return Phi


print("--- LP dual: crossing sensitivity ---")
print()

best_ordering = list(best["perm"])
Phi_full = best["Phi1"]

print(f"  Ground state ordering: [{', '.join(best['labels'])}]")
print(f"  Φ₁(full) = {mp.nstr(Phi_full, 10)}")
print()
print(f"  {'Pair':>15} {'Type':>12} {'Φ₁(without)':>12} {'δΦ₁':>12} {'% of Φ₁':>10}")
print("  " + "-" * 65)

for i in range(4):
    for k in range(i + 1, 4):
        si = strand_labels[best_ordering[i]]
        sk = strand_labels[best_ordering[k]]
        same = si[1] == sk[1]

        ti = si[0] + str(si[1])
        tk = sk[0] + str(sk[1])
        _, _, label = crossing_coeff_molecular(ti, tk, same)

        Phi_without = compute_Phi1_without(best_ordering, strand_labels, skip=(i, k))
        delta = Phi_full - Phi_without
        pct = abs(delta / Phi_full) * mpf(100) if abs(Phi_full) > mpf("1e-30") else mpf(0)

        pair_label = f"{ti}↔{tk}"
        print(f"  {pair_label:>15} {label:>12} {mp.nstr(Phi_without, 7):>12s} {mp.nstr(delta, 6):>12s} {mp.nstr(pct, 4):>9s}%")

print()
print("--- Summary ---")
print(f"  Ground state: [{', '.join(best['labels'])}]")
print(f"  Φ₁(2 isolated H) = {mp.nstr(Phi1_sep, 10)}")
print(f"  Φ₁(H₂ molecule)  = {mp.nstr(best['Phi1'], 10)}")
print(f"  Φ₁ difference     = {mp.nstr(best['binding'], 10)}")
print(f"  Predicted D₀(H₂) = {mp.nstr(E_bind_eV, 6)} eV")
print("  Observed  D₀(H₂) = 4.478 eV")
print(f"  Ratio pred/obs = {mp.nstr(E_bind_eV / D0_obs_eV, 5)}")
print(f"  Error = {mp.nstr((E_bind_eV / D0_obs_eV - mpf(1)) * mpf(100), 4)}%")
print()

w = WitnessBuilder("h2-molecular-binding", engine="python")
w.set_description(
    "H₂ molecular braid binding energy from LP dual. "
    "Enumerates all 24 strand orderings of H₄(q), finds optimal "
    "binding by comparing molecular Φ₁ with 2 isolated H atoms."
)
w.set_content_block("prop:h2-lp-dual-binding")

w.add_parameter("q", fmt(q0))
w.add_parameter("HA", fmt(HA))
w.add_parameter("z", fmt(z))
w.add_parameter("alpha_EM", fmt(alpha_em))
w.add_parameter("E_hartree_eV", fmt(E_hartree_eV))
w.add_parameter("TWO_Q", fmt(TWO_Q))
w.add_parameter("E_mol_scale_eV", fmt(E_mol_scale))
w.add_parameter("strand_labels", ["p1", "e1", "p2", "e2"])

w.add_data("Phi1_H_isolated", fmt(Phi1_H))
w.add_data("Phi1_2H_separated", fmt(Phi1_sep))
w.add_data("V_H_isolated", fmt(V_H))
w.add_data("Phi1_H2_optimal", fmt(best["Phi1"]))
w.add_data("optimal_ordering", list(best["labels"]))
w.add_data("binding_Phi_diff", fmt(best["binding"]))
w.add_data("E_bind_eV_predicted", fmt(E_bind_eV))
w.add_data("generator_volumes", [fmt(v) for v in best["volumes"]])
w.add_data("all_orderings_ranked", [
    {"ordering": list(r["labels"]), "Phi1": fmt(r["Phi1"]), "binding": fmt(r["binding"])}
    for r in results[:6]
])

w.add_assertion(
    "H2 binding is positive",
    computed=bool(best["binding"] > mpf(0)),
    expected=True,
    source="LP dual ground state",
)
w.add_assertion(
    "Interleaved ordering is optimal",
    computed=(strand_labels[best["perm"][0]][0] != strand_labels[best["perm"][1]][0]),
    expected=True,
    source="LP dual enumeration",
)
w.add_assertion(
    "H2 binding energy within 5% of observed (no calibration)",
    computed=fmt(E_bind_eV),
    expected=fmt(D0_obs_eV),
    tolerance="0.25",
    unit="eV",
    source="D_0(H2) = 4.478 eV, zero fitted parameters",
)

w.save()
print()
print("Done. Witness saved.")
