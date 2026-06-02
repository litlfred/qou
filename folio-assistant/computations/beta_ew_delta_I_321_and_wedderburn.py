# archimedean_by_design: numpy-vectorized eigenvalue analysis
#   for the cot θ_W hypothesis search. Single np.exp(np.mean(np.log(pos)))
#   site at L195 computes the geometric mean of positive eigenvalues
#   of a Wedderburn aggregate — vectorized log on a numpy array is
#   the standard idiom for this; mp.log is not vectorized. The
#   eigenvalue compute itself is float64 (np.linalg eigh) so the
#   log/exp roundtrip preserves the available precision.
"""β_EW(Δ_I^minimal) deep-dive: (3,2,1) 16-dim partition + Wedderburn-
weighted Markov-trace aggregate.

Paths (b) and (c) from PR #550 follow-on:

  (b) (3,2,1) 16-dim block analysis: enumerate the 16 eigenvalues of
      β_EW(Δ_I^minimal) on V_(3,2,1); test whether they encode the
      EW-mixing matrix (W^3, B) → (Z, γ) via specific eigenvalue
      pairings or sub-block traces.

  (c) Wedderburn-weighted Markov trace: tr_M(β_EW Δ_I) =
      Σ_λ w_λ · χ^λ(β_EW Δ_I) where w_λ = dim_q(λ)² / [n]_q!.
      Recompute cot θ_W candidates using Wedderburn-weighted
      aggregates (vs the unweighted aggregates that returned NULL
      in the prior probe).

References:
  - PR #550 commit a08379190 + fdcf90354 (numerical Δ_I spectrum)
  - hecke_character_symbolic.py (PR #546, on main)
  - def:ew-interface-knot, conj:hoefsmit-ew-cell-content
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
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


def beta_ew_delta_I_word():
    delta_I = [1, 3, 1]
    return [0]*4 + delta_I + [2]*6 + delta_I + [4]*8 + delta_I


def beta_ew_matrix_numerical(shape, q_0):
    matrices, dim, _ = _hoefsmit_build(list(shape), q_0)
    if dim == 0:
        return None, 0
    word = beta_ew_delta_I_word()
    M = sp.eye(dim)
    for gen_idx in word:
        M = M * matrices[gen_idx]
    return M, dim


def q_int_at(n, q_0):
    """[n]_q at q = q_0 numerical."""
    return float((q_0 ** n - q_0 ** -n) / (q_0 - 1 / q_0)) if n != 0 else 0.0


def q_factorial_at(n, q_0):
    """[n]_q! at q = q_0 numerical."""
    if n <= 0:
        return 1.0
    return q_int_at(n, q_0) * q_factorial_at(n - 1, q_0)


def dim_q_at(shape, q_0):
    """dim_q V_λ at q = q_0 (q-deformed Specht dimension via hook formula)."""
    n = sum(shape)
    # hook lengths
    hooks = []
    rows = list(shape)
    cols_with_count = [0] * max(rows)
    for r, length in enumerate(rows):
        for c in range(length):
            cols_with_count[c] += 1
    for r, length in enumerate(rows):
        for c in range(length):
            arm = length - c - 1
            leg = cols_with_count[c] - r - 1
            hook = arm + leg + 1
            hooks.append(hook)
    # dim_q = [n]_q! / prod_{x in λ} [h_x]_q
    num = q_factorial_at(n, q_0)
    den = 1.0
    for h in hooks:
        den *= q_int_at(h, q_0)
    return num / den


def main() -> int:
    n = 6
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)
    q_0_float = float(q_0)

    print(f"β_EW(Δ_I^minimal) deep-dive at q_0 ≈ {q_0_float:.10f}")
    print(f"  Word: {beta_ew_delta_I_word()}")
    print()

    parts = partitions_of(n)

    # ── Part (b): (3,2,1) 16-dim partition ──────────────────────
    shape_321 = (3, 2, 1)
    M_321, dim_321 = beta_ew_matrix_numerical(shape_321, q_0)
    M_321_np = np.array(M_321.tolist(), dtype=np.complex128)
    eigs_321 = np.linalg.eigvals(M_321_np).real  # all real
    eigs_321_sorted = sorted(eigs_321, key=lambda x: -x)

    print(f"Part (b): λ = (3,2,1), dim = {dim_321}")
    print(f"  16 eigenvalues sorted descending:")
    for i, ev in enumerate(eigs_321_sorted):
        print(f"    {i+1:>2}: {ev:>+15.6f}")
    print(f"  trace = Σ ev = {sum(eigs_321_sorted):.6f}")
    print(f"  product = Π ev = {np.prod(eigs_321_sorted):.4e}")
    print()

    # Look for structural pairings — eigenvalues that come in (a, 1/a)
    # bar-anti-self-dual pairs or (a, -a) sign-pairs
    print("  Structural pairing analysis:")
    eps = 1e-6
    pairings = []
    used = set()
    for i, ev_i in enumerate(eigs_321_sorted):
        if i in used:
            continue
        for j, ev_j in enumerate(eigs_321_sorted):
            if j <= i or j in used:
                continue
            # Bar-pair: ev_i · ev_j ≈ ±1 (geometric inversion, |ev_i| · |ev_j| = 1)
            if abs(abs(ev_i * ev_j) - 1) < eps:
                sign = "+" if ev_i * ev_j > 0 else "-"
                pairings.append(("bar", i, j, ev_i, ev_j, sign))
                used.update([i, j])
                break
            # Sign-pair: ev_i + ev_j ≈ 0
            if abs(ev_i + ev_j) < eps:
                pairings.append(("sign-flip", i, j, ev_i, ev_j, ""))
                used.update([i, j])
                break
    print(f"    Found {len(pairings)} structural pairs:")
    for kind, i, j, ev_i, ev_j, sign in pairings:
        print(f"      {kind}{sign}: ({i+1}) {ev_i:+.4f} ↔ ({j+1}) {ev_j:+.4f}")
    print(f"    Unpaired: {dim_321 - 2*len(pairings)}")
    print()

    # CODATA
    cot_codata = float(sp.sqrt(sp.Rational(1) - sp.Rational("0.23129"))
                       / sp.sqrt(sp.Rational("0.23129")))

    # (3,2,1) candidate cot θ_W readings
    print(f"  (3,2,1) Weinberg-angle candidates (CODATA cot θ_W = {cot_codata:.6f}):")
    candidates_321 = []
    if eigs_321_sorted:
        # H1: max / min positive
        pos = sorted([e for e in eigs_321_sorted if e > 0])
        if pos:
            h1 = pos[-1] / pos[0]
            candidates_321.append(("max+/min+", h1))
        # H2: |ev_1 / ev_dim|
        h2 = abs(eigs_321_sorted[0] / eigs_321_sorted[-1])
        candidates_321.append(("ev_1 / ev_16 (extremes)", h2))
        # H3: 8th eigenvalue (median pair)
        if len(eigs_321_sorted) >= 8:
            h3 = eigs_321_sorted[7]
            candidates_321.append(("ev_8 (median)", h3))
            h3b = abs(eigs_321_sorted[7])
            candidates_321.append(("|ev_8|", h3b))
        # H4: ratio of trace to determinant
        h4 = abs(sum(eigs_321_sorted) / np.prod(eigs_321_sorted)) \
            if np.prod(eigs_321_sorted) != 0 else float("inf")
        candidates_321.append(("|trace/det|", h4))
        # H5: ratio of largest two positive eigenvalues
        if len(pos) >= 2:
            h5 = pos[-1] / pos[-2]
            candidates_321.append(("max+/2nd-max+", h5))
        # H6: log-mean of positive eigenvalues
        if pos:
            log_mean_pos = np.exp(np.mean(np.log(pos)))
            candidates_321.append(("geometric mean of positive evs", log_mean_pos))

    for name, val in candidates_321:
        rel_err = abs(val - cot_codata) / cot_codata
        flag = "★" if rel_err < 0.001 else ("·" if rel_err < 0.01 else " ")
        print(f"    {flag} {name:<45} {val:>14.6f} {rel_err*100:>9.2f}%")
    print()

    best_321 = min(candidates_321, key=lambda x: abs(x[1] - cot_codata))
    print(f"  Best (3,2,1): {best_321[0]} = {best_321[1]:.6f}")
    print(f"    rel err = {abs(best_321[1] - cot_codata)/cot_codata*100:.4f}%")
    print()

    # ── Part (c): Wedderburn-weighted Markov trace ──────────────
    print("Part (c): Wedderburn-weighted Markov trace")
    print(f"  w_λ = dim_q(λ)² / [{n}]_q!")
    print(f"  [{n}]_q! at q_0 = {q_factorial_at(n, q_0):.6f}")
    print()

    fact_n = q_factorial_at(n, q_0)
    per_partition = []
    for shape in parts:
        f_lambda = len(standard_young_tableaux(shape)[0])
        if f_lambda == 0:
            continue
        M, dim = beta_ew_matrix_numerical(shape, q_0)
        chi = float(M.trace())
        d_q = dim_q_at(shape, q_0)
        w = d_q ** 2 / fact_n
        per_partition.append({
            "shape": list(shape),
            "f_lambda": dim,
            "chi": chi,
            "dim_q": d_q,
            "w_lambda": w,
            "w_chi": w * chi,
        })
        print(f"  λ = {str(shape):<15} dim_q = {d_q:>10.6f}  w_λ = "
              f"{w:>10.6f}  w · χ^λ = {w*chi:>+15.6f}")

    tr_M_total = sum(p["w_chi"] for p in per_partition)
    print()
    print(f"  Markov trace tr_M(β_EW Δ_I) = Σ w_λ · χ^λ ≈ {tr_M_total:.6f}")
    print()

    # Wedderburn-weighted candidate readings
    print(f"  Wedderburn-weighted Weinberg-angle candidates "
          f"(CODATA cot θ_W = {cot_codata:.6f}):")
    candidates_w = []

    # H1: ratio of positive-weighted to negative-weighted contributions
    pos_w = sum(p["w_chi"] for p in per_partition if p["w_chi"] > 0)
    neg_w = sum(p["w_chi"] for p in per_partition if p["w_chi"] < 0)
    if neg_w != 0:
        candidates_w.append(("|Σ_{wχ>0} / Σ_{wχ<0}|", abs(pos_w / neg_w)))

    # H2: full tr_M / leading w·χ
    leading = max(per_partition, key=lambda p: abs(p["w_chi"]))
    candidates_w.append(("tr_M / max|w·χ|", abs(tr_M_total / leading["w_chi"])))

    # H3: tr_M / (2 · χ^(6) w_(6))  — invariant-normalized
    row = next(p for p in per_partition if tuple(p["shape"]) == (6,))
    candidates_w.append(("tr_M / (2·w_(6)·χ^(6))",
                        abs(tr_M_total / (2 * row["w_chi"]))))

    # H4: cot θ_W = sqrt(tr_M_pos / tr_M_neg)
    if neg_w != 0:
        candidates_w.append(("sqrt(|Σ_pos / Σ_neg|)",
                            abs(pos_w / neg_w) ** 0.5))

    # H5: tr_M / Σ |w·χ|
    sum_abs = sum(abs(p["w_chi"]) for p in per_partition)
    if sum_abs != 0:
        candidates_w.append(("|tr_M| / Σ |w·χ|", abs(tr_M_total) / sum_abs))

    # H6: ratio of pos sum to total (a "polarisation" reading)
    if tr_M_total != 0:
        candidates_w.append(("Σ_pos w·χ / tr_M", pos_w / tr_M_total))

    for name, val in candidates_w:
        rel_err = abs(val - cot_codata) / cot_codata
        flag = "★" if rel_err < 0.001 else ("·" if rel_err < 0.01 else " ")
        print(f"    {flag} {name:<45} {val:>14.6f} {rel_err*100:>9.2f}%")
    print()

    best_w = min(candidates_w, key=lambda x: abs(x[1] - cot_codata))
    best_w_err = abs(best_w[1] - cot_codata) / cot_codata
    print(f"  Best (Wedderburn): {best_w[0]} = {best_w[1]:.6f}")
    print(f"    rel err = {best_w_err*100:.4f}%")
    print()

    # ── Verdict ────────────────────────────────────────────────
    if best_w_err < 0.001 or abs(best_321[1] - cot_codata)/cot_codata < 0.001:
        verdict = "candidate-found-precision-1e-3"
    elif best_w_err < 0.01 or abs(best_321[1] - cot_codata)/cot_codata < 0.01:
        verdict = "near-miss-precision-1e-2"
    elif best_w_err < 0.05 or abs(best_321[1] - cot_codata)/cot_codata < 0.05:
        verdict = "near-miss-precision-5pct"
    else:
        verdict = "no-clean-fit"
    print(f"VERDICT: {verdict}")

    out = {
        "computation": "beta-ew-delta-I-321-and-wedderburn",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Deep-dive of β_EW(Δ_I^minimal) on H_6(q): (b) (3,2,1) "
            "16-dim partition spectrum + structural pairing analysis; "
            "(c) Wedderburn-weighted Markov trace tr_M = Σ w_λ · χ^λ "
            "with w_λ = dim_q(λ)²/[6]_q! and re-tested Weinberg-angle "
            "candidate readings."
        ),
        "reference_blocks": [
            "def:ew-interface-knot",
            "conj:hoefsmit-ew-cell-content",
            "conj:weinberg-angle-categorical",
        ],
        "audit": "docs/audits/2026-05-06-delta-I-interface-knot-refinement.md",
        "n_strands": n,
        "delta_I": "σ_2 · σ_4 · σ_2",
        "q_0": str(q_0),
        "part_b_321_eigenvalues": [float(x) for x in eigs_321_sorted],
        "part_b_pairings": [
            {"kind": kind, "i": i + 1, "j": j + 1,
             "ev_i": ev_i, "ev_j": ev_j, "sign": sign}
            for kind, i, j, ev_i, ev_j, sign in pairings
        ],
        "part_b_n_pairs": len(pairings),
        "part_b_n_unpaired": dim_321 - 2 * len(pairings),
        "part_b_candidates": [
            {"form": name, "value": val,
             "rel_err": abs(val - cot_codata) / cot_codata}
            for name, val in candidates_321
        ],
        "part_b_best": {"form": best_321[0], "value": best_321[1],
                        "rel_err": abs(best_321[1] - cot_codata) / cot_codata},
        "part_c_per_partition": per_partition,
        "part_c_tr_M_total": tr_M_total,
        "part_c_candidates": [
            {"form": name, "value": val,
             "rel_err": abs(val - cot_codata) / cot_codata}
            for name, val in candidates_w
        ],
        "part_c_best": {"form": best_w[0], "value": best_w[1],
                        "rel_err": best_w_err},
        "codata_cot_theta_W": cot_codata,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "beta-ew-delta-I-321-and-wedderburn.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
