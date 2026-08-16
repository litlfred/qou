---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-050-71-the-two-variable-colored-jones-invariant-part
section_title: "The two-variable colored Jones invariant. Part of the following overlaps"
section_number: 7.1
pages: 24-25
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
[17, Section 3.3], where some results are stated without pro ofs.
It follows from the results in the previous sections that we h ave
JK =JT =
∑
n≥0
JK(P ′′
n )σn∈Z( ˜U ev
q )∼
= lim
←−kZ[q,q −1][C2]/(σk).
ThusJK may be regarded as an invariant with two variables q and C. It is useful
to introduce variables t and α satisfying
α2 =C2− 4 = t +t−1− 2.
ThenZ( ˜U ev
q ) may be identiﬁed with
Λ := lim←−kZ[q,q −1][t +t−1]/(σk)∼
= lim
←−kZ[q,q −1][α2]/(σk),
where
σk =
k∏
i=1
(t +t−1−qi−q−i) =
k∏
i=1
(α2−qi−q−i + 2)
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 25
Remark 7.1. Λ can be naturally regarded as a subring of
˜Λ := lim←−kZ[q,q −1,t,t −1]/(σk)∼
= lim
←−kZ[q,q −1,t,t −1]/
( ∏
−k≤i≤k, i ⁄=0
(t−qi)
)
.
In fact, Λ consists of the elements of ˜Λ which are invariant under the involutive
continuous ring automorphism of ˜Λ deﬁned by f (q,t )↦→f (q,t −1).
By abuse of notation, we write
JK(t,q ) = JK∈ Λ .
Fori∈ Z, let
θi : Z[q,q −1][t +t−1]→ Z[q,q −1]
be the unique Z[q,q −1]-algebra homomorphism such that θi(t +t−1) = qi +q−i.
We have
θi(σk) =
k∏
j=1
(qi +q−i−qj−q−j).(7.1)
If i⁄= 0, then θi induces a homomorphism
ˆθi : Λ → Z[q,q −1],
since it follows from (7.1) that θi(σj ) = 0 for all j≥|i|. Since we have θi =θ−i, it
follows that ˆθi = ˆθ−i. By (6.5), it follows that for i> 0
θi(JK) = JK(qi,q ) = JK(V′
i−1),(7.2)
where V′
i−1 = Vi−1/[i]. Thus JK (qi,q ) ∈ Z[q,q −1] is the ( i− 1)st normalized
colored Jones polynomial. Hence, it may be natural to call JK(t,q )∈ Λ the two-
variable colored Jones invariant of K. For the comparison with the well-known,
two-variable power series expansion of the colored Jones po lynomials, known as the
Melvin-Morton expansion, see Section 7.2 below.
Now, consider the case i = 0. θ0 induces a continuous ring homomorphism
ˆθ0 : Λ → ˆZ[q], f (t,q )↦→f (1,q ),
since it follows from (7.1) that θ0(σk) = (−1)k({k}!2)∈ Z[q,q −1] is divisible by
(q)k
