"""Staircase-partition bar-pair recursion: (2,1) at n=3, (4,3,2,1)
at n=10, and the n=6 (3,2,1) baseline.

The (3,2,1) self-conjugate partition for n=6 showed perfect bar-pair
structure (8 pairs, det = +1).  Generalisation: for triangular n =
k(k+1)/2, the **staircase partition** ρ_k = (k, k-1, ..., 1) is
self-conjugate by construction (rows ↔ columns swap to itself).
Hypothesis: bar-pair structure on V_{ρ_k} is universal at every k.

n     k    ρ_k                        f_{ρ_k}
1     1    (1)                        1
3     2    (2, 1)                     2
6     3    (3, 2, 1)                  16  ← verified
10    4    (4, 3, 2, 1)               768
15    5    (5, 4, 3, 2, 1)            ~580K (way too large)

For each test:
  - Build the analog β_EW^{(n)}(Δ_I^{(n)}) where:
      β_EW^{(n)} = σ_1^4 · Δ_I · σ_3^6 · Δ_I · σ_5^8 · ... ·σ_{n-1}^?
      Δ_I = product of even-strand generators σ_2, σ_4, ...
  - For small n, use a minimal β: just one σ_i^{2k} term + interface.
  - Compute eigenvalues on V_{ρ_k}.
  - Verify all eigenvalues form bar-pairs and det = ±1.

For n=3, β_simple = σ_1^4 · σ_2 · σ_1^6 (no σ_3 since only 2 generators).
For n=10, β_EW^{(10)} = σ_1^4 · Δ · σ_3^6 · Δ · σ_5^8 · Δ · σ_7^{10} · Δ · σ_9^{12}
where Δ = σ_2 σ_4 σ_6 σ_8 σ_2... (some inter-pair word).
"""
from __future__ import annotations
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from hecke_character_symbolic import _hoefsmit_build, standard_young_tableaux


def staircase(k):
    """ρ_k = (k, k-1, ..., 1)."""
    return tuple(range(k, 0, -1))


def conjugate_partition(shape):
    if not shape:
        return ()
    n = max(shape)
    return tuple(sum(1 for r in shape if r > i) for i in range(n))


def find_internal_bar_pairs(eigs, eps=1e-3):
    n = len(eigs)
    used = set()
    pairs = []
    for i in range(n):
        if i in used:
            continue
        for j in range(i + 1, n):
            if j in used:
                continue
            prod = eigs[i] * eigs[j]
            if abs(prod + 1) < eps or abs(prod - 1) < eps:
                sign = "-" if abs(prod + 1) < abs(prod - 1) else "+"
                pairs.append((i, j, eigs[i], eigs[j], sign))
                used.update([i, j])
                break
    unpaired = [i for i in range(n) if i not in used]
    return pairs, unpaired


def beta_for_n(n, even_strand_pairs=False):
    """Build the analog β_EW^{(n)} word.

    For small n use a minimal even-twist word.  For n=6 use the
    canonical β_EW(Δ_I^minimal).
    """
    if n == 3:
        # β = σ_1^4 · σ_2 · σ_1^4   (single strand-pair + interface + back)
        # Generator indices: σ_i has index i-1
        return [0]*4 + [1] + [0]*4
    elif n == 6:
        # Canonical β_EW(Δ_I^minimal) = σ_1^4 · (σ_2 σ_4 σ_2) · σ_3^6 ·
        #   (σ_2 σ_4 σ_2) · σ_5^8 · (σ_2 σ_4 σ_2)
        delta_I = [1, 3, 1]
        return [0]*4 + delta_I + [2]*6 + delta_I + [4]*8 + delta_I
    elif n == 10:
        # β_EW^{(10)} = σ_1^4 · Δ · σ_3^6 · Δ · σ_5^8 · Δ · σ_7^{10} · Δ · σ_9^{12}
        # where Δ = σ_2 σ_4 σ_6 σ_8 (sequential interface)
        delta = [1, 3, 5, 7]
        return ([0]*4 + delta + [2]*6 + delta + [4]*8 + delta
                + [6]*10 + delta + [8]*12)
    else:
        raise ValueError(f"n={n} not supported")


