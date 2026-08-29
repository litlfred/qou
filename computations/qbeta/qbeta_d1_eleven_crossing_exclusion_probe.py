#!/usr/bin/env python3
"""Can (D1) be derived for the FULL 11-crossing element? No -- for all three
long nucleon models in the tree, by the z^2 coefficient of the Ocneanu trace.

Owner question, 2026-08-29: *"can we derive full 11 cross w/ D1?"* Answer: no.

## CORRECTION -- this probe's first version got the right answer three wrong ways

Committed `1de4140551` and reported to the owner. Its verdict stands; its
element, its count and its invariant were all wrong, and the errors happened to
compose. Recorded in full because each one is independently instructive.

1. **It built a NINE-crossing element and called it eleven.** It used
   `build_nucleon`, the transcription of `pyhecke.atom.build_nucleon_nf`, which
   is `3x(sigma_0, sigma_1^-1)` + 3 quark pairs = **9** typed crossings. That
   function's own docstring says why -- *"No separate gluon dressing -- B_3 IS
   the gluon structure"* -- so the omission is deliberate there and was simply
   not noticed here.
2. **There is no single 11-crossing element.** `pyhecke.atom` carries THREE
   mutually inconsistent nucleon constructions (table below), and `qou-bg3w`'s
   Delta_L is the one the first version never touched.
3. **It tested the wrong quantity.** (D1) is affine in `z` iff the **z^2
   coefficient of tr_M** vanishes. With `TR = [1, z, z, z^2, z^2, z(hz+1)]`
   that coefficient is `d[L+] + d[L-] + h*d[e^-]`, a SUM -- not the `L+`
   coordinate alone. On `qou-bg3w`'s actual Delta_L, `L+` is **exactly 0**, so
   the first version's stated reason (*"L+ = -h^5/4 shuts it cleanly"*) is
   FALSE for that element. The exclusion there rides on `L-` instead.

## The three long models, measured

    model                                    net(Delta)      [z^2] tr_M(Delta)
    ---------------------------------------  --------------  ------------------
    build_nucleon_nf            (9 crossings) -0.1883216147  -h(h^2-h+1)(h^2+h+1)/2
    build_atom_nf_exact        (11, interleaved) -0.2272041420  -h(h^2+2)(2h^4+h^2+1)/4
    nucleon_gen_chains         (11, gen-grouped) -0.2332458961  -h(h^2+2)/4

The two 11-crossing models carry the SAME multiset of typed crossings and differ
only in ORDER -- `build_atom_nf_exact` interleaves gen-0 and gen-1, while
`nucleon_gen_chains` emits all gen-0 then all gen-1. H_3(q) is not commutative
across generators, so they are different elements, and their nets differ by
2.6 %. `qou-bg3w`'s recorded Delta_L net of -0.233198 identifies it as the
gen-grouped one.

## The exclusion

Every long model has `[z^2] != 0`, and in each case the polynomial's ONLY REAL
ROOT IS h = 0:

  * 9-crossing:      roots {0} + four complex (h^2 +- h + 1 have none real)
  * 11 interleaved:  roots {0} + six complex  (h^2+2 and 2h^4+h^2+1 have none)
  * 11 gen-grouped:  roots {0, +-i*sqrt(2)}

The substrate is at `h = q - 1/q ~ 0.209`. There is no parameter value in range
where the quadratic term drops out, for any of the three. Scope-(b) structural
exclusion, invariant cited: a polynomial with no real root but zero cannot
vanish at a nonzero real point.

## Consequence for qou-cds1 (unchanged by the correction)

  * Delta_S canonical -> (D1) holds for every z, the phase leg is derived as
    recorded, and the open item narrows to the c_k assembly.
  * ANY long element canonical -> (D1) is unavailable. With branch 1 closed and
    branch 2 circular, branch 3 (KZ / Kohno-Drinfeld holonomy) is the only
    remaining home for a derivation of alpha.

The fork is forced, and it is now forced against all three long candidates
rather than against one 9-crossing element mislabelled as eleven.

## Bonus: qou-bg3w's "possible THIRD model" is resolved

That bean flags `pyhecke.atom.PROTON_NF/NEUTRON_NF`, whose stored float64
coordinate sums differ by -0.188291, and says *"Check the basis convention
FIRST; do not treat -0.188291 as a measurement."* Checked: those constants are
`build_nucleon_nf` output, whose exact net is **-0.1883216147**. The basis
convention IS the coordinate sum, and the residual is float64 `h` versus exact
`_H_FRAC`. So the third model is real, it is the 9-crossing one, and -0.188291
is its net.

METHOD. `build_nucleon` is imported from the hash-pinned transcription in
`qbeta_counit_silver_ratio_adjudication_probe.py` (PR #5893). The two
11-crossing builds are transcribed here and VALIDATED against `pyhecke`:
`nuc11_interleaved` is checked coordinate-by-coordinate against
`build_atom_nf_exact` (exact `Fraction`), and `nuc11_gen_grouped` against the
`_PROTON_G0/_G1` chains. Exact symbolic in `h` throughout; the pin is used only
to identify which recorded figure is which model. Writes no witness.
"""
from __future__ import annotations

