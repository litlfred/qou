#!/usr/bin/env python3
"""Markov-stabilization trace-level axis probe for the H₃→H₄ jump.

Executes the §3 plan of
[`docs/audits/2026-06-04-markov-stab-trace-axis-scope.md`](../../docs/audits/2026-06-04-markov-stab-trace-axis-scope.md).

Formalize-first (PR #1826): the structural invariant is the Markov
stabilization parameter

    z = 1 / (q^½ + q^{-½})        ([`hecke_symbolic.py:46`])

which at the substrate q₀ is z ≈ 0.4993 < 1, whereas the production
`linking_weight ≈ 2.53 > 1`.  A single stabilization β ↦ β·σ₃ scales
the trace by z < 1, so it CANNOT be a >1 multiplier — the naive
reading is dead before any scan.  The probe records that obstruction
and tests the two surviving candidates exactly:

  M1 — linking_weight ?= tr_M(1_{H₄}) = Σ_{λ⊢4} y_λ·f^λ  (identity
       trace; f^λ = ordinary/hook dimension, χ^λ(1) = f^λ).
  M2 — (1/4)·Σ_{λ⊢4} dim_q ?= z^{±k}·(clean H₃ quantity), k ∈ {1,2}.

EXPLORATORY — no production code, content, or production witnesses
changed.  Emits `markov-stab-trace-axis-probe.witness.json`.
"""
from __future__ import annotations

# Path bridge — `_path_bridge` puts computations/ + cluster subdirs on
# sys.path, so `_precision`/`witness_base` resolve (single approach).
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

# Canonical 50-dps q₀ anchor — matches every chi-cache witness header.
Q_0_50DPS = "1.1099785955573347198997632204832250266562084087802"


# ── Young-diagram combinatorics (shared with the Option B probe) ──


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
    """f^λ = n! / ∏ hook lengths (= χ^λ(1), the dimension of V_λ)."""
    import math
    n = sum(lam)
    prod = 1
    for h in hook_lengths(lam):
        prod *= h
    return math.factorial(n) // prod


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    """Symmetric q-number [n]_q = q^{-(n-1)}·(1 + q² + … + q^{2(n-1)})."""
    if n == 0:
        return sp.Integer(0)
    return sum(q ** (2 * k - (n - 1)) for k in range(n))


def q_factorial_sym(n: int, q: sp.Expr) -> sp.Expr:
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out = sp.expand(out * q_number_sym(k, q))
    return out


def dim_q_sym(lam: tuple[int, ...], q: sp.Expr) -> sp.Expr:
    """q-Hecke Wedderburn dimension via the q-hook formula."""
    n = sum(lam)
    num = q_factorial_sym(n, q)
    den = sp.Integer(1)
    for h in hook_lengths(lam):
        den = sp.expand(den * q_number_sym(h, q))
    return sp.cancel(num / den)


def linking_weight_family_a_sym(q: sp.Expr) -> sp.Expr:
    return (3 * q ** 2 + 4 + 3 * q ** (-2)) / 4


def z_markov_sym(q: sp.Expr) -> sp.Expr:
    """z = 1 / (q^½ + q^{-½}) — Markov stabilization parameter
    (`hecke_symbolic.py:46`)."""
    qh = sp.sqrt(q)
    return 1 / (qh + 1 / qh)


def _load_y_lambda_n(n: int) -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "y-lambda-at-q0.witness.json"
    raw = json.loads(path.read_text())["data"]["by_n"]
    return {
        tuple(row["partition"]): mp.mpf(row["y_at_q0_50dps"])
        for row in raw[str(n)]
    }


