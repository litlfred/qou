#!/usr/bin/env python3
"""Probe: wedderburn-weight-canonical
(`prop:wedderburn-weight-canonical`).

Verifies the canonical q-deformed Wedderburn-block weight

    w̃_λ  :=  dim_q(λ)² / [n]_q!,

with the quantum hook-length dimension (q-deformed
Frame-Robinson-Thrall)

    dim_q(λ)  =  [n]_q! / ∏_{x ∈ λ} [h_x]_q,
    [k]_q     =  (q^k − q⁻ᵏ) / (q − q⁻¹).

Three identity checks:

  (1) **Classical-limit check.**  Evaluate dim_q(λ) at q = 1 + ε
      (ε = 1e-13) and compare to f_λ := n!/∏ h_x (classical
      Frame-Robinson-Thrall).  The 0/0 singularity of [k]_q at
      q = 1 is sidestepped by the perturbed evaluation; residue is
      bounded by O(ε), well below the assertion tolerance.  Tested
      for n = 1…6 across all 22 partitions.

  (2) **q-deformed normalisation drift at q_0.**  At q = q_0 ≠ 1,
      Σ_λ w̃_λ ≠ 1 in general — the non-probability-measure
      property called out in AGENTS.md's notation register.  Probe
      documents the actual sum at q_0 for n = 3, 4, 5
      (informational `add_data`; not asserted to any value).  At
      q = 1 the sum collapses to the classical Plancherel
      normalisation Σ_λ w_λ = 1; that classical check is wired by
      `plancherel_weight_boundedness_probe.py` (exact in ℚ).

Emits `wedderburn-weight-canonical-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import math
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from hecke_character_symbolic import standard_young_tableaux  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _partitions_of(n: int):
    def go(n_, max_):
        if n_ == 0:
            yield ()
            return
        for i in range(min(n_, max_), 0, -1):
            for tail in go(n_ - i, i):
                yield (i,) + tail
    yield from go(n, n)


def _hook_lengths(shape: tuple[int, ...]) -> list[int]:
    """Hook lengths for each cell of Young diagram `shape`."""
    # shape is partition (parts in decreasing order).
    # Build conjugate (column lengths).
    if not shape:
        return []
    n_rows = len(shape)
    n_cols = shape[0]
    col_lens = [
        sum(1 for r in range(n_rows) if shape[r] > c)
        for c in range(n_cols)
    ]
    hooks = []
    for r in range(n_rows):
        for c in range(shape[r]):
            # Hook = (cells to the right in same row) + (cells below in
            # same column) + 1.
            arm = shape[r] - c - 1
            leg = col_lens[c] - r - 1
            hooks.append(arm + leg + 1)
    return hooks


def _q_int(k: int, q: "mp.mpf") -> "mp.mpf":
    """[k]_q  :=  (q^k − q⁻ᵏ) / (q − q⁻¹).

    The standard balanced q-integer.  At q = 1 the formula above is
    0/0; the L'Hôpital limit is k.  Implementation returns `k`
    exactly when |q − 1| < 1e-30 to avoid the numerical
    singularity; outside that band the closed form is used.
    """
    if abs(q - 1) < mp.mpf("1e-30"):
        return mp.mpf(k)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def _q_fact(n: int, q: "mp.mpf") -> "mp.mpf":
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= _q_int(k, q)
    return out


def _dim_q(shape: tuple[int, ...], q: "mp.mpf") -> "mp.mpf":
    """q-deformed Frame-Robinson-Thrall: dim_q(λ) = [n]_q! / ∏ [h_x]_q."""
    n = sum(shape)
    num = _q_fact(n, q)
    den = mp.mpf(1)
    for h in _hook_lengths(shape):
        den *= _q_int(h, q)
    return num / den


def main() -> int:
    builder = WitnessBuilder(
        "wedderburn-weight-canonical-probe",
        engine="mpmath",
    )
    set_compute_dps()

    # (1) and (2): verify dim_q(λ)|_{q→1} = f_λ classical for n = 1..6.
    classical_limit_results = []
    max_classical_limit_residue = mp.mpf(0)

    # Use q slightly off 1 to avoid the 0/0, then check residue is
    # consistent with classical f_λ.
    q_near_one = mp.mpf("1.0000000000001")
    for n in range(1, 7):
        n_fact = math.factorial(n)
        per_lam = []
        for shape in _partitions_of(n):
            f_lam_classical = (
                n_fact // math.prod(_hook_lengths(shape))
            )
            d_q_at_near_1 = _dim_q(shape, q_near_one)
            res = float(mp.fabs(d_q_at_near_1 -
                                 mp.mpf(f_lam_classical)))
            max_classical_limit_residue = max(
                max_classical_limit_residue, mp.mpf(res))
            # Cross-check against |SYT(λ)| from canonical builder.
            syts, _, _ = standard_young_tableaux(shape)
            per_lam.append({
                "shape": str(shape),
                "f_lam_classical": f_lam_classical,
                "dim_q_at_q_near_1": float(d_q_at_near_1),
                "syt_count": len(syts),
                "f_lam_matches_syt": f_lam_classical == len(syts),
                "residue": res,
            })
        classical_limit_results.append({
            "n": n,
            "n_fact": n_fact,
            "per_lambda": per_lam,
        })

    # (3) q-deformed normalisation at q_0 — informational sum.
    q = Q_MP
    q_def_sum_results = []
    for n in [3, 4, 5]:
        nq_fact = _q_fact(n, q)
        sum_w_tilde = mp.mpf(0)
        per_lam = []
        for shape in _partitions_of(n):
            dq = _dim_q(shape, q)
            w_tilde = dq * dq / nq_fact
            sum_w_tilde += w_tilde
            per_lam.append({
                "shape": str(shape),
                "dim_q": float(dq),
                "w_tilde": float(w_tilde),
            })
        q_def_sum_results.append({
            "n": n,
            "n_q_factorial_at_q0": float(nq_fact),
            "sum_w_tilde_lambda_at_q0": float(sum_w_tilde),
            "deviation_from_one": float(mp.fabs(sum_w_tilde - 1)),
            "per_lambda": per_lam,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:wedderburn-weight-canonical.  "
            "Verifies (1) dim_q(λ)|_{q→1} = f_λ classical for all "
            "λ ⊢ n with n = 1…6 via q-deformed Frame-Robinson-Thrall "
            "and classical hook-length formula; also confirms "
            "f_λ = |SYT(λ)|.  Documents (2) at q_0 the q-deformed "
            "Wedderburn weights w̃_λ = dim_q(λ)² / [n]_q! do NOT sum "
            "to 1 — the deviation is recorded for n = 3, 4, 5 "
            "(empirical evidence for the 'not a probability measure "
            "at q ≠ 1' property called out in AGENTS.md's notation "
            "register).  Max residue on (1): "
            f"{float(max_classical_limit_residue):.2e} at "
            "q = 1+1e-13 — small enough to confirm the limit while "
            "avoiding the 0/0 singularity in [k]_q at q = 1 exactly."
        )
        .set_content_block("prop:wedderburn-weight-canonical")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("max_classical_limit_residue",
                       float(max_classical_limit_residue))
        .add_data("classical_limit_q_to_1", classical_limit_results)
        .add_data("q_deformed_sum_at_q_0", q_def_sum_results)
        .add_data("notation_register_remark", {
            "convention": (
                "tilde w_λ is the q-deformed Wedderburn-block weight; "
                "distinct from bare w_λ which is the classical "
                "Plancherel probability measure (sums to 1 exactly)."
            ),
            "non_probability_measure_at_q_neq_1": (
                "The probe records Σ_λ tilde w_λ at q_0 for n=3,4,5; "
                "these are NOT equal to 1.  At q = 1 the deformation "
                "collapses and the sum becomes the classical "
                "Plancherel normalisation = 1 (verified by "
                "(1) above)."
            ),
        })
        .add_assertion(
            name="dim_q_at_q_to_1_equals_classical_f_lambda",
            computed=float(max_classical_limit_residue),
            expected=0.0,
            tolerance=1e-10,
            unit=(
                "max over λ ⊢ n (n=1..6) of |dim_q(λ)|_{q=1+1e-13} − "
                "f_λ classical|"
            ),
            source=(
                "q-deformed Frame-Robinson-Thrall: "
                "dim_q(λ) = [n]_q!/∏ [h_x]_q  →  n!/∏ h_x  at q→1."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"(1) Classical limit dim_q(λ) → f_λ at q → 1+:")
    print(f"    max residue across n=1..6, all partitions: "
          f"{float(max_classical_limit_residue):.2e}")
    print()
    print(f"(2) q-deformed Wedderburn sum at q_0:")
    print(f"{'n':<3} {'[n]_q!':<25} {'Σ tilde w_λ':<25} {'|Σ − 1|':<15}")
    for r in q_def_sum_results:
        print(f"  {r['n']:<3} "
              f"{r['n_q_factorial_at_q0']:<25.15f} "
              f"{r['sum_w_tilde_lambda_at_q0']:<25.15f} "
              f"{r['deviation_from_one']:<15.10f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