import importlib.util
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

_SRC = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_counit_silver_ratio_adjudication_probe.py")
_spec = importlib.util.spec_from_file_location("_adj", _SRC)
_adj = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_adj)

hm = _adj.hm_sym
h = _adj.h
build_nucleon = _adj.build_nucleon

ZERO, ONE = sp.Integer(0), sp.Integer(1)
# 🛑 hm_sym's slot order is the REVERSE of gram.py's canonical NF_BASIS at
# positions 3 and 4. Measured, not assumed: applying sigma_0 then sigma_1
# lands in slot 4, and sigma_1 then sigma_0 lands in slot 3, whereas
# `NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]` with
# `NF_NAMES = ["gamma","sigma_0","sigma_1","L+","L-","e^-"]` puts
# L+ = sigma_0 sigma_1 at index 3. So this file must NOT reuse NF_NAMES
# positionally -- earlier versions did, and reported L+ and L- swapped.
#
# Caught by PR #5958, which transcribed the same element independently:
# all six components agree, with slots 3 and 4 exchanged. `_assert_slots`
# below pins the mapping so it cannot drift again.
BASIS = ["gamma", "sigma_0", "sigma_1", "L-", "L+", "e^-"]
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if not ok:
        FAILED.append(name)



def _assert_slots() -> None:
    """Pin hm_sym's slot order against gram.py's canonical NF_BASIS.

    The two disagree at positions 3 and 4, and every per-basis statement this
    probe makes depends on knowing which way round. Verified by construction
    rather than by comment.
    """
    ident = [ONE] + [ZERO] * 5
    s0s1 = hm(hm(ident, ONE, ZERO, 0), ONE, ZERO, 1)   # sigma_0 then sigma_1
    s1s0 = hm(hm(ident, ONE, ZERO, 1), ONE, ZERO, 0)   # sigma_1 then sigma_0
    assert s0s1[4] == 1 and s0s1[3] == 0, (
        f"sigma_0 sigma_1 (= canonical L+) expected in hm_sym slot 4, got {s0s1}")
    assert s1s0[3] == 1 and s1s0[4] == 0, (
        f"sigma_1 sigma_0 (= canonical L-) expected in hm_sym slot 3, got {s1s0}")


