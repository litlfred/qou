#!/usr/bin/env python3
"""GAP-A-3 P_λ bar-even admissibility probe — formalize-first narrowing.

Follow-up to `gap_a3_deuteron_p_lambda_channels_probe.py`, whose five
*content channels* (C1 sl₂ Schur–Weyl mult, C2 sl₃ Schur–Weyl mult, C3
sl₂ q-dim, C4 ≤2-row indicator, C5 zero control) were ALL REFUTED
numerically on the deuteron P_λ target. That probe asked "which content
channel reproduces the target?" and answered "none". This probe asks the
prior structural question the content-channel probe never checked:

    Which P_λ are even ADMISSIBLE as a categorical binding deviation?

The `cbnf` bean's non-fit direction
(`docs/audits/2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`)
sharpens GAP-A-3 to the two-layer factorisation Δ_λ(K) = A(K)·P_λ(K)
with the structural reading: since tr_M(β) = Σ_λ y_λ χ^λ(β) (Frobenius),
P_λ ≡ 1 recovers A(K)·tr_M(β_K) exactly, so **P_λ is the per-partition
deviation of binding from the flat trace distribution**, subject to a
**bar-even (λ ↔ λᵀ) admissibility constraint**: the bar involution
q ↦ q⁻¹ sends χ^λ ↦ χ^{λᵀ}, so any P_λ realised by a real, bar-symmetric
(Im q = 0 at the archimedean anchor; CLAUDE.md §"Im(q) at fibre vs
observable level") categorical deviation must satisfy P_λ = P_{λᵀ}.

THE NARROWING (formalize-first — the invariant prunes the class):

  1. The refuted content channels C1–C4 are all built from a *row-count
     selector* `rows(λ) ≤ k`. Row count is NOT transpose-invariant
     (rows(λᵀ) = λ₁ = columns(λ)), so these P_λ are bar-ODD-contaminated:
     they violate the admissibility constraint structurally, independent
     of any numerical target. Their refutation is therefore explained by
     symmetry, not coincidence — and the next P_λ ansatz must be
     transpose-invariant.

  2. The flat weight distribution w_λ = y_λ·χ^λ(β_D) is itself measured
     for bar-evenness (w_λ vs w_{λᵀ}). A bar-even substrate is the
     premise that makes "P_λ = P_{λᵀ}" the right admissibility class.

  3. Under any bar-even P_λ, the bar-ODD part of w is annihilated
     (Σ w_λ P_λ = Σ_orbits (Σ_{μ∈orbit} w_μ) P_orbit), so the achievable
     target space is the span of the bar-even orbit weights. We report
     that reachable budget and the orbit structure (5 transpose pairs +
     1 self-conjugate (3,2,1) at n=6).

DISCIPLINE. EXPLORATORY, derive-or-refute, zero free parameters. This is
a *narrowing/refutation* tool, NOT a 7th Δ_λ fit ansatz (it proposes no
new P_λ value — it rules a whole family inadmissible and constrains the
admissible family). No production code, content blocks, or production
witnesses changed. Emits
`gap-a3-plambda-bar-even-admissibility-probe.witness.json`.
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

Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"
VOL_HYP_D = mp.mpf("12.776")
M_E_MEV = mp.mpf("0.51099895069")
B_D_MEV = mp.mpf("2.2245")


# ── Young diagram combinatorics ──


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


def transpose(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r >= c) for c in range(1, max(lam) + 1))


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


# ── The refuted content channels (for admissibility re-test) ──


def C1_sl2_schur_weyl(lam):
    return ordinary_dim(lam) if len(lam) <= 2 else 0


def C2_sl3_schur_weyl(lam):
    return ordinary_dim(lam) if len(lam) <= 3 else 0


def C3_sl2_qdim(lam, q_0):
    if len(lam) > 2:
        return mp.mpf(0)
    lam1 = lam[0]
    lam2 = lam[1] if len(lam) > 1 else 0
    q_sym = sp.Symbol("q", positive=True)
    expr = q_number_sym(lam1 - lam2 + 1, q_sym)
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def C4_sl2_indicator(lam):
    return 1 if len(lam) <= 2 else 0


# ── Witness loaders (same caches as the content-channel probe) ──


def _load_y_lambda_n(n: int) -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "y-lambda-at-q0.witness.json"
    raw = json.loads(path.read_text())["data"]["by_n"]
    return {tuple(r["partition"]): mp.mpf(r["y_at_q0_50dps"]) for r in raw[str(n)]}


def _load_chi_deuteron_h6() -> dict[tuple, mp.mpf]:
    path = COMPUTE_DIR / "chi-deuteron-h6-at-q0-50dps.witness.json"
    raw = json.loads(path.read_text())
    return {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in raw["by_partition"]}


def _phase4_amplitude_D(q_0: mp.mpf) -> mp.mpf:
    """A(D) = Vol_hyp(D)/[8]_q · (q^{1/2}+q^{-1/2})^4  (Z=1 ⇒ [3]_q^0=1)."""
    q_sym = sp.Symbol("q", positive=True)
    eight_q = q_number_sym(8, q_sym)
    spin = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** 4
    expr = sp.Float(str(VOL_HYP_D), 50) / eight_q * spin
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def main() -> int:
    w = WitnessBuilder(
        "gap-a3-plambda-bar-even-admissibility-probe",
        engine="sympy+mpmath",
    )
    w.set_audit_only(
        "docs/audits/2026-06-20-gap-a3-plambda-bar-even-admissibility.md"
    )
    w.set_description(
        "GAP-A-3 P_λ bar-even (λ↔λᵀ) admissibility probe. Follow-up to the "
        "content-channel probe (C1–C4 all refuted): tests whether those "
        "refuted channels are even ADMISSIBLE under the transpose-invariance "
        "constraint a real bar-symmetric categorical deviation must satisfy, "
        "measures bar-evenness of the flat weight w_λ=y_λχ^λ(β_D), and "
        "reports the bar-even orbit budget. Formalize-first narrowing, no "
        "fit, no 7th ansatz. EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    parts6 = partitions_of(6)
    y = _load_y_lambda_n(6)
    chi = _load_chi_deuteron_h6()
    missing = [list(p) for p in parts6 if p not in y or p not in chi]
    if missing:
        raise RuntimeError(f"missing y_λ/χ^λ for {missing}; refresh n=6 caches.")

    A_D = _phase4_amplitude_D(q_0)
    target_after_A = (-B_D_MEV / M_E_MEV) / A_D

    # flat weights and their bar (transpose) partners
    wflat = {p: y[p] * chi[p] for p in parts6}
    tr_M = sum(wflat.values())

    print("=" * 78)
    print("GAP-A-3 P_λ bar-even (λ↔λᵀ) admissibility probe")
    print("=" * 78)
    print(f"  A(D) at q₀            = {float(A_D):+.6f}")
    print(f"  tr_M(β_D) = Σ y_λ χ^λ = {float(tr_M):+.8f}")
    print(f"  P_λ target            = −B(D)/(m_e·A(D)) = {float(target_after_A):+.6f}")

    # ── (1) transpose-orbit structure ──
    seen = set()
    orbits = []  # each: {"members":[...], "self": bool}
    for p in parts6:
        if p in seen:
            continue
        pT = transpose(p)
        if pT == p:
            orbits.append({"members": [p], "self": True})
            seen.add(p)
        else:
            orbits.append({"members": [p, pT], "self": False})
            seen.update({p, pT})
    n_pairs = sum(1 for o in orbits if not o["self"])
    n_self = sum(1 for o in orbits if o["self"])
    print(f"\n  transpose orbits: {n_pairs} pairs + {n_self} self-conjugate "
          f"({[list(o['members'][0]) for o in orbits if o['self']]})")

    # ── (2) admissibility re-test of the refuted content channels ──
    print("\n  ADMISSIBILITY of the refuted content channels (P_λ = P_{λᵀ}?):")
    channels = {
        "C1_sl2_schur_weyl": lambda p: mp.mpf(C1_sl2_schur_weyl(p)),
        "C2_sl3_schur_weyl": lambda p: mp.mpf(C2_sl3_schur_weyl(p)),
        "C3_sl2_qdim": lambda p: C3_sl2_qdim(p, q_0),
        "C4_sl2_indicator": lambda p: mp.mpf(C4_sl2_indicator(p)),
    }
    admissibility = {}
    for name, fn in channels.items():
        vals = {p: fn(p) for p in parts6}
        violations = []
        odd_norm = mp.mpf(0)
        for o in orbits:
            if o["self"]:
                continue
            a, b = o["members"]
            diff = vals[a] - vals[b]
            odd_norm += abs(diff)
            if abs(diff) > mp.mpf("1e-40"):
                violations.append({
                    "pair": [list(a), list(b)],
                    "P_lambda": float(vals[a]),
                    "P_lambdaT": float(vals[b]),
                })
        admissible = len(violations) == 0
        admissibility[name] = {
            "bar_even_admissible": admissible,
            "n_violating_pairs": len(violations),
            "bar_odd_norm": str(odd_norm),
            "violations": violations,
        }
        tag = "ADMISSIBLE" if admissible else f"INADMISSIBLE ({len(violations)} pairs break P_λ=P_λᵀ)"
        print(f"    {name:20} → {tag}")
        for v in violations:
            print(f"        {str(v['pair'][0]):12} vs {str(v['pair'][1]):12} : "
                  f"P={v['P_lambda']:.4f}  Pᵀ={v['P_lambdaT']:.4f}")

    # ── (3) bar-evenness of the flat substrate weight w_λ ──
    even_norm = mp.mpf(0)
    odd_norm = mp.mpf(0)
    per_orbit = []
    for o in orbits:
        if o["self"]:
            p = o["members"][0]
            even_norm += abs(wflat[p])
            per_orbit.append({"orbit": [list(p)], "self": True,
                              "w_even": str(wflat[p]), "w_odd": "0"})
        else:
            a, b = o["members"]
            we = (wflat[a] + wflat[b]) / 2
            wo = (wflat[a] - wflat[b]) / 2
            even_norm += abs(wflat[a] + wflat[b])
            odd_norm += abs(wflat[a] - wflat[b])
            per_orbit.append({"orbit": [list(a), list(b)], "self": False,
                              "w_a": str(wflat[a]), "w_b": str(wflat[b]),
                              "w_even_pair": str(we), "w_odd_pair": str(wo)})
    odd_frac = odd_norm / (even_norm + odd_norm) if (even_norm + odd_norm) else mp.mpf(0)
    print(f"\n  flat weight w_λ = y_λ·χ^λ(β_D) bar-decomposition:")
    print(f"    bar-even ℓ1 mass = {float(even_norm):.6f}")
    print(f"    bar-odd  ℓ1 mass = {float(odd_norm):.6f}")
    print(f"    bar-odd fraction = {float(odd_frac):.4%}  "
          f"({'substrate ~bar-even' if odd_frac < mp.mpf('0.05') else 'substrate carries bar-odd weight'})")

    # bar-even reachable budget: Σ over orbits of the (signed) even orbit weight
    even_budget = sum(
        (wflat[o["members"][0]] if o["self"]
         else wflat[o["members"][0]] + wflat[o["members"][1]])
        for o in orbits
    )
    print(f"    bar-even reachable Σw (P-orbit=1) = {float(even_budget):.8f}  "
          f"(= tr_M since P≡1 is bar-even)")

    # ── verdict ──
    inadmissible = [n for n, a in admissibility.items() if not a["bar_even_admissible"]]
    verdict = (
        f"NARROWING. The bar-even (λ↔λᵀ) admissibility constraint rules the "
        f"row-count content channels INADMISSIBLE independently of their "
        f"numerical refutation: {', '.join(inadmissible)} all break "
        f"P_λ = P_{{λᵀ}} (the `rows(λ) ≤ k` selector is not transpose-"
        f"invariant — rows(λᵀ) = columns(λ)). The flat substrate weight "
        f"w_λ = y_λ·χ^λ(β_D) is "
        + ("predominantly bar-even — bar-odd fraction "
           f"{float(odd_frac):.2%}), consistent with the premise that a real "
           f"bar-symmetric P_λ is the right admissibility class. "
           if odd_frac < mp.mpf("0.05") else
           f"carrying a substantial bar-odd component (fraction "
           f"{float(odd_frac):.2%}); "
           f"a bar-even P_λ annihilates it, so any deviation living in the "
           f"bar-odd sector is structurally unreachable. ")
        + f"Conclusion: GAP-A-3 P_λ must be a TRANSPOSE-INVARIANT functional "
        f"(e.g. of {{λ,λᵀ}}-symmetric statistics: n(λ)+n(λᵀ), symmetric "
        f"hook/content combinations), NOT a row-count or column-count "
        f"selector. This is a formalize-first refutation of the content-"
        f"channel family and a constraint on the admissible family — not a "
        f"new fitted P_λ (no 7th ansatz)."
    )
    print("\n  VERDICT:")
    for chunk in verdict.split(". "):
        print(f"    {chunk.strip()}")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("A_D_at_q0", str(A_D))
    w.add_parameter("tr_M_beta_D", str(tr_M))
    w.add_parameter("target_after_A_factored", str(target_after_A))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("transpose_orbits",
               {"n_pairs": n_pairs, "n_self_conjugate": n_self,
                "self_conjugate": [list(o["members"][0]) for o in orbits if o["self"]]})
    w.add_data("content_channel_admissibility", admissibility)
    w.add_data("flat_weight_bar_decomposition", {
        "bar_even_l1_mass": str(even_norm),
        "bar_odd_l1_mass": str(odd_norm),
        "bar_odd_fraction": str(odd_frac),
        "bar_even_reachable_sum": str(even_budget),
        "per_orbit": per_orbit,
    })
    w.add_data("verdict", verdict)

    w.add_assertion(
        "row_count_channels_bar_inadmissible",
        computed=len(inadmissible),
        expected=4,
        tolerance=0,
        source="All four row-count content channels C1–C4 must violate "
               "P_λ = P_{λᵀ} (rows(λ)≤k is not transpose-invariant).",
    )
    w.add_assertion(
        "self_conjugate_count_n6",
        computed=n_self,
        expected=1,
        tolerance=0,
        source="n=6 has exactly one self-conjugate partition, (3,2,1).",
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
