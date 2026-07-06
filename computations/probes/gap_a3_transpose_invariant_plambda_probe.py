#!/usr/bin/env python3
"""GAP-A-3 transpose-invariant P_λ candidate probe — formalize-first.

Direct continuation of `gap_a3_plambda_bar_even_admissibility_probe.py`
(merged PR #2522), which showed the refuted content channels C1–C4 are
bar-INADMISSIBLE: their `rows(λ) ≤ k` selector is not transpose-invariant.
The narrowing left a sharp instruction — GAP-A-3 P_λ must be a
**transpose-invariant functional** (P_λ = P_{λᵀ}).

This probe tests the natural transpose-invariant candidates. The key
structural observation that makes them admissible by construction:

  * The **hook-length multiset** of λ equals that of λᵀ (transpose permutes
    cells but preserves the multiset of hook lengths). Hence every
    symmetric function of the hook multiset is transpose-invariant:
    the Specht dimension f^λ = n!/∏h (so f^λ = f^{λᵀ}, classical), ∑h,
    ∑h², and the q-hook product ∏[h]_q.
  * n(λ) + n(λᵀ) is transpose-symmetric by construction (n(λ) = ∑(i−1)λ_i).

So C1/C2 (which used f^λ) failed ONLY because of the row cutoff, not f^λ.
The admissible candidates here drop the cutoff.

Candidates (each parameter-free; the probe asserts P_λ = P_{λᵀ} for each
before scoring it):

  T0 — constant control: P_λ = 1. Exposes the required scale
       c* = target / tr_M (whether a flat deviation is even the right sign).
  T1 — Specht dimension: P_λ = f^λ (= dim_λ, transpose-invariant).
  T2 — n(λ) + n(λᵀ): the row/column moment, transpose-symmetric.
  T3 — hook sum: P_λ = ∑ h (over the hook multiset).
  T4 — hook-square sum: P_λ = ∑ h².
  T5 — q-hook product at q₀: P_λ = ∏ [h]_q.

Each scored against the deuteron target −B(D)/(m_e·A(D)) ≈ −0.1895 with
the tiered verdict (exact / near-5% / near-50% / refuted). Underdetermined
single-equation match: a near-match is a lead, a clean refutation further
narrows. EXPLORATORY — no fit (no free parameter is tuned; T0's c* is
reported, not used to "wire" anything), no production rewire, no 7th Δ_λ
ansatz. Emits `gap-a3-transpose-invariant-plambda-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import json
from pathlib import Path

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import (  # noqa: E402
    hook_lengths,
    dim_lambda,
    conjugate_partition as transpose,
)

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = "1.1099785955573347198997632204832250266562084087802"
VOL_HYP_D = mp.mpf("12.776")
M_E_MEV = mp.mpf("0.51099895069")
B_D_MEV = mp.mpf("2.2245")


def partitions_of(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, acc: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(acc))
            return
        for p in range(min(remaining, max_part), 0, -1):
            rec(remaining - p, p, acc + [p])

    rec(n, n, [])
    return out


def n_statistic(lam: tuple[int, ...]) -> int:
    """n(λ) = Σ_i (i−1)·λ_i  (0-indexed rows)."""
    return sum(i * part for i, part in enumerate(lam))


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sum(q ** (2 * k - (n - 1)) for k in range(n))


def q_hook_product(lam: tuple[int, ...], q_0: mp.mpf) -> mp.mpf:
    """∏ [h]_q over the hook multiset, evaluated at q₀ (balanced q-number).
    Transpose-invariant: the hook multiset is preserved under λ ↦ λᵀ."""
    q_sym = sp.Symbol("q", positive=True)
    prod = sp.Integer(1)
    for h in hook_lengths(lam):
        prod *= q_number_sym(h, q_sym)
    return mp.mpf(str(sp.N(prod.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


# ── transpose-invariant candidates ──


def T0_const(lam, q_0):
    return mp.mpf(1)


def T1_specht(lam, q_0):
    return mp.mpf(dim_lambda(lam))


def T2_n_plus_nT(lam, q_0):
    return mp.mpf(n_statistic(lam) + n_statistic(transpose(lam)))


def T3_hook_sum(lam, q_0):
    return mp.mpf(sum(hook_lengths(lam)))


def T4_hook_sq_sum(lam, q_0):
    return mp.mpf(sum(h * h for h in hook_lengths(lam)))


def T5_q_hook_product(lam, q_0):
    return q_hook_product(lam, q_0)


CANDIDATES = [
    ("T0", "constant_control", T0_const, "P_λ = 1"),
    ("T1", "specht_dim", T1_specht, "P_λ = f^λ (= dim_λ)"),
    ("T2", "n_plus_nT", T2_n_plus_nT, "P_λ = n(λ) + n(λᵀ)"),
    ("T3", "hook_sum", T3_hook_sum, "P_λ = Σ h"),
    ("T4", "hook_sq_sum", T4_hook_sq_sum, "P_λ = Σ h²"),
    ("T5", "q_hook_product", T5_q_hook_product, "P_λ = ∏ [h]_q at q₀"),
]


def _load_y_lambda_n(n: int) -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "y-lambda-at-q0.witness.json"
    raw = json.loads(path.read_text())["data"]["by_n"]
    return {tuple(r["partition"]): mp.mpf(r["y_at_q0_50dps"]) for r in raw[str(n)]}


def _load_chi_deuteron_h6() -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "chi-deuteron-h6-at-q0-50dps.witness.json"
    raw = json.loads(path.read_text())
    return {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in raw["by_partition"]}


def _phase4_amplitude_D(q_0: mp.mpf) -> mp.mpf:
    q_sym = sp.Symbol("q", positive=True)
    eight_q = q_number_sym(8, q_sym)
    spin = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** 4
    expr = sp.Float(str(VOL_HYP_D), 50) / eight_q * spin
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def _verdict(rel_err: mp.mpf) -> str:
    if abs(rel_err) < mp.mpf("1e-12"):
        return "EXACT-MATCH"
    if abs(rel_err) < mp.mpf("5e-2"):
        return "NEAR-MATCH (< 5 %)"
    if abs(rel_err) < mp.mpf("0.5"):
        return "NEAR-MATCH (< 50 %)"
    return "REFUTED"


def main() -> int:
    w = WitnessBuilder(
        "gap-a3-transpose-invariant-plambda-probe",
        engine="sympy+mpmath",
    )
    w.set_audit_only(
        "docs/audits/2026-06-20-gap-a3-transpose-invariant-plambda.md"
    )
    w.set_description(
        "GAP-A-3 transpose-invariant P_λ candidate probe (continuation of the "
        "bar-even admissibility narrowing, PR #2522). Tests six manifestly "
        "transpose-invariant candidates (constant, Specht dim, n(λ)+n(λᵀ), "
        "Σh, Σh², ∏[h]_q) against the deuteron P_λ target; each is asserted "
        "P_λ=P_{λᵀ} before scoring. Tiered verdict, no fit, no production "
        "rewire. EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    parts6 = partitions_of(6)
    y = _load_y_lambda_n(6)
    chi = _load_chi_deuteron_h6()
    missing = [list(p) for p in parts6 if p not in y or p not in chi]
    if missing:
        raise RuntimeError(f"missing y_λ/χ^λ for {missing}; refresh n=6 caches.")

    A_D = _phase4_amplitude_D(q_0)
    tr_M = mp.fsum(y[p] * chi[p] for p in parts6)
    target = (-B_D_MEV / M_E_MEV) / A_D

    print("=" * 78)
    print("GAP-A-3 transpose-invariant P_λ candidate probe")
    print("=" * 78)
    print(f"  A(D) at q₀  = {float(A_D):+.6f}")
    print(f"  tr_M(β_D)   = {float(tr_M):+.8f}")
    print(f"  P_λ target  = −B(D)/(m_e·A(D)) = {float(target):+.6f}")
    print(f"  flat scale  c* = target/tr_M  = {float(target / tr_M):+.6f}\n")

    results = []
    all_admissible = True
    for code, name, fn, formula in CANDIDATES:
        vals = {p: fn(p, q_0) for p in parts6}
        # admissibility self-check: P_λ = P_{λᵀ}
        admissible = all(abs(vals[p] - vals[transpose(p)]) < mp.mpf("1e-40")
                         for p in parts6)
        all_admissible = all_admissible and admissible
        S = mp.fsum(y[p] * chi[p] * vals[p] for p in parts6)
        rel = (S - target) / target if target != 0 else mp.mpf("inf")
        verdict = _verdict(rel) if code != "T0" else (
            f"SCALE c*={float(target / tr_M):+.4f} (control)")
        adm = "✓adm" if admissible else "✗INADM"
        print(f"  {code} ({name:18}) {formula:24} {adm}  "
              f"S={float(S):+.6f}  rel_err={float(rel):+.3e}  → {verdict}")
        results.append({
            "code": code, "name": name, "formula": formula,
            "bar_even_admissible": admissible,
            "S_at_q0": str(S), "target": str(target),
            "relative_error": str(rel), "verdict": verdict,
        })

    matched = [r["code"] for r in results
               if r["verdict"].startswith("NEAR-MATCH (< 5") or r["verdict"] == "EXACT-MATCH"]
    near50 = [r["code"] for r in results if r["verdict"] == "NEAR-MATCH (< 50 %)"]

    if matched:
        synthesis = (
            f"At least one transpose-invariant candidate ({', '.join(matched)}) "
            f"reproduces the deuteron P_λ target within 5% with zero free "
            f"parameters AND satisfies the bar-even admissibility constraint. "
            f"This is the first admissible P_λ lead post-#2522; recommend "
            f"cross-checking on T/³He/⁴He before any Lean formalization."
        )
    elif near50:
        synthesis = (
            f"No transpose-invariant candidate matches within 5%; "
            f"{', '.join(near50)} land within 50% (right order of magnitude). "
            f"The admissible family is constrained but not closed by these "
            f"single functionals — a derived (not fitted) symmetric "
            f"combination is the next formalize-first step."
        )
    else:
        synthesis = (
            "All natural transpose-invariant single functionals (Specht dim, "
            "n(λ)+n(λᵀ), Σh, Σh², ∏[h]_q) REFUTE the deuteron P_λ target. "
            "Bar-even admissibility is necessary but these elementary "
            "symmetric functionals are insufficient: GAP-A-3 P_λ, if it "
            "exists categorically, is a non-elementary transpose-invariant "
            "object (e.g. a knot-dependent symmetric combination), "
            "consistent with the s5-so3 keystone framing (conj:s5-so3-fiber-"
            "action) where the per-atom selection is operator-valued. No "
            "fit attempted; the elementary symmetric family is now excluded."
        )
    print(f"\n  SYNTHESIS:\n    {synthesis}")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("A_D_at_q0", str(A_D))
    w.add_parameter("tr_M_beta_D", str(tr_M))
    w.add_parameter("target_after_A_factored", str(target))
    w.add_parameter("flat_scale_c_star", str(target / tr_M))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("candidates", results)
    w.add_data("synthesis_verdict", synthesis)

    w.add_assertion(
        "all_candidates_transpose_invariant",
        computed=all_admissible,
        expected=True,
        tolerance=0.0,
        source="Every candidate P_λ must satisfy P_λ = P_{λᵀ} (the "
               "admissibility constraint the candidates are built to meet).",
    )

    out = w.save()
    try:
        rel = out.relative_to(COMPUTE_DIR.parent)
    except ValueError:
        rel = out
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
