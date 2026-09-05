#!/usr/bin/env python3
"""`B = alpha L` cannot be a binding energy by way of the free-energy reading,
because that reading has **no energy spectrum** (`qou-qnqf`).

THE CLAIM UNDER TEST
--------------------
`rem:bond-log-ratio-is-a-free-energy` establishes that

    L = log(Z_free / Z_bonded) = sum_interfaces -log E_w[lambda + d_i]

is "a free-energy difference in the standard sense -- dimensionless, in units of
`kT`, per-interface additive", and records as OPEN the separate claim that
`B = alpha L` is the nuclear binding energy. The evidence already on the books is
three misses (the `A = 2` ordering, the absence of a valley of stability, the
`31 %` at `4He`). Misses are evidence about a formula; this probe asks the prior
question, about the reading itself.

A free energy is `F = -kT log Z` with `Z = sum_i exp(-E_i/kT)`. Every summand of
a partition function is a positive Boltzmann factor, and that positivity is not
decoration -- it is what makes `F` a Legendre transform, hence what gives it an
internal energy `U` and an entropy `S` at all. So the question is whether this
state sum has positive summands.

MEASURED: IT DOES NOT, FOR ANY BOND
-----------------------------------
The two `H_2` blocks carry `sigma`-eigenvalues `lambda_+ = q` and
`lambda_- = -q^-1`, so the per-block factors of
`tr_2(sigma + d) = w_+ (q + d) + w_- (-q^-1 + d)` are, at `q0`:

    bond        lambda_+ + d          lambda_- + d           z + d
    pp        1.10997858275138   **-0.90091828395574**   0.61268803714647
    pn        1.00552033498165   **-1.00537653172547**   0.50822978937674
    nn        0.90091828395574   **-1.10997858275138**   0.40362773835083

Every `lambda_- + d` is **negative**. The total is positive only because the
`(2)` block outweighs the `(1,1)` block; the sum is signed, not a partition
function.

AND NO LETTER THE ALGEBRA HAS REPAIRS IT, AT ANY q > 0
------------------------------------------------------
Positivity of the `(1,1)` summand needs `-q^-1 + d > 0`, i.e. `d > 1/q`. The
algebra's interface letters are `d in {0, -h/2, d_pn, -h}`, so `-h <= d <= 0`,
and `1/q > 0` for every `q > 0`. **The required offset is not merely outside the
available range -- it is on the other side of zero from all of it.** This is the
same shape as the arc's "no interface offset can close the gap" result, and it
holds for every `q`, not only at `q0`.

Hence there is no real `E_-` with `exp(-E_-) = lambda_- + d`: `exp` is positive
and `lambda_- + d` is not. **The `(1,1)` block has no energy.**

WHAT FOLLOWS
------------
`L` remains exactly what the block says it is -- a real, exactly computable,
convention-D-canonical quantity, and every one of the 80 files computing it
stands. What does not follow is the next sentence. Without positive summands
there is no Legendre structure, so there is no `U` and no `S` for `alpha L` to be
or to differ from, and "the free energy is the binding energy" has no step to
make. The free-energy reading does not supply the identification; it was never
going to, and the three measured misses are downstream of that.

The block already records the signedness ("a free energy of a signed observable
over a quasi-probability, not of a positive one"). This probe draws the
consequence the block stops short of: a quasi-probability free energy is not a
thermodynamic potential.

A CONDITIONAL COROLLARY, AND ITS OWN OBJECTION
-----------------------------------------------
If one grants the reading anyway and asks what temperature it runs at, the only
candidate is `alpha` itself -- `L` is dimensionless "in units of `kT`" and
`B = alpha L`, so `kT = alpha`. Applying Gibbs-Helmholtz `U = F - T dF/dT` along
the `q`-curve then gives

    atom     F = alpha L      U (internal)        T S        U/F
    2H          2.833163         -0.118006  -2.951168    -0.0417
    3H          6.630946          0.675955  -5.954990     0.1019
    3He         4.883872         -0.833502  -5.717374    -0.1707
    4He         8.681655         -0.039541  -8.721196    -0.0046

i.e. essentially all of it is `-TS` and the internal energy is roughly zero.
**The objection to this is mine, and it is real:** varying `q` changes the block
eigenvalues as well as the scale, so `q` is not a pure temperature and
Gibbs-Helmholtz along that curve is not the textbook identity. This section is
therefore indicative and NOT the finding; the finding is the missing spectrum
above, which needs no temperature at all.

A DETAIL WORTH KEEPING
----------------------
For the `pn` bond the two block factors nearly cancel:
`1.00552033498165` against `-1.00537653172547`, summing to
`(lambda_+ + d) + (lambda_- + d) = h + 2 d_pn = h * delta / 2 =
1.4380325618674e-4` exactly. So the `pn` interface -- the one the binding arc
turns on -- is the near-null vector of the unweighted block sum, and survives in
`z + d` only because `w_+ != w_-`.

**Definitional, not structural — an earlier note of mine overstated it.**
`d_pn = -h(1 - delta/2)/2 = -h/2 + h*delta/4` is BY CONSTRUCTION the average of
the `pp` offset `0` and the `nn` offset `-h`, so `h + 2 d_pn` is forced to equal
`h*delta/2` and would vanish exactly at the colour-blind `-h/2`. And the `w~`
family the nuclear-jet level uses (`qou-gpb5`) is **uniform on `H_2`**, because
both blocks there are one-dimensional (`d_q = 1`) -- so "null vector of `w~`" and
"null vector of the unweighted sum" are the SAME statement on two strands. I
called these "two different weight families, one distinguished letter"; they are
one family and one letter, and the near-cancellation is the definition of an
average read through a measure that is uniform only here. `w~` is NOT uniform at
`H_3` (`0.1634`, `0.6607`, `0.1634`) or `H_4`, so nothing generalises. Measured
in §5.

WHAT IS NOT CLAIMED
-------------------
No retraction of `L`, of any number computed from it, or of the free-energy
*description* -- signed free energies over quasi-probabilities are legitimate
objects and the block names this one correctly. No claim that binding is
unreachable in the framework, only that this reading does not reach it. Nothing
about the Reeb-flow or Wigner channels, which are separate. And no new binding
formula: this probe removes a candidate justification, it does not supply one.
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

TOL = mpfr("1e-45")
Q, H = E.Q, E.H
BONDS = (("pp", E.ZERO), ("pn", E.D_PN), ("nn", -E.H))


def s(v, n=20):
    """Decimal string with the point placed. `gmpy2.digits` returns a bare
    mantissa, which cannot be read for magnitude."""
    m, e, _ = gmpy2.digits(mpfr(v), 10, n)
    neg = m.startswith("-")
    m = m.lstrip("-")
    body = ("0." + "0" * (-e) + m) if e <= 0 else (m[:e] + "." + m[e:])
    return ("-" if neg else "") + body


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR")

    _ps, (wp, wm) = E.weights(2)
    lam_p, lam_m = Q, -1 / Q

    print("\n" + "=" * 78)
    print("§1  THE STATE SUM'S PER-BLOCK FACTORS — ONE IS NEGATIVE FOR EVERY BOND")
    print("=" * 78)
    print(f"    w_+ = {s(wp)}   lambda_+ = {s(lam_p)}")
    print(f"    w_- = {s(wm)}   lambda_- = {s(lam_m)}   (w_+ + w_- = "
          f"{s(wp + wm, 6)})")
    print(f"\n    {'bond':>5} {'lambda_+ + d':>24} {'lambda_- + d':>24} {'z + d':>22}")
    all_neg, all_tot_pos = True, True
    for nm, d in BONDS:
        fp, fm = lam_p + d, lam_m + d
        tot = wp * fp + wm * fm
        all_neg &= (fm < 0)
        all_tot_pos &= (tot > 0)
        print(f"    {nm:>5} {s(fp):>24} {s(fm):>24} {s(tot):>22}")
    check("the (1,1) block's factor lambda_- + d is NEGATIVE for every bond — "
          "the state sum is signed, not a partition function", all_neg)
    check("while the total z + d is positive for every bond, so L is real — the "
          "positive block simply outweighs the negative one", all_tot_pos)

    print("\n" + "=" * 78)
    print("§2  NO LETTER THE ALGEBRA HAS REPAIRS IT, AT ANY q > 0")
    print("=" * 78)
    print(f"    positivity of the (1,1) summand needs  d > 1/q = {s(1 / Q)}")
    print(f"    the algebra's letters are d in [-h, 0] = [{s(-H, 12)}, 0]")
    print(f"    most positive available d = 0  ->  lambda_- + 0 = {s(lam_m)} < 0")
    ok_range = (mpfr(0) < 1 / Q) and (mpfr(0) - 1 / Q < 0)
    print("\n    and for other q, since d <= 0 always and 1/q > 0 always:")
    ok_all_q = True
    for qs in ("1.0001", "1.5", "3.0", "10.0", "100.0"):
        qv = mpfr(qs)
        best = -1 / qv                      # d = 0, the most positive letter
        ok_all_q &= (best < 0)
        print(f"      q = {qs:>8}   best lambda_- + d = {s(best, 12):>18}   < 0")
    check("the required offset d > 1/q lies on the OTHER SIDE OF ZERO from every "
          "letter the algebra has (all d <= 0)", ok_range)
    check("and that holds for every q > 0, not only at q0 — 1/q > 0 always, so "
          "no q rescues the sign", ok_all_q)

    print("\n" + "=" * 78)
    print("§3  HENCE NO REAL ENERGY: exp(-E) > 0 AND lambda_- + d < 0")
    print("=" * 78)
    ok_noE = True
    for nm, d in BONDS:
        fm = lam_m + d
        ok_noE &= (fm < 0)
        print(f"    {nm:>5}: exp(-E_-) = {s(fm)} has no real solution E_-")
    check("no real E_- satisfies exp(-E_-) = lambda_- + d, so the (1,1) block "
          "has no energy and the Legendre structure F = U - TS is absent",
          ok_noE)

    print("\n" + "=" * 78)
    print("§4  THE pn NEAR-CANCELLATION, EXACTLY")
    print("=" * 78)
    fp, fm = lam_p + E.D_PN, lam_m + E.D_PN
    ssum = fp + fm
    ident = H * E.DELTA / 2
    print(f"    (lambda_+ + d_pn) = {s(fp)}")
    print(f"    (lambda_- + d_pn) = {s(fm)}")
    print(f"    sum               = {s(ssum)}")
    print(f"    h * delta / 2     = {s(ident)}")
    check("(lambda_+ + d_pn) + (lambda_- + d_pn) = h + 2 d_pn = h*delta/2 exactly "
          "— the pn letter is the near-null vector of the UNWEIGHTED block sum, "
          "surviving in z + d only because w_+ != w_-",
          abs(ssum - ident) < TOL and abs(ssum) < mpfr("1e-3"))

    print("\n" + "=" * 78)
    print("§5  THAT NEAR-CANCELLATION IS DEFINITIONAL, AND H_2 ONLY")
    print("=" * 78)
    from hecke_characters import dim_q, partitions_of, qfac  # noqa: E402

    def _call(fn, *a):
        try:
            return fn(*a)
        except TypeError:
            return fn(*a[:-1])

    print("    (a) d_pn is the AVERAGE of the pp and nn offsets, by construction:")
    print(f"        d_pn        = {s(E.D_PN)}")
    print(f"        -h/2        = {s(-H / 2)}")
    print(f"        d_pn + h/2  = {s(E.D_PN + H / 2)}   = h*delta/4")
    ok_mid = abs((E.D_PN + H / 2) - H * E.DELTA / 4) < TOL
    print("    (b) w~ is UNIFORM on H_2 and on no larger tower level:")
    unif = {}
    for n in (2, 3, 4):
        fac = mpfr(str(_call(qfac, n, Q)))
        vals = set()
        for p in partitions_of(n):
            dq = mpfr(str(_call(dim_q, list(p), Q)))
            vals.add(s(dq * dq / fac, 12))
        unif[n] = (len(vals) == 1)
        print(f"        H_{n}: {len(vals)} distinct w~ value(s)  uniform = {unif[n]}")
    check("d_pn + h/2 = h*delta/4 exactly — the pn offset IS the average of the "
          "other two, so h + 2 d_pn = h*delta/2 is forced", ok_mid)
    check("w~ is uniform on H_2 but NOT on H_3 or H_4 — so 'pn is w~'s null "
          "vector' and 'pn is the unweighted sum's null vector' are one H_2 "
          "statement, not two families agreeing",
          unif[2] and not unif[3] and not unif[4])

    print("\n" + "=" * 78)
    print("§S  WHAT THIS SETTLES")
    print("=" * 78)
    print("  The free-energy reading cannot deliver `B = alpha L` as a binding")
    print("  energy, and the reason is prior to any of the three measured")
    print("  misses: the state sum has a negative summand, for every bond and")
    print("  every q > 0, so there is no energy spectrum behind it and no")
    print("  Legendre structure to supply a U or an S. L stays exactly what the")
    print("  block says — a signed free energy over a quasi-probability. What")
    print("  goes is the sentence after it. No number moves.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Asks the prior question behind rem:bond-log-ratio-is-a-free-energy's open "
            "claim that B = alpha L is the binding energy. A free energy is -kT log Z "
            "with Z a sum of POSITIVE Boltzmann factors, and that positivity is what "
            "makes F a Legendre transform with an internal energy and an entropy. "
            "Measured at 200 bits: the (1,1) block's factor lambda_- + d = -1/q + d is "
            "NEGATIVE for all three bonds (-0.900918283956, -1.005376531725, "
            "-1.109978582751), while the total z + d stays positive because the (2) "
            "block outweighs it. Positivity would need d > 1/q, and the algebra's "
            "letters satisfy -h <= d <= 0, so the required offset is on the other side "
            "of zero from all of them -- for every q > 0, since 1/q > 0 always. Hence no "
            "real E_- has exp(-E_-) = lambda_- + d, the (1,1) block has no energy, and "
            "there is no U or S for alpha L to be. L itself is untouched and no number "
            "moves; what fails is the identification. Also recorded: the pn factors "
            "nearly cancel, summing to h*delta/2 = 1.4380325618674e-4 exactly.")
        for nm, d in BONDS:
            wb.add_data(f"minus_block_factor_{nm}",
                        gmpy2.digits(lam_m + d, 10, 25)[0])
            wb.add_data(f"total_factor_{nm}",
                        gmpy2.digits(wp * (lam_p + d) + wm * (lam_m + d), 10, 25)[0])
        wb.add_data("pn_block_sum_eq_h_delta_over_2", gmpy2.digits(ssum, 10, 25)[0])
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Nothing is retracted. L remains a correct, exactly computable, convention-D "
            "canonical quantity in all 80 files that compute it; the free-energy "
            "DESCRIPTION is also correct, since signed free energies over "
            "quasi-probabilities are legitimate objects.")
        wb.add_caveat(
            "The Gibbs-Helmholtz corollary in the docstring (U ~ 0 if one grants "
            "kT = alpha) is INDICATIVE ONLY and is not asserted here: varying q changes "
            "the block eigenvalues as well as the scale, so q is not a pure temperature. "
            "The finding needs no temperature.")
        wb.add_caveat(
            "No new binding formula. This removes a candidate justification; it does not "
            "supply one, and says nothing about the Reeb-flow or Wigner channels.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