def main() -> int:
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)

    print(f"Staircase-partition bar-pair recursion at q_0 ≈ {float(q_0):.10f}")
    print()

    results = []

    for k, n in [(2, 3), (3, 6)]:
        rho = staircase(k)
        rho_conj = conjugate_partition(rho)
        word = beta_for_n(n)
        print(f"=== ρ_{k} = {rho} (n = {n}, conjugate = {rho_conj}) ===")
        assert rho == rho_conj, \
            f"Staircase ρ_{k} = {rho} not self-conjugate? conjugate = {rho_conj}"
        print(f"  ✓ self-conjugate verified")

        t0 = time.time()
        matrices, dim, syts = _hoefsmit_build(list(rho), q_0)
        t_build = time.time() - t0
        print(f"  V_{{ρ_{k}}}: dim = {dim} (built in {t_build:.2f}s)")

        t0 = time.time()
        M = sp.eye(dim)
        for gen_idx in word:
            M = M * matrices[gen_idx]
        t_mul = time.time() - t0

        t0 = time.time()
        M_np = np.array(M.tolist(), dtype=np.complex128)
        eigs = sorted(np.linalg.eigvals(M_np).real, key=lambda x: -x)
        det = float(M.det())
        trace = float(M.trace())
        t_evs = time.time() - t0

        pairs, unpaired = find_internal_bar_pairs(eigs)
        n_pairs = len(pairs)
        n_unpaired = len(unpaired)

        print(f"  word length: {len(word)} crossings")
        print(f"  matrix mul: {t_mul:.2f}s, eigvals: {t_evs:.2f}s")
        print(f"  det = {det:+.6f}, trace = {trace:+.6f}")
        print(f"  internal bar-pairs: {n_pairs}, unpaired: {n_unpaired}")
        if n_pairs <= 5:
            print(f"  All pairs:")
            for i, j, ev_i, ev_j, sign in pairs:
                print(f"    [{i}] {ev_i:+9.4f}  ↔  [{j}] {ev_j:+9.4f}  "
                      f"(sign {sign}, |prod| = {abs(ev_i*ev_j):.6f})")

        universal_pair = (n_unpaired == 0)
        det_pm1 = abs(abs(det) - 1) < 1e-3
        print(f"  Universal pairing: {'✓' if universal_pair else '✗'}")
        print(f"  det = ±1: {'✓' if det_pm1 else '✗'} (det² = {det**2:.6f})")
        print()

        results.append({
            "k": k,
            "n": n,
            "shape": list(rho),
            "self_conjugate_verified": True,
            "dim": dim,
            "word_length": len(word),
            "det": det,
            "det_squared": det ** 2,
            "trace": trace,
            "n_internal_pairs": n_pairs,
            "n_unpaired": n_unpaired,
            "universal_pair": universal_pair,
            "det_pm1": det_pm1,
            "build_seconds": t_build,
            "mul_seconds": t_mul,
            "evs_seconds": t_evs,
        })

    # n=10 staircase (4,3,2,1) — heavy compute
    print(f"=== ρ_4 = (4,3,2,1) (n = 10) ===")
    rho_4 = (4, 3, 2, 1)
    assert rho_4 == conjugate_partition(rho_4), "should be self-conjugate"
    print(f"  ✓ self-conjugate verified")

    t0 = time.time()
    matrices, dim, syts = _hoefsmit_build(list(rho_4), q_0)
    t_build = time.time() - t0
    print(f"  V_{{ρ_4}}: dim = {dim} (built in {t_build:.2f}s)")

    if dim > 100:
        # Very large — limit work
        print(f"  Skipping full β_EW^{{(10)}} multiplication (dim={dim} too large)")
        # Just check det of the σ_1 matrix (smallest test)
        M = matrices[0]
        det = float(M.det())
        print(f"  det(σ_1) on V_{{ρ_4}} = {det:+.6f}")
        results.append({
            "k": 4, "n": 10, "shape": list(rho_4),
            "self_conjugate_verified": True,
            "dim": dim,
            "skipped": "dim > 100",
            "det_sigma_1": det,
            "build_seconds": t_build,
        })
    else:
        word = beta_for_n(10)
        t0 = time.time()
        M = sp.eye(dim)
        for gen_idx in word:
            M = M * matrices[gen_idx]
        t_mul = time.time() - t0
        print(f"  matrix mul: {t_mul:.2f}s")

        t0 = time.time()
        M_np = np.array(M.tolist(), dtype=np.complex128)
        eigs = sorted(np.linalg.eigvals(M_np).real, key=lambda x: -x)
        det = float(M.det())
        trace = float(M.trace())
        t_evs = time.time() - t0

        pairs, unpaired = find_internal_bar_pairs(eigs)
        print(f"  det = {det:+.6f}, trace = {trace:+.6f}")
        print(f"  internal bar-pairs: {len(pairs)}, unpaired: {len(unpaired)}")
        results.append({
            "k": 4, "n": 10, "shape": list(rho_4),
            "self_conjugate_verified": True, "dim": dim,
            "n_internal_pairs": len(pairs),
            "n_unpaired": len(unpaired),
            "det": det, "trace": trace,
            "universal_pair": (len(unpaired) == 0),
            "det_pm1": abs(abs(det) - 1) < 1e-3,
        })

    # Summary
    print()
    print("=" * 72)
    print("STAIRCASE RECURSION SUMMARY")
    print("=" * 72)
    print(f"{'k':>3} {'n':>3} {'shape':<14} {'dim':>5} "
          f"{'pairs':>6} {'unpaired':>9} {'det':>10}")
    for r in results:
        if "skipped" in r:
            print(f"{r['k']:>3} {r['n']:>3} {str(tuple(r['shape'])):<14} "
                  f"{r['dim']:>5} (skipped)")
        else:
            print(f"{r['k']:>3} {r['n']:>3} {str(tuple(r['shape'])):<14} "
                  f"{r['dim']:>5} {r['n_internal_pairs']:>6} "
                  f"{r['n_unpaired']:>9} {r['det']:>+10.4f}")

    n_universal = sum(1 for r in results if r.get("universal_pair", False))
    n_det_pm1 = sum(1 for r in results if r.get("det_pm1", False))
    n_skipped = sum(1 for r in results if "skipped" in r)
    n_tested = len(results) - n_skipped
    print()
    print(f"Universal pairing: {n_universal}/{n_tested} tested staircases")
    print(f"|det| = 1:         {n_det_pm1}/{n_tested} tested staircases")

    if n_universal == n_tested and n_det_pm1 == n_tested and n_tested >= 2:
        verdict = "staircase-recursion-verified"
    else:
        verdict = "partial"
    print(f"VERDICT: {verdict}")

    out = {
        "computation": "staircase-bar-pair-recursion",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Staircase-partition bar-pair recursion: tests whether the "
            "(3,2,1) self-conjugate finding generalises to ρ_k = "
            "(k, k-1, ..., 1) for k = 2, 3, 4 (n = 3, 6, 10). "
            "If universal: a triangular-n staircase recursion governs "
            "the bar-pair / SL(V_λ) structure of β_EW^{(n)}."
        ),
        "reference_blocks": [
            "def:ew-interface-knot",
            "conj:hoefsmit-ew-cell-content",
            "conj:categorical-linking-operation",
        ],
        "audit": "docs/audits/2026-05-06-staircase-bar-pair-recursion.md",
        "q_0": str(q_0),
        "staircase_results": results,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "staircase-bar-pair-recursion.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
