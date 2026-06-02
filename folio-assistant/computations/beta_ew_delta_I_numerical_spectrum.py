"""β_EW(Δ_I^minimal) numerical spectrum at q_0 on every partition of 6.

Numerical specialization (q := q_0 from start) avoids the symbolic
combinatorial blowup that timed out on partitions with f_λ ≥ 5.  For
each partition λ ⊢ 6:
  1. Build Hoefsmit-seminormal-form matrices ρ_λ(σ_i) numerically
     at q = q_0 (uses sympy hoefsmit_matrices_symbolic with q_0 as
     a Rational specialization — bypasses the cached symbolic path).
  2. Multiply matrices to form β_EW(Δ_I^minimal) numerically.
  3. Compute eigenvalues numerically (via sp.Matrix.eigenvals).
  4. Test Weinberg-angle candidate readings.

Since q_0 = 1.10997859... is a real positive rational specialization,
the Hoefsmit matrices are real numerical matrices, and eigenvalues
are real or come in complex conjugate pairs.  We expect:
  - 2 real eigenvalues at q_0^27, -q_0^{-27} from b_+, b_- (1-dim invariants)
  - 18 eigenvalues from the Δ_I-mixed sub-space (real or complex pairs)
  - additional structural patterns

This probe replaces the symbolic version (timed out) with the
numerical analog.
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
    """β_EW(Δ_I^minimal) generator-index word."""
    delta_I = [1, 3, 1]
    return [0]*4 + delta_I + [2]*6 + delta_I + [4]*8 + delta_I


def beta_ew_matrix_numerical(shape, q_0):
    """Build β_EW(Δ_I^minimal) numerically at q = q_0."""
    matrices, dim, _ = _hoefsmit_build(list(shape), q_0)
    if dim == 0:
        return None, 0
    word = beta_ew_delta_I_word()
    M = sp.eye(dim)
    for gen_idx in word:
        M = M * matrices[gen_idx]
    return M, dim


def main() -> int:
    n = 6
    # sp.Float specialization (not Rational) — Rational-based matrix mult
    # blows up the numerator/denominator complexity of Hoefsmit entries
    # (~1/(1 - q^{-2c}) etc.); Float keeps each entry bounded in
    # representation and gives 50-digit numerical accuracy.
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)

    print(f"β_EW(Δ_I^minimal) numerical spectrum at q_0 ≈ {float(q_0):.10f}")
    print(f"  Word: {beta_ew_delta_I_word()}")
    print()

    parts = partitions_of(n)
    per_partition = []
    all_eigenvalues = []  # (shape, eigenvalue_real, eigenvalue_imag, multiplicity)

    for shape in parts:
        f_lambda = len(standard_young_tableaux(shape)[0])
        if f_lambda == 0:
            continue
        t0 = time.time()
        M, dim = beta_ew_matrix_numerical(shape, q_0)
        elapsed_build = time.time() - t0

        # Numerical trace + det
        chi = float(M.trace())
        det = float(M.det())

        # Numerical eigenvalues via numpy.linalg.eigvals — fast and works
        # on Float matrices (sympy.Matrix.eigenvals requires exact
        # arithmetic).  Convert sympy Matrix to numpy float64 array.
        t0 = time.time()
        M_np = np.array(M.tolist(), dtype=np.complex128)
        eigs = np.linalg.eigvals(M_np)
        elapsed_evs = time.time() - t0

        evs_list = []
        for ev in eigs:
            evs_list.append({
                "real": float(ev.real),
                "imag": float(ev.imag),
                "multiplicity": 1,
            })
            all_eigenvalues.append((shape, complex(ev), 1))

        print(f"  λ = {shape}, dim = {dim}, χ^λ = {chi:.4f}, "
              f"det = {det:.3e}, build {elapsed_build:.2f}s, "
              f"evs {elapsed_evs:.2f}s")

        per_partition.append({
            "shape": list(shape),
            "f_lambda": dim,
            "chi_at_q0": chi,
            "det_at_q0": det,
            "eigenvalues": evs_list,
        })

    print()
    print(f"Total eigenvalues across all partitions: "
          f"{sum(p['f_lambda'] for p in per_partition)}")
    print()

    # Identify the 2 invariant eigenvalues (q^27 and -q^{-27})
    expected_plus = float(q_0 ** 27)
    expected_minus = -float(q_0 ** -27)
    print(f"Expected invariants: {expected_plus:.4f}, {expected_minus:.4f}")
    invariants_found = []
    for shape, ev, mult in all_eigenvalues:
        if abs(ev.imag) < 1e-9 and abs(ev.real - expected_plus) < 1e-6:
            invariants_found.append(("b_+ (q^27)", shape, ev.real))
        elif abs(ev.imag) < 1e-9 and abs(ev.real - expected_minus) < 1e-6:
            invariants_found.append(("b_- (-q^-27)", shape, ev.real))
    print(f"Invariants found: {len(invariants_found)}")
    for name, shape, val in invariants_found:
        print(f"  {name} in λ = {shape}: {val:.6f}")
    print()

    # Aggregate: separate real eigenvalues from complex pairs
    real_evs = [(s, ev.real) for s, ev, m in all_eigenvalues
                if abs(ev.imag) < 1e-9]
    complex_evs = [(s, ev) for s, ev, m in all_eigenvalues
                   if abs(ev.imag) >= 1e-9]
    print(f"Real eigenvalues: {len(real_evs)}; Complex eigenvalues: "
          f"{len(complex_evs)}")
    print()

    # Find the eigenvalues by magnitude
    real_evs_sorted = sorted(real_evs, key=lambda x: -abs(x[1]))
    print("Top 10 real eigenvalues by |magnitude|:")
    for s, v in real_evs_sorted[:10]:
        print(f"  λ = {s}: {v:>15.6f}  (|·| = {abs(v):.4e})")
    print()

    # CODATA target
    cot_codata = float(sp.sqrt(sp.Rational(1) - sp.Rational("0.23129"))
                       / sp.sqrt(sp.Rational("0.23129")))

    # Candidate Weinberg-angle readings using full numerical spectrum
    candidates = []

    # H1: ratio of largest positive to smallest positive real eigenvalue
    pos_real = sorted([v for s, v in real_evs if v > 0])
    if pos_real:
        h1 = max(pos_real) / min(pos_real)
        candidates.append((f"max/min positive real eigval", h1))

    # H2: |χ^(6) / χ^(1^6)|
    if per_partition:
        row = next((p for p in per_partition if tuple(p["shape"]) == (6,)), None)
        col = next((p for p in per_partition if tuple(p["shape"]) == (1,)*6), None)
        if row and col:
            h2 = abs(row["chi_at_q0"] / col["chi_at_q0"]) if col["chi_at_q0"] != 0 else float("inf")
            candidates.append(("|χ^(6) / χ^(1^6)|", h2))

    # H3: sum of |real eigenvalues| / sum of |complex eigenvalues real part|
    real_abs_sum = sum(abs(v) for s, v in real_evs)
    complex_abs_sum = sum(abs(ev.real) for s, ev in complex_evs)
    if complex_abs_sum > 0:
        h3 = real_abs_sum / complex_abs_sum
        candidates.append(("Σ|real ev|/Σ|complex ev real part|", h3))

    # H4: 18-tableau-mixed sub-space — the eigenvalues that are NEITHER
    #     b_+ nor b_-. cot θ_W candidate via their structure:
    mixed_evs = [(s, ev) for s, ev, m in all_eigenvalues
                 if not (abs(ev.imag) < 1e-9
                         and (abs(ev.real - expected_plus) < 1e-6
                              or abs(ev.real - expected_minus) < 1e-6))]
    if mixed_evs:
        # H4a: ratio of max |real| to min |real| in the mixed sub-space
        mixed_real = [(s, ev) for s, ev in mixed_evs if abs(ev.imag) < 1e-9]
        if len(mixed_real) >= 2:
            mixed_abs = sorted([abs(ev) for s, ev in mixed_real])
            h4a = mixed_abs[-1] / mixed_abs[0]
            candidates.append(("max/min |real ev| in 18-mixed", h4a))

        # H4b: number of real vs complex in mixed
        h4b = len([1 for s, ev in mixed_evs if abs(ev.imag) < 1e-9])
        # not a Weinberg candidate, just a count

    # H5: Markov-trace style aggregate
    # tr_M(β_EW Δ_I) ≈ Σ_λ dim_q(λ) · χ^λ / [n]_q!
    # For the corrected reading, use the 11-dim per-partition data
    sum_chi_unweighted = sum(p["chi_at_q0"] for p in per_partition)
    sum_chi_weighted = sum(p["chi_at_q0"] * p["f_lambda"] for p in per_partition)
    candidates.append(("|sum χ^λ unweighted|", abs(sum_chi_unweighted)))
    candidates.append(("|sum χ^λ · f_λ|", abs(sum_chi_weighted)))

    # H6: Try ratio of (sum positive / sum negative) at q_0
    pos_sum = sum(p["chi_at_q0"] for p in per_partition if p["chi_at_q0"] > 0)
    neg_sum = sum(p["chi_at_q0"] for p in per_partition if p["chi_at_q0"] < 0)
    if neg_sum != 0:
        h6 = abs(pos_sum / neg_sum)
        candidates.append(("|Σ_{χ>0} χ^λ / Σ_{χ<0} χ^λ|", h6))

    print(f"Candidate cot θ_W readings (CODATA target {cot_codata:.6f}):")
    print(f"  {'form':<55} {'value':>14} {'rel err':>10}")
    print("  " + "-" * 80)
    for name, val in candidates:
        rel_err = abs(val - cot_codata) / cot_codata
        flag = "★" if rel_err < 0.001 else ("·" if rel_err < 0.05 else " ")
        print(f"  {flag} {name:<55} {val:>14.4f} {rel_err*100:>9.2f}%")
    print()

    best = min(candidates, key=lambda x: abs(x[1] - cot_codata))
    best_err = abs(best[1] - cot_codata) / cot_codata
    print(f"  Best: {best[0]}")
    print(f"    value     = {best[1]:.6f}")
    print(f"    CODATA    = {cot_codata:.6f}")
    print(f"    rel err   = {best_err*100:.4f}%")

    if best_err < 1e-3:
        verdict = "candidate-found-precision-1e-3"
    elif best_err < 0.01:
        verdict = "near-miss-precision-1e-2"
    elif best_err < 0.05:
        verdict = "near-miss-precision-5pct"
    else:
        verdict = "no-clean-fit"

    print(f"VERDICT: {verdict}")

    out = {
        "computation": "beta-ew-delta-I-numerical-spectrum",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Numerical-at-q_0 spectrum extraction of β_EW(Δ_I^minimal) "
            "across all 11 partitions of 6, using PR #546's "
            "_hoefsmit_build directly at q = q_0 = Rational specialization. "
            "Avoids the symbolic-q combinatorial blowup that timed out on "
            "partitions with f_λ ≥ 5.  Tests Weinberg-angle candidate "
            "readings using the full Δ_I-coupled spectrum + invariants."
        ),
        "reference_blocks": [
            "def:ew-interface-knot",
            "conj:hoefsmit-ew-cell-content",
            "conj:weinberg-angle-categorical",
            "conj:categorical-linking-operation",
        ],
        "audit": "docs/audits/2026-05-06-delta-I-interface-knot-refinement.md",
        "n_strands": n,
        "delta_I": "σ_2 · σ_4 · σ_2",
        "beta_EW_word_indices": beta_ew_delta_I_word(),
        "q_0": str(q_0),
        "per_partition": per_partition,
        "invariants_found": [
            {"name": name, "shape": list(shape), "value": val}
            for name, shape, val in invariants_found
        ],
        "n_real_eigenvalues": len(real_evs),
        "n_complex_eigenvalues": len(complex_evs),
        "candidate_cot_theta_W_readings": [
            {"form": name, "value": val,
             "rel_err": abs(val - cot_codata) / cot_codata}
            for name, val in candidates
        ],
        "best": {"form": best[0], "value": best[1], "rel_err": best_err},
        "codata_cot_theta_W": cot_codata,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "beta-ew-delta-I-numerical-spectrum.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
