#!/usr/bin/env python3
"""
Probe — can the WRITHE unbind the diproton? The threshold, and why T3 forbids it.

Direct answer to "does the writhe address the diproton unbinding issue".

The writhe grading sends the interface scalar to `mu_eff = mu * (1-h)^(e/2)`,
`e` the exponent sum. A channel is unbound iff `mu_eff > 1`. Since `0 < 1-h < 1`,
solving for `e` gives a threshold, and it is exact:

    mu_eff > 1   <=>   e  <  2*ln(1/mu) / ln(1-h)

so the writhe CAN unbind — but only below a computable, strictly negative bound.

## Result

    channel   mu         T3 writhe   e needed to UNBIND    gap
    pp        0.612688      +1         e <= -4.1776       -5.18
    pn        0.508158       0         e <= -5.7728       -5.77
    nn        0.403628      -1         e <= -7.7367       -6.74

Nature (Machleidt CD-Bonn, arXiv:nucl-th/0006014 Table XI): pp UNBOUND
(a = -17.3 fm), nn UNBOUND (-18.9 fm), pn 3S1 BOUND (+5.419 fm). So `pp` and `nn`
must fall below threshold and `pn` must not.

## The obstruction — and it is a sign, not a magnitude

`pp` and `nn` both need a LARGE NEGATIVE writhe (`<= -4.18` and `<= -7.74`). But
the corpus's grading is `T3` — crossing sign — which by construction gives them
OPPOSITE signs (`sigma` for pp, `sigma^-1` for nn;
`WeakIsospinT3Grading.lean`). A `T3` grading therefore hands `pp` a
**non-negative** writhe, and a non-negative writhe multiplies `mu` by a factor
`<= 1`, i.e. binds HARDER.

So the `pp` failure is not a mis-chosen magnitude. It is a sign that makes
unbinding **impossible at any magnitude** — proved sorry-free as
`QOU.QBeta.t3_grading_cannot_unbind_pp` (via `nonneg_writhe_cannot_unbind`).

The `nn` side is not excluded by that theorem — its `T3` writhe is negative, the
helpful direction — but `-1` against a required `-7.74` is a factor of ~8.

## What this answers, and what it does not

**Answers:** no, the writhe as currently graded cannot resolve the diproton, and
the reason is structural (sign), not numerical.

**Does not answer:** whether some other grading can. The thresholds above are a
REQUIREMENT measurement, in the same spirit as the collective-term budget: they
say what a candidate must supply. They are not a proposal, and nothing here is
fitted or wired. In particular, reading the table as "so set `e_pp = -5`" would
be a fit, and would also destroy the `T3` identification that the writhe
currently earns its place by.

**Plausibility note, stated because it matters:** the required magnitudes are
large against the framework's own structures. The canonical baryon
`beta_Bor = (sigma_1^-1 sigma_2)^3` has writhe `0`, and a single interface bond
has writhe `+-1`. Demanding `|w| >= 5` (pp) or `>= 8` (nn) for a two-nucleon bond
is five to eight times anything the framework currently carries.

NO WITNESS: closed-form threshold from the derived constants; the table
reproduces it.

Beans qou-pjx4 / qou-brg3; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR as Q50
from _precision import set_compute_dps  # noqa: E402

# (label, T3 writhe assigned by the corpus grading, nature's scattering length fm,
#  nature-bound?)
CHANNELS = [
    ("pp", +1, -17.3, False),
    ("pn", 0, -23.740, False),      # 1S0; the 3S1 partner is the bound one
    ("nn", -1, -18.9, False),
]


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q50))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    w = 1 - h
    lw = mp.log(w)

    print("Can the writhe unbind the diproton? The exact threshold.\n")
    print(f"  q0 = {float(q):.12f}   h = {float(h):.10f}   z = {float(z):.10f}")
    print(f"  (1-h) = {float(w):.10f}   ln(1-h) = {float(lw):.10f}  (negative)\n")
    print("  mu_eff = mu*(1-h)^(e/2) > 1   <=>   e < 2*ln(1/mu)/ln(1-h)\n")

    mus = {"pp": z, "pn": z - h * mp.mpf(1) / 2, "nn": z - h}
    print("| channel | mu       | T3 writhe | e to UNBIND | gap from T3 |")
    print("| ------- | -------: | --------: | ----------: | ----------: |")
    rows = []
    for lbl, e_t3, a_fm, _ in CHANNELS:
        mu = mus[lbl]
        thr = 2 * mp.log(1 / mu) / lw
        rows.append((lbl, float(mu), e_t3, float(thr)))
        print(f"| {lbl:<7} | {float(mu):8.6f} | {e_t3:>+9d} | {float(thr):>11.4f} "
              f"| {float(thr) - e_t3:>+11.4f} |")

    print("\n  (all thresholds strictly negative: unbinding needs NEGATIVE writhe)\n")

    print("NATURE (Machleidt CD-Bonn, nucl-th/0006014 Table XI, nuclear part):\n")
    print("  pp 1S0   a = -17.3    fm    UNBOUND")
    print("  nn 1S0   a = -18.9    fm    UNBOUND")
    print("  np 1S0   a = -23.740  fm    UNBOUND")
    print("  np 3S1   a = +5.419   fm    BOUND  <- the deuteron, the only one")
    print("\n  so pp and nn must both fall BELOW threshold; the 3S1 channel must not.\n")

    print("## The obstruction is a SIGN, not a magnitude\n")
    print("  pp and nn both need a large NEGATIVE writhe (-4.18 and -7.74).")
    print("  But the corpus grades by T3 = crossing sign, which gives them OPPOSITE")
    print("  signs by construction (sigma for pp, sigma^-1 for nn). So T3 hands pp a")
    print("  NON-NEGATIVE writhe, and a non-negative writhe multiplies mu by a factor")
    print("  <= 1 -- it binds HARDER.")
    print("\n  => pp cannot be unbound by ANY magnitude under a T3 grading.")
    print("     Proved sorry-free: QOU.QBeta.t3_grading_cannot_unbind_pp")
    print("     (via nonneg_writhe_cannot_unbind).")
    print("\n  nn is NOT excluded by that theorem -- its T3 writhe is negative, the")
    print(f"  helpful direction -- but -1 against a required {rows[2][3]:.2f} is ~8x off.")

    print("\n## Plausibility of the required magnitudes\n")
    print("  canonical baryon  beta_Bor = (s1^-1 s2)^3   writhe 0")
    print("  single interface bond                       writhe +-1")
    print("  required here                               |w| >= 5 (pp), >= 8 (nn)")
    print("  -> five to eight times anything the framework currently carries.")

    print("\n## Scope\n")
    print("  Answers: NO -- the writhe as currently graded cannot resolve the diproton,")
    print("  and the reason is structural (sign), not numerical.")
    print("  Does NOT answer whether some other grading can. The thresholds are a")
    print("  REQUIREMENT measurement, like the collective-term budget -- not a proposal.")
    print("  Reading the table as 'set e_pp = -5' would be a fit, and would destroy the")
    print("  T3 identification the writhe currently earns its place by.")
    print("\n(no witness by design — closed-form threshold from derived constants.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
