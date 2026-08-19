---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-005-34-on-parabolic-representations-of-twist-knot-gr
section_title: "On parabolic representations of twist knot groups"
section_number: 3.4
pages: 6-8
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
terested in the parabolic representationsof (hyperbolic) two–bridge knot groups and espe-
cially twist knot groups. The holonomy representation is on e of them. Lemma 5 charac-
terizes the holonomy representation algebraically and say s that it corresponds to a root of
Riley’s equationφK(1, u) = 0. A natural and interesting question is the following: whic h
roots of Riley’s equation φK(1, u) = 0 correspond to the holonomy representation? Here
we will give a geometric characterization of such roots in the case of two–bridge knots.
3.4.1. Remarks. We begin this section by some elementary but important remar ks on the
roots of Riley’s equationφK(1, u) = 0 corresponding to holonomy representations.
(1) One can ﬁrst notice that such roots are necessarily complex numbers which are
not real, because the discrete and faithful representation is irred ucible and not
conjugate to a real representation (i.e. a representation such that the image of each
element is a matrix with real entries).
6
(2) One can also observe that holonomy representations corr espond to a pair of com-
plex conjugate roots of Riley’s equationφK(1, u) = 0 as it is easy to see.
3.4.2. Generalities: the case of two–bridge knots. Let K be a hyperbolic two–bridge knot.
Suppose that a presentation of the knot group Π(K) is given as in Eq. (4) by
Π(K) =⟨x, y| Ωx = yΩ⟩, where Ωis a word in x, y.
The longitude of K is of the form: λ =
←
ΩΩxn. Here n is an integer such that the sum of
the exponents in the word λ is 0 and we repeat that
←
Ωdenotes the word obtained from Ω
by reversing the order of the letters.
Let ρ: Π(K)→ SL2(C) be a representation such that:
x↦→±
( 1 1
0 1
)
, y↦→±
( 1 0
−u 1
)
where u is necessarily a root of Riley’s equationφK(1, u) = 0. Suppose that
ρ(Ω) =
( w1,1 w1,2
w2,1 w2,2
)
where wi, j is a polynomial in u for all i, j∈{ 1, 2}.
Riley’s method gives us the following identities (see Section 3.2):
w1,1 = 0 and uw1,2 + w2,1 = 0.
Thus
ρ(Ω) =
( 0 w1,2
−uw1,2 w2,2
)
.
The fact that ρ(w)∈ SL2(C) further gives the following equation:
(7) uw2
1,2 = 1.
The crucial point for computing ρ(λ) is to express ρ(
←
Ω) with the help of ρ(Ω). Consider
the diagonal matrix:
i =
( i 0
0 −i
)
∈ SL2(C),
where i stands for a square root of−1. Let Ad denote the adjoint representation of the Lie
group SL2(C). Then the following identities hold:
ρ(x−1) = Adi(ρ(x)), ρ (y−1) = Adi(ρ(y)) and ρ(Ω−1) = Adi(ρ(
←
Ω)).
Thus, we have
ρ(
←
Ω) = Adi(ρ(Ω−1)) =
( w2,2 w1,2
w2,1 w1,1
)
.
Next, a direct computation gives:
(8) ρ(λ) = ρ(
←
Ω)ρ(Ω)ρ(x)n =
(−uw2
1,2 −nuw2
1,2 + 2w1,2w2,2
0 −uw2
1,2
)
.
Combining Eqs. (7) and (8), we obtain
(9) ρ(λ) =
(−1 −n + 2w1,2w2,2
0 −1
)
.
And we conclude that the cusp shape of K is
(10) c = n− 2w1,2w2,2.
Remark 6. In particular, Eq. (9) gives us, by an elementary and direct computation, Cale-
gari’s result [Cal06]: trρ0(λ) =−2 for the discrete faithful representation ρ0 associated to
the complete hyperbolic structure of the exterior of a (hyperbolic) two–bridge knot.
7
3.4.3. The special case of twist knots. In the case of hyperbolic twist knots, we can further
estimate wi, j in Eq. (10). In fact, we only consider the case where K = J(2, 2m) in what
follows. The group Π(K) of such a knot has the following presentation:
Π(K) =⟨x, y| wmx = ywm⟩,
where w is the commutator [ y, x−1] (see Fact 1, Section 2). A direct computation of the
commutator ρ(w) = [ρ(y), ρ(x)−1] gives:
W = ρ(w) =
( 1− u −u
u2 u2 + u + 1
)
(where u is such that φK(1, u) = 0).
Using the Cayley–Hamilton identity, it is easy to obtain thefollowing recursive formula
for the powers of the matrix W:
(11) Wk− (u2 + 2)Wk−1 + Wk−2 = 0, k /greaterorequalslant2.
Eq. (11) implies, by induction on k,
w2,2 =−(u + 2)w1,2.
Since n = 0 and uw2
1,2 = 1, the cusp shape of the twist knot K is:
c = n + (2u + 4)w2
1,2 = 2u + 4
u .
In other words, the root u0 of Riley’s equationφK(1, u) = 0 corresponding to the holo-
nomy representation satisﬁes the following equation:
(12) u0 = 4
c− 2 ,
where c is the cusp shape of the knot exterior.
Remark 7. Eq. (12) gives a geometric characterization of the (pair of c omplex conjugate)
roots of Riley’s equation φK(1, u) = 0 associated to the holonomy representation in terms
of the cusp shape, a geometric quantity associated to each cusped hyperbolic 3-dimensional
manifold.