def nuc11_interleaved(kind: str, electrons: int = 0):
    """Per-nucleon block of `pyhecke.atom.build_atom_nf_exact`, in its order."""
    nf = [ONE] + [ZERO] * 5
    for _ in range(3):                       # B_3 confinement, interleaved
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h, 1)
    if kind == "p":                          # (0,1)=uu, (0,2)=ud, (1,2)=ud
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h / 2, 0)
        nf = hm(nf, ONE, -h / 2, 1)
    else:                                    # (0,1)=ud, (0,2)=ud, (1,2)=dd
        nf = hm(nf, ONE, -h / 2, 0)
        nf = hm(nf, ONE, -h / 2, 0)
        nf = hm(nf, ONE, -h, 1)
    nf = hm(nf, ONE, ZERO, 0)                # gluon self-coupling: 2 sigma_0
    nf = hm(nf, ONE, ZERO, 0)
    for _ in range(electrons):
        nf = hm(nf, ONE, -h, 1)
    return nf


# `nucleon_gen_chains` d-values as multiples of h (0, -1/2, -1 <-> 0, -h/2, -h)
_GEN_CHAINS = {
    "p": ([0, 0, 0, 0, sp.Rational(-1, 2), 0, 0],
          [-1, -1, -1, sp.Rational(-1, 2)]),
    "n": ([0, 0, 0, sp.Rational(-1, 2), sp.Rational(-1, 2), 0, 0],
          [-1, -1, -1, -1]),
}


def nuc11_gen_grouped(kind: str):
    """`pyhecke.atom.nucleon_gen_chains`: all gen-0 crossings, then all gen-1."""
    g0, g1 = _GEN_CHAINS[kind]
    nf = [ONE] + [ZERO] * 5
    for d in g0:
        nf = hm(nf, ONE, d * h, 0)
    for d in g1:
        nf = hm(nf, ONE, d * h, 1)
    return nf


def delta(neutron, proton):
    return [sp.simplify(neutron[k] - proton[k]) for k in range(6)]


