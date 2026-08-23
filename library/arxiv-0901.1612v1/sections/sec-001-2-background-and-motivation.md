---
doc_id: arxiv-0901.1612v1
doc_title: "TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INV ARIANTS"
section_id: sec-001-2-background-and-motivation
section_title: "Background and motivation"
section_number: 2
pages: 4-5
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
Let L be an ordered oriented link in R3 with two parametrized components
X ={x(s)| s∈S1} and Y ={y(t)| t∈S1}.
The classical linking number Lk(X,Y ) is the degree of the Gauss map S1×S1→S2
sending (s,t ) to (y(t)−x(s))/‖y(t)−x(s)‖, and can be expressed by the famous integral
formula of Gauss [1833],
Lk(X,Y ) = 1
4π
∫
S1×S1
x′(s)×y′(t) •
x(s)−y(t)
‖x(s)−y(t)‖3 dsdt
=
∫
S1×S1
x′(s)×y′(t) •∇xϕ (‖x(s)−y(t)‖) dsdt,
whereϕ(r) =−1/(4πr) is the fundamental solution of the scalar Laplacian in R3. The
integrand is invariant under the group of orientation-preserving rigid motions of R3,
acting on the linkL. Corresponding formulas inS3 appear in DeTurck and Gluck [2008]
and in Kuperberg [2008].
Theorems A and B above give a similar formulation of Milnor’s triple linking number
in S3. We emphasize that these two theorems are set speciﬁcally in S3, and that so
far we have been unable to ﬁnd corresponding formulas in Euclidean space R3 which
are equivariant (for Theorem A) and invariant (for Theorem B) under the noncompact
group of orientation-preserving rigid motions of R3.
For some background on higher order linking invariants, see Milnor [1957] and,
for example, Massey [1969], Casson [1975], Turaev [1976], Porter [1980], Fenn [1983],
Orr [1989], and Cochran [1990].
The helicity of a vector ﬁeld V deﬁned on a bounded domain Ω in R3 is given by
the formula
Hel(V ) =
∫
Ω×Ω
V (x)×V (y) •
x−y
‖x−y‖3 dxdy
=
∫
Ω×Ω
V (x)×V (y) •∇xϕ (‖x−y‖) dxdy
where, as above, ϕ is the fundamental solution of the scalar Laplacian on R3.
Woltjer [1958] introduced this notion during his study of the magnetic ﬁeld in the
Crab Nebula, and showed that the helicity of a magnetic ﬁeld remains constant as the
ﬁeld evolves according to the equations of ideal magnetohydrodynamics, and that it
provides a lower bound for the ﬁeld energy during such evolution. The term “helicity”
was coined by Moﬀatt [1969], who also derived the above formula.
There is no mistaking the analogy with Gauss’s linking integral, and no surprise that
helicity is a measure of the extent to which the orbits of V wrap and coil around one
another. Since its introduction, helicity has played an important role in astrophysics
and solar physics, and in plasma physics here on earth.
4
Triple linking numbers, ambiguous Hopf invariants and integral formulas
Looking back at Theorem B, we see that the integral in our formula for Milnor’s
µ-invariant of a three-component link L in the 3-sphere expresses the helicity of the
associated vector ﬁeld VL on the 3-torus.
Our study was motivated by a problem proposed by Arnol ′d and Khesin [1998]
regarding the search for “higher helicities” for divergence-free vector ﬁelds. In their
own words:
The dream is to deﬁne such a hierarchy of invariants for generic vector
ﬁelds such that, whereas all the invariants of order ≤k have zero value
for a given ﬁeld and there exists a nonzero invariant of order k + 1,
this nonzero invariant provides a lower bound for the ﬁeld energy.
Many others have been motivated by this problem, and have contributed to its un-
derstanding; see, for example, Berger and Field [1984], Berger [1990, 1991], Evans and
Berger [1992], Akhmetiev and Ruzmaiken [1994, 1995], Akhmetiev [1998], Laurence
and Stredulinsky [2000], Hornig and Mayer [2002], Rivi` ere [2002], Khesin [2003], and
Bodecker and Hornig [2004].
The formulation in Theorems A and B has led to partial results that address the
case of vector ﬁelds on invariant domains such as ﬂux tubes modeled on the Borromean
rings; see Komendarczyk [2008].
