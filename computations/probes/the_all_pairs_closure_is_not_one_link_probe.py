#!/usr/bin/env python3
"""The all-pairs closure is not one link: the band generators do not commute
with the adjacent bonds they span, so the bond MULTISET does not determine a
braid word, a trace, or a link. At `A = 3` six bond orderings give three
distinct Markov traces and three distinct Jones polynomials; at `A = 4` forty
random orderings give thirty-three distinct traces spanning `0.992` in `L`,
which is `4.15 MeV`, or `15 %` of helium-4's binding energy.

WHERE THIS SITS
---------------
`the_canonical_mass_trace_factorises_over_the_chain_probe` (bean `qou-m3sh`)
proved the canonical CHAIN closure is a linear connected sum, so its Markov
trace is a product and its `L` an exact sum of interface terms. It carries no
many-body binding by theorem. The arc's cumulants therefore had to live
somewhere else, and the only candidate on the table was the ALL-PAIRS bond
model, whose band-routed bonds interleave generators across blocks. Bean
`qou-bygw` asked which prime closure that model produces.

This probe answers a prior question the bean assumed away: **the all-pairs
model does not produce a closure at all.** It produces one per bond ordering,
and they are different links.

THE MECHANISM
-------------
A bond between adjacent blocks `k, k+1` is the single generator `sigma_{3k+2}`.
A bond between distant blocks `i < j` is the BKL band generator

    band(i,j) = (sigma_{b-1} ... sigma_{a+1}) (sigma_a + d) (sigma_{a+1} ... sigma_{b-1})^-1,
    a = 3i+2,  b = 3j,

which spans every generator from `a` to `b-1`. For `i, j = 0, 2` that is
generators `2, 3, 4, 5` — and generator `2` is the `01` adjacent bond while
generator `5` is the `12` adjacent bond. The band therefore fails to commute
with BOTH adjacent bonds it reaches over. The chain has no bands, every bond
is a lone generator two apart from the next, and everything commutes; that is
the same fact that makes the chain a connected sum.

MEASURED, AT 200 BITS (exact engine, `q` from `Q_50_DIGIT_STR`)
---------------------------------------------------------------
§1  The control and the effect, same machinery, one bond different:

      chain defect   L_chain - (L_01 + L_12)   ~ 1e-60   (zero: connected sum)
      all-pairs c_3  L_all   - sum of pairs    ~ -0.34   (60 orders of magnitude up)

    So `c_3 != 0` and, by the contrapositive of the connected-sum theorem, the
    all-pairs closure is not a connected sum along its bonds. That much the
    bean expected.

§2  What it did not expect. The six orderings of the three bonds give

      four orderings (band first or last)   L = 2.017810478620   (3H)
      a01 . band . a12                      L = 1.911851878916
      a12 . band . a01                      L = 2.094298399424

    with IDENTICAL letter multiset, exponent sum (`12` on the `sigma` branch,
    `-4` on `sigma^-1`) and strand count, so the Markov normalisation is
    identical and the traces are comparable as invariants. Resolving each
    letter to a crossing and taking the Jones polynomial of the closure gives
    **three distinct Jones polynomials, matching the three traces one for
    one**, on both classical branches. Different Jones means different links.

§3  A SECOND, independent ambiguity: which nucleons are adjacent. The
    production word groups all protons and then all neutrons, `p^Z n^N` —
    read off the interface letters of `atom_canonical_crossings`, which are
    `(pp, pn)` for `3He`, `(pn, nn)` for `3H`, `(pp, pn, nn)` for `4He`. That
    is exactly what the closed form `(Z-1)L_pp + L_pn + (N-1)L_nn` encodes:
    one `pn` interface. The corpus's saturation and ceiling probes hardcode
    `["p","n","p"]` for `3He`, which has the SAME bond multiset `{pp, pn, pn}`
    but makes the FAR bond `pp` instead of `pn`, and is worth `0.070` in `L`:

      3He canonical `ppn`  L_allpairs = 1.607030797631
      3He probes'   `pnp`  L_allpairs = 1.676935518146   <- the published value
      3H  canonical `pnn`  L_allpairs = 2.017810478620   <- the published value

    so `3H` is canonical and `3He` is not. All are reproduced here from the
    exact engine: this is a reconciliation, not an accusation. No number was
    wrong; they answer different questions, and nothing had flagged that they
    were different questions.

§4  At `A = 4` the ambiguity is no longer a detail. Six bonds, `720` orderings;
    forty sampled give thirty-three distinct values of `L` (deduplicated at 40
    decimal digits — the 200-bit working precision is ~60 digits, and comparing
    at full precision inflates the count to 37 on last-bit noise), spanning

      L in [1.921376, 2.913802],  spread 0.992426
      x alpha = 4.185981 MeV  ->  4.154 MeV  =  14.7 % of B_AME(4He) = 28.2957

    The choice of bond ordering is worth more than the entire many-body
    cumulant it is supposed to measure.

§5  At `A = 2` there is no ordering and no arrangement to choose — one bond,
    one word — and the model is falsified without any convention in play:

      2He (pp)  L = 0.489899  B = 2.0507 MeV   reality: UNBOUND (diproton)
      2H  (pn)  L = 0.676822  B = 2.8332 MeV   reality: BOUND, 2.22452 MeV
      2n  (nn)  L = 0.907263  B = 3.7978 MeV   reality: UNBOUND (dineutron)

    The model ranks `nn > pn > pp`; reality binds only `pn`. The sibling's
    charge term `-(e/2) log(1-h)` adds `+0.1173 e`, which raises `pp` and `pn`
    and leaves `nn` alone, so it deepens the inversion rather than repairing
    it. The honest caveat is that this arc's `L` carries no spin, and the real
    distinction is a spin one — the deuteron binds in the triplet channel and
    every `1S0` two-body system is unbound — so a spinless bond constant cannot
    be expected to separate them. What it can be expected not to do is rank the
    unbound `nn` system above the bound `pn` one, and it does.

WHAT THIS MEANS FOR THE BINDING GAP
-----------------------------------
The bean's question — which prime closure carries the cumulants — is not yet
well posed. The all-pairs bond model specifies a bond MULTISET; a link needs a
WORD. Because the bands do not commute with the bonds they span, those are not
the same datum, and the difference is 15 % of helium-4 at `A = 4`. Any
many-body cumulant quoted from this model is a cumulant of a particular
ordering, and the ordering is currently an accident of loop order in the code
rather than a modelling decision.

Three ways out, none of them taken here:
  * name a canonical ordering and defend it physically;
  * symmetrise over orderings, which is a choice and not a derivation, and
    which does not obviously close under the Markov trace;
  * abandon the braid-word presentation for one where simultaneous bonding is
    representable, since a set of pairwise bonds applied "at once" is not a
    braid word at all.

WHAT IS NOT CLAIMED
-------------------
Not that no prime closure carries the cumulants — only that this model does not
name one. Not that the cumulants are meaningless: they are well defined once an
ordering is fixed, and `c_3 = -0.34` is the production convention's value. Not
that any published number is wrong. Nothing about which ordering is right, and
nothing connecting any of this to binding beyond the `alpha` conversion, which
is quoted for scale only. `A = 4` is sampled, not enumerated.
"""
from __future__ import annotations

