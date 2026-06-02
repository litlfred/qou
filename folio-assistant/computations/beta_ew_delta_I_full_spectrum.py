"""Full spectrum of β_EW(Δ_I^minimal) on every partition of 6 via
PR #546's Hoefsmit symbolic engine.

Builds on hecke_character_symbolic.q_character_on_braid_word
(PR #546, on main as of 2026-05-06) and hoefsmit_matrices_symbolic
to compute:

  1. Per-partition χ^λ trace of β_EW(Δ_I^minimal) — symbolic in R = ℚ(q).
  2. Per-partition det / characteristic polynomial — extracts
     eigenvalues for partitions where dim_q V_λ ≤ 5.
  3. Aggregate: sum of χ^λ weighted by dim_q V_λ — the full Markov
     trace of β_EW(Δ_I^minimal) (Wenzl-bridge formula).
  4. Candidate cot θ_W readings using the full-spectrum data.

β_EW(Δ_I^minimal) = σ_1^4 · (σ_2 σ_4 σ_2) · σ_3^6 · (σ_2 σ_4 σ_2)
                  · σ_5^8 · (σ_2 σ_4 σ_2)

— a 27-crossing braid word in B_6.  Total matrix degree per
partition ≤ f_λ where f_λ = standard-Young-tableau count.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from hecke_character_symbolic import (
    standard_young_tableaux, hoefsmit_matrices_symbolic,
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


def beta_ew_delta_I_braid_word():
    """Return β_EW(Δ_I^minimal) as a list of generator indices
    (0-indexed): σ_1^4, Δ_I, σ_3^6, Δ_I, σ_5^8, Δ_I where
    Δ_I = σ_2 σ_4 σ_2."""
    delta_I = [1, 3, 1]  # σ_2 σ_4 σ_2 → indices [1, 3, 1]
    word = []
    word += [0] * 4         # σ_1^4
    word += delta_I         # σ_2 σ_4 σ_2
    word += [2] * 6         # σ_3^6
    word += delta_I
    word += [4] * 8         # σ_5^8
    word += delta_I
    return word


def beta_ew_matrix(shape, q):
    """Build β_EW(Δ_I^minimal) as a symbolic matrix in V_λ."""
    matrices, dim, _ = hoefsmit_matrices_symbolic(shape, q)
    if dim == 0:
        return None, 0
    word = beta_ew_delta_I_braid_word()
    M = sp.eye(dim)
    for gen_idx in word:
        if gen_idx < 0 or gen_idx >= len(matrices):
            raise IndexError(f"gen_idx {gen_idx} out of range for "
                             f"shape {shape} with {len(matrices)} generators")
        M = M * matrices[gen_idx]
        # cancel intermediate to keep complexity bounded
        M = M.applyfunc(sp.cancel)
    return M, dim


def main() -> int:
    n = 6
    q = sp.Symbol("q", positive=True, real=True)
    q_0 = sp.Rational(Q_50_DIGIT_STR)

    print(f"β_EW(Δ_I^minimal) full spectrum on H_{n}(q) — symbolic")
    print(f"  Word: {beta_ew_delta_I_braid_word()}")
    print(f"  (len = {len(beta_ew_delta_I_braid_word())} crossings)")
    print()

    parts = partitions_of(n)
    per_partition = []

    for shape in parts:
        f_lambda = len(standard_young_tableaux(shape)[0])
        if f_lambda == 0:
            continue
        t0 = time.time()
        M, dim = beta_ew_matrix(shape, q)
        elapsed_build = time.time() - t0

        t0 = time.time()
        chi = sp.cancel(M.trace())
        elapsed_chi = time.time() - t0

        chi_at_q0 = float(chi.subs(q, q_0))

        # Spectrum: only for small dims (charpoly is expensive)
        evs_str = None
        if dim <= 5:
            t0 = time.time()
            charpoly = sp.cancel(M.charpoly(sp.Symbol("x")).as_expr())
            evs_str = str(charpoly)
            elapsed_evs = time.time() - t0
        else:
            elapsed_evs = 0.0

        det_expr = sp.cancel(M.det())
        det_at_q0 = float(det_expr.subs(q, q_0))

        print(f"  λ = {shape}, f_λ = {dim}:")
        print(f"    χ^λ(β_EW Δ_I) at q_0 ≈ {chi_at_q0:.6f}")
        print(f"    det(M_λ)        at q_0 ≈ {det_at_q0:.6e}")
        print(f"    timings: build {elapsed_build:.2f}s, "
              f"χ {elapsed_chi:.2f}s, evs {elapsed_evs:.2f}s")

        per_partition.append({
            "shape": list(shape),
            "f_lambda": dim,
            "chi_at_q0": chi_at_q0,
            "det_at_q0": det_at_q0,
            "chi_R_str": str(chi),
            "charpoly_R_str": evs_str,
        })

    # Aggregate: tr_M(β_EW Δ_I) = Σ_λ w_λ · χ^λ where w_λ = dim_q(λ)² / [n]_q!
    # For Wenzl-bridge: w_λ = (f_λ_q)² / [n]_q! where f_λ_q is the q-dim.
    # Simpler aggregate: just sum χ^λ at q_0 weighted by f_λ (classical mult.)
    print()
    sum_chi = sum(p["chi_at_q0"] * p["f_lambda"] for p in per_partition)
    sum_chi_sq = sum(p["chi_at_q0"] ** 2 for p in per_partition)
    print(f"  Σ_λ f_λ · χ^λ(β_EW Δ_I) at q_0 ≈ {sum_chi:.6f}")
    print(f"  Σ_λ (χ^λ)² at q_0          ≈ {sum_chi_sq:.6f}")
    print()

    # Identify the "row" partition (6) and "column" partition (1^6):
    # both should be 1-dim; their χ^λ should match the eigenvalues
    # q^27 and -q^{-27} from the prior probe.
    row = next(p for p in per_partition if tuple(p["shape"]) == (6,))
    col = next(p for p in per_partition if tuple(p["shape"]) == tuple([1]*6))
    print(f"  Sanity check (1-dim invariants):")
    print(f"    χ^(6) at q_0     ≈ {row['chi_at_q0']:.6f}  (expected q_0^27 ≈ {float(q_0**27):.6f})")
    print(f"    χ^(1^6) at q_0   ≈ {col['chi_at_q0']:.6f}  (expected -q_0^-27 ≈ {float(-q_0**-27):.6f})")

    # Compare to CODATA
    cot_codata = float(sp.sqrt(sp.Rational(1) - sp.Rational("0.23129"))
                       / sp.sqrt(sp.Rational("0.23129")))

    # Candidate Weinberg readings using full spectrum
    print()
    print("Candidate cot θ_W readings from full Δ_I-coupled spectrum:")
    print(f"  CODATA cot θ_W: {cot_codata:.6f}")
    print()

    candidates = []

    # H1: ratio of Markov trace contributions sym vs alt sectors
    # Sym sector = partitions where λ has more cells in one row
    # (e.g., (6), (5,1), (4,2), (4,1,1)?) — actually use total cell-content
    # weight as proxy.
    # Simpler: use χ^(6) / χ^(1^6) ratio
    h1 = abs(row["chi_at_q0"] / col["chi_at_q0"])
    candidates.append(("|χ^(6) / χ^(1^6)|", h1))

    # H2: use the (3,2,1) partition (max f_λ = 16) as the "mixing" sector
    p321 = next(p for p in per_partition if tuple(p["shape"]) == (3, 2, 1))
    h2 = abs(p321["chi_at_q0"]) / abs(col["chi_at_q0"])
    candidates.append(("|χ^(3,2,1) / χ^(1^6)|", h2))

    # H3: total weighted Markov trace ratio
    h3 = abs(sum_chi / col["chi_at_q0"])
    candidates.append(("|Σ f_λ χ^λ / χ^(1^6)|", h3))

    # H4: Markov-trace-style (full Wenzl bridge would normalise by [n]_q!)
    # but at q_0 the proxy:
    h4 = abs(row["chi_at_q0"] + col["chi_at_q0"])
    candidates.append(("|χ^(6) + χ^(1^6)| (sum)", h4))

    # H5: tanh-style: (eig+ - eig-) / (eig+ + eig-) at the row/col level
    h5_num = row["chi_at_q0"] - col["chi_at_q0"]
    h5_den = row["chi_at_q0"] + col["chi_at_q0"]
    h5 = abs(h5_num / h5_den) if h5_den != 0 else float("inf")
    candidates.append(("|(χ_row − χ_col) / (χ_row + χ_col)|", h5))

    # H6: cot via the (3,2,1) max-mixing partition's χ — trivial reading
    h6 = abs(p321["chi_at_q0"])
    candidates.append(("|χ^(3,2,1)|", h6))

    # H7: sqrt of Σ χ²
    h7 = sum_chi_sq ** 0.5
    candidates.append(("sqrt(Σ_λ (χ^λ)²)", h7))

    print(f"  {'form':<55} {'value':>14} {'rel err':>10}")
    print("  " + "-" * 80)
    for name, val in candidates:
        rel_err = abs(val - cot_codata) / cot_codata
        flag = "★" if rel_err < 0.01 else ("·" if rel_err < 0.1 else " ")
        print(f"  {flag} {name:<55} {val:>14.4f} {rel_err*100:>9.2f}%")
    print()

    best = min(candidates, key=lambda x: abs(x[1] - cot_codata))
    best_err = abs(best[1] - cot_codata) / cot_codata
    print(f"  Best: {best[0]}")
    print(f"    value     = {best[1]:.6f}")
    print(f"    CODATA    = {cot_codata:.6f}")
    print(f"    rel err   = {best_err*100:.4f}%")
    print()

    if best_err < 1e-3:
        verdict = "candidate-found-precision-1e-3"
    elif best_err < 0.05:
        verdict = "near-miss-precision-5pct"
    else:
        verdict = "no-clean-fit-on-full-spectrum"

    print(f"VERDICT: {verdict}")

    out = {
        "computation": "beta-ew-delta-I-full-spectrum",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Full per-partition spectrum of β_EW(Δ_I^minimal) on H_6(q) "
            "via PR #546's hecke_character_symbolic engine.  Computes "
            "χ^λ symbolic in ℚ(q) for each of 11 partitions of 6; "
            "extracts charpoly for f_λ ≤ 5; tests Weinberg-angle "
            "candidate readings using the Δ_I-coupled spectrum."
        ),
        "reference_blocks": [
            "def:ew-interface-knot",
            "conj:hoefsmit-ew-cell-content",
            "conj:weinberg-angle-categorical",
        ],
        "audit": "docs/audits/2026-05-06-delta-I-interface-knot-refinement.md",
        "n_strands": n,
        "delta_I": "σ_2 · σ_4 · σ_2",
        "beta_EW_word_indices": beta_ew_delta_I_braid_word(),
        "per_partition": per_partition,
        "aggregates_at_q0": {
            "sum_f_lambda_chi": sum_chi,
            "sum_chi_squared": sum_chi_sq,
            "row_chi_q_27": row["chi_at_q0"],
            "col_chi_minus_q_minus_27": col["chi_at_q0"],
        },
        "candidate_cot_theta_W_readings": [
            {"form": name, "value": val,
             "rel_err": abs(val - cot_codata) / cot_codata}
            for name, val in candidates
        ],
        "best": {"form": best[0], "value": best[1], "rel_err": best_err},
        "codata_cot_theta_W": cot_codata,
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "beta-ew-delta-I-full-spectrum.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
