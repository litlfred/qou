---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-015-36-lifting-lemma-for-morphisms
section_title: "Lifting lemma for morphisms"
section_number: 3.6
pages: 18-20
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
facts about our lifting procedure.
Lemma 3.7. Suppose we are are given (F•,d +
• ),Fi = (Mi,D i) and ( ˜F•, ˜d+
• ), ˜Fi = ( ˜Mi, ˜Di) be an element
of Comh,ℓ
per(Z) and F ∈ C[Z]h such that they satisfy conditions of lemma 3.5 and ∂,d −, ˜∂, ˜d− are as in
conclusion of lemma 3.5. Let us also assume that elements of Hom<0
d+, ˜d+(F•, ˜F•) are homotopic to 0
Suppose also that there is a map Ψ ∈ Homk(CEh⊗
∆
F•, CEh⊗
∆
˜F•), k≤ 0 such that ˜d+◦ Ψ = −Ψ◦d+ and
( ˜D + ˜dce +∂)◦ Ψ − Ψ ◦ (D +dce + ˜∂) is d+, ˜d+ homotopic to 0. Then there are h-equivariant elements
Ψ i∈ Homk−i(CEh⊗
∆
F•, CEh⊗
∆
˜F•), i> 0 such that
˜Dtot◦ (Ψ +
∑
i
Ψ i) = (Ψ +
∑
i
Ψ i)◦Dtot,
˜Dtot := ˜d+ + ˜D +∂ + ˜d− + ˜dce + ˜∂−, D tot :=d+ +D +∂ +dce +∂−,
The elements Ψ i are unique up-to the homotopy: if
Ψ ′
i∈ Homk−i(CEh⊗
∆
F•, CEh⊗
∆
˜F•)
is another collection of elements satisfying previous equa tion then there is h such that
∑
i
Ψ i− Ψ ′
i = ˜Dtot◦h−h◦Dtot
18
Proof. Let us introduce short-hand notations d0 = D +∂ +dce and ˜d0 = ˜D + ˜∂ + ˜dce, d− = d− +∂−,
˜d− = ˜d− + ˜∂−. We also use notations Hom i, Hom i
d+ as in the previous lemmas.
First let us notice that
˜Dtot◦ Ψ− Ψ◦Dtot =
Ä ˜d0◦ Ψ− Ψ◦d0
ä
+
Ä ˜d−◦ Ψ− Ψ ◦d−
ä
.
The ﬁrst summand is homotopic to 0 by the theorem assumption and t he second term is from Hom <k and
[d+, ˜d−◦ Ψ− Ψ◦d−] = [d+, ˜d−]+◦ Ψ− Ψ◦ [d+,d −]+ = (F− ˜d2
0)◦ Ψ− Ψ ◦ (F−d2
0) = 0.
Thus there are maps Ψ 1 ∈ Homk−1, Ψ 2 ∈ Homk−2 such that [ d+, Ψ 2]+ = [ ˜d−◦ Ψ − Ψ ◦d−]k−1 and
[d+, Ψ 1]+ = ˜d0◦ Ψ− Ψ ◦d0. Hence Ψ (2) = Ψ + Ψ 1 + Ψ 2 such that
˜Dtot◦ Ψ (2)− Ψ (2)◦Dtot∈ Hom≤k−2.
That is the seed to the inductive construction of Ψ (m) = Ψ + ∑ m
i=1 Ψ m such that
˜Dtot◦ Ψ (m)− Ψ (m)◦Dtot∈ Hom≤k−m.
To prove the step of induction we observe that
˜Dtot◦
Ä ˜Dtot◦ Ψ (m)− Ψ (m)◦Dtot
ä
−
Ä ˜Dtot◦ Ψ (m)− Ψ (m)◦Dtot
ä
◦Dtot = 0
because D2
tot =F and ˜Dtot =F . If we denote by R the expression ˜Dtot◦ Ψ (m)− Ψ (m)◦Dtot then we get:
0 = ˜Dtot◦R−R◦Dtot = [d+, [R]k−m] +
Ä
( ˜d0 + ˜d−)◦ [R]k−m
−[R]k−m◦ (d0 +d−)) +
Ä ˜Dtot◦ [R]<k−m− [R]<k−m◦Dtot
ä
.
Since the ﬁrst summand of the last expression is from Hom k−m+1 and the last two terms are from Hom ≤k+m
we conclude that [ d+, [R]k−m] = 0. Thus [ R]k−m∈ Homk−m
d+ and there is Ψ m+1∈ Homk−m−1 such that
[R]k−m = [Ψ m+1,d +]+. Hence Ψ (m+1) = Ψ (m) + Ψ m+1 proves the induction step.
The last part of the lemma follows from the following statement. Supp ose Ψ ∈ Hom<k, k≤ 0 is such
that ˜Dtot◦ Ψ = Ψ ◦Dtot then there is h∈ Hom<k+1 such that Ψ ′ = Ψ − ( ˜Dtot◦h +h◦Dtot)∈ Hom<k−1.
Indeed, since
˜DtotΨ ′− Ψ ′◦Dtot = ( ˜Dtot)2◦h−h◦ (Dtot)2 = 0,
we can run inductive argument and construct g such that Ψ = ˜Dtot◦g +g◦Dtot.
The statement itself follows from the computation below:
0 = ˜Dtot◦ Ψ− Ψ◦Dtot = [d+, [Ψ] k−1] +
Ä
( ˜d0 + ˜d−)◦ [Ψ] k−1]
−[Ψ] <k−1◦ (d0 +d−)) +
Ä ˜Dtot◦ [Ψ] <k−1− [Ψ] <k−1◦Dtot
ä
since the ﬁrst summand is from Hom k and the other summands are from Hom <k and thus [d+, [Ψ] k−1] = 0
and [Ψ] k−1 is homotopically trivial with respect to d+. It is easy to check that h, such that [d+,h ]− = [Ψ] k−1
provides a proof of the statement. ✷
19
