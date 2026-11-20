#!/usr/bin/env python3
"""The canonical mass trace factorises over the chain: the Markov trace of the
3A-strand atom word is the PRODUCT of two-strand traces, one per generator, to
~1e-59 — because the closure is a connected sum. So the canonical closure
carries no many-body binding at all, and the arc's bond constants are
`-log(z + d)`.

WHAT THE CHAIN FORM IMPLIES
---------------------------
`the_canonical_closure_is_a_chain_of_torus_links_probe` (bean `qou-m3sh`)
showed the canonical atom word is, letter for letter, a product of
per-generator powers in Coxeter order — on each classical branch a chain form
`∏_i σ_i^{e_i}` whose closure is a linear connected sum of the torus links
`T(2, e_i)`. Every multiplicative link invariant is then a product over the
chain, and the normalised Markov trace is multiplicative under shared-strand
concatenation (the connected sum), not only under split union — that is the
content of `P(L_1 # L_2) = P(L_1) P(L_2)` read back through the closure.

The averaged letters do not spoil this. Each sits inside the power of its own
generator, so the Hecke word is `∏_i p_i(σ_i)` with `p_i` a polynomial in one
generator, and the trace of a product of one-generator polynomials in Coxeter
order is the product of their two-strand traces. On `H_2` under convention D
the two blocks are `(2)` and `(1,1)` with `σ ↦ q` and `σ ↦ -1/q`, so

    tr_M( ∏_i p_i(σ_i) )  =  ∏_i [ w₊ p_i(q) + w₋ p_i(-1/q) ],
    w₊ = [3]_q / ([3]_q + 1),   w₋ = 1 / ([3]_q + 1).

MEASURED, AT 200 BITS
---------------------
Full `H_{3A}` trace of `atom_canonical_crossings(Z, N)` (the exact engine of
`the_binding_arc_was_measured_in_float64_probe`, q from `Q_50_DIGIT_STR`)
against the product of two-strand factors:

    2H   n = 6    |rel diff|  2.3e-59
    3H   n = 9                3.1e-59
    3He  n = 9                3.1e-59
    4He  n = 12               4.0e-59

and Jones multiplicativity `V(W_A) = ∏_i V(T(2, e_i))` holds exactly on both
branches for `A ≤ 4`.

WHAT THE FACTORS ARE
--------------------
An interface generator carries one letter `σ + d`, and its two-strand trace is
`w₊(q + d) + w₋(-1/q + d) = z + d` with `z = w₊ q - w₋ / q = q³/(q²+1)` — the
affine law `μ(d) = z + d` the arc measured. The free word drops the interfaces,
so `L = log(tr_free / tr_atom)` is a SUM over the `A - 1` interfaces of
`-log(z + d)`:

    L_pp = -log z            = 0.48989938425513485140655016749462194823043396786058
    L_nn = -log(z - h)       = 0.90726226553321290067017528738691153644541109117659
    L_pn = -log(z + d_pn)    = 0.67682159238634338966311878404365178434961219856897

These are the arc's three bond constants to all sixty digits — derived here in
one line each from the two-strand trace, where the arc measured them with
`H_6`. The chain closed form `B_sym = a[(Z-1) L_pp + L_pn + (N-1) L_nn]`
(`QOU.BraidKnot.BsymLinearChain`, bean `6z40`, where the factorisation was
"the named structural input, not asserted") is therefore a corollary of the
topology: connected sum ⟹ multiplicative trace ⟹ additive `L`.

THE CONSEQUENCE FOR THE BINDING GAP
-----------------------------------
The many-body cumulants of the arc (`c_3 < 0`, `c_4 < 0`, `c_5 > 0`, the
order-six datum) belong to the ALL-PAIRS bond model, whose band-routed bonds
interleave generators across blocks and destroy the chain form. The canonical
closure itself has none: its Markov trace is exactly a product, its `L` exactly
a sum of pairwise interface terms, and by the same token so is every other
multiplicative invariant of a connected sum. With `alpha = m_e/(q0(q0-1)) =
4.185981 MeV` the chain gives `4He` `alpha (L_pp + L_pn + L_nn) = 8.6817 MeV`
against `B_AME = 28.2957`, i.e. **31 %**; the missing **69 %** is therefore not
absent from the canonical closure by measurement — it is absent by theorem.

(A first draft of this paragraph said `62 %` short. That was wrong twice over:
it was not a corpus figure, and it is not what the chain delivers. Chain
fractions of `B_AME`, recomputed here: `2H` 1.274, `3H` 0.782, `3He` 0.633,
`4He` 0.307, `6Li` 0.454 — the naive-additive ALL-PAIRS fractions, for
contrast, are 1.274 / 1.116 / 1.000 / 0.607 / 1.345.)

Any closure that carries genuinely many-body binding must fail to be a
connected sum: non-split, non-composite, with the kind of irreducibly
multi-component linking the Borromean rings have and this chain does not. That
is the precise form of "the missing binding is not in the bond graph", and it
says which topology the search has to move to (bean `qou-bygw`).

AND IT RULES OUT THE OBVIOUS REPAIR, IN ONE LINE
------------------------------------------------
Because the interface law is affine, `mu(d) = z + d`, ANY proposed modification
that acts as an interface offset — a different convention, a fractional twist
insertion `q^{2c(lambda)/n}` — has bond constant `-log(z + d)` immediately, with
no trace to run. Invert it on `4He`: closing the chain's gap with a common
offset on all three interfaces needs `-log(z + d) = (B_AME/alpha)/3 = 2.253212`,
i.e. `z + d = 0.105061`, i.e. `d = -0.507627 = -2.4281 h`. The algebra's letters
supply `d in {0, -h/2, D_PN, -h}`, so `d/h in [-1, 0]`: the required offset is
**2.43x more negative than the most negative letter that exists**, and the
required factor `0.105` is a quarter of the smallest available one
(`z - h = 0.403628`). No interface offset can close the gap — not a marginal
miss, an out-of-range one. §4 computes this.

WHAT IS NOT CLAIMED
-------------------
Nothing about which non-composite closure is right, or that one exists in the
framework. The identity is checked for `A ≤ 4` here (`A = 6` is a longer run of
the same engine and is not part of the CI budget); the multiplicativity it
instantiates is a theorem for every `A` given the chain form, which the chain
probe verified through `A = 12`.
"""
from __future__ import annotations

