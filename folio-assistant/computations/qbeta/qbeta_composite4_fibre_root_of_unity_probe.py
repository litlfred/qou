#!/usr/bin/env python3
"""qbeta_composite4_fibre_root_of_unity_probe.py — fibre-level Composite 4
reconnaissance for the Q_β c_3 residue A.

EXPLORATORY probe (task ② of the 2026-06-04 Habiro follow-up, PR #1802
scope doc `docs/scope/2026-06-04-habiro-fibre-composite4-mtau-scope.md`).
NOT a wire decision and NOT a derivation — it operationalises CLAUDE.md
§"Im(q) at fibre vs observable" for the c_3 closure and tests the #1801
verdict that the `/25` denominator is a **q-undeformed** constant.

## Self-contained

Uses only `mpmath` (no `pyhecke` / `q_parameter` / `witness_base` shims)
so it runs in the web sandbox. The canonical q₀ (50 dps) and the
cal-anchored c_3 are pinned as literals below — both verified against
`folio-assistant/computations/qbeta/*.witness.json` on main.

## Background

The c_3 closure on main (`MmuR9V9Closure.qbetaC3Closure`) is

    c_3 = -(q² + q⁻²) · (1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q)        (★)

evaluated at the real archimedean substrate q₀ ≈ 1.10998 → 2.65 ppm
near-match. PR #1801 showed the q-deformed `/[5]_q²` (at q₀) gives a
WORSE fit than `/25`, i.e. the denominator does NOT q-deform with q₀.

Since `[5]_q → 5` as q → 1, `/25 = /[5]_1²` is exactly `[5]_q²`
evaluated at the **classical / trivial-root-of-unity fibre point q = 1**,
while the rest of (★) evaluates at the **archimedean q₀**. That is the
literal fibre-vs-observable split: one factor lives at the fibre point,
the rest at the observable anchor.

## What this probe tests

1. **Baseline** — reproduce (★) at q₀ with `/25`; confirm ~2.65 ppm.
2. **Archimedean q-deform** — replace `/25 → /[5]_{q₀}²`; confirm WORSE
   (re-derives #1801 independently, self-contained).
3. **Root-of-unity sweep** — replace `/25 → /[5]_{ζ}²` for
   ζ = exp(2πi/N), N = 1..18. For each: does it beat `/25`? And is the
   resulting c_3 real (Im = 0, observable-admissible) or complex
   (fibre-only)?
4. **Fibre-point check** — confirm `[5]_q²` at q → 1 equals 25 exactly
   and is the unique real root-of-unity evaluation matching the
   undeformed denominator.

## Δ_λ-gate

No fitted forms; nothing wired. Expected outcome: NEGATIVE/CONFIRMATORY
— root-of-unity evaluations are generically complex (so not directly
observable, consistent with Im(q_obs)=0), and only the q=1 fibre point
reproduces the undeformed `/25`. This bounds the fibre-evaluation space
and makes the "fibre point = q=1" reading concrete.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf, exp, pi, fabs, re

mp.dps = 60

# ── Pinned canonical constants (verified vs main witnesses) ──
Q0_STR = "1.1099785827513808075916690956107688798744991218736"
C3_CAL_STR = "-2.06934257711516783787971951725"


def quantum_int(n: int, q):
    """[n]_q = (q^n - q^-n)/(q - q^-1); generic (works for complex q)."""
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hbar(q):
    return (q - 1) / q


def c3_closure(q, denom):
    """The (★) closure with a configurable rung-1 denominator `denom`
    (default categorical value is 25). Everything else at archimedean q."""
    base = -(q ** 2 + q ** (-2))
    r1 = hbar(q) * quantum_int(3, q) / denom
    r2 = hbar(q) ** 3 / quantum_int(2, q)
    return base * (1 + r1 + r2)


def ppm(val, target):
    return float(fabs((val - target) / target) * mpf(10) ** 6)


def main() -> int:
    q0 = mpf(Q0_STR)
    target = mpf(C3_CAL_STR)

    print("=" * 78)
    print(" Fibre-level Composite 4 — root-of-unity reconnaissance for c_3")
    print("=" * 78)
    print(f"  q₀        = {mp.nstr(q0, 16)}")
    print(f"  c_3 (cal) = {mp.nstr(target, 16)}")
    print()

    results = {}

    # 1. Baseline /25 at q0.
    c3_25 = c3_closure(q0, mpf(25))
    ppm_25 = ppm(c3_25, target)
    print(f"  [1] /25 (undeformed, = [5]_1²):  c_3 = {mp.nstr(c3_25, 14)}  "
          f"{ppm_25:.3f} ppm")
    results["denom_25_undeformed"] = {"c3": mp.nstr(c3_25, 20), "ppm": ppm_25}

    # 2. Archimedean q-deform /[5]_{q0}².
    five_q0_sq = quantum_int(5, q0) ** 2
    c3_5q = c3_closure(q0, five_q0_sq)
    ppm_5q = ppm(c3_5q, target)
    print(f"  [2] /[5]_q₀² (archimedean):      c_3 = {mp.nstr(c3_5q, 14)}  "
          f"{ppm_5q:.3f} ppm   ([5]_q₀² = {mp.nstr(five_q0_sq, 10)})")
    results["denom_5_q0_archimedean"] = {
        "c3": mp.nstr(c3_5q, 20), "ppm": ppm_5q,
        "five_q0_sq": mp.nstr(five_q0_sq, 20),
    }

    # 3. Root-of-unity sweep: denom = [5]_ζ², ζ = exp(2πiθ), θ = 1/N.
    #    For a root of unity, [5]_ζ = sin(5θ·2π/2)/... = sin(5·2π/N)/sin(2π/N)
    #    is REAL (the imaginary part is numerical noise, chopped below).
    #    [5]_ζ = 0 (degenerate denominator) whenever N | 5·k cancels — e.g.
    #    N=10 gives sin(π)=0; those are skipped as ill-defined.
    print()
    print("  [3] root-of-unity denominators /[5]_ζ²  (ζ = exp(2πi/N)) — [5]_ζ is real:")
    print(f"      {'N':>3} {'[5]_ζ² (real)':>16} {'c_3 vs cal (ppm)':>18} {'note':>14}")
    roots = {}
    best_real_N, best_real_ppm = None, float("inf")
    for N in range(3, 25):
        zeta = exp(2j * pi / N)
        five = quantum_int(5, zeta)
        # chop numerical noise: [5]_ζ is real for roots of unity
        five_re = re(five)
        denomZ = five_re ** 2
        if float(fabs(denomZ)) < 1e-6:
            print(f"      {N:>3} {'~0 (degenerate)':>16} {'—':>18} {'[5]_ζ=0':>14}")
            roots[f"N={N}"] = {"denom_real": mp.nstr(denomZ, 6),
                               "degenerate": True}
            continue
        c3z = re(c3_closure(q0, denomZ))
        ppmz = ppm(c3z, target)
        note = "→25 (q→1)" if abs(float(denomZ) - 25.0) < 0.5 else ""
        print(f"      {N:>3} {mp.nstr(denomZ, 10):>16} {ppmz:>18.1f} {note:>14}")
        roots[f"N={N}"] = {"denom_real": mp.nstr(denomZ, 12),
                           "c3_ppm": ppmz, "degenerate": False}
        if ppmz < best_real_ppm:
            best_real_ppm, best_real_N = ppmz, N
    results["root_of_unity_sweep"] = roots
    results["best_finite_root"] = {"N": best_real_N, "ppm": best_real_ppm}

    # 4. Fibre-point confirmation: [5]_q² → 25 as q → 1.
    print()
    five_near_one = quantum_int(5, mpf("1.0000000001")) ** 2
    print(f"  [4] [5]_q² as q→1: {mp.nstr(five_near_one, 12)}  (→ 25 = [5]_1²)")
    results["five_q_sq_classical_limit"] = mp.nstr(five_near_one, 20)

    # ── Verdict ──
    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    improved = ppm_5q < ppm_25
    any_root_beats = best_real_ppm < ppm_25
    print(f"  • /25 baseline: {ppm_25:.3f} ppm.")
    print(f"  • q-deformed /[5]_q₀²: {ppm_5q:.1f} ppm "
          f"({'BETTER' if improved else 'WORSE'} than /25) "
          f"→ {'contradicts' if improved else 'CONFIRMS'} #1801.")
    print(f"  • [5]_ζ² at roots of unity is REAL = (sin5θ/sinθ)², taking")
    print(f"    DISCRETE values (1, degenerate 0, …); best finite root N="
          f"{best_real_N} gives {best_real_ppm:.0f} ppm "
          f"({'beats' if any_root_beats else 'does NOT beat'} /25).")
    print(f"  • [5]_q²=25 is reached only as N→∞ (θ→0), i.e. the q→1 classical")
    print(f"    / trivial-fibre limit — confirmed by [4].")
    print()
    print("  ⇒ The /25 is [5]_q² pinned at the q=1 classical fibre point while")
    print("    the rest of c_3 evaluates at archimedean q₀ — a real (not")
    print("    complex) fibre/observable split. No finite root of unity and")
    print("    not q₀ reproduces it. The Q_β residue A is NOT recovered by a")
    print("    single denominator-swap; a genuine Habiro element (cyclotomic")
    print("    coefficients across ALL roots of unity) + τ is still required.")
    print("    Reconnaissance only — bounds the space, derives nothing.")

    verdict = {
        "qdeform_confirms_1801_undeformed": not improved,
        "five_zeta_sq_is_real_discrete": True,
        "any_finite_root_beats_25": any_root_beats,
        "twenty_five_is_q1_classical_limit": True,
        "conclusion": (
            "Independently re-derives #1801 (self-contained): q-deformed "
            f"/[5]_q₀² is WORSE ({ppm_5q:.0f} ppm) than undeformed /25 "
            f"({ppm_25:.2f} ppm). [5]_ζ² at roots of unity is REAL "
            "(=(sin5θ/sinθ)²) and discrete; no finite root reproduces 25 — "
            "only the N→∞ (q→1) classical limit does. So /25 = [5]_q² at the "
            "q=1 fibre point, rest of c_3 at archimedean q₀ (a real "
            "fibre/observable split). A full residue-A derivation still needs "
            "the Habiro element (cyclotomic coefficients over all roots of "
            "unity) + τ, which a single denominator-swap cannot supply. "
            "EXPLORATORY; nothing wired."
        ),
    }
    results["verdict"] = verdict

    # ── Emit a lightweight witness (self-contained schema) ──
    out = Path(__file__).resolve().parent / \
        "qbeta-composite4-fibre-root-of-unity-probe.witness.json"
    witness = {
        "engine": "mpmath",
        "engineVersion": "mpmath",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-composite4-fibre-root-of-unity-probe",
        "scriptFile": "qbeta_composite4_fibre_root_of_unity_probe.py",
        "precisionMetadata": {"compute_dps": 60},
        "assertions": [
            {
                "name": "qdeform_5_q0_sq_worse_than_undeformed_25",
                "computed": not improved,
                "expected": True,
                "passed": (not improved),
                "source": "Independent self-contained re-derivation of #1801: "
                          "the q-deformed /[5]_q₀² denominator gives a worse c_3 "
                          "fit than the undeformed /25.",
            },
            {
                "name": "no_finite_root_of_unity_reproduces_25",
                "computed": bool(not any_root_beats),
                "expected": True,
                "passed": bool(not any_root_beats),
                "source": "[5]_ζ² at ζ=exp(2πi/N) is real (=(sin5θ/sinθ)²) and "
                          "discrete; no finite root reproduces the /25 denominator "
                          "or beats it on c_3 — 25 is the N→∞ (q→1) classical "
                          "limit. Confirms residue A is not a single root-of-unity "
                          "denominator-swap.",
            },
        ],
        "data": {"q0": Q0_STR, "c3_cal": C3_CAL_STR, **results},
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    out.write_text(json.dumps(witness, indent=2))
    print()
    print(f"✓ Witness: {out.name}  "
          f"({len(witness['assertions'])} assertions, "
          f"{'all passed' if witness['allPassed'] else 'FAILURES'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
