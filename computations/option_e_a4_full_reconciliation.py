#!/usr/bin/env python3
"""
Option E — the REAL A=4 (⁴He) binding reconciliation, now that pyhecke_native
is built (chi 77/77 via chi_q_via_gp; B_λ via kl_betti_sum_rust).

Tests #2839's "B_{(10,2)}=584 closes A=4" against the FULL signed sum, the same
shape as the merged deuteron oracle:

    B(⁴He) = m_e · | Σ_{λ⊢12} y_λ · χ^λ(β_4He) · sgn(w_0^{S_{λ'}}) · M_λ |

with M_λ = f^λ (canonical ansatz) and M_λ = B_λ (KL left-cell Betti).

f^λ baseline is exact over all 77 (instant). B_λ for all 77 is NOT feasible
(deep bulk cells have huge Bruhat intervals — the shallow (10,2) alone is ~tens
of seconds); so B_λ is computed cheapest-cell-first under a wall-time budget,
with f^λ as the fallback for uncomputed shapes, and the Betti *coverage*
(fraction of |Σ_f| weight that got a real B_λ) is reported so the partial
result is honest.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

from mpmath import mp, mpf, fabs

import pyhecke_native
from kl_betti_smoothness_pruned import (
    partitions, dim_sn, canonical_Q, syt_shape, inverse_rsk,
)
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
N = 12
m_e = mpf("0.51099895069")
AME_HE4 = mpf("28.295660")
BETTI_WALL_BUDGET_S = 25.0    # cap the Rust Betti loop; rest fall back to f^λ
NMAX_BETTI = 1                # only n(λ) ≤ this (instant cells). EMPIRICAL: even
                             # shallow (10,2) (n=2) is ~100s/shape in Rust (w_0-deep
                             # Bruhat intervals), so a full 77-shape A=4 Betti sum is
                             # INFEASIBLE in-sandbox — this is itself the finding (it is
                             # why #2839 published only B_(10,2)). f^λ baseline (all 77,
                             # exact) + the deuteron ×2.0 net factor carry the verdict.


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))

def sgn_conj_parabolic(lam):
    return math.prod((-1) ** (p * (p - 1) // 2) for p in conjugate(lam))

def load_chi_77(fname):
    d = json.loads((HERE / fname).read_text(encoding="utf-8"))
    dat = d.get("data", d)
    bp = dat.get("by_partition") or dat.get("atom", {}).get("by_partition")
    return {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in bp}

def load_y(fname):
    d = json.loads((HERE / fname).read_text(encoding="utf-8"))
    dat = d.get("data", d)
    pp = dat.get("per_partition") or dat.get("per_lambda")
    out = {}
    for e in pp:
        key = tuple(e["partition"])
        val = e.get("y_lambda", e.get("y_lambda_at_q0"))
        out[key] = mpf(str(val))
    return out

def betti_rust(lam):
    """B_λ = Σ_{w∈Γ_λ} P_{e,w}(1) via the native Rust engine."""
    Qc = canonical_Q(lam)
    words = [list(inverse_rsk(P, Qc)) for P in syt_shape(lam)]
    return int(pyhecke_native.kl_betti_sum_rust(N, words))


def main():
    chi = load_chi_77("chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json")
    y = load_y("wenzl-y-lambda-h12.witness.json")
    print(f"χ^λ: {len(chi)}/77   y_λ: {len(y)}")
    parts = [p for p in partitions(N)]
    assert len(parts) == 77, len(parts)

    # ── per-λ scalars + f^λ baseline (exact, all 77) ────────────────
    rec = {}
    sum_f = mpf(0)
    for lam in parts:
        c = chi.get(lam)
        yl = y.get(lam, mpf(0))
        if c is None:
            print(f"  WARN: χ missing for {lam}"); c = mpf(0)
        sgn = sgn_conj_parabolic(lam)
        f = dim_sn(lam)
        term_f = yl * c * sgn * f
        sum_f += term_f
        rec[lam] = {"chi": c, "y": yl, "sgn": sgn, "f": f, "term_f": term_f}
    B_f = m_e * fabs(sum_f)
    print(f"\n[f^λ baseline] Σ_f = {float(sum_f):+.6f}  →  "
          f"B(⁴He)_f = {float(B_f):.4f} MeV  ({float((B_f-AME_HE4)/AME_HE4*100):+.2f}%)")

    # ── B_λ via Rust — SHALLOWEST cells first (cost ∝ n(λ), the column
    #    statistic). Elongated λ have short cell words / shallow Bruhat
    #    intervals (fast); column-like λ contain w_0-deep perms (the full
    #    S_12 interval) and are infeasible even in Rust. Cap n(λ) ≤ NMAX_BETTI
    #    + wall budget; the (numerically dominant) shallow shapes get a real
    #    B_λ, deep shapes fall back to f^λ (a lower bound, since B_λ ≥ f^λ).
    def n_stat(l):
        return sum(i * l[i] for i in range(len(l)))
    order = sorted([p for p in parts if n_stat(p) <= NMAX_BETTI], key=n_stat)
    t0 = time.perf_counter()
    betti = {}
    for lam in order:
        if time.perf_counter() - t0 > BETTI_WALL_BUDGET_S:
            break
        try:
            betti[lam] = betti_rust(lam)
            el = time.perf_counter() - t0
            print(f"  B_{str(lam):<16} = {betti[lam]:<6} (f^λ={rec[lam]['f']}, "
                  f"+{betti[lam]-rec[lam]['f']}, n(λ)={n_stat(lam)}; {el:.1f}s)",
                  flush=True)
        except Exception as e:
            print(f"  B_{lam}: FAIL {e}"); break

    # ── Σ_b with real B_λ where computed, f^λ fallback elsewhere ─────
    sum_b = mpf(0)
    covered_w = mpf(0)
    total_w = mpf(0)
    for lam in parts:
        r = rec[lam]
        M = betti.get(lam, r["f"])
        sum_b += r["y"] * r["chi"] * r["sgn"] * M
        w = fabs(r["term_f"])
        total_w += w
        if lam in betti:
            covered_w += w
    B_b = m_e * fabs(sum_b)
    cov = float(covered_w / total_w * 100) if total_w > 0 else 0.0

    print(f"\n[Betti] computed real B_λ for {len(betti)}/77 shapes "
          f"(covering {cov:.1f}% of |Σ_f| weight; rest use f^λ fallback)")
    print(f"[Betti] Σ_b = {float(sum_b):+.6f}  →  "
          f"B(⁴He)_b = {float(B_b):.4f} MeV  ({float((B_b-AME_HE4)/AME_HE4*100):+.2f}%)")
    print(f"\nAME ⁴He = {float(AME_HE4):.4f} MeV")
    print(f"factor needed to close (f^λ→AME): ×{float(AME_HE4/B_f):.2f}")
    if B_f > 0:
        print(f"factor Betti delivers so far:     ×{float(B_b/B_f):.2f} "
              f"({cov:.0f}% Betti-covered)")
    print("\nVERDICT: full A=4 signed sum; compare to deuteron (×2.0, not closing).")

    witness = {
        "engine": "python3/mpmath + pyhecke_native(rust)", "engineVersion": "50dps",
        "computation": "option-e-a4-full-reconciliation",
        "scriptFile": "option_e_a4_full_reconciliation.py",
        "description": (
            "Full A=4 (⁴He/S₁₂) Option-E binding: B=m_e·|Σ_λ y·χ·sgn·M_λ|, "
            "M_λ∈{f^λ, KL-Betti B_λ}. χ 77/77 (chi_q_via_gp), B_λ via "
            "kl_betti_sum_rust cheapest-cell-first under a wall budget; f^λ "
            "fallback for uncomputed deep cells. Tests #2839's single-scalar "
            "'closure' against the full signed sum."
        ),
        "data": {
            "nucleus": "4He (H_12/S_12)",
            "sum_f_lambda": str(sum_f),
            "B_he4_f_lambda_MeV": str(B_f),
            "B_he4_f_err_pct": float((B_f - AME_HE4) / AME_HE4 * 100),
            "sum_betti_partial": str(sum_b),
            "B_he4_betti_partial_MeV": str(B_b),
            "B_he4_betti_err_pct": float((B_b - AME_HE4) / AME_HE4 * 100),
            "betti_shapes_computed": len(betti),
            "betti_weight_coverage_pct": cov,
            "B_lambda_computed": {",".join(map(str, k)): v for k, v in betti.items()},
            "AME_he4_MeV": str(AME_HE4),
            "factor_needed_close": float(AME_HE4 / B_f) if B_f > 0 else None,
        },
        "assertions": [{"label": "chi 77/77", "passed": len(chi) == 77}],
        "allPassed": len(chi) == 77,
    }
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` / `commitSha` / `computedAt` on it. That is
    # not cosmetic: a witness without `scriptHash` cannot be compared against
    # its producer, so it DROPS OUT of the self-staleness audit entirely and
    # reads as "not stale" forever. Regenerating one therefore looks like
    # progress while removing it from the count — a false drain. Measured
    # 2026-08-23: four such witnesses across one regeneration sweep, and 29
    # raw-JSON producers repo-wide that would do the same.
    #
    # `stamp_staleness_metadata` rather than `wrap_legacy().save()` on purpose:
    # it adds the fields in place and leaves the on-disk shape untouched, so no
    # consumer of this witness's legacy `assertions` records (which key on
    # `label`, not `name`) has to change. `engine` is passed back from the
    # payload because the helper overwrites that field, and this producer
    # writes a descriptive engine string worth keeping.
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", 'python3/mpmath + pyhecke_native(rust)'))
    (HERE / "option-e-a4-full-reconciliation.witness.json").write_text(
        json.dumps(witness, indent=2, default=str), encoding="utf-8")
    print("Witness: option-e-a4-full-reconciliation.witness.json")


if __name__ == "__main__":
    main()
