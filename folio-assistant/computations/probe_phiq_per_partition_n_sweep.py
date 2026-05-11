#!/usr/bin/env python3
"""Per-partition k_λ operator-valued Φ_q brane-tower probe — joint
PR #638 infrastructure + PR #639 per-partition rule, sweep over
non-dominant truncation depth N.

This probe is the joint deliverable across PR #638 (operator-valued
Φ_q probe at uniform k) and PR #639 (per-partition k_λ rule). Per
the cross-PR synthesis at
`docs/audits/2026-05-11-path-to-1ppb-cross-pr-synthesis.md`:

    PR #638 refuted uniform k ∈ {1, ..., 10}.
    PR #639 sharpened the surviving open form to a per-partition
    rule: k_λ = 1 for the max-|μ| partition, k_λ = 2 otherwise.
    Empirical: closes {D, T, ³He} to ~5%.

    The substrate c(K) ceiling
    (`c-k-beta-decay-bound.witness.json`) reaches:
        N=1 → 97 ppm,   N=2 → 0.96 ppm,
        N=3 → 9.4 ppb,  N=4 → 0.092 ppb.

    Q: Does pushing the non-dominant blocks to k_λ = N for higher
    N approach the structural ceiling, or does the prefactor
    plateau substantially above it?

This probe answers the question empirically. It implements:

    k_λ(N) = 1       if λ = argmax_λ' max_a |μ_a^(λ')(β)|
           = N       otherwise
    tower^(N)(β)    = | Σ_λ y_λ(q_0) · Σ_a Φ_q^{[≤k_λ(N)]}(μ_a^(λ)) |
    B^(N)(𝔥)        = m_e · ρ · (|tr_M| + tower^(N) + σ_{3A})

for N ∈ {1, 2, 3, 4, 5} and 𝔥 ∈ {D, T, ³He}. The N=2 row reproduces
PR #639's empirically-closing rule; higher-N rows test the ceiling.

Cherry-pick attribution (per /coordinate skill §10):
- Eigenvalue / operator-trace infrastructure: PR #638's
  `probe_phiq_operator_valued.py` (commit `d1d1893f` on
  `claude/close-level-selection-rule-bvMvw`).
- Per-partition k_λ rule: PR #639's `per-partition-k-lambda-rule.md`
  (commit `3fdecb7b` on `claude/q-beta-spectral-bridge-content`).
- c(K) ceiling for comparison: PR #639's
  `c_k_beta_decay_witness.py` and
  `c-k-beta-decay-bound.witness.json` (same commit).

Output: `probe-phiq-per-partition-n-sweep.witness.json`
"""
import sys
import json
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
from wedderburn_jones_markov import y_lambda_at
from mass_at_3A_proper import atom_braid_word_3A


AME = {"deuteron": 2.224566, "tritium": 8.481798, "he3": 7.71806}
Z_N = {"deuteron": (1, 1), "tritium": (1, 2), "he3": (2, 1)}
RHO_MAP = {"deuteron": 1, "tritium": 2, "he3": 2}
# Non-dominant depth N to sweep over.  Dominant partition always at
# k_λ = 1 (per PR #639 rule).  N=2 reproduces #639's empirical rule;
# N ≥ 3 tests whether pushing non-dominant deeper approaches the
# c(K) ceiling.
SWEEP_N = [1, 2, 3, 4, 5]
THRESHOLD_PCT = 5.0  # PR #639 empirical closure threshold


class PhiQPoleHit(Exception):
    pass


def phi_q_truncated_complex(mu, k_max, q=float(Q0)):
    """Truncated Φ_q^{[≤k_max]}(μ) for complex μ.

    Φ_q^{[≤k_max]}(μ) := ∏_{j=1}^{k_max} (1 - q^{-j}·μ)^{-1}.

    By convention, k_max = 0 ⇒ empty product ⇒ 1 (Φ_q^{[≤0]} acts
    as identity).  Raises PhiQPoleHit if any factor is numerically
    within 1e-14 of zero.
    """
    if k_max <= 0:
        return 1.0 + 0j
    qi = 1.0 / q
    product = 1.0 + 0j
    qi_pow = qi
    for j in range(1, k_max + 1):
        factor = 1.0 - qi_pow * mu
        if abs(factor) < 1e-14:
            raise PhiQPoleHit(
                f"Φ_q pole at j={j}: q^(-j)·μ = {qi_pow * mu:.4g}"
            )
        product = product / factor
        qi_pow *= qi
    return product


