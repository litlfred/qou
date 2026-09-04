#!/usr/bin/env python3
"""There is no within-generator non-commutativity: every crossing at one
generator is a polynomial in the same `S`, and polynomials in one matrix commute.
The question `qou-jebr` was opened to settle is empty. What IS true, and is a
different thing, is that the readout is not MULTIPLICATIVE within a generator —
non-multiplicative is not non-commutative, and it still cannot produce a
quadratic in `N - Z`.

WHERE THIS SITS
---------------
Bean `qou-jebr`, opened to clean up after a retracted test. In
`docs/audits/2026-09-04-graded-scales-are-per-partition-not-per-type.md` I ran a
matrix version of the type-two test, got an exciting answer (the logarithm
appeared NOT to kill the `(N-Z)^2` term), and only then checked the transfer
matrix against a known value. It failed: my readout gave `1.128089` at `q_0`
where the proved single-crossing bond factor is `z = 0.612688`. Retracted.

The residue was a narrower question I had not actually tested: the corpus
multiplies transfer matrices WITHIN a generator and takes a scalar product
ACROSS generators, so could non-commutativity inside a generator carry a
quadratic?

THE CONVENTION, PINNED FIRST THIS TIME
--------------------------------------
`ground_state_ordering_convention_independence_probe` states it:
`M = alpha*1 + beta*S` with `S = [[h, 1], [1, 0]]`, `h = q - 1/q`, and the
readout is

    Vhat = z * M[1][0] + M[1][1] = z*beta + alpha.

Check before use: a single crossing is the Hecke element `sigma + d`, i.e.
`M = S + d*1`, so `alpha = d`, `beta = 1`, and `Vhat = z + d` — exactly the bond
factor `qou-m3sh` proved and `QOU.Mass.ChainTraceFactor.twoStrandTrace_eq`
formalises. The convention is confirmed against a known value BEFORE anything is
built on it, which is the step whose omission produced the retraction.

The readout I used in the retracted test, `z*M[0,0] + M[1,0]`, is the one in
`computations/_deprecated/transfer_matrix_symbolic.py` — deprecated, and it does
not reproduce `z + d`.

THE ANSWER: THE QUESTION IS EMPTY
---------------------------------
`S` satisfies the Hecke quadratic `S^2 = h S + 1` exactly, and every crossing at
a given generator is `S + d` for some offset. Therefore

    [S + d1, S + d2] = 0   identically.

All crossings at one generator are polynomials in the same matrix and commute.
There is no within-generator non-commutativity to carry anything. `qou-jebr`
closes negative, structurally rather than numerically.

WHAT IS TRUE INSTEAD, AND WHY IT STILL DOES NOT HELP
----------------------------------------------------
The readout is **not multiplicative** within a generator:

    Vhat((S+d1)(S+d2)) - Vhat(S+d1)*Vhat(S+d2)  =  z*h - z^2 + 1
                                                =  (q^4 + q^2 + 1)/(q^2 + 1)^2

which is non-zero for every `q`. That is the Hecke relation folding `S^2` back
down to `alpha + beta S`; it is a real effect and it is easy to mistake for
non-commutativity. It is not: the factors commute, the readout is simply not a
ring homomorphism.

It still cannot produce a `(N-Z)^2` term, for a reason that has nothing to do
with either property. **In the canonical chain each interface generator carries
exactly one crossing** — the bond — so `M_i = S + d` and `Vhat_i = z + d` with
no within-generator combination happening at all. The generators that do carry
several crossings are the intra-nucleon ones (`3k`, `3k+1`), and those sit
inside a single nucleon, so their factor depends only on whether that nucleon is
a proton or a neutron. Summed, that is `Z * (p-factor) + N * (n-factor)`: linear
in the counts, never bilinear. Nothing in the within-generator structure ever
mixes two different nucleons, and a quadratic in `N - Z` needs exactly that.

So the last remnant of the type-two direction closes, and it closes for a
third independent reason, on top of the per-partition scales and the logarithm.

WHAT IS NOT CLAIMED
-------------------
Nothing about the all-pairs word, whose band generators DO span several
generators and genuinely fail to commute — that is `qou-bygw`, untouched and
still blocked. Nothing about whether `B = alpha L` is a binding energy
(`qou-qnqf`). This settles one narrow question that I created by testing the
wrong object.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402
import gmpy2  # noqa: E402

import _exact_trace_engine as E  # noqa: E402


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    q, z, d, d1, d2 = sp.symbols("q z d d1 d2")
    h = q - 1 / q
    S = sp.Matrix([[h, 1], [1, 0]])

    def vhat(M):
        return sp.simplify(z * M[1, 0] + M[1, 1])

    def vhat_deprecated(M):
        return sp.simplify(z * M[0, 0] + M[1, 0])

    print("\n" + "=" * 74)
    print("§1  PIN THE CONVENTION AGAINST A KNOWN VALUE — BEFORE USING IT")
    print("=" * 74)
    M1 = S + d * sp.eye(2)
    live = sp.expand(vhat(M1))
    dep = sp.expand(vhat_deprecated(M1))
    print(f"    live readout  z*M[1][0] + M[1][1] = {live}")
    print(f"    deprecated    z*M[0,0]  + M[1,0]  = {dep}")
    print(f"    proved bond factor (qou-m3sh, ChainTraceFactor.twoStrandTrace_eq) = z + d")
    check("the live readout reproduces the proved single-crossing bond factor z + d",
          sp.simplify(live - (z + d)) == 0)
    check("the deprecated readout does NOT — this is the error behind the retracted test",
          sp.simplify(dep - (z + d)) != 0)

    print("\n" + "=" * 74)
    print("§2  THE QUESTION IS EMPTY: NO WITHIN-GENERATOR NON-COMMUTATIVITY")
    print("=" * 74)
    hecke = sp.simplify(S * S - h * S - sp.eye(2))
    A, B = S + d1 * sp.eye(2), S + d2 * sp.eye(2)
    comm = sp.simplify(A * B - B * A)
    print(f"    Hecke quadratic  S^2 - hS - 1 = {hecke.tolist()}")
    print(f"    commutator  [S + d1, S + d2] = {comm.tolist()}")
    print("    every crossing at one generator is a polynomial in the SAME S,")
    print("    and polynomials in one matrix commute.")
    check("S satisfies the Hecke quadratic S^2 = hS + 1 exactly", hecke == sp.zeros(2, 2))
    check("crossings at a generator commute identically — there is no within-generator "
          "non-commutativity for anything to be carried by", comm == sp.zeros(2, 2))

    print("\n" + "=" * 74)
    print("§3  WHAT IS TRUE INSTEAD: NOT MULTIPLICATIVE (a different property)")
    print("=" * 74)
    defect = sp.simplify(sp.expand(vhat(sp.expand(A * B)) - (z + d1) * (z + d2)))
    zval = q ** 3 / (q ** 2 + 1)
    defect_at_z = sp.simplify(sp.factor(defect.subs(z, zval)))
    print(f"    Vhat(AB) - Vhat(A)Vhat(B) = {defect}")
    print(f"    at z = q^3/(q^2+1):        = {defect_at_z}")
    print("    non-zero for every q — the Hecke relation folding S^2 back to alpha + beta S.")
    print("    Easy to mistake for non-commutativity. It is not: the factors commute,")
    print("    the readout is simply not a ring homomorphism.")
    check("the readout is NOT multiplicative within a generator, and the defect is "
          "independent of d1, d2", sp.simplify(sp.diff(defect, d1)) == 0
          and sp.simplify(sp.diff(defect, d2)) == 0 and defect != 0)

    print("\n" + "=" * 74)
    print("§4  AND IT STILL CANNOT MAKE A QUADRATIC IN N - Z")
    print("=" * 74)
    from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
    ok_iface = True
    for Z, N, nm in ((2, 1, "3He"), (1, 2, "3H"), (2, 2, "4He"), (3, 3, "6Li")):
        w = atom_canonical_crossings(Z, N)
        per = {}
        for g, _k in w:
            per[g] = per.get(g, 0) + 1
        iface = {g: c for g, c in per.items() if g % 3 == 2}
        ok_iface &= all(c == 1 for c in iface.values())
        print(f"    {nm:5s} interface generators {sorted(iface)} carry "
              f"{sorted(set(iface.values()))} crossing(s) each")
    check("every INTERFACE generator carries exactly one crossing, so no "
          "within-generator combination happens on a bond at all", ok_iface)
    print("    the multi-crossing generators are the intra-nucleon ones (3k, 3k+1),")
    print("    which sit inside ONE nucleon, so their factor depends only on that")
    print("    nucleon's type. Summed that is Z*(p-factor) + N*(n-factor): LINEAR in")
    print("    the counts, never bilinear. Nothing within a generator ever mixes two")
    print("    different nucleons, and a quadratic in N - Z needs exactly that.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Closes qou-jebr negative. The corpus readout is Vhat = z*M[1][0] + M[1][1] "
            "with M = alpha + beta*S, S = [[h,1],[1,0]]; pinned against the proved "
            "single-crossing bond factor z + d before use, which is the step whose "
            "omission caused the earlier retraction (the deprecated readout "
            "z*M[0,0] + M[1,0] does not reproduce it). S satisfies S^2 = hS + 1, so every "
            "crossing at a generator is a polynomial in the same S and [S+d1, S+d2] = 0 "
            "identically: there is NO within-generator non-commutativity and the question "
            "is empty. What is true instead is that the readout is not multiplicative "
            "within a generator, defect z*h - z^2 + 1 = (q^4+q^2+1)/(q^2+1)^2, independent "
            "of the offsets — a different property, easy to confuse with the first. It "
            "still cannot make a quadratic in N-Z: every interface generator carries "
            "exactly one crossing, and the multi-crossing generators are intra-nucleon, so "
            "their contribution is linear in the counts and never mixes two nucleons.")
        wb.add_data("live_readout", "z*M[1][0] + M[1][1] = z*beta + alpha")
        wb.add_data("single_crossing_vhat", "z + d")
        wb.add_data("commutator", "0")
        wb.add_data("multiplicativity_defect_at_z", str(defect_at_z))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Says nothing about the all-pairs word, whose band generators span several "
            "generators and genuinely fail to commute — that is qou-bygw, untouched and "
            "still blocked on a modelling decision.")
        wb.add_caveat(
            "Says nothing about whether B = alpha L is a binding energy (qou-qnqf). This "
            "settles one narrow question created by testing the wrong object.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
