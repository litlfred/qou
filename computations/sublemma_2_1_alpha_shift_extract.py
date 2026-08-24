#!/usr/bin/env python3
"""
Extract α_shift(I; λ, μ, ν) values via LR-system inversion.

Sub-lemma 2.1 (`docs/audits/2026-05-04-confinement-nf-structure-forcing-proof.md`):

    χ^λ(β_1 · I · β_2)
        = Σ_{(μ,ν)}  c^λ_{μ,ν} · χ^μ(β_1) · α_shift(I; λ, μ, ν) · χ^ν(β_2).

Strategy: for each λ ⊢ 6, run K independent (β_1, β_2) braid pairs
through both:
  (a) the direct H_6 character χ^λ(β_1 · σ_2 · β_2)
  (b) the LR side Σ c^λ_{μν} χ^μ(β_1) χ^ν(β_2) · X_{μν}

where X_{μν} = α_shift(I; λ, μ, ν) are the unknowns.

Stack K = N_λ + safety_margin equations and solve the linear system
per λ. The result is the α_shift(I; λ, μ, ν) values consistent with
the empirical character data.

For (μ, ν) pairs with c^λ_{μν} > 1 (e.g. c^{(3,2,1)}_{(2,1)(2,1)} = 2),
the scalar formula doesn't hold — α_shift is matrix-valued. Such
cases are flagged for the refined Sub-lemma 2.1 statement.

Reads: lr table from sublemma_2_1_deuteron_branching.py
Output: sublemma-2-1-alpha-shift-extract.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from char_fast import chi_lambda_fast_mp  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()
from sublemma_2_1_deuteron_branching import (  # noqa: E402
    LR_TABLE_3_3_TO_6 as LR_TABLE,
    lr_coef,
    partitions_of,
)
# q_parameter.Q is a Python FLOAT; Q_MP is the mpf. chi_lambda_fast_mp's
# contract is "q_val MUST be an mpmath.mpf" — seeding it with Q makes the
# result READ as 50-digit while carrying 53 bits, which fmt() then pads.
from q_parameter import Q_MP as Q0  # noqa: E402


# ── Test braid words for β_p- and β_n-position ────────────────
# Each is a list of (c, d, gen_idx) for an H_3 element. We'll
# pair them up to generate K independent equations per λ.
def _w(*pairs):
    """Build a word from (gen_idx, c, d) tuples (default c=1, d=0)."""
    return [(c, d, g) for (g, c, d) in pairs]


# Ten distinct H_3 algebra elements (mix of pure σ words and
# c·σ + d·1 algebra elements). They span the 6-dim Hecke algebra
# H_3 well enough for system inversion.
# Hecke parameter h := q − q⁻¹ at q = Q0 (the canonical substrate
# parameter from q_parameter.Q).  Defined at module level to keep a
# single source of truth and avoid drift between this file and
# mass_at_3A_proper.HA.
H = Q0 - 1 / Q0
TEST_WORDS_H3 = [
    [],                                   # identity
    [(1.0, 0.0, 0)],                      # σ_0
    [(1.0, 0.0, 1)],                      # σ_1
    [(1.0, 0.0, 0), (1.0, 0.0, 1)],       # σ_0 σ_1
    [(1.0, 0.0, 1), (1.0, 0.0, 0)],       # σ_1 σ_0
    [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],  # σ_0 σ_1 σ_0 (trefoil)
    [(1.0, -H, 0)],                       # σ_0 - h
    [(1.0, -H/2, 1)],                     # σ_1 - h/2
    [(1.0, 0.0, 0), (1.0, -H, 1)],        # σ_0 (σ_1 - h)
    [(1.0, -H, 0), (1.0, -H/2, 1)],       # (σ_0 - h)(σ_1 - h/2)
]


def disjoint(beta1: list, beta2: list) -> list:
    """Combine β_1 (acting on H_3 generators 0,1) with β_2 (acting on
    H_6 generators 3, 4) into a disjoint H_6 word."""
    out = list(beta1)
    out += [(c, d, g + 3) for (c, d, g) in beta2]
    return out


def with_interface(beta1: list, beta2: list,
                    interface_c: float = 1.0,
                    interface_d: float = -H/2) -> list:
    """β_1 · I · β_2 in H_6 with I = c·σ_2 + d·1 (single inter-block
    crossing; default = averaged σ_2 - h/2 matching the atomic-braid
    proton-neutron interface)."""
    out = list(beta1)
    out.append((interface_c, interface_d, 2))
    out += [(c, d, g + 3) for (c, d, g) in beta2]
    return out


def build_lr_pair_index(lam: tuple, parts_3: list) -> list:
    """List the (μ, ν) pairs with c^λ_{μν} > 0, in stable order."""
    pairs = []
    for mu in parts_3:
        for nu in parts_3:
            c = lr_coef(mu, nu, lam)
            if c > 0:
                pairs.append((mu, nu, c))
    return pairs


_RESID_FLOOR = mp.mpf('1e-40')   # was 1e-12, a float64 artifact


def _serialize(o):
    """mpf -> output-precision string, recursively; exactly-integral -> int.

    Applied ONCE, at the witness boundary, so every in-script consumer still
    sees real mpf. alpha_shift's imaginary part is exactly zero on every
    solved lambda; the old float() wrote it as -0.0, putting a raw f64 in the
    witness for a value that is exactly 0.
    """
    if isinstance(o, mp.mpf):
        n = mp.floor(o)
        return int(n) if o == n else fmt(o)
    if isinstance(o, dict):
        return {k: _serialize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_serialize(v) for v in o]
    return o


def solve_alpha_shift_for_lambda(
    lam: tuple,
    test_pairs: list,
    parts_3: list,
    chi_table_p: dict, chi_table_n: dict,
    chi_table_lam_with_I: dict,
) -> dict:
    """Solve for α_shift(I; λ, μ, ν) per (μ,ν) ∈ support(c^λ).

    Returns dict with the LR pair index, system matrix, RHS, solution,
    and residuals.
    """
    pairs = build_lr_pair_index(lam, parts_3)
    if not pairs:
        return {"lambda": list(lam), "support": [], "skip": "empty support"}

    K = len(test_pairs)
    N = len(pairs)
    if K < N:
        return {"lambda": list(lam),
                "skip": f"K={K} < N={N}: not enough equations"}

    # Build system matrix: M[k, p] = c^λ_{μν} · χ^μ(β_1) · χ^ν(β_2)
    M = mp.zeros(K, N)
    rhs = mp.zeros(K, 1)
    for k, (idx_1, idx_2) in enumerate(test_pairs):
        for p, (mu, nu, c) in enumerate(pairs):
            M[k, p] = c * chi_table_p[(idx_1, mu)] * chi_table_n[(idx_2, nu)]
        rhs[k] = chi_table_lam_with_I[(idx_1, idx_2, lam)]

    # Solve in least-squares sense. mp.qr_solve is mpmath's overdetermined
    # solver — the direct analogue of np.linalg.lstsq, at full working
    # precision rather than float64.
    sol, _resid = mp.qr_solve(M, rhs)

    # Rank from the singular values: np.linalg.lstsq handed this back, mpmath
    # does not, so take it from the spectrum with an explicit tolerance.
    sv = mp.svd(M, compute_uv=False)
    sv_max = max(sv) if len(sv) else mp.mpf(0)
    rank_tol = max(K, N) * sv_max * mp.mpf('1e-40')
    rank = sum(1 for x in sv if x > rank_tol)

    # Predicted RHS using fitted α_shift
    pred = M * sol
    max_rel = mp.mpf(0)
    for k in range(K):
        denom = max(abs(rhs[k]), _RESID_FLOOR)
        r = abs(pred[k] - rhs[k]) / denom
        if r > max_rel:
            max_rel = r

    return {
        "lambda": list(lam),
        "support": [(list(mu), list(nu), int(c)) for mu, nu, c in pairs],
        "alpha_shift": {f"{list(mu)}|{list(nu)}": {
            "value_re": sol[p].real, "value_im": sol[p].imag,
            "c_lr": int(c),
        } for p, (mu, nu, c) in enumerate(pairs)},
        "rank": int(rank),
        "n_equations": K,
        "n_unknowns": N,
        "max_relative_residual": max_rel,
        "system_well_posed": rank >= N,
        "consistent_within_1e6": max_rel < mp.mpf('1e-6'),
    }


def main() -> int:
    parts_3 = partitions_of(3)
    parts_6 = partitions_of(6)

    print("=" * 96)
    print("  α_shift extraction via LR-system inversion (deuteron interface I = σ_2 - h/2)")
    print("=" * 96)

    # Pre-compute χ^μ(β) for all test words and all μ ⊢ 3
    print(f"\n  Pre-computing characters at q_0 = {mp.nstr(Q0, 7)}...")
    chi_p_tab = {}    # chi_p_tab[(test_idx, μ)] = χ^μ(test_word)
    chi_n_tab = {}    # same on n side
    chi_lam_tab = {}  # chi_lam_tab[(test_idx_1, test_idx_2, λ)] = χ^λ(β_1 · I · β_2)
    for i, w in enumerate(TEST_WORDS_H3):
        for mu in parts_3:
            chi_p_tab[(i, mu)] = chi_lambda_fast_mp(mu, w, Q0)
            chi_n_tab[(i, mu)] = chi_p_tab[(i, mu)]   # same map; placeholder
    # Compute χ^λ(β_p_test_i · I · β_n_test_j) for each pair (i, j)
    test_pairs = [(i, j) for i in range(len(TEST_WORDS_H3))
                          for j in range(len(TEST_WORDS_H3))]
    print(f"  {len(test_pairs)} test (β_1, β_2) pairs across {len(parts_6)} λ partitions...")
    for i, w1 in enumerate(TEST_WORDS_H3):
        for j, w2 in enumerate(TEST_WORDS_H3):
            comb = with_interface(w1, w2)
            for lam in parts_6:
                chi_lam_tab[(i, j, lam)] = chi_lambda_fast_mp(lam, comb, Q0)

    # Solve per λ
    print(f"\n  Per-λ α_shift extraction:")
    print(f"  {'λ ⊢ 6':<14} {'N_λ':>4} {'max c=':<8} {'rank':>5}  {'max rel res':>12}  status")
    print("  " + "-" * 76)
    results_per_lambda = {}
    overall_consistent = []
    multiplicity_geq_2 = []
    for lam in parts_6:
        support = build_lr_pair_index(lam, parts_3)
        if not support:
            print(f"  {str(lam):<14} {0:>4} {'—':<8}  {'—':>5}  {'—':>12}  empty support")
            continue
        max_c = max(c for _, _, c in support)
        if max_c >= 2:
            multiplicity_geq_2.append(lam)
        result = solve_alpha_shift_for_lambda(
            lam, test_pairs, parts_3, chi_p_tab, chi_n_tab, chi_lam_tab,
        )
        results_per_lambda[lam] = result
        if "skip" in result:
            print(f"  {str(lam):<14} {len(support):>4} {max_c:<8} {'—':>5}  {'—':>12}  {result['skip']}")
            continue
        rank = result["rank"]
        N_unk = result["n_unknowns"]
        max_rel = result["max_relative_residual"]
        if max_c >= 2:
            status = "MATRIX-VALUED (formula needs refinement)"
        elif max_rel < mp.mpf('1e-6'):
            status = "✓ scalar α_shift consistent"
            overall_consistent.append(lam)
        else:
            status = f"✗ rel res {mp.nstr(max_rel, 3)} (formula inadequate)"
        print(f"  {str(lam):<14} {N_unk:>4} {max_c:<8}  {rank:>5}  {mp.nstr(max_rel, 3):>12}  {status}")

    print(f"\n  Summary:")
    print(f"    {len(overall_consistent)} of {len(parts_6)} λ have a consistent SCALAR α_shift")
    print(f"    {len(multiplicity_geq_2)} λ have c^λ_{{μν}} ≥ 2 (matrix-valued; formula refinement)")

    # Print the extracted α_shift values for scalar-consistent cases
    print(f"\n  Extracted α_shift(I; λ, μ, ν) values (scalar-consistent λ only):")
    print(f"  {'λ':<14} {'(μ, ν)':<24} {'α_shift':<28} {'c_LR':>4}")
    print("  " + "-" * 76)
    for lam in overall_consistent:
        result = results_per_lambda[lam]
        for key, info in result["alpha_shift"].items():
            mu_str, nu_str = key.split("|")
            v_re = info["value_re"]
            v_im = info["value_im"]
            v_str = (mp.nstr(v_re, 5)
                     + (f"+{mp.nstr(v_im, 5)}i" if abs(v_im) > mp.mpf('1e-10') else ""))
            print(f"  {str(lam):<14} (({mu_str}), ({nu_str})){' '*(24-len(mu_str)-len(nu_str)-6)} {v_str:<28} {info['c_lr']:>4}")

    print(f"\n  Matrix-valued (c^λ ≥ 2) cases requiring formula refinement:")
    for lam in multiplicity_geq_2:
        support = build_lr_pair_index(lam, parts_3)
        for mu, nu, c in support:
            if c >= 2:
                print(f"    λ = {lam}, (μ, ν) = ({mu}, {nu}), c^λ = {c}")

    witness = {
        "computation": "sublemma-2-1-alpha-shift-extract",
        "description": (
            "Extracts α_shift(I; λ, μ, ν) per λ ⊢ 6 in the deuteron "
            "case (I = single inter-nucleon averaged crossing) via "
            "LR-system inversion. Runs 100 (β_1, β_2) Hecke-element "
            "test pairs to over-determine the α_shift unknowns per λ, "
            "then solves by least squares. For c^λ_{μν} = 1 cases, the "
            "scalar α_shift values are consistent with character data "
            "to ~1e-13 (machine precision). For c^λ_{μν} ≥ 2 cases "
            "(only λ = (3,2,1) for n=6), the formula is matrix-valued "
            "and requires the refined Sub-lemma 2.1 statement."
        ),
        "reference_blocks": [
            "conj:confinement-nf-structure-forcing",
            "prop:atomic-mass-gb-nf",
            "prop:alpha-shift-torus-knot",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": fmt(Q0),
            "interface": "I = σ_2 - h/2 (atomic-braid pn averaged crossing)",
            "n_test_pairs": len(test_pairs),
            "n_lambda": len(parts_6),
        },
        "results_per_lambda": {
            str(lam): results_per_lambda.get(lam, {})
            for lam in parts_6
        },
        "scalar_consistent_lambda": [list(l) for l in overall_consistent],
        "matrix_valued_lambda": [list(l) for l in multiplicity_geq_2],
        "n_scalar_consistent": len(overall_consistent),
        "n_matrix_valued": len(multiplicity_geq_2),
    }
    out = HERE / "sublemma-2-1-alpha-shift-extract.witness.json"
    out.write_text(json.dumps(_serialize(witness), indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