def rho_lambda_braid(sigmas, dim, word):
    """Numerical braid operator ρ_λ(β) in irrep V_λ.

    Multiplies (c · σ_g + d · I) along the braid word.  Returns a
    `dim × dim` complex matrix.  Cherry-picked from PR #638's
    `probe_phiq_operator_valued.py`.
    """
    M = np.eye(dim, dtype=complex)
    Id = np.eye(dim, dtype=complex)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"σ_{g} out of range for {len(sigmas)} sigmas"
            )
        sigma_g = sigmas[g]
        if hasattr(sigma_g, "toarray"):
            sigma_g = sigma_g.toarray()
        sigma_g = np.asarray(sigma_g, dtype=complex)
        M = M @ (c * sigma_g + d * Id)
    return M


def compute_per_atom_eigenvalue_data(q0_val, block_cache):
    """For each atom, compute per-partition eigenvalue spectra and
    identify the dominant partition via TWO selectors:

    * **Selector A** (max-$\\lvert\\mu\\rvert$): the partition with the
      largest eigenvalue magnitude over $\\rho_\\lambda(\\beta)$ —
      stated rule in PR #639's `per-partition-k-lambda-rule.md`.
    * **Selector B** (max-$\\lvert y_\\lambda \\cdot \\sum_a \\Phi_q^{[\\le 2]}(\\mu_a^{(\\lambda)}) \\rvert$):
      the partition with the largest absolute Wedderburn contribution
      at $k = 2$ — *empirical* selector implicit in PR #639's table
      (its values $-6.220, -3.001, -11.692$ match `|contrib_k2|`
      exactly under this selector, not under Selector A).

    The empirical selector B is the one that actually closes the
    rule (verified during this branch's investigation —
    `docs/audits/2026-05-11-per-partition-k-lambda-selector-investigation.md`).

    Returns a dict keyed by atom name with fields:
        Z, N, A, n, tr_M, rows,
        dominant_shape_A, dominant_index_A, dominant_max_mu_abs,
        dominant_shape_B, dominant_index_B, dominant_contrib_abs_k2.
    """
    qi = 1.0 / q0_val

    def phi_q_trunc_local(mu, k):
        if k <= 0:
            return 1.0 + 0j
        prod = 1.0 + 0j
        qi_pow = qi
        for j in range(1, k + 1):
            prod = prod / (1.0 - qi_pow * mu)
            qi_pow *= qi
        return prod

    per_atom = {}
    for name, (Z, N) in Z_N.items():
        A = Z + N
        n = 3 * A
        print(f"    {name:>10}  (Z={Z}, N={N}, n={n})...", flush=True)
        word = atom_braid_word_3A(Z, N, include_inter=True)
        y_vals = y_lambda_at(n, q_val=q0_val)
        rows = []
        tr_M = 0.0
        for shape, y in y_vals.items():
            sigmas, dim, _ = build_seminormal_matrices_cached(
                shape, cache=block_cache,
            )
            if dim == 0:
                continue
            rho = rho_lambda_braid(sigmas, dim, word)
            eigenvalues = np.linalg.eigvals(rho)
            chi_q = complex(np.trace(rho))
            tr_M += float(y) * chi_q.real
            max_mu_abs = float(max(abs(z) for z in eigenvalues))
            # Selector B value: |y · sum_a Φ_q^{[≤2]}(μ_a)|
            tower_k2 = sum(
                phi_q_trunc_local(complex(z), 2) for z in eigenvalues
            )
            contrib_k2_signed = float(y) * tower_k2
            rows.append({
                "partition": list(shape),
                "dim": int(dim),
                "y_at_q0": float(y),
                "chi_q_at_q0": float(chi_q.real),
                "eigenvalues_real": [float(z.real) for z in eigenvalues],
                "eigenvalues_imag": [float(z.imag) for z in eigenvalues],
                "max_eigval_abs": max_mu_abs,
                "contrib_k2_real": float(contrib_k2_signed.real),
                "contrib_k2_imag": float(contrib_k2_signed.imag),
                "abs_contrib_k2": abs(contrib_k2_signed),
            })
        # Selector A: max-|μ|.  Selector B: max-|y · contrib_k=2|.
        dom_idx_A = max(range(len(rows)),
                        key=lambda i: rows[i]["max_eigval_abs"])
        dom_idx_B = max(range(len(rows)),
                        key=lambda i: rows[i]["abs_contrib_k2"])
        per_atom[name] = {
            "Z": Z, "N": N, "A": A, "n": n,
            "tr_M": float(tr_M),
            "n_partitions": len(rows),
            "rows": rows,
            "dominant_shape_A": rows[dom_idx_A]["partition"],
            "dominant_max_mu_abs": rows[dom_idx_A]["max_eigval_abs"],
            "dominant_index_A": dom_idx_A,
            "dominant_shape_B": rows[dom_idx_B]["partition"],
            "dominant_contrib_abs_k2": rows[dom_idx_B]["abs_contrib_k2"],
            "dominant_index_B": dom_idx_B,
        }
        print(f"      done — n_part={len(rows)}, tr_M={tr_M:.5f}")
        print(f"               Selector A (max|μ|): "
              f"λ={rows[dom_idx_A]['partition']}, "
              f"max|μ|={rows[dom_idx_A]['max_eigval_abs']:.3f}")
        print(f"               Selector B (max|y·contrib_k=2|): "
              f"λ={rows[dom_idx_B]['partition']}, "
              f"|contrib_k=2|={rows[dom_idx_B]['abs_contrib_k2']:.3f}")
    return per_atom


