---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-052-91-introduction
section_title: "Introduction"
section_number: 9.1
pages: 79-84
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
---
Despite the wide range of proposals to simplify the standard model, most schemes tend
to share the same impedances. Few uniﬁed models naturally oﬀer more than a single
generation of particles, and few are able to evade proton decay without repercussion.
In previous chapters, we were also concerned with ﬁnding just a one-generation model
of particle physics, based on C⊗ O. However, this begs the question: could C⊗ O provide
room for three?
In this chapter, we point out a somewhat mysterious appearance of SU (3)c represen-
tations, which exhibit the behaviour of three full generations of standard model particles.
These representations are found in the Cliﬀord algebra Cl(6), arising from the complex
octonions. Back in Section 6.3, we explained how this 64-complex-dimensional space came
about. With the algebra in place, we will now identify new generators of SU (3) within
it. These SU (3) generators then act to partition the remaining part of the 64-dimensional
Cliﬀord algebra into six triplets, six singlets, and their antiparticles. That is, the algebra
mirrors the chromodynamic structure of exactly three generations of the standard model’s
quarks and leptons.
Passing from particle to antiparticle, or vice versa, requires nothing more than eﬀecting
the complex conjugate, ∗: i↦→− i. The entire result is achieved using only the eight-
dimensional complex octonions as a single ingredient.
71
The purpose of this chapter is not to oﬀer a completed uniﬁed gauge theory, or even a
completed description of QCD. Instead, we propose a gateway from which such a theory
might be found.
To the best of this author’s knowledge, [35] was the ﬁrst account of these three-
generation results found either within the octonions, or Cl(6).
9.2 Generators of SU (3)c
As mentioned earlier, the automorphism group of the octonions is G2, which is a 14-
dimensional exceptional Lie group. Within G2, we may ﬁnd a subgroup, SU (3), which
is deﬁned as that subgroup of G2 which keeps the imaginary unit, e7, invariant. The Lie
algebra of this SU (3), acting on f∈ C⊗ O may be expressed as
Λ1f = i
2
(
e1 (e5 f )−e3 (e4 f )
)
,
Λ2f =−i
2
(
e1 (e4 f ) +e3 (e5 f )
)
,
Λ3f = i
2
(
e4 (e5 f )−e1 (e3 f )
)
,
Λ4f = i
2
(
e2 (e5 f ) +e4 (e6 f )
)
,
Λ5f = i
2
(
e5 (e6 f )−e2 (e4 f )
)
,
Λ6f = i
2
(
e1 (e6 f ) +e2 (e3 f )
)
,
Λ7f = i
2
(
e1 (e2 f ) +e3 (e6 f )
)
,
Λ8f = i
2
√
3
(
e1 (e3 f ) +e4 (e5 f )− 2e2 (e6 f )
)
.
(9.1)
The Lie algebra’s commutation relations take the form
[
Λa
2 , Λb
2
]
f≡
[Λa
2
Λb
2 − Λb
2
Λa
2
]
f =icabc
Λc
2 f, (9.2)
∀f∈ C⊗ O, with the usual SU (3) structure constants, cabc.
Clearly, the Λi, as expressed above, constitute elements of C⊗← −O. In earlier references,
[41], [42], [26], these Λi are shown to act on quark and lepton representations in the eight-
dimensional C⊗ O, or multiple copies thereof. In contrast, here we introduce the Λi acting
on quark and lepton representations within the 64-dimensional C⊗← −O.
72
Taking a hint from [34], let us now introduce a related representation of su(3), which
will draw out structure in C⊗← −O, familiar from the behaviour of quarks and leptons.
Consider a resolution of the identity in C⊗← −O
1f = [ν +ν∗]f, (9.3)
where ν≡ 1
2(1 +i← −e7). Both ν and ν∗ act as projectors, whereby νν =ν, ν∗ν∗ =ν∗, and
νν∗ =ν∗ν = 0.
As [
Λn,ν
]
= 0 ∀n = 1... 8, (9.4)
equation (9.2) then leads to
[
Λa
2 ν, Λb
2 ν
]
=icabc
Λc
2 ν. (9.5)
That is, the eight 1
2Λnν form a representation of su(3). Taking the complex conjugate
of (9.5) gives
[
− Λ∗
a
2 ν∗,−Λ∗
b
2 ν∗
]
=icabc
[
−Λ∗
c
2 ν∗
]
, (9.6)
so that the− 1
2Λ∗
nν∗ give a further representation.
9.3 Three generations under SU (3)c
Knowing that the Λ nν behave as an eight dimensional representation under the action
of [Λmν, · ], one might wonder how objects of the more general form aν behave under
[Λmν, · ].
Obeying [Λmν,𝓁 jν] = 0 ∀m = 1... 8, we ﬁnd six SU (3) singlets, whose basis vectors
are given by
73
𝓁a≡ (1 +ie13 +ie26 +ie45)ν,
𝓁b≡ (3−ie13−ie26−ie45)ν,
𝓁c≡ (−ie124−e125 +e146−ie156)ν,
𝓁d≡ (−ie1−e3 +e126 +e145)ν,
𝓁e≡ (ie2 +e6 +e123 +ie136)ν,
𝓁f≡ (ie4 +e5−e134 +ie135)ν,
(9.7)
where the left-pointing arrows were dropped throughout for notational simplicity, and
right-to-left multiplication is still meant to occur. The notation eab is meant here to be
shorthand for ea(eb· ), etc.
The set of basis vectors
qR
1 ≡ (−ie12−e16 +e23 +ie36)ν
qG
1 ≡ (−ie24−e25 +e46−ie56)ν
qB
1 ≡ (ie14 +e15 +e34−ie35)ν
(9.8)
acts as a triplet under commutation with the Λ mν. Next, we ﬁnd ﬁve anti-triplets given
by
¯qR
2 ≡ (ie12−e16 +e23−ie36)ν
¯qG
2 ≡ (ie24−e25 +e46 +ie56)ν
¯qB
2 ≡ (−ie14 +e15 +e34 +ie35)ν,
(9.9)
¯qR
3 ≡ (ie4 +e5 +e134−ie135)ν
¯qG
3 ≡ (ie1 +e3 +e126 +e145)ν
¯qB
3 ≡ (ie2 +e6−e123−ie136)ν,
(9.10)
¯qR
4 ≡ (ie1−e3 +e126−e145)ν
¯qG
4 ≡ (−ie4 +e5 +e134 +ie135)ν
¯qB
4 ≡ (ie124−e125−e146−ie156)ν,
(9.11)
74
¯qR
5 ≡ (−ie2 +e6 +e123−ie136)ν
¯qG
5 ≡ (ie124−e125 +e146 +ie156)ν
¯qB
5 ≡ (ie4−e5 +e134 +ie135)ν,
(9.12)
¯qR
6 ≡ (ie124 +e125 +e146−ie156)ν
¯qG
6 ≡ (ie2−e6 +e123−ie136)ν
¯qB
6 ≡ (−ie1 +e3 +e126−e145)ν.
(9.13)
Taking the complex conjugate,∗: i↦→−i, of these 32 basis vectors gives 32 new linearly
independent basis vectors. Under commutation with −Λ∗
mν∗,
𝓁∗
a = (1−ie13−ie26−ie45)ν∗,
𝓁∗
b = (3 +ie13 +ie26 +ie45)ν∗,
𝓁∗
c = (ie124−e125 +e146 +ie156)ν∗,
𝓁∗
d = (ie1−e3 +e126 +e145)ν∗,
𝓁∗
e = (−ie2 +e6 +e123−ie136)ν∗,
𝓁∗
f = (−ie4 +e5−e134−ie135)ν∗
(9.14)
transform as SU (3) singlets,
qR∗
1 = (ie12−e16 +e23−ie36)ν∗≡ ¯qR
1
qG∗
1 = (ie24−e25 +e46 +ie56)ν∗≡ ¯qG
1
qB∗
1 = (−ie14 +e15 +e34 +ie35)ν∗≡ ¯qB
1
(9.15)
behaves as an anti-triplet,
¯qR∗
2 = (−ie12−e16 +e23 +ie36)ν∗≡qR
2
¯qG∗
2 = (−ie24−e25 +e46−ie56)ν∗≡qG
2
¯qB∗
2 = (ie14 +e15 +e34−ie35)ν∗≡qB
2
(9.16)
behaves as a triplet, and so on.
75
That is, unlike the standard model, we are able to pass back and forth between particle
and anti-particle using only the complex conjugatei↦→−i. This feature appeared early on
in the work of [41] for some internal degrees of freedom, and also in [34] and Section 3.5.3
when passing between left- and right-handed Weyl spinors.
