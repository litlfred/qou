#!/usr/bin/env python3
from computations.substrate.codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION
"""Operator-valued Φ_q brane-tower probe (Wedderburn-block form).

Companion to ``probe_phiq_uniform_k.py``.  The earlier probe — and the
``n_⋆ = ℓ·n₀ + k`` per-atom probe ``probe_phiq_n_star_rule.py`` —
evaluate Φ_q at the **scalar** per-generator volume |V̂_i|, then sum
over generators.  That collapses the Hecke irrep structure: every
partition λ ⊢ n₀ contributes through a single 1-D eigenvalue of the
generator's algebraic volume.

This probe promotes Φ_q to an **operator-valued** evaluation across
the Wedderburn decomposition of H_{3A}(q_0):

    tower_op^(k)(𝔥)  :=  Σ_{λ ⊢ 3A}  y_λ(q_0) · Φ_q^{[≤k]}(|χ^λ_q(β_𝔥)| / dim V_λ)

where:
- y_λ(q_0)        is the canonical Jones-Markov weight via
                  ``wedderburn_jones_markov.y_lambda_at`` (Wenzl
                  Schur principal specialization, NOT the 2-variable
                  Schur formula that vanishes on ≥3-row partitions).
- χ^λ_q(β_𝔥)      is the Hoefsmit q-Hecke seminormal character of the
                  full atomic braid word β_𝔥 — computed once via
                  ``global_wedderburn_sum_q_hecke_seminormal`` (trusted
                  to 1e-13 at q_0 vs ``markov_trace_recursive``).
- |χ^λ_q| / dim   is the per-irrep average character magnitude — the
                  Wenzl-style normalization aligned with the
                  "per-generator volume" in the scalar form.
- Σ_λ y_λ ...     IS the convolution-aware combination: the character
                  of a braid product encodes the full Hecke
                  convolution structure (R-matrix action), not a
                  per-generator scalar sum.

The binding formula remains absolute-form (matches ``probe_phiq_uniform_k``
absolute case):

    B_op^(k)(𝔥)  =  m_e · ρ · (|tr_M(β_𝔥)| + tower_op^(k)(𝔥) + σ_{3A})

The probe answers: **does promoting Φ_q from the scalar form to the
Wedderburn-block (higher-irrep, convolution-aware) form close the AME
light-isotope gap at any uniform k?**

If yes, the operator-valued form of `conj:brane-tower-z-habiro`'s
`n_⋆` existence claim is empirically supported and the scalar
refutation in the §"Closure (2026-05-11)" section is properly scoped.
If no, the open question shifts to the strictly-stronger
**per-eigenvalue operator** form: Φ_q applied to each eigenvalue of
ρ_λ(β_𝔥), summed (= operator-trace), Wedderburn-weighted.

Output: ``probe-phiq-avg-chi-over-classical-dim.witness.json``
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder
from wedderburn_jones_markov import global_wedderburn_sum_q_hecke_seminormal

AME = {"deuteron": 2.224566, "tritium": AME_B_TRITIUM_MEV_VALIDATION, "he3": AME_B_HE3_MEV_VALIDATION}
Z_N = {"deuteron": (1, 1), "tritium": (1, 2), "he3": (2, 1)}
RHO_MAP = {"deuteron": 1, "tritium": 2, "he3": 2}
SWEEP_K = [1, 2, 3, 4, 5, 6, 8, 10]

# Falsifiability threshold from conj:brane-tower-z-habiro §Falsifiability
THRESHOLD_PCT = 10.0


class PhiQPoleHit(Exception):
    """Φ_q truncation factor (1 - q^{-k}·z) within numerical zero."""
    def __init__(self, k, qi_pow_z):
        super().__init__(
            f"Φ_q pole encountered at k={k}: |1 - q^(-k)·z| < 1e-14"
            f" (q^(-k)·z = {qi_pow_z:.6g})"
        )
        self.k = k


def phi_q_truncated(z, k_max, q=float(Q0)):
    """Truncated Φ_q^{[≤k_max]}(z) = ∏_{k=1}^{k_max} (1 - q^{-k}z)^{-1}.

    Same convention as ``probe_phiq_uniform_k.Phi_q_truncated`` —
    raises PhiQPoleHit on near-singular factors so we surface a pole
    rather than NaN.
    """
    qi = 1.0 / q
    product = 1.0
    qi_pow = qi
    for k in range(1, k_max + 1):
        factor = 1.0 - qi_pow * z
        if abs(factor) < 1e-14:
            raise PhiQPoleHit(k, qi_pow * z)
        product /= factor
        qi_pow *= qi
    return product


def main():
    HERE = Path(__file__).parent
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma(A):
        return float(sigma_3A_witness[f"n={3 * A}"])

    # Start WitnessBuilder timer at the top so durationMs reflects the
    # actual per-atom Wedderburn-sum compute (Copilot review on PR #638).
    w = (
        WitnessBuilder("probe-phiq-avg-chi-over-classical-dim", engine="python")
        .set_description(
            "Operator-valued Φ_q brane-tower probe in Wedderburn-block "
            "form. For each isotope in {D, T, ³He} and each k in "
            "{1,2,3,4,5,6,8,10}, computes "
            "tower_op^(k) = Σ_λ y_λ Φ_q^{[≤k]}(|χ^λ_q(β)|/dim V_λ), "
            "Wedderburn-summed across irreps of H_{3A}(q_0) via the "
            "trusted q-Hecke seminormal infrastructure (per-irrep χ^λ "
            "via Hoefsmit, y_λ via Wenzl Schur principal specialization). "
            "Historical / superseded variant of the canonical "
            "per-eigenvalue operator-valued probe in "
            "probe_phiq_operator_valued.py: this one uses three "
            "approximations (classical SYT-count dim_V_λ instead of "
            "quantum dim_q; abs(χ) instead of signed χ; "
            "mean-of-eigenvalues instead of per-eigenvalue Φ_q + "
            "operator trace) that biased the k=2 ³He result."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", float(Q0))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("k_sweep", SWEEP_K)
        .add_parameter("threshold_pct", THRESHOLD_PCT)
    )

    print("=" * 88)
    print("Operator-valued (Wedderburn-block) Φ_q brane-tower probe")
    print("=" * 88)
    print(f"  q_0 = {float(Q0)}, m_e = {M_E_MEV} MeV")
    print()

    # Cache per-atom Wedderburn rows (tr_M + per-irrep χ^λ).  This is
    # the bottleneck — n=9 calls (T, ³He) are ~60-90 s each.
    print("  Computing per-irrep χ^λ_q(β) and y_λ(q_0) per atom...")
    print("    (n=6 deuteron: ~4 s; n=9 tritium + he3: ~60-90 s each)")
    per_atom = {}
    for name, (Z, N) in Z_N.items():
        A = Z + N
        n = 3 * A
        print(f"    {name:>10}  (Z={Z}, N={N}, n={n})...", flush=True)
        tr_M, rows = global_wedderburn_sum_q_hecke_seminormal(
            Z, N, q_val=float(Q0),
        )
        per_atom[name] = {
            "tr_M": float(tr_M),
            "rows": rows,
            "Z": Z,
            "N": N,
            "A": A,
        }
    print()

    # Sweep k uniformly across {D, T, ³He}.
    print("  Sweep over uniform k (per-irrep average character |χ|/dim,")
    print("  Wedderburn-weighted by y_λ at q_0):")
    print()
    print(f"  {'k':>3} {'atom':>10} {'|tr_M|':>9} {'tower_op':>11}"
          f"  {'B_op_abs':>9}  {'AME':>7}  {'err_pct':>10}")
    print("  " + "-" * 76)

    results = {}
    for k in SWEEP_K:
        results[str(k)] = {}
        for name, data in per_atom.items():
            tr_M_abs = abs(data["tr_M"])
            try:
                tower_op = 0.0
                for row in data["rows"]:
                    dim = int(row["dim"])
                    chi = float(row["chi_q_at_q0"])
                    y = float(row["y_at_q0"])
                    if dim == 0:
                        continue
                    z_lambda = abs(chi) / dim
                    phi_lambda = phi_q_truncated(z_lambda, k)
                    tower_op += y * phi_lambda
            except PhiQPoleHit as e:
                results[str(k)][name] = {"pole_hit": True, "k_at_pole": e.k}
                print(f"  {k:>3} {name:>10} -- pole hit at k={e.k}, skipping")
                continue
            A = data["A"]
            rho = RHO_MAP[name]
            sigma_3A = sigma(A)
            B_op_abs = M_E_MEV * rho * (tr_M_abs + tower_op + sigma_3A)
            err_pct = 100.0 * (B_op_abs - AME[name]) / AME[name]
            results[str(k)][name] = {
                "tr_M_abs": tr_M_abs,
                "tower_op": float(tower_op),
                "B_op_abs_MeV": float(B_op_abs),
                "AME_MeV": AME[name],
                "err_pct": float(err_pct),
                "ame_close_within_threshold": abs(err_pct) < THRESHOLD_PCT,
            }
            print(f"  {k:>3} {name:>10} {tr_M_abs:>9.4f} {tower_op:>+11.4f}"
                  f"  {B_op_abs:>9.4f}  {AME[name]:>7.4f}"
                  f"  {err_pct:>+9.2f}%")
        print()

    # Verdict: does any uniform k close all three within threshold?
    print("  Verdict (does any uniform k close all three within "
          f"{THRESHOLD_PCT}%?):")
    closed_any = False
    closed_k = []
    for k in SWEEP_K:
        per = results[str(k)]
        if any("pole_hit" in v for v in per.values()):
            continue
        max_err = max(abs(per[a]["err_pct"]) for a in AME)
        verdict = "YES" if max_err < THRESHOLD_PCT else f"NO ({max_err:.0f}%)"
        if max_err < THRESHOLD_PCT:
            closed_any = True
            closed_k.append(k)
        print(f"    k={k:>3}:  {verdict}")
    print()
    if closed_any:
        print(f"  Closure achieved at k ∈ {closed_k} — operator-valued form")
        print(f"  empirically supports `conj:brane-tower-z-habiro` n_⋆ "
              f"existence.")
    else:
        print("  No uniform-k closure under operator-valued (Wedderburn-")
        print("  block, χ^λ-normalized) form. The scalar refutation in")
        print("  §\"Closure (2026-05-11)\" extends to this irrep-weighted")
        print("  promotion; the per-eigenvalue operator form is the next")
        print("  refinement (open).")

    w = (
        w
        .add_data("per_atom", {
            name: {
                "Z": d["Z"], "N": d["N"], "A": d["A"],
                "n_partitions": len(d["rows"]),
                "tr_M": d["tr_M"],
            } for name, d in per_atom.items()
        })
        .add_data("results", results)
        .add_assertion(
            "no_uniform_k_closes_within_threshold",
            computed=0 if closed_any else 1,
            expected=1,
        )
        .add_caveat(
            "Absolute-form binding B = m_e·ρ·(|tr_M|+tower_op+σ_{3A}); "
            "subtractive form would require recomputing χ^λ at "
            "include_inter=False and is queued as a separate probe."
        )
        .add_caveat(
            "Wedderburn-weighted Φ_q at |χ^λ|/dim is the irrep-weighted "
            "scalar promotion. The strictly-stronger per-eigenvalue "
            "operator form (Φ_q applied to each eigenvalue of "
            "ρ_λ(β) in V_λ, summed as the operator trace, then "
            "Wedderburn-weighted) is in probe_phiq_operator_valued.py."
        )
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    # Exit 0 whenever the witness assertions pass — a successful
    # refutation IS the expected outcome (Copilot review on PR #638).
    return 0


if __name__ == "__main__":
    sys.exit(main())