def compute_tower_per_partition(rows, dominant_index, k_non_dom,
                                  k_dom=1):
    """Compute |tower^(per-partition)(β)| under the k_λ rule:
        k_λ = k_dom    if λ is the dominant partition
        k_λ = k_non_dom otherwise.
    """
    tower_complex = 0.0 + 0j
    for i, row in enumerate(rows):
        y = float(row["y_at_q0"])
        evs = [complex(r, i) for r, i in zip(
            row["eigenvalues_real"],
            row["eigenvalues_imag"],
        )]
        k_lambda = k_dom if i == dominant_index else k_non_dom
        tower_lambda = sum(
            phi_q_truncated_complex(mu, k_lambda) for mu in evs
        )
        tower_complex += y * tower_lambda
    return tower_complex


def c_k_ceiling_at_depth(q0_val, N):
    """The PR #639 substrate c(K) geometric ceiling at depth N:
        |R_N| ≤ ℏ_q^(2(N+1)) / (1 - ℏ_q²)
    with ℏ_q = (q_0 - 1)/q_0.

    Returns the bound in (relative_fraction, ppb) pairs.
    """
    hbar_q = (q0_val - 1.0) / q0_val
    bound = hbar_q ** (2 * (N + 1)) / (1.0 - hbar_q ** 2)
    return bound, bound * 1e9


