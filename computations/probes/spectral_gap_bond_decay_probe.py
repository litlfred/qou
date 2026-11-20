#!/usr/bin/env python3
"""
spectral_gap_bond_decay_probe — the decay rate per bond type, taken from the
TRANSFER MATRIX SPECTRA rather than assumed: `pp` and `nn` decay at exactly
`1/q^2`, `pn` at `0.99986` -- i.e. like-nucleon bonds are SHORT-range and the
p-n bond is LONG-range. Parameter-free. It transforms `A = 3` (3He to
**+0.136 %**) and makes `A >= 6` worse.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Owner direction: *"Don't assume
scalar interactions or characteristic. you probably need to look at the spectral
values of the respective transfer matrices."*

## What was wrong with the previous attempt

`allpairs_distance_decay_probe` weighted a scalar `L_XY` by a scalar `r` and
solved for `r`. That is still scalar space, and it needed a fitted rate that
turned out inconsistent across isotopes (spread 0.118). The transfer matrices
have their own spectra, and in a transfer-matrix chain the correlation decay
**is** the spectral gap ratio `|lambda_2 / lambda_1|`. So the rate is not a
parameter to solve for -- each bond type already carries its own.

## The rates, and they are exact

`T(c,d) = [[c*h + d, c], [c, d]]` (appendix `tm-general-form`):

    bond      lambda_1          lambda_2           |l2/l1|
    pp        1.1099785828     -0.90091828396     0.81165375437
    nn       -1.1099785828      0.90091828396     0.81165375437
    pn        1.005520335      -1.0053765317      0.99985698623

`pp` is `sigma`, so its spectrum is `{q, -1/q}` by the Hecke quadratic and the
ratio is **exactly `1/q^2`**; `nn` is `sigma^-1` with the inverse spectrum, so
it is `1/q^2` as well (both verified to 45 digits below). `pn` is not a braid
generator and its ratio is a different number -- **and it is 1 to one part in
7000.**

**That is "the rate depends on the type of bond", derived rather than posited,
and it says something sharp: like-nucleon bonds are SHORT-range while the p-n
bond is essentially LONG-range.** The one bound two-nucleon channel is the
long-range one.

## Result, with NO free parameter

`B = alpha * sum_{i<j} L_{X_i X_j} * r_{X_i X_j}^{|i-j|-1}`, every `r` taken
from the table above:

    iso     blocked            alternating
            B_model   err %    B_model   err %
    2H       2.832825  +27.343  2.832825  +27.343
    3H       8.972151   +5.781  8.972151   +5.781
    3He      8.206831   +6.333  7.728538   **+0.136**
    4He     17.17817   -39.29  16.07744   -43.181
    6Li     41.93207   +31.06  38.11248   +19.124
    7Li     58.59518   +49.31  53.52792   +36.394

    mean |err|  26.5 %            22.0 %

**Mixed, and the split is structural rather than noisy:**

  * **`A = 3` improves sharply.** `3H` to `+5.78 %` and `3He` to `+0.136 %`
    (alternating) -- against production's chain, which is the `r -> 0` corner
    of this same family.
  * **`A >= 6` gets WORSE**, and the reason is the `pn` rate. At `r_pn ~ 1`
    every p-n pair contributes at full strength regardless of separation, so
    `B` grows like `Z*N` and overshoots: `+19 %` at `6Li`, `+36 %` at `7Li`.
  * **`2H` is untouched** (`+27.34 %`) -- at `A = 2` there is only one pair and
    no separation for a decay to act on. Consistent with the deuteron defect
    being in the bond itself, which `he4_exceeds_pairwise_maximum_probe`
    already located.
  * **`4He` remains far under** (`-39 %`/`-43 %`), the known super-pairwise
    excess. No pairwise weighting can reach it; that is proved elsewhere.

## 🛑 What is derived and what is still assumed

**Derived:** the *rates*. They are the spectral gaps of the framework's own
transfer matrices, exact for `pp`/`nn` (`1/q^2`), no fit anywhere.

**Assumed, and this is the load-bearing assumption:** the *form*
`weight ∝ r^{s-1}`. Reading the spectral gap as a per-separation weight is the
standard transfer-matrix correlation-decay identification, but the framework's
binding functional is `-alpha*log(tr_atom/tr_free)`, and nothing here derives
that a bond at separation `s` enters it with weight `r^{s-1}`. That step is a
model, not a theorem.

**Also assumed: the strand ORDERING.** Blocked and alternating differ
materially (mean 26.5 % vs 22.0 %), and `3He`'s `+0.136 %` appears under
alternating only -- under blocked it is `+6.33 %`. **I have no derivation of
which ordering is correct, so that single good number must not be quoted on its
own.** It is one isotope, in one of two orderings I tried.

## Scope

Scope **(a)**: a parameter-free measurement of an assumed functional form.
Nothing is wired, nothing fitted, and no rate is adjusted. AME is the
comparison target only.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import json  # noqa: E402

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -45

ISO = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
       ("6Li", 3, 3), ("7Li", 3, 4)]


def fmt(x, n=9):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q = Q_MP
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    al = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dx = flavor_split_leading(q)
    lw = mp.log(1 - h)
    w = mp.mpf(1) / 2 - dx / 4

    def L(d, e):
        return -mp.log(z + d) - e / 2 * lw

    Lb = {"pp": L(mp.mpf(0), mp.mpf(1)),
          "nn": L(-h, mp.mpf(-1)),
          "pn": L(-h * w, 2 * w - 1)}
    D = {"pp": mp.mpf(0), "nn": -h, "pn": -h * w}

    def spec(d):
        T = mp.matrix([[h + d, 1], [1, d]])
        tr = T[0, 0] + T[1, 1]
        dt = T[0, 0] * T[1, 1] - 1
        r = mp.sqrt(tr * tr - 4 * dt)
        e = [(tr + r) / 2, (tr - r) / 2]
        e.sort(key=lambda x: -abs(x))
        return e

    print("spectral_gap_bond_decay_probe")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}  h = {fmt(h)}  z = {fmt(z)}  alpha = {fmt(al)} MeV")
    print()
    print("THE RATES — the transfer matrix's OWN spectral gap, per bond type")
    print("-" * 78)
    print("  T(c,d) = [[c*h+d, c],[c, d]];  in a transfer-matrix chain the")
    print("  correlation decay IS |lambda_2 / lambda_1|.  Not a parameter.")
    print()
    print(f"{'bond':>5} {'lambda_1':>17} {'lambda_2':>17} {'|l2/l1|':>16}")
    R = {}
    for nm in ("pp", "pn", "nn"):
        e = spec(D[nm])
        R[nm] = abs(e[1]) / abs(e[0])
        print(f"{nm:>5} {fmt(e[0], 12):>17} {fmt(e[1], 12):>17} {fmt(R[nm], 12):>16}")
    print(f"\n  1/q^2 = {fmt(1 / q**2, 12)}")
    assert abs(R["pp"] - 1 / q**2) < TOL, "pp rate must be exactly 1/q^2"
    assert abs(R["nn"] - 1 / q**2) < TOL, "nn rate must be exactly 1/q^2"
    print("  pp and nn are EXACTLY 1/q^2 (sigma has spectrum {q,-1/q};")
    print("  sigma^-1 the inverse -- so both ratios are 1/q^2 identically).")
    print(f"  pn = {fmt(R['pn'], 12)}, i.e. 1 to one part in "
          f"{fmt(1 / (1 - R['pn']), 5)}.")
    assert R["pn"] > mp.mpf("0.999"), "pn must be near-unity (long range)"
    assert R["pp"] < mp.mpf("0.9"), "pp must be genuinely short range"
    print()
    print("  => LIKE-nucleon bonds are SHORT-range; the p-n bond is LONG-range.")
    print("     The one BOUND two-nucleon channel is the long-range one.")
    print()

    p = _Path(__file__).resolve().parent.parent / "data" / "ame2020.json"
    raw = json.loads(p.read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    AME = {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
           for r in rows if r.get("binding_energy_total_keV") is not None}

    def arr(Z, N, mode):
        if mode == "blocked":
            return ["p"] * Z + ["n"] * N
        s, pp, nn = [], Z, N
        while pp or nn:
            if pp:
                s.append("p")
                pp -= 1
            if nn:
                s.append("n")
                nn -= 1
        return s

    def B(Z, N, mode):
        s = arr(Z, N, mode)
        t = mp.mpf(0)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                k = s[i] + s[j]
                k = k if k in Lb else k[::-1]
                t += Lb[k] * (R[k] ** (j - i - 1))
        return al * t

    print("RESULT — no free parameter anywhere")
    print("-" * 78)
    means = {}
    for mode in ("blocked", "alternating"):
        print(f"\n  arrangement = {mode}")
        print(f"    {'iso':>5} {'B_model':>12} {'B_AME':>12} {'err %':>10}")
        errs = []
        for nm, Z, N in ISO:
            b, a = B(Z, N, mode), AME[(Z, Z + N)]
            e = (b / a - 1) * 100
            errs.append(abs(e))
            print(f"    {nm:>5} {fmt(b, 8):>12} {fmt(a, 8):>12} {fmt(e, 6):>10}")
        means[mode] = sum(errs) / len(errs)
        print(f"    mean |err| = {fmt(means[mode], 5)} %   "
              f"max = {fmt(max(errs), 5)} %")
    print()

    print("WHAT IMPROVED AND WHAT GOT WORSE — structural, not noise")
    print("-" * 78)
    e3he = (B(2, 1, "alternating") / AME[(2, 3)] - 1) * 100
    e2h = (B(1, 1, "blocked") / AME[(1, 2)] - 1) * 100
    e7li = (B(3, 4, "blocked") / AME[(3, 7)] - 1) * 100
    print(f"  A = 3 improves sharply: 3He to {fmt(e3he, 4)} % (alternating).")
    print(f"  A >= 6 gets WORSE ({fmt(e7li, 4)} % at 7Li) and the reason is the")
    print("    pn rate: at r_pn ~ 1 every p-n pair contributes at full strength")
    print("    regardless of separation, so B grows like Z*N and overshoots.")
    print(f"  2H is UNTOUCHED ({fmt(e2h, 5)} %) -- one pair, no separation for a")
    print("    decay to act on.  The deuteron defect is in the bond itself.")
    print("  4He stays far under: the known super-pairwise excess, which no")
    print("    pairwise weighting can reach (proved elsewhere).")
    assert abs(e2h) > 27 and abs(e2h) < 28, "2H must be unchanged at ~27.3 %"
    print()

    print("🛑 WHAT IS DERIVED AND WHAT IS STILL ASSUMED")
    print("-" * 78)
    print("  DERIVED: the RATES.  Spectral gaps of the framework's own transfer")
    print("    matrices, exact for pp/nn (1/q^2).  No fit anywhere.")
    print("  ASSUMED (load-bearing): the FORM, weight ~ r^(s-1).  Reading a")
    print("    spectral gap as a per-separation weight is the standard")
    print("    transfer-matrix identification, but nothing here derives that a")
    print("    bond at separation s enters -alpha*log(tr_atom/tr_free) that way.")
    print("    That step is a model, not a theorem.")
    print("  ASSUMED: the strand ORDERING.  blocked vs alternating differ")
    print(f"    materially ({fmt(means['blocked'], 4)} % vs "
          f"{fmt(means['alternating'], 4)} % mean), and 3He's +0.136 % appears")
    print("    under alternating ONLY (blocked gives +6.33 %).  I have no")
    print("    derivation of the ordering, so that one good number MUST NOT be")
    print("    quoted on its own -- one isotope, one of two orderings tried.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
