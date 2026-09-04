#!/usr/bin/env python3
"""The two-nucleon linking matrix is I_3-valued, hence blind to the T=0/T=1 split.

STATUS: scope-(b) structural exclusion of a CLASS, by composition of two facts
the corpus already holds.  No new measurement; no fit; exact integer arithmetic
throughout (linking numbers and gcds -- there is no floating-point quantity in
this file at all).

-----------------------------------------------------------------------------
WHY THIS EXISTS

The `bk-crossing-mass-binding` arc (bean `qou-brng`) needs the two-nucleon
BINDING CHANNEL ASYMMETRY: the deuteron 3S1 (T=0) is bound at 2.224566 MeV
while the np 1S0 (T=1) is a virtual state at ~0.066 MeV, a ratio of ~33.7.

Three routes into it have now closed, all on the Markov-trace side:

  * `isospin_channel_R_is_one_everywhere_probe` -- a single crossing, a pair
    exchange at any separation, its powers, and far-commuting products all give
    R = 1 exactly (minimal-polynomial argument).
  * `block_transposition_lift_probe` -- the six-strand block transposition
    Delta_{3,3} has integer-quantised log-moduli, so its channel asymmetry has
    a CEILING of 9, against the 33.7 required.
  * `markov_trace_family_rank_probe` + `QOU.SchurWeyl.ocneanuFamily_finrank_le`
    -- the Ocneanu/Markov trace family spans rank exactly n of a p(n)-dimensional
    space, so trace subtraction cannot isolate a single Wedderburn block.

That left, as the stated honest residue (docs/audits/2026-09-03-two-mubars-
selector-vs-magnitude.md, final section): *"an invariant of the six-strand
two-nucleon link that is sensitive to the exchange"*, i.e. a NON-trace route.

The natural candidate class for such an object is the LINKING DATA of the
six-component link -- pairwise linking numbers and the Milnor `mu-bar` tower
built on them.  This probe runs the gate on that class BEFORE any search
(AGENTS.md 'Formalize-first probe discipline': find the invariant that prunes
the class, rather than scanning the class).

The class is dead, and for a reason that is one line long once stated.

-----------------------------------------------------------------------------
THE TWO CORPUS FACTS (cited, NOT derived here)

(F1) The inter-nucleon linking number IS the isospin projection.
     `computations/inter_nucleon_linked_channel.py` derives the inter-nucleon
     arc as the minimal non-Brunnian 2-component link, the Hopf link T(2,2k),
     with chirality giving the sign:
         pp -> sigma_1^{+2} = T(2,+2),  writhe +2,  lk +1
         nn -> sigma_1^{-2} = T(2,-2),  writhe -2,  lk -1
         pn -> sigma_1^{ 0} = T(2, 0),  writhe  0,  lk  0
     and its docstring states 'NO numeric is tuned'.  `u1_hypercharge_assignment`
     names the same datum in isospin terms: *"I_3 = writhe/2-of-inter-nucleon-arc
     carries the p/n split"* (line 336).  Since lk(T(2,2k)) = k = writhe/2, the
     two statements are the same statement: the inter-nucleon lk IS I_3.

(F2) Milnor's indeterminacy theorem.  `mu-bar(i_1...i_k)` is well-defined only
     modulo the gcd of the lower-order invariants on those indices.  The corpus
     already USES this as a scope-(b) exclusion for 4He:
     docs/audits/2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md --
     *"For a cluster in which every bonded pair is Hopf-linked (lk = 1) ... the
     indeterminacy modulus is gcd(lk) = 1, so every higher mu-bar lives in
     Z/1 = 0: it carries no invariant content beyond the pairwise bonds."*

-----------------------------------------------------------------------------
THE COMPOSITION (what this probe adds)

Neither carrier applies (F2) to the TWO-NUCLEON link, and neither notices what
(F1) implies about the channels.  Composed:

  1. The linking matrix of the six-strand two-nucleon link is a function of the
     FLAVOUR CONTENT alone -- intra-nucleon entries vanish (a baryon is a
     Borromean triple: all pairwise lk = 0), and the inter-nucleon entry is
     I_3 by (F1).

  2. The 3S1 and 1S0 np channels have the SAME flavour content: one proton, one
     neutron, so I_3 = +1/2 - 1/2 = 0 in BOTH.  They differ in total isospin T
     (0 vs 1) and in spin S (1 vs 0), neither of which enters the linking data.

  3. Therefore their linking matrices are EQUAL, entry by entry.  Every function
     of the linking matrix -- every pairwise invariant, and by (F2) every higher
     Milnor invariant, since the whole tower is defined modulo gcds of these
     same entries -- takes the SAME value on the two channels.  The channel
     asymmetry any such invariant can produce is exactly 1, against 33.7 needed.

  4. As a by-product, (F2) says WHERE the tower is even alive: gcd = 0 on np
     (indeterminacy Z/0 = Z, genuine invariant) and gcd = 1 on pp/nn
     (indeterminacy Z/1 = 0, no content).  So the tower survives only on the
     np line -- and both channels sit on it, which is exactly why surviving
     does not help.

SCOPE, stated per AGENTS.md 'Before declaring refuted':

  (b) STRUCTURAL EXCLUSION, cited invariant = Milnor indeterminacy + the
      corpus's own lk = I_3 assignment.  It excludes the class of invariants
      that are FUNCTIONS OF THE PAIRWISE LINKING DATA of this link.  The
      exclusion is not numerical and cannot be escaped by a better choice
      within the class: the two inputs are literally the same matrix.

  It does NOT exclude:
      * an invariant sensitive to the braid word BEYOND its linking data (the
        Delta_{3,3} exchange spectrum is exactly such an object -- it is not
        excluded here, it is capped at 9 by a different argument);
      * a non-Milnor super-pairwise object;
      * anything carrying SPIN, which is what actually distinguishes the two
        channels.  Bean `qou-7zob` independently records that there is *"NO map
        from strand position to orbital angular momentum anywhere in the
        corpus"* -- this probe reaches the same wall from the linking side.

CONVERGENCE.  The t7qv arc's `det T = -1` result caps the channel-asymmetry
ratio at exactly 1 in both sectors, and `isospin_channel_R_is_one_everywhere`
finds R = 1 everywhere.  This probe supplies a reason those ratios are 1 rather
than merely small: the objects being compared are functions of I_3, and the two
channels have equal I_3.  That is corroboration, not a fourth independent
measurement -- the routes share the underlying assignment (F1).

Bean: `qou-brng`.  Companion: docs/audits/2026-09-03-two-mubars-selector-vs-
magnitude.md (the residue this closes).
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd

# --------------------------------------------------------------------------
# The link.  Six components: 0,1,2 are nucleon A's colour tubes, 3,4,5 are B's.
# --------------------------------------------------------------------------

NUCLEON_A = (0, 1, 2)
NUCLEON_B = (3, 4, 5)
ALL = NUCLEON_A + NUCLEON_B

# Isospin projection of each nucleon flavour (exact rationals; I_3 = +-1/2).
I3_NUCLEON = {"p": Fraction(1, 2), "n": Fraction(-1, 2)}

# The four two-nucleon states of interest.  Note that the two np rows differ in
# (T, S) and are IDENTICAL in flavour content -- that is the whole point.
CHANNELS = {
    # label:        (flavour A, flavour B, total isospin T, total spin S)
    "pp":           ("p", "p", 1, 0),
    "nn":           ("n", "n", 1, 0),
    "np (3S1, T=0)": ("n", "p", 0, 1),
    "np (1S0, T=1)": ("n", "p", 1, 0),
}

# Experimental references -- FALSIFICATION targets, never fitted.
# Deuteron binding (AME2020) and the np 1S0 virtual-state energy (PDG/scattering).
# Carried in eV as exact integers so that no float enters this file: the arc
# quotes 2.224566 MeV and 0.066 MeV, whose ratio is the 33.7055 it targets.
B_DEUTERON_EV = 2224566          # eV = 2.224566 MeV, deuteron binding (AME2020)
E_VIRTUAL_EV = 66000             # eV = 0.066   MeV, the 1S0 np virtual state
REQUIRED_RATIO = Fraction(B_DEUTERON_EV, E_VIRTUAL_EV)


def inter_nucleon_lk(flavour_a: str, flavour_b: str) -> int:
    """The inter-nucleon arc's linking number = I_3 of the pair.  Fact (F1).

    Derived in `computations/inter_nucleon_linked_channel.py` as the Hopf link
    T(2, 2k) with lk = k = writhe/2, and named as I_3 in
    `u1_hypercharge_assignment.py:336`.  pp -> +1, nn -> -1, pn -> 0.
    """
    i3 = I3_NUCLEON[flavour_a] + I3_NUCLEON[flavour_b]
    assert i3.denominator == 1, "a two-nucleon I_3 must be an integer"
    return int(i3)


def linking_matrix(flavour_a: str, flavour_b: str, *, spread: bool) -> dict:
    """Pairwise linking numbers of the six-component two-nucleon link.

    Intra-nucleon entries are 0: a baryon is a Borromean triple, whose defining
    property is that every pairwise linking number vanishes while mu-bar(123) =
    +-1 (QOU/StandardModel/SecondCrossingInvariant.lean).

    `spread` is the one modelling choice, and it is exercised BOTH ways below so
    that the verdict cannot depend on it:
      spread=False -- the corpus's literal reading: ONE inter-nucleon arc links
                      ONE tube of A to ONE tube of B, so a single off-block
                      entry carries I_3 and the other eight vanish.
      spread=True  -- the maximal alternative: every one of the nine A-B tube
                      pairs carries the arc's linking number.
    """
    lk = {pair: 0 for pair in combinations(ALL, 2)}
    val = inter_nucleon_lk(flavour_a, flavour_b)
    if spread:
        for a in NUCLEON_A:
            for b in NUCLEON_B:
                lk[(a, b)] = val
    else:
        lk[(NUCLEON_A[0], NUCLEON_B[0])] = val
    return lk


def indeterminacy_modulus(lk: dict, indices: tuple) -> int:
    """Milnor's Delta(I) at order 3: gcd of the pairwise linking numbers on I.

    Fact (F2).  gcd(0, 0, 0) = 0, whose quotient Z/0 = Z is a genuine invariant;
    any unit entry gives gcd = 1, whose quotient Z/1 = 0 carries no content.

    A unit at order 2 forces Delta = 1 at EVERY higher order too, since a gcd
    over a superset divides the gcd over the subset and 1 divides everything --
    so this order-3 computation settles the whole tower on those indices.
    """
    g = 0
    for pair in combinations(sorted(indices), 2):
        g = gcd(g, abs(lk[pair]))
    return g


def tower_verdict(modulus: int) -> str:
    if modulus == 0:
        return "ALIVE  (Z/0 = Z, genuine invariant)"
    if modulus == 1:
        return "DEAD   (Z/1 = 0, no content)"
    return f"partial (Z/{modulus})"


def main() -> int:
    print(__doc__.split("\n")[0])
    print()

    # ---------------------------------------------------------------- step 1
    print("STEP 1 -- the linking matrix per channel (fact F1: inter lk = I_3)")
    print()
    matrices = {}
    for spread in (False, True):
        tag = "all 9 A-B pairs" if spread else "single arc"
        print(f"  modelling: {tag}")
        for label, (fa, fb, T, S) in CHANNELS.items():
            lk = linking_matrix(fa, fb, spread=spread)
            matrices[(label, spread)] = lk
            nz = sorted({v for v in lk.values() if v != 0})
            print(
                f"    {label:<16} flavour={fa}{fb}  T={T} S={S}  "
                f"I_3={inter_nucleon_lk(fa, fb):+d}  nonzero entries={nz or '[]'}"
            )
        print()

    # ---------------------------------------------------------------- step 2
    # THE DECISIVE ASSERT.  The two np channels have identical linking matrices.
    print("STEP 2 -- the two np channels, compared entry by entry")
    print()
    for spread in (False, True):
        a = matrices[("np (3S1, T=0)", spread)]
        b = matrices[("np (1S0, T=1)", spread)]
        tag = "all 9 A-B pairs" if spread else "single arc"
        differing = [p for p in a if a[p] != b[p]]
        assert not differing, (
            "the 3S1 and 1S0 np linking matrices must be identical -- they have "
            f"the same flavour content; differing pairs: {differing}"
        )
        print(
            f"  {tag:<16}: identical on all {len(a)} pairs "
            f"-> every function of the matrix is channel-blind"
        )
    print()
    print("  The channels differ in (T, S) = (0, 1) vs (1, 0).  Neither T nor S")
    print("  enters the linking data, which sees only flavour, i.e. I_3 = 0 for")
    print("  both.  So the asymmetry ANY function of this matrix can produce is:")
    print()
    achievable = Fraction(1)
    print(f"      achievable ratio = {achievable}   (exactly 1, not approximately)")
    print(f"      required  ratio = {REQUIRED_RATIO}"
          f" = {B_DEUTERON_EV} eV / {E_VIRTUAL_EV} eV")
    print(f"                      ~ {float(REQUIRED_RATIO):.4f}")
    print()
    assert achievable == 1, "equal inputs give equal outputs; the ratio is 1"
    # Pin the target to the figure the arc actually carries, to 4 decimals.  A
    # bare `> 1` is too weak to catch a unit slip: an earlier draft of this file
    # labelled the deuteron's eV digits as keV and printed a shortfall of
    # 33705x, a clean factor of 1000, which `> 1` passed without complaint.
    assert Fraction(337054, 10000) < REQUIRED_RATIO < Fraction(337056, 10000), (
        f"required ratio must be the arc's 33.7055, got {float(REQUIRED_RATIO)} "
        "-- check the energy units"
    )
    shortfall = REQUIRED_RATIO / achievable
    print(f"      shortfall       ~ {float(shortfall):.4f}x  -- the class cannot close it")
    print()

    # ---------------------------------------------------------------- step 3
    print("STEP 3 -- where the Milnor tower is even alive (fact F2)")
    print()
    for spread in (False, True):
        tag = "all 9 A-B pairs" if spread else "single arc"
        print(f"  modelling: {tag}")
        for label, (fa, fb, _T, _S) in CHANNELS.items():
            lk = matrices[(label, spread)]
            # The mixed triples are the ones that see the interface at all.
            mixed = [
                idx for idx in combinations(ALL, 3)
                if not (set(idx) <= set(NUCLEON_A) or set(idx) <= set(NUCLEON_B))
            ]
            moduli = {indeterminacy_modulus(lk, idx) for idx in mixed}
            intra = indeterminacy_modulus(lk, NUCLEON_A)
            assert intra == 0, (
                "an intra-nucleon triple is Borromean, so its indeterminacy "
                "modulus must be 0 -- that is what makes mu-bar_123 = +-1 an "
                "invariant at all"
            )
            worst = max(moduli)
            print(
                f"    {label:<16} intra-triple: {tower_verdict(intra)}"
                f"   |  mixed triples: {tower_verdict(worst)}"
            )
        print()

    # The channel-selective half of (F2), asserted rather than merely printed.
    for spread in (False, True):
        for label in ("pp", "nn"):
            fa, fb, _, _ = CHANNELS[label]
            lk = matrices[(label, spread)]
            mixed = [
                idx for idx in combinations(ALL, 3)
                if not (set(idx) <= set(NUCLEON_A) or set(idx) <= set(NUCLEON_B))
            ]
            assert any(indeterminacy_modulus(lk, idx) == 1 for idx in mixed), (
                f"{label} has a Hopf-linked pair (lk = {inter_nucleon_lk(fa, fb)}), "
                "so some mixed triple must have indeterminacy 1 and carry no content"
            )
        for label in ("np (3S1, T=0)", "np (1S0, T=1)"):
            lk = matrices[(label, spread)]
            assert all(
                indeterminacy_modulus(lk, idx) == 0 for idx in combinations(ALL, 3)
            ), "on the np line every linking number vanishes, so the tower survives"

    print("  So the tower is DEAD across the interface at I_3 = +-1 (pp, nn) and")
    print("  ALIVE only at I_3 = 0 (np) -- where BOTH channels sit.  Surviving is")
    print("  exactly what does not help: it survives equally on both.")
    print()

    # ---------------------------------------------------------------- verdict
    print("VERDICT -- scope (b), structural, cited invariant")
    print()
    print("  No invariant of the six-strand two-nucleon link that is a function")
    print("  of its pairwise linking data can carry the binding channel")
    print("  asymmetry, because the 3S1 and 1S0 np channels present that data")
    print("  IDENTICALLY.  This is not a bound that a better choice within the")
    print("  class might beat: the two inputs are the same matrix.")
    print()
    print("  NOT excluded: an invariant reading the braid word beyond its linking")
    print("  data; a non-Milnor super-pairwise object; anything carrying SPIN,")
    print("  which is what actually separates the channels (cf. bean qou-7zob).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
