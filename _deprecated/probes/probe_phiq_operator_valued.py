#!/usr/bin/env python3
from computations.substrate.codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION
"""Operator-valued Φ_q brane-tower probe — per-eigenvalue, signed,
operator-trace form.

True convolution-aware operator-valued promotion of the scalar
brane-tower:

    tower_op^(k)(β_𝔥)
      :=  Σ_{λ ⊢ 3A}  y_λ(q_0) · tr_λ( Φ_q^{[≤k]}(ρ_λ(β_𝔥)) )
      =   Σ_λ y_λ(q_0) · Σ_{a=1}^{dim V_λ} Φ_q^{[≤k]}( μ_a^{(λ)} )

where:
- y_λ(q_0)        — Jones-Markov weight (Wenzl Schur principal spec)
- ρ_λ(β_𝔥)        — braid operator in irrep V_λ (numerical matrix
                    built from Hoefsmit seminormal sigmas)
- μ_a^{(λ)}       — eigenvalues of ρ_λ(β_𝔥) (complex)
- Φ_q^{[≤k]}(μ)   — ∏_{j=1}^{k}(1 - q^{-j}·μ)^{-1}, complex-valued
- tr_λ(...)       — operator trace inside V_λ (sum over eigenvalues)

Replaces the earlier `_avg_chi_over_classical_dim` variant, which
used three approximations that biased the result:

1. **Classical dim_V_λ vs quantum dim_q V_λ.**  Per-irrep normalization
   used the SYT count (classical) instead of the q-Hecke quantum
   dimension.  In the per-eigenvalue form, no per-irrep denominator
   appears — the operator trace tr_λ replaces the average, so the
   classical/quantum dim issue is structurally resolved.
2. **Abs of χ^λ vs signed χ^λ.**  The earlier variant took
   |χ^λ_q(β)| before feeding Φ_q.  This loses sign information for
   sign-indefinite characters at n ≥ 4.  The per-eigenvalue form
   keeps full complex amplitudes throughout and only takes |·| of
   the final Wedderburn sum.
3. **Mean-of-eigenvalues vs operator-trace of Φ_q.**  The earlier
   variant applied Φ_q to the mean per-irrep character |χ^λ|/dim —
   one scalar input per irrep.  The per-eigenvalue form applies Φ_q
   to each μ_a^{(λ)} separately, summing as the operator trace.
   This is the strictly stronger (and canonical) promotion.

The binding formula is the absolute form, matching the prior probes:

    B_op^(k)(𝔥)  =  m_e · ρ · ( |tr_M(β_𝔥)| + |tower_op^(k)(𝔥)| + σ_{3A} )

Output: `probe-phiq-operator-valued.witness.json`
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
from hecke_characters import build_seminormal_matrices
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
from wedderburn_jones_markov import y_lambda_at
from mass_at_3A_proper import atom_braid_word_3A

AME = {"deuteron": 2.224566, "tritium": AME_B_TRITIUM_MEV_VALIDATION, "he3": AME_B_HE3_MEV_VALIDATION}
Z_N = {"deuteron": (1, 1), "tritium": (1, 2), "he3": (2, 1)}
RHO_MAP = {"deuteron": 1, "tritium": 2, "he3": 2}
SWEEP_K = [1, 2, 3, 4, 5, 6, 8, 10]
THRESHOLD_PCT = 10.0


class PhiQPoleHit(Exception):
    pass


def phi_q_truncated_complex(mu, k_max, q=float(Q0)):
    """Truncated Φ_q^{[≤k_max]}(μ) for complex μ.

    Returns ∏_{j=1}^{k_max} (1 - q^{-j}·μ)^{-1} as a complex number.
    Raises PhiQPoleHit if a factor is within numerical zero.
    """
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

    Multiplies the per-step factors `c · σ_g + d · I` along the
    braid word.  Returns a `dim × dim` complex matrix.
    """
    M = np.eye(dim, dtype=complex)
    I = np.eye(dim, dtype=complex)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"σ_{g} out of range for {len(sigmas)} sigmas"
            )
        sigma_g = sigmas[g]
        if hasattr(sigma_g, "toarray"):
            sigma_g = sigma_g.toarray()
        sigma_g = np.asarray(sigma_g, dtype=complex)
        M = M @ (c * sigma_g + d * I)
    return M


