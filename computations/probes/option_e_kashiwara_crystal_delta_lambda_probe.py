#!/usr/bin/env python3
"""Option E (Kashiwara crystal) Δ_λ closure probe — formalize-first
multi-candidate structural test for the deuteron Δ_λ system.

Executes the §4 plan of
[`docs/audits/2026-06-04-option-e-kashiwara-crystal-scope.md`](../../docs/audits/2026-06-04-option-e-kashiwara-crystal-scope.md).

Per the Δ_λ-gate audit (2026-05-18-delta-lambda-gating-context.md),
six closure ansätze (Frobenius co-Casimir, Demazure-fibre, LP-
Plancherel, LP-Frobenius, Occam, Wenzl-bridge augmented) have failed
on the deuteron. Option E (Kashiwara crystal at q→1) is the only
TBD entry. AGENTS.md is explicit: "do not propose a seventh fit-based
ansatz" — so this probe is parameter-free.

Each candidate fixes `Δ_λ = c(λ)` in closed form BEFORE the sum runs,
no LP, no fitted scalar. The deuteron sum
`S = Σ_{λ⊢6} y_λ(q₀) · χ^λ(β_D) · c(λ)` is then a single number per
candidate, compared to the target `−B_D / m_e = −4.353`.

Five candidates:
  E1 — content sum n(λ) = Σ_i (i−1)·λ_i  (1-indexed rows)
  E2 — co-content n(λ') = Σ_i C(λ_i, 2)
  E3 — dim ratio f^λ / dim_q(V_λ)|_{q₀}
  E4 — charge-zero control (Δ_λ ≡ 0; expect S = 0)
  E5 — ordinary dimension f^λ (sanity: under normalized trace,
       Σ y_λ(1)·f^λ ≈ 1 at q→1; not the target)

Verdict: EXACT-MATCH (|rel_err| < 1e-12) / NEAR-MATCH (< 5 %) /
REFUTED otherwise.

EXPLORATORY. No production code, content blocks, or production
witnesses changed. Emits
`option-e-kashiwara-crystal-delta-lambda-probe.witness.json`.
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

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# Empirical target — audit-doc convention `target_signed = -B_D / m_e`
# (B_D ≈ 2.2245 MeV; m_e ≈ 0.51099895069 MeV → −4.35313...).  Hard-pin
# to the audit-doc rounded value −4.353 used for the gate test.
TARGET_SIGNED = mp.mpf("-4.353")
TARGET_PRECISE = mp.mpf("-2.2245") / mp.mpf("0.51099895069")

# Canonical 50-dps q₀ — matches every chi-cache witness header.
Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"


# ── Partitions + hook-length combinatorics ──


def partitions_of(n: int) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, acc: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(acc))
            return
        for p in range(min(remaining, max_part), 0, -1):
            rec(remaining - p, p, acc + [p])

    rec(n, n, [])
    return out


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    hooks: list[int] = []
    L = len(lam)
    for i in range(L):
        for j in range(lam[i]):
            arm = lam[i] - 1 - j
            leg = sum(1 for k in range(i + 1, L) if lam[k] > j)
            hooks.append(arm + leg + 1)
    return hooks


def ordinary_dim(lam: tuple[int, ...]) -> int:
    """f^λ = n! / Π hook lengths."""
    import math
    n = sum(lam)
    prod = 1
    for h in hook_lengths(lam):
        prod *= h
    return math.factorial(n) // prod


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sum(q ** (2 * k - (n - 1)) for k in range(n))


def q_factorial_sym(n: int, q: sp.Expr) -> sp.Expr:
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out = sp.expand(out * q_number_sym(k, q))
    return out


def dim_q_sym(lam: tuple[int, ...], q: sp.Expr) -> sp.Expr:
    """q-Hecke Wedderburn dim via the q-hook formula."""
    n = sum(lam)
    num = q_factorial_sym(n, q)
    den = sp.Integer(1)
    for h in hook_lengths(lam):
        den = sp.expand(den * q_number_sym(h, q))
    return sp.cancel(num / den)


def conjugate_partition(lam: tuple[int, ...]) -> tuple[int, ...]:
    """λ' — the transpose of λ."""
    if not lam:
        return ()
    L = lam[0]
    return tuple(sum(1 for p in lam if p > j) for j in range(L))


# ── Five crystal-statistic candidates ──


def candidate_E1_macdonald_n_lambda(lam: tuple[int, ...]) -> int:
    """E1 — Macdonald `n(λ) = Σ_{x∈λ} (row(x) − 1) = Σ_i (i−1)·λ_i`
    (1-indexed rows).

    This is the standard Macdonald row-index statistic, NOT the
    cell-content `col(x) − row(x)` (Copilot review caught the earlier
    mis-labelling). Canonical bias toward column shapes; companion
    statistic to E2's `n(λ')` via `n(λ) + n(λ') = C(|λ|, 2)`.
    """
    return sum(i * lam_i for i, lam_i in enumerate(lam))


