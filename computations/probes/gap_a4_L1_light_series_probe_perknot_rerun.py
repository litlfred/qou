#!/usr/bin/env python3
"""GAP-A-4 L1 probe — PER-KNOT-DENSITY RE-RUN (bean x5az, artifact audit).

Re-runs the PR #1874 L1 light-series probe with the canonical PER-KNOT
Hecke-trace density substituted for the fitted global scalar λ_A, per
the re-run protocol of
[`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](../../docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md).
The audit classifies the original refutation as λ_A-family-bound: its
negative verdicts ruled out only λ_A-family forms; the canonical
per-knot density tr_M(K) was never tried.

Density-swap mapping (λ_A-family form → like-for-like per-knot form):

  | candidate | λ_A baseline (PR #1874)                     | per-knot re-run                              |
  |-----------|----------------------------------------------|----------------------------------------------|
  | L1a       | λ(K) = λ_A = (3q²+4+3q⁻²)/4 ≈ 2.533 (const, | λ(K) = tr_M(K) — canonical chi-cache Markov   |
  |           | p = n degenerate)                            | trace, p ≠ n distinct                         |
  | L1b       | A_Phase-4(K)·Vol(K)/Vol(𝓑₃)·ℏ_q²             | UNCHANGED (density-independent; reproduced    |
  |           | (no λ_A — density-independent)               | as baseline cross-check only)                 |
  | L1c       | λ_A · [3]_q^{2(Z−1)} · (q^½+q^{−½})^{4N}     | tr_M(K) · [3]_q^{2(Z−1)} · (q^½+q^{−½})^{4N}  |

Same isotopes {p, n, D, T, ³He, ⁴He}, same CODATA/AME validation
masses (codata_constants registry), same per-knot volumes (p/n: 8·G
Borromean; D/T: Phase-4 JSJ 12.776; ³He/⁴He: 12.554), same empirical
target λ_emp(K) = m(K)·ℏ_q²/(m_e·Vol(K)), same verdict thresholds
(<5 % / <25 % / REFUTED), same canonical muon-q₀
(q-pinning-50-digit.witness.json), same precision defaults
(_precision.set_compute_dps).

Per-knot traces are loaded from the canonical numerical chi-cache
witnesses (`chi-{atom}-h{3A}-at-q0-50dps.witness.json`) via
`canonical_tr_m_via_chi_cache.canonical_tr_m` — proton ≈ 1.0653,
neutron ≈ 0.9232 (p ≠ n distinct, which the degenerate λ_A erases).
This sandbox lacks the Rust kernel (pyhecke_native) that the on-disk
original needs for `compute_tau_M_nucleon_H3`, so the λ_A baseline is
reproduced closed-form in-script (λ_A needs no Hecke trace) and
cross-checked against the documented PR #1874 numbers (+2.96 % proton
gap; −55.6 % worst at ⁴He).

Three-calibration discipline: NO new fitted constants, NO new ansatz
families — only the original L1 functional forms with the density base
swapped. If the per-knot base also fails, that is a scope-limited
negative (a): "these multiplicative forms, alone, on either density
base, do not reproduce λ_emp" — not a structural exclusion (b).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits
`gap-a4-L1-light-series-probe-perknot-rerun.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from canonical_tr_m_via_chi_cache import canonical_tr_m  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as M_N_MEV,
    M_D_MEV_VALIDATION as M_D_MEV,
    M_T_MEV_VALIDATION as M_T_MEV,
    M_HE3_MEV_VALIDATION as M_HE3_MEV,
    M_HE4_MEV_VALIDATION as M_HE4_MEV,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# Canonical 50-dps muon-anchored q₀ (q-pinning-50-digit.witness.json),
# identical to the original probe.
Q_0_50DPS = Q_50_DIGIT_STR

# Per-knot hyperbolic volumes — identical to the original probe.
VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")

# Light-series registry: (label, chi-cache atom name, Z, N, m_K, vol_K).
LIGHT_SERIES = [
    ("p",   "proton",   1, 0, M_P_MEV,   VOL_BORROMEAN_8G),
    ("n",   "neutron",  0, 1, M_N_MEV,   VOL_BORROMEAN_8G),
    ("D",   "deuteron", 1, 1, M_D_MEV,   VOL_PHASE4_Z1),
    ("T",   "tritium",  1, 2, M_T_MEV,   VOL_PHASE4_Z1),
    ("3He", "helium-3", 2, 1, M_HE3_MEV, VOL_PHASE4_Z2),
    ("4He", "helium-4", 2, 2, M_HE4_MEV, VOL_PHASE4_Z2),
]


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sp.Add(*(q ** (2 * k - (n - 1)) for k in range(n)))


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    """ℏ_q² where ℏ_q = 1 − q⁻¹."""
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def lambda_empirical(m_K: mp.mpf, vol_K: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """λ_emp(K) = m(K)·ℏ_q²/(m_e·Vol(K)) — identical to the original."""
    return m_K * hbar_q_sq(q_0) / (M_E_MEV * vol_K)


def A_phase4(Z: int, N: int, vol_hyp: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """Phase-4 amplitude — identical to the original (incl. the Z=0
    `[3]_q^{-2}` extension from the PR #1874 Copilot review)."""
    q_sym = sp.Symbol("q", positive=True)
    eight_q = q_number_sym(8, q_sym)
    three_q = q_number_sym(3, q_sym)
    spin_carrier = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** (4 * N)
    color_carrier = three_q ** (2 * (Z - 1))
    expr = sp.Float(str(vol_hyp), 50) / eight_q * color_carrier * spin_carrier
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def carriers(Z: int, N: int, q_0: mp.mpf) -> mp.mpf:
    """Phase-4 per-(Z, N) carriers [3]_q^{2(Z−1)}·(q^½+q^{−½})^{4N}."""
    q_sym = sp.Symbol("q", positive=True)
    three_q = q_number_sym(3, q_sym)
    spin_carrier = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** (4 * N)
    color_carrier = three_q ** (2 * (Z - 1))
    expr = color_carrier * spin_carrier
    return mp.mpf(str(sp.N(expr.subs(q_sym, sp.Float(str(q_0), 50)), 50)))


def _verdict(rel_err: mp.mpf) -> str:
    a = abs(rel_err)
    if a < mp.mpf("5e-2"):
        return "NEAR-MATCH (< 5 %)"
    if a < mp.mpf("0.25"):
        return "NEAR-MATCH (< 25 %)"
    return "REFUTED"


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-L1-light-series-probe-perknot-rerun", engine="sympy+mpmath"
    )
    w.set_audit_only(
        "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    )
    w.set_description(
        "Bean x5az per-knot-density re-run of the PR #1874 GAP-A-4 L1 "
        "light-series probe. Substitutes the canonical per-knot Markov "
        "trace tr_M(K) (chi-cache, p≠n distinct) for the fitted global "
        "λ_A ≈ 2.533 in the L1a / L1c ansatz forms; L1b is "
        "density-independent and reproduced unchanged as a baseline "
        "cross-check. Same isotopes, targets, thresholds, q₀ and "
        "precision as the original. NO new ansatz families. "
        "EXPLORATORY — nothing wired to production."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    lam_A = linking_weight_family_a(q_0)  # fitted global scalar ≈ 2.533
    hbar2 = hbar_q_sq(q_0)

    print("=" * 96)
    print("GAP-A-4 L1 probe — per-knot density re-run (bean x5az)")
    print("=" * 96)
    print(f"  q0 (muon-anchored)  = {Q_0_50DPS}")
    print(f"  hbar_q^2            = {mp.nstr(hbar2, 12)}")
    print(f"  lambda_A (fitted)   = {mp.nstr(lam_A, 12)}   [p = n degenerate]")

    # Per-knot traces from the canonical chi-cache.
    tr_M: dict[str, mp.mpf] = {}
    for label, atom, Z, N, _m, _v in LIGHT_SERIES:
        r = canonical_tr_m(atom, Z, N)
        if r.get("partial_cache"):
            raise RuntimeError(f"partial chi cache for {atom} — abort")
        tr_M[label] = mp.mpf(str(r["abs_tr_M_q0"]))
        print(f"  tr_M({label:<3}) [chi-cache {atom}, H_{3*(Z+N)}] = "
              f"{mp.nstr(tr_M[label], 12)}")
    print(f"  p/n distinction: tr_M(n)/tr_M(p) = "
          f"{mp.nstr(tr_M['n'] / tr_M['p'], 10)}  (lambda_A gives 1 exactly)")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("lambda_A_at_q0", str(lam_A))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("rerun_of", "computations/probes/gap_a4_L1_light_series_probe.py")
    w.add_data("density_swap", {
        "baseline": "global lambda_A = linking_weight_family_a(q0) ~ 2.533 (fit, p=n degenerate)",
        "perknot": "tr_M(K) from canonical chi-cache (canonical_tr_m_via_chi_cache), p!=n distinct",
        "tr_M_per_atom": {k: str(v) for k, v in tr_M.items()},
    })

    hdr = (f"  {'atom':<4} {'lam_emp':>9} | "
           f"{'L1a_lamA':>9} {'rel':>8} | {'L1a_trM':>9} {'rel':>8} | "
           f"{'L1b':>9} {'rel':>8} | "
           f"{'L1c_lamA':>9} {'rel':>8} | {'L1c_trM':>9} {'rel':>8}")
    print("-" * 96)
    print(hdr)
    print("-" * 96)

    rows = []
    worst: dict[str, tuple[str, mp.mpf]] = {}

    def track(key: str, label: str, rel: mp.mpf) -> None:
        if key not in worst or abs(rel) > abs(worst[key][1]):
            worst[key] = (label, rel)

    for label, atom, Z, N, m_K, vol_K in LIGHT_SERIES:
        lam_emp = lambda_empirical(m_K, vol_K, q_0)
        car = carriers(Z, N, q_0)

        # --- λ_A baseline (PR #1874 forms, reproduced closed-form) ---
        L1a_base = lam_A
        L1c_base = lam_A * car
        # --- density-independent L1b (baseline cross-check only) ---
        A = A_phase4(Z, N, vol_K, q_0)
        L1b = A * vol_K / VOL_BORROMEAN_8G * hbar2
        # --- per-knot variant (same functional forms, base swapped) ---
        L1a_pk = tr_M[label]
        L1c_pk = tr_M[label] * car

        rels = {
            "L1a_lambdaA": (L1a_base - lam_emp) / lam_emp,
            "L1a_perknot": (L1a_pk - lam_emp) / lam_emp,
            "L1b_phase4": (L1b - lam_emp) / lam_emp,
            "L1c_lambdaA": (L1c_base - lam_emp) / lam_emp,
            "L1c_perknot": (L1c_pk - lam_emp) / lam_emp,
        }
        for k, r in rels.items():
            track(k, label, r)

        print(f"  {label:<4} {float(lam_emp):>9.4f} | "
              f"{float(L1a_base):>9.4f} {float(rels['L1a_lambdaA']):>+8.2%} | "
              f"{float(L1a_pk):>9.4f} {float(rels['L1a_perknot']):>+8.2%} | "
              f"{float(L1b):>9.4f} {float(rels['L1b_phase4']):>+8.2%} | "
              f"{float(L1c_base):>9.4f} {float(rels['L1c_lambdaA']):>+8.2%} | "
              f"{float(L1c_pk):>9.4f} {float(rels['L1c_perknot']):>+8.2%}")

        rows.append({
            "label": label, "Z": Z, "N": N,
            "vol_K": str(vol_K), "m_K_MeV": str(m_K),
            "lambda_empirical": str(lam_emp),
            "tr_M_K": str(tr_M[label]),
            "candidates": {
                k: {
                    "prediction": str(v),
                    "relative_error": str(rels[k]),
                    "verdict": _verdict(rels[k]),
                }
                for k, v in {
                    "L1a_lambdaA": L1a_base,
                    "L1a_perknot": L1a_pk,
                    "L1b_phase4": L1b,
                    "L1c_lambdaA": L1c_base,
                    "L1c_perknot": L1c_pk,
                }.items()
            },
        })

    w.add_data("rows", rows)

    print("-" * 96)
    for k, (lbl, rel) in worst.items():
        print(f"  worst-rel {k:<12}: {float(rel):>+9.2%}  at {lbl}")
    w.add_data("worst_relative_error", {
        k: {"atom": lbl, "rel_err": str(rel)} for k, (lbl, rel) in worst.items()
    })

    # p ≠ n asymmetry direction check — the physical point of the re-run.
    pn_emp = lambda_empirical(M_N_MEV, VOL_BORROMEAN_8G, q_0) / \
        lambda_empirical(M_P_MEV, VOL_BORROMEAN_8G, q_0)
    pn_pk = tr_M["n"] / tr_M["p"]
    pn_check = {
        "lambda_emp_n_over_p": str(pn_emp),
        "tr_M_n_over_p": str(pn_pk),
        "lambda_A_n_over_p": "1 (degenerate by construction)",
        "note": (
            "Empirical n/p ratio of lambda_emp is m_n/m_p ~ 1.0014 (slightly "
            ">1). The per-knot base predicts tr_M(n)/tr_M(p) ~ 0.867 (<1, "
            "wrong direction, ~13% too low); lambda_A predicts exactly 1 "
            "(no split). Neither base carries the observed tiny p/n "
            "asymmetry at the multiplicative-lambda level."
        ),
    }
    w.add_data("pn_asymmetry_check", pn_check)
    print("-" * 96)
    print(f"  p/n split: lam_emp(n)/lam_emp(p) = {mp.nstr(pn_emp, 10)}   "
          f"tr_M(n)/tr_M(p) = {mp.nstr(pn_pk, 10)}   lambda_A ratio = 1")

    # Baseline-reproduction assertions vs the documented PR #1874 verdicts.
    proton_rel = (lam_A - lambda_empirical(M_P_MEV, VOL_BORROMEAN_8G, q_0)) \
        / lambda_empirical(M_P_MEV, VOL_BORROMEAN_8G, q_0)
    w.add_assertion(
        "L1a_lambdaA_proton_gap_matches_documented",
        computed=float(proton_rel),
        expected=0.0296,
        tolerance=2e-3,
        source=(
            "PR #1874 / AGENTS.md documented +2.96% lambda_A proton gap "
            "(lambda_A ~ 2.533 vs CODATA-implied ~ 2.46)."
        ),
    )
    w.add_assertion(
        "L1a_lambdaA_worst_at_4He_matches_documented",
        computed=float(worst["L1a_lambdaA"][1]),
        expected=-0.556,
        tolerance=5e-3,
        source="PR #1874 L1a worst-rel ~ -55.6% at 4He (lambda_A constant vs growing lambda_emp).",
    )

    # Honest verdict (audit-scope classification).
    l1a_pk_worst = abs(worst["L1a_perknot"][1])
    l1c_pk_worst = abs(worst["L1c_perknot"][1])
    if min(l1a_pk_worst, l1c_pk_worst) >= mp.mpf("0.25"):
        verdict = (
            "ROBUST (scope-limited, class (a)): swapping the fitted "
            "lambda_A for the canonical per-knot tr_M(K) does NOT rescue "
            "the L1 multiplicative lambda(K) closure — the per-knot forms "
            "fail HARDER on every atom (per-knot density is smaller than "
            "lambda_emp everywhere and shrinks with A while lambda_emp "
            "grows). The original refutation's negative verdict therefore "
            "extends to the per-knot base FOR THESE MULTIPLICATIVE FORMS "
            "ONLY. This is a scope-limited negative (a): it constrains the "
            "L1a/L1c functional family on both density bases; it does not "
            "structurally exclude tr_M(K) as an ingredient (binding-ratio "
            "uses, where the absolute scale cancels, are untouched). The "
            "p!=n structure of tr_M also points the wrong way for the "
            "n/p lambda ratio (0.867 vs empirical 1.0014), so the per-knot "
            "leverage claimed by the audit is NOT realized in this "
            "multiplicative absolute-mass family — consistent with the "
            "audit's own nuance that per-knot leverage lives in BINDING, "
            "not absolute mass."
        )
    else:
        verdict = (
            "ARTIFACT-INDICATIVE: at least one per-knot form lands within "
            "25% where the lambda_A form was refuted — the original "
            "refutation over-reached the density family. Re-scope per "
            "AGENTS.md (a)/(b) discipline."
        )
    w.add_data("rerun_verdict", verdict)
    print("-" * 96)
    print("  RERUN VERDICT:")
    for chunk in verdict.split(". "):
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
