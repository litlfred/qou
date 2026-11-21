---
doc_id: arxiv-1203.6041v2
doc_title: "S and D-wave phase shifts in isospin-2 ππ scattering from lattice QCD"
section_id: sec-019-1-operator-construction
section_title: "Operator construction"
section_number: 1
pages: 29-30
source_pdf: 1203.6041v2.pdf
source_sha256: 1113e87534ffd6e0
toc_source: outline
doc_brief: "S and D-wave phase shifts in isospin-2 ππ scattering from lattice QCD — 24 sections: Front matter; S and D-wave phase shifts in isosp; I Introduction"
---
In Section A 1 we describe our general multi-particle op-
erator construction and in Section A 2 discuss the method
used to calculate the Clebsch-Gordan coeﬃcients.
In
Section A 3 we state our conventions for the lattice ir-
reps and choices of rotations before giving some exam-
ple Clebsch-Gordan coeﬃcients in Section A 4. Further
Clebsch-Gordan coeﬃcients are given in supplementary
material [43].
1.
Operator construction
Here we describe our construction of multi-particle op-
erators, generalising the discussion in Section II. We will
consider two-particle operators but the procedure can be
applied iteratively to construct multi-particle operators
for a larger number of particles.
In Refs. [11, 12] we discussed how operators with a def-
inite continuum JP and spin-component M, OJP ,M(⃗p =⃗
0), can be constructed out of gauge-covariant derivatives
and Dirac gamma matrices. The appropriate lattice op-
erators were formed by subducing these continuum oper-
ators into octahedral group irreps,
h
O[JP ]
ΛP ,µ(⃗0)
i†
=
X
M
SΛ,µ
J,M
h
OJP (⃗0)
i†
,
where ΛP is an irrep of OD
h , µ is the irrep row and SΛ,µ
J,M
are subduction coeﬃcients discussed in Refs. [11, 12, 14].
In Ref. [27] we discussed how to construct helicity op-
erators16,
h
OJP ,λ(⃗p)
i†
=
X
m
D(J)
mλ(R)
h
OJP ,m(⃗p)
i†
,
(A1)
where λ is the helicity, JP refers to the spin and parity
of the operator with⃗p =⃗0 and D is a Wigner-D matrix;
a summary of our conventions is given in Appendix A 3
and we refer to Ref. [27] for more details, for example,
on the choice of R. From these we constructed subduced
helicity operators,
h
O[JP ,|λ|]
Λ,µ
(⃗p)
i†
=
X
ˆλ=±|λ|
S ˜η,ˆλ
Λ,µ
h
OJP ,ˆλ(⃗p)
i†
,
where Λ is an irrep of LG(⃗p) (the little group for momen-
tum⃗p), µ is the irrep row and ˜η ≡P(−1)J. The subduc-
tion coeﬃcients, S ˜η,ˆλ
Λ,µ, which were discussed in Ref. [27],
are given in Table IX. Note that here we give subductions
coeﬃcients for creation helicity operators which trans-
form like states, i.e.
under a rotation by φ about the
axis deﬁned by⃗p they transform as Rφ |λ⟩= e−iφλ |λ⟩.
In Ref. [27] we showed that these subduced helicity op-
erators are useful for studying mesons with non-zero mo-
mentum on the lattice.
In general, a two-particle creation operator with total
momentum⃗P can be constructed from the product of
two single-particle operators,
Group
|λ|˜η
Λ(µ)
S ˜η,λ
Λ,µ
Dic4
[0, 0, n]
0+
A1(1)
1
0−
A2(1)
1
1
E2 ( 1
2 )
(δs,+ ± ˜ηδs,−)/
√
2
2
B1(1)
(δs,+ + ˜ηδs,−)/
√
2
2
B2(1)
(δs,+ −˜ηδs,−)/
√
2
3
E2 ( 1
2 )
(±δs,+ + ˜ηδs,−)/
√
2
4
A1(1)
(δs,+ + ˜ηδs,−)/
√
2
4
A2(1)
(δs,+ −˜ηδs,−)/
√
2
Dic2
[0, n, n]
0+
A1(1)
1
0−
A2(1)
1
1
B1(1)
(δs,+ + ˜ηδs,−)/
√
2
1
B2(1)
(δs,+ −˜ηδs,−)/
√
2
2
A1(1)
(δs,+ + ˜ηδs,−)/
√
2
2
A2(1)
(δs,+ −˜ηδs,−)/
√
2
3
B1(1)
(δs,+ + ˜ηδs,−)/
√
2
3
B2(1)
(δs,+ −˜ηδs,−)/
√
2
4
A1(1)
(δs,+ + ˜ηδs,−)/
√
2
4
A2(1)
(δs,+ −˜ηδs,−)/
√
2
Dic3
[n, n, n]
0+
A1(1)
1
0−
A2(1)
1
1
E2 ( 1
2 )
(δs,+ ± ˜ηδs,−)/
√
2
2
E2 ( 1
2 )
(±δs,+ −˜ηδs,−)/
√
2
3
A1(1)
(δs,+ −˜ηδs,−)/
√
2
3
A2(1)
(δs,+ + ˜ηδs,−)/
√
2
4
E2 ( 1
2 )
(δs,+ ∓˜ηδs,−)/
√
2
C4
[n, m, 0]
[n, n, m]
0+
A1(1)
1
0−
A2(1)
1
1
A1(1)
(δs,+ −˜ηδs,−)/
√
2
1
A2(1)
(δs,+ + ˜ηδs,−)/
√
2
2
A1(1)
(δs,+ + ˜ηδs,−)/
√
2
2
A2(1)
(δs,+ −˜ηδs,−)/
√
2
3
A1(1)
(δs,+ −˜ηδs,−)/
√
2
3
A2(1)
(δs,+ + ˜ηδs,−)/
√
2
4
A1(1)
(δs,+ + ˜ηδs,−)/
√
2
4
A2(1)
(δs,+ −˜ηδs,−)/
√
2
TABLE IX. Subduction coeﬃcients, S ˜η,λ
Λ,µ, for integer spin,
|λ| ≤4 and with s ≡sign(λ); other notation is deﬁned in the
text.
16 here we give expressions for creation operators
h
O[Λ1{⃗k1}⋆; Λ2{⃗k2}⋆]
Λµ
(⃗P)
i†
=
X
µ1,µ2⃗
k1∈{⃗k1}⋆⃗
k2∈{⃗k2}⋆⃗
k1+⃗k2=⃗P
C(⃗PΛµ;⃗k1Λ1µ1;⃗k2Λ2µ2)
h
OΛ1µ1(⃗k1)
i† h
OΛ2µ2(⃗k2)
i†
,
where Λ1,2(µ1,2) and Λ(µ) are respectively irreps(irrep rows) of LG(⃗k1,2) and LG(⃗P). C are the Clebsch-Gordan
coeﬃcients for Λ1({⃗k1}⋆) ⊗Λ2({⃗k2}⋆) →Λ(⃗P) which we discuss in the following section. The sum over⃗k1,2 is a sum
over all momenta in the stars of⃗k1,2, {⃗k1,2}⋆, i.e. all momenta related to⃗k1,2 by an allowed lattice rotation. In other
words, the sum is over R⃗k1,2 ∀R ∈OD
h ; the restriction that⃗k1 +⃗k2 =⃗P is equivalent to requiring R ∈LG(⃗P).