def candidate_E2_co_content(lam: tuple[int, ...]) -> int:
    """E2 — n(λ') = Σ_{x∈λ} (col(x) − 1) = Σ_i C(λ_i, 2).

    Crystal interpretation: sum of co-contents (= contents of the
    conjugate partition).  Canonical bias toward row shapes.
    """
    return sum(p * (p - 1) // 2 for p in lam)


def candidate_E3_dim_ratio(lam: tuple[int, ...], q_0: mp.mpf) -> mp.mpf:
    """E3 — f^λ / dim_q(V_λ)|_{q₀}.

    The classical-to-q dimension ratio EVALUATED AT q₀ (not a q→1
    limit — that limit equals 1 since dim_q(V_λ) → f^λ; Copilot review
    caught the earlier mis-labelling). At the substrate anchor the
    ratio measures how far the q-deformation deviates from the
    classical irrep dimension.
    """
    q_sym = sp.Symbol("q", positive=True)
    dq_sym = dim_q_sym(lam, q_sym)
    dq_at_q0 = mp.mpf(str(sp.N(dq_sym.subs(q_sym, sp.Float(str(q_0), 50)), 50)))
    return mp.mpf(ordinary_dim(lam)) / dq_at_q0


def candidate_E4_charge_zero(lam: tuple[int, ...]) -> int:
    """E4 — control: Δ_λ ≡ 0.  Should give S = 0."""
    return 0


def candidate_E5_dim(lam: tuple[int, ...]) -> int:
    """E5 — f^λ.  Sanity: at q→1, Σ_λ y_λ(1)·f^λ ≈ 1 (normalized
    Markov trace at the classical limit).  Not the target."""
    return ordinary_dim(lam)


# ── Witness loaders ──


def _load_y_lambda_n(n: int) -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "y-lambda-at-q0.witness.json"
    raw = json.loads(path.read_text())["data"]["by_n"]
    return {
        tuple(row["partition"]): mp.mpf(row["y_at_q0_50dps"])
        for row in raw[str(n)]
    }


def _load_chi_deuteron_h6() -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "chi-deuteron-h6-at-q0-50dps.witness.json"
    raw = json.loads(path.read_text())
    return {
        tuple(entry["partition"]): mp.mpf(entry["chi_lambda"])
        for entry in raw["by_partition"]
    }


def _verdict(rel_err: mp.mpf) -> str:
    if abs(rel_err) < mp.mpf("1e-12"):
        return "EXACT-MATCH"
    if abs(rel_err) < mp.mpf("5e-2"):
        return "NEAR-MATCH (< 5 %)"
    return "REFUTED"


def main() -> int:
    w = WitnessBuilder(
        "option-e-kashiwara-crystal-delta-lambda-probe",
        engine="sympy+mpmath",
    )
    w.set_audit_only("docs/audits/2026-06-04-option-e-kashiwara-crystal-scope.md")
    w.set_description(
        "Option E (Kashiwara crystal at q→1) for Δ_λ closure — "
        "parameter-free multi-candidate test on the deuteron (λ⊢6, "
        "11 partitions). Five no-fit crystal-statistic candidates "
        "(E1 content sum, E2 co-content, E3 dim ratio, E4 charge-zero "
        "control, E5 ordinary dimension); each c(λ) is closed-form "
        "and fixed BEFORE the sum runs. Compares Σ_λ y_λ·χ^λ·c(λ) at "
        "q₀ to -B_D/m_e = -4.353. EXPLORATORY — no production code."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    parts6 = partitions_of(6)
    y_by_lam = _load_y_lambda_n(6)
    chi_by_lam = _load_chi_deuteron_h6()

    # Coverage check (no silent skip).
    missing_y = [list(lam) for lam in parts6 if lam not in y_by_lam]
    missing_chi = [list(lam) for lam in parts6 if lam not in chi_by_lam]
    if missing_y or missing_chi:
        raise RuntimeError(
            f"missing y_λ for {missing_y} or χ^λ for {missing_chi}; "
            f"refresh the n=6 caches before re-running."
        )

    candidates = [
        ("E1", "macdonald_n_lambda",
         candidate_E1_macdonald_n_lambda,
         "Δ_λ = n(λ) = Σ_i (i−1)·λ_i  (Macdonald row-index statistic)"),
        ("E2", "co_content_n_lambda_prime",
         candidate_E2_co_content, "Δ_λ = n(λ') = Σ_i C(λ_i, 2)"),
        ("E3", "dim_ratio_f_over_dim_q",
         lambda lam: candidate_E3_dim_ratio(lam, q_0),
         "Δ_λ = f^λ / dim_q(V_λ)|_{q₀}"),
        ("E4", "charge_zero_control",
         candidate_E4_charge_zero, "Δ_λ ≡ 0 (control)"),
        ("E5", "ordinary_dim_f_lambda",
         candidate_E5_dim, "Δ_λ = f^λ"),
    ]

    print("=" * 78)
    print("Option E (Kashiwara crystal) Δ_λ probe — deuteron")
    print("=" * 78)
    print(f"  target (signed) = -B_D/m_e = {float(TARGET_SIGNED):+.6f}")
    print(f"  target (precise from CODATA m_e + AME B_D) = "
          f"{float(TARGET_PRECISE):+.6f}")
    print(f"  partitions of 6 = {len(parts6)} (expect 11)")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("target_signed", str(TARGET_SIGNED))
    w.add_parameter("target_precise_from_codata_ame", str(TARGET_PRECISE))
    w.add_parameter("partitions_of_6_count", len(parts6))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "scope_doc",
        "docs/audits/2026-06-04-option-e-kashiwara-crystal-scope.md",
    )

    results = []
    for code, name, c_fn, formula in candidates:
        S = mp.mpf(0)
        per_lambda = []
        for lam in parts6:
            c_lam = c_fn(lam)
            c_lam_mpf = mp.mpf(c_lam) if not isinstance(c_lam, mp.mpf) else c_lam
            term = y_by_lam[lam] * chi_by_lam[lam] * c_lam_mpf
            S += term
            per_lambda.append({
                "partition": list(lam),
                "c_lambda": str(c_lam_mpf),
                "y_chi_c": str(term),
            })
        delta = S - TARGET_SIGNED
        rel_err = delta / TARGET_SIGNED if TARGET_SIGNED != 0 else mp.mpf("inf")
        verdict = _verdict(rel_err)
        print(f"\n  {code} ({name}):  {formula}")
        print(f"      S = {float(S):+.10f}  vs target {float(TARGET_SIGNED):+.6f}")
        print(f"      rel_err = {float(rel_err):+.3e}  →  {verdict}")
        results.append({
            "code": code,
            "name": name,
            "formula": formula,
            "S_at_q0": str(S),
            "target": str(TARGET_SIGNED),
            "delta": str(delta),
            "relative_error": str(rel_err),
            "verdict": verdict,
            "per_lambda": per_lambda,
        })

    w.add_data("candidates", results)

    # Synthesis
    any_match = any(r["verdict"] in ("EXACT-MATCH", "NEAR-MATCH (< 5 %)")
                    for r in results)
    if any_match:
        synthesis = (
            "At least one Kashiwara crystal-statistic candidate matches "
            "the deuteron Δ_λ target within 5 % with zero free "
            "parameters — the Δ_λ gate opens for deuteron. "
            "Recommend immediate Lean formalization of the categorical "
            "derivation behind the matching statistic and replication "
            "across T, ³He, ⁴He."
        )
    else:
        synthesis = (
            "All five Kashiwara crystal-statistic candidates REFUTED. "
            "The no-fit crystal-statistic family is now closed for "
            "deuteron Δ_λ. Combined with the six prior failures in "
            "the Δ_λ-gate audit (Frobenius co-Casimir, Demazure-fibre, "
            "LP-Plancherel, LP-Frobenius, Occam, Wenzl-bridge), this "
            "leaves only research-grade categorical paths (GAP-A-3 "
            "categorical brane-tower level selection; GAP-A-4 ρ general "
            "rule) as productive directions for Δ_λ binding-energy "
            "closure. A seventh fit-based ansatz is forbidden by "
            "AGENTS.md."
        )
    w.add_data("synthesis_verdict", synthesis)
    print(f"\n  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Witness assertion: E4 control sums to exactly 0 (sanity for the
    # arithmetic pipeline; if this fails the whole probe is wrong).
    e4_S = mp.mpf([r["S_at_q0"] for r in results if r["code"] == "E4"][0])
    w.add_assertion(
        "charge_zero_control_sums_to_zero",
        computed=float(abs(e4_S)),
        expected=0.0,
        tolerance=1e-40,
        source=(
            "E4 control: with c(λ) ≡ 0, every term y_λ·χ^λ·c(λ) = 0 so "
            "the sum must be exactly 0; any deviation is a bug in the "
            "summation pipeline, not a crystal-statistic finding."
        ),
    )

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