import itertools
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402
import importlib.util  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "tc", HERE / "total_curvature_is_the_computable_half_probe.py")
tc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tc)

ALPHA = mpfr(str(M_E_MEV)) / (E.Q * (E.Q - 1))
B_AME_4HE = mpfr("28.2957")
# the corpus's two published A=3 all-pairs values (all_pairs_bonds_and_saturation_probe,
# quoted in pairwise_ceiling_is_overstated_probe as MEASURED_L)
CORPUS = {"3H": ("pnn", "2.017810478620"), "3He": ("pnp", "1.676935518146")}


def fmt(x, k=18):
    m, e, _ = gmpy2.digits(x, 10, k)
    s = "-" if m.startswith("-") else ""
    m = m.lstrip("-")
    return f"{s}{m[0]}.{m[1:]}e{e - 1}"


def blocks_of(order):
    return [E.nucleon_word(E.B_P if c == "p" else E.B_N, 3 * k, 3 * k + 1)
            for k, c in enumerate(order)]


def bond_word(order, i, j):
    d = E.bond_d(order[i], order[j])
    return [(1, d, 3 * i + 2)] if j == i + 1 else E.band(i, j, d)


def chain_word(order):
    """Adjacent bonds only, interleaved — the connected-sum closure."""
    w = []
    for k in range(len(order)):
        w += blocks_of(order)[k]
        if k > 0:
            w += [(1, E.bond_d(order[k - 1], order[k]), 3 * (k - 1) + 2)]
    return w


