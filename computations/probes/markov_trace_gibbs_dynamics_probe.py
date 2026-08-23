#!/usr/bin/env python3
"""Probe — what dynamics would make the Markov trace a Gibbs state? None, on the
full algebra: the state is not faithful.

Opened from beans qou-unqc and qou-892m, which came out of the literature check
on the binding law's interpretation block (#5320). That block asserted the
Markov trace "forms a temperature (Gibbs-type) state in the operator-algebraic
sense", citing jones1987 -- a knot-polynomial paper that does not say so, and
the library holds no source that does. #5320 scoped the claim to an analogy.
This probe asks the mathematical question the scoping left open.

## The reconstruction, and where it dies

`H_n(q)` is semisimple, so it splits as `+_lambda M_{d_lambda}(C)`. A tracial
state is `omega(A) = sum_lambda p_lambda * tr_lambda(A) / d_lambda`. For that to
be `Tr(e^{-beta H} A) / Z`, the operator `e^{-beta H}` must be a SCALAR on each
block -- so `H` is central, `H = sum_lambda E_lambda P_lambda`, and

    p_lambda / d_lambda  ~  exp(-beta E_lambda).

With `tr_M = sum_lambda y_lambda chi^lambda` and `chi^lambda(1) = d_lambda`, the
normalisation `tr_M(1) = 1` reads `sum_lambda y_lambda d_lambda = 1` (verified
below, exactly, at n = 3, 4, 6). So `p_lambda = y_lambda d_lambda`, and

    E_lambda = -(1/beta) log y_lambda + const.

**This requires y_lambda > 0.** A Gibbs state of a FINITE Hamiltonian is
faithful -- `exp(-beta E)` is never zero. Measured at the substrate anchor:
no `y_lambda` is negative, but many are EXACTLY zero, and they are exactly the
partitions with three or more rows (the level-2 Wenzl restriction). At n = 6,
seven of eleven blocks are annihilated.

So the Markov trace is **not** the Gibbs state of any finite Hamiltonian on
`H_n(q)`. Representing it needs `E_lambda = +infinity` on the vanishing blocks
-- a limit of Gibbs states, not a Gibbs state. That is the concrete form of the
objection #5320 recorded abstractly (a tracial state has trivial modular
dynamics, i.e. KMS at beta = 0).

## What survives, and it is not nothing

Restricted to its SUPPORT -- the at-most-two-row blocks -- the trace is
faithful and the reconstruction goes through. There `E_lambda = -E_0 log
y_lambda` is well defined, and the numbers are nuclear-scale.

**The binding law is this level assignment.** `B = -E_0 log mu` is not an
independent postulate sitting beside a thermodynamic analogy: it is exactly
`E_lambda = -E_0 log y_lambda` evaluated on the interface channel. The
"free-energy difference" reading and the "level energy" reading are the same
formula, which is why the law survived every attack on the analogy.

## The (beta, H) degeneracy -- qou-892m

Only the PRODUCT `beta * H` is determined by the state: rescaling
`beta -> c*beta`, `E_lambda -> E_lambda / c` leaves every `p_lambda` fixed.
So `kT = E_0` is a gauge choice fixing that split, not a derived temperature.
This is why the corpus can carry two different `kT` without a contradiction in
the mathematics -- and also why neither is a physical temperature:

    information-theory/boltzmann-constant.md   k_B T_phys = hbar_q = (q-1)/q
    mass-endomorphism/...gibbs-free-energy.md  kT = E_0

Both are admissible gauges for their own algebra; neither is forced. The defect
is presentational -- each block presents its choice as THE temperature -- and
the fix is to say which quantity is being held fixed, not to pick a winner.

## Scope

Scope-(b) on the full algebra, with the invariant named: a Gibbs state of a
finite Hamiltonian is faithful, and this state is not (7 of 11 blocks
annihilated at n = 6). Scope-(a) on the support: the reconstruction works
there, and nothing here says the support-restricted dynamics is unique or
physical -- only that it exists and that `E_lambda = -E_0 log y_lambda`.

NO FLOAT64: y_lambda from the exact mpmath closed form at the proton pin,
all arithmetic at 50 dps.

Beans qou-unqc, qou-892m.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR as Q50
from _precision import set_compute_dps  # noqa: E402

E0_STR = "4.1859813632944758969"


def main() -> int:
    set_compute_dps()
    with mp.workdps(60):
        q0 = +mp.mpf(str(Q50))
    E0 = mp.mpf(E0_STR)

    from schur_principal_mpmath import y_lambda_at_q0_mpmath as ylam
    from hecke_characters import partitions_of, standard_young_tableaux

    print("Would any dynamics make the Markov trace a Gibbs state?\n")
    print("  A tracial state on +_lam M_{d_lam}(C) is Gibbs for a CENTRAL H:")
    print("      p_lam / d_lam ~ exp(-beta E_lam),   p_lam = y_lam d_lam")
    print("  so   E_lam = -(1/beta) log y_lam + const,  requiring y_lam > 0.\n")

    verdict_rows = []
    for n in (3, 4, 6):
        y = ylam(n, q0)
        tot = mp.mpf(0)
        rows = []
        for lam in partitions_of(n):
            syts, _, _ = standard_young_tableaux(lam)
            d = len(syts)
            yl = y.get(tuple(lam))
            if yl is None:
                continue
            yl = mp.mpf(yl)
            tot += yl * d
            rows.append((tuple(lam), d, yl))
        zeros = [r for r in rows if r[2] == 0]
        negs = [r for r in rows if r[2] < 0]
        # the vanishing blocks are exactly the >=3-row partitions
        misfiled = [r for r in rows
                    if (len(r[0]) >= 3) != (r[2] == 0)]
        verdict_rows.append((n, len(rows), len(zeros), len(negs), tot, misfiled))

        print(f"n = {n}:  sum_lam y_lam d_lam = {mp.nstr(tot, 20)}"
              "   (normalisation, must be 1)")
        print(f"          blocks {len(rows)},  y_lam = 0 exactly: {len(zeros)},"
              f"  y_lam < 0: {len(negs)}")
        print(f"          vanishing blocks are exactly the >=3-row partitions:"
              f" {'YES' if not misfiled else 'NO -- ' + str(misfiled)}")
        for lam, d, yl in rows:
            if yl > 0:
                E = -E0 * mp.log(yl)
                print(f"            lam={str(lam):18s} d={d:3d}"
                      f"  y={mp.nstr(yl, 12):>16s}"
                      f"  E_lam = -E0 log y = {mp.nstr(E, 10):>12s} MeV")
        print()

    print("VERDICT\n")
    print("  SCOPE-(b), full algebra: the Markov trace is NOT the Gibbs state of")
    print("  any finite Hamiltonian. A Gibbs state exp(-beta H)/Z is FAITHFUL --")
    print("  exp of a finite number is never zero -- and this state annihilates")
    print("  7 of 11 blocks at n = 6. Representing it needs E_lam = +infinity on")
    print("  the vanishing blocks: a LIMIT of Gibbs states, not a Gibbs state.\n")
    print("  SCOPE-(a), on the support (the <=2-row blocks): the reconstruction")
    print("  goes through, and E_lam = -E_0 log y_lam. THE BINDING LAW IS THIS")
    print("  ASSIGNMENT -- B = -E_0 log mu is that formula on the interface")
    print("  channel, not an independent postulate beside a thermodynamic")
    print("  analogy. Which is why the law outlived every attack on the analogy.\n")
    print("  (beta, H) DEGENERACY: only the product beta*H is fixed by the state")
    print("  (beta -> c beta, E -> E/c leaves every p_lam invariant). So kT = E_0")
    print("  is a GAUGE CHOICE, and so is k_B T_phys = hbar_q in the")
    print("  information-theory chapter. Neither is derived; the defect is that")
    print("  each block presents its own choice as THE temperature.\n")

    # ---- guards ---------------------------------------------------------
    for n, nb, nz, nn, tot, misfiled in verdict_rows:
        assert abs(tot - 1) < mp.mpf("1e-40"), f"n={n}: y_lam d_lam != 1"
        assert nn == 0, f"n={n}: a NEGATIVE y_lam would break positivity too"
        assert not misfiled, f"n={n}: vanishing set is not the >=3-row set"
    n6 = [r for r in verdict_rows if r[0] == 6][0]
    assert n6[2] == 7 and n6[1] == 11, "n=6 should annihilate 7 of 11 blocks"
    print("(no witness by design — exact y_lambda at the anchor plus one")
    print(" faithfulness argument; the tables reproduce every number.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
