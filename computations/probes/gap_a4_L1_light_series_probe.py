#!/usr/bin/env python3
"""GAP-A-4 L1 probe — substrate-derived λ(K) candidates for the light series.

Implements §4 candidate **L1** of [`docs/audits/2026-06-04-gap-a4-path-b-lambda-K-scope.md`](../../docs/audits/2026-06-04-gap-a4-path-b-lambda-K-scope.md).
Tests whether the per-atom λ(K) of Path B (`m(K) = m_e·Vol(K)/ℏ_q²·λ(K) + S(K)`,
ignoring S(K)) is reproducible from simple substrate quantities for the light
series {p, n, D, T, ³He, ⁴He}.

Empirical anchor (from §3 of the scope doc):

  λ_emp(K) = m(K) · ℏ_q² / (m_e · Vol(K))

with `Vol(K)` per-knot:
  - p, n:    Vol(𝓑₃) = 8·G  (Borromean)
  - D, T:    Vol_Phase-4 = 12.776  (SnapPy JSJ, Z=1 atoms)
  - ³He, ⁴He: Vol_Phase-4 = 12.554  (SnapPy JSJ, Z=2 atoms)

Three candidate substrate-derived forms (no fit, each closed-form):

  L1a — uniform linking-weight: λ(K) = linking_weight_family_a(q₀)
        = (3q²+4+3q⁻²)/4 ≈ 2.533. The production constant. Predicts λ
        constant across atoms. Expected to land near 2.46 for the proton
        (the "CODATA-implied near-match" framing).

  L1b — Phase-4 ratio in Path B coordinates:
        λ_L1b(K) = A_Phase-4(K) · ℏ_q² · m_e / m(K) · (Vol(𝓑₃)/Vol(K))
        (re-expression of Phase-4 amplitude; uses only substrate factors
        and the per-atom Vol).

  L1c — Phase-4 carriers alone, normalised by linking-weight at Z=1, N=0:
        λ_L1c(K) = linking_weight_family_a(q₀) · [3]_q^{2(Z-1)} ·
                   (q^{1/2}+q^{-1/2})^{4N}.
        Hypothesis: the per-(Z, N) carriers of Phase-4 transfer directly
        to the Path B per-atom multiplier with the same exponents.

Verdict per atom per candidate: NEAR-MATCH (<5 %) / NEAR-MATCH (<25 %) /
REFUTED otherwise.

EXPLORATORY — no production code, content blocks, or production witnesses
changed. Emits `gap-a4-L1-light-series-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
from codata_constants import M_D_MEV_VALIDATION, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, M_T_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from closed_form_tau_M import (  # noqa: E402
    compute_tau_M_nucleon_H3,
    closed_form_tau_M,
)

from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# Canonical 50-dps q₀
Q_0_50DPS = Q_50_DIGIT_STR

# CODATA-2022 / AME-2020 nucleon + light-atom masses (MeV), routed
# through the canonical registry (I9 — no hardcoded literals). See
# substrate/codata_constants.py + audits/hardcoded_literal_audit.py.
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as m_n_derived_3input,
    M_D_MEV_VALIDATION as M_D_MEV,
    M_T_MEV_VALIDATION as M_T_MEV,
    M_HE3_MEV_VALIDATION as M_HE3_MEV,
    M_HE4_MEV_VALIDATION as M_HE4_MEV,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# Per-knot hyperbolic volumes.  p/n: Borromean 8·G; D/T: Phase-4 JSJ
# Z=1 value 12.776; ³He/⁴He: Phase-4 JSJ Z=2 value 12.554.
VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")  # 8·G
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sum(q ** (2 * k - (n - 1)) for k in range(n))


def linking_weight_family_a_sym(q: sp.Expr) -> sp.Expr:
    return (3 * q ** 2 + 4 + 3 * q ** (-2)) / 4


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    """ℏ_q² where ℏ_q = (q − 1)/q = 1 − q⁻¹."""
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def lambda_empirical(m_K: mp.mpf, vol_K: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """λ_emp(K) = m(K)·ℏ_q²/(m_e·Vol(K))."""
    return m_K * hbar_q_sq(q_0) / (M_E_MEV * vol_K)


def A_phase4(Z: int, N: int, vol_hyp: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """Phase-4 |Δ_λ*(K)| amplitude:
    A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}.

    For Z=0 (neutron) the color carrier extends naturally to `[3]_q^{-2}`
    (q-numbers are invertible at real q₀ ≈ 1.11); not zero (Copilot
    review on PR #1874 caught the over-cautious early-out).
    """
    q_sym = sp.Symbol("q", positive=True)
    eight_q = q_number_sym(8, q_sym)
    three_q = q_number_sym(3, q_sym)
    spin_carrier = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** (4 * N)
    color_carrier = three_q ** (2 * (Z - 1))
    expr = sp.Float(str(vol_hyp), 50) / eight_q * color_carrier * spin_carrier
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def lambda_L1a(tr_M_K: mp.mpf) -> mp.mpf:
    """L1a — canonical per-knot Hecke density tr_M(K)."""
    return tr_M_K


def lambda_L1b(Z: int, N: int, vol_hyp: mp.mpf, m_K: mp.mpf,
               q_0: mp.mpf) -> mp.mpf:
    """L1b — Phase-4 amplitude transposed to Path B coordinates.

    Original scope-doc formula (`A · ℏ_q² · m_e · Vol(𝓑₃) / (m_K · Vol_hyp)`)
    was dimensionally wrong (Copilot review on PR #1874): A is
    dimensionless in m_e units (it's |Δ_λ*|), and the original
    multiplication by `m_e/m_K` collapsed the prediction to ≈ 0.

    Corrected form: ask "what fraction of |Δ_λ*|/A is the empirical λ?",
    i.e. `λ_L1b(K) = A_Phase-4(K) · m_K / (m_e · A_phase4_normaliser)`
    so that L1b reproduces λ_emp when A_phase4 / |Δ_λ*| = 1 by Phase-4's
    own claim.  Concretely, use the normaliser
    `A_phase4_normaliser = m_K · Vol(𝓑₃) / (m_e · Vol_hyp · ℏ_q²)`
    so the ratio reduces to:

        λ_L1b(K)  =  A_Phase-4(K) · Vol_hyp(K) / Vol(𝓑₃) · ℏ_q²

    which gives O(1)-scale predictions comparable to λ_emp(K).
    """
    A = A_phase4(Z, N, vol_hyp, q_0)
    return A * vol_hyp / VOL_BORROMEAN_8G * hbar_q_sq(q_0)


def lambda_L1c(Z: int, N: int, q_0: mp.mpf, tr_M_K: mp.mpf) -> mp.mpf:
    """L1c — Phase-4 carriers alone scaled by tr_M(K):
    λ(K) = tr_M(K) · [3]_q^{2(Z-1)} ·
           (q^{1/2}+q^{-1/2})^{4N}.
    At Z=1, N=0 (proton) this reduces to tr_M(p) alone.
    """
    q_sym = sp.Symbol("q", positive=True)
    three_q = q_number_sym(3, q_sym)
    spin_carrier = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** (4 * N)
    # `[3]_q^{2(Z-1)}` extends naturally to Z=0 (= [3]_q^{-2}); no
    # zero-clamp (Copilot review on PR #1874).
    color_carrier = three_q ** (2 * (Z - 1))
    expr = color_carrier * spin_carrier
    return tr_M_K * mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def _verdict(rel_err: mp.mpf) -> str:
    a = abs(rel_err)
    if a < mp.mpf("5e-2"):
        return "NEAR-MATCH (< 5 %)"
    if a < mp.mpf("0.25"):
        return "NEAR-MATCH (< 25 %)"
    return "REFUTED"


# Light-series registry: (label, Z, N, m_K, vol_hyp_K).
LIGHT_SERIES = [
    ("p",   1, 0, M_P_MEV,    VOL_BORROMEAN_8G),
    ("n",   0, 1, m_n_derived_3input,    VOL_BORROMEAN_8G),
    ("D",   1, 1, M_D_MEV,    VOL_PHASE4_Z1),
    ("T",   1, 2, M_T_MEV,    VOL_PHASE4_Z1),
    ("3He", 2, 1, M_HE3_MEV,  VOL_PHASE4_Z2),
    ("4He", 2, 2, M_HE4_MEV,  VOL_PHASE4_Z2),
]


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-L1-light-series-probe", engine="sympy+mpmath"
    )
    w.set_audit_only("docs/audits/2026-06-04-gap-a4-path-b-lambda-K-scope.md")
    w.set_description(
        "GAP-A-4 §4 candidate L1 probe: test whether the per-atom "
        "Path B λ(K) is substrate-derivable for the light series "
        "{p, n, D, T, ³He, ⁴He}. Three closed-form candidates (L1a "
        "uniform linking-weight, L1b Phase-4 re-expression, L1c "
        "Phase-4 carriers). Per-knot Vol from §3: p/n = 8·G "
        "(Borromean); D/T = 12.776 (Phase-4 JSJ Z=1); ³He/⁴He = "
        "12.554 (Z=2). EXPLORATORY — no production code, content, "
        "or production witnesses changed."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    tau_p_H3 = compute_tau_M_nucleon_H3("p", q_0)
    tau_n_H3 = compute_tau_M_nucleon_H3("n", q_0)

    print("=" * 78)
    print("GAP-A-4 L1 probe — substrate-derived λ(K) for the light series")
    print("=" * 78)
    print(f"  q₀                                = {Q_0_50DPS}")
    print(f"  m_e (MeV)                         = {float(M_E_MEV):.9f}")
    print(f"  ℏ_q²                              = {float(hbar_q_sq(q_0)):.10f}")
    print(f"  Vol(𝓑₃) = 8·G                     = {float(VOL_BORROMEAN_8G):.10f}")
    print("-" * 78)
    print(f"  {'atom':<4} {'Z':>2} {'N':>2} {'Vol(K)':>10} "
          f"{'λ_emp':>10} "
          f"{'L1a':>10} (rel) "
          f"{'L1b':>10} (rel) "
          f"{'L1c':>10} (rel)")
    print("-" * 78)

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "scope_doc",
        "docs/audits/2026-06-04-gap-a4-path-b-lambda-K-scope.md",
    )

    rows = []
    for label, Z, N, m_K, vol_K in LIGHT_SERIES:
        tr_M_K = closed_form_tau_M(Z, N, q_0, tau_p_H3, tau_n_H3)
        lam_emp = lambda_empirical(m_K, vol_K, q_0)
        L1a_pred = lambda_L1a(tr_M_K)
        L1b_pred = lambda_L1b(Z, N, vol_K, m_K, q_0)
        L1c_pred = lambda_L1c(Z, N, q_0, tr_M_K)
        rel_a = (L1a_pred - lam_emp) / lam_emp
        rel_b = (L1b_pred - lam_emp) / lam_emp
        rel_c = (L1c_pred - lam_emp) / lam_emp
        ver_a = _verdict(rel_a)
        ver_b = _verdict(rel_b)
        ver_c = _verdict(rel_c)
        print(f"  {label:<4} {Z:>2} {N:>2} {float(vol_K):>10.4f} "
              f"{float(lam_emp):>10.4f} "
              f"{float(L1a_pred):>10.4f} ({float(rel_a):>+7.2%}) "
              f"{float(L1b_pred):>10.4f} ({float(rel_b):>+7.2%}) "
              f"{float(L1c_pred):>10.4f} ({float(rel_c):>+7.2%})")
        rows.append({
            "label": label, "Z": Z, "N": N,
            "vol_K": str(vol_K),
            "m_K_MeV": str(m_K),
            "lambda_empirical": str(lam_emp),
            "L1a_tr_M": {
                "prediction": str(L1a_pred),
                "relative_error": str(rel_a),
                "verdict": ver_a,
            },
            "L1b_phase4_reexpression": {
                "prediction": str(L1b_pred),
                "relative_error": str(rel_b),
                "verdict": ver_b,
            },
            "L1c_phase4_carriers": {
                "prediction": str(L1c_pred),
                "relative_error": str(rel_c),
                "verdict": ver_c,
            },
        })

    w.add_data("rows", rows)

    # Per-candidate worst-case. Keep mp.mpf precision in the witness;
    # only downcast to float for the printed console summary
    # (Copilot review on PR #1874).
    def worst_rel(key: str) -> tuple[str, mp.mpf]:
        worst_label = ""
        worst = mp.mpf(0)
        for r in rows:
            rel = mp.mpf(r[key]["relative_error"])
            if abs(rel) > abs(worst):
                worst = rel
                worst_label = r["label"]
        return worst_label, worst

    L1a_worst = worst_rel("L1a_tr_M")
    L1b_worst = worst_rel("L1b_phase4_reexpression")
    L1c_worst = worst_rel("L1c_phase4_carriers")
    print("-" * 78)
    print(f"  worst-rel L1a (tr_M):       {float(L1a_worst[1]):+.2%}  at {L1a_worst[0]}")
    print(f"  worst-rel L1b (Phase-4 re-expr):  {float(L1b_worst[1]):+.2%}  at {L1b_worst[0]}")
    print(f"  worst-rel L1c (Phase-4 carriers): {float(L1c_worst[1]):+.2%}  at {L1c_worst[0]}")

    w.add_data("worst_relative_error_L1a", {"atom": L1a_worst[0], "rel_err": str(L1a_worst[1])})
    w.add_data("worst_relative_error_L1b", {"atom": L1b_worst[0], "rel_err": str(L1b_worst[1])})
    w.add_data("worst_relative_error_L1c", {"atom": L1c_worst[0], "rel_err": str(L1c_worst[1])})

    # Synthesis
    def best_candidate():
        candidates = [
            ("L1a", abs(L1a_worst[1])),
            ("L1b", abs(L1b_worst[1])),
            ("L1c", abs(L1c_worst[1])),
        ]
        candidates.sort(key=lambda t: t[1])
        return candidates[0]

    best, worst = best_candidate()
    if worst < 0.05:
        synthesis = (
            f"Best candidate {best} lands within 5 % across all six "
            f"light atoms — GAP-A-4 (Path B λ(K) substrate-derivation) "
            f"closes for the light series at the same precision as "
            f"Phase-4. The framework can drop the Δ_λ decomposition "
            f"layer entirely without losing accuracy."
        )
    elif worst < 0.25:
        synthesis = (
            f"Best candidate {best} lands within 25 % but exceeds 5 %. "
            f"The substrate carriers capture the leading per-atom "
            f"structure but a higher-order correction is needed for "
            f"closure. Investigate the next-order term in the Phase-4 "
            f"expansion or a small sub-leading S(K) in Path B."
        )
    else:
        synthesis = (
            f"All three candidates REFUTED (worst-rel ≥ 25 %). The "
            f"per-atom Path B λ(K) is NOT a simple substrate combination "
            f"of linking_weight_family_a and the Phase-4 carriers. "
            f"GAP-A-4 needs a richer derivation route (e.g. a brane-"
            f"tower formula that's separately tuned for the Path B "
            f"mass-equation rather than the Δ_λ binding-energy "
            f"equation)."
        )
    w.add_data("synthesis_verdict", synthesis)
    print("-" * 78)
    print(f"  SYNTHESIS: best={best} with worst-atom rel_err={float(worst):.2%}")
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
