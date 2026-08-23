---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-011-12-jianqiang-zhao
section_title: "Jianqiang Zhao"
section_number: 12
pages: 12-14
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
we assume σ1 ⁄= 1 and σp ⁄= 0. Set (σ1, . . . , σp, {0}n) = ( σ1, . . . , σq). Then
C({1}m, σ1, . . . , σp, {0}n)
=























0, if mn = p = 0;
Z
(
πcv(xσ1 · · ·xσp )
)
, if m = n = 0;
− 1
m
q∑
i=1
C({1}m−1, σ1, . . . , σi, 1, σi+1, . . . , σq), if m > 0;
− 1
n
p∑
i=1
C(σ1, . . . , σi−1, 0, σi, . . . , σp, {0}n−1), if m = 0, n > 0.
(16)
Here Z is deﬁned by (5) after using the identiﬁcation given by Remark 4.2.
Remark 4.4. This proposition provides the recursive relations one may u se to
compute all the coeﬃcients of I.
Proof. Since I is group-like one has
∆ I = I ⊗ I . (17)
The ﬁrst case follows from this immediately since C(0) = C(1) = 0. The second
case is essentially the deﬁnition (5) of Z. If m > 0 then one can compare the
coeﬃcient of x1 ⊗ xm−1
1 xσ1 · · ·xσq of the two sides of (17) and ﬁnd the relation
(16). Finally, if m = 0 and n > 0 then one may similarly consider the coeﬃcient
of xσ1 · · ·xσp xn−1
0 ⊗ x0 in (17). This ﬁnishes the proof of the proposition.
For any divisor d of N let Γ d = {σd : σ ∈ Γ }, id : Γ d֒→Γ the embedding, and
pd : Γ ։ Γ d the dth power map. They induce two algebra homomorphisms:
pd
∗ : Q⟨XΓ ⟩ − →Q⟨XΓ d⟩
xσ ↦− →
{
dx0, if σ = 0,
xσd , if σ ∈ Γ ,
and
i∗
d : Q⟨XΓ ⟩ − →Q⟨XΓ d⟩
xσ ↦− →





x0, if σ = 0,
xσ, if σ ∈ Γ d,
0, otherwise.
It is easy to see that both i∗
d and pd
∗ are ∆-coalgebra morphisms such that
i∗
d(I) and pd
∗(I) have the same image under the map πcv. By the standard
Lie-algebra mechanism one has
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 13
Proposition 4.5. ([26, Prop.2.26]) For every divisor d of N
pd
∗(I) = exp

 ∑
σd=1,σ⁄=1
Li1(σ)x1

 i∗
d(I). (18)
Combined with Proposition 4.3 the above result provides the so-called regular-
ized distribution relations (RDT) which of course include all the FDT of MPVs
given by (14).
However, sometimes FDT are not independent of the other rela tions. In the
next theorem one sees that when the weight w = 2 and level N is a prime, all
the distribution relations in (14), where xj = 1 for all j, are consequences of
RDS of MPVs of level N .
Theorem 4.6. For any prime p write L(i, j) = Lp(1, 1|i, j) and D(i) = Lp(2|i).
Deﬁne for 1 ≤ i, j < p :
FDT := −D(0) + p
p−1∑
j=0
D(j), RDS(i) := D(i) + L(i, 0) − L(i, −i),
FDS(i, j) := D(i + j) + L(i, j) + L(j, i) − L(i, j − i) − L(j, i − j).
Then one has
FDT =
∑
1≤i<p
FDS(i, i) + 2
∑
1≤j<i<p
FDS(i, j) + 2
p−1∑
i=1
RDS(i). (19)
Proof. When p = 2 the second term on the right hand side of (19) is vacuous.
Then it is easy to see that both sides of (19) are equal to D(0) + 2D(1).
We now assume p ≥ 3. Changing the order of summation yields that
2
∑
1≤j<i<p
D(i + j) =
p−1∑
i=2
i−1∑
j=1
D(i + j) +
p−2∑
j=1
p−1∑
i=j+1
D(i + j)
=
p−2∑
i=2
p−1∑
i⁄=j=1
D(i + j) +
p−2∑
j=1
D(j − 1) +
p−1∑
i=2
D(i + 1)
=(p − 3)
p−1∑
j=0
D(j) −
p−2∑
i=2
D(i) −
p−1∑
i=1
D(2i) +
p−2∑
j=1
D(j) +
p−1∑
j=2
D(j) + 2D(0)
=(p − 1)D(0) + (p − 3)
p−1∑
j=1
D(j)
since∑ p−1
j=0 D(i + j) =∑ p−1
j=0 D(j) for all i and∑ p−1
i=1 D(2i) =∑ p−1
i=1 D(i). This
implies that the dilogarithms on the right hand side of (19) e xactly add up to
Documenta Mathematica 15 (2010) 1–34
