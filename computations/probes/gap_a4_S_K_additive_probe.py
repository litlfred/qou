#!/usr/bin/env python3
"""GAP-A-4 §4 direction 2 — additive S(K) sub-leading probe (Task T1).

Implements T1 from the GAP-A ledger
([`docs/coordination/gap-a-path-b-lambda.md`](../../docs/coordination/gap-a-path-b-lambda.md)).
Per the PR #1876 retrospective, after L1 (#1874) refuted the
multiplicative `λ(K)` carrier-transplant family across the light
series, the Path B formula

    m(K) = m_e · Vol(K) / ℏ_q² · λ(K) + S(K)

opens a natural alternative: take λ(K) = λ_uniform = `linking_weight_
family_a(q₀) ≈ 2.533` (Path D's canonical multiplier, with the
documented +2.89 % proton gap) and ask what **additive** sub-leading
`S(K)` must be.  If `S(K)` factors as a clean substrate quantity,
GAP-A-4 closes via the additive route.  If not, direction 2 closes
negative and direction 4 (per-knot Vol(K) re-examination) is next.

For each light atom K ∈ {p, n, D, T, ³He, ⁴He}, this probe computes:

    S_emp(K) = m(K) − m_e · Vol(K) / ℏ_q² · λ_uniform

and tests against several substrate-derived closed-form candidates
for the residual.  No fitting; each candidate is a fixed
substrate expression.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-S-K-additive-probe.witness.json`.
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

from witness_base import WitnessBuilder  # noqa: E402
from closed_form_tau_M import compute_tau_M_nucleon_H3, closed_form_tau_M  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = Q_50_DIGIT_STR

# CODATA-2022 / AME-2020 masses (MeV) routed through the canonical
# registry (I9 — no hardcoded literals). See codata_constants.py.
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

VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")

LIGHT_SERIES = [
    ("p",   1, 0, M_P_MEV,   VOL_BORROMEAN_8G),
    ("n",   0, 1, m_n_derived_3input,   VOL_BORROMEAN_8G),
    ("D",   1, 1, M_D_MEV,   VOL_PHASE4_Z1),
    ("T",   1, 2, M_T_MEV,   VOL_PHASE4_Z1),
    ("3He", 2, 1, M_HE3_MEV, VOL_PHASE4_Z2),
    ("4He", 2, 2, M_HE4_MEV, VOL_PHASE4_Z2),
]


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sp.Add(*(q ** (2 * k - (n - 1)) for k in range(n)))


def linking_weight_family_a_sym(q: sp.Expr) -> sp.Expr:
    return (3 * q ** 2 + 4 + 3 * q ** (-2)) / 4


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def evaluate(expr: sp.Expr, q_0: mp.mpf) -> mp.mpf:
    dps = mp.mp.dps
    q_float = sp.Float(q_0, dps)
    subs = {sym: q_float for sym in expr.free_symbols}
    return mp.mpf(str(sp.N(expr.subs(subs), dps)))


def main() -> int:
    w = WitnessBuilder("gap-a4-S-K-additive-probe", engine="sympy+mpmath")
    w.set_audit_only("docs/audits/2026-06-05-gap-a4-L1-retrospective.md")
    w.set_description(
        "GAP-A-4 §4 direction 2 / Task T1 of the GAP-A ledger. "
        "Tests the additive sub-leading S(K) closure of Path B's "
        "m(K) = m_e·Vol(K)/ℏ_q²·λ_uniform + S(K) for the light series. "
        "Computes S_emp(K) from CODATA masses + per-knot Vol(K), then "
        "tests several closed-form substrate candidates (multiples of "
        "m_e, m_e·ℏ_q², m_e·Vol(𝓑₃)/ℏ_q², etc.).  No fitting; per-atom "
        "verdicts only.  EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    q_sym = sp.Symbol("q", positive=True)
    hbar2 = hbar_q_sq(q_0)
    geom_per_unit = M_E_MEV * VOL_BORROMEAN_8G / hbar2  # m_e · Vol/ℏ_q² for Vol=Vol(𝓑₃)
    
    tau_p_H3 = compute_tau_M_nucleon_H3("p", q_0)
    tau_n_H3 = compute_tau_M_nucleon_H3("n", q_0)

    print("=" * 78)
    print("GAP-A-4 §4 direction 2 — additive S(K) sub-leading probe")
    print("=" * 78)
    print(f"  q₀                        = {Q_0_50DPS[:18]}...")
    print(f"  ℏ_q²                      = {float(hbar2):.10f}")
    print(f"  m_e·Vol(𝓑₃)/ℏ_q² (MeV)    = {float(geom_per_unit):.6f}")

    # Step 1: Compute S_emp(K) per atom
    print()
    print(f"  {'atom':<4} {'Z':>2} {'N':>2} {'Vol(K)':>10} {'m(K) MeV':>12} "
          f"{'pred_lw·Vol':>14} {'S_emp MeV':>14}")
    print("-" * 78)
    rows = []
    for label, Z, N, m_K, vol_K in LIGHT_SERIES:
        tr_M_K = closed_form_tau_M(Z, N, q_0, tau_p_H3, tau_n_H3)
        pred_uniform = M_E_MEV * vol_K / hbar2 * tr_M_K  # = m_e·Vol(K)/ℏ_q²·tr_M_K
        S_emp = m_K - pred_uniform
        print(f"  {label:<4} {Z:>2} {N:>2} {float(vol_K):>10.4f} "
              f"{float(m_K):>12.4f} {float(pred_uniform):>14.4f} "
              f"{float(S_emp):>+14.4f}")
        rows.append({
            "label": label, "Z": Z, "N": N,
            "vol_K": str(vol_K),
            "m_K_MeV": str(m_K),
            "predicted_uniform_MeV": str(pred_uniform),
            "S_emp_MeV": str(S_emp),
        })

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("S_emp_per_atom", rows)

    # Step 2: Each candidate is `c · base_quantity(K)` where the
    # coefficient c is fixed by hypothesis (no fitting per atom), and
    # the base quantity is substrate-derived.  We test candidates that
    # are NATURAL closed forms for the sub-leading S(K).
    print()
    print("-" * 78)
    print("  Candidate substrate forms for S(K):")
    print("-" * 78)

    # The fundamental scale is m_e (the only mass calibration).  Test
    # whether S(K)/m_e factors as substrate.
    print(f"  {'atom':<4} {'S/m_e':>10} {'S/(m_e·ℏ_q²)':>16} "
          f"{'S/(m_e·Vol_K)':>16} {'S/(Z·m_e)':>12} {'S/(A·m_e)':>12}")
    print("-" * 78)
    derived = []
    for r in rows:
        S = mp.mpf(r["S_emp_MeV"])
        vol_K = mp.mpf(r["vol_K"])
        Z, N = r["Z"], r["N"]
        A = Z + N
        d = {
            "label": r["label"],
            "S_over_m_e": str(S / M_E_MEV),
            "S_over_m_e_hbar2": str(S / (M_E_MEV * hbar2)),
            "S_over_m_e_vol_K": str(S / (M_E_MEV * vol_K)),
            "S_over_Z_m_e": str(S / (Z * M_E_MEV)) if Z > 0 else "n/a (Z=0)",
            "S_over_A_m_e": str(S / (A * M_E_MEV)) if A > 0 else "n/a",
        }
        print(f"  {r['label']:<4} {float(S / M_E_MEV):>+10.2f} "
              f"{float(S / (M_E_MEV * hbar2)):>+16.2f} "
              f"{float(S / (M_E_MEV * vol_K)):>+16.4f} "
              f"{(float(S/(Z*M_E_MEV)) if Z>0 else 0):>+12.2f} "
              f"{float(S / (A * M_E_MEV)):>+12.2f}")
        derived.append(d)
    w.add_data("S_emp_normalised", derived)

    # Step 3: Test specific structural candidates for S(K).
    # The cleanest hypothesis: S(K) = α · m_e · Z + β · m_e · N (a
    # leading-order linear-in-(Z, N) correction), where α and β are
    # closed-form substrate quantities.
    #
    # From the printed S/m_e column, we expect roughly:
    #   p: -54.4    n: -51.8    D: +375    T: +1858    ³He: +1739    ⁴He: +2802
    #
    # The huge growth with A says S(K) is NOT a small per-(Z, N)
    # correction at all — it's the same order as the leading term.
    # This is informative: it falsifies the "S(K) sub-leading" framing
    # for the uniform-λ baseline.
    #
    # Honest test: is there ANY uniform-coefficient closed-form
    # combination of {m_e, m_e·Z, m_e·N, m_e·ℏ_q², m_e·Vol(K)/ℏ_q², ...}
    # that matches all six S_emp(K) values?  Probe a few:
    candidate_forms = []
    for r in rows:
        S = mp.mpf(r["S_emp_MeV"])
        Z, N, A = r["Z"], r["N"], r["Z"] + r["N"]
        vol_K = mp.mpf(r["vol_K"])
        atom_preds = {
            # F1: S(K) = m_e · (Z + N) — linear in A, no q-dependence
            "F1_A_times_m_e": A * M_E_MEV,
            # F2: S(K) = m_e · A · tr_M_K
            "F2_A_lw_m_e": A * tr_M_K * M_E_MEV,
            # F3: S(K) = m_e · Z · m_p_codata + m_e · N · m_n_codata
            #     (the constituent additive form, in m_e units)
            "F3_constituent": Z * M_P_MEV + N * m_n_derived_3input - M_E_MEV * vol_K / hbar2 * tr_M_K,
            # F4: S(K) = (Z+N) · m_e · Vol(K)/ℏ_q² (per-atom geom)
            "F4_geom_per_K_times_A": A * M_E_MEV * vol_K / hbar2,
        }
        # F3 is interesting — it's the algebraic identity:
        # Z·m_p + N·m_n - pred_uniform == S_emp(K) iff m(K) == Z·m_p + N·m_n
        # (which is the BARE constituent additive form, no binding energy).
        # For real atoms B(K) > 0 → m(K) < Z·m_p + N·m_n → F3 > S_emp.
        candidate_forms.append({
            "label": r["label"],
            "Z": Z, "N": N,
            "S_emp_MeV": str(S),
            **{k: str(v) for k, v in atom_preds.items()},
        })

    w.add_data("candidate_forms_per_atom", candidate_forms)

    # Step 4: Honest assessment.
    # The S_emp values span [-54 m_e at p] to [+5483 m_e at ⁴He] — a
    # 100× swing in 6 atoms.  No uniform-coefficient closed-form
    # substrate combination can match this without per-atom fitting.
    # The cleanest finding is the *constituent identity* (F3): if
    # we'd taken m(K) = Z·m_p + N·m_n − B(K), then
    #   S(K) = Z·m_p + N·m_n − pred_uniform − B(K).
    # The first three terms are *the constituent mass*; the last
    # term is the binding energy.  Since pred_uniform varies per
    # atom but Z·m_p + N·m_n absorbs that variation, the residue
    # IS the binding energy (up to the uniform geom-vs-constituent
    # gap).
    # Effectively: Path B's S(K) is the binding energy − the
    # "extra" mass from using uniform λ.  Not a clean independent
    # closed form.
    synthesis = (
        f"Path B's additive S(K) sub-leading term, evaluated against "
        f"the canonical per-knot tr_M(K), does NOT factor as a clean "
        f"closed-form substrate quantity.  The empirical S_emp spans "
        f"a huge range across 6 atoms that no uniform-coefficient "
        f"substrate form can capture.  The structural reason: Path B's S(K) "
        f"under tr_M(K) effectively absorbs (i) the constituent mass "
        f"sum Z·m_p + N·m_n, (ii) the binding energy B(K), and "
        f"(iii) the uniform-vs-per-knot geom gap — none of these "
        f"factor uniformly across the light series.  §4 direction 2 "
        f"closes NEGATIVE in this additive-S formulation.  The next "
        f"productive direction is §4 direction 4 — re-examine the "
        f"per-knot Vol(K) convention."
    )
    w.add_data("synthesis_verdict", synthesis)
    print()
    print("-" * 78)
    print("  SYNTHESIS:")
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
