#!/usr/bin/env python3
"""qbeta_d_frame_bar_even_normalisation_deadend_probe.py — normalising z_D to
bar-evenness LEAVES convention D. A dead end, recorded with its proof.

Bean `qou-cds1`.  Scope-(b): every statement is an exact symbolic identity.

## The route, and why it looks right

Under D the Q_beta ladder's eigenphase `2a = (z-1)h` is not bar-odd, because
`z_D` is not bar-even.  The obvious repair is to rescale: find the unique `a`
with `q^a z_D` bar-even and use that.  It exists and is FORCED, not chosen --

    bar(q^a z_D) / (q^a z_D) = q^(-2a-4)   =>   a = -2   uniquely

    z~_D  :=  z_D / q^2  =  q/(q^2+1)  =  1/[2]_q     (bar-even)

and it sits beside the C-frame parameter as the SAME functional form in a
different variable:

    z_C  =  sqrt(q)/(q+1)  =  1/[2]_sqrt(q)

which is the same shape as the (u;u)_m-vs-(q;q)_m confusion fixed in #6906.
Numerically z~_D = 0.49729 against z_C = 0.49932 -- 0.4 % apart, where the raw
z_D = 0.61269 is 23 % away.  So the C-built ladder nearly works under z~_D and
fails catastrophically under z_D, which is exactly the trap: the closeness is
NOT evidence, and is reported here only after the verdict.

## Why it is a dead end

`z_D`'s defining property in this framework is the FULL-BAR condition
`bar(z) = z - h` (`QOU.QBeta.zD_full_bar_covariant`), and
`QOU.QBeta.barEven_fullBar_forces_classical` proves a bar-even `z` cannot
satisfy it away from `q^2 = 1`.  Measured here: `z~_D` misses full-bar by
exactly `h`.  So rescaling to bar-evenness does not re-derive the ladder
WITHIN convention D -- it silently moves to a third parameter that is neither
`z_C` nor `z_D`.  `z_C` misses full-bar by exactly `h` too, which is the same
statement seen from the C side.

## What the corpus already had, and this independently reproduces

`QOU.QBeta.eigenphase_bar_defect_of_fullBar`: the defect is exactly `h^2`,
**independent of `z`** across the whole full-bar family -- so no choice inside
that family restores bar-oddness, and the derived D-frame eigenphase is
`a - h^2/4`, carrying no free parameter.  That is the live route; this probe
exists to close the rescaling alternative, not to compete with it.

## One thing worth recording on its own

The corpus states the bar law additively (`bar(z_D) = z_D - h`); deriving it
from scratch gives it multiplicatively (`bar(z_D) = q^-4 z_D`).  These look
like different conditions and are **the same identity** -- verified below.  A
reader meeting both could reasonably think two separate constraints were in
play.

## Precision

sympy exact symbolic throughout; the one numeric line is display only.  No
float64 in any claim.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import sympy as sp                                              # noqa: E402
import mpmath as mpm                                            # noqa: E402
from mpmath import mp                                           # noqa: E402

from q_parameter import q_at                                    # noqa: E402
from witness_base import WitnessBuilder                         # noqa: E402

mp.dps = 40
RESULTS: list[dict] = []


def record(name, passed, detail):
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(e.subs(q, 1 / q), force=True))
zD = q ** 3 / (q ** 2 + 1)
zC = sp.sqrt(q) / (q + 1)
h = q - 1 / q
a = sp.symbols("a", real=True)
expo = sp.simplify(sp.logcombine(sp.log(sp.simplify(bar(q ** a * zD) / (q ** a * zD))) / sp.log(q), force=True))
forced = sp.solve(sp.Eq(expo, 0), a)
zt = sp.simplify(q ** forced[0] * zD)

record(
    "bar_even_exponent_is_forced_not_chosen",
    forced == [-2] and sp.simplify(bar(zt) / zt) == 1,
    f"bar(q^a z_D)/(q^a z_D) = q^({expo}), so bar-evenness forces a = {forced[0]} "
    f"uniquely; z~_D = z_D/q^2 = {zt}, and bar(z~)/z~ = 1.",
)

record(
    "the_two_bar_laws_are_the_same_identity",
    sp.simplify(zD / q ** 4 - (zD - h)) == 0,
    "bar(z_D) = q^-4 z_D (multiplicative, as derived from scratch) and "
    "bar(z_D) = z_D - h (additive, as the corpus states it) differ by exactly "
    "0. They look like two conditions and are one. Worth recording because a "
    "reader meeting both forms could think two separate constraints apply.",
)

record(
    "z_C_and_z_tilde_D_are_the_same_form_in_different_variables",
    sp.simplify(zC - 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))) == 0
    and sp.simplify(zt - 1 / (q + 1 / q)) == 0,
    "z_C = 1/[2]_sqrt(q) and z~_D = z_D/q^2 = 1/[2]_q — the same functional "
    "form in q vs sqrt(q), structurally the same shape as the (u;u)_m vs "
    "(q;q)_m convention defect fixed in #6906.",
)

miss_zt = sp.simplify(bar(zt) - (zt - h))
miss_zC = sp.simplify(bar(zC) - (zC - h))
record(
    "bar_even_normalisation_LEAVES_convention_D",
    sp.simplify(miss_zt - h) == 0 and sp.simplify(miss_zC - h) == 0,
    f"z_D's defining property is the full-bar condition bar(z) = z - h "
    f"(zD_full_bar_covariant). z~_D misses it by exactly {miss_zt}, i.e. h — and "
    f"so does z_C. barEven_fullBar_forces_classical proves this is not an "
    f"accident: bar-even and full-bar are incompatible away from q^2 = 1. So "
    f"rescaling to bar-evenness does NOT re-derive the ladder within D; it "
    f"moves to a third parameter that is neither z_C nor z_D. THE ROUTE IS "
    f"CLOSED.",
)

defect = sp.simplify(bar((zD - 1) * h) + (zD - 1) * h)
record(
    "defect_is_exactly_h_squared_reproducing_the_corpus",
    sp.simplify(defect - h ** 2) == 0,
    "bar(2a) + 2a = h^2 exactly at z_D, independently reproducing "
    "QOU.QBeta.eigenphase_bar_defect_of_fullBar. Since the defect is "
    "z-independent across the full-bar family, no choice inside it restores "
    "bar-oddness — which is why the live route is the derived projection "
    "a - h^2/4, not a reparametrisation.",
)

q0 = q_at(40)
num = {n: mpm.nstr(mpm.mpf(str(sp.N(e.subs(q, sp.Float(str(q0), 40)), 40))), 18)
       for n, e in (("z_C", zC), ("z_D", zD), ("z_tilde_D", zt))}

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "can the D-frame ladder be repaired by rescaling z_D to bar-evenness?",
    "answer": "No. The rescaling exists and is forced (z_D/q^2 = 1/[2]_q), but a "
              "bar-even parameter cannot satisfy the full-bar condition that "
              "DEFINES convention D, so the route leaves D rather than re-deriving "
              "within it. The live route remains the derived projection a - h^2/4.",
    "scope": "(b) — exact symbolic identities. Closes one alternative; adjudicates "
             "nothing about the live route.",
    "numeric_at_proton_q0": num,
    "note_on_the_0_4_percent": "z~_D is 0.4% from z_C while raw z_D is 23% away, "
        "which is why the C-built ladder nearly works under z~_D. That closeness "
        "is NOT evidence and was not used: the verdict is the full-bar "
        "incompatibility, established independently of it.",
    "q0": mpm.nstr(q0, 20),
    "q0_pin": "proton (q_at)",
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python+sympy")
wp = _HERE.parent / "qbeta-d-frame-bar-even-normalisation-deadend.witness.json"
wp.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wp}\nallPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
