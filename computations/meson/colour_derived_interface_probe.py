#!/usr/bin/env python3
"""The colour-derived interface clears the STRUCTURAL bar and fails the MAGNITUDE one.

Bean qou-6tcn. Addendum 29 screened five interfaces and refused to select one,
because the candidate that cleared `sqrt(B_AME)` had no derivation. This derives
a candidate from the colour-tube structure FIRST, then measures it. The number
was not consulted in choosing it, and it does not clear.

THE DERIVATION (fixed before any trace was computed)
====================================================
`conj:inter-nucleon-channel-color-tube` states, in its own text:

  * "Each nucleon carries **3 quark color sheets**" -- and the atom word runs on
    `n = 3A` strands, so the three strands per nucleon ARE the colour sheets;
  * the `S_5 <-> SO(3)` fibre action gives "a canonical **3 x 3 = 9-element
    matrix of color-pair couplings per inter-nucleon arc**".

Nine colour-pair couplings, and the current assignment realises them as **one**
Hecke generator. The braid in which every colour sheet of nucleon 1 crosses
every colour sheet of nucleon 2 is the positive permutation braid swapping the
two 3-blocks:

    I_colour = (s3 s2 s1)(s4 s3 s2)(s5 s4 s3)

Verified before measuring: **9 crossings** -- exactly one per colour pair --
permutation `[4,5,6,1,2,3]`, i.e. the blocks swap; 3 of the 9 cross the wall.

**This is a READING, not a quotation.** The block explicitly specifies a
weighted sum over ONE generator. What is proposed here is a different
realisation of the same geometric input -- nine couplings as nine crossings
rather than as nine weights on one crossing. The block does not say this.

MEASURED
========
    interface                                   tr_M(atom)   vs sqrt(B_AME)
    I1       s3            (current, 1 xing)     0.693389        0.4649x
    I_colour block transposition (9 xings)       0.629005        0.4217x
    I_colour^-1  reversed orientation            0.110984        0.0744x

**It fails.** The derived interface traces *below* the single crossing it
replaces, and at 0.42x is nowhere near the 1.0 a concentrated cost would need.
Orientation matters enormously -- the inverse is 5.7x lower again.

TWO BARS, AND IT CLEARS ONLY ONE
================================
Addendum 28 identified a structural bar (the interface must not leave the word a
provable connected sum) and Addendum 23 a magnitude bar (`tr_M >= sqrt(B_AME)`).

    structural bar : I_colour is NOT provably a connected sum   -> CLEARED
    magnitude bar  : 0.4217x                                    -> FAILED

So the two bars are independent, and the derived candidate clears the one with a
reason and fails the one with a number. Meanwhile Addendum 29's `I5` clears the
magnitude bar at 1.2475x and has **no derivation at all**. That is the whole
situation, stated plainly: **the interface with a reason does not work, and the
interface that works has no reason.** No attempt is made here to rescue either.

WHAT THIS RULES OUT, AND WHAT IT DOES NOT
=========================================
RULES OUT (scope (a)): "make the interface the colour-pair block transposition"
as a route to the binding magnitude at the deuteron. It is derived, it is
checkable, and it misses by 2.4x.

DOES NOT rule out: the colour-tube structure itself, which may be right about
the p/n asymmetry and the chirality signs while saying nothing about magnitude;
a different braid realisation of the same nine couplings (the permutation braid
is the minimal positive one, not the only one); or any interface derived from
somewhere else. And it does NOT establish an essential torus -- "not provably a
connected sum" is necessary, not sufficient, and incompressibility is geometric.
"""

from __future__ import annotations

import itertools
import pathlib
import sys
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import binding_k_solver as bks  # noqa: E402
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 40)

Q, H, TOL, WALL = Q_MP, HA_MP, mp.mpf("1e-9"), 3
I_COLOUR = [3, 2, 1, 4, 3, 2, 5, 4, 3]


