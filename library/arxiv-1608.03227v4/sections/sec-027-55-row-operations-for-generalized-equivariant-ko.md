---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-027-55-row-operations-for-generalized-equivariant-ko
section_title: "Row operations for generalized equivariant Koszul matrix factorizations"
section_number: 5.5
pages: 29-30
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
of the lemma 3.5 here and we also assume that the complex ( F•,d +) is the Koszul complex tensored with
matrix factorization (M,D,∂ ):
F• = ˜M⊗ Λ •V, d + =
n∑
j=1
fiθi,
whereθi form a basis of V andf1,...,f n form a regular sequence in C[Z]. We call such matrix factorizations
generalized equivariant Koszul matrix factorizations.
In these notations the corrective diﬀerentials that are computed by the iterative procedure from lemma 3.5
are of the form
d− =
∑
⃗i
d−
⃗i
∂
∂θ⃗i
, ∂ − =
∑
⃗i
∂−
⃗i
∂
∂θ⃗i
,
where θ⃗i =θi1...θ ik and d−
⃗i ∈Hom C[Z]( ˜M, ˜M ), ∂−
⃗i ∈Hom(Λ •n, Λ <•n)⊗Hom C[Z]( ˜M, ˜M ).
Let us use notation Dtot := d+ +D +∂ +d− +∂− +dce. There are three types of (generalized) row
transformations for the complex (F•,d ++D+d−,∂ +∂−). The ﬁrst type is given by automorphism exp( φ ∂
∂θk
),
φ∈ HomC[Z](F,F ) is an odd automorphism and the aﬀect of this automorphism on the d iﬀerential is:
(5.14) exp( −φ ∂
∂θk
)◦Dtot◦ exp(φ ∂
∂θk
) =
Å
D +d− +d+ + [φ,D ]+
∂
∂θk
+fkφ
ã
+dce +∂ +∂− + [φ,d ce +∂ +∂−]+
∂
∂θk
.
That is the result of the row transformation of the ﬁrst type is the equivariant matrix factorization
( ˜M,D +d− +d+ + [φ,D ]+
∂
∂θk
+fkφ,∂ +∂− + [φ,d ce +∂ +∂−]+
∂
∂θk
).
The second type elementary row transformation is given by conjug ation by the automorphism exp( φθ).
The result of conjugation of Dtot by this automorphims is the following expression
exp(−φθk)◦Dtot◦ exp(φθk) = Dtot +D′ +∂′.
(5.15) D′ = [φ,D ]+θk +
∑
k∈⃗i
d−
⃗i φ ∂
∂ ˆθ⃗i
+θk
∑
⃗i
[φ,d −
⃗i ] ∂
∂θ⃗i
,
(5.16) ∂′ =
∑
k∈⃗i
∂−
⃗i φ ∂
∂ ˆθ⃗i
+φdk
ce +θk(
∑
i
[φ,d i
ce] ∂
∂θi
+ [φ,∂ ]+ +
∑
⃗i
[φ,∂ −
⃗i ] ∂
∂θ⃗i
),
where ∂ ˆθ⃗i =∂θi1... ˆ∂θk...∂ im ,⃗i = (i1,...,i m) and dce = ∑
idi
ce
∂
∂θi
.
The computation above indicates that if last summands in (5.15) and ( 5.16) vanish
(5.17)
∑
⃗i
[φ,d −
⃗i ] ∂
∂θ⃗i
= 0,
∑
i
[φ,d i
ce] ∂
∂θi
+ [φ,∂ ]+ +
∑
⃗i
[φ,∂ −
⃗i ] ∂
∂θ⃗i
= 0
then result of the row transformation is the equivariant matrix fac torization:
( ˜M,d + +D +d− + [φ,D ]+θk +
∑
k∈⃗i
d−
⃗i φ ∂
∂ ˆθ⃗i
,∂ +∂− +
∑
k∈⃗i
∂−
⃗i φ ∂
∂ ˆθ⃗i
+φdk
ce)
Finally the third type of row operation is given by automorphism exp( cθi ∂
∂θj
) where c∈ HomC[Z](F,F )
is an even morphism. This type of row transformation was discussed in the subsection 2.3 for strongly
equivariant matrix factorizations. We will use these type row opera tions only for strongly equivariant matrix
29
factorization and omit a discussion about complications that arise fo r weakly equivariant generalized Koszul
complexes.
The key feature of the row transformations discussed here is tha t diﬀerentials that encode the equivariant
structure of the matrix factorization do not contribute to the ch ange of the non-equivariant shadow of the
matrix factorization. Other words, if T is one the transformations discussed above then
T (F )♯ =T (F ♯).
