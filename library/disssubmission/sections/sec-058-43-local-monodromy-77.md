---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-058-43-local-monodromy-77
section_title: "Local monodromy 77"
section_number: 4.3
pages: 85-87
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
inserted to be conform with the graded pieces on the left).
... . . .
Gr2(Ψ1(δ)) P−2(δ)(−2)
N∼= Gr1(Ψ1(δ)) P−1(δ)(−1)
N∼= 
. . .
Gr0(Ψ1(δ)) P0(δ) P−2(δ)(−1)
N∼= Gr−1(Ψ1(δ)) P−1(δ) . . .
Gr−2(Ψ1(δ)) P−2(δ)
... . . .
The lower boundary entriesP0(δ),P−1(δ),P−2(δ), . . .of the triangle are the
graded pieces of the specialization
sp(δ) = ker(N : Ψ1(δ)→ Ψ1(δ)(−1)),
with P0(δ) as the top quotient. Accordingly the graded pieces ofsp(δ)
determine those of all theGri(Ψ1(δ)). Furthermore, in the case of mixed
perverse sheaves of geometric origin in the sense of [10, chapt. 6] we have
the following result due to O. Gabber [9, th 5.1.2].
REMARK 4.8. If δ is pure of weight w, then each Gri(Ψ1(δ)) is pure
of weight w+i so that the monodromy ﬁltration coincides with the weight
ﬁltration up to an index shift.
In this case, to compute the graded piecesGri(Ψ1(δ)) we only need
to determine the specializationsp(δ) and its weight ﬁltration. Returning
again to the general case, let us denote byj : Yη ↪→Y resp. i : Ys ↪→Y the
embedding of the generic resp. special ﬁbre. Recall [60, p. 48] that the
perverset-structure onY is deﬁned by
K∈ pD≤0(Y)⇐⇒i∗K∈ pD≤0(Ys) and j∗K∈ pD≤−1(Yη),
K∈ pD≥0(Y)⇐⇒i!K∈ pD≥0(Ys) and j∗K∈ pD≥−1(Yη).
We denote byP(Y) the abelian category of perverse sheaves which is the
core of the above perverset-structure. By abuse of notation we also writeδ
for the pull-back toP(Yη) of the perverse sheafδ∈ P(Yη). Then Artin’s
afﬁne vanishing theorem implies that the direct image complexesR j!(δ[1])
and R j∗(δ[1]) are perverse, see loc. cit. This being said, we deﬁne the
intermediate extension
j!∗(δ[1]) = im(R j!(δ[1])−→R j∗(δ[1]))
to be the image of the natural morphism between these two direct image
complexes in the abelian categoryP(Y).
78 Chapter 4 – The Tannaka group of the theta divisor
LEMMA 4.9. With notations as above, the specialization ofδ is given
by the formulae
sp(δ) = pH0(i∗R j∗(δ)) = i∗(j!∗δ[1])[−1].
Proof.We ﬁrst claim that in the triangulated categoryD(Ys) =Dbc (Ys,Λ),
the cone of the morphismN is given by
(⋆) Cone(Ψ1(δ) N−→Ψ1(δ)(−1)) = i∗R j∗(δ[1]).
Indeed, if we forget about weights, the cone ofN on Ψ1(δ) is isomorphic to
the cone ofT−1 onΨ(δ) becauseT−1 is an isomorphism onΨ⁄=1(δ) and
on Ψ1(δ) its kernel and cokernel are isomorphic to those ofN. Hence (⋆)
follows by the same argument as in [60, eq. (3.6.2) and thereafter], using
that by assumption the wild inertia groupP acts trivially onΨ(δ). Now if
for n∈{0,1} we write
spn(δ) = pHn(i∗R j∗(δ)),
we obtain from (⋆) an exact sequence of perverse sheaves
0−→sp0(δ)−→Ψ1(δ) N−→Ψ1(δ)(−1)−→sp1(δ)−→0.
Hence the ﬁrst equality in the lemma follows. For the second equality note
that we always havei∗ j!∗(δ[1]) = pτ<0i∗R j∗(δ[1]) by the basic properties
of the intermediate extension functor shown as in [65, sect. III.5.1], and
that again by (⋆) the sheaf complexi∗R j∗(δ[1]) is concentrated in perverse
cohomology degrees−1 and 0. □
To connect these local algebraic results to the more global setting of
section 4.4 below, it will be convenient to reset our notation. So letS be a
smooth complex algebraic curve andf : Y−→S a morphism of complex
algebraic varieties which is smooth over the complement of some given
points∈ S(C). Consider the strict Henselization˜S =Spec(Osh
S,s )−→S of S
at the points, and letη be the generic point of the strictly Henselian local
scheme ˜S. Referring to the base change
˜f : ˜Y = Y×S ˜S−→ ˜S
of the morphismf under this strict Henselization, we can form as above the
nearby cycles and specialization functors
P(Yη)
Ψ ))
sp
55 P(Ys)
