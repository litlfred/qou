#!/usr/bin/env python3
"""
Derivation-only checks — no fitting.

(1) Rigorously verify χ_sym·χ_alt = -(1 + H_A²/4)^(2A+1) by
    counting ud factors in atom_braid_word_3A directly.

(2) Determine what normalization factor makes α·Φ_1 match B_AME.
    No fit — just report the target factor per atom.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))

from mass_at_3A_proper import atom_braid_word_3A
from hecke_core import atom_per_generator_volumes
from q_parameter import Q as q0, HA

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN_8G = 8.0 * CATALAN_G
M_E_MEV = 0.51099895
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN_8G

ATOMS = [
    ("D",   1, 1, 2.22456612),
    ("T",   1, 2, 8.4817984),
    ("3He", 2, 1, 7.7180375),
    ("4He", 2, 2, 28.295674),
]

# Classify each (c, d) pair appearing in atom_braid_word_3A.
# Expected cases:
#   (1, 0)      → pure σ_k        (B_3, uu, gluon)
#   (1, -HA)    → pure σ_k^{-1}   (B_3 inverse)
#   (1, -HA/2)  → "ud" quark pair (pn coupling also uses -HA/2)
#   (0.5, 0)    → 1/2 σ_k (pn half-crossing?)
def classify_factor(c: float, d: float, tol: float = 1e-9):
    if abs(c - 1) < tol and abs(d) < tol:
        return "sigma"
    if abs(c - 1) < tol and abs(d + HA) < tol:
        return "sigma_inv"
    if abs(c - 1) < tol and abs(d + HA / 2) < tol:
        return "ud_half"
    return f"other(c={c:.4f},d={d:.4f})"


def analyse_word(Z, N):
    word = atom_braid_word_3A(Z, N)
    types = Counter()
    for (c, d, g) in word:
        types[classify_factor(c, d)] += 1
    return word, types


def predicted_chi_product(A: int, n_ud: int) -> float:
    """Per derivation: χ_sym·χ_alt = -(1 + H_A²/4)^(n_ud) for ud factors
    only; pure σ and σ^{-1} each contribute -1 (trivial)."""
    hsq = float(HA) ** 2
    return -(1.0 + hsq / 4.0) ** n_ud


if __name__ == "__main__":
    print("=" * 100)
    print("DERIVATION CHECK (1): χ_sym · χ_alt closed form")
    print(f"  H_A = q - q^(-1) = {float(HA):.6f}")
    print(f"  H_A²/4 = {float(HA)**2/4:.6f}")
    print(f"  1 + H_A²/4 = {1 + float(HA)**2/4:.6f}")
    print("=" * 100)

    check_results = []

    # Observed χ_sym · χ_alt values from sym_alt_mirror_probe
    OBSERVED_CHI_PROD = {
        "D":   -1.0558,
        "T":   -1.0790,
        "3He": -1.0790,
        "4He": -1.1027,
    }

    print(f"\n  {'atom':>4} {'A':>2} {'word_len':>9} "
          f"{'n_sigma':>9} {'n_sigma_inv':>12} {'n_ud':>6} "
          f"{'2A+1':>5} {'other':>20}")
    for (name, Z, N, B_ame) in ATOMS:
        word, types = analyse_word(Z, N)
        n_sigma = types.get("sigma", 0)
        n_siginv = types.get("sigma_inv", 0)
        n_ud = types.get("ud_half", 0)
        other = {k: v for k, v in types.items()
                  if k not in ("sigma", "sigma_inv", "ud_half")}
        A = Z + N
        print(f"  {name:>4} {A:>2} {len(word):>9} "
              f"{n_sigma:>9} {n_siginv:>12} {n_ud:>6} "
              f"{2*A + 1:>5} {str(other) if other else '{}':>20}")

        predicted = predicted_chi_product(A, n_ud)
        observed = OBSERVED_CHI_PROD[name]
        check_results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "word_length": len(word),
            "n_sigma": n_sigma, "n_sigma_inv": n_siginv,
            "n_ud_half": n_ud,
            "expected_2A_plus_1": 2*A + 1,
            "other_factors": dict(other),
            "chi_sym_times_chi_alt_predicted": predicted,
            "chi_sym_times_chi_alt_observed": observed,
            "diff_pct": ((predicted - observed) / abs(observed) * 100
                          if observed else float("nan")),
        })

    print(f"\n  {'atom':>4} {'n_ud':>6} "
          f"{'predicted':>14} {'observed':>14} {'diff %':>10}")
    for r in check_results:
        print(f"  {r['atom']:>4} {r['n_ud_half']:>6} "
              f"{r['chi_sym_times_chi_alt_predicted']:>+14.6f} "
              f"{r['chi_sym_times_chi_alt_observed']:>+14.6f} "
              f"{r['diff_pct']:>+9.3f}%")

    # Derivation check (2): what correction would match B?
    print(f"\n{'=' * 100}")
    print("DERIVATION CHECK (2): what correction brings α·|Φ_1| to B_AME?")
    print(f"  α = m_e · 8G = {ALPHA_MEV:.6f} MeV")
    print("=" * 100)

    print(f"\n  {'atom':>4} {'Φ_1':>10} {'α·|Φ_1|':>14} "
          f"{'B_AME':>10} {'factor':>10} {'simple?':>20}")

    norm_results = []
    for (name, Z, N, B_ame) in ATOMS:
        v_atom = atom_per_generator_volumes(Z, N, include_inter=True)
        v_free = atom_per_generator_volumes(Z, N, include_inter=False)

        def _sum_ln(vs):
            total = 0.0
            for v in vs:
                f = v["full"]
                if abs(f) < 1e-30:
                    return float("nan")
                total += math.log(abs(f))
            return total

        phi_1 = _sum_ln(v_atom) - _sum_ln(v_free)
        B_derived = -ALPHA_MEV * phi_1
        factor = B_ame / B_derived if B_derived else float("nan")

        # Check if factor is a simple rational / q-expression
        candidates = {
            "1": 1.0,
            "1/2": 0.5,
            "2": 2.0,
            "ℏ_q²": float(HA)**2 / float(q0)**2,
            "1/[2]_q": 1 / (float(q0) + 1/float(q0)),
            "z = 1/(q^½+q^-½)": 1 / (float(q0)**0.5 + float(q0)**(-0.5)),
            "2z": 2 / (float(q0)**0.5 + float(q0)**(-0.5)),
            "1/(1+q·H_A)": 1 / (1 + float(q0) * float(HA)),
            "(A=1)": 1.0 if (Z+N) == 1 else 0.0,
        }
        best_match = ("none", float("inf"))
        for label, val in candidates.items():
            if val > 0:
                diff = abs(factor / val - 1)
                if diff < best_match[1]:
                    best_match = (label, diff)

        print(f"  {name:>4} {phi_1:>+10.4f} {B_derived:>+14.4f} "
              f"{B_ame:>10.4f} {factor:>10.5f} "
              f"{best_match[0]+' ('+f'{best_match[1]*100:.1f}%)':>20}")

        norm_results.append({
            "atom": name, "Z": Z, "N": N,
            "phi_1": phi_1, "B_derived_MeV": B_derived,
            "B_AME_MeV": B_ame,
            "correction_factor": factor,
            "closest_simple": best_match[0],
            "closest_simple_err_pct": best_match[1] * 100,
        })

    # Look for a clean A-dependent pattern in the factor
    print(f"\n  correction-factor sequence: "
          f"{[r['correction_factor'] for r in norm_results]}")
    print(f"  product across atoms: "
          f"{math.prod(r['correction_factor'] for r in norm_results):.6f}")

    # Check: is factor ≈ (V_hyp / Vol_free) or similar?
    # (the derivation implicitly assumes α · Φ_1 = full binding
    # but maybe it's scaled by some topological ratio)

    witness = {
        "computation": "derivation-checks",
        "description": (
            "Two derivation-only checks:\n"
            "(1) χ_sym·χ_alt = -(1 + H_A²/4)^n_ud verified by counting "
            "ud factors in atom_braid_word_3A.\n"
            "(2) What correction factor brings α·|Φ_1| to B_AME, and is "
            "it a simple algebraic quantity?"
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "H_A_at_q0": float(HA),
        "alpha_MeV": ALPHA_MEV,
        "check_1_ud_counting": check_results,
        "check_2_norm_factor": norm_results,
    }
    out = Path(__file__).parent / "derivation-checks.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