import sys
import time
from collections import defaultdict
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
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

_spec = importlib.util.spec_from_file_location(
    "tc", HERE / "total_curvature_is_the_computable_half_probe.py")
tc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tc)

DVAL = {"sigma": E.ZERO, "sigma_inv": -E.H, "averaged": -E.H / 2,
        "averaged_weighted": E.D_PN}
ISOTOPES = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He")]
# the arc's exact bond constants (200-bit, the_binding_arc_was_measured_in_float64_probe)
ARC = {
    "pp": "0.48989938425513485140655016749462194823043396786058",
    "pn": "0.67682159238634338966311878404365178434961219856897",
    "nn": "0.90726226553321290067017528738691153644541109117659",
}


def canonical_word(Z, N):
    """The GROUPED chain word, named explicitly since 2026-09-05.

    The per-generator factorisation this probe measures — `tr_M(∏ p_i(σ_i)) =
    ∏_i tr_2(p_i)` — requires each generator's letters to be CONTIGUOUS, which
    is a property of the word's assembly rather than of the chain topology.
    `atom_braid_word_3A` now defaults to the Borromean `(σ_0 σ_1^-1)^3` intra
    core, which interleaves them and does not satisfy the identity (it misses
    by 2.8x at A=2 rising to 13.3x at A=4). So this probe asks for the word
    whose property it is testing.

    Nothing measured here changes as a result. The bond constants, `L_pp +
    L_nn`, the 31 % figure and the offset inversion are all log-RATIO
    quantities, which are invariant under the intra ordering to ~1e-60 —
    proved in `QOU.Mass.IntraOrdering.chainRatio_eq_of_intra`, measured in
    `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py`.
    """
    return [(1, DVAL[k], g)
            for g, k in atom_canonical_crossings(Z, N, intra_order="grouped")]


def two_strand():
    ps, ws = E.weights(2)
    assert ps == [(2,), (1, 1)]
    return ws[0], ws[1], E.Q, -1 / E.Q


def tr2(letters, wp, wm, lp, lm):
    pp = mpfr(1)
    pm = mpfr(1)
    for c, d, _g in letters:
        pp *= c * lp + d
        pm *= c * lm + d
    return wp * pp + wm * pm


def fmt(x, k=30):
    m, e, _ = gmpy2.digits(x, 10, k)
    sign = "-" if m.startswith("-") else ""
    m = m.lstrip("-")
    return f"{sign}{m[0]}.{m[1:]}e{e - 1}"


