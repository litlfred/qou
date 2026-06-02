"""Option E v9 multiplicative correction — categorical-uniqueness test.

Per author 2026-05-31 direction ("C — Test Option E v9's (1+q)/2 structurally").

## Context

Option E v9 (`option_e_v9_all_symmetries.py`, commit 30c5393b7e)
needed to close a 6.15% gap on the T - ³He mirror-pair Casimir
difference. From a curated 10-candidate scan:

  v8 base = 0.7232 MeV ; target = 0.7637 MeV
  required multiplicative correction = 1.05605

Best candidate found:
  (1 + q)/2 = 1.054855 → -0.11% off

This is a striking near-match. The commit headline reads
"BREAKTHROUGH — mirror pair CLOSED to 0.11%."

## What this probe does

Tests whether `(1 + q)/2` is **uniquely identified** by the
0.11% match — or if multiple categorically-natural candidates
also match within this band (in which case the v9 finding is a
"coincidence basin," NOT a structural derivation, per CLAUDE.md
anti-pattern "matches at q_0 ≠ uniquely fixed by structure").

Method:
1. Enumerate ~30 Hecke-algebra-natural and q-arithmetic-natural
   candidates for multiplicative corrections at q_0
2. Compare each to target 1.05605
3. Report ALL candidates matching within 0.5%, 0.1%
4. If `(1 + q)/2` is unique, structurally significant
5. If multiple match, v9 is one of several basins — pre-screen
   for v10 to test more candidates structurally

## Categorical interpretation of (1+q)/2 (if structurally unique)

`(1 + q)/2 = (q^0 + q^1)/2` is the arithmetic mean of the trivial-rep
eigenvalue `q^0 = 1` and the q-deformed positive-crossing eigenvalue
`q^1 = q` on Hecke generators. Specifically: T_s acts as q on the
trivial rep V_{(n)} and as -q⁻¹ on the sign rep V_{(1^n)}; the
average (1 + q)/2 represents a balanced superposition of trivial-rep
weight with positive-crossing weight.

## Cross-references

- option_e_v9_all_symmetries.py (the v9 probe)
- 2026-05-31 audit on canonical-no-negative-result-in-paper watcher (#1574)
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps(50)

    q = mp.mpf(Q_50_DIGIT_STR)

    # Recompute target precisely from v9's v8_base and diff_target
    v8_base = mp.mpf("0.7232")
    diff_target = mp.mpf("0.7637")
    target_exact = diff_target / v8_base
    print("=" * 78)
    print("Option E v9 multiplicative-correction uniqueness audit (50 dps)")
    print("=" * 78)
    print(f"\nq_0      = {Q_50_DIGIT_STR}")
    print(f"v8 base  = {mp.nstr(v8_base, 12)} MeV")
    print(f"target   = {mp.nstr(diff_target, 12)} MeV")
    print(f"required multiplicative correction = "
          f"target/v8_base = {mp.nstr(target_exact, 18)}")
    print()

    # Helpers
    h = q - 1 / q
    h2 = h * h
    qi = 1 / q
    qbracket2 = q + qi
    qbracket3 = q ** 2 + 1 + qi ** 2
    qbracket4 = q ** 3 + q + qi + qi ** 3
    qbracket5 = q ** 4 + q ** 2 + 1 + qi ** 2 + qi ** 4
    hbar_q = 1 - qi  # ℏ_q = 1 - 1/q

    # Candidate list — Hecke / q-arithmetic naturals
    candidates = [
        # Originals from v9
        ("(1 + q)/2", (1 + q) / 2),
        ("1 + h_q²", 1 + h2),
        ("1 + h", 1 + h),
        ("1 + h/2", 1 + h / 2),
        ("q/[2]_q", q / qbracket2),
        ("[2]_q/2", qbracket2 / 2),
        ("(q²+1)/q²", (q ** 2 + 1) / q ** 2),
        ("(q+1)²/(4q)", (q + 1) ** 2 / (4 * q)),
        ("1 + h_q + h_q²", 1 + h + h2),
        # More q-arithmetic naturals
        ("(1 + q⁻¹)/2", (1 + qi) / 2),
        ("(1 + q²)/2", (1 + q ** 2) / 2),
        ("q^(1/2)", mp.sqrt(q)),
        ("[3]_q/3", qbracket3 / 3),
        ("[4]_q/4", qbracket4 / 4),
        ("[5]_q/5", qbracket5 / 5),
        ("(1+q)/[2]_q", (1 + q) / qbracket2),
        ("(1+q²)/(2q)", (1 + q ** 2) / (2 * q)),
        ("(1+q²)/[2]_q²", (1 + q ** 2) / qbracket2 ** 2),
        # Hecke-eigenvalue averages
        ("(q + 1)/(q − q⁻¹+1)", (q + 1) / (q - qi + 1)),
        # h-based
        ("1 + h²/2", 1 + h2 / 2),
        ("1 + h²·G", 1 + h2 * mp.catalan),
        ("1 - h²·G", 1 - h2 * mp.catalan),
        ("ℏ_q² + 1", hbar_q ** 2 + 1),
        ("(1 + ℏ_q)", 1 + hbar_q),
        ("(1 + ℏ_q²)", 1 + hbar_q ** 2),
        # Mixed
        ("[2]_q·q/(1+q²)", qbracket2 * q / (1 + q ** 2)),
        ("(2q)/(1+q²)", 2 * q / (1 + q ** 2)),
        ("cosh(h)", mp.cosh(h)),
        ("cosh(h/2)", mp.cosh(h / 2)),
        ("exp(h/10)", mp.exp(h / 10)),
        ("exp(h²/2)", mp.exp(h2 / 2)),
    ]

    # Score each candidate
    scored = []
    for name, val in candidates:
        err_pct = (val - target_exact) / target_exact * 100
        scored.append((name, val, err_pct))

    scored.sort(key=lambda r: abs(r[2]))

    print(f"All candidates sorted by |error|:")
    print(f"  {'name':<28}{'value':<16}{'err (%)':<14}{'within band'}")
    for name, val, err in scored:
        marker = ""
        if abs(err) < 0.05:
            marker = " ⭐ within 0.05%"
        elif abs(err) < 0.1:
            marker = " * within 0.1%"
        elif abs(err) < 0.5:
            marker = " . within 0.5%"
        print(f"  {name:<28}{mp.nstr(val, 12):<16}{mp.nstr(err, 8):<14}{marker}")

    # Discrimination
    within_005 = [r for r in scored if abs(r[2]) < mp.mpf("0.05")]
    within_011 = [r for r in scored if abs(r[2]) < mp.mpf("0.11")]
    within_05 = [r for r in scored if abs(r[2]) < mp.mpf("0.5")]

    print(f"\n[Summary]")
    print(f"  Within 0.05%: {len(within_005)} candidates")
    for n, v, e in within_005:
        print(f"    {n}: err = {mp.nstr(e, 6)}%")
    print(f"  Within 0.11% (v9 threshold): {len(within_011)} candidates")
    for n, v, e in within_011:
        print(f"    {n}: err = {mp.nstr(e, 6)}%")
    print(f"  Within 0.5%: {len(within_05)} candidates")

    if len(within_011) == 1:
        verdict = (
            f"UNIQUE: only '{within_011[0][0]}' matches within 0.11%. "
            f"This is structurally suggestive (though not yet a derivation)."
        )
    elif len(within_011) <= 3:
        verdict = (
            f"NEAR-UNIQUE: {len(within_011)} candidates match within 0.11%. "
            f"v9 found one of a small basin; structurally weak — need "
            f"a categorical derivation, not a curated scan."
        )
    else:
        verdict = (
            f"COINCIDENCE BASIN: {len(within_011)} candidates match within "
            f"0.11%. The v9 'BREAKTHROUGH' framing overstates — many "
            f"q-arithmetic forms cluster at this precision. CLAUDE.md "
            f"anti-pattern: 'matches at q_0 ≠ uniquely fixed by structure'."
        )

    print(f"\n  VERDICT: {verdict}")

    # Witness
    w = WitnessBuilder("option-e-v9-one-plus-q-structural-audit",
                       engine="python")
    w.set_description(
        "Categorical-uniqueness test for Option E v9's (1+q)/2 "
        "multiplicative correction. Tests whether the 0.11% match is "
        "uniquely identifying or one of several near-matches in a "
        "coincidence basin."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_parameter("target_multiplicative_correction",
                    mp.nstr(target_exact, 25))
    w.add_data("n_candidates_tested", len(candidates))
    w.add_data("n_within_0.05_pct", len(within_005))
    w.add_data("n_within_0.11_pct", len(within_011))
    w.add_data("n_within_0.5_pct", len(within_05))
    w.add_data("matches_within_0.11_pct",
               [(n, mp.nstr(v, 18), mp.nstr(e, 10)) for n, v, e in within_011])
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="audit_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Option E v9 uniqueness audit completed.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
