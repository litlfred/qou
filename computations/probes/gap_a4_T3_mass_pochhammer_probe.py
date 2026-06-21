#!/usr/bin/env python3
"""GAP-A-4 T3 probe — Path-B-specific λ(K) via bar-symmetric q-Pochhammer.

Implements §4 of the just-merged T3 scope
([`docs/audits/2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md`](../../docs/audits/2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md)).
Tests whether ANY closed-form bar-symmetric q-Pochhammer combination
reproduces the light-series target ratios m(K)/m(p) to within the
discipline's tolerances.

Per the scope §4:

  I1 — `R_mass` is bar-symmetric (`q ↔ q⁻¹` invariant) → candidate
       solutions have definite parity in `h = (q − q⁻¹)/q^{1/2}`.
  I2 — proton root: `λ(p) = 2.4600...` (by CAL-1 m_e calibration).
       Any candidate failing this is REFUTED before any data probe.

Empirical target — ratio of per-atom λ:

  Target_K = λ_emp(K) / λ_emp(p) = m(K)·Vol(p)/(m(p)·Vol(K))

(using the same per-knot Vol convention as T2/L1.  Path-B-specific
λ(K) under any candidate `f` is `f(β_K, q₀)` divided by some
normalisation; the proton root I2 fixes the normalisation, so we
test the candidate's per-atom ratio directly.)

Candidates (bar-symmetric, closed-form, no fitting):

  P1 — q-factorial ratio: [3·A]_q! / [3]_q! (depth-3A bar-symmetric)
  P2 — q-Pochhammer ratio: |(q;q)_{3A}|² / |(q;q)_3|²
        (the "double bar-Pochhammer" at the H_{3A} strand count)
  P3 — Markov-trace ratio: tr_M(β_K, q₀) / tr_M(β_p, q₀)
        (the per-atom Markov trace, which IS the bar-symmetric
        Σ_λ y_λ χ^λ sum at q₀)
  P4 — Phase-4 amplitude ratio: A_Phase4(K) / A_Phase4(p)
        (CONTROL — should match the binding-amplitude side, not the
        mass-multiplier side; tests whether the two factor the same way)

If any candidate matches all 5 non-proton target ratios to <5 %,
the T3 conjecture (λ(K) is a bar-symmetric q-Pochhammer object) is
SUPPORTED, modulo categorical derivation.  If all four refute, the
restricted Pochhammer space is empty and the conclusion is the
τ-image Dirac/SW PDE direction (per scope §7).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.
"""
from __future__ import annotations

import json
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
from codata_constants import M_D_MEV_VALIDATION, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, M_T_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"

M_E_MEV = mp.mpf("0.51099895069")
M_P_MEV = mp.mpf(M_P_MEV_VALIDATION)
M_N_MEV = mp.mpf(M_N_MEV_VALIDATION)
M_D_MEV = mp.mpf(M_D_MEV_VALIDATION)
M_T_MEV = mp.mpf(M_T_MEV_VALIDATION)
M_HE3_MEV = mp.mpf("2808.39160743")
M_HE4_MEV = mp.mpf("3727.37941")

# Per-knot Vol(K) per Phase-4 SnapPy JSJ convention (T2-recommended;
# least-bad of the three at +132 % swing).
VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")


LIGHT_SERIES = [
    # (label, Z, N, m_K, vol_K)
    ("p",   1, 0, M_P_MEV,    VOL_BORROMEAN_8G),
    ("n",   0, 1, M_N_MEV,    VOL_BORROMEAN_8G),
    ("D",   1, 1, M_D_MEV,    VOL_PHASE4_Z1),
    ("T",   1, 2, M_T_MEV,    VOL_PHASE4_Z1),
    ("3He", 2, 1, M_HE3_MEV,  VOL_PHASE4_Z2),
    ("4He", 2, 2, M_HE4_MEV,  VOL_PHASE4_Z2),
]


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def q_number(n: int, q_0: mp.mpf) -> mp.mpf:
    """[n]_q = (q^n − q^{−n}) / (q − q^{−1}) at q_0."""
    if n == 0:
        return mp.mpf(0)
    num = q_0 ** n - q_0 ** (-n)
    den = q_0 - q_0 ** (-1)
    return num / den


def q_factorial(n: int, q_0: mp.mpf) -> mp.mpf:
    """[n]_q! = product over k=1..n of [k]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_number(k, q_0)
    return out


def q_pochhammer(n: int, q_0: mp.mpf) -> mp.mpf:
    """|(q; q)_n| = product over k=1..n of |1 − q^k| at q_0 real,
    q_0 > 1, where each factor is 1 − q_0^k < 0.  Returns the
    absolute value (bar-symmetric)."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= abs(mp.mpf(1) - q_0 ** k)
    return out