def chain_runs(word):
    runs = []
    for g, s in word:
        if runs and runs[-1][0] == g:
            runs[-1][1] += s
            if runs[-1][1] == 0:
                runs.pop()
        else:
            runs.append([g, s])
    return runs


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR")
    wp, wm, lp, lm = two_strand()
    z = wp * lp + wm * lm
    print(f"  two-strand weights  w+ = {fmt(wp, 20)}  w- = {fmt(wm, 20)}")
    print(f"  z = w+ q - w-/q     = {fmt(z, 30)}   (q^3/(q^2+1) = {fmt(E.Q**3/(E.Q**2+1), 30)})")
    check("two-strand trace of a single sigma is the Markov z = q^3/(q^2+1)",
          abs(z - E.Q ** 3 / (E.Q ** 2 + 1)) < mpfr(2) ** (-(E.BITS - 12)))

    print("\n" + "=" * 72)
    print("§1  FULL H_{3A} TRACE vs PRODUCT OF TWO-STRAND GENERATOR TRACES")
    print("=" * 72)
    worst = mpfr(0)
    for Z, N, name in ISOTOPES:
        n = 3 * (Z + N)
        w = canonical_word(Z, N)
        t0 = time.time()
        full = E.trM(n, w)
        by_gen = defaultdict(list)
        for c, d, g in w:
            by_gen[g].append((c, d, g))
        prod = mpfr(1)
        for g in sorted(by_gen):
            prod *= tr2(by_gen[g], wp, wm, lp, lm)
        rel = abs(full - prod) / abs(full)
        worst = max(worst, rel)
        print(f"  {name:4s} n={n:2d}  tr_M(full) = {fmt(full)}   product = {fmt(prod)}"
              f"   |rel diff| {float(rel):.2e}   ({time.time() - t0:.1f}s)")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
        if name == "2H":
            for g in sorted(by_gen):
                kinds = [k for gg, k in
                         atom_canonical_crossings(Z, N, intra_order="grouped")
                         if gg == g]
                print(f"        gen {g}: {len(by_gen[g])} letters  tr_2 = {fmt(tr2(by_gen[g], wp, wm, lp, lm), 24)}"
                      f"   [{', '.join(kinds)}]")
    check("tr_M(atom) = prod_i tr_2(p_i(sigma)) for A = 2, 3, 4 below 1e-55", worst < mpfr("1e-55"))

    print("\n" + "=" * 72)
    print("§2  THE INTERFACE FACTORS ARE z + d, AND THE BOND CONSTANTS ARE -log(z + d)")
    print("=" * 72)
    ok_all = True
    for name, d in (("pp", E.ZERO), ("nn", -E.H), ("pn", E.D_PN)):
        f = tr2([(1, d, 0)], wp, wm, lp, lm)
        L = -gmpy2.log(f)
        gap = abs(L - mpfr(ARC[name]))
        ok_all &= gap < mpfr("1e-48")
        print(f"  {name}: tr_2(sigma + d) = z + d = {fmt(f, 24)}   -log = {fmt(L, 40)}"
              f"\n       arc (H_6, 200-bit)         {ARC[name][:42]}   |diff| {float(gap):.1e}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    check("L_pp, L_nn, L_pn = -log(z + d) reproduce the arc's 200-bit H_6 values", ok_all)
    print("  consequently L(canonical) = sum over the A-1 interfaces of -log(z + d_i):"
          " no many-body term exists in the canonical closure.")

    print("\n" + "=" * 72)
    print("§3  JONES MULTIPLICATIVITY OVER THE CHAIN (both branches, A ≤ 4)")
    print("=" * 72)
    all_j = True
    for Z, N, name in ISOTOPES:
        n = 3 * (Z + N)
        for avg, bname in ((1, "sigma"), (-1, "sigma^-1")):
            word = tc.resolve(Z, N, avg)
            V = tc.jones_closure(n, word)
            prod = {0: 1}
            for g, e in chain_runs(word):
                prod = tc.pmul(prod, tc.jones_closure(2, [(0, 1 if e > 0 else -1)] * abs(e)))
            same = (V == prod)
            all_j &= same
            print(f"  {name:4s} {bname:8s}  V(W_A) == prod_i V(T(2,e_i)): {same}")
    check("Jones of the closure is the product of the torus-link Jones over the chain", all_j)

    print("\n" + "=" * 72)
    print("§4  WHAT THE CHAIN IS WORTH, AND WHY NO INTERFACE OFFSET CAN FIX IT")
    print("=" * 72)
    from codata_constants import M_E_MEV  # noqa: E402
    from math import comb  # float64-ok: integer combinatorics (comb), no float arithmetic
    alpha = mpfr(str(M_E_MEV)) / (E.Q * (E.Q - 1))
    Lc = {"pp": -gmpy2.log(tr2([(1, E.ZERO, 0)], wp, wm, lp, lm)),
          "nn": -gmpy2.log(tr2([(1, -E.H, 0)], wp, wm, lp, lm)),
          "pn": -gmpy2.log(tr2([(1, E.D_PN, 0)], wp, wm, lp, lm))}
    print(f"  alpha = m_e/(q0(q0-1)) = {float(alpha):.6f} MeV")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    print(f"  L_pp + L_nn = {fmt(Lc['pp'] + Lc['nn'], 20)}   2 log(q + 1/q) = "
          f"{fmt(2 * gmpy2.log(E.Q + 1 / E.Q), 20)}")
    check("L_pp + L_nn = 2 log[2]_q — the pp and nn bond constants are not independent",
          abs(Lc["pp"] + Lc["nn"] - 2 * gmpy2.log(E.Q + 1 / E.Q)) < mpfr(2) ** (-(E.BITS - 12)))
    AME = {"2H": (1, 1, "2.22452"), "3H": (1, 2, _ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)), "3He": (2, 1, _ame_nstr(AME_B_HE3_MEV_VALIDATION, 30)),
           "4He": (2, 2, _ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)), "6Li": (3, 3, "31.9946")}
    print(f"\n  {'iso':>5} {'B_chain':>9} {'B_allpairs':>11} {'B_AME':>9} {'chain/AME':>10} {'allpr/AME':>10}")
    frac = {}
    for name, (Z, N, B) in AME.items():
        B = mpfr(B)
        ch = alpha * ((Z - 1) * Lc["pp"] + Lc["pn"] + (N - 1) * Lc["nn"])
        ap = alpha * (comb(Z, 2) * Lc["pp"] + Z * N * Lc["pn"] + comb(N, 2) * Lc["nn"])
        frac[name] = ch / B
        print(f"  {name:>5} {float(ch):9.4f} {float(ap):11.4f} {float(B):9.4f} "  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
              f"{float(ch / B):10.4f} {float(ap / B):10.4f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    check("the chain delivers 31 % of 4He's AME binding (so 69 % is missing by theorem)",
          abs(frac["4He"] - mpfr("0.3068")) < mpfr("0.0005"))

    B4, need = mpfr(_ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)), mpfr(_ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)) / alpha
    per = need / 3
    d_req = gmpy2.exp(-per) - (wp * lp + wm * lm)
    print(f"\n  Inversion on 4He: a COMMON interface offset closing the chain needs")
    print(f"    -log(z + d) = (B_AME/alpha)/3 = {float(per):.6f}  =>  z + d = {float(gmpy2.exp(-per)):.6f}"  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
          f"  =>  d = {float(d_req):.6f} = {float(d_req / E.H):.4f} h")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    print(f"    the algebra's letters are d in {{0, -h/2, D_PN, -h}}, i.e. d/h in [-1, 0]:")
    print(f"      most negative available factor  z - h = {float(wp * lp + wm * lm - E.H):.6f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    print(f"      required factor                 z + d = {float(gmpy2.exp(-per)):.6f}"  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
          f"   ({float((wp * lp + wm * lm - E.H) / gmpy2.exp(-per)):.2f}x larger)")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    check("the offset that would close 4He is d = -2.43 h, OUTSIDE the algebra's range d/h in [-1, 0] "
          "— no interface offset, fractional twist included, can close the gap",
          d_req / E.H < mpfr("-2") and (wp * lp + wm * lm - E.H) > gmpy2.exp(-per))

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "The Markov trace (convention D, 200-bit) of the full 3A-strand canonical "
            "atom word equals the product over generators of two-strand traces of the "
            "per-generator Hecke polynomials, to ~1e-59 at A = 2, 3, 4; Jones factorises "
            "over the chain on both branches. Reason: the closure is a linear connected "
            "sum (chain form), and multiplicative invariants are multiplicative under "
            "connected sum. Interface factors are z + d, so the arc's bond constants "
            "are -log(z + d) to 60 digits and the canonical L is exactly a sum over "
            "interfaces: the canonical closure carries no many-body binding by "
            "theorem. The arc's cumulants belong to the all-pairs bond model, which "
            "is not a chain.")
        wb.add_data("z_two_strand", fmt(z, 40))
        for name, d in (("pp", E.ZERO), ("nn", -E.H), ("pn", E.D_PN)):
            wb.add_data(f"L_{name}_from_two_strand", fmt(-gmpy2.log(tr2([(1, d, 0)], wp, wm, lp, lm)), 50))
        wb.add_data("worst_rel_diff_full_vs_product", f"{float(worst):.3e}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Checked at A <= 4 (n <= 12) in CI budget; the identity is a theorem for "
            "every A given the chain form, which the chain probe verified through "
            "A = 12. A = 6 is the same computation on a longer run.")
        wb.add_caveat(
            "Says nothing about which non-composite closure would carry many-body "
            "binding, or whether one exists in the framework. It says the canonical "
            "chain cannot, and why.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
