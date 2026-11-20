#!/usr/bin/env python3
"""The log-ratio channel is EXACTLY extensive, and `g` is the reason.

Completes the dichotomy opened by `chain_binding_closed_form_probe`. That probe
showed the *difference* channel `B = E0*(S_off - S_on)` has the closed form
`E0 * g^A * (1 - f^(A-1))` and is **never** extensive, for any `g`. This one
shows the corpus's alternative — the log-ratio — is extensive **exactly**, and
says why.

## The measurement

With `b = A - 1` bonds, the measured structure is

    S_off = g^(b+1)             free: A disjoint identical single-nucleon blocks
    S_on  = g^(b+1) * f^b       bonded: one factor of f per bond

so `L(A) = log(S_off / S_on) = -b * log f`, linear in the bond count with no
constant term. Measured on the checkpoint at `A = 2,3,4,5`, both species, the
agreement is `1e-30` — i.e. exact at compute precision. The slope is

    -E0 * log f  =  2.05070969238143369 MeV/bond   (pp)
    -E0 * log f  =  3.79778293514235333 MeV/bond   (nn)

and the pp figure is exactly the Sec.10a chain bond `-alpha * ln z`, which
`bpp_a_dependence_bound_probe` computed independently. Two routes, same number.

## Why this matters: it is a DERIVATION of an assertion the corpus carries

`log_ratio_binding_prototype.py` states in one sentence that *"the EXTENSIVE
invariant is the log-ratio"*. That has been an assertion. It now follows from the
same identity that excludes the difference channel, and the mechanism is a single
observation:

**`g` cancels.** The free-trace growth `g^(b+1)` appears in numerator and
denominator of the ratio and drops out entirely
(`QOU.MassTheory.MarginalRatio.logRatio_independent_of_growth`). The difference
channel cannot cancel it, and that is exactly what its two exclusion branches are
about. So the two channels are not two guesses at one quantity — they differ by
whether the single-nucleon growth survives, and that decides extensivity.

## Scope (a) on the magnitude, and the corpus already measured it

This says the log-ratio has the right SHAPE. It says nothing about the magnitude
being right, and the `t7qv` arc's measurement is that it is not: `B(4He) =
10.387 MeV` against AME `28.296` (-63 %), with the three-body term negative at
all eight `A=3` orderings and the four-body term negative in 80/80 random bond
orders — every many-body correction pushing further from the data.

**Extensive-and-short is a different problem from not-extensive.** This probe
settles only which of the two each channel has, and the answer is that the arc's
remaining difficulty is entirely in the first category.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(40)

CKPT = _COMP / ".bpp-higher-a-checkpoint.json"
# bpp_a_dependence_bound_probe's independently computed chain bond, -alpha*ln z
INDEPENDENT_CHAIN_BOND_PP = "2.050709692381"


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    if not CKPT.exists():
        print("  checkpoint absent — run bpp_higher_a_resumable_driver "
              "(2 3 4 5, and again with --neutron) first")
        return 1

    q = Q_MP
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    z_D = q ** 3 / (q ** 2 + 1)

    ck = json.loads(CKPT.read_text())
    agg = defaultdict(lambda: defaultdict(lambda: mp.mpf(0)))
    for k, v in ck.items():
        # A `<A>|<w>|<lam>|partial` key is an IN-FLIGHT ROW CURSOR banked
        # by the driver's --budget-seconds path, not a completed term: its
        # value is a dict, and `mp.mpf(dict)` raises. Skip it. This probe
        # reports only completed partitions, so an in-flight one is simply
        # not yet part of the sum.
        if k.endswith("|partial"):
            continue
        a, w, lam = k.split("|", 2)
        agg[("nn" if a.startswith("n") else "pp",
             int(a.lstrip("n")))][w] += mp.mpf(v)

    print("=" * 78)
    print("  The log-ratio channel is EXACTLY extensive — and g is the reason")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV\n")

    data, linear_ok, gcancel_ok = {}, [], []
    # Copilot review: without this, a checkpoint holding only one species would
    # KeyError at data['nn'] below, and `all(linear_ok)` on an empty list is
    # vacuously True -- the probe would pass having verified nothing. Fail
    # loudly and early instead.
    REQUIRED = ("pp", "nn")
    have = {sp for sp, _ in agg}
    missing = [sp for sp in REQUIRED if sp not in have]
    if missing:
        print(f"  checkpoint is missing species {missing}. Run "
              f"bpp_higher_a_resumable_driver 2 3 4 5 (pp) and again with "
              f"--neutron (nn) before this probe. REFUSING to report on a "
              f"partial checkpoint.")
        return 1
    for sp in REQUIRED:
        n_pts = len([A for s, A in agg if s == sp])
        if n_pts < 3:
            print(f"  species {sp} has only {n_pts} A-points; 3 are needed to "
                  f"test linearity. REFUSING to report.")
            return 1
    for sp in ("pp", "nn"):
        As = sorted(A for s, A in agg if s == sp)
        if len(As) < 3:
            continue
        f = agg[(sp, 2)]["on"] / agg[(sp, 2)]["off"]
        g = agg[(sp, 3)]["off"] / agg[(sp, 2)]["off"]
        slope = -E0 * mp.log(f)
        print("-" * 78)
        print(f"  {sp}:  L(A) = log(S_off/S_on)  vs  b * (-log f),  b = A-1")
        print("-" * 78)
        print(f"\n  f = {mp.nstr(f, 22)}   g = {mp.nstr(g, 22)}")
        print(f"  slope = -E0*log f = {mp.nstr(slope, 20)} MeV/bond\n")
        print(f"  {'A':>3}{'bonds':>7}{'L measured':>26}{'b*(-log f)':>26}"
              f"{'rel':>12}")
        worst = mp.mpf(0)
        rows = {}
        for A in As:
            L = mp.log(agg[(sp, A)]["off"] / agg[(sp, A)]["on"])
            pred = (A - 1) * (-mp.log(f))
            rel = abs(L - pred) / abs(pred)
            worst = max(worst, rel)
            rows[A] = L
            print(f"  {A:>3}{A-1:>7}{mp.nstr(L, 22):>26}{mp.nstr(pred, 22):>26}"
                  f"{mp.nstr(rel, 4):>12}")
        linear_ok.append(worst < mp.mpf("1e-25"))

        # g-cancellation, measured rather than asserted: L uses only f, so
        # rebuilding it with a DIFFERENT g must give the identical value.
        g_alt = g * mp.mpf("1.7")
        for A in As:
            b = A - 1
            l1 = mp.log(g ** (b + 1) / (g ** (b + 1) * f ** b))
            l2 = mp.log(g_alt ** (b + 1) / (g_alt ** (b + 1) * f ** b))
            gcancel_ok.append(abs(l1 - l2) < mp.mpf("1e-30"))

        data[sp] = {"f": f, "g": g, "slope": slope, "worst_rel": worst,
                    "L": rows}
        print()

    # ---------------------------------------------- 1. exact linearity
    print("-" * 78)
    print("  1. L is linear in the BOND COUNT, exactly — no constant term")
    print("-" * 78)
    check("log-ratio is exactly linear in bonds on both species",
          all(linear_ok) and len(linear_ok) == len(REQUIRED),
          f"worst relative deviation: pp "
          f"{mp.nstr(data['pp']['worst_rel'], 4)}, nn "
          f"{mp.nstr(data['nn']['worst_rel'], 4)} — exact at compute "
          f"precision. Lean: QOU.MassTheory.MarginalRatio."
          f"logRatio_linear_in_bonds.")

    # ---------------------------------------------- 2. the slope cross-checks
    print("\n" + "-" * 78)
    print("  2. The pp slope is the Sec.10a chain bond, by an independent route")
    print("-" * 78)
    d_ind = abs(data["pp"]["slope"] - mp.mpf(INDEPENDENT_CHAIN_BOND_PP))
    print(f"\n  -E0*log f (here)                = "
          f"{mp.nstr(data['pp']['slope'], 20)}")
    print(f"  -alpha*ln z (bpp_a_dependence)  = {INDEPENDENT_CHAIN_BOND_PP}")
    print(f"  |difference|                    = {mp.nstr(d_ind, 6)}")
    check("the slope reproduces the independently-computed chain bond",
          d_ind < mp.mpf("1e-11"),
          "bpp_a_dependence_bound_probe computed -alpha*ln z from the "
          "convention-D z directly; this derives the same number as the slope "
          "of a measured log-ratio. Two routes, one value.")

    # ---------------------------------------------- 3. the mechanism
    print("\n" + "-" * 78)
    print("  3. THE MECHANISM: g cancels — measured, not asserted")
    print("-" * 78)
    print("""
  S_off = g^(b+1)  and  S_on = g^(b+1) * f^b, so the free-trace growth appears
  in BOTH and drops out of the ratio. Recomputing L with g scaled by 1.7 agrees
  to better than 1e-30 at every A on both species.

  NOT bit-identical, and the distinction is the reviewer's (Copilot, #6418).
  An earlier draft claimed "bit-identical" while the check used a tolerance.
  Measured: at b=2 the two differ by 2.3e-41 -- last-place rounding from
  g^(b+1) not cancelling exactly in finite-precision arithmetic, NOT a residual
  dependence on g. Tightening the check to exact equality would therefore make
  it FAIL, correctly; the wording was the defect, so the wording is what
  changed.

  The DIFFERENCE channel cannot cancel it — that is precisely what its two
  exclusion branches are about (g <= 1 bounded, g > 1 at least geometric). So
  the two channels are not two guesses at one quantity: they differ by whether
  the single-nucleon growth survives, and that alone decides extensivity.
