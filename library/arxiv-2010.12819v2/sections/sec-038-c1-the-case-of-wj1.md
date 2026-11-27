---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-038-c1-the-case-of-wj1
section_title: "C.1 The case of Wj,1"
section_number: null
pages: 43-44
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
The main goal of this section is to provide numerical support for the conjecture (108) and the concept of strong
duality (97). We start by showing explicitly in Table 3 the duality for conjugate states for the ﬁrst few sizes,
giving an example of how matrix elements for raising operators will follow from those for the lowering operators.
In this example we consider Sz = 1, e=±1. We here also see the issue of mixing discussed in section 4.1.1.
Call theSz = 1, e=−1 primary state|u−⟩ and theSz = 1, e= 1 primary state|u+⟩. The sector of relevant
lattice momentum for the chiral level 1 state |a−1u−⟩ is then the same as that of the anti-chiral level 1 state
|¯a−1u+⟩. Within this sector, the two lowest-energy Bethe states have close but not identical energies. We call
these two states |v1⟩ and|v2⟩. Since nothing in our theory favours chiral over anti-chiral, or vice versa, we
must assume that we cannot identify one of |v1⟩,|v2⟩ to|a−1u−⟩ and the other to |¯a−1u+⟩. Instead, to keep
their energy on the lattice identical, we must consider them as linear combinations, containing equal parts of
the two states. We identify |¯a−1u+⟩ = 1√
2(|v1⟩ +|v2⟩) and|a−1u−⟩ = 1√
2(|v1⟩−| v2⟩) (with the phases of the
eigenvectors|v1⟩,|v2⟩ ﬁxed to give the same phase for the relevant matrix elements.) We then obtain the results
in Table 4, which are in line with our conjectures.
⟨v1|L−1|u−⟩ ⟨v2|L−1|u−⟩ ⟨ ¯a−1u−| ¯L−1|u−⟩
N ⟨u+| ¯L1|v1⟩ ⟨ u+| ¯L1|v2⟩ ⟨ u+|L1|a−1u+⟩
8 0.0526552 0.08033931 0.71811371
10 0.04744019 0.07094947 0.87777283
12 0.04357369 0.06336333 0.9762023
14 0.04048884 0.0573236 1.03974472
16 0.03793402 0.05245015 1.08270653
18 0.03576776 0.04844714 1.11294418
20 0.03389957 0.04510245 1.13495942
22 0.03226707 0.04226491 1.15145137
p7 0.00580449 0.00549332 1.23163297
conj 0 0 1.23170369
⟨v1| ¯L−1|u+⟩ ⟨v2| ¯L−1|u+⟩ ⟨a−1u+|L−1|u+⟩
N ⟨u−|L1|v1⟩ ⟨ u−|L1|v2⟩ ⟨ u−| ¯L1|¯a−1u−⟩
8 0.19977481 0.30480884 0.99943154
10 0.20854526 0.31189113 1.19506516
12 0.21572193 0.31369525 1.31480472
14 0.22148634 0.31357761 1.39180979
16 0.22616506 0.31271118 1.44376243
18 0.23002327 0.3115647 1.48028264
20 0.23325554 0.31034011 1.50685293
22 0.23600264 0.30912729 1.52674922
p7 0.27168088 0.2829496 1.62371173
conj 0.27723073 0.27723073 1.62376715
Table 3: Matrix elements of L±1 and ¯L±1 in the sector of Sz = 1, at x =π. We call|u−⟩ the primary state at
e =−1 and|u+⟩ the primary state ate = 1 (both in theN→∞ limit), with charges given by (66).|v1⟩ and|v2⟩
are linear combinations of |a−1u−⟩ and|¯a−1u+⟩ containing equal parts of both states, as discussed in Section
4.1.1. We here denote the corresponding scaling states on the lattice by the same labels as the states in the
limits. The matrix elements are computed at increasing lattice size N, after which polynomial extrapolations
pn(1/N) of degree n = 7 to all the data points is made in order to approximate the value at N→∞ . The CFT
value (“conj”)⟨a−1u|L−1u⟩ for a primary state u with charge α is
√
2α, as described in Section 5.2. Due to
|v1⟩,|v2⟩ being mixed states, the nonzero matrix elements involving these states are conjectured to come with
a factor of 1√
2: while the full value is 0.39206346 ( α = 2α0) we here instead conjecture a value of 0.27723073
each.
43
N ⟨¯a−1u+|L−1|u−⟩ ⟨a−1u−|L−1|u−⟩
8 0.09388641 0.02030561
10 0.08364162 0.01698464
12 0.07557809 0.01419611
14 0.06914237 0.01202808
16 0.0638982 0.01034544
18 0.05954055 0.00902118
20 0.05585724 0.00796118
22 0.05269816 0.00709863
p7 0.00798875 -0.00022102
conj 0 0
N ⟨¯a−1u+| ¯L−1|u+⟩ ⟨a−1u−| ¯L−1|u+⟩
8 0.35679453 0.07427027
10 0.3680041 0.07307657
12 0.37435448 0.0692776
14 0.37834734 0.06511836
16 0.38104305 0.06119735
18 0.38296053 0.0576585
20 0.38438017 0.05450702
22 0.38546507 0.05170693
p7 0.39218298 0.00796819
conj 0.39206346 0
N ⟨u+| ¯L1|¯a−1u+⟩ ⟨u+| ¯L1|a−1u−⟩
8 0.01957562 0.09404132
10 0.01662357 0.08371413
12 0.01399339 0.07561589
14 0.01190397 0.06916384
16 0.01026446 0.06391126
18 0.00896568 0.05954893
20 0.00792163 0.05586287
22 0.00706954 0.05270207
p7 -0.00022003 0.00798876
conj 0 0
N ⟨u−|L1|¯a−1u+⟩ ⟨u−|L1|a−1u−⟩
8 0.07703985 0.35620678
10 0.07466382 0.36768535
12 0.07028121 0.37416736
14 0.06579726 0.37822987
16 0.06168015 0.38096519
18 0.0580154 0.38290662
20 0.05477911 0.38434149
22 0.05191965 0.38543648
p7 0.00796872 0.39218313
conj 0 0.39206346
Table 4: Matrix elements of L±1 and ¯L±1 in the sector of Sz = 1, at x = π, with the same conventions as
in Table 3. Having separated |¯a−1u+⟩ and|a−1u−⟩ from each other we here obtain the full conjectured norm.
We note that strong duality does not apply to this table, since we no longer deal with single Bethe states but
rather linear combinations thereof.
With this result in mind we then restrict our attention to only considering lowering operators in tables 6–9.
In these four tables we look at the null states at level 1 and 2 for W1,1 and W2,1; the use of form factors here
enables us to access higher sizes. For comparison we show in each table both the action of Ar,s and ¯Ar,s, even
though only one of the conformal weights of the primary state is degenerate.
We also restrict our attention to|v1⟩ in the case of mixing at level 1, having already seen in tables 3–4 that
we recover the full norm when taking both|v1⟩ and|v2⟩ into account. The reason for this restriction is technical:
when using form factors instead of exact diagonalization, |v2⟩ corresponds to a singular Bethe state and would
require regularization that in turn would perturb the numerical results. We note that when excluding singular
states in this way in the cases of overlap, the results at both level 1 and 2 do not match the conjecture as well
as in the cases of no overlap. Meanwhile we see in Table 4 that the agreement when including all singular states
and taking the proper linear combinations is comparable to the cases of no overlap.
