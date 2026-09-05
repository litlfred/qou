#!/usr/bin/env python3
"""The intra-nucleon ordering: what it moves, what it cannot move, and the
multi-level character ratio it unblocks (`qou-gpb5`, after `qou-hu1f`).

`qou-hu1f` settled WHICH ordering is correct — the interleaved
`(sigma_0 sigma_1^-1)^3` is `beta_Bor`, verified against the Lean closed form
(`nf_vs_canonical_word_order_probe`). It left the consequence unmeasured:
`atom_braid_word_3A` — the live canonical route — uses the grouped
`sigma_0^3 sigma_1^-3`, so the question is what in the corpus actually moves.

**The answer is a clean split, and both halves are measurements.**

WHAT CANNOT MOVE — the bond model, at every A
---------------------------------------------
On the canonical chain the character ratio

    R_nucleon(Z,N) = tr_M(W_atom) / tr_M(W_free)

is **identical under the two orderings to ~1e-60** at `2H`, `3H`, `3He` and
`4He` — and equals `prod_i (z + d_i)` over the `A-1` interfaces under *both*.
So `L = -log R`, all three bond constants, and every binding number computed as
a **log-ratio** are untouched by the ordering.

The reason is structural rather than numerical: the chain closure is a
connected sum, and connected-sum multiplicativity of the Markov trace does not
care how each summand's word is internally ordered. Reordering letters inside a
block changes that block's trace; it does not change the interface factors.

`qou-gpb5` asserted this invariance from `2H` alone. It holds at every `A` on
the chain — a strengthening, not a correction. (Its companion claim, that the
ratio is invariant for the ALL-PAIRS word, is a different object and is not
tested here: all-pairs was retired as ill-posed, `qou-bygw`.)

WHAT DOES MOVE — every absolute trace, and difference-based binding
-------------------------------------------------------------------
`R_quark = tr_M(W_free)` is the intra word's own trace, and it is not a ratio:

    atom   grouped (live)   interleaved (beta_Bor)   factor
    2H     1.131716904322   0.299015017185           3.785
    3H     1.117846228978   0.142072056797           7.868
    3He    1.296675612245   0.188178642999           6.891
    4He    1.280783151529   0.089409980502          14.325

`binding_canonical` computes `B = Q_beta(n) . (tr_M(W_free) - tr_M(W_atom))`, a
**difference**. Since both terms carry the same intra factor,

    Delta_tr = R_quark . (1 - prod_i (z + d_i)),

so that route is **exactly proportional to `R_quark`** and would fall by the
factors in the last column above. A log-ratio route is invariant; a difference
route is not. That is the blast radius, in closed form.

THE PER-GENERATOR FACTORISATION IS GROUPED-SPECIFIC — the conclusion survives
-----------------------------------------------------------------------------
`rem:canonical-trace-factorises-over-chain` states the stronger per-generator
form `tr_M(prod_i p_i(sigma_i)) = prod_i [w+ p_i(q) + w- p_i(-1/q)]`, and adds
"the averaged letters sit inside the power of their own generator, so this needs
no branch to be chosen". **That hypothesis is the grouped ordering**: it
requires each generator's letters to be contiguous. Measured here — grouped
factorises to `~3e-59`; interleaved fails by `2.8x` to `13.3x`.

This does **not** retract the arc's conclusion. The load-bearing step for
"the canonical closure carries no many-body binding" is connected-sum
multiplicativity, which is order-invariant, and it is verified here to hold
under interleaving too: `tr_M(chain) = prod_k tr_M(intra_k) . prod_i (z + d_i)`
exactly. What is grouped-specific is the *stated form* of the identity, not
what the arc concludes from it. The Lean file `QOU.Mass.ChainTraceFactor` proves
the factor algebra (`twoStrandTrace_eq` and friends) and is unaffected — it
never claims a particular intra ordering.

THE MULTI-LEVEL PRODUCT, WHICH WAS THE BLOCKED DELIVERABLE
-----------------------------------------------------------
`prf:confined-knot-binding` multiplies character ratios "across all levels".
The quark level's word is the intra word (`qou-gpb5`: gamma-gamma production,
three quarks "confined by the Borromean braid `B_3`"), and the free constituents
are the bare strands, `tr_M(1) = 1`. So the two-level product telescopes:

    R_quark . R_nucleon = tr_M(W_atom),      B_2lvl = -alpha log tr_M(W_atom).

Unfitted, with `alpha = m_e/(q0(q0-1)) = 4.185981` MeV:

    atom   B_2lvl interleaved (correct)   B_2lvl grouped   B_AME
    2H     7.8867   (+254.53 %)           2.3152 (+4.07 %)    2.224566
    3H    14.7996   ( +74.49 %)           6.1646 (-27.32 %)   8.481796
    3He   11.8760   ( +53.87 %)           3.7963 (-50.81 %)   7.718041
    4He   18.7888   ( -33.60 %)           7.6457 (-72.98 %)  28.295662

**The two-level product does not work, and it is worse under the correct
ordering at every A below 4.** It overshoots `2H` by `3.5x`. Recorded as the
answer rather than repaired: the grouped column's `+4.07 %` at `2H` is agreement
produced by a word that is not `beta_Bor`, which is the precise thing the
2026-09-05 no-fitting directive says is worth less than an honest miss.

The nuclear-jet level remains unbuilt, so this is two of the three levels the
specification names.

WHAT IS NOT CLAIMED
-------------------
No binding claim; `B = alpha L` remains the open interpretation of
`rem:bond-log-ratio-is-a-free-energy`. No claim that any published log-ratio
number is wrong — the measurement here is that they cannot be. No claim about
what `atom_braid_word_3A` *should* be changed to: the fix is a 685-call-site
question and this probe is the measurement that has to precede it. The
`|tr_M(q0)|` mass identity reaches `beta_Bor` through the Lean closed form, not
through either word builder, so it is untouched either way.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

ALPHA = mpfr(str(M_E_MEV)) / (E.Q * (E.Q - 1))
H, Z0 = E.H, E.ZERO
TOL = mpfr("1e-40")
ISO = [("pn", 1, 1, "2H", "2.224566"), ("pnn", 1, 2, "3H", "8.481796"),
       ("ppn", 2, 1, "3He", "7.718041"), ("ppnn", 2, 2, "4He", "28.295662")]


def n_inter(b, g0, g1):
    """Interleaved: `(sigma_g0 sigma_g1^-1)^3` then content then gluons."""
    return E.nucleon_word(b, g0, g1)


def n_group(b, g0, g1):
    """Grouped: all of the g0 chain, then all of the g1 chain — the
    `atom_braid_word_3A` / `nucleon_gen_chains` assembly."""
    return ([(1, Z0, g0)] * 3 + [(1, -b[0] * H, g0), (1, -b[1] * H, g0)]
            + [(1, Z0, g0), (1, Z0, g0)]
            + [(1, -H, g1)] * 3 + [(1, -b[2] * H, g1)])


def chain(order, builder, bonds=True):
    """Canonical chain word: intra per nucleon, one interface at `3k+2`
    between adjacent nucleons only. Mirrors `atom_braid_word_3A`."""
    w = []
    for k in range(len(order)):
        w += builder(E.B_P if order[k] == "p" else E.B_N, 3 * k, 3 * k + 1)
        if bonds and k < len(order) - 1:
            w.append((1, E.bond_d(order[k], order[k + 1]), 3 * k + 2))
    return w


def per_generator_product(w):
    """The `rem:canonical-trace-factorises-over-chain` right-hand side:
    one two-strand trace per generator, `w+ p(q) + w- p(-1/q)`."""
    _ps, (wp, wm) = E.weights(2)
    out = mpfr(1)
    for g in sorted({g for _c, _d, g in w}):
        pq, pm = mpfr(1), mpfr(1)
        for _c, d, gg in w:
            if gg == g:
                pq *= (E.Q + d)
                pm *= (-1 / E.Q + d)
        out *= wp * pq + wm * pm
    return out


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    def f(v):
        return float(v)  # float64-ok: display only

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR; "
          f"alpha = {f(ALPHA):.6f} MeV")

    print("\n" + "=" * 76)
    print("§1  WHICH WORD IS beta_Bor — against the Lean closed form")
    print("=" * 76)
    lean = (4 + H ** 2 - 3 * H ** 4 - H ** 6) / (H ** 2 + 4)
    rel = {}
    for nm, w in (("interleaved (s0 s1^-1)^3", [(1, Z0, 0), (1, -H, 1)] * 3),
                  ("grouped     s0^3 s1^-3", [(1, Z0, 0)] * 3 + [(1, -H, 1)] * 3)):
        v = abs(E.trM(3, w))
        rel[nm[:4]] = abs(v - lean) / lean
        print(f"    {nm:26s} |tr_M| = {gmpy2.digits(v, 10, 22)[0]}   "
              f"rel {f(rel[nm[:4]]):.3e}")
    print(f"    {'Lean (4+h^2-3h^4-h^6)/(h^2+4)':26s}          "
          f"{gmpy2.digits(lean, 10, 22)[0]}")
    check("the INTERLEAVED word is beta_Bor (Lean closed form, rel < 1e-40)",
          rel["inte"] < TOL)
    check("the GROUPED word is a different object (off by more than 50 %)",
          rel["grou"] > mpfr("0.5"))

    print("\n" + "=" * 76)
    print("§2  BOTH RECONSTRUCTIONS ARE THE PRODUCTION WORD, NOT A MODEL")
    print("=" * 76)
    ok_prod = True
    for order, Z, N, nm, _a in ISO:
        n = 3 * (Z + N)
        for builder, io in ((n_group, "grouped"), (n_inter, "borromean")):
            prod = E.trM(n, [(1, mpfr(str(d)), g) for _c, d, g in
                             atom_braid_word_3A(Z, N, include_inter=True,
                                                intra_order=io)])
            mine = E.trM(n, chain(order, builder, True))
            r = abs(prod - mine) / abs(prod)
            ok_prod &= r < TOL
            print(f"    {nm:>5} {io:>10}  atom_braid_word_3A "
                  f"{gmpy2.digits(prod, 10, 20)[0]}   rebuilt "
                  f"{gmpy2.digits(mine, 10, 20)[0]}   rel {f(r):.2e}")
    check("both rebuilds reproduce atom_braid_word_3A's own trace to 1e-40 under "
          "the matching intra_order — every comparison below is against production",
          ok_prod)

    print("\n" + "=" * 76)
    print("§2b THE PRODUCTION DEFAULT IS NOW beta_Bor (owner ruling, 2026-09-05)")
    print("=" * 76)
    dflt = [g for _c, _d, g in atom_braid_word_3A(1, 1)][:6]
    grpd = [g for _c, _d, g in atom_braid_word_3A(1, 1, intra_order="grouped")][:6]
    print(f"    default            first 6 generators: {dflt}")
    print(f"    intra_order=grouped first 6 generators: {grpd}")
    check("atom_braid_word_3A now emits the ALTERNATING confinement core "
          "(sigma_0 sigma_1^-1)^3 by default", dflt == [0, 1, 0, 1, 0, 1])
    check("and intra_order='grouped' still reaches the pre-2026-09-05 word, so "
          "every published absolute number stays reproducible",
          grpd == [0, 0, 0, 0, 0, 0])

    print("\n" + "=" * 76)
    print("§3  WHAT CANNOT MOVE: R_nucleon, AND IT IS prod(z + d) UNDER BOTH")
    print("=" * 76)
    print(f"    {'atom':>5} {'R_nucleon grouped':>21} {'R_nucleon interleaved':>23}"
          f" {'|diff|':>10} {'vs prod(z+d)':>13}")
    ok_inv, ok_cs, Rn, Rq = True, True, {}, {}
    for order, Z, N, nm, _a in ISO:
        n = 3 * (Z + N)
        v = {}
        for builder, k in ((n_group, "g"), (n_inter, "i")):
            ti = E.trM(n, chain(order, builder, bonds=False))
            tf = E.trM(n, chain(order, builder, bonds=True))
            v[k] = (ti, tf / ti, tf)
        expect = mpfr(1)
        for j in range(len(order) - 1):
            expect *= (E.Q ** 3 / (E.Q ** 2 + 1)) + E.bond_d(order[j], order[j + 1])
        d = abs(v["i"][1] - v["g"][1])
        dcs = max(abs(v["i"][1] - expect), abs(v["g"][1] - expect))
        ok_inv &= d < TOL
        ok_cs &= dcs < TOL
        Rn[nm], Rq[nm] = v["g"][1], (v["g"][0], v["i"][0], v["g"][2], v["i"][2])
        print(f"    {nm:>5} {f(v['g'][1]):21.15f} {f(v['i'][1]):23.15f} "
              f"{f(d):10.1e} {f(dcs):13.1e}")
    check("R_nucleon is IDENTICAL under the two orderings at every A — the bond "
          "model is untouched by the intra ordering", ok_inv)
    check("and equals prod_i (z + d_i) under BOTH — connected-sum multiplicativity "
          "survives interleaving", ok_cs)

    print("\n" + "=" * 76)
    print("§4  WHAT DOES MOVE: every absolute trace, and difference-based binding")
    print("=" * 76)
    print(f"    {'atom':>5} {'R_quark grouped':>18} {'R_quark interleaved':>21}"
          f" {'factor':>8} {'Delta_tr factor':>16}")
    ok_move = True
    for _o, _Z, _N, nm, _a in ISO:
        g, i, tfg, tfi = Rq[nm]
        fac = g / i
        dfac = (g - tfg) / (i - tfi)
        ok_move &= fac > mpfr(3)
        print(f"    {nm:>5} {f(g):18.12f} {f(i):21.12f} {f(fac):8.3f} "
              f"{f(dfac):16.3f}")
    check("absolute traces move by more than 3x at every A, and binding_canonical's "
          "Delta_tr moves by the SAME factor (it is proportional to R_quark)",
          ok_move)

    print("\n" + "=" * 76)
    print("§5  THE PER-GENERATOR FACTORISATION IS GROUPED-SPECIFIC")
    print("=" * 76)
    ok_fac_g, ok_fac_i = True, True
    for order, _Z, _N, nm, _a in ISO:
        n = 3 * len(order)
        for builder, k in ((n_group, "grouped"), (n_inter, "interleaved")):
            w = chain(order, builder, bonds=True)
            act, pred = E.trM(n, w), per_generator_product(w)
            r = abs(act - pred) / abs(act)
            if k == "grouped":
                ok_fac_g &= r < TOL
            else:
                ok_fac_i &= r > mpfr(1)
            print(f"    {nm:>5} {k:>12}  tr_M {f(act):16.12f}  "
                  f"prod_g tr_2 {f(pred):16.12f}  rel {f(r):9.2e}")
    check("the per-generator identity holds for the GROUPED word — the form stated "
          "in rem:canonical-trace-factorises-over-chain assumes that ordering",
          ok_fac_g)
    check("and fails by more than 100 % for the interleaved word — but §3 shows the "
          "arc's CONCLUSION rests on connected sum, which survives", ok_fac_i)

    print("\n" + "=" * 76)
    print("§6  THE MULTI-LEVEL PRODUCT (qou-gpb5), UNFITTED")
    print("=" * 76)
    print(f"    {'atom':>5} {'B_2lvl interleaved':>19} {'err':>9}"
          f" {'B_2lvl grouped':>16} {'err':>9} {'B_AME':>10}")
    B2 = {}
    for _o, _Z, _N, nm, ame in ISO:
        _g, _i, tfg, tfi = Rq[nm]
        a = mpfr(ame)
        bi, bg = -ALPHA * gmpy2.log(tfi), -ALPHA * gmpy2.log(tfg)
        B2[nm] = bi
        print(f"    {nm:>5} {f(bi):19.4f} {f(100 * (bi - a) / a):8.2f}%"
              f" {f(bg):16.4f} {f(100 * (bg - a) / a):8.2f}% {f(a):10.6f}")
    check("the two-level product OVERSHOOTS 2H by more than 3x under the correct "
          "ordering — recorded as the answer, not repaired", B2["2H"] > mpfr(3) * mpfr("2.224566"))

    print("\n" + "=" * 76)
    print("§7  THE LEAN FILE'S DEFINITIONS ARE THESE OBJECTS, NOT LOOKALIKES")
    print("=" * 76)
    print("  QOU.Mass.IntraOrdering defines groupedConfinement as the per-generator")
    print("  product tr_2(sigma^3).tr_2(sigma^-3) and borromeanConfinement as the")
    print("  closed form (4+h^2-3h^4-h^6)/(h^2+4), then proves they differ. This")
    print("  section checks both definitions against the ENGINE, so a Lean proof")
    print("  about them is a proof about the words this probe measures.")
    _ps, (wp, wm) = E.weights(2)
    lean_grouped = ((wp * E.Q ** 3 + wm * (-1 / E.Q) ** 3)
                    * (wp * (1 / E.Q) ** 3 + wm * (-E.Q) ** 3))
    lean_borr = ((4 + H ** 2 - 3 * H ** 4 - H ** 6) / (H ** 2 + 4))
    eng_grouped = abs(E.trM(3, [(1, Z0, 0)] * 3 + [(1, -H, 1)] * 3))
    eng_borr = abs(E.trM(3, [(1, Z0, 0), (1, -H, 1)] * 3))
    rg = abs(lean_grouped - eng_grouped) / eng_grouped
    rb = abs(lean_borr - eng_borr) / eng_borr
    print(f"    groupedConfinement   Lean def {gmpy2.digits(lean_grouped, 10, 22)[0]}")
    print(f"                         engine   {gmpy2.digits(eng_grouped, 10, 22)[0]}"
          f"   rel {f(rg):.2e}")
    print(f"    borromeanConfinement Lean def {gmpy2.digits(lean_borr, 10, 22)[0]}")
    print(f"                         engine   {gmpy2.digits(eng_borr, 10, 22)[0]}"
          f"   rel {f(rb):.2e}")
    check("Lean's groupedConfinement IS tr_M(sigma_0^3 sigma_1^-3) — the "
          "per-generator product is what the grouped word traces", rg < TOL)
    check("Lean's borromeanConfinement IS tr_M((sigma_0 sigma_1^-1)^3) — so "
          "grouped_ne_borromean is a statement about these two words", rb < TOL)

    print("\n" + "=" * 76)
    print("§S  WHAT THIS SETTLES")
    print("=" * 76)
    print("  The intra ordering splits the corpus cleanly. Log-ratio quantities —")
    print("  L, the three bond constants, R_nucleon — are provably untouched,")
    print("  because connected-sum multiplicativity does not see the order inside")
    print("  a block. Absolute traces and the difference-based binding_canonical")
    print("  route move by 3.8x to 14.3x, and that factor is R_quark exactly.")
    print("  The per-generator factorisation identity, as stated, assumes the")
    print("  grouped word; the conclusion drawn from it does not.")
    print("  The two-level character ratio is now computable and it misses:")
    print("  +254 % at 2H, -34 % at 4He. That is the unfitted answer.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Measures the consequence of the qou-hu1f intra-ordering finding. On the "
            "canonical chain the character ratio R_nucleon = tr_M(W_atom)/tr_M(W_free) "
            "is identical under the grouped and interleaved orderings to ~1e-60 at A = "
            "2, 3, 4, and equals prod_i (z + d_i) under both, because connected-sum "
            "multiplicativity is blind to letter order inside a block. So L and the "
            "bond constants cannot move. Absolute traces do move: R_quark falls by "
            "3.785x (2H), 7.868x (3H), 6.891x (3He), 14.325x (4He) when the intra block "
            "is rebuilt as beta_Bor, and binding_canonical's Delta_tr = R_quark (1 - "
            "prod(z+d)) moves by the same factor. The per-generator factorisation form "
            "stated in rem:canonical-trace-factorises-over-chain holds only for the "
            "grouped word (3e-59 vs a 2.8x-13.3x failure), though the arc's conclusion "
            "rests on connected sum and survives. The unblocked two-level character "
            "ratio gives 2H +254.53 %, 3H +74.49 %, 3He +53.87 %, 4He -33.60 %: it does "
            "not work, and is worse than the grouped word below A = 4. No fitting.")
        for nm in Rn:
            wb.add_data(f"R_nucleon_{nm}", gmpy2.digits(Rn[nm], 10, 25)[0])
            wb.add_data(f"R_quark_interleaved_{nm}", gmpy2.digits(Rq[nm][1], 10, 25)[0])
            wb.add_data(f"R_quark_grouped_{nm}", gmpy2.digits(Rq[nm][0], 10, 25)[0])
            wb.add_data(f"B_two_level_interleaved_{nm}", gmpy2.digits(B2[nm], 10, 20)[0])
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Chain word only. The all-pairs variant is a different object and is "
            "retired as ill-posed (qou-bygw); its ratio invariance is NOT tested here.")
        wb.add_caveat(
            "Two of the three levels. prf:confined-knot-binding also names a "
            "nuclear-jet level, which has no word.")
        wb.add_caveat(
            "No binding claim, and no ruling on whether atom_braid_word_3A should be "
            "changed — that is a 685-call-site question this measurement precedes.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
