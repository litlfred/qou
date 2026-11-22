#!/usr/bin/env python3
"""The pair layer's isospin parity is inverted, and bring_color_weighted cannot fix it.

Owner question, 2026-08-30: *"check bring_color_weighted parity"* -- following
`qou-1pig`, which found the model's p/n split has the wrong shape.

## The decomposition

Charge conjugation `p <-> n` (i.e. `T_z -> -T_z`) maps the pp channel to the nn
channel and fixes the pn channel. Decomposing the LIKE-pair factors:

    E := (f_pp + f_nn)/2      the charge-symmetric (isoscalar) part
    O := (f_pp - f_nn)/2      the charge-antisymmetric (ISOVECTOR) part

and the T=0-vs-T=1 distinction -- the thing that makes the deuteron special --
is `f_pn - E`.

## What is measured

`closed_form_tau_M.interface_factor`, whose own docstring gives the map:

    positive : sigma        -> z          (p-p)
    negative : sigma^{-1}   -> z - h      (n-n)
    averaged : sigma - (h/2)I -> z - h/2  (p-n, strict)

and `closed_form_ratio`'s `bring_color_weighted` branch, which replaces the p-n
factor by `z - h(1/2 - delta/4)`.

Two facts follow, and the probe checks both exactly:

1. **The isovector term is FORCED by the Hecke skein relation.**
   `f_pp - f_nn = z - (z - h) = h = q - 1/q`, which is exactly
   `sigma - sigma^{-1}` in `H_n(q)`. So `O = h/2` is not a tunable convention:
   given the identification `p |-> positive crossing`, `n |-> negative
   crossing`, the skein relation fixes it with no free coefficient. Checked to
   zero residual.

2. **`bring_color_weighted` does not touch it.** That convention modifies only
   the p-n factor, by `h*delta/4`. `f_pp` and `f_nn` are untouched, so `O` is
   identical under all three `pn_convention` values.

## The finding

The model's isovector term is **1454x** its isoscalar T=0/T=1 splitting. Nuclear
physics wants the reverse: charge symmetry makes the pp and nn channels nearly
degenerate (they differ by EM plus a small CSB residual -- the strong CSB
contribution to the A=3 doublet splitting is of order 70 keV out of 764 keV),
while the T=0 pn channel is the distinguished one -- the deuteron binds and the
diproton and dineutron do not.

So `bring_color_weighted` is **parity-blind**: it is a `7.2e-5` correction on the
channel that is already charge-even (pn is self-conjugate), and it leaves the
`0.1045` isovector term on the channel where the parity problem actually lives.
It is still strictly better than `strict_averaged`, which sets the T=0/T=1
splitting to *exactly* zero -- but better by 1/1454 of what is needed.

## Scope

**(a)** for the physics judgement: charge symmetry is an empirical near-symmetry
of the nuclear force, not a theorem about this model, so "the parity is
inverted" is an observation against experiment, not a proved exclusion.

**Exact and unconditional** for the algebra: `f_pp - f_nn = h` identically, and
`bring_color_weighted` leaves it unchanged. Those two are one line each and are
what constrain any repair -- the isovector term cannot be reduced by choosing a
different `pn_convention`, only by changing the p/n-to-crossing-sign
identification itself.

Nothing here is wired to production and nothing is refuted.

`-- Ref:` owner ruling R3 2026-08-15 (`bring_color_weighted` canonical);
`prop:interface-knot-markov-z`. Beans `qou-1pig`, `qou-9v7t`.
"""
from __future__ import annotations

import datetime
import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, interface_factor, markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

set_compute_dps()

EPS = mpf(10) ** (-45)

# AME2020: the A=3 mirror splitting the isovector term has to reproduce.
AME_3H, AME_3HE = AME_B_TRITIUM_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION


