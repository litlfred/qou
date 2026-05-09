"""β_EW(Δ_I^minimal) bar-pair structure across ALL partitions of 6.

Verifies whether the structural finding from the (3,2,1) deep-dive
(all 16 eigenvalues form 8 bar-pairs with ev_i · ev_j = -1)
generalises to every partition λ ⊢ 6.

If yes: a strong structural claim — β_EW(Δ_I^minimal) acts on every
Wedderburn block V_λ as an SL(V_λ) element with bar-anti-self-dual
spectrum.  This is the categorical-physics realisation of:

  - Property 5 of conj:categorical-linking-operation (bar-involution
    compatibility);
  - The QOU substrate's bar T-duality;
  - The Higgs-vev coupling preserving SL-structure (mass eigenvalues
    come in (m, 1/m)-style pairs at the categorical level).

For each partition:
  1. Compute β_EW(Δ_I^minimal) numerically at q_0.
  2. Extract eigenvalues.
  3. Identify bar-pairs (ev_i · ev_j = ±1).
  4. Report: # paired, # unpaired, det(M), trace(M).

If det(M_λ) = ±1 for ALL λ, then β_EW(Δ_I^minimal) is an SL/PSL
(or O/SO)-element category-wise.

Generalisation:
  - Test β_EW(Δ_I) for alternative Δ_I words (σ_2 σ_3 σ_4, σ_2² σ_4²)
  - Test arbitrary even-twist words ∏ σ_{i_k}^{2 n_k}
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from hecke_character_symbolic import (
    standard_young_tableaux, _hoefsmit_build,
)


def partitions_of(n):
    if n == 0:
        return [()]
    result = []

    def gen(remaining, max_part, current):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            current.append(p)
            gen(remaining - p, p, current)
            current.pop()
    gen(n, n, [])
    return result


def beta_ew_delta_I_word(delta_I=None):
    """β_EW(Δ_I) word: σ_1^4 · Δ_I · σ_3^6 · Δ_I · σ_5^8 · Δ_I.
    Default Δ_I = σ_2 σ_4 σ_2 = [1, 3, 1]."""
    if delta_I is None:
        delta_I = [1, 3, 1]
    return [0]*4 + delta_I + [2]*6 + delta_I + [4]*8 + delta_I


def beta_matrix_numerical(shape, q_0, word):
    matrices, dim, _ = _hoefsmit_build(list(shape), q_0)
    if dim == 0:
        return None, 0
    M = sp.eye(dim)
    for gen_idx in word:
        M = M * matrices[gen_idx]
    return M, dim


def find_bar_pairs(eigs, eps=1e-6):
    """Identify eigenvalues that pair up via ev_i · ev_j ≈ ±1."""
    n = len(eigs)
    used = set()
    pairs_minus = []  # ev_i · ev_j ≈ -1
    pairs_plus = []   # ev_i · ev_j ≈ +1
    for i in range(n):
        if i in used:
            continue
        for j in range(i + 1, n):
            if j in used:
                continue
            prod = eigs[i] * eigs[j]
            if abs(prod + 1) < eps:
                pairs_minus.append((i, j, eigs[i], eigs[j]))
                used.update([i, j])
                break
            elif abs(prod - 1) < eps:
                pairs_plus.append((i, j, eigs[i], eigs[j]))
                used.update([i, j])
                break
    unpaired = [i for i in range(n) if i not in used]
    return pairs_minus, pairs_plus, unpaired


def main() -> int:
    n = 6
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)
    parts = partitions_of(n)

    print(f"β_EW(Δ_I) bar-pair structure across all 11 partitions of {n}")
    print(f"  q_0 ≈ {float(q_0):.10f}")
    print()

    # Test multiple Δ_I candidates
    delta_I_candidates = [
        ("σ_2 σ_4 σ_2 (minimal)",        [1, 3, 1]),
        ("σ_2 σ_3 σ_4 (sequential)",     [1, 2, 3]),
        ("σ_2² σ_4² (paired-square)",    [1, 1, 3, 3]),
        ("σ_4 σ_2 σ_4 (mirror)",         [3, 1, 3]),
        ("trivial (Δ_I = 1)",            []),
    ]

    all_results = {}
    for delta_name, delta_I in delta_I_candidates:
        print(f"=== Δ_I = {delta_name} (word indices: {delta_I}) ===")
        word = beta_ew_delta_I_word(delta_I)
        per_partition = []
        total_pairs_minus = 0
        total_pairs_plus = 0
        total_unpaired = 0
        total_dets_pm1 = 0
        total_partitions_with_universal_pairing = 0

        for shape in parts:
            f_lambda = len(standard_young_tableaux(shape)[0])
            if f_lambda == 0:
                continue
            M, dim = beta_matrix_numerical(shape, q_0, word)
            M_np = np.array(M.tolist(), dtype=np.complex128)
            eigs_complex = np.linalg.eigvals(M_np)
            # All real (verified in prior probe)
            eigs = sorted(eigs_complex.real, key=lambda x: -x)
            det = float(M.det())
            trace = float(M.trace())

            pairs_minus, pairs_plus, unpaired = find_bar_pairs(eigs)
            n_pm = len(pairs_minus)
            n_pp = len(pairs_plus)
            n_u = len(unpaired)

            # Universal pairing = all evs paired (+1 or -1 product)
            universal_pair = (n_u == 0)
            if universal_pair:
                total_partitions_with_universal_pairing += 1

            # det near ±1
            det_pm1 = abs(abs(det) - 1) < 1e-3
            if det_pm1:
                total_dets_pm1 += 1

            total_pairs_minus += n_pm
            total_pairs_plus += n_pp
            total_unpaired += n_u

            print(f"  λ = {str(shape):<20} dim={dim:>2} pairs(-)={n_pm:>2} "
                  f"pairs(+)={n_pp:>2} unpaired={n_u:>2}  "
                  f"det={det:>+12.6f}  trace={trace:>+12.6f}"
                  f"{'  ✓' if universal_pair else ''}")

            per_partition.append({
                "shape": list(shape),
                "dim": dim,
                "pairs_minus": n_pm,
                "pairs_plus": n_pp,
                "unpaired": n_u,
                "universal_pair": universal_pair,
                "det": det,
                "trace": trace,
                "eigenvalues": [float(x) for x in eigs],
            })

        print(f"  TOTALS: pairs(-)={total_pairs_minus}  pairs(+)={total_pairs_plus}  "
              f"unpaired={total_unpaired}")
        print(f"  Universal-pairing partitions: "
              f"{total_partitions_with_universal_pairing}/11")
        print(f"  |det| ≈ 1 partitions: {total_dets_pm1}/11")
        print()

        all_results[delta_name] = {
            "delta_I_word": delta_I,
            "totals": {
                "pairs_minus": total_pairs_minus,
                "pairs_plus": total_pairs_plus,
                "unpaired": total_unpaired,
                "universal_pairing_partitions": total_partitions_with_universal_pairing,
                "det_near_pm1_partitions": total_dets_pm1,
            },
            "per_partition": per_partition,
        }

    # Verdict: does any Δ_I give universal bar-pairing across ALL 11 partitions?
    print("=" * 72)
    print("UNIVERSALITY ANALYSIS")
    print("=" * 72)
    universally_paired_deltas = [
        name for name, r in all_results.items()
        if r["totals"]["universal_pairing_partitions"] == 11
    ]
    sl_deltas = [
        name for name, r in all_results.items()
        if r["totals"]["det_near_pm1_partitions"] == 11
    ]
    print(f"Δ_I with universal bar-pairing on ALL 11 partitions: "
          f"{len(universally_paired_deltas)} of {len(delta_I_candidates)}")
    for name in universally_paired_deltas:
        print(f"  ✓ {name}")
    print()
    print(f"Δ_I with |det| ≈ 1 on ALL 11 partitions (SL-element): "
          f"{len(sl_deltas)} of {len(delta_I_candidates)}")
    for name in sl_deltas:
        print(f"  ✓ {name}")
    print()

    # Recursive structure hint: trace pattern across partitions
    # If trace(β_EW Δ_I on V_λ) follows a clean recursion on shape, that's
    # a closed-form predictor.
    print("Trace/det pattern (Δ_I^minimal):")
    minimal = all_results["σ_2 σ_4 σ_2 (minimal)"]
    for entry in minimal["per_partition"]:
        s = tuple(entry["shape"])
        chi = entry["trace"]
        det = entry["det"]
        print(f"  λ = {str(s):<20} χ^λ = {chi:>+10.4f}  det = {det:>+10.4f}")

    out = {
        "computation": "beta-ew-delta-I-bar-pair-universality",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Bar-pair structural universality of β_EW(Δ_I) across all 11 "
            "partitions of 6 and across multiple Δ_I candidates.  Tests "
            "whether the (3,2,1) finding (all 16 eigenvalues form 8 "
            "bar-anti-self-dual pairs ev_i · ev_j = -1) generalises:"
            "(i) to every partition under the same Δ_I^minimal; "
            "(ii) to alternative Δ_I words.  Verdict identifies which "
            "Δ_I gives universal bar-pairing + det = ±1 (SL-element)."
        ),
        "reference_blocks": [
            "def:ew-interface-knot",
            "conj:hoefsmit-ew-cell-content",
            "conj:categorical-linking-operation",
            "conj:weinberg-angle-categorical",
        ],
        "audit": "docs/audits/2026-05-06-bar-pair-universality.md",
        "n_strands": n,
        "q_0": str(q_0),
        "delta_I_candidates": list(all_results.keys()),
        "universally_paired_deltas": universally_paired_deltas,
        "sl_element_deltas": sl_deltas,
        "by_delta_I": all_results,
    }
    out_path = Path(__file__).parent / "beta-ew-delta-I-bar-pair-universality.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