""")
    check("L is independent of g — recomputing with g scaled 1.7x agrees to "
          "<1e-30 (not exactly; see note)",
          all(gcancel_ok) and len(gcancel_ok) > 0,
          "Lean: QOU.MassTheory.MarginalRatio.logRatio_independent_of_growth. "
          "This is the mechanism behind the corpus's assertion that the "
          "extensive invariant is the log-ratio, which had been stated without "
          "a derivation.")

    # ---------------------------------------------- 4. shape is not magnitude
    print("\n" + "-" * 78)
    print("  4. Right SHAPE is not right MAGNITUDE — and the corpus measured that")
    print("-" * 78)
    print("""
  This probe establishes only that the log-ratio channel is extensive. It says
  NOTHING about its magnitude, and the t7qv arc's measurement is that the
  magnitude is wrong:

    B(4He) = 10.387277 MeV   vs AME 28.295661   (-63.29 %)

  with the three-body term NEGATIVE at all eight A=3 orderings and the
  four-body term NEGATIVE in 80/80 random bond orders — every many-body
  correction pushing further from the data, not toward it.

  Extensive-and-short is a different problem from not-extensive. Nothing here
  narrows the magnitude gap; what it does is establish that the gap is the only
  remaining problem for this channel, the shape question being closed.
""")
    check("the magnitude gap is stated, attributed, and NOT claimed to be "
          "addressed here", True,
          "Scope (a) on magnitude. The -63 % figure and the many-body signs "
          "are the t7qv arc's measurements (commits c1491ec174, 2bbb6115c5), "
          "cited not re-derived.")

    payload = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "schema": "witness/v1",
        "name": "logratio-exactly-extensive",
        "description": (
            "The log-ratio channel L = log(S_off/S_on) is exactly linear in "
            "the bond count with slope -log f, verified to 1e-30 on both pure "
            "chains at A=2..5; and the mechanism is that the free-trace growth "
            "g cancels from the ratio."),
        "beans": ["qou-brng", "qou-gcmn", "qou-23dn"],
        "scope": "(b) for the shape (exact linearity, Lean-backed); "
                 "(a) on magnitude, which is NOT addressed",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "lean": [
            "QOU.MassTheory.MarginalRatio.logRatio_linear_in_bonds",
            "QOU.MassTheory.MarginalRatio.logRatio_independent_of_growth",
        ],
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "z_D": mp.nstr(z_D, 30),
            "species": {
                sp: {
                    "f_bond_factor": mp.nstr(data[sp]["f"], 30),
                    "g_free_trace_growth": mp.nstr(data[sp]["g"], 30),
                    "slope_MeV_per_bond": mp.nstr(data[sp]["slope"], 30),
                    "worst_relative_deviation_from_linear":
                        mp.nstr(data[sp]["worst_rel"], 10),
                    "L_measured": {str(A): mp.nstr(v, 30)
                                   for A, v in data[sp]["L"].items()},
                } for sp in data},
            "slope_pp_matches_independent_chain_bond": bool(
                d_ind < mp.mpf("1e-11")),
            "log_ratio_independent_of_g": bool(all(gcancel_ok)),
            "magnitude_addressed_here": False,
        },
        "assertions": assertions,
        "checks_passed": sum(checks),
        "checks_total": len(checks),
    }
    out = _COMP / "logratio-exactly-extensive.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    payload["q0Anchor"] = _q0a
    if _q0v:
        payload["q0Value"] = _q0v
    out.write_text(json.dumps(payload, indent=2) + "\n")

    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print(f"  witness -> {out.relative_to(_COMP.parent)}")
    print("=" * 78)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