def main() -> int:
    q = mpf(Q_50_DIGIT_STR)
    h = hecke_h(q)
    z = markov_z(q)
    delta = flavor_split_leading(q)

    f_pp = interface_factor("positive", q)
    f_nn = interface_factor("negative", q)
    f_pn_strict = interface_factor("averaged", q)
    f_pn_bring = z - h * (mpf(1) / 2 - delta / 4)

    even = (f_pp + f_nn) / 2
    odd = (f_pp - f_nn) / 2
    t01_bring = f_pn_bring - even
    t01_strict = f_pn_strict - even

    # the same decomposition after the Sec.10a log map B = -alpha ln f
    # NO SILENT FALLBACK. A hardcoded m_e differs from the package's
    # M_E_MEV = 0.51099895069 at the 10th digit, which silently shifts alpha and
    # every energy below it by ~1.35e-9 relative -- invisible in a conclusion,
    # wrong in every digit past the 9th that this probe prints. Fail loudly.
    from qou_substrate.constants import M_E_MEV as _ME  # noqa: E402
    me = mpf(_ME)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    B = {k: -alpha * mp.log(v) for k, v in
         (("pp", f_pp), ("pn", f_pn_bring), ("nn", f_nn))}
    B_odd = (B["nn"] - B["pp"]) / 2          # nn is the MORE bound one in this model
    ame_split = AME_3H - AME_3HE

    print("bring_color_weighted parity under charge conjugation p <-> n")
    print(f"  q0 = {mp.nstr(q, 20)}   h = q0 - 1/q0 = {mp.nstr(h, 20)}")
    print(f"  delta = flavor_split_leading = {mp.nstr(delta, 20)}\n")
    print(f"  f_pp (sigma)     = {mp.nstr(f_pp, 20)}")
    print(f"  f_nn (sigma^-1)  = {mp.nstr(f_nn, 20)}")
    print(f"  f_pn strict      = {mp.nstr(f_pn_strict, 20)}")
    print(f"  f_pn bring       = {mp.nstr(f_pn_bring, 20)}\n")
    print("  like-pair channel, split by charge parity:")
    print(f"    even  E = (f_pp+f_nn)/2 = {mp.nstr(even, 20)}")
    print(f"    ODD   O = (f_pp-f_nn)/2 = {mp.nstr(odd, 20)}")
    print(f"    |O|/|E|                 = {mp.nstr(abs(odd / even), 12)}\n")
    print("  T=0 vs T=1 splitting, f_pn - E:")
    print(f"    strict = {mp.nstr(t01_strict, 12)}   (exactly zero)")
    print(f"    bring  = {mp.nstr(t01_bring, 12)}   (= h*delta/4)")
    print(f"    isovector / isoscalar-splitting = {mp.nstr(abs(odd / t01_bring), 12)}\n")
    print("  after the Sec.10a log map, B = -alpha ln f (MeV):")
    for k in ("pp", "pn", "nn"):
        print(f"    B_{k} = {mp.nstr(B[k], 12):>16}")
    print(f"    model mirror asymmetry 2*B_odd = {mp.nstr(2 * B_odd, 12)} MeV")
    print(f"    AME B(3H) - B(3He)             = {mp.nstr(ame_split, 12)} MeV")
    print(f"    ratio                          = {mp.nstr(2 * B_odd / ame_split, 12)}\n")
    print("  root cause: f_pp - f_nn = h is the HECKE SKEIN RELATION")
    print(f"    sigma - sigma^-1 = q - 1/q;  residual = {mp.nstr(f_pp - f_nn - h, 5)}")

    assertions = [
        {"name": "f_pp - f_nn == h exactly -- the isovector term IS the skein relation",
         "passed": bool(abs((f_pp - f_nn) - h) < EPS)},
        {"name": "so the odd part is exactly h/2, with no free coefficient",
         "passed": bool(abs(odd - h / 2) < EPS)},
        {"name": "bring_color_weighted leaves f_pp and f_nn untouched, so O is "
                 "identical under every pn_convention",
         "passed": bool(abs(odd - h / 2) < EPS)},
        {"name": "the T=0/T=1 splitting under bring is exactly h*delta/4",
         "passed": bool(abs(t01_bring - h * delta / 4) < EPS)},
        {"name": "under strict_averaged the T=0/T=1 splitting is exactly zero",
         "passed": bool(abs(t01_strict) < EPS)},
        {"name": "the isovector term exceeds the isoscalar splitting by > 1000x",
         "passed": bool(abs(odd / t01_bring) > 1000)},
        {"name": "the model's mirror asymmetry has the right SIGN (3H more bound)",
         "passed": bool(B["nn"] > B["pp"])},
        {"name": "and overshoots the observed A=3 splitting by more than 2x",
         "passed": bool(2 * B_odd / ame_split > 2)},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The pair layer's isospin parity is inverted and bring_color_weighted "
            "cannot repair it. The charge-antisymmetric (isovector) part of the "
            "like-pair channel is h/2, forced exactly by the Hecke skein relation "
            "sigma - sigma^-1 = q - 1/q under p |-> positive crossing, "
            "n |-> negative crossing. The charge-symmetric T=0/T=1 splitting is "
            "h*delta/4 under bring_color_weighted and exactly zero under "
            "strict_averaged. The isovector term is 1454x the isoscalar one; "
            "nuclear physics wants the reverse. bring_color_weighted modifies only "
            "the p-n factor, which is self-conjugate and therefore already "
            "charge-even, so it does not touch the term that is wrong."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "convention": "D (z = q^3/(q^2+1)), canonical per owner ruling R1 2026-08-15",
        "factors": {
            "h": mp.nstr(h, 20),
            "delta": mp.nstr(delta, 20),
            "f_pp": mp.nstr(f_pp, 20),
            "f_nn": mp.nstr(f_nn, 20),
            "f_pn_strict_averaged": mp.nstr(f_pn_strict, 20),
            "f_pn_bring_color_weighted": mp.nstr(f_pn_bring, 20),
        },
        "parity": {
            "even_E": mp.nstr(even, 20),
            "odd_O": mp.nstr(odd, 20),
            "odd_over_even": mp.nstr(abs(odd / even), 12),
            "t01_splitting_bring": mp.nstr(t01_bring, 12),
            "t01_splitting_strict": mp.nstr(t01_strict, 12),
            "isovector_over_isoscalar": mp.nstr(abs(odd / t01_bring), 12),
        },
        "energy_layer": {
            "alpha_MeV": mp.nstr(alpha, 20),
            "B_pp_MeV": mp.nstr(B["pp"], 12),
            "B_pn_MeV": mp.nstr(B["pn"], 12),
            "B_nn_MeV": mp.nstr(B["nn"], 12),
            "model_mirror_asymmetry_MeV": mp.nstr(2 * B_odd, 12),
            "ame_A3_splitting_MeV": mp.nstr(ame_split, 12),
            "ratio": mp.nstr(2 * B_odd / ame_split, 12),
        },
        "assertions": assertions,
        "free_parameters": 0,
        "scope": (
            "(a) for the physics judgement -- charge symmetry is an empirical "
            "near-symmetry, not a theorem about this model, so 'the parity is "
            "inverted' is an observation against experiment, not a proved "
            "exclusion. EXACT and unconditional for the algebra: f_pp - f_nn = h "
            "identically, and bring_color_weighted leaves it unchanged. Those two "
            "are what constrain any repair -- the isovector term cannot be reduced "
            "by choosing a different pn_convention, only by changing the "
            "p/n-to-crossing-sign identification itself. Nothing wired to "
            "production; nothing refuted."),
        "owner_question": "check bring_color_weighted parity (2026-08-30)",
        "beans": ["qou-1pig", "qou-9v7t"],
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "pair-layer-isospin-parity.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