def crossing_sign(d, avg):
    """sigma (d = 0) -> +1, sigma^-1 (d = -h) -> -1, any mixture -> the branch."""
    if d == 0:
        return 1
    if d == -E.H:
        return -1
    return avg


def braid(word, avg):
    return [(g, crossing_sign(d, avg)) for (_c, d, g) in word]


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR; alpha = {float(ALPHA):.6f} MeV")

    print("\n" + "=" * 74)
    print("§1  THE CONTROL AND THE EFFECT: chain defect ~ 0, all-pairs c_3 ~ -0.34")
    print("=" * 74)
    c3 = {}
    chain_defect = {}
    for order, name in (("ppn", "3He"), ("pnn", "3H")):
        n = 3 * len(order)
        free = E.trM(n, E.word(order, set()))
        Lp = {pr: gmpy2.log(free / E.trM(n, E.word(order, set(pr))))
              for pr in ((0, 1), (1, 2), (0, 2))}
        Lall = gmpy2.log(free / E.trM(n, E.word(order, {0, 1, 2})))
        Lch = gmpy2.log(free / E.trM(n, chain_word(order)))
        c3[name] = Lall - sum(Lp.values())
        chain_defect[name] = Lch - (Lp[(0, 1)] + Lp[(1, 2)])
        print(f"  {name} (order {order}, n={n})")
        for pr in ((0, 1), (1, 2), (0, 2)):
            print(f"      L{pr} = {fmt(Lp[pr], 20)}")
        print(f"      sum of pairs   = {fmt(sum(Lp.values()), 20)}")
        print(f"      L_allpairs     = {fmt(Lall, 20)}")
        print(f"      c_3            = {fmt(c3[name], 20)}")
        print(f"      L_chain        = {fmt(Lch, 20)}")
        print(f"      CHAIN DEFECT   = {fmt(chain_defect[name], 8)}   (must be ~1e-59)")
    check("the chain is exactly additive — defect below 1e-55, so it IS a connected sum",
          all(abs(v) < mpfr("1e-55") for v in chain_defect.values()))
    check("the all-pairs c_3 is nonzero by 59 orders of magnitude, so that closure is NOT "
          "a connected sum along its bonds",
          all(abs(v) > mpfr("0.3") for v in c3.values()))

    print("\n" + "=" * 74)
    print("§2  THE BOND MULTISET DOES NOT DETERMINE A LINK")
    print("=" * 74)
    n = 9
    order = "pnn"
    blk = blocks_of(order)
    base = blk[0] + blk[1] + blk[2]
    free = E.trM(n, base)
    bonds = {"a01": bond_word(order, 0, 1), "a12": bond_word(order, 1, 2),
             "b02": bond_word(order, 0, 2)}
    print(f"  3H, order {order}: six orderings of {{a01, a12, b02}} appended after the blocks")
    trace_of, jones_of, esum_of = {}, {}, {}
    for perm in itertools.permutations(("a01", "a12", "b02")):
        w = base[:]
        for p in perm:
            w += bonds[p]
        trace_of[perm] = gmpy2.log(free / E.trM(n, w))
        bw = braid(w, 1)
        esum_of[perm] = sum(s for _g, s in bw)
        jones_of[perm] = tuple(sorted(tc.jones_closure(n, bw).items()))
        print(f"    {' '.join(perm):16s} L = {fmt(trace_of[perm], 15)}   exp-sum {esum_of[perm]}")
    nL = len({fmt(v, 40) for v in trace_of.values()})
    nV = len(set(jones_of.values()))
    print(f"\n    distinct L values          : {nL}")
    print(f"    distinct Jones polynomials : {nV}   (sigma branch)")
    print(f"    exponent sums              : {sorted(set(esum_of.values()))}  (identical, so the")
    print(f"                                 Markov normalisation is the same for all six)")
    check("the six bond orderings give exactly three distinct Markov traces", nL == 3)
    check("they give exactly three distinct Jones polynomials, one per trace — so the "
          "orderings close to at least three DIFFERENT LINKS", nV == 3 and nL == nV)
    nV_inv = len({tuple(sorted(tc.jones_closure(
        n, braid(base + bonds[p[0]] + bonds[p[1]] + bonds[p[2]], -1)).items()))
        for p in itertools.permutations(("a01", "a12", "b02"))})
    print(f"    distinct Jones polynomials : {nV_inv}   (sigma^-1 branch)")
    check("the same three-way split appears on the sigma^-1 branch", nV_inv == 3)
    grouped = {}
    for perm, L in trace_of.items():
        grouped.setdefault(fmt(L, 40), []).append(perm)
    for L, perms in grouped.items():
        where = "band at an end" if len(perms) == 4 else "band in the middle"
        print(f"    L = {L[:18]}  <- {len(perms)} ordering(s), {where}")
    check("the four orderings with the band first or last agree; only a band BETWEEN the "
          "two adjacent bonds moves the answer",
          max(len(v) for v in grouped.values()) == 4)

    print("\n" + "=" * 74)
    print("§3  A SECOND AMBIGUITY: WHICH NUCLEONS ARE ADJACENT")
    print("=" * 74)
    from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
    kind_to_bond = {"sigma": "pp", "sigma_inv": "nn", "averaged_weighted": "pn",
                    "averaged": "pn"}
    print("  production interface letters (atom_canonical_crossings), i.e. the arrangement:")
    arrangement_ok = True
    for Z, N, nm in ((2, 1, "3He"), (1, 2, "3H"), (2, 2, "4He")):
        ifs = [kind_to_bond[k] for g, k in atom_canonical_crossings(Z, N) if g % 3 == 2]
        expect = ["pp"] * (Z - 1) + ["pn"] + ["nn"] * (N - 1)
        arrangement_ok &= (ifs == expect)
        print(f"    {nm:4s} (Z={Z},N={N}): {ifs}   == p^Z n^N -> {expect}   {ifs == expect}")
    check("the production word groups all protons then all neutrons, p^Z n^N — exactly one "
          "pn interface, which is what (Z-1)L_pp + L_pn + (N-1)L_nn encodes", arrangement_ok)

    ok_corpus = True
    print("\n  the published A=3 all-pairs values, at their own arrangements:")
    for name, (ordr, val) in CORPUS.items():
        b = blocks_of(ordr)
        bs = b[0] + b[1] + b[2]
        fr = E.trM(9, bs)
        w = bs + bond_word(ordr, 0, 1) + bond_word(ordr, 1, 2) + bond_word(ordr, 0, 2)
        L = gmpy2.log(fr / E.trM(9, w))
        agree = abs(L - mpfr(val)) < mpfr("1e-11")
        ok_corpus &= agree
        canon = "p" * ordr.count("p") + "n" * ordr.count("n")
        print(f"    {name:4s} order {ordr}  L = {fmt(L, 15)}   corpus {val}   "
              f"|diff| {float(abs(L - mpfr(val))):.1e}   canonical? {ordr == canon}")
    check("both published A=3 all-pairs values are reproduced exactly at their own "
          "arrangements", ok_corpus)

    bc = blocks_of("ppn")
    bs = bc[0] + bc[1] + bc[2]
    fr = E.trM(9, bs)
    Lcanon = gmpy2.log(fr / E.trM(9, bs + bond_word("ppn", 0, 1)
                                  + bond_word("ppn", 1, 2) + bond_word("ppn", 0, 2)))
    gapa = abs(Lcanon - mpfr(CORPUS["3He"][1]))
    print(f"    3He canonical ppn  L = {fmt(Lcanon, 15)}  vs published pnp "
          f"{CORPUS['3He'][1]}   arrangement is worth {float(gapa):.6f} in L "
          f"= {float(gapa * ALPHA):.4f} MeV")
    check("3He's published all-pairs number uses the NON-canonical arrangement pnp, which "
          "moves the far bond from pn to pp and is worth 0.07 in L",
          gapa > mpfr("0.06") and gapa < mpfr("0.08"))
    Lprod = gmpy2.log(free / E.trM(9, E.word("pnn", {0, 1, 2})))
    print(f"    and the production engine word() ordering for 3H: L = {fmt(Lprod, 15)}, "
          f"differing from the published value by {float(abs(Lprod - mpfr(CORPUS['3H'][1]))):.4f}")

    print("\n" + "=" * 74)
    print("§4  AT A = 4 THE AMBIGUITY IS WORTH 15 % OF HELIUM-4")
    print("=" * 74)
    order4 = "pnpn"
    A, n4 = 4, 12
    blk4 = blocks_of(order4)
    base4 = [x for b in blk4 for x in b]
    free4 = E.trM(n4, base4)
    pairs = [(i, j) for i in range(A) for j in range(i + 1, A)]
    bw4 = {pr: bond_word(order4, *pr) for pr in pairs}
    sumL = sum(gmpy2.log(free4 / E.trM(n4, base4 + bw4[pr])) for pr in pairs)
    random.seed(7)
    sample = random.sample(list(itertools.permutations(pairs)), 40)
    t0 = time.time()
    vals = []
    for perm in sample:
        w = base4[:]
        for p in perm:
            w += bw4[p]
        vals.append(gmpy2.log(free4 / E.trM(n4, w)))
    lo, hi = min(vals), max(vals)
    spread = hi - lo
    print(f"  order {order4}, {len(pairs)} bonds ({sum(1 for i, j in pairs if j == i+1)} adjacent, "
          f"{sum(1 for i, j in pairs if j > i+1)} bands), 720 orderings; 40 sampled "
          f"[{time.time() - t0:.0f}s]")
    print(f"    distinct L values  : {len({fmt(v, 40) for v in vals})} of 40")
    print(f"    L range            : {fmt(lo, 15)} .. {fmt(hi, 15)}")
    print(f"    SPREAD             : {fmt(spread, 10)}")
    print(f"    x alpha            : {float(spread * ALPHA):.4f} MeV "
          f"= {float(100 * spread * ALPHA / B_AME_4HE):.1f} % of B_AME(4He) = {float(B_AME_4HE)}")
    print(f"    sum of pairwise L  : {fmt(sumL, 15)}")
    print(f"    defect range       : {fmt(lo - sumL, 8)} .. {fmt(hi - sumL, 8)}")
    check("at A=4 the bond ordering moves L by more than 0.9, i.e. over 3.7 MeV and more "
          "than 13 % of helium-4's binding energy",
          spread > mpfr("0.9") and spread * ALPHA / B_AME_4HE > mpfr("0.13"))
    check("the ordering spread is comparable to the many-body defect it is meant to measure",
          spread > abs(hi - sumL) / 3)

    print("\n" + "=" * 74)
    print("§5  A = 2: NO AMBIGUITY AT ALL, AND THE MODEL INVERTS THE PHYSICS")
    print("=" * 74)
    REAL = {"pp": ("2He  (Z=2,N=0)", "UNBOUND — no bound diproton"),
            "pn": ("2H   (Z=1,N=1)", "BOUND, B = 2.22452 MeV"),
            "nn": ("2n   (Z=0,N=2)", "UNBOUND — no bound dineutron")}
    charge = {"pp": 2, "pn": 1, "nn": 0}
    ct = -gmpy2.log(1 - E.H) / 2      # the sibling's charge term per unit charge
    print(f"  {'system':<18}{'bond':<6}{'L':>14}{'B (MeV)':>10}{'L + charge':>12}"
          f"{'B+ (MeV)':>10}   reality")
    L2 = {}
    for o in ("pp", "pn", "nn"):
        bb = blocks_of(o)
        bs2 = bb[0] + bb[1]
        L2[o] = gmpy2.log(E.trM(6, bs2) / E.trM(6, bs2 + bond_word(o, 0, 1)))
        Lc = L2[o] + charge[o] * ct
        print(f"  {REAL[o][0]:<18}{o:<6}{float(L2[o]):14.9f}{float(ALPHA * L2[o]):10.4f}"
              f"{float(Lc):12.6f}{float(ALPHA * Lc):10.4f}   {REAL[o][1]}")
    print(f"  charge term -(e/2)log(1-h) = +{float(ct):.6f} per unit charge: it raises pp and")
    print(f"  pn and leaves nn alone, so it deepens the inversion rather than repairing it.")
    check("the model ranks nn > pn > pp while reality binds only pn — an inversion needing "
          "no ordering convention, since A=2 has a single bond",
          L2["nn"] > L2["pn"] > L2["pp"])
    check("the charge term does not repair the inversion",
          L2["nn"] > L2["pn"] + charge["pn"] * ct and L2["nn"] > L2["pp"] + charge["pp"] * ct)

    print("\n" + "=" * 74)
    print("§S  WHAT THE BEAN ASKED, AND WHAT IT HAS TO ASK FIRST")
    print("=" * 74)
    print("  asked : which PRIME closure carries the many-body cumulants?")
    print("  first : the all-pairs model specifies a bond MULTISET; a link needs a WORD,")
    print("          and the bands do not commute with the bonds they span, so those are")
    print("          not the same datum. At A=4 the difference is 15 % of helium-4.")
    print("  the chain is immune: no bands, every bond a lone generator, all commuting —")
    print("  which is the same fact that makes it a connected sum and its L a sum.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "The all-pairs bond model does not determine a link. Band generators do not "
            "commute with the adjacent bonds whose generators they span, so the bond "
            "multiset does not fix a braid word. At A=3 the six orderings of three bonds "
            "give three distinct 200-bit Markov traces and three distinct Jones "
            "polynomials, at identical letter multiset, exponent sum and strand count. At "
            "A=4, 40 sampled orderings of 720 give a spread of 0.99 in L, which is 4.15 "
            "MeV or 15 percent of helium-4's binding. The chain closure is the control: "
            "its defect is 1e-60, it is a connected sum, and its L is exactly additive. "
            "The corpus's two published A=3 all-pairs values are reconciled as two "
            "different orderings (3He is order pnp, not ppn); the production engine uses "
            "a third. Bean qou-bygw.")
        for k, v in c3.items():
            wb.add_data(f"c3_{k}_production_ordering", fmt(v, 30))
            wb.add_data(f"chain_defect_{k}", fmt(chain_defect[k], 8))
        wb.add_data("A3_distinct_traces", str(nL))
        wb.add_data("A3_distinct_jones_sigma", str(nV))
        wb.add_data("A3_distinct_jones_sigma_inv", str(nV_inv))
        wb.add_data("A4_distinct_of_40_sampled", str(len({fmt(v, 40) for v in vals})))
        wb.add_data("A4_ordering_spread_L", fmt(spread, 20))
        wb.add_data("A4_ordering_spread_MeV", f"{float(spread * ALPHA):.6f}")
        wb.add_data("A4_ordering_spread_pct_of_B_AME_4He",
                    f"{float(100 * spread * ALPHA / B_AME_4HE):.4f}")
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "A=4 is sampled (40 of 720 orderings under a fixed seed), not enumerated, so "
            "the reported spread is a lower bound on the true spread.")
        wb.add_caveat(
            "The Jones comparison resolves every mixed letter to a crossing sign on each "
            "classical branch, as the qou-m3sh probes do; the unresolved Hecke element is "
            "not a link and no statement is made about it.")
        wb.add_caveat(
            "Says nothing about which ordering is correct, whether a canonical one exists, "
            "or whether some prime closure carries the cumulants. It says the multiset "
            "does not name one. The alpha conversion is quoted for scale only and no "
            "binding claim is made.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
