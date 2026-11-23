#!/usr/bin/env python3
"""
allpairs_extrapolation_fidelity_probe — I predicted the all-pairs extrapolation was
a type-mix artefact. Measured, it is not. This records the negative and its reason.

Bean `qou-ge9f`, arc `bk-crossing-mass-binding` (`qou-brng`). Follows #6360, #6364.

## The conjecture under test, and whose it was

`log_ratio_binding_prototype` reports an all-pairs binding estimate as

    B_allpairs_est = E₀ · L · C(A,2)/(A−1)          L = log(tr_free/tr_atom)

i.e. it takes `L`, which is measured on the **chain** bond set, divides by the
chain's `A−1` bonds to get a mean per-bond log, and multiplies by `C(A,2)`.

After #6364 refreshed that producer's 68-day-stale witness, its all-pairs range
came out at **0.61–1.63×** of AME — the only range in the arc that straddles 1.
I flagged it as probably an artefact, on this reasoning: the extrapolation assumes
the chain's mean per-bond energy applies to all pairs, but the two bond sets have
very different type mixes. At `A = 6, N = Z` the chain is `(2 pp, 1 pn, 2 nn)`
while the complete graph is `(3 pp, 9 pn, 3 nn)`, and the per-bond energies differ
by a factor 1.85 (`ε_pp = 2.0507`, `ε_pn = 2.8332`, `ε_nn = 3.7978` MeV). A
mix-blind extrapolation across energies that spread by 85 % looked unsafe.

**It is safe, and the conjecture is refuted.** Measured against the true all-pairs
sum `C(Z,2)·ε_pp + Z·N·ε_pn + C(N,2)·ε_nn`, the extrapolation is accurate to
within 5 % on every nucleus, and exact on the deuteron.

## Why it survives — the reason is structural, not luck

`ε_pn` sits close to the arithmetic mean of `ε_pp` and `ε_nn`
(`(2.0507 + 3.7978)/2 = 2.9242` against `2.8332`, 3.1 % apart), so the mean
per-bond energy is nearly independent of the mix, and any reweighting between the
three types moves it very little.

That near-equality is itself structural rather than coincidental. The bond factors
satisfy `f_pn = (f_pp + f_nn)/2 + hδ/4` — `f_pn` is essentially the *arithmetic*
mean of the other two. The energies are `ε = −E₀ log f`, so comparing `ε_pn`
against `(ε_pp + ε_nn)/2` compares `log` of an arithmetic mean against the
arithmetic mean of `log`s. By Jensen (AM–GM) the first is the larger, so
`ε_pn ≤ (ε_pp + ε_nn)/2` **necessarily** — the sign of the 3.1 % gap is forced —
and the gap is small because `f_pp` and `f_nn` are within a factor 1.52 of each
other. The probe checks the inequality's direction rather than asserting it.

## What this does NOT rescue

The separate objection from #6346 stands untouched: the complete graph is **not
expressible** in the 3A braid word at all, because a single generator joins only
consecutive nucleons (`QOU.Mass.StrandLayoutForcesChain`). So the all-pairs number
is an arithmetically faithful evaluation of a bond set the word cannot write. The
extrapolation is sound; what it extrapolates *to* remains unrealised.

Scope **(a)**: a fidelity check on an arithmetic step, plus a refuted conjecture
of mine. Nothing is wired and no bond set is recommended.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin; `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50

NUCLEI = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
          ("6Li", 3, 3), ("7Li", 3, 4), ("7Be", 4, 3), ("12C", 6, 6),
          ("16O", 8, 8)]


def constants():
    from codata_constants import M_E_MEV as me
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    me = me if isinstance(me, mp.mpf) else mp.mpf(str(me))
    z = q0**3 / (q0**2 + 1)
    d = flavor_split_leading(q0)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    f = {"pp": z, "nn": z - h, "pn": z - h * (mp.mpf(1) / 2 - d / 4)}
    eps = {k: E0 * mp.log(1 / v) for k, v in f.items()}
    return q0, h, d, E0, f, eps


def mixes(Z: int, N: int):
    o = ["p"] * Z + ["n"] * N
    cb = ["pp" if a == b == "p" else ("nn" if a == b == "n" else "pn")
          for a, b in zip(o, o[1:])]
    chain = (cb.count("pp"), cb.count("pn"), cb.count("nn"))
    complete = (Z * (Z - 1) // 2, Z * N, N * (N - 1) // 2)
    return chain, complete


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0, h, d, E0, f, eps = constants()
    print("allpairs_extrapolation_fidelity_probe")
    print("=" * 78)
    print("Per-bond energies eps = E_0*log(1/f), derived (bean qou-vsqh, #6338):")
    for k in ("pp", "pn", "nn"):
        print(f"    f_{k} = {fmt(f[k], 12):>16}   eps_{k} = {fmt(eps[k], 12)} MeV")
    spread = eps["nn"] / eps["pp"]
    print(f"  energies spread by a factor {fmt(spread, 6)} -- which is why a")
    print("  mix-blind extrapolation looked unsafe.")
    print()

    print("THE TEST.  B_allpairs_est = E_0*L*C(A,2)/(A-1), with L measured on the")
    print("CHAIN, against the true all-pairs sum over the complete graph's own mix.")
    print(f"{'nucleus':>8} {'chain mix':>15} {'complete mix':>17} {'est':>11} "
          f"{'true':>11} {'est/true':>10}")
    worst = mp.mpf(0)
    for nm, Z, N in NUCLEI:
        A = Z + N
        cm, km = mixes(Z, N)
        L = cm[0] * mp.log(1 / f["pp"]) + cm[1] * mp.log(1 / f["pn"]) \
            + cm[2] * mp.log(1 / f["nn"])
        est = E0 * L * (A * (A - 1) // 2) / (A - 1)
        true = km[0] * eps["pp"] + km[1] * eps["pn"] + km[2] * eps["nn"]
        r = est / true
        worst = max(worst, abs(r - 1))
        print(f"{nm:>8} {str(cm):>15} {str(km):>17} {fmt(est, 7):>11} "
              f"{fmt(true, 7):>11} {fmt(r, 6):>10}")
    print()
    print(f"  worst deviation from 1: {fmt(worst * 100, 4)} %")
    refuted = worst < mp.mpf("0.10")
    print(f"  => my 'type-mix artefact' conjecture is "
          f"{'REFUTED' if refuted else 'SUPPORTED'} "
          f"(threshold: a mix artefact would have to exceed 10 %)")
    print()

    print("WHY IT SURVIVES — structural, not luck")
    am = (eps["pp"] + eps["nn"]) / 2
    gap = (am - eps["pn"]) / am
    print(f"  arithmetic mean of eps_pp, eps_nn = {fmt(am, 10)}")
    print(f"  eps_pn                            = {fmt(eps['pn'], 10)}")
    print(f"  gap                               = {fmt(gap * 100, 5)} %")
    print()
    print("  The bond factors satisfy f_pn = (f_pp + f_nn)/2 + h*delta/4, i.e. f_pn")
    print("  is essentially the ARITHMETIC mean of the other two.  Checked:")
    predicted_fpn = (f["pp"] + f["nn"]) / 2 + h * d / 4
    diff = abs(predicted_fpn - f["pn"])
    print(f"    (f_pp + f_nn)/2 + h*delta/4 = {fmt(predicted_fpn, 20)}")
    print(f"    f_pn                        = {fmt(f['pn'], 20)}")
    print(f"    |difference|                = {fmt(diff, 6)}")
    # Algebraically exact: (z + (z-h))/2 + h*d/4 = z - h/2 + h*d/4 = f_pn.  The
    # residual is rounding ORDER at 50 dps, not a real difference -- reporting a
    # bare `==` here would print False under two identical-looking numbers, which
    # is worse than useless.
    print(f"    exact to 1e-45: {diff < mp.mpf(10) ** -45}   "
          "(algebraically (z + (z-h))/2 + h*d/4 = z - h/2 + h*d/4 = f_pn;")
    print("     the residual is rounding order at 50 dps, not a difference)")
    print()
    print("  Since eps = -E_0*log f, comparing eps_pn against (eps_pp+eps_nn)/2")
    print("  compares log of an arithmetic mean against the arithmetic mean of")
    print("  logs.  By Jensen the first is larger, so eps_pn <= (eps_pp+eps_nn)/2")
    print("  NECESSARILY -- the sign of the gap is forced, not observed.  Checked")
    print(f"  rather than asserted: eps_pn <= mean is {eps['pn'] <= am}.")
    print(f"  The gap is SMALL because f_pp/f_nn = {fmt(f['pp']/f['nn'], 6)}, close")
    print("  to 1, and Jensen's gap vanishes as the arguments coincide.")
    print()

    print("WHAT THIS DOES NOT RESCUE")
    print("-" * 78)
    print("  The objection from #6346 stands untouched: the complete graph is NOT")
    print("  EXPRESSIBLE in the 3A braid word, because a single generator joins")
    print("  only consecutive nucleons (QOU.Mass.StrandLayoutForcesChain).  So the")
    print("  all-pairs number is an arithmetically faithful evaluation of a bond")
    print("  set the word cannot write.  The extrapolation is sound; what it")
    print("  extrapolates TO remains unrealised.")
    print()
    print("  So the 0.61-1.63x all-pairs range from #6364 is not an arithmetic")
    print("  artefact -- it is a real evaluation of a hypothetical bond set.  That")
    print("  makes it more interesting than I said, and no more realised.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
