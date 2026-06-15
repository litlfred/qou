#!/usr/bin/env python3
"""GAP-A-3 deuteron P_λ content-channel probe — formalize-first.

Implements the §4 probe plan of
[`docs/audits/2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](../../docs/audits/2026-06-04-gap-a3-brane-tower-level-selection-scope.md).

The two-layer factorisation `Δ_λ(K) = A(K) · P_λ(K)` takes the
Phase-4 substrate-derived per-atom amplitude `A(K) ≈ |Δ_λ*(K)|` as
already-known and probes whether the per-partition projection
`P_λ(K)` follows a natural brane-tower content channel — NOT a
partition statistic of λ (those are closed by PR #1860).

For the deuteron (Z=1, N=1, A=2, n=6, 11 partitions of 6):

  A(D) = Vol_hyp(D) / [8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}
       = 12.776 / [8]_q · (q^{1/2}+q^{-1/2})^4
       ≈ 22.97 (matches Phase-4 |Δ_λ*(D)| = 22.96 to 0.07 %)

Target after factoring out A(D):

  Σ_{λ⊢6} y_λ(q₀) · χ^λ(β_D) · P_λ(D)  =  −B(D) / (m_e · A(D))  ≈  −0.1895

Five channel candidates, each parameter-free:

  C1 — sl_2 Schur–Weyl multiplicity: P_λ = f^λ if rows(λ) ≤ 2, else 0.
        (V_{1/2}^{⊗6} decomposition; selects ≤2-row partitions; the
        per-neutron `(q^{½}+q^{−½})^4` carrier in the Phase-4 amplitude
        suggests this is the natural spin channel.)
  C2 — sl_3 Schur–Weyl multiplicity: P_λ = f^λ if rows(λ) ≤ 3, else 0.
        (V_1^{⊗?} fundamental of SU(3); selects ≤3-row partitions; the
        per-extra-proton `[3]_q^2 = (dim_q V_1)^2` carrier suggests
        this color channel.)
  C3 — sl_2 q-dim: P_λ = [λ_1−λ_2+1]_q at q₀ if rows(λ) ≤ 2, else 0.
        (Quantum analog of C1; matches the per-neutron carrier's
        `(dim_q V_{1/2})^4 = (q^{½}+q^{−½})^4` literally.)
  C4 — sl_2 indicator: P_λ = 1 if rows(λ) ≤ 2, else 0.
        (Channel baseline: tests whether the ≤2-row indicator alone,
        with no per-irrep weight, recovers the target.)
  C5 — constant-zero control: P_λ ≡ 0. (Should give exactly 0.)

EXPLORATORY — no production code, content blocks, or production
witnesses changed. Emits
`gap-a3-deuteron-p-lambda-channels-probe.witness.json`.
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

# Canonical 50-dps q₀ — matches every chi-cache witness header.
Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"

# Phase-4 deuteron hyperbolic volume (canonical atomic braid closure,
# SnapPy JSJ value from `2026-05-19-delta-lambda-phase4-z4N-closure.md`
# §"Phase 4 — categorical observation"). Vol(D) = Vol(T) = 12.776
# at Z=1 (Phase 3 found Vol clusters by Z; N-direction is Seifert-
# fibered).
VOL_HYP_D = mp.mpf("12.776")

# CODATA m_e (MeV) at 50 dps; the binding energy is at lower precision.
M_E_MEV = mp.mpf("0.51099895069")
B_D_MEV = mp.mpf("2.2245")


# ── Young diagram combinatorics (same as the Option B + E probes) ──


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


# ── Five channel candidates for P_λ(D) ──


def channel_C1_sl2_schur_weyl(lam: tuple[int, ...]) -> int:
    """C1 — sl_2 Schur–Weyl multiplicity of V_λ in V_{1/2}^{⊗n}.

    Only partitions with ≤ 2 rows survive; the multiplicity is f^λ
    (ordinary irrep dimension of S_n). Partitions with > 2 rows have
    multiplicity 0 (no sl_2 image).
    """
    if len(lam) > 2:
        return 0
    return ordinary_dim(lam)


def channel_C2_sl3_schur_weyl(lam: tuple[int, ...]) -> int:
    """C2 — sl_3 Schur–Weyl multiplicity (≤ 3 rows; else 0).

    Color channel — the per-extra-proton carrier in the Phase-4
    amplitude is `[3]_q^2 = (dim_q V_1)^2`, where V_1 = (1,0) is the
    **defining/fundamental** 3-dim irrep of SU(3) (the rep labelled
    by the highest weight (1,0); NOT the 8-dim adjoint, which is
    (1,1) and has q-dim `[3]_q · [4]_q / [2]_q` ≠ `[3]_q^2` — Copilot
    review catch). Schur–Weyl: V_λ of S_n appears in the n-fold
    tensor power of the SU(3) defining rep iff λ has ≤ 3 rows.
    Partitions with > 3 rows have no sl_3 image.
    """
    if len(lam) > 3:
        return 0
    return ordinary_dim(lam)


def channel_C3_sl2_qdim(lam: tuple[int, ...], q_0: mp.mpf) -> mp.mpf:
    """C3 — sl_2 quantum dimension at q₀ if rows(λ) ≤ 2, else 0.

    For λ = (λ_1, λ_2) with λ_2 = 0 if single row, the corresponding
    sl_2 spin is j = (λ_1 − λ_2) / 2, and dim_q(V_j) = [2j+1]_q.
    Quantum analog of C1; matches the per-neutron carrier
    `(dim_q V_{1/2})^4 = (q^{1/2}+q^{-1/2})^4` literally.
    """
    if len(lam) > 2:
        return mp.mpf(0)
    lam1 = lam[0]
    lam2 = lam[1] if len(lam) > 1 else 0
    two_j_plus_1 = lam1 - lam2 + 1  # = 2j+1
    q_sym = sp.Symbol("q", positive=True)
    expr = q_number_sym(two_j_plus_1, q_sym)
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def channel_C4_sl2_indicator(lam: tuple[int, ...]) -> int:
    """C4 — pure ≤2-row indicator (channel baseline)."""
    return 1 if len(lam) <= 2 else 0


def channel_C5_zero_control(lam: tuple[int, ...]) -> int:
    """C5 — constant-zero control. Should give S = 0 exactly."""
    return 0


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


def _phase4_amplitude_D(q_0: mp.mpf) -> mp.mpf:
    """A(D) = Vol_hyp(D) / [8]_q · (q^{1/2}+q^{-1/2})^4  at q₀.

    Deuteron Z=1 N=1: [3]_q^{2(Z-1)} = [3]_q^0 = 1.
    """
    q_sym = sp.Symbol("q", positive=True)
    eight_q = q_number_sym(8, q_sym)
    spin_carrier = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** 4
    expr = sp.Float(str(VOL_HYP_D), 50) / eight_q * spin_carrier
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def _verdict(rel_err: mp.mpf, is_control: bool = False,
             S_abs: mp.mpf | None = None) -> str:
    """Channel verdict.

    For target-match channels (`is_control=False`): compare relative
    error vs target. For control channels (`is_control=True`):
    succeed when |S| is at machine zero (the control's *purpose*
    is `S = 0`, not matching the target). Copilot review on PR
    #1870 caught the prior conflation: a zero-control with a
    non-zero target trivially had `rel_err = -1` and printed
    REFUTED, which mis-stated the channel's purpose.
    """
    if is_control:
        if S_abs is None:
            S_abs = mp.mpf(0)
        if S_abs < mp.mpf("1e-40"):
            return "CONTROL OK (|S| ≈ 0)"
        return f"CONTROL FAIL (|S| = {mp.nstr(S_abs, 6)})"
    if abs(rel_err) < mp.mpf("1e-12"):
        return "EXACT-MATCH"
    if abs(rel_err) < mp.mpf("5e-2"):
        return "NEAR-MATCH (< 5 %)"
    if abs(rel_err) < mp.mpf("0.5"):
        return "NEAR-MATCH (< 50 %)"
    return "REFUTED"


def main() -> int:
    w = WitnessBuilder(
        "gap-a3-deuteron-p-lambda-channels-probe",
        engine="sympy+mpmath",
    )
    w.set_audit_only("docs/audits/2026-06-04-gap-a3-brane-tower-level-selection-scope.md")
    w.set_description(
        "GAP-A-3 deuteron P_λ content-channel probe (PR #1762 / "
        "post-#1864 productive direction). Tests the two-layer "
        "factorisation Δ_λ(D) = A(D)·P_λ(D), taking the Phase-4 "
        "substrate-derived A(D) ≈ 22.97 as already-known and probing "
        "whether P_λ(D) follows a natural brane-tower content "
        "channel. Five candidates (C1 sl_2 Schur–Weyl mult, C2 sl_3 "
        "Schur–Weyl mult, C3 sl_2 q-dim, C4 ≤2-row indicator, C5 "
        "zero control); each P_λ closed-form, no fit. EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    parts6 = partitions_of(6)
    y_by_lam = _load_y_lambda_n(6)
    chi_by_lam = _load_chi_deuteron_h6()

    # Coverage check
    missing = [list(lam) for lam in parts6
               if lam not in y_by_lam or lam not in chi_by_lam]
    if missing:
        raise RuntimeError(
            f"missing y_λ or χ^λ for {missing}; refresh n=6 caches "
            f"before re-running."
        )

    # Phase-4 amplitude A(D) at q₀.
    A_D = _phase4_amplitude_D(q_0)
    target_signed = -B_D_MEV / M_E_MEV
    target_after_A = target_signed / A_D

    print("=" * 78)
    print("GAP-A-3 deuteron P_λ content-channel probe")
    print("=" * 78)
    print(f"  Phase-4 A(D) at q₀         = {float(A_D):+.6f}")
    print(f"  empirical |Δ_λ*(D)|        = 22.9594  (Phase-4 table)")
    print(f"  rel err A(D) vs |Δ_λ*(D)|  = "
          f"{float(abs(A_D - mp.mpf('22.9594')) / mp.mpf('22.9594')):.3e}  "
          f"(expect ≤ 0.07 %)")
    print(f"  −B(D)/m_e                  = {float(target_signed):+.6f}")
    print(f"  −B(D)/(m_e·A(D))           = {float(target_after_A):+.6f}  "
          f"← P_λ probe target")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("vol_hyp_D_phase4", str(VOL_HYP_D))
    w.add_parameter("A_D_at_q0", str(A_D))
    w.add_parameter("B_D_MeV", str(B_D_MEV))
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("target_signed", str(target_signed))
    w.add_parameter("target_after_A_factored", str(target_after_A))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "scope_doc",
        "docs/audits/2026-06-04-gap-a3-brane-tower-level-selection-scope.md",
    )

    channels = [
        ("C1", "sl2_schur_weyl_mult", channel_C1_sl2_schur_weyl,
         "P_λ = f^λ if rows(λ) ≤ 2 else 0  (V_{1/2}^{⊗6} mult)"),
        ("C2", "sl3_schur_weyl_mult", channel_C2_sl3_schur_weyl,
         "P_λ = f^λ if rows(λ) ≤ 3 else 0  (V_1^{⊗?} mult)"),
        ("C3", "sl2_qdim", lambda lam: channel_C3_sl2_qdim(lam, q_0),
         "P_λ = [λ_1 − λ_2 + 1]_q at q₀ if rows(λ) ≤ 2 else 0"),
        ("C4", "sl2_indicator", channel_C4_sl2_indicator,
         "P_λ = 1 if rows(λ) ≤ 2 else 0  (channel baseline)"),
        ("C5", "zero_control", channel_C5_zero_control,
         "P_λ ≡ 0  (control; should give S = 0)"),
    ]

    results = []
    for code, name, p_fn, formula in channels:
        S = mp.mpf(0)
        per_lambda = []
        for lam in parts6:
            p_lam = p_fn(lam)
            p_lam_mpf = mp.mpf(p_lam) if not isinstance(p_lam, mp.mpf) else p_lam
            term = y_by_lam[lam] * chi_by_lam[lam] * p_lam_mpf
            S += term
            per_lambda.append({
                "partition": list(lam),
                "p_lambda": str(p_lam_mpf),
                "y_chi_p": str(term),
            })
        delta = S - target_after_A
        rel_err = (delta / target_after_A
                   if target_after_A != 0 else mp.mpf("inf"))
        is_control = (code == "C5")
        verdict = _verdict(rel_err, is_control=is_control, S_abs=abs(S))
        print(f"\n  {code} ({name}):  {formula}")
        print(f"      S = {float(S):+.10f}  vs target "
              f"{float(target_after_A):+.6f}  rel_err "
              f"{float(rel_err):+.3e}  →  {verdict}")
        results.append({
            "code": code,
            "name": name,
            "formula": formula,
            "S_at_q0": str(S),
            "target": str(target_after_A),
            "delta": str(delta),
            "relative_error": str(rel_err),
            "verdict": verdict,
            "per_lambda": per_lambda,
        })

    w.add_data("channels", results)

    # Witness assertions
    A_rel_err = abs(A_D - mp.mpf("22.9594")) / mp.mpf("22.9594")
    w.add_assertion(
        "phase4_amplitude_A_D_matches_table",
        computed=float(A_rel_err),
        expected=0.0,
        tolerance=1e-3,
        source=(
            "Sanity check: re-derived A(D) from the Phase-4 formula must "
            "match the Phase-4 doc's tabulated |Δ_λ*(D)| = 22.9594 to "
            "≤ 0.1 % (the doc's quoted 0.07 % rel.err.)."
        ),
    )
    c5_S = mp.mpf([r["S_at_q0"] for r in results if r["code"] == "C5"][0])
    w.add_assertion(
        "zero_control_C5_sums_to_zero",
        computed=float(abs(c5_S)),
        expected=0.0,
        tolerance=1e-40,
        source="C5 control with P_λ ≡ 0 must give |S| = 0 exactly.",
    )

    # Synthesis
    matched = [r for r in results if r["verdict"] in
               ("EXACT-MATCH", "NEAR-MATCH (< 5 %)")]
    near_50 = [r for r in results if r["verdict"] == "NEAR-MATCH (< 50 %)"]
    if matched:
        synthesis = (
            f"At least one brane-tower content channel matches the "
            f"P_λ(D) target within 5 % with zero free parameters: "
            f"{', '.join(r['code'] for r in matched)}. The two-layer "
            f"GAP-A-3 factorisation Δ_λ(D) = A(D)·P_λ(D) is "
            f"empirically supported for the deuteron. Recommend "
            f"immediate cross-check on T, ³He, ⁴He, and Lean "
            f"formalization of the matching channel's categorical "
            f"derivation."
        )
    elif near_50:
        synthesis = (
            f"No channel matches within 5 %, but {', '.join(r['code'] for r in near_50)} "
            f"land within 50 %, indicating the two-layer factorisation "
            f"captures the right ORDER of magnitude for P_λ(D). The "
            f"residual (< 50 %) suggests the brane-tower content "
            f"channels carry the leading structure but need a "
            f"composite or weighted combination. NOT a 7th-fit-ansatz "
            f"opening: a no-fit additive combination of channels is "
            f"still parameter-free if the additive structure is "
            f"derived from the Phase-4 carrier factors."
        )
    else:
        synthesis = (
            "All four target-match channels (C1-C4) REFUTED and the "
            "C5 zero-control passes (|S| ≈ 0 as required) — none of "
            "the natural brane-"
            "tower content projections (sl_2 / sl_3 Schur-Weyl mult, "
            "sl_2 q-dim, ≤2-row indicator) reproduces the deuteron "
            "P_λ(D) target. The remaining direction is GAP-A-4 — the "
            "ρ general rule / per-atom λ(K) substrate-derivation in "
            "Path B, which bypasses the Δ_λ gate entirely by re-"
            "opening the per-atom λ(K) question."
        )
    w.add_data("synthesis_verdict", synthesis)
    print(f"\n  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

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