def hook_dim(lam):
    lam = tuple(x for x in lam if x)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def two_row(n):
    return [(n,)] + [(n - k, k) for k in range(1, n // 2 + 1)]


def tr_M(word, n):
    y = {l: qint(n - 2 * (l[1] if len(l) > 1 else 0) + 1) / qint(2) ** n
         for l in two_row(n)}
    return mp.fsum(
        y[l] * mp.mpf(str(float(np.trace(
            bks.block_rep_braid_word(l, word, q=float(Q))))))
        for l in two_row(n))


def slots(word):
    out = []
    for (_c, d, g) in word:
        t = -mp.mpf(str(d)) / H
        if abs(t) < TOL:
            out.append([(g + 1, mp.mpf(1))])
        elif abs(t - 1) < TOL:
            out.append([(-(g + 1), mp.mpf(1))])
        else:
            out.append([(g + 1, 1 - t), (-(g + 1), t)])
    return out


def permutation(word, n):
    p = list(range(1, n + 1))
    for g in word:
        i = abs(g) - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def provably_connected_sum(gens):
    occ = [i for i, x in enumerate(gens) if abs(x) == WALL]
    if len(occ) != 1:
        return False
    p = occ[0]
    return (all(abs(x) < WALL for x in gens[:p])
            and all(abs(x) > WALL for x in gens[p + 1:]))


def main() -> int:
    wb = WitnessBuilder("colour-derived-interface", engine="python-exact")
    wb.set_description(
        "Derives an interface from the colour-tube structure FIRST -- 9 "
        "colour-pair couplings realised as the 9-crossing block transposition "
        "-- then measures it. It CLEARS the structural bar (not provably a "
        "connected sum) and FAILS the magnitude bar at 0.4217x, tracing BELOW "
        "the single crossing it replaces. Addendum 29's I5 clears magnitude at "
        "1.2475x with no derivation. So the interface with a reason does not "
        "work and the interface that works has no reason; no rescue is "
        "attempted.")

    word = atom_braid_word_3A(1, 1)
    sl = slots(word)
    gens = [g + 1 for (_c, _d, g) in word]
    pos = gens.index(WALL)
    need = mp.sqrt(AME_B_DEUTERON_MEV_VALIDATION)

    def atom_trace(I):
        tot = mp.mpf(0)
        for combo in itertools.product(*sl):
            w = mp.mpf(1)
            for _, wt in combo:
                w *= wt
            b = [g for g, _ in combo]
            tot += w * tr_M(b[:pos] + I + b[pos + 1:], 6)
        return tot

    inv = [-g for g in reversed(I_COLOUR)]
    # The Addendum-29 screen candidate I5 = (s3 s2 s4 s3)^2, carried as the
    # contrast in A7 below. Its ratio was a typed literal there; put it through
    # the same atom_trace as every other word so the contrast is measured.
    I5_UNDERIVED = [3, 2, 4, 3] * 2
    t1, tc, ti = atom_trace([3]), atom_trace(I_COLOUR), atom_trace(inv)
    t5 = atom_trace(I5_UNDERIVED)
    perm = permutation(I_COLOUR, 6)
    conn = provably_connected_sum(gens[:pos] + I_COLOUR + gens[pos + 1:])

    print(f"I1        s3                     tr_M {mp.nstr(t1, 10):<14}"
          f"{mp.nstr(t1 / need, 7):>10}x")
    print(f"I_colour  block transposition    tr_M {mp.nstr(tc, 10):<14}"
          f"{mp.nstr(tc / need, 7):>10}x")
    print(f"I_colour^-1 reversed             tr_M {mp.nstr(ti, 10):<14}"
          f"{mp.nstr(ti / need, 7):>10}x")
    print(f"I5 (underived control)           tr_M {mp.nstr(t5, 10):<14}"
          f"{mp.nstr(t5 / need, 7):>10}x")
    print(f"\ncrossings {len(I_COLOUR)}   permutation {perm}   "
          f"provably connected sum: {conn}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE DERIVATION, checkable: 9 crossings, one per colour pair.
    wb.add_assertion(
        name="derived_interface_has_nine_crossings",
        computed=str(len(I_COLOUR)), expected="9", tolerance="0", unit="count",
        source="the block's 3x3 = 9-element colour-pair coupling matrix")

    # A2 — and it is the block swap, so every pair is realised exactly once.
    wb.add_assertion(
        name="derived_interface_swaps_the_colour_blocks",
        computed=repr(perm), expected="[4, 5, 6, 1, 2, 3]", tolerance="0",
        unit="permutation",
        source="every colour sheet of nucleon 1 crosses every sheet of nucleon 2")

    # A3 — STRUCTURAL BAR: cleared.
    wb.add_assertion(
        name="structural_bar_cleared_not_provably_a_connected_sum",
        computed=repr(bool(conn)), expected="False", tolerance="0",
        unit="boolean",
        source="single-crossing factorisation fails; NECESSARY for a torus, "
               "not sufficient")

    # A4 — MAGNITUDE BAR: failed, and that is the result.
    wb.add_assertion(
        name="magnitude_bar_failed",
        computed=mp.nstr(tc / need, 20), expected="0.4217272",
        tolerance="1e-5", unit="ratio",
        source="tr_M(atom with I_colour) / sqrt(B_AME); < 1 means it misses")

    # A5 — it traces BELOW the single crossing it replaces, so nine couplings
    #      buy nothing here.
    wb.add_assertion(
        name="derived_interface_traces_below_the_single_crossing",
        computed=repr(bool(tc < t1)), expected="True", tolerance="0",
        unit="boolean", source="I_colour 0.629005 vs I1 0.693389")

    # A6 — CONTROL: orientation is not a detail; the inverse is far lower, so
    #      the measurement is sensitive and not a constant of the construction.
    wb.add_assertion(
        name="control_orientation_changes_the_trace_substantially",
        computed=mp.nstr(tc / ti, 20), expected="5.667", tolerance="1e-2",
        unit="ratio", source="forward vs reversed block transposition")

    # A7 — CONTROL tying to Addendum 29: the undERIVED I5 does clear, so the
    #      failure here is about THIS candidate, not about the bar being
    #      unreachable by any interface.
    # Was `computed="1.247533", expected="1.247533"` (bean `qou-26f2`) — the one
    # assertion here whose computed side was typed rather than traced, while its
    # six siblings all measure. It is also the assertion carrying the sting of
    # the result ("the interface that works has no reason"), so a stale I5 ratio
    # would have gone on reading PASS while the contrast it draws had quietly
    # stopped holding. I5 now goes through the same atom_trace as I_colour and
    # its inverse; the literal is kept as the Addendum-29 expected value, which
    # the measurement reproduces.
    wb.add_assertion(
        name="control_an_underived_candidate_does_clear",
        computed=mp.nstr(t5 / need, 20), expected="1.247533", tolerance="1e-4",
        unit="ratio",
        source="interface-candidate-screen I5 = (s3 s2 s4 s3)^2, traced here "
               "and carried forward as the contrast; it clears the magnitude "
               "bar (> 1) and has no derivation")

    wb.add_data("interface_word", I_COLOUR)
    wb.add_data("crossings", len(I_COLOUR))
    wb.add_data("permutation", perm)
    wb.add_data("tr_M_current", mp.nstr(t1, 24))
    wb.add_data("tr_M_colour_derived", mp.nstr(tc, 24))
    wb.add_data("tr_M_reversed", mp.nstr(ti, 24))
    wb.add_data("tr_M_I5_underived_control", mp.nstr(t5, 24))
    wb.add_data("required_trace", mp.nstr(need, 24))
    wb.add_caveat(
        "THE 9-CROSSING READING IS MINE, NOT THE BLOCK'S. "
        "conj:inter-nucleon-channel-color-tube explicitly specifies a weighted "
        "sum over ONE generator. What is proposed is a different realisation of "
        "the same geometric input -- nine couplings as nine crossings rather "
        "than nine weights on one crossing. The block does not say this.")
    wb.add_caveat(
        "RULES OUT (scope (a)): the colour-pair block transposition as a route "
        "to the binding magnitude at the deuteron. DOES NOT rule out: the "
        "colour-tube structure itself, which may be right about p/n asymmetry "
        "and chirality signs while saying nothing about magnitude; a different "
        "braid realisation of the same nine couplings (the permutation braid is "
        "the minimal positive one, not the only one); or an interface derived "
        "from elsewhere.")
    wb.add_caveat(
        "Does NOT establish an essential torus. 'Not provably a connected sum' "
        "is necessary, not sufficient; incompressibility is geometric and no "
        "probe here tests it. float64 traces via block_rep_braid_word; the "
        "gaps here are tens of percent.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