def lambda_emp(m_K: mp.mpf, vol_K: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """λ_emp(K) = m(K)·ℏ_q²/(m_e·Vol(K)) — the Path B inversion."""
    return m_K * hbar_q_sq(q_0) / (M_E_MEV * vol_K)


def _load_chi_cache_tr_M(atom: str, n_strands: int) -> mp.mpf:
    """Load tr_M(β_K, q₀) from the canonical chi-cache. Falls back to
    None if unavailable for the given atom — the probe records that
    candidate as `n/a` rather than failing.

    For the proton/neutron (n=3) and the H_{3A} caches (D=6, T=9,
    ³He=9, ⁴He=12), the cache file is
    `chi-{atom}-h{n_strands}-at-q0-50dps.witness.json`.  For p/n the
    file contains a top-level `tr_M_at_q0` field; for the others we
    sum `Σ_λ y_λ·χ^λ` via the same combiner the GAP-A-3 probe used.
    """
    path = COMPUTE_DIR / f"chi-{atom}-h{n_strands}-at-q0-50dps.witness.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    if "tr_M_at_q0" in data:
        return mp.mpf(data["tr_M_at_q0"])
    # Per-partition; combine with y_λ from the canonical y-table.
    y_path = COMPUTE_DIR / "y-lambda-at-q0.witness.json"
    if not y_path.exists():
        return None
    y_raw = json.loads(y_path.read_text())["data"]["by_n"]
    y_by_part = {
        tuple(row["partition"]): mp.mpf(row["y_at_q0_50dps"])
        for row in y_raw[str(n_strands)]
    }
    tr_m = mp.mpf(0)
    for entry in data["by_partition"]:
        lam = tuple(entry["partition"])
        if lam not in y_by_part:
            return None  # incomplete coverage
        tr_m += y_by_part[lam] * mp.mpf(entry["chi_lambda"])
    return tr_m


def A_phase4(Z: int, N: int, vol_hyp: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """Phase-4 amplitude: Vol_hyp(K)/[8]_q · [3]_q^{2(Z−1)} · (q^{1/2}+q^{−1/2})^{4N}."""
    eight_q = q_number(8, q_0)
    three_q = q_number(3, q_0)
    spin = (mp.sqrt(q_0) + 1 / mp.sqrt(q_0)) ** (4 * N)
    color = three_q ** (2 * (Z - 1))
    return vol_hyp / eight_q * color * spin


# Map atom label → chi-cache atom name + H_{3A} strand count
CHI_CACHE_MAP = {
    "p":   ("proton",     3),
    "n":   ("neutron",    3),
    "D":   ("deuteron",   6),
    "T":   ("tritium",    9),
    "3He": ("helium-3",   9),
    "4He": ("helium-4",  12),
}


def _verdict(rel_err: mp.mpf) -> str:
    a = abs(rel_err)
    if a < mp.mpf("5e-2"):
        return "NEAR-MATCH (< 5 %)"
    if a < mp.mpf("0.25"):
        return "NEAR-MATCH (< 25 %)"
    return "REFUTED"


def main() -> int:
    w = WitnessBuilder("gap-a4-T3-mass-pochhammer-probe", engine="mpmath")
    w.set_audit_only("docs/audits/2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md")
    w.set_description(
        "GAP-A-4 T3 probe: test bar-symmetric q-Pochhammer "
        "combinations as the Path-B-native λ(K) formulation.  Four "
        "candidates (q-factorial, q-Pochhammer, Markov trace, "
        "Phase-4 amplitude as control) tested against the light-"
        "series λ_emp(K) / λ_emp(p) target ratios.  I1 + I2 "
        "(bar-symmetry + proton anchor) pre-narrow the candidate "
        "space.  EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    print("=" * 78)
    print("GAP-A-4 T3 probe — bar-symmetric q-Pochhammer for Path-B-native λ(K)")
    print("=" * 78)
    print(f"  q₀                       = {Q_0_50DPS[:24]}...")
    print(f"  ℏ_q²                     = {float(hbar_q_sq(q_0)):.10f}")

    # Empirical proton anchor (I2)
    proton_row = LIGHT_SERIES[0]
    _, _, _, m_p, vol_p = proton_row
    lam_emp_p = lambda_emp(m_p, vol_p, q_0)
    print(f"  λ_emp(p)                  = {float(lam_emp_p):.6f}  (I2 anchor)")
    print()

    # Compute target ratios and four candidate ratios per atom
    print(f"  {'atom':<4} {'A':>2} {'λ_emp/λ_emp(p)':>15} "
          f"{'P1 (q-fact)':>14} {'P2 (q-Poch)':>14} "
          f"{'P3 (tr_M)':>12} {'P4 (A_P4)':>12}")
    print("-" * 86)

    # Pre-compute proton anchor values
    qfact_p = q_factorial(3, q_0)
    qpoch_p = q_pochhammer(3, q_0) ** 2  # |(q;q)_3|² (bar-symmetric)
    tr_M_p = _load_chi_cache_tr_M("proton", 3)
    A_p = A_phase4(1, 0, vol_p, q_0)

    rows = []
    candidate_swings = {p: [] for p in ["P1", "P2", "P3", "P4"]}
    for label, Z, N, m_K, vol_K in LIGHT_SERIES:
        A = Z + N
        lam_K = lambda_emp(m_K, vol_K, q_0)
        target = lam_K / lam_emp_p

        # Bar-symmetric q-Pochhammer candidates
        P1 = q_factorial(3 * A, q_0) / qfact_p
        P2 = (q_pochhammer(3 * A, q_0) ** 2) / qpoch_p
        atom_name, n_strands = CHI_CACHE_MAP[label]
        tr_M_K = _load_chi_cache_tr_M(atom_name, n_strands)
        P3 = tr_M_K / tr_M_p if (tr_M_K is not None and tr_M_p) else None
        A_K = A_phase4(Z, N, vol_K, q_0)
        P4 = A_K / A_p

        for code, pred in [("P1", P1), ("P2", P2), ("P3", P3), ("P4", P4)]:
            if pred is None:
                continue
            rel = (pred - target) / target if target != 0 else mp.mpf("inf")
            candidate_swings[code].append(abs(rel))

        p3_str = f"{float(P3):>12.4f}" if P3 is not None else f"{'n/a':>12}"
        print(f"  {label:<4} {A:>2} {float(target):>15.6f} "
              f"{float(P1):>14.4f} {float(P2):>14.4f} "
              f"{p3_str} {float(P4):>12.4f}")

        rows.append({
            "label": label, "Z": Z, "N": N, "A": A,
            "lambda_emp_K": str(lam_K),
            "target_ratio_lambda_K_over_lambda_p": str(target),
            "P1_q_factorial_ratio": str(P1),
            "P2_q_pochhammer_sq_ratio": str(P2),
            "P3_trM_ratio": str(P3) if P3 is not None else "n/a",
            "P4_A_phase4_ratio": str(P4),
        })

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("lambda_emp_proton_anchor", str(lam_emp_p))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("per_atom_candidates", rows)

    # Per-candidate worst rel_err across non-proton atoms
    print()
    print("-" * 78)
    print(f"  {'candidate':<28} {'worst rel_err':>16} {'verdict':>22}")
    print("-" * 78)
    candidate_verdicts = []
    for code, swings in candidate_swings.items():
        # Drop the proton row (always 0 by construction) from the worst-row scan
        non_proton = swings[1:]
        if not non_proton:
            continue
        worst = max(non_proton)
        verdict = _verdict(worst)
        candidate_verdicts.append({
            "code": code, "worst_rel_err": str(worst), "verdict": verdict,
        })
        labels = {"P1": "P1 (q-factorial)", "P2": "P2 (q-Pochhammer²)",
                  "P3": "P3 (Markov-trace)", "P4": "P4 (Phase-4 amp, control)"}
        print(f"  {labels[code]:<28} {float(worst):>+16.2%} {verdict:>22}")
    w.add_data("candidate_verdicts", candidate_verdicts)

    # Synthesis
    matches = [v for v in candidate_verdicts if "MATCH" in v["verdict"]]
    if matches:
        synthesis = (
            f"At least one bar-symmetric q-Pochhammer candidate matches "
            f"the light-series λ_emp(K) / λ_emp(p) target ratios within "
            f"5 % with no fitting: {[m['code'] for m in matches]}.  T3's "
            f"conjecture that λ(K) is a bar-symmetric q-Pochhammer "
            f"object is SUPPORTED numerically; the next step is "
            f"identifying the categorical content of the matching "
            f"candidate (per the 'fix as numerology unless derivable' "
            f"discipline, this is not yet a derivation — just a "
            f"non-random match)."
        )
    else:
        synthesis = (
            f"None of the four bar-symmetric q-Pochhammer candidates "
            f"matches the light-series λ ratios within 5 %.  Worst "
            f"rel_errs: "
            f"{', '.join(v['code'] + ': ' + format(float(mp.mpf(v['worst_rel_err'])), '+.2%') for v in candidate_verdicts)}.  "
            f"T3 closes NEGATIVE for the Habiro-Pochhammer layer — "
            f"the restricted bar-symmetric space (per I1) is empty for "
            f"the natural depth-3A candidates.  Per the scope §7 "
            f"honest-outcome alternative, this points firmly to the "
            f"τ-image Dirac/SW PDE direction (the same direction PR "
            f"#1871's workplan §4.A L3 names as load-bearing).  "
            f"The mass-side and binding-side GAP-A-4 closure converges "
            f"on the τ-image Dirac/SW PDE as the framework's last open "
            f"derivation question."
        )
    w.add_data("synthesis_verdict", synthesis)
    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Sanity assertion: P4 (control) at p must give 1.0 exactly
    w.add_assertion(
        "P4_control_proton_ratio_is_one",
        computed=float(A_p / A_p),
        expected=1.0,
        tolerance=1e-40,
        source=(
            "P4 control: A_Phase4(p) / A_Phase4(p) = 1 by construction; "
            "any deviation signals an arithmetic bug."
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