def main():
    HERE = Path(__file__).parent
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma_3A(A):
        return float(sigma_3A_witness[f"n={3 * A}"])

    q0_val = float(Q0)

    # Start WitnessBuilder timer at the top so durationMs reflects the
    # actual per-atom eigenvalue compute (Copilot review on PR #638).
    w = (
        WitnessBuilder("probe-phiq-operator-valued", engine="python")
        .set_description(
            "Per-eigenvalue, signed-character, operator-trace promotion "
            "of the scalar Φ_q brane-tower probe. For each isotope in "
            "{D, T, ³He} and each k in {1,2,3,4,5,6,8,10}, computes "
            "tower_op^(k) = |Σ_λ y_λ(q_0) · tr_λ(Φ_q^{[≤k]}(ρ_λ(β)))| "
            "where ρ_λ(β) is the numerical braid operator in irrep V_λ "
            "(via Hoefsmit seminormal at q_0). Eigenvalues μ_a^(λ) via "
            "numpy.linalg.eigvals; Φ_q applied per eigenvalue; "
            "operator-trace = Σ_a Φ_q^{[≤k]}(μ_a^(λ)); Wedderburn-summed "
            "with signed y_λ (complex), final |·| at binding-formula "
            "level. Replaces the prior _avg_chi_over_classical_dim "
            "variant which used three approximations (classical dim, "
            "abs χ, mean-of-eigenvalues) that biased the result. "
            "Per-irrep eigenvalue spectra are persisted in "
            "data.per_atom[atom].rows[i].eigenvalues_{real,imag} for "
            "downstream audit and multiplicity-refined probes."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", q0_val)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("k_sweep", SWEEP_K)
        .add_parameter("threshold_pct", THRESHOLD_PCT)
    )

    # Per-q BlockCache shared across irreps (Copilot perf review).
    block_cache = BlockCache(q0_val, q0_val - 1.0 / q0_val)

    print("=" * 88)
    print("Operator-valued Φ_q brane-tower probe — PER-EIGENVALUE form")
    print("=" * 88)
    print(f"  q_0 = {q0_val}, m_e = {M_E_MEV} MeV")
    print()
    print("  Building ρ_λ(β) and computing eigenvalues per atom × per irrep")
    print("  (Hoefsmit seminormal at q_0 via BlockCache; numpy.linalg.eigvals)")
    print()

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
            # tr_λ(ρ) is the per-irrep character χ^λ_q(β); should be real
            chi_q = complex(np.trace(rho))
            tr_M += float(y) * chi_q.real
            rows.append({
                "partition": list(shape),
                "dim": int(dim),
                "y_at_q0": float(y),
                "chi_q_at_q0": float(chi_q.real),
                "eigenvalues_real": [float(z.real) for z in eigenvalues],
                "eigenvalues_imag": [float(z.imag) for z in eigenvalues],
                "max_eigval_abs": float(max(abs(z) for z in eigenvalues)),
            })
        per_atom[name] = {
            "Z": Z, "N": N, "A": A, "n": n,
            "tr_M": float(tr_M),
            "n_partitions": len(rows),
            "rows": rows,
        }
        max_ev = max(r["max_eigval_abs"] for r in rows)
        print(f"      done — n_part={len(rows)}, tr_M={tr_M:.5f},"
              f" max|μ|={max_ev:.3f}")
    print()

    print("  Sweep over uniform k (per-eigenvalue Φ_q^{[≤k]},")
    print("  operator-traced, signed Wedderburn-weighted, |·| at end):")
    print()
    print(f"  {'k':>3} {'atom':>10} {'|tr_M|':>9} {'|tower|':>12}"
          f"  {'B_op_abs':>9}  {'AME':>7}  {'err_pct':>11}")
    print("  " + "-" * 80)

    results = {}
    for k in SWEEP_K:
        results[str(k)] = {}
        for name, data in per_atom.items():
            tr_M_abs = abs(data["tr_M"])
            try:
                tower_op_complex = 0.0 + 0j
                for row in data["rows"]:
                    y = float(row["y_at_q0"])
                    evs = [complex(r, i) for r, i in zip(
                        row["eigenvalues_real"],
                        row["eigenvalues_imag"],
                    )]
                    # Operator-trace of Φ_q^{[≤k]}(ρ_λ(β)):
                    #   tr_λ(Φ_q^{[≤k]}(ρ_λ(β))) = Σ_a Φ_q^{[≤k]}(μ_a^{(λ)})
                    tower_lambda = sum(
                        phi_q_truncated_complex(mu, k) for mu in evs
                    )
                    tower_op_complex += y * tower_lambda
                tower_op_abs = abs(tower_op_complex)
                if not math.isfinite(tower_op_abs):
                    raise OverflowError(
                        f"|tower_op| non-finite (|μ|^k overflow)")
            except (PhiQPoleHit, OverflowError, ValueError) as e:
                results[str(k)][name] = {"error": str(e)}
                print(f"  {k:>3} {name:>10} -- {e}, skipping")
                continue
            A = data["A"]
            rho_atom = RHO_MAP[name]
            B_op_abs = M_E_MEV * rho_atom * (
                tr_M_abs + tower_op_abs + sigma_3A(A)
            )
            err_pct = 100.0 * (B_op_abs - AME[name]) / AME[name]
            results[str(k)][name] = {
                "tr_M_abs": tr_M_abs,
                "tower_op_complex_real": float(tower_op_complex.real),
                "tower_op_complex_imag": float(tower_op_complex.imag),
                "tower_op_abs": float(tower_op_abs),
                "B_op_abs_MeV": float(B_op_abs),
                "AME_MeV": AME[name],
                "err_pct": float(err_pct),
                "ame_close_within_threshold": abs(err_pct) < THRESHOLD_PCT,
            }
            print(f"  {k:>3} {name:>10} {tr_M_abs:>9.4f} {tower_op_abs:>+12.4f}"
                  f"  {B_op_abs:>9.4f}  {AME[name]:>7.4f}"
                  f"  {err_pct:>+10.2f}%")
        print()

    closed_any = False
    closed_k = []
    print(f"  Verdict (does any uniform k close all three within "
          f"{THRESHOLD_PCT}%?):")
    for k in SWEEP_K:
        per = results[str(k)]
        if any("error" in v for v in per.values()):
            atom_errors = [a for a, v in per.items() if "error" in v]
            print(f"    k={k:>3}:  SKIPPED (errors on {atom_errors})")
            continue
        max_err = max(abs(per[a]["err_pct"]) for a in AME)
        verdict = "YES" if max_err < THRESHOLD_PCT else f"NO ({max_err:.1f}%)"
        if max_err < THRESHOLD_PCT:
            closed_any = True
            closed_k.append(k)
        print(f"    k={k:>3}:  {verdict}")
    print()
    if closed_any:
        print(f"  Closure achieved at k ∈ {closed_k} — per-eigenvalue")
        print("  operator-valued form supports the n_⋆ existence claim.")
    else:
        print("  No uniform-k closure under the per-eigenvalue,")
        print("  operator-trace, signed Wedderburn-weighted form.")
        print("  All probed forms (scalar-eigenvalue + Wedderburn-block-avg")
        print("  + per-eigenvalue operator-trace) now fail the AME light-")
        print("  isotope falsifiability threshold.")

    # Per-irrep eigenvalue spectra kept in `per_atom[atom].rows[i].eigenvalues_{real,imag}`
    # for downstream audit + the multiplicity-refined probe (PR #638
    # Copilot review: persistence claim now matches reality).

    w = (
        w
        .add_data("per_atom", per_atom)
        .add_data("results", results)
        .add_assertion(
            "no_uniform_k_closes_within_threshold",
            computed=0 if closed_any else 1,
            expected=1,
        )
        .add_caveat(
            "Absolute-form binding B = m_e·ρ·(|tr_M|+|tower_op|+σ_{3A}); "
            "subtractive form would require recomputing all per-irrep "
            "eigenvalues at include_inter=False, deferred."
        )
        .add_caveat(
            "Eigenvalues computed via numpy float64. For braid words "
            "where |μ| exceeds q_0^k_max, the per-eigenvalue Φ_q^{[≤k]} "
            "can overflow numerically — values are surfaced as errors "
            "rather than silently producing NaN. mpmath promotion is "
            "the obvious refinement if higher-k cases need to be "
            "probed quantitatively."
        )
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    # Exit 0 whenever the witness assertions pass: the witness asserts
    # `no_uniform_k_closes_within_threshold` and a successful refutation
    # IS the expected outcome under the falsifiability criterion
    # (Copilot review on PR #638).
    return 0


if __name__ == "__main__":
    sys.exit(main())
