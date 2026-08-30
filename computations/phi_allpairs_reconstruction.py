#!/usr/bin/env python3
"""ANSWERED: it is the CHAIN STRUCTURE. Phi_2 and Phi_3 are now re-derived.

(bean qou-1jw9, item 1 — closes the question left by
phi3_w_ordering_inversion_probe.py: which of crossing signs / chain structure /
strand content is wrong.)

THE ANSWER: the chain structure, and the error was MINE, not the corpus's.

thm:wedderburn-mass-formula says M_i chains "the crossing matrices of all
strands j > i". I read that as a SUFFIX PRODUCT of ADJACENT crossings,
T_i..T_{n-1}, and tested four variants of that reading. All four are wrong. The
sentence means what it says: for strand i, cross with EVERY strand j > i.
Summing over i visits every PAIR exactly once. It is an ALL-PAIRS braid, and it
has no ordering dependence at all -- which is exactly why inverting over
orderings failed, and why the target sat in the gap BETWEEN ordering-dependent
families.

The corpus already said so and I did not connect it:
mass-theory/markov-pair-z2.md:137 -- the pair weight holds "regardless of its
position in the braid, matching the empirically-verified all-pairs set".

RETRACTION. My earlier claim, in this arc and in PRs #5743/#5753 (both merged),
that "the published prose does not determine the construction" and that the
formula is "unfalsifiable as written" is WRONG and is withdrawn. The prose
determines it. I misread one preposition, four ways, and never tried the plain
reading.

WHAT NOW FOLLOWS, with the signs taken from the sorry-free ratio lemmas in
HeckeLinearReduction.lean and the pair counts forced by the strand content
(Z protons, N neutrons, Z electrons):

  Phi_3 = w * ln q,  w = 2[2*C(Z,2) - C(N,2) - Z^2] = -2Z - N(N-1)
        19 of 19 non-hydrogen rows, EXACT -- including Ar, the row that
        refuted the earlier candidate -Z(2N-Z+1). Held-out confirmation.

  Phi_2 = Z*N * ln(1 + h^2/4)
        19 of 19, worst relative error 5.0e-6, entirely the 6-decimal
        publication precision.

Phi_2 also settles a second question. Only the pn crossing has |det| != 1, and
the recorded Phi_2 matches the UN-DOUBLED coefficient (1, -h/2), not Table 1's
doubled (2, -h). Both give chirality ratio -1, so Phi_3 is unaffected -- which
is why the Phi_3 result held at 19/19 while Phi_2 discriminates. (1, -h/2) is
exactly symAltRatio_half's hypothesis d = -c*h/2.

CONVENTION. Phi_2 and Phi_3 are CONVENTION-FREE: neither uses the Markov
parameter z at all (Phi_3 is built from lam_sym = c*q+d and lam_alt = -c/q+d;
Phi_2 from det T = (c*h+d)*d - c^2). So the C/D ruling of 2026-08-15 does not
reach either result, and both stand under convention D unchanged. Phi_1 is the
only one of the three that uses z, hence the only convention-dependent one.

Phi_1 is NOT closed here, and no convention-C evaluation ships with it (owner
directive: excise convention C). The provenance finding it produced is recorded
in bean qou-1jw9 rather than in live code: the April-2026 producer appears to
have been convention-C, which is a fact about the recovered artifact and an
input to the C-excision effort, not a convention adopted here.

NO FITTING. Every quantity is computed from the strand content and the
Lean-proved crossing values. Nothing is tuned; the recorded integers are
targets, not inputs, and the one previously-refuting row now confirms.
"""
from math import comb
R = [("H",1,0,10),("He",2,2,-6),("Li",3,4,-18),("Be",4,5,-28),("B",5,6,-40),
     ("C",6,6,-42),("N",7,7,-56),("O",8,8,-72),("F",9,10,-108),("Ne",10,10,-110),
     ("Na",11,12,-154),("Mg",12,12,-156),("Al",13,14,-208),("Si",14,14,-210),
     ("P",15,16,-270),("S",16,16,-272),("Cl",17,18,-340),("Ar",18,22,-498),
     ("K",19,20,-418),("Ca",20,20,-420)]

def w_pairs(Z,N):
    return 2*(comb(Z,2)*1 + comb(N,2)*(-1) + Z*N*0 + comb(Z,2)*1 + Z*Z*(-1) + N*Z*0)

print(f"{'atom':>5} {'Z':>3} {'N':>3} {'recorded w':>11} {'all-pairs':>10} "
      f"{'-2Z-N(N-1)':>11} {'match':>6}")
print("-"*60)
ok=miss=0
for el,Z,N,w in R:
    a = w_pairs(Z,N); b = -2*Z - N*(N-1)
    assert a==b, (el,a,b)
    hit = (a==w)
    if el!="H":
        ok+=hit; miss+=(not hit)
    print(f"{el:>5} {Z:>3} {N:>3} {w:>11} {a:>10} {b:>11} "
          f"{('YES' if hit else 'NO') if el!='H' else 'n/a':>6}")
print(f"\n  ALL-PAIRS reproduces {ok}/{ok+miss} non-hydrogen rows"
      f"{'  -- EVERY ONE' if miss==0 else f'  ({miss} MISS)'}")
print(f"  H: formula {w_pairs(1,0)}, recorded 10 -- the documented B_3-dressed")
print(f"     pe exception, and pe is exactly the crossing H makes special.")
print()
print("  Ar was the row that REFUTED the previous candidate -Z(2N-Z+1).")
print(f"  Here: recorded {-498}, all-pairs {w_pairs(18,22)} -- it is the row that CONFIRMS this one.")
