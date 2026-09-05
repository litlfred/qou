---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-014-35-extension-lemmas
section_title: "Extension lemmas"
section_number: 3.5
pages: 16-18
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
Lemma 3.4. Let (C•,d +
• ) be a h-equivariant complex
C0
d+
1
←−−C1
d+
2
←−−...
d+
ℓ
←−−Cℓ
of C[Z] modules and F∈ C[Z]h such that
(1) Elements of Hom<0
d+ (C•,C •) are homotopic to 0
(2) The element F∈ Hom0
d+ (C•,C •) is homotopic to 0.
Then there are homomophisms d−
ij :Ci→Cj , i>j of C[Z]-modules such that
[(C•,d + +d−)]per∈ MF(Z,F )
and there are homomorphisms of C[Z], ∂−
ij : Λ •h⊗Ci→ Λ <•h⊗Cj, j >i such that
[(C•,d − +d+,∂ −)]per∈ MFh(Z,F ).
We do not provide a proof of this lemma since it is a particular case of a m ore general statement that is
proven below. The more general statement is an equivariant versio n of lemmas 3.1 and 3.2.
Let Mod h
per(Z) be a category of Z2-graded free C[Z] modules with endomorphisms equipped with h-
equivariant structure. That is an object F∈ Modh
per(Z) is the triple (M,D,∂ ),M =M 0⊕M 1,M i = C[Z]⊗
W i where W i∈ Modh, D∈ HomC[Z](M 1,M 0)⊕ HomC[Z](M 0,M 1), ∂ = ∑
i>j∂ij, ∂ij∈ HomC[Z](Λ ih⊗
M, Λ jh⊗M ).
The h-action on Mi is deﬁned by the Hopf formula and using this action one deﬁne diﬀeren tial dce
on CE h⊗
∆
M . The space of morphism between two objects ( M,D,∂ ), ( ˜M, ˜D, ˜∂)∈ Modh
per(Z) consists of
morphisms Ψ ∈ HomC[Z](M, ˜M ) that intertwine the endomorphisms:
Ψ◦ (D +dce +∂) = ( ˜D + ˜dce + ˜∂)◦ Ψ.
We do not require h-equivariance for the morphisms in the category and we do not requ ire h-equivariance of
D.
Similarly we deﬁne Com h
per(Z) to be the category of (not necessarily h-equivariant) complexes of objects
of Mod h
per(Z), we do not impose h-equivariance conditions on the morphisms and homotopies in Com h
per(Z).
In this setting we have the following equivariant version lemma 3.1,3.2:
Lemma 3.5. Let (F•,d +
• ),Fi = (Mi,D i,∂ i) be an element of Comh,ℓ
per(Z) and F∈ C[Z]h such that
(1) Elements of Hom<0
d+ (F•,F•) are homotopic to 0
(2) Element F−D2∈ Hom0
d+ (F•,F•) is homotopic to 0
16
(3) Element F− (D +∂ +dce)2∈ Hom0
d+(CEh⊗
∆
F•, CEh⊗
∆
F•) is homotopic to 0.
Then there are maps d−
ij :Fi→F j, i>j of elements of Modper(Z) such that
[(F•,d + +D +d−)]per∈ MF(Z,F )
and there are maps of elements of Modper(Z), ∂−
ij : Λ •h⊗F i→ Λ <•h⊗F j, j >i such that
[(F•,D +d− +d+,∂ +∂−)]per∈ MFh(Z,F ).
Proof. In the proof we would use short hand notations Hom i, Hom i
d+ for space morphisms Hom i(F•,F•)
and Homi
d+(F•,F•). We also assume that we have chosen the signs in our construction ofd+ in such that the
equivariance condition is equivalent to [d++D,d ce+∂]+ = 0. Given linear map A∈ Hom(CEh⊗
∆
F•, CEh⊗
∆
F•)
we denote by [ A]k the part of A that is in Hom(CE h, CEh)⊗ Homi.
As ﬁrst step of our construction we apply the lemma 3.1 to construc t diﬀerentials d−
ij :Fi→F j such that
[(F•,D +d+ +d−)]per∈ MF(Z,F ).
By the ﬁrst step and the assumption of the lemma we have
(d+ +d− +D +∂ +dce)2−F = [d+ +d− +D,∂ +dce]+
+ (∂ +dce)2∈ Hom(Λ ∗h, Λ ∗h)⊗ Hom≤0.
Since∂ +dce∈ Hom(Λ •h, Λ <•h)⊗ Hom0, we conclude that there is h(−1)∈ Hom(Λ •h, Λ <•h)⊗ Hom−1 such
that [h(−1),d +]+ = (∂ +dce)2 and hence
d(−1) := (d+ +d− +D +∂ +dce)2−F− [h(−1),d +]+
= [d−,∂ +dce]∈ Hom(Λ ∗h, Λ ∗h)⊗ Hom<0.
Let us deﬁne D(0) :=d+ +D +∂ +dce +d− +h(−1) then we see that
(D(0))2−F =d(−1) + [h(−1),d − +D +∂ +dce]+ + (h(−1))2∈ Hom(Λ •h, Λ <•)⊗ Hom<0.
We have proved the seed of induction for the following statement. F or anyk there ish(k)∈ Hom(Λ •h, Λ <•h)⊗
Hom−k such that
(D(k))2−F∈ Hom(Λ •h, Λ <•h)⊗ Hom<−k, D (k) =D(k−1) +h(−k−1).
Suppose we have constructed D(k) and h(−i), i≤ k + 1. By induction assumption we have ( D(k))2 =
F + [(D(k))2]<−k and we see that
0 = [D(k), (D(k))2] = [D(k), [(D(k))2]<−k] = [d+, [(D(k))2)]−k−1]
+ [d+, [(D(k))2]<−k−1] + [D +∂ +dce +d− +
∑
i
h(−i), [(D(k))2]<−k].
the ﬁrst summand of the last expression is from Hom(Λ •h, Λ <•h)⊗ Hom−k and the last two summands are
from Hom(Λ •h, Λ <•h)⊗ Hom<−k. Hence [( D(k))2]−k−1∈ Hom−k−1
d+ and hence it is homotopic to 0 and thus
there is
h(−k−2)∈ Hom(Λ •h, Λ <•h)⊗ Hom−k−2
17
such that [(D(k))2]−k−1 = [d+,h (−k−2)]+. The diﬀerential D(k+1) =D(k) +h(−k−2) provides the induction
step.
By setting ∂− = ∑
ih(−i) we complete our proof. ✷
Lemma 3.6. Let (F•,d +
• ) be an element of Comh,ℓ(Z) andF∈ C[Z]H that satisfy conditions of the previous
lemma. Suppose there two sets of diﬀerentials d−, ˆd− :Fi→F j, ∂−
ij, ˆ∂ij : Λ •h⊗F i→ Λ <•h⊗F j, j >i such
that
[(F•,D +∂ +d+ +d− +dce +∂−)]per, [(F•,D +∂ +d+ +dce + ˆd− + ˆ∂−)]per∈ MF(Z,F )
then there is Ψ = ∑
i≤0 Ψ i, Ψ −i∈ Hom−i(CEh⊗
∆
F•, CEh⊗
∆
F•), Ψ 0 = Id, Ψ −1 = 0, such
Ψ◦ (D +∂ +d+ +d− +dce +∂−)◦ Ψ −1 =D +∂ +d+ + ˆd− +dce + ˆ∂−.
Proof. Let d0 =D +∂ +dce,d− =d− +∂− and Dtot =d+ +d0 +d−, ˆd− = ˆ∂− + ˆd−, ˆDtot =d+ +d0 + ˆd−.
Suppose we constructed Ψ −i∈ Hom−i(CEh⊗
∆
F•, CEh⊗
∆
F•),k >i≥ 0 such that Ψ (k) := ∑
0≤i<k Ψ −i satisﬁes
ˆDtot−D(k)
tot∈ Hom≥−k+1, D (k)
tot = Ψ (k)◦Dtot◦ (Ψ (k))−1.
Let us use notation ∆ = − ˆDtot +D(k)
tot then we have
0 = ( ˆDtot + ∆) 2− ( ˆDtot)2 = [[∆] −k+1,d +]+ + [[∆] ≤−k,d +]+ + [∆ ,d 0 + ˆd−]+ + ∆ 2.
Since the ﬁrst summand is from Hom −k+2 and the rest of summands are from Hom ≤−k+1 we get that
[[∆] −k+1,d +]+ = 0. Thus there is Ψ −k∈ Hom−k such that [∆] −k+1 = [d+, Ψ −k]. The element Ψ (k+1) :=
Ψ (k) + Ψ −k prove our inductive statement.
✷
