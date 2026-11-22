# Preregistration: bonds with two or more interface letters (issue #8960)

Written 2026-11-22, before any value in this directory was computed.

## Setup (unchanged from `../he4_bond_both_nucleons/`)

H_6(q), sigma^2 = h sigma + 1, h = q - q^-1, Markov trace at z_D = q^3/(q^2+1).
Nucleon 1 on generators {0,1}, nucleon 2 on {3,4}, interface (gap) generator 2.
Nucleon words, free word X Y^(3), atom word X Y^(3) B, mu = tr(atom)/tr(free):
all reused from `he4_bond_both_nucleons_probe.py` (imported, not copied).
Exact Fractions; q0 = Fraction(Q_50_DIGIT_STR) (proton pin); also q = 1.

## Two chiralities (coordinator addition)

- V: vertex(i) = sigma_i sigma_{i+1}^-1 (the class of the earlier probe).
- M: mirror vertex(i) = sigma_i^-1 sigma_{i+1}.
Same 84 words (1..3 vertices, i in 0..3) for each.

## Lean predictions being tested (MarkovTraceMultiGapBond.lean)

For a bond with exactly two gap letters, write the piece between them as A C^(3)
(A on generators {0,1}, C on {3,4}). If A has no sigma_1 OR C has no sigma_3,
`towerTr_twoGap_outerLeft_crossRatio` / `_outerRight_crossRatio` predict
mu_pp mu_nn = mu_pn mu_np exactly. Only "both inner letters present" can break it.

## Quantities

1. mu for all 84 words x 4 pairs x 2 chiralities at q0 and q = 1.
2. Class of each word: n_gap (0..3); for n_gap = 2, (left_inner, right_inner).
3. Cross-ratio holds exactly? (Fraction equality.)
4. Exact bilinear rank of (x, y) -> tr(x y^(3) B) on the 6 x 6 standard bases
   T_w of H_3 on {0,1} and on {3,4}.
5. Pattern (strong): mu_pn < 1, mu_np < 1, mu_pp > 1, mu_nn > 1; weak as before.
6. For every word whose cross-ratio fails: does SOME choice of two first-cluster
   and two second-cluster basis elements T_w (all four mu > 0, free traces != 0)
   show the strong pattern? Yes would mean the bond alone does not forbid it.

No word added, removed or reordered after seeing values.

## Addendum (written after the first run, before the second; marked as such)

The first run found bilinear rank 2 for all 9 cross-ratio failures and no pattern among
pairs of basis elements T_w. A scratch search over random integer combinations then found
the pattern for 7 of the 9 bonds and none for [2,1] and [2,1,1]. Added for the second run:
for each failing word, (a) whether the free-trace vectors lie in the column / row space of
the bond matrix, and if so the constant c in mu(x,y) = c + l'(x) r'(y); (b) the same random
search (seed 1, 40 x 40 integer combinations in [-3,3], exact). Lean:
`not_pattern_of_affine_rankOne` (c <= 1/2 excludes the pattern with all mu > 0).
