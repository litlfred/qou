---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-012-33-quasi-r-matrix-and-commutativity-isomorphisms
section_title: "Quasi R-matrix and commutativity isomorphisms"
section_number: 3.3
pages: 14-16
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
{bµ,i} be a basis of U −
−µ. Let {bµ
i} be the dual basis of U +
µ with respect to the
pairing (2.8). Deﬁne
Rµ =
∑
i
bµ,i ⊗bµ
i ∈U − ⊗U +.
The element Rµ is independent of the chosen basis {bµ,i}. The quasi R-matrix
R =
∑
µ∈Q+
Rµ(3.4)
gives a well-deﬁned element U (2)
0 . Indeed, for M,N ∈Ob(Oint) only ﬁnitely many
summands Rµ act nontrivially on any element of M ⊗N .
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 15
Remark 3.5. The element R ∈ U (2)
0 coincides with the quasi-R-matrix deﬁned
in [Lus94, 4.1.4] and in [Jan96, 7.2] in the ﬁnite case. Those references use the
symbol Θ for the quasi-R-matrix, but we change notation to avoid conf usion with
the involutive automorphism Θ : h∗ → h∗ deﬁned in Section 5.1.
The quasi R-matrix has a second characterization in terms of the b ar involution
(2.23) of Uq(g). Deﬁne a bar involution on Uq(g) ⊗Uq(g) by u ⊗v = u ⊗v.
By [Lus94, Theorem 4.1.2] the quasi-R-matrix is the uniquely determin ed element
R = ∑
µ∈Q+Rµ ∈ ∏
µ∈Q+U −
−µ ⊗U +
µ with Rµ ∈ U −
−µ ⊗U +
µ and R0 = 1 ⊗ 1 for
which
∆( u)R =R∆( u) for all u ∈Uq(g).(3.5)
Moreover,R is invertible, with
R−1 =R.(3.6)
Remark 3.6. If g is of ﬁnite type then the quasi-R-matrix R can be factorized into
a product of R-matrices for sl2. Choose a reduced expression w0 =σi1...σ it for the
longest element w0 of W . For j = 1,...,t set γj =σi1σi2...σ ij−1 (αij ) and deﬁne
(3.7) Eγj =Ti1Ti2...T ij−1 (Eij ), F γj =Ti1Ti2...T ij−1 (Fij ).
Then {γ1,...,γ t} is the set of positive roots of g, and (3.7) are the root vectors used
in the construction of the PBW basis corresponding to the cho sen reduced expression
for w0. For j = 1,...,t deﬁne
R[j] =
∑
r≥0
(−1)rq−r(r−1)/2
ij
(qij −q−1
ij )r
[r]qij ! Fr
γj ⊗Er
γj(3.8)
and for i ∈I set Ri =R[j] if γj =αi. By [Jan96, Remark 8.29] one has
R =R[t] ·R[t−1] · · · · ·R[2] ·R[1].(3.9)
The quasi-R-matrix R and the transformation κ deﬁned in Example 3.4 give rise
to a family of commutativity isomorphisms. Deﬁne
ˆR =R ·κ−1 · ﬂip(3.10)
in U (2). By [Lus94, Theorem 32.1.5] the maps
ˆRM,N :M ⊗N →N ⊗M(3.11)
are isomorphisms of Uq(g)-modules for all M,N ∈ Ob(Oint). Moreover, the iso-
morphisms ˆRM,N satisfy the hexagon property
ˆRM,N ⊗N ′ = (idN ⊗ ˆRM,N ′)( ˆRM,N ⊗ idN ′ ),
ˆRM⊗M ′,N = ( ˆRM,N ⊗ idM ′ )(idM ⊗ ˆRM ′,N ′)
for all M,M ′,N,N ′ ∈ Ob(Oint), see [Lus94, 32.2]. This implies that Oint is a
braided tensor category as deﬁned for example in [Kas95, XIII.1.1 ].
Remark 3.7. In the construction of the commutativity isomorphisms ˆRM,N in
[Lus94, Chapter 32] it is assumed that g is of ﬁnite type. Moreover, Lusztig deﬁnes
the commutativity isomorphisms on tensor products of integ rable weight modules.
Lusztig’s arguments extend to the Kac-Moody case if one rest ricts to category O.
We retain the assumption of integrability so that the Luszti g automorphisms TiM
16 MARTINA BALAGOVI ´C AND STEF AN KOLB
given by (3.2) are well deﬁned. The restrictions imposed by ˆRM,N and TiM force
us to work with the category Oint.
It follows from the deﬁnitions of the completion U and the coproduct ∆ : U →
U (2) that in U (2) one has
ˆR · ∆( u) = ∆( u) · ˆR for all u ∈ U.(3.12)
In the proof of the next Lemma we will use this property for u =Ti. Moreover, by
[Lus94, Proposition 5.3.4] the Lusztig automorphisms Ti ∈ U satisfy
∆(Ti) = Ti ⊗Ti ·R−1
i(3.13)
where Ri was deﬁned just below (3.8). To generalize the above formula we rec all
the following well known lemma, see for example [CP94, Proposition 8.3.1 1]. We
include a proof to assure that we have the correct formula in our co nventions. Recall
that for g of ﬁnite type w0 ∈ W denotes the longest element. Deﬁne, moreover,
R21 = ﬂip ·R · ﬂip ∈ U (2)
0 .
Lemma 3.8. Assume that g is of ﬁnite type. Then the relations
∆(Tw0 ) = Tw0 ⊗Tw0 ·R−1,(3.14)
∆(T −1
w0 ) = T −1
w0 ⊗T −1
w0 ·κ ·R21 ·κ−1(3.15)
hold in U (2)
0 .
Proof. First observe that Equations (3.14) and (3.15) are equivalent. Ind eed, Equa-
tion (3.12) for u =Tw0 implies that Equation (3.14) is equivalent to
ˆR ·∆(Tw0) = κ−1 · ﬂip ·Tw0 ⊗Tw0.
The inverse of the above equation is (3.15). It remains to verify tha t (3.15) holds.
Applying the equivalence between (3.14) and (3.15) to (3.13) one obt ains
∆(T −1
i ) = T −1
i ⊗T −1
i ·κ ·Ri21 ·κ−1
where Ri21 = ﬂip ·Ri · ﬂip. Hence for Tw0 =Ti1Ti2...T it one has
∆(T −1
w0 ) = ∆(T −1
it ) · · · · ·∆(T −1
i2 ) ·∆(T −1
i1 )
=T −1
it ⊗T −1
it ·κ ·Rit 21 ·κ−1 · · · · ·T −1
i1 ⊗T −1
i1 ·κ ·Ri1 21 ·κ−1
=T −1
w0 ⊗T −1
w0 ·κ ·R[t]
21 ·R[t−1]
21 · · · · ·R[2]
21 ·R[1]
21 ·κ−1
where R[j]
21 = ﬂip ·R[j] · ﬂip. By (3.9) one obtains relation (3.15). □