def main():
    HERE = Path(__file__).parent
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]

    def sigma_3A(A):
        return float(sigma_3A_witness[f"n={3 * A}"])

    q0_val = float(Q0)
    hbar_q = (q0_val - 1.0) / q0_val

    w = (
        WitnessBuilder("probe-phiq-per-partition-n-sweep",
                       engine="python")
        .set_description(
            "Joint PR #638 + #639 operator-valued Φ_q probe under "
            "the per-partition k_λ rule, sweeping non-dominant "
            "depth N ∈ {1, 2, 3, 4, 5}. Tests whether pushing the "
            "non-dominant Wedderburn blocks to deeper truncation "
            "approaches PR #639's substrate c(K) ceiling (N=3 → "
            "9.4 ppb, N=4 → 0.092 ppb). N=2 row reproduces PR "
            "#639's empirical closing rule (k_λ = 1 for dominant, "
            "k_λ = 2 otherwise → ~5% closure on {D, T, ³He}). "
            "Eigenvalues via numpy.linalg.eigvals on Hoefsmit "
            "seminormal ρ_λ(β); per-eigenvalue Φ_q; Wedderburn-summed "
            "with signed y_λ(q_0); |·| at binding-formula level. "
            "Cherry-picks (per /coordinate §10): #638's eigenvalue / "
            "operator-trace infrastructure + #639's max-|μ| selector "
            "+ #639's c(K) ceiling for comparison."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", q0_val)
        .add_parameter("hbar_q", hbar_q)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("non_dominant_depth_sweep", SWEEP_N)
        .add_parameter("k_dominant", 1)
        .add_parameter("threshold_pct", THRESHOLD_PCT)
    )

    block_cache = BlockCache(q0_val, q0_val - 1.0 / q0_val)

    print("=" * 88)
    print("Per-partition k_λ operator-valued Φ_q probe — non-dominant"
          " depth sweep")
    print("=" * 88)
    print(f"  q_0 = {q0_val}")
    print(f"  ℏ_q = (q_0 - 1)/q_0 = {hbar_q:.6f}")
    print(f"  m_e = {M_E_MEV} MeV")
    print()

    print("  Building ρ_λ(β), eigenvalues, identifying dominant λ"
          " per atom:")
    per_atom = compute_per_atom_eigenvalue_data(q0_val, block_cache)
    print()

    print("  Substrate c(K) ceiling table (PR #639):")
    ceiling = {}
    for N in SWEEP_N:
        bound, ppb = c_k_ceiling_at_depth(q0_val, N)
        ceiling[str(N)] = {"bound_rel": bound, "bound_ppb": ppb}
        print(f"    N={N}: |R_N| ≤ {bound:.4e} ({ppb:.4g} ppb)")
    print()

    print("  Sweep over non-dominant depth N (dominant always k=1),")
    print("  separate runs under Selector A and Selector B:")
    print()
    header = (f"  {'sel':>4} {'N':>3} {'atom':>10} {'|tr_M|':>9} "
              f"{'tower':>11}  {'B^N':>9}  {'AME':>7}  "
              f"{'err_pct':>10}  {'err_ppb':>11}  "
              f"{'ceiling_ppb':>12}")
    print(header)
    print("  " + "-" * (len(header) - 2))

    results = {"A": {}, "B": {}}
    for selector in ("A", "B"):
        dom_key = f"dominant_index_{selector}"
        for N in SWEEP_N:
            results[selector][str(N)] = {}
            for name, data in per_atom.items():
                tr_M_abs = abs(data["tr_M"])
                try:
                    tower_complex = compute_tower_per_partition(
                        data["rows"],
                        data[dom_key],
                        k_non_dom=N,
                        k_dom=1,
                    )
                    tower_abs = abs(tower_complex)
                    if not math.isfinite(tower_abs):
                        raise OverflowError("|tower| non-finite")
                except (PhiQPoleHit, OverflowError, ValueError) as e:
                    results[selector][str(N)][name] = {"error": str(e)}
                    print(f"  {selector:>4} {N:>3} {name:>10}  "
                          f"-- {e}")
                    continue
                A = data["A"]
                rho_atom = RHO_MAP[name]
                B_op = M_E_MEV * rho_atom * (
                    tr_M_abs + tower_abs + sigma_3A(A)
                )
                err_rel = (B_op - AME[name]) / AME[name]
                err_pct = 100.0 * err_rel
                err_ppb = abs(err_rel) * 1e9
                results[selector][str(N)][name] = {
                    "tr_M_abs": tr_M_abs,
                    "tower_complex_real": float(tower_complex.real),
                    "tower_complex_imag": float(tower_complex.imag),
                    "tower_abs": float(tower_abs),
                    "B_op_MeV": float(B_op),
                    "AME_MeV": AME[name],
                    "err_rel": float(err_rel),
                    "err_pct": float(err_pct),
                    "err_ppb": float(err_ppb),
                    "ame_close_within_threshold":
                        abs(err_pct) < THRESHOLD_PCT,
                    "ceiling_ppb": ceiling[str(N)]["bound_ppb"],
                    "headroom_observed_over_ceiling":
                        float(err_ppb / ceiling[str(N)]["bound_ppb"])
                        if ceiling[str(N)]["bound_ppb"] > 0
                        else float("nan"),
                }
                print(f"  {selector:>4} {N:>3} {name:>10} "
                      f"{tr_M_abs:>9.4f} "
                      f"{tower_abs:>+11.4f}  {B_op:>9.4f}  "
                      f"{AME[name]:>7.4f}  {err_pct:>+9.2f}%  "
                      f"{err_ppb:>11.4e}  "
                      f"{ceiling[str(N)]['bound_ppb']:>12.4e}")
            print()
        print()

    # Per-N closure verdict against the empirical 5% threshold
    # (PR #639's stated closure criterion).
    print("  Per-N closure verdict (all 3 within "
          f"{THRESHOLD_PCT}%), per selector:")
    closure_by_N = {"A": {}, "B": {}}
    for selector in ("A", "B"):
        print(f"  --- Selector {selector} ---")
        for N in SWEEP_N:
            per = results[selector][str(N)]
            if any("error" in v for v in per.values()):
                closure_by_N[selector][str(N)] = False
                print(f"    N={N}: SKIPPED (errors)")
                continue
            max_err = max(abs(per[a]["err_pct"]) for a in AME)
            closure_by_N[selector][str(N)] = max_err < THRESHOLD_PCT
            verdict = ("YES" if max_err < THRESHOLD_PCT
                       else f"NO ({max_err:.1f}%)")
            print(f"    N={N}: {verdict} "
                  f"(worst err: {max_err:.2f}%)")
    print()

    # Headroom analysis — does observed match c(K) ceiling decay?
    print("  Headroom (observed_ppb / ceiling_ppb) by N, per selector:")
    for selector in ("A", "B"):
        print(f"  --- Selector {selector} ---")
        for N in SWEEP_N:
            per = results[selector][str(N)]
            if any("error" in v for v in per.values()):
                continue
            ratios = [per[a]["headroom_observed_over_ceiling"]
                      for a in AME]
            avg_ratio = sum(ratios) / len(ratios)
            max_ratio = max(ratios)
            print(f"    N={N}: mean = {avg_ratio:.4e}, "
                  f"max = {max_ratio:.4e}")
    print()

    n2_closure_A = closure_by_N["A"].get("2", False)
    n2_closure_B = closure_by_N["B"].get("2", False)
    any_closure_A = any(closure_by_N["A"].values())
    any_closure_B = any(closure_by_N["B"].values())

    if n2_closure_B:
        print("  ✓ PR #639's empirical N=2 rule reproduced under "
              "Selector B (max|y·contrib_k=2|).")
    if not n2_closure_A:
        print("  ✗ PR #639's STATED rule (Selector A, max|μ|) does "
              "NOT close at N=2 — the .md mislabels the selector.")

    w = (
        w
        .add_data("hbar_q_50dps_string", repr(hbar_q))
        .add_data("ceiling", ceiling)
        .add_data("per_atom_dominant_summary", {
            name: {
                "Z": d["Z"], "N": d["N"], "A": d["A"], "n": d["n"],
                "dominant_shape_A_max_mu": d["dominant_shape_A"],
                "dominant_max_mu_abs": d["dominant_max_mu_abs"],
                "dominant_shape_B_max_contrib_k2":
                    d["dominant_shape_B"],
                "dominant_contrib_abs_k2":
                    d["dominant_contrib_abs_k2"],
                "tr_M": d["tr_M"],
            }
            for name, d in per_atom.items()
        })
        .add_data("results_selector_A_max_mu", results["A"])
        .add_data("results_selector_B_max_contrib_k2", results["B"])
        .add_data("closure_by_N_selector_A", closure_by_N["A"])
        .add_data("closure_by_N_selector_B", closure_by_N["B"])
        .add_assertion(
            "PR_639_N2_rule_reproduces_under_selector_B",
            computed=1 if n2_closure_B else 0,
            expected=1,
        )
        .add_assertion(
            "stated_selector_A_max_mu_does_NOT_close_at_N2",
            computed=0 if n2_closure_A else 1,
            expected=1,
            # The .md mis-labels the selector — its stated rule
            # (Selector A) does NOT close even though the table's
            # values match Selector B exactly.
        )
        .add_caveat(
            "Absolute-form binding B = m_e·ρ·(|tr_M|+|tower|+σ_{3A}); "
            "subtractive form would require recomputing all per-irrep "
            "eigenvalues at include_inter=False. Deferred (matches "
            "PR #638's scope)."
        )
        .add_caveat(
            "Eigenvalues via numpy float64. The c(K) ceiling table is "
            "the STRUCTURAL upper bound from PR #639's "
            "c_k_beta_decay_witness.py. The observed binding-formula "
            "residual is NOT directly the truncation remainder |R_N| — "
            "it folds in σ_{3A} (Wedderburn jet correction) and the "
            "ρ pre-factor (atomic gauge). Headroom comparison is "
            "indicative, not definitive: a probe of |R_N| directly "
            "would require subtracting the tr_M and σ_{3A} terms."
        )
        .add_caveat(
            "Cherry-picks (per /coordinate §10): PR #638's "
            "probe_phiq_operator_valued.py (eigenvalue / "
            "operator-trace infrastructure) and PR #639's "
            "per-partition-k-lambda-rule.md (max-|μ| selector + "
            "k_λ rule), c_k_beta_decay_witness.py (ceiling). "
            "Neither PR has merged at the time of this probe; if "
            "either lands and changes the relevant infrastructure, "
            "this probe should be re-run."
        )
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
