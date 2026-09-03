#!/usr/bin/env python3
"""
mirror_nuclei_coulomb_systematics.py — the mirror binding split is Coulomb across the
WHOLE isobaric chain, bounding the strong-CSB budget any QOU kernel is allowed.

Generalises the A=3 result of #3564 (`mirror_split_coulomb_diagnosis.py`): there the
observed ³H/³He mirror split was shown to be the pp Coulomb displacement energy. This
extends it to the mirror-nuclei chain ³H/³He … ³⁹K/³⁹Ca using the repo's canonical
uniform-sphere Coulomb (`computations/coulomb_energy.mirror_displacement_mev`, discrete-
proton self-energy Z(Z−1), r₀=1.2 fm — NO free parameter):

    ΔE_C = (3/5)·(α ħc)·[Z_hi(Z_hi−1) − Z_lo(Z_lo−1)] / (r₀·A^{1/3}).

The observed split tracks ΔE_C: the ratio split_AME/ΔE_C is ~0.8 across A=3–39 — i.e.
the split is PROPORTIONAL to Coulomb (the ~0.8 factor is the known uniform-sphere
over-estimate of the Coulomb displacement energy). The scatter of that ratio bounds the
strong charge-symmetry-breaking.

⚠ THE RATIO IS NOT CONSTANT — corrected 2026-08-25. This docstring, the witness
description and the assertion source all said "≈ constant". They were wrong: the ratio
rises MONOTONICALLY with A, and the +/- 0.06 is a trend, not noise about a mean.
Measured on these same eight rows with exact Fraction arithmetic (see the trend block
below): Pearson r = 0.830, t = 3.65 on 6 dof (crit 2.447 => p < 0.05), and a straight
line beats the mean by 44% in rms (0.0329 vs 0.0589).

The proportionality FINDING is unaffected — the split does track Coulomb, and the
charge-symmetry consequence for the strong kernel stands. What was wrong is the
characterisation of the residual as constant scatter.

CONSEQUENCE, and the reason this matters rather than being pedantry: the A=3 datum is
0.765, against the chain mean of 0.838 — 1.15 sd away. A=3 is the He-3 case that the
m_d - m_u front reads. Anyone quoting the chain mean for it is off by that much. The
witness now carries per-A trend data so no consumer has to take a mean on trust.

QOU consequence: any strong/categorical binding kernel (#2089 log-trace `f_bond`,
#3548 connected `tr_M`) must be charge-symmetric — the split is Coulomb, not strong.
The #2089 kernel's pure-strong A=3 mirror split (2.27 MeV, #3564) is ~3× the whole
observed split and the Coulomb systematics shows this is a SYSTEMATIC requirement (all
A), not an A=3 accident. Constrains the kernel derivation (→ #3548); does not fit binding.

EXPLORATORY — scope-limited (a). Canonical shared Coulomb (no free parameter); no
production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from decimal import Decimal, getcontext  # noqa: E402
from fractions import Fraction as F  # noqa: E402

from codata_constants import _ame_binding_mev  # noqa: E402

getcontext().prec = 50
from coulomb_energy import mirror_displacement_mev  # noqa: E402 — canonical Z(Z−1), r₀=1.2
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()

# mirror pairs: (name, Z_light, Z_heavy, A). Same A, Z_heavy = Z_light + 1 (T_z mirror).
PAIRS = [("3H/3He", 1, 2, 3), ("7Li/7Be", 3, 4, 7), ("11B/11C", 5, 6, 11),
         ("13C/13N", 6, 7, 13), ("15N/15O", 7, 8, 15), ("23Na/23Mg", 11, 12, 23),
         ("27Al/27Si", 13, 14, 27), ("39K/39Ca", 19, 20, 39)]


def split_ame(Z1, Z2, A):
    # lighter-Z mirror binds MORE (less Coulomb) ⇒ positive split = B(lo) − B(hi)
    return float(mp.mpf(str(_ame_binding_mev(Z1, A))) - mp.mpf(str(_ame_binding_mev(Z2, A))))


def main() -> int:
    print("  Canonical uniform-sphere Coulomb ΔE_C (Z(Z−1), r₀=1.2 fm; "
          "computations/coulomb_energy.py) — NO free parameter.\n")
    print(f"  {'pair':<11}{'A':>3}{'split_AME':>10}{'ΔE_C':>9}{'split/ΔE_C':>12}")
    ratios = []
    rows = []
    for nm, Z1, Z2, A in PAIRS:
        s = split_ame(Z1, Z2, A)
        c = mirror_displacement_mev(Z2, Z1, A)
        ratio = s / c
        # mpf is kept in the DATA path (the raw-float64 gate requires it); the
        # float() below is display-only, which AGENTS.md permits in an f-string.
        ratios.append(ratio)
        rows.append((nm, A, s, c, ratio))
        # float() here is DISPLAY ONLY (AGENTS.md permits it inside an f-string).
        # mirror_displacement_mev returns an mpf, which has no __format__ for the
        # 'f' presentation type — this line raised TypeError on main until
        # 2026-08-25, so the producer could not run at all. Third instance of the
        # mpf-formatting class fixed in PR #5615.
        print(f"  {nm:<11}{A:>3}{float(s):>10.3f}{float(c):>9.3f}{float(ratio):>12.3f}")

    mean_r = sum(ratios) / len(ratios)
    rms_dev = (sum((r - mean_r) ** 2 for r in ratios) / len(ratios)) ** 0.5

    # --- trend in A (added 2026-08-25; the ratio is NOT constant) -------------
    # Exact Fraction arithmetic: the ratios are quotients of exact decimals, so
    # nothing here needs mpmath and nothing accumulates float error. The two
    # square roots are taken with `decimal` at 50 digits. The mean/rms above are
    # left on their original float path deliberately, so the committed values do
    # not move: this block ADDS data, it does not restate the old numbers.
    _A = [F(int(A)) for _, A, _, _, _ in rows]
    _R = [F(str(r)) for *_, r in rows]
    _n = len(_A)
    _mA, _mR = sum(_A) / _n, sum(_R) / _n
    _sAA = sum((a - _mA) ** 2 for a in _A)
    _sRR = sum((r - _mR) ** 2 for r in _R)
    _sAR = sum((a - _mA) * (r - _mR) for a, r in zip(_A, _R))
    _r2 = _sAR * _sAR / (_sAA * _sRR)
    _slope = _sAR / _sAA
    _intercept = _mR - _slope * _mA
    _resid = sum((y - (_intercept + _slope * a)) ** 2 for a, y in zip(_A, _R))

    def _sq(fr):
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    pearson_r = float(_sq(_r2).sqrt())
    t_stat = float(_sq(_r2).sqrt() * Decimal(_n - 2).sqrt() / (Decimal(1) - _sq(_r2)).sqrt())
    rms_about_line = float((_sq(_resid) / _n).sqrt())
    ratio_at_A3 = float(_R[0])

    print(f"\n  TREND IN A (the ratio is NOT constant):")
    print(f"    Pearson r = {pearson_r:.3f}, t = {t_stat:.2f} on {_n-2} dof "
          f"(crit 2.447 ⇒ p < 0.05)")
    print(f"    slope = {float(_slope):+.5f} per unit A; "
          f"line: {float(_intercept + _slope*3):.3f} at A=3 → "
          f"{float(_intercept + _slope*39):.3f} at A=39")
    print(f"    rms about the line {rms_about_line:.4f} vs about the mean {rms_dev:.4f} "
          f"({100*(1-rms_about_line/rms_dev):.0f}% better)")
    print(f"    ⇒ quote the A you need: A=3 (³H/³He) is {ratio_at_A3:.3f}, NOT the mean "
          f"{mean_r:.3f}")
    print(f"\n  split/ΔE_C = {mean_r:.3f} ± {rms_dev:.3f}  (mean ± RMS scatter, {100*rms_dev/mean_r:.0f}%)")
    print(f"  ⇒ the split is PROPORTIONAL to Coulomb across A=3–39 (the {mean_r:.2f} factor is")
    print(f"    the known uniform-sphere over-estimate of ΔE_C). The ~{100*rms_dev/mean_r:.0f}% ratio")
    print(f"    scatter (plus the ~0.07 MeV Nolen–Schiffer anomaly) bounds the strong CSB.")

    # QOU consequence
    kernel_a3 = 2.271                          # #2089 pure-strong A=3 mirror split (#3564)
    split_a3 = rows[0][2]
    print("\n### QOU consequence — the strong kernel must be charge-symmetric")
    print(f"  The observed split is Coulomb (∝ ΔE_C, one shared radius, all A), so the")
    print(f"  strong/categorical kernel must NOT carry it. The #2089 pure-strong A=3 mirror")
    print(f"  split = {kernel_a3:.3f} MeV (#3564) is {kernel_a3/split_a3:.1f}× the whole observed")
    print(f"  A=3 split ({split_a3:.3f} MeV) — and the systematics shows charge symmetry is")
    print(f"  required at ALL A, not an A=3 accident. Any QOU strong kernel (#2089 f_bond,")
    print(f"  #3548 connected tr_M) must be charge-symmetric, Coulomb sourced separately.")
    print(f"  Scope-(a): constrains the kernel derivation, does not fit binding.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mirror-nuclei-coulomb-systematics", engine="mpmath")
            wb.set_description(
                "The mirror binding split is Coulomb across the isobaric chain ³H/³He…³⁹K/³⁹Ca: "
                "using the repo's canonical uniform-sphere Coulomb (Z(Z−1) self-energy, r₀=1.2 fm, "
                "coulomb_energy.mirror_displacement_mev — NO free parameter), the ratio "
                "split_AME/ΔE_C = %.2f ± %.2f across A=3–39 (the ~0.8 factor is the "
                "known uniform-sphere over-estimate). ⇒ the split is proportional to Coulomb, so "
                "any QOU strong kernel must be charge-symmetric (Coulomb separate); the #2089 "
                "kernel's 2.27 MeV A=3 strong split (#3564) is 3× the whole observed split, "
                "systematically. Scope-(a), no wiring. "
                "⚠ THE RATIO IS NOT CONSTANT (corrected 2026-08-25): this field said "
                "'≈constant across A=3–39'. It rises monotonically — Pearson r = %.3f, "
                "t = %.2f on 6 dof (p < 0.05), and a line beats the mean by "
                "%.0f%% in rms. The proportionality finding and the charge-symmetry "
                "consequence are unaffected; only the 'constant' characterisation was "
                "wrong. Consumers must say WHICH A: the A=3 (³H/³He) ratio is %.3f, not "
                "the chain mean %.2f."
                % (mean_r, rms_dev, pearson_r, t_stat,
                   100 * (1 - rms_about_line / rms_dev), ratio_at_A3, mean_r))
            wb.add_data("mirror_pairs", [
                {"pair": nm, "A": A, "split_AME": s, "coulomb_canonical": c, "ratio": r}
                for nm, A, s, c, r in rows])
            wb.add_data("ratio_mean", mean_r)
            wb.add_data("ratio_rms_scatter", rms_dev)
            wb.add_data("ratio_trend_in_A", {
                "pearson_r": pearson_r,
                "t_statistic": t_stat,
                "dof": _n - 2,
                "t_critical_p05": 2.447,
                "slope_per_A": float(_slope),
                "line_at_A3": float(_intercept + _slope * 3),
                "line_at_A39": float(_intercept + _slope * 39),
                "rms_about_line": rms_about_line,
                "rms_about_mean": rms_dev,
                "ratio_at_A3": ratio_at_A3,
                "note": ("The ratio is NOT constant in A; it rises monotonically. "
                         "A line describes the eight points better than their mean. "
                         "Quote the A you need, not ratio_mean."),
            })
            wb.add_assertion(
                name="mirror_split_proportional_to_canonical_coulomb_all_A",
                computed=str(int(rms_dev / mean_r < 0.15)), expected="1", tolerance=0,
                source=(f"split_AME/ΔE_C(canonical Z(Z−1), r₀=1.2) = {mean_r:.3f} ± {rms_dev:.3f} "
                        f"({100*rms_dev/mean_r:.0f}% spread) across 8 mirror pairs A=3–39 ⇒ the "
                        "split is proportional to Coulomb ⇒ the strong kernel must be charge-symmetric. "
                        f"The spread is a monotone TREND, not constant scatter (Pearson r = {pearson_r:.3f}); "
                        "the proportionality conclusion is unaffected."))
            wb.add_assertion(
                name="mirror_ratio_trends_monotonically_with_A",
                computed=str(int(t_stat > 2.447)), expected="1", tolerance=0,
                source=(f"Pearson r = {pearson_r:.3f} between split/ΔE_C and A over the 8 pairs; "
                        f"t = {t_stat:.2f} on 6 dof exceeds the 2.447 two-sided p=0.05 critical "
                        f"value, and a straight line has rms {rms_about_line:.4f} against the "
                        f"mean's {rms_dev:.4f}. Recorded so 'ratio_mean' is not consumed as if "
                        f"it applied at every A — at A=3 the ratio is {ratio_at_A3:.3f}."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
