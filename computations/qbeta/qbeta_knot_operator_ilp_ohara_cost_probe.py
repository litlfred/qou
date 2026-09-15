#!/usr/bin/env python3
"""THE ILP, run as specified: which knot operator activates, costed by O'Hara.

## The program

    variables    x_K in {0,1}   for each knot operator K in the catalogue
    constraint   sum_K x_K = 1                 -- exactly one operator fires
                 reading-3 feasibility of the DRESSED element
    objective    min  sum_K x_K * E(K)

`x_K` is integral because a knot operator is indivisible: half a braid word is
not a knot operator, so the relaxation `x_K in [0,1]` has no physical meaning.
The catalogue is finite, so exhaustion IS the exact optimum -- there is no LP
relaxation here and nothing is rounded.

## 🛑 THIS PROBE EXISTS BECAUSE I GOT THE PROGRAM WRONG

`operator_selection_ilp_does_not_escape_s4.py` (same branch, committed
1ba7662fddf) tested whether the NF COORDINATE VECTOR of `B_3` is integral, and
concluded "integrality does not escape S4". **That is the wrong program.** Two
different programs live in this corpus and I conflated them:

    operator_selection_lattice_symbolic.py   universal-ilp.py
    -------------------------------------    -----------------------------
    variables: continuous x in R^6,          variables: WHICH braid word
      the NF coordinates                       (knot operator) fires
    feasible set: a POLYHEDRON                feasible set: a FINITE SET
      {G x >= 0, sum x = n}                     of words
    S4's relative-interior argument           S4 does NOT apply -- there is
      applies                                   no polyhedron to be interior to

The NF coordinates of a braid image are never required to be integers; what is
indivisible is the OPERATOR. So the earlier probe's two readings (`Z^6` and
`Z[q_0,q_0^-1]^6`) are both about the wrong space, and its density argument --
`Z[q_0,q_0^-1]` dense in `R` -- says nothing about `Z^N` in `R^N`, which is not
dense. **The conclusion "integrality does not escape S4" is RETRACTED.**

What survives from that file is its Lean, and read correctly it says the
OPPOSITE of what I concluded: `linear_min_two_sided_kills_direction` needs
feasible points on BOTH sides along a direction, and bounded integer
activations (`x_K in {0,1}`) are exactly what denies that. The theorem explains
why an activation ILP CAN select where the LP cannot.

## What is measured here

The incumbent cost is the word length. `QOU/Mass/GammaGammaWordSelection.lean`
defines the selection with `cost : W -> R` as a FREE PARAMETER -- a socket --
and every instantiation in the corpus fills it with `fun w => (w.length : R)`;
`universal-ilp.py` does the same ("Select minimum crossing number"), with
`min |tr_M|` as a tiebreaker. So:

  [A1] catalogue + both costs computed
  [A2] the COUNT cost cannot select: its argmin is a huge tie class, because a
       letter-sum is permutation-invariant (`LetterSumBlindness.lean`,
       sorry-free, scope-(b)). The `|tr_M|` tiebreaker is silently doing the
       real selection -- the stated objective picks only the LENGTH.
  [A3] the O'HARA cost breaks those ties, and by how much.
  [A4] reading-3 feasibility (owner ruling 2026-09-12, whole-word scope
       2026-09-13): chi_lambda >= 0 on every block with y_lambda > 0. Under
       convention D `y_(1^3) = 0`, so the binding blocks are `(3)` and `(2,1)`.
  [A5] the ILP optimum under each cost, on the feasible set.
  [A6] the mixed-length optimum, which is DEGENERATE at E = 0 for a structural
       reason: a pair kernel is empty on a 1-crossing operator.
  [A7] the fixed-length comparison -- the one the physics actually asks, and
       where the count is constant by definition.
  [A8] the cyclic invariance that makes [A7]'s orbit count legitimate.

## NO SELECTION BY ACCURACY

No Q_beta, no CODATA, no AME, no residual, no experimental number appears
anywhere in this file. The costs are computed and their tie structure is
reported; nothing is chosen because it lands a target. Which cost the framework
SHOULD use is the owner's design decision (stated: O'Hara, was Hecke energy) and
is not adjudicated here by comparing either one to data.

## Scope

Scope-(a). This measures whether each cost can discriminate at all, on a
catalogue of short operators. It does NOT claim the resulting minimiser is the
physical operator, and it does not extend the catalogue to the 11-letter
elements of `qou-99qc`.

Precision: mpmath 60 dps end to end, convention-D Markov root `z_D`. `float`
appears only inside f-strings. Emits no witness (bean qou-pb1w).

Beans qou-99qc, qou-uilp (universal-ilp.py aborts at Level 4).

-- Ref: [manuscript] computations/universal-ilp.py
-- Ref: [manuscript] computations/qbeta/qbeta_ecat_pair_kernel_probe.py
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/Mass/GammaGammaWordSelection.lean
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/QBeta/LetterSumBlindness.lean
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE, _HERE.parent, _HERE.parent / "substrate"):
    sys.path.insert(0, str(_p))

from _precision import set_compute_dps  # noqa: E402

import qbeta_ecat_block_cost_vector_probe as B  # noqa: E402

mp = B.mp
set_compute_dps(60)

Q0, H0, ZD = B.Q0, B.H0, B.ZD
SHAPES = B.SHAPES

#: The NF basis words, as generator-index tuples (0-based), from
#: `pyhecke.gram.NF_BASIS`. Carried explicitly so the character of an NF vector
#: is computed from the same basis the NF reduction uses.
NF_WORDS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]

#: The four knot-operator generators, as `(gen, d)` letters where the operator
#: is `sigma_gen + d*h*I`:  d = 0 is `sigma`, d = -1 is `sigma^-1`.
ALPHABET = [
    ("s0", (0, mp.mpf(0))),
    ("s1", (1, mp.mpf(0))),
    ("s0i", (0, mp.mpf(-1))),
    ("s1i", (1, mp.mpf(-1))),
]

MAX_LEN = 4

#: Working-precision tolerance. 🛑 NEVER compare ANYTHING here exactly --
#: not costs with `==`, and not characters with `>= 0`. This one root cause bit
#: THREE times while this probe was being written, each time looking like a
#: different bug:
#:   1. tie counting: `==` on costs split cyclic orbits that are genuinely tied
#:      (reported folds of 6 and 2 that were bitwise artifacts);
#:   2. [A8]: one sampled operator appeared to change FEASIBILITY under
#:      rotation, which is mathematically impossible (rotation is conjugation,
#:      chi_lambda is a class function);
#:   3. the cause of (2): `s0s1s1` has chi_(2,1) EXACTLY 0, computed as
#:      -5.1e-52 in two rotations and +7.8e-62 in the third, so `>= 0` flipped.
#: 12 of the 340 operators sit within this tolerance of a binding-block
#: boundary, so ~3.5% of the catalogue would otherwise be decided by rounding.
#: Reading 3 is `chi >= 0`, so an exact zero IS feasible and `>= -TIE_TOL` is
#: the faithful test, not a loosened one.
#:
#: 🛑 AND RAISING `mp.dps` CANNOT FIX ANY OF IT -- the limit is the ANCHOR, not
#: the arithmetic. `Q_50_DIGIT_STR` carries exactly 50 significant digits, and
#: `chi` responds to `q` at ORDER 1: perturbing `q` by a relative 1e-k moves
#: `chi` by about 2e-k (measured: 1e-50 -> 2.14e-50; 1e-52 -> a ~2e-52 shift;
#: 1e-60 -> no change to 12 digits). So `chi` is knowable to ~2e-50 whatever
#: the working precision.
#:
#: That is why the artifact is STABLE rather than shrinking: `chi_(2,1)` of two
#: rotations of `s0s1s1` sits at -5.11494191126e-52 unchanged from dps 60 to
#: 300, while the third rotation shrinks like 10^-dps (0.0, 7.8e-62, -1.2e-91,
#: -1.9e-121, -3.3e-201, -5.6e-301). The shrinking one is the honest zero; the
#: stable one is the exact value AT THE TRUNCATED q. Raising dps computes the
#: truncated-q answer more sharply, which is not the same as computing a better
#: answer. `TIE_TOL = 1e-50` is therefore the anchor's information content, not
#: a fudge factor -- and it is the floor for ANY order-1 function of q here.
#: Tie tolerance. 🛑 NEVER compare these costs with `==`. `E_ohara` is
#: cyclic-invariant as mathematics, but two rotations of one word accumulate
#: their pair sums in a different ORDER, so they differ by ~1e-61 at 60 dps.
#: Exact equality therefore SPLITS orbits that are genuinely tied, and the
#: first version of this probe reported fold counts (6 at length 3, 2 at
#: length 4) that were artifacts of bitwise equality rather than measurements
#: of the degeneracy. Measured spreads across rotations: 3.1e-61, 1.6e-61, 0.0.
TIE_TOL = mp.mpf("1e-50")

FAILURES: list[str] = []


def argmin_within_tol(vals: dict):
    """`(minimum, [labels within TIE_TOL of it])` — the honest tie class."""
    m = min(vals.values())
    return m, [lab for lab, v in vals.items() if abs(v - m) <= TIE_TOL]


def cyclic_orbit(labels):
    """Group word-labels into orbits under CYCLIC ROTATION.

    On a closed braid a rotation is a conjugation, so rotated words are the
    same knot operator — `tr_M` is a trace and `chi_lambda` is a class
    function, so both the cost and the reading-3 constraint are constant on an
    orbit — measured in [A8]. Counting orbits rather than words is therefore
    the right notion of "does this select".
    """
    seen, orbits = set(), []
    for lab in labels:
        if lab in seen:
            continue
        toks = _tokens(lab)
        orb = {"".join(toks[k:] + toks[:k]) for k in range(len(toks))}
        orb &= set(labels)
        seen |= orb
        orbits.append(sorted(orb))
    return orbits


def _tokens(label: str):
    """Split a concatenated label back into its letter tokens."""
    out, i = [], 0
    while i < len(label):
        for name, _ in sorted(ALPHABET, key=lambda a: -len(a[0])):
            if label.startswith(name, i):
                out.append(name)
                i += len(name)
                break
        else:                                   # pragma: no cover - guarded
            raise ValueError(f"unparseable label {label!r}")
    return out


def check(tag: str, ok: bool, msg: str) -> None:
    print(f"   [{tag}] {'PASS' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILURES.append(tag)


def cyclic_sep(i: int, j: int, L: int) -> int:
    """Arc separation on the CLOSED braid -- the closure is a circle."""
    d = abs(j - i)
    return min(d, L - d)


def tr_letters(letters):
    """Markov trace at the convention-D root, on a list of `(gen, d)` letters."""
    return B._order.tr_at(B._order.word_nf(list(letters)), ZD)


def e_ohara(letters):
    """O'HARA cost: the discretised `E_cat` pair kernel.

        E(w) = sum_{i<j} tr_M(w_i w_j) / d_arc(i,j)^2

    Every factor is read off `prop:mobius-energy` rather than chosen; see
    `qbeta_ecat_pair_kernel_probe.py`, which derives the discretisation and
    measures that the `1/d^2` weight is what breaks permutation ties.
    """
    L = len(letters)
    if L < 2:
        return mp.mpf(0)
    total = mp.mpf(0)
    for i in range(L):
        for j in range(i + 1, L):
            total += tr_letters([letters[i], letters[j]]) / mp.mpf(
                cyclic_sep(i, j, L)) ** 2
    return total


def e_count(letters):
    """INCUMBENT cost: the crossing count. What `universal-ilp.py` minimises
    and what every `GammaGammaWordSelection` instantiation puts in the socket.
    """
    return mp.mpf(len(letters))


def chi_of_nf(shape, nf):
    """`chi_lambda` of an element given by its NF coordinate vector.

    By linearity of the character over the NF basis -- so a word with non-braid
    letters (shifts) is handled by the NF reduction rather than by a 2^k
    expansion.
    """
    return mp.fsum(nf[i] * B.chi_braid(shape, [g + 1 for g in NF_WORDS[i]])
                   for i in range(6))


def reading3_feasible(nf, y):
    """Reading 3 (owner ruling 2026-09-12; whole-word scope 2026-09-13):
    `chi_lambda >= 0` on EVERY block whose Markov weight is positive.

    Under convention D `y_(1^3) = 0` -- that vanishing IS convention D -- so
    the alternating block is unconstrained and the binding blocks are `(3)` and
    `(2,1)`. Returns `(feasible, {shape: chi})`.
    """
    chis = {s: chi_of_nf(s, nf) for s in SHAPES}
    # `>= -TIE_TOL`, not `>= 0`: reading 3 admits chi = 0, and an exactly-zero
    # character lands at +-1e-61 here. See TIE_TOL for the three bugs this one
    # comparison caused.
    ok = all(chis[s] >= -TIE_TOL for s in SHAPES if y[s] > 0)
    return ok, chis


def main() -> int:
    y = B.y_lambda()

    print("=" * 78)
    print("[A1] THE CATALOGUE -- whole knot operators, nothing fractional")
    print("=" * 78)
    catalogue = []
    for n in range(1, MAX_LEN + 1):
        for combo in itertools.product(ALPHABET, repeat=n):
            label = "".join(c[0] for c in combo)
            letters = [c[1] for c in combo]
            catalogue.append((label, letters))
    print(f"   alphabet          : {[a[0] for a in ALPHABET]}"
          f"   (s0i = sigma_0^-1 = sigma_0 - h*I)")
    print(f"   lengths           : 1 .. {MAX_LEN}")
    print(f"   |catalogue|       : {len(catalogue)} operators")
    print(f"   binding blocks    : {[s for s in SHAPES if y[s] > 0]}"
          f"   (y_(1,1,1) = 0 IS convention D)")
    check("A1", len(catalogue) == sum(4 ** n for n in range(1, MAX_LEN + 1)),
          f"catalogue is the full 0/1 activation domain, {len(catalogue)} operators")

    print()
    print("=" * 78)
    print("[A2] THE INCUMBENT COST CANNOT SELECT -- its argmin is a tie class")
    print("=" * 78)
    counts = {lab: e_count(w) for lab, w in catalogue}
    cmin = min(counts.values())
    ctied = [lab for lab, v in counts.items() if v == cmin]
    by_len = Counter(len(w) for _, w in catalogue)
    print(f"   min crossing count            : {int(cmin)}")
    print(f"   operators attaining it        : {len(ctied)}   {ctied}")
    print(f"   tie-class size by length      : "
          f"{ {k: by_len[k] for k in sorted(by_len)} }")
    print("   Every operator of a given length is TIED, because the crossing")
    print("   count is a letter-sum and a letter-sum is permutation-invariant")
    print("   (LetterSumBlindness.lean, sorry-free, scope-(b)). So the stated")
    print("   objective selects only the LENGTH; universal-ilp.py's")
    print("   `min |tr_M|` tiebreaker is doing the real operator selection.")
    check("A2", len(ctied) > 1,
          f"the count cost ties {len(ctied)} distinct operators at its optimum "
          f"-- it cannot select one")

    print()
    print("=" * 78)
    print("[A3] THE O'HARA COST BREAKS THOSE TIES")
    print("=" * 78)
    ohara = {lab: e_ohara(w) for lab, w in catalogue}
    # within each count-tie class, how many distinct O'Hara values?
    print(f"   {'length':>7} {'operators':>10} {'distinct E_ohara':>18}"
          f" {'distinct E_count':>18}")
    all_broken = True
    for n in sorted(by_len):
        labs = [lab for lab, w in catalogue if len(w) == n]
        vals = {mp.nstr(ohara[lab], 30) for lab in labs}
        note = "  <- no pairs: E = 0 by construction" if n == 1 else ""
        print(f"   {n:>7} {len(labs):>10} {len(vals):>18} {1:>18}{note}")
        if n >= 2 and len(labs) > 1 and len(vals) <= 1:
            all_broken = False
    print()
    print("   Length 1 is EXCLUDED from the claim, and not as a convenience:")
    print("   a pair kernel sums over pairs, and a 1-letter word has none, so")
    print("   E = 0 identically there. That is a real property of the cost and")
    print("   it comes back as the degeneracy in [A6].")
    check("A3", all_broken and len(ctied) > 1,
          "at every length >= 2 the O'Hara cost takes several distinct values "
          "(6, 8, 24) where the count takes exactly one -- the tie the "
          "incumbent cannot break is broken by the separation weight")

    print()
    print("=" * 78)
    print("[A4] READING-3 FEASIBILITY -- the ILP's constraint")
    print("=" * 78)
    feasible = []
    for lab, w in catalogue:
        nf = B._order.word_nf(list(w))
        ok, chis = reading3_feasible(nf, y)
        if ok:
            feasible.append((lab, w, chis))
    marginal = 0
    for lab, w in catalogue:
        _, ch = reading3_feasible(B._order.word_nf(list(w)), y)
        if any(abs(ch[s]) <= TIE_TOL for s in SHAPES if y[s] > 0):
            marginal += 1
    print(f"   feasible operators : {len(feasible)} of {len(catalogue)}")
    print(f"   ON THE BOUNDARY    : {marginal}  (|chi| <= {mp.nstr(TIE_TOL, 3)} "
          f"on a binding block)")
    print("   Those are exact zeros, feasible under reading 3's `chi >= 0`.")
    print("   Testing `>= 0` literally would decide them by rounding sign.")
    print(f"   {'operator':>10} {'chi_(3)':>22} {'chi_(2,1)':>22}")
    for lab, w, chis in feasible[:8]:
        print(f"   {lab:>10} {mp.nstr(chis[(3,)], 16):>22}"
              f" {mp.nstr(chis[(2, 1)], 16):>22}")
    if len(feasible) > 8:
        print(f"   ... and {len(feasible) - 8} more")
    check("A4", 0 < len(feasible) < len(catalogue),
          f"the constraint is non-trivial: it admits {len(feasible)} and "
          f"rejects {len(catalogue) - len(feasible)}")

    print()
    print("=" * 78)
    print("[A5] THE ILP OPTIMUM UNDER EACH COST")
    print("=" * 78)
    if not feasible:
        check("A5", False, "no feasible operator -- nothing to optimise")
    else:
        fc = {lab: counts[lab] for lab, _, _ in feasible}
        fo = {lab: ohara[lab] for lab, _, _ in feasible}
        c_opt, c_arg = argmin_within_tol(fc)
        o_opt, o_arg = argmin_within_tol(fo)
        print(f"   COUNT  : optimum {int(c_opt)}   attained by {len(c_arg)}"
              f" operator(s)  {c_arg[:8]}")
        print(f"   O'HARA : optimum {mp.nstr(o_opt, 22)}   attained by "
              f"{len(o_arg)} operator(s)  {o_arg}")
        check("A5", True,
              f"count optimum is {len(c_arg)}-fold, O'Hara optimum is "
              f"{len(o_arg)}-fold")

        print()
        print("=" * 78)
        print("[A6] CAN THE PROGRAM SELECT? -- uniqueness of the minimiser")
        print("=" * 78)
        print(f"   under the COUNT cost  : {len(c_arg)}-fold  -> "
              f"{'SELECTS' if len(c_arg) == 1 else 'DOES NOT SELECT'}")
        print(f"   under the O'HARA cost : {len(o_arg)}-fold  -> "
              f"{'SELECTS' if len(o_arg) == 1 else 'DOES NOT SELECT'}")
        print()
        print("   🛑 THE OPTIMUM IS AT E = 0, ON THE ZERO-PAIR OPERATORS, and")
        print("   that is a STRUCTURAL property of a pair kernel, not a")
        print("   numerical accident. A 1-crossing operator has no pairs, so")
        print("   its pair energy is identically 0; if any feasible operator")
        print("   has positive energy, the 1-letter ones win by construction.")
        print("   So `min E_ohara` over a MIXED-LENGTH catalogue degenerates")
        print("   to 'fire the shortest operator' for a trivial reason, and")
        print("   then ties s0 with s1 by the sigma_0 <-> sigma_1 symmetry of")
        print("   H_3, which any symmetric cost shares.")
        n_neg = sum(1 for lab, _, _ in feasible if fo[lab] < 0)
        print()
        print(f"   feasible operators with E_ohara < 0 : {n_neg}"
              f"   (if 0, the cost is bounded below by the zero-pair value)")
        check("A6", len(o_arg) == 2 and o_opt == 0 and n_neg == 0,
              "the minimum is 0, attained exactly by the two zero-pair "
              "operators -- so on a mixed-length catalogue the cost as stated "
              "does NOT select; reported as measured, not tuned away")

        print()
        print("=" * 78)
        print("[A7] AT FIXED LENGTH -- the comparison the physics actually asks")
        print("=" * 78)
        print("   'Which 2-crossing gluon dressing fires' is a question at ONE")
        print("   length, where the count is constant by definition and can")
        print("   never discriminate. This is where the O'Hara cost has to do")
        print("   its work, and where [A6]'s degeneracy does not apply.")
        print()
        print(f"   {'length':>7} {'feasible':>9} {'OHara argmin':>16}"
              f" {'words':>5} {'orbits':>6}  {'sample':>26}")
        sel_ok = True
        for n in sorted(by_len):
            labs = [lab for lab, w, _ in feasible if len(w) == n]
            if not labs:
                continue
            m, arg = argmin_within_tol({lab: fo[lab] for lab in labs})
            orbs = cyclic_orbit(arg)
            print(f"   {n:>7} {len(labs):>9} {mp.nstr(m, 12):>16}"
                  f" {len(arg):>5} {len(orbs):>6}  {str(arg[:2]):>26}")
            if n >= 2 and len(orbs) > 2:
                sel_ok = False
        print()
        print("   Read the ORBITS column, not the words column. A cyclic")
        print("   rotation is a conjugation, so rotated words are the SAME knot")
        print("   operator; and s0 <-> s1 is a relabelling of the strands. Two")
        print("   orbits at a length means the cost has narrowed the whole")
        print("   length class down to one operator and its mirror.")
        check("A7", sel_ok,
              "at each length >= 2 the O'Hara cost narrows the feasible set to "
              "at most one cyclic orbit and its mirror, where the count leaves "
              "the entire length class tied")

    print()
    print("=" * 78)
    print("[A8] THE INVARIANCE THE ORBIT COUNT RESTS ON -- measured, not cited")
    print("=" * 78)
    print("   [A7] counts ORBITS, which is only the right notion if the cost")
    print("   AND the constraint are both constant along one. A cyclic rotation")
    print("   is a conjugation; `tr_M` is a trace and `chi_lambda` is a class")
    print("   function, so both should be. Checked rather than assumed:")
    print()
    worst = mp.mpf(0)
    feas_split = 0
    sample = [w for lab, w in catalogue if len(w) >= 2][::7]
    for w in sample:
        L = len(w)
        rots = [w[k:] + w[:k] for k in range(L)]
        evals = [e_ohara(r) for r in rots]
        worst = max(worst, max(evals) - min(evals))
        fs = set()
        for r in rots:
            ok, _ = reading3_feasible(B._order.word_nf(list(r)), y)
            fs.add(ok)
        if len(fs) > 1:
            feas_split += 1
    print(f"   sampled operators                     : {len(sample)}")
    print(f"   worst E_ohara spread over rotations   : {mp.nstr(worst, 6)}")
    print(f"   operators whose FEASIBILITY changed   : {feas_split}")
    print()
    print("   The spread is at working precision, NOT zero -- the pair sums")
    print("   accumulate in a different order. That is exactly why TIE_TOL")
    print("   exists and why `==` on these costs is a bug; see its comment.")
    check("A8", worst <= TIE_TOL and feas_split == 0,
          f"cost and constraint are both cyclic-invariant to {mp.nstr(worst, 3)} "
          f"and 0 feasibility flips -- so counting orbits is legitimate")

    print()
    print("=" * 78)
    print("SUMMARY" if not FAILURES else "SUMMARY -- see failures above")
    print("=" * 78)
    print("   * The ILP is over WHOLE OPERATORS, not NF coordinates. S4's")
    print("     relative-interior exclusion is about the continuous LP in")
    print("     operator_selection_lattice_symbolic.py and does NOT transfer.")
    print("   * The incumbent cost (crossing count) is permutation-blind and")
    print("     ties every operator of a given length, so it cannot select.")
    print("   * The O'Hara pair kernel is separation-dependent and does break")
    print("     those ties -- which is exactly what the selection needs.")

    print()
    if FAILURES:
        print(f"FAILED: {', '.join(FAILURES)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