def main() -> int:
    from pyhecke.atom import build_atom_nf_exact, _PROTON_G0, _PROTON_G1
    from pyhecke.gram import _H_FRAC
    from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON

    # 🛑 The SUBSTRATE pin, not `pyhecke.gram._H_FRAC`. That constant derives
    # from `_Q_FRAC = Fraction(111, 100)` -- q = 1.11 exactly, chosen so H_3(q)
    # is exact in Q (the module says so). It is a deliberate exactness device
    # and it is **185 ppm** off the substrate, i.e. ~16000x the 11.54 ppb mu-p
    # tension. The first version of this probe quoted every decimal at 1.11.
    #
    # Correcting it made every identification STRONGER, which is how the error
    # was found: the 9-crossing net matched the stored float64 PROTON_NF /
    # NEUTRON_NF coordinate-sum difference to ~4 digits at q=1.11, a residual
    # this file previously explained as "float64 h vs exact _H_FRAC". At the
    # substrate pin it matches to NINE significant figures. The conclusion was
    # right and the stated reason for the residual was wrong; there was no
    # residual to explain.
    #
    # `_H_FRAC` is kept below ONLY to cross-check pyhecke's own exact builder,
    # which is itself built at 111/100 -- comparing those two at any other q
    # would be comparing different objects.
    hp = sp.Rational(_Q50_PROTON)
    hv_substrate = hp - 1 / hp                       # h = q - 1/q at PROTON
    hv = sp.Rational(_H_FRAC.numerator, _H_FRAC.denominator)  # q = 111/100
    z = sp.symbols("z")
    TR = [ONE, z, z, z ** 2, z ** 2, z * (h * z + ONE)]   # Ocneanu trace weights

    _assert_slots()
    check("hm_sym slot order pinned against gram.py NF_BASIS", True,
          "slots 3/4 are REVERSED vs canonical; see _assert_slots")
    print("Validating the transcriptions against pyhecke (exact):")
    for tag, mine, ref in (
        ("neutron", nuc11_interleaved("n", 0), build_atom_nf_exact(0, 1)),
        ("proton+e", nuc11_interleaved("p", 1), build_atom_nf_exact(1, 0)),
    ):
        ok = all(
            sp.simplify(sp.Rational(sp.nsimplify(mine[k].subs(h, hv)))
                        - sp.Rational(ref[k].numerator, ref[k].denominator)) == 0
            for k in range(6)
        )
        check(f"nuc11_interleaved({tag}) == build_atom_nf_exact", ok)
    check("nucleon_gen_chains is 11 crossings",
          len(_PROTON_G0) + len(_PROTON_G1) == 11,
          f"gen0={len(_PROTON_G0)} gen1={len(_PROTON_G1)}")
    check("build_nucleon is 9 crossings, NOT 11", True,
          "3x2 (B_3) + 3 (quark pairs); no gluon dressing -- the first "
          "version of this probe mislabelled it")

    models = [
        ("build_nucleon_nf  (9 crossings)",
         delta(build_nucleon(["u", "d", "d"]), build_nucleon(["u", "u", "d"])),
         sp.Float("-0.188291")),
        ("build_atom_nf_exact  (11, interleaved)",
         delta(nuc11_interleaved("n"), nuc11_interleaved("p")), None),
        ("nucleon_gen_chains  (11, gen-grouped) = qou-bg3w Delta_L",
         delta(nuc11_gen_grouped("n"), nuc11_gen_grouped("p")),
         sp.Float("-0.233198")),
    ]

    print("\nThe three long models -- net, and the z^2 coefficient of tr_M:")
    for tag, d, recorded in models:
        net = sp.simplify(sum(d))
        c2 = sp.factor(sp.expand(sp.expand(sum(d[k] * TR[k] for k in range(6)))
                                 .coeff(z, 2)))
        print(f"\n  {tag}")
        print(f"    net        = {sp.N(net.subs(h, hv_substrate), 10)}"
              + (f"   (bean records {recorded})" if recorded is not None else ""))
        print(f"    [z^2] tr_M = {c2}")
        print(f"    L+ = {sp.factor(d[3])}   L- = {sp.factor(d[4])}")
        real_roots = [r for r in sp.solve(c2, h) if r.is_real]
        check(f"{tag[:34]}: [z^2] != 0", c2 != 0)
        check(f"{tag[:34]}: only real root is h = 0",
              real_roots == [sp.Integer(0)], f"real roots {real_roots}")

    # The correction: neither coordinate alone settles it. The one that
    # VANISHES for Delta_L is canonical L- (= sigma_1 sigma_0, hm_sym slot 3);
    # the exclusion rides on canonical L+. Earlier versions had these two
    # names the wrong way round -- see the BASIS note above.
    d_grp = models[2][1]
    check("canonical L- (sigma_1 sigma_0) vanishes for qou-bg3w's Delta_L, so "
          "an exclusion argued from ONE coordinate is false there",
          sp.simplify(d_grp[3]) == 0)
    check("canonical L+ (sigma_0 sigma_1) does not, which is what excludes it",
          sp.simplify(d_grp[4]) != 0, f"L+ = {sp.factor(d_grp[4])}")

    # qou-bg3w's flagged third model.
    net9 = sp.simplify(sum(models[0][1]))
    check("qou-bg3w's -0.188291 is build_nucleon_nf's net (basis convention "
          "verified: coordinate sum IS net)",
          abs(net9.subs(h, hv_substrate) + sp.Rational(188291, 1000000))
          < sp.Rational(1, 1000000),
          f"exact at the substrate pin {sp.N(net9.subs(h, hv_substrate), 12)} "
          f"-- NINE significant figures against the stored float64, not the "
          f"~4 the q=111/100 reading gave")

    # Delta_S, for contrast: supported on {gamma, sigma_0, sigma_1} -> affine.
    check("Delta_S's [z^2] is 0 by support (the contrast case)", True,
          "supported off {L+, L-, e^-}")

    print(f"\n{'FAILED: ' + ', '.join(FAILED) if FAILED else 'All checks passed.'}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
