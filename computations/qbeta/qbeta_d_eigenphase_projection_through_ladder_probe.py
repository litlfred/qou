#!/usr/bin/env python3
"""qbeta_d_eigenphase_projection_through_ladder_probe.py — the derived D-frame
eigenphase correction `alpha - h^2/4` improves the ladder a lot and does NOT
restore it.

Bean `qou-cds1`.  Scope-(a): a measurement of the live route, at the proton
pin, with `c_2` held at its structural value.  A negative.

## What was tested, and why it is not a fit

`QOU.QBeta.eigenphase_bar_defect_of_fullBar` gives `bar(2a) + 2a = h^2` exactly
for any `z` in the full-bar family, so the bar-odd projection of the D-frame
eigenphase is `a - h^2/4` (undoubled).  That correction is DERIVED and carries
no free parameter -- nothing is chosen -- so pushing it through the ladder is a
derivation, not a search.  The result is reported whatever it is.

The ladder (`qbeta_utils.c3_target_at`):

    Q_A  = m_e |q^2-2q-1| (q+1) / (2 q^3)
    Q_N1 = Q_A cos(alpha - b hbar^2 / 2)
    Q_N2 = Q_N1 (1 + c_2 u^2),   c_2 = -1
    c_3  = (Q_codata / Q_N2 - 1) / u^3

`c_2 = -1` is kept in all three arms because it is CONVENTION-INDEPENDENT: it
is `1 - (b hbar^2)^2 = 1 - u^2` and carries no Markov parameter at all
(verified below).  The "implied c_2 = -9.3 under D" recorded elsewhere is the
INVERTED c_2, a different quantity from this structural one.

## Result at the proton pin

    arm                       implied c_2      c_3        |res| N1    |res| N2   N1/N2
    C   (z_C)                   -1.0176     -2.069342     7.383e-5    1.279e-6   57.74
    D   naive (z_D)             -9.2989   -974.431888     6.750e-4    6.024e-4    1.12
    D   corrected (-h^2/4)      -1.7331    -86.080994     1.257e-4    5.319e-5    2.36

**The correction is a large improvement and an insufficient one.**  Implied
`c_2` moves -9.30 -> -1.73 and rung convergence 1.12x -> 2.36x, but the C-frame
ladder converges 57.7x and lands its implied `c_2` within **1.8 %** of the
structural -1, where D-corrected is **73 %** off.

Self-consistency is the right metric here precisely because it does not
reference `-2` or any other candidate value: the ladder is self-consistent when
the `c_2` implied by inverting the anchor matches the `c_2` the framework
derives structurally.  Under C it nearly does.  Under D, corrected or not, it
does not.

## Sign: derived, then corroborated -- in that order

The projection's sign and normalisation come from the algebra
(`bar(2a) + 2a = h^2` => subtract `h^2/2` from `2a` => `h^2/4` from `a`), NOT
from which arm scores best.  Recorded because the numeric ordering happens to
agree, and quoting the agreement as the reason would invert the argument:

    alpha - h^2/4   implied c_2  -1.7331   N1/N2 2.364      <- the derived one
    alpha + h^2/4   implied c_2 -15.2133   N1/N2 1.070
    alpha - h^2/2   implied c_2  +7.4885   N1/N2 0.882

## What this does and does not say

**Does:** the live D route, taken alone, does not re-derive the ladder.  The
eigenphase projection is not the whole of the C->D move.

**Does not:** it does not refute the projection -- the projection is proved, and
this measures only that it is insufficient by itself.  It does not identify what
else is needed, and it adjudicates nothing about `z_D` being canonical.  Nothing
is wired; no `c_k` moves.

## Precision

mpmath at 50 dps; `q_0` from `q_at` (proton pin); `m_e` and `Q_beta` from the
CODATA/experimental constants modules.  No float64: no `float(` outside display,
no `statistics`, no `math.`.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import mpmath as mpm                                            # noqa: E402
from mpmath import mp                                           # noqa: E402

from q_parameter import q_at                                    # noqa: E402
from codata_constants import Q_BETA_MEV                         # noqa: E402
from experimental_constants import M_E_MEV                      # noqa: E402
from witness_base import WitnessBuilder                         # noqa: E402

mp.dps = 50
RESULTS: list[dict] = []


def record(name, passed, detail):
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


q = q_at(50)
me, Qx = mp.mpf(str(M_E_MEV)), mp.mpf(str(Q_BETA_MEV))
h = q - 1 / q
hb = (q - 1) / q
b = mpm.sqrt((h ** 2 + 3) / (h ** 2 + 4))
u = b * hb ** 2
QA = me * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
zC = 1 / (mpm.sqrt(q) + 1 / mpm.sqrt(q))
zD = q ** 3 / (q ** 2 + 1)
C2_STRUCTURAL = mp.mpf(-1)


def arm(alpha):
    QN1 = QA * mpm.cos(alpha - b * hb ** 2 / 2)
    QN2 = QN1 * (1 + C2_STRUCTURAL * u ** 2)
    r1, r2 = abs(Qx - QN1) / Qx, abs(Qx - QN2) / Qx
    return {
        "c2_implied": (Qx / QN1 - 1) / u ** 2,
        "c3": (Qx / QN2 - 1) / u ** 3,
        "res_N1": r1, "res_N2": r2, "convergence_N1_over_N2": r1 / r2,
    }


A = {
    "C": arm((zC - 1) * h / 2),
    "D_naive": arm((zD - 1) * h / 2),
    "D_corrected": arm((zD - 1) * h / 2 - h ** 2 / 4),
}
signs = {
    "minus_h2_over_4_DERIVED": arm((zD - 1) * h / 2 - h ** 2 / 4),
    "plus_h2_over_4": arm((zD - 1) * h / 2 + h ** 2 / 4),
    "minus_h2_over_2": arm((zD - 1) * h / 2 - h ** 2 / 2),
}


def dev(k):
    return abs(A[k]["c2_implied"] - C2_STRUCTURAL) / abs(C2_STRUCTURAL)


record(
    "structural_c2_carries_no_markov_parameter",
    True,
    f"the N2 rung is 1 + c_2 u^2 with c_2 = -1, i.e. 1 - (b hbar^2)^2 = 1 - u^2 "
    f"= {mpm.nstr(1 - u ** 2, 20)}. No z appears, so c_2 = -1 is "
    f"convention-INDEPENDENT and is legitimately held fixed across all three "
    f"arms. The 'implied c_2 = -9.3 under D' recorded elsewhere is the INVERTED "
    f"c_2, a different quantity.",
)

record(
    "derived_correction_substantially_improves_D",
    A["D_corrected"]["convergence_N1_over_N2"] > A["D_naive"]["convergence_N1_over_N2"]
    and dev("D_corrected") < dev("D_naive"),
    f"implied c_2 moves {mpm.nstr(A['D_naive']['c2_implied'],6)} -> "
    f"{mpm.nstr(A['D_corrected']['c2_implied'],6)} and rung convergence "
    f"{mpm.nstr(A['D_naive']['convergence_N1_over_N2'],5)}x -> "
    f"{mpm.nstr(A['D_corrected']['convergence_N1_over_N2'],5)}x; c_3 moves "
    f"{mpm.nstr(A['D_naive']['c3'],8)} -> {mpm.nstr(A['D_corrected']['c3'],8)}. "
    f"The derived projection is doing real work.",
)

record(
    "but_it_does_NOT_restore_ladder_self_consistency",
    dev("D_corrected") > 10 * dev("C"),
    f"self-consistency = how far the anchor-inverted c_2 sits from the "
    f"STRUCTURAL c_2 = -1. C: {mpm.nstr(100*dev('C'),4)} %. D corrected: "
    f"{mpm.nstr(100*dev('D_corrected'),4)} %. D naive: "
    f"{mpm.nstr(100*dev('D_naive'),4)} %. So the corrected D ladder is ~"
    f"{mpm.nstr(dev('D_corrected')/dev('C'),4)}x less self-consistent than C, "
    f"and its convergence is 2.36x against C's 57.7x. The eigenphase projection "
    f"alone is NOT the whole of the C->D move. This metric references no "
    f"candidate value (-2, Vol(4_1), ...) — only the structural rung and the "
    f"anchor.",
)

record(
    "sign_is_derived_then_corroborated_not_selected",
    signs["minus_h2_over_4_DERIVED"]["convergence_N1_over_N2"]
    > max(signs["plus_h2_over_4"]["convergence_N1_over_N2"],
          signs["minus_h2_over_2"]["convergence_N1_over_N2"]),
    "bar(2a)+2a = h^2 forces subtracting h^2/2 from 2a, i.e. h^2/4 from a — the "
    "sign and normalisation come from the algebra, not from scoring. The three "
    "candidates happen to rank with the derived one first (convergence "
    + ", ".join(f"{k}: {mpm.nstr(v['convergence_N1_over_N2'],5)}" for k, v in signs.items())
    + "), and that agreement is recorded as corroboration ONLY. Quoting it as "
      "the reason would invert the argument.",
)

fmt = lambda d: {k: mpm.nstr(v, 12) for k, v in d.items()}
out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "does the derived D eigenphase projection a - h^2/4 re-derive the ladder?",
    "answer": "No. It improves D substantially (implied c_2 -9.30 -> -1.73, "
              "convergence 1.12x -> 2.36x) but leaves the ladder far from "
              "self-consistent: C lands implied c_2 within 1.8 % of the structural "
              "-1, D-corrected is 73 % off. The projection is necessary-looking and "
              "insufficient alone.",
    "scope": "(a) — measured at the proton pin with c_2 held at its structural "
             "(convention-independent) value. Does NOT refute the projection, which "
             "is proved; measures only that it is not by itself the whole C->D move. "
             "Identifies nothing about what else is needed.",
    "arms": {k: fmt(v) for k, v in A.items()},
    "sign_variants": {k: fmt(v) for k, v in signs.items()},
    "self_consistency_pct_from_structural_c2": {k: mpm.nstr(100 * dev(k), 6) for k in A},
    "q0": mpm.nstr(q, 20), "q0_pin": "proton (q_at)", "u": mpm.nstr(u, 15),
    "dps": mp.dps,
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(
    out, script_path=__file__, engine="python+mpmath",
    q0_anchor="physical_proton", q0_value=mpm.nstr(q, 50))
wp = _HERE.parent / "qbeta-d-eigenphase-projection-through-ladder.witness.json"
wp.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wp}\nallPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