def main() -> int:
    w = WitnessBuilder("markov-stab-trace-axis-probe", engine="sympy+mpmath")
    w.set_audit_only("docs/audits/2026-06-04-markov-stab-trace-axis-scope.md")
    w.set_description(
        "Markov-stabilization trace-level axis probe for the H₃→H₄ jump "
        "(PR #1762 chain; sibling #1841 Bratteli REFUTED, #1808 Option E "
        "lead). Formalize-first: records the z<1 direction obstruction, "
        "then tests M1 (identity trace tr_M(1_{H₄}) = Σ_{λ⊢4} y_λ·f^λ) "
        "and M2 (z^{±k}·linking_weight vs clean H₃ quantities) exactly. "
        "EXPLORATORY — no production code or witnesses changed."
    )

    q = sp.Symbol("q", positive=True)
    q_0 = mp.mpf(Q_0_50DPS)
    q_0_sp = sp.Float(Q_0_50DPS, 50)

    print("=" * 78)
    print("Markov-stabilization trace-level axis probe")
    print("=" * 78)

    # ── §2. The direction obstruction (formalize-first kill) ──
    z_sym = z_markov_sym(q)
    z_at_q0 = mp.mpf(str(sp.N(z_sym.subs(q, q_0_sp), 50)))
    lw_sym = linking_weight_family_a_sym(q)
    lw_at_q0 = mp.mpf(str(sp.N(lw_sym.subs(q, q_0_sp), 50)))

    print(f"\n  z(q₀)          = {float(z_at_q0):.10f}  (Markov stab. param)")
    print(f"  linking_weight = {float(lw_at_q0):.10f}")
    print(f"  z⁻¹(q₀)        = {float(1/z_at_q0):.10f}")
    obstruction = (z_at_q0 < 1) and (lw_at_q0 > 1)
    print(f"  Direction obstruction (z<1<linking_weight): {obstruction}")
    print("  → a single stabilization (factor z<1) cannot be a >1 multiplier")

    w.add_data("z_markov_at_q0", str(z_at_q0))
    w.add_data("z_markov_inv_at_q0", str(1 / z_at_q0))
    w.add_data("linking_weight_at_q0", str(lw_at_q0))
    w.add_data("direction_obstruction", bool(obstruction))
    w.add_data(
        "direction_obstruction_note",
        "z = 1/(q^½+q^{-½}) ≈ 0.4993 < 1 at q₀; linking_weight ≈ 2.53 > 1. "
        "A single Markov stabilization β↦β·σ₃ scales tr_M by z < 1, so it "
        "cannot produce the >1 linking_weight multiplier. The naive "
        "stabilization reading is structurally dead.",
    )
    w.add_assertion(
        "z_markov_below_one_linking_weight_above_one",
        computed=1.0 if obstruction else 0.0,
        expected=1.0,
        tolerance=0.5,
    )

    # ── M1: identity trace tr_M(1_{H₄}) = Σ_{λ⊢4} y_λ·f^λ ──
    y4 = _load_y_lambda_n(4)
    parts4 = partitions_of(4)
    tr_m_identity = mp.mpf(0)
    m1_rows = []
    for lam in parts4:
        f_lam = ordinary_dim(lam)
        y_lam = y4[lam]
        contrib = y_lam * f_lam
        tr_m_identity += contrib
        m1_rows.append({
            "partition": list(lam),
            "f_lambda": f_lam,
            "y_lambda_at_q0": str(y_lam),
            "contribution": str(contrib),
        })
    m1_delta = tr_m_identity - lw_at_q0
    m1_rel = abs(m1_delta) / abs(lw_at_q0)
    # tr_M(1) should be ~1 (the normalized Markov trace).
    m1_is_one = abs(tr_m_identity - 1) < mp.mpf("1e-6")
    m1_verdict = "REFUTED" if m1_rel > mp.mpf("1e-3") else "MATCH"

    print(f"\n  M1: tr_M(1_{{H₄}}) = Σ_{{λ⊢4}} y_λ·f^λ = {float(tr_m_identity):.10f}")
    print(f"      vs linking_weight = {float(lw_at_q0):.6f}  →  {m1_verdict}")
    print(f"      (tr_M(1) ≈ 1 confirms normalized Markov trace: {m1_is_one})")

    w.add_data("M1_identity_trace", {
        "verdict": m1_verdict,
        "tr_M_identity_H4_at_q0": str(tr_m_identity),
        "linking_weight_at_q0": str(lw_at_q0),
        "relative_error": str(m1_rel),
        "tr_M_identity_is_one": bool(m1_is_one),
        "note": (
            "tr_M(1_{H₄}) = 1 (the normalized Markov trace), NOT the "
            "linking_weight 2.53. The linking_weight is not the H₄ "
            "identity trace."
        ),
        "per_lambda": m1_rows,
    })

    # ── M2: z^{±k}·linking_weight vs clean H₃ quantities (exact) ──
    # Clean H₃ candidates (symbolic in q):
    sigma3 = sp.cancel(sum(dim_q_sym(lam, q) for lam in partitions_of(3)))
    candidates = {
        "(1/4)Sum_{lam|-3} dim_q": sp.cancel(sigma3 / 4),
        "Sum_{lam|-3} dim_q": sigma3,
        "[4]_q": q_number_sym(4, q),
        "[3]_q": q_number_sym(3, q),
        "[2]_q": q_number_sym(2, q),
    }
    # z^{±k}·linking_weight, exact symbolic.
    m2_tests = []
    m2_hit = False
    for k, label in [(1, "z^1"), (-1, "z^-1"), (2, "z^2"), (-2, "z^-2")]:
        scaled = sp.simplify(lw_sym * z_sym ** k)
        for cand_name, cand in candidates.items():
            diff = sp.simplify(sp.cancel(scaled - cand))
            if diff == 0:
                m2_hit = True
                m2_tests.append({
                    "form": f"linking_weight · {label}",
                    "equals": cand_name,
                    "verdict": "EXACT-MATCH",
                })
        scaled_q0 = mp.mpf(str(sp.N(scaled.subs(q, q_0_sp), 30)))
        m2_tests.append({
            "form": f"linking_weight · {label}",
            "value_at_q0": str(scaled_q0),
        })
    m2_verdict = "EXACT-MATCH" if m2_hit else "REFUTED"
    print(f"\n  M2: z^{{±k}}·linking_weight vs clean H₃ quantities → {m2_verdict}")
    for cand_name, cand in candidates.items():
        cval = mp.mpf(str(sp.N(cand.subs(q, q_0_sp), 30)))
        print(f"      {cand_name:28s} = {float(cval):.6f}")
    print(f"      z⁻¹·linking_weight at q₀ = "
          f"{float(lw_at_q0 / z_at_q0):.6f}  (z⁻¹≈2.003 near 2)")

    w.add_data("M2_z_renormalised", {
        "verdict": m2_verdict,
        "candidates_at_q0": {
            name: str(mp.mpf(str(sp.N(cand.subs(q, q_0_sp), 30))))
            for name, cand in candidates.items()
        },
        "tests": m2_tests,
        "note": (
            "No exact z^{±k}·linking_weight = clean-H₃ coincidence found; "
            "the z⁻¹ ≈ 2.003 near-2 is not exact (z⁻¹ = q^½+q^{-½}, "
            "irrational at q₀)."
        ),
    })

    # ── Synthesis ──
    synthesis = (
        "Markov stabilization at the trace level does NOT derive the "
        "linking_weight. The z<1 direction obstruction kills the naive "
        "form; M1 shows tr_M(1_{H₄}) = 1 (normalized trace), not 2.53; "
        "M2 finds no exact z^{±k} coincidence with a clean H₃ quantity. "
        "Combined with #1841 (Bratteli induction REFUTED), neither the "
        "algebra-tower nor the trace-stabilization axis derives the H₄ "
        "count. This points back to the production code's own framing: "
        "the linking_weight (1/4)·Σ_{λ⊢4} dim_q is a CODATA-implied "
        "near-match (`_li_2_q_util.py:298-313`), landing near "
        "λ = m_p/(m_e·Vol/ℏ²) ≈ 2.46, rather than a derived categorical "
        "count of either kind."
    )
    w.add_data("synthesis_verdict", synthesis)
    print(f"\n  SYNTHESIS:")
    for line in synthesis.split(". "):
        print(f"    {line.strip()}")

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
