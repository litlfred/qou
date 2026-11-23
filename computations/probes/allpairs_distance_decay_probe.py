#!/usr/bin/env python3
"""
allpairs_distance_decay_probe — the strand-routing cost is EXACTLY z^2 per unit
of separation (derived, 12-digit), but it cannot be the binding's distance
decay: read as interaction it makes distant pairs bind MORE, read as kinematics
it divides out. And the decay AME actually wants is not constant and is not
fast -- r* runs 0.709..0.827, falling monotonically with A.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Tests the owner's proposal that
the binding runs over ALL pairs, "highly concentrated on adjacent pairs but then
falls away quickly (rate depending on the type of bond)".

## Why this is the right shape to test

The framework's binding bracket has two endpoints, and a geometric distance
decay interpolates them exactly:

    B(r) = alpha * sum_{i<j} L_{X_i X_j} * r^{|i-j|-1}

    r -> 0   only adjacent pairs survive          = the CHAIN (A-1 bonds)
    r  = 1   every pair weighted equally          = the COMPLETE GRAPH

So this is not a new family; it is the *interior* of the bracket
`he4_exceeds_pairwise_maximum_probe` measured, and the separation `|i-j|` is not
an arbitrary metric -- it is the **far-commutation distance** of the braid,
`sigma_i` and `sigma_j` commuting exactly when `|i-j| >= 2`.

## Result 1 — the routing cost is exactly z^2, and it is DERIVED

`derived_bond_graph_binding.py` establishes that bonds far-commute
(`|3i-3j| >= 3`) and sit at Markov-removable positions, so the trace
**factorizes** over bonds with `f_bond = c*z + d`. That factorization carries
**no distance dependence at all** -- every wired bond contributes the same
factor, and the atom braid wires only the `A-1` chain.

So a decay would have to come from the cost of ROUTING a strand past the
intervening ones. Measured directly in `H_{s+2}`, forming the bond between
strands `1` and `1+s` as

    w_s = (sigma_1 ... sigma_{s-1}) * BOND * (sigma_{s-1} ... sigma_1)

    s   tr_M(w_s)         ratio to s-1
    1   0.612688037146    --
    2   0.229994898034    0.3753866309
    3   0.0863370098886   0.3753866309
    4   0.0324097592608   0.3753866309
    5   0.012166190336    0.3753866309

**Exactly `z^2 = 0.375386630862`, identical at every separation to 12 digits.**
Derived from the Markov trace, not chosen.

## 🛑 Result 2 — but z^2 cannot BE the binding decay, either way you read it

`B = -alpha*log(tr_atom/tr_free)`, so **more suppression means more binding**.
Then `L(s) = L + 2(s-1)*|log z|` *grows* with separation:
`L_pp(1) = 0.6072` becomes `L_pp(2) = 1.5870`.

  * Read as **interaction**: distant pairs bind MORE. Backwards.
  * Read as **kinematics** (overhead to bring the strands adjacent, not part of
    the coupling): it divides out and leaves NO distance dependence.

Neither reading produces a falloff. **So if the binding decays with distance,
the decay is not the routing cost** -- it is an independent weight the framework
does not currently supply.

## 🛑 Result 3 — and AME does not want ONE decay rate

Solving `B(r) = B_AME` per isotope. One `r`, five isotopes: heavily
over-determined and therefore falsifiable.

    iso    B(r=0) chain   B(r=1) all-pairs   AME        r*
    3H       6.139731       8.972556        8.481796   0.82675948
    3He      5.374411       8.207236        7.718041   0.82731205
    4He      8.681318      17.17979        28.29566    1.8149516   (> 1)
    6Li     14.52981       43.0409         31.99399    0.76942666
    7Li     17.83672       61.4601         39.24508    0.70896209

**No single `r` fits**: spread 0.118 over the four with a root in `[0,1]`, far
outside any plausible tolerance. `4He` needs `r = 1.81 > 1`, i.e. *outside the
family altogether* -- the same super-pairwise excess already proved in
`he4_exceeds_pairwise_maximum_probe`. Robust to the strand ordering: blocked
(`pp..nn..`) and alternating (`pnpn..`) give spreads 0.118 and 0.111.

**Two things the failure does say, and they are worth more than the fit:**

1. **The falloff AME wants is SLOW, not fast.** `r ~ 0.71..0.83` means a
   next-nearest pair carries ~80 % of an adjacent one. The proposal was
   "concentrated on adjacent, falls away quickly"; the data wants nearly the
   complete graph. And the derived routing rate `z^2 = 0.375` is ~2x too fast
   even before the inconsistency.
2. **`r*` is not scattered -- it falls monotonically with A** under BOTH
   orderings (blocked 0.8268, 0.8273, 0.7694, 0.7090; alternating 0.8268,
   0.8075, 0.7729, 0.7157). Scatter would not be monotone in A twice over, so
   `r*` tracks something real and A-dependent -- a sharper target than "the
   decay rate".

   **The A=3 mirrors agree to 0.07 % (`0.826759` vs `0.827312`) in the BLOCKED
   ordering ONLY.** Under alternating they are `0.826759` vs `0.807524`, 2.3 %
   apart. So that near-degeneracy is a property of the chosen strand order, not
   of the nuclei, and must not be quoted unscoped -- which is exactly how I
   first wrote it.

## Scope

Scope **(a)** for results 1 and 3 (measurements); result 2 is an argument from
the sign of `-log`, not an exclusion theorem. Nothing is wired, nothing fitted:
`r*` is *solved for* and reported as inconsistent, never adopted. AME is the
comparison target only.

NO FLOAT64: mpmath `mpf` at 40 dps, 50-digit proton pin, exact Hecke recursion.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import json  # noqa: E402

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 40
TOL = mp.mpf(10) ** -25

ISO = [("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4)]


def fmt(x, n=10):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    al = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dx = flavor_split_leading(q)
    lw = mp.log(1 - h)

    def L(d, e):
        return -mp.log(z + d) - e / 2 * lw

    Lpp = L(mp.mpf(0), mp.mpf(1))
    Lnn = L(-h, mp.mpf(-1))
    Lpn = L(-h * (mp.mpf(1) / 2 - dx / 4), 2 * (mp.mpf(1) / 2 - dx / 4) - 1)

    # ---- Hecke Markov trace, coset recursion ----
    def mul_gen(elt, i):
        out = {}
        for w, c in elt.items():
            v = list(w)
            v[i - 1], v[i] = v[i], v[i - 1]
            v = tuple(v)
            out[v] = out.get(v, mp.mpf(0)) + c
            if w[i - 1] > w[i]:
                out[w] = out.get(w, mp.mpf(0)) + c * h
        return {k: val for k, val in out.items() if val != 0}

    def t_word(word, n):
        e = {tuple(range(1, n + 1)): mp.mpf(1)}
        for i in word:
            e = mul_gen(e, i)
        return e

    memo = {}

    def tr_perm(w, n):
        if n == 1:
            return mp.mpf(1)
        key = (w, n)
        if key in memo:
            return memo[key]
        if w[n - 1] == n:
            r = tr_perm(w[:n - 1], n - 1)
        else:
            j = list(w).index(n)
            u = list(w)
            u.pop(j)
            r = tr_perm((tuple(u) + (n,))[:n - 1], n - 1) * (z ** ((n - 1) - j))
        memo[key] = r
        return r

    def trM(elt, n):
        return sum(c * tr_perm(w, n) for w, c in elt.items())

    print("allpairs_distance_decay_probe")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}  h = {fmt(h)}  z = {fmt(z)}  alpha = {fmt(al)} MeV")
    print()

    print("RESULT 1 — the routing cost is EXACTLY z^2 per unit of separation")
    print("-" * 78)
    print("  w_s = (sig_1..sig_{s-1}) * BOND * (sig_{s-1}..sig_1)  in H_{s+2}")
    print(f"\n{'s':>3} {'tr_M(w_s)':>20} {'ratio':>16} {'ratio/z^2':>12}")
    prev, ratios = None, []
    for s in range(1, 6):
        n = s + 2
        word = (list(range(1, s)) + [s] + list(range(s - 1, 0, -1))) if s > 1 else [1]
        t = trM(t_word(word, n), n)
        r = (t / prev) if prev is not None else None
        if r is not None:
            ratios.append(r)
        print(f"{s:>3} {fmt(t, 12):>20} {(fmt(r, 10) if r else '--'):>16} "
              f"{(fmt(r / z**2, 10) if r else '--'):>12}")
        prev = t
    for r in ratios:
        assert abs(r - z**2) < TOL, "the routing ratio must be exactly z^2"
    print(f"\n  every ratio equals z^2 = {fmt(z**2, 12)} to {len(ratios)} places tested")
    print("  DERIVED from the Markov trace, not chosen.")
    print()

    print("RESULT 2 — but z^2 cannot BE the binding decay, either reading")
    print("-" * 78)
    print("  B = -alpha*log(tr_atom/tr_free): MORE suppression = MORE binding.")
    print(f"  L_pp(s=1) = {fmt(Lpp, 7)}  ->  L_pp(s=2) = "
          f"{fmt(Lpp + 2 * abs(mp.log(z)), 7)}   (GROWS)")
    assert Lpp + 2 * abs(mp.log(z)) > Lpp, "routing must increase L"
    print("   * as INTERACTION: distant pairs bind MORE.  Backwards.")
    print("   * as KINEMATICS: it divides out; NO distance dependence.")
    print("  Neither gives a falloff, so the decay -- if real -- is NOT the")
    print("  routing cost, and the framework does not currently supply it.")
    print()

    p = _Path(__file__).resolve().parent.parent / "data" / "ame2020.json"
    raw = json.loads(p.read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    AME = {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
           for r in rows if r.get("binding_energy_total_keV") is not None}

    def arrangement(Z, N, mode):
        if mode == "blocked":
            return ["p"] * Z + ["n"] * N
        seq, pp, nn = [], Z, N
        while pp or nn:
            if pp:
                seq.append("p")
                pp -= 1
            if nn:
                seq.append("n")
                nn -= 1
        return seq

    def Bofr(Z, N, r, mode):
        s = arrangement(Z, N, mode)
        tot = mp.mpf(0)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                t = s[i] + s[j]
                Lb = Lpp if t == "pp" else (Lnn if t == "nn" else Lpn)
                tot += Lb * (r ** (j - i - 1))
        return al * tot

    print("RESULT 3 — and AME does not want ONE decay rate")
    print("-" * 78)
    print("  r -> 0 is the CHAIN, r = 1 the COMPLETE GRAPH; solve B(r) = B_AME.")
    spreads = {}
    for mode in ("blocked", "alternating"):
        print(f"\n  arrangement = {mode}")
        print(f"    {'iso':>5} {'chain':>11} {'all-pairs':>11} {'AME':>10} {'r*':>12}")
        good = []
        for nm, Z, N in ISO:
            ame = AME[(Z, Z + N)]
            b0, b1 = Bofr(Z, N, mp.mpf(0), mode), Bofr(Z, N, mp.mpf(1), mode)
            try:
                r = mp.findroot(lambda x: Bofr(Z, N, x, mode) - ame, mp.mpf("0.5"))
                rs = fmt(r, 8)
                if 0 <= r <= 1:
                    good.append((nm, r))
            except Exception:
                r, rs = None, "no root"
            print(f"    {nm:>5} {fmt(b0, 7):>11} {fmt(b1, 7):>11} "
                  f"{fmt(ame, 7):>10} {rs:>12}"
                  + ("   > 1, OUTSIDE the family" if r is not None and r > 1 else ""))
        vals = [v for _n, v in good]
        sp = max(vals) - min(vals)
        spreads[mode] = sp
        print(f"    r* in [0,1]: {[fmt(v, 6) for v in vals]}")
        print(f"    spread = {fmt(sp, 4)}   one r fits all? {sp < mp.mpf('0.02')}")
        assert sp > mp.mpf("0.05"), "the spread must refute a single r"
    print()
    print("  REFUTED: no single r, under either strand ordering "
          f"(spreads {fmt(spreads['blocked'], 4)}, "
          f"{fmt(spreads['alternating'], 4)}).")
    print()

    print("WHAT THE FAILURE DOES SAY — worth more than the fit would have been")
    print("-" * 78)
    print("  1. The falloff AME wants is SLOW, not fast.  r ~ 0.71..0.83 means a")
    print("     next-nearest pair carries ~80 % of an adjacent one -- nearly the")
    print(f"     complete graph.  The DERIVED routing rate z^2 = {fmt(z**2, 6)} is")
    print("     ~2x too fast even before the inconsistency.")
    print("  2. r* is NOT scattered: it falls monotonically with A under BOTH")
    print("     orderings.  Scatter would not be monotone in A twice over, so")
    print("     r* tracks something real and A-dependent -- a sharper target")
    print("     than 'the decay rate'.")
    print("     CAVEAT, scoped: the A=3 mirrors agree to 0.07 % (0.826759 vs")
    print("     0.827312) in the BLOCKED ordering ONLY; alternating gives")
    print("     0.826759 vs 0.807524, 2.3 % apart.  That near-degeneracy is a")
    print("     property of the strand order, NOT of the nuclei.")
    print()
    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT that all-pairs binding is refuted -- only that a SINGLE")
    print("    geometric decay rate is, and that z^2 is not the carrier.")
    print("  * NOT a fit: r* is solved for and reported inconsistent, never")
    print("    adopted.  Nothing is wired.")
    print("  * Result 2 is an argument from the sign of -log, not a theorem.")
    print("  * 4He needing r > 1 is the SAME super-pairwise excess already")
    print("    measured; this adds no new information about it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
