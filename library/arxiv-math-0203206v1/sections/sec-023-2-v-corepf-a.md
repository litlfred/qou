---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-023-2-v-corepf-a
section_title: "V ∈ Corepf (A, ∆) ,"
section_number: 2
pages: 19-20
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
3. πV =πV . (Here it is understood that the same J :K →K is used in both constructions.)
Proof. To prove 1., observe that
(ω ⊗ι)VJ ∗J =πV (ω)πV ( ˆf −1) = πV (ω ˆf −1) = πV ( ˆf −1)πV ( ˆfω ˆf −1)
=J ∗JπV ( ˆS2(ω)) = J ∗J( ˆS2(ω) ⊗ι)V =J ∗J(ω ⊗ι)(S2 ⊗ι)V
for all ω ∈ ˆA.
To prove 3., note ﬁrst that ˆS(ω)(a) = ωS (a) and ω∗(a) = ω(S(a)∗) for all a ∈ A and ω ∈ ˆA. Writing
V =∑
kak ⊗xk we compute
∑
k
ˆS(ω∗)(ak)xk =
∑
k
ω∗S(ak)xk = (ω∗ ⊗ι)(S ⊗ι)V = (ω∗ ⊗ι)(V ∗)
=
∑
k
ω∗(a∗
k)x∗
k =
∑
k
ω(S(a∗
k)∗)x∗
k =
∑
k
ωS −1(ak)x∗
k.
Since (S ⊗ι)V =V ∗, we thus obtain
πV (ω) = JπV ˆS(ω∗)J −1 =J( ˆS(ω∗) ⊗ι)VJ −1 =
∑
k
J( ˆS(ω∗)(ak)xk)J −1 =
∑
k
J(ωS −1(ak)x∗
k)J −1
=
∑
k
ωS −1(ak)Jx ∗
kJ −1 = (ω ⊗ι)(S−1 ⊗j)(
∑
k
ak ⊗xk) = (ω ⊗ι)(S−1 ⊗j)V =πV (ω)
for all ω ∈ ˆA, proving 3. Now 3., together with Proposition 3.5 and Proposition 3.21 , imply 2., completing the
proof. ■
This suggests the following proposition, which is a formulation more int rinsic to the category Corep f (A, ∆).
19
Proposition 3.23 Let (A, ∆) be a compact aqg and V ∈ Corepf (A, ∆) be non-zero. Pick a ﬁnite dimensional
Hilbert space K and any antilinear map J : K → K such that V (1 ⊗J ∗J) = (1 ⊗J ∗J)(S2 ⊗ι)V . Then
V ∈ A ⊗B(K) given by V = (S−1 ⊗j)V belongs to Corepf (A, ∆) . It is a conjugate of V with normalized
solutions r ∈ Hom(1 ⊗ 1,V ×V ), r ∈ Hom(1 ⊗ 1,V ×V ) of the conjugate equations for V and V given by
r(1) =
∑
i
Jei ⊗ei and r(1) =
∑
i
ei ⊗J ∗−1ei.
Proof. The irreducible case follows from Proposition 3.21, Theorem 3.14 and t he fact that J ∗J is the unique (up
to a positive scalar) positive operator in B(K) with the property V (1 ⊗J ∗J) = (1 ⊗J ∗J)(S2 ⊗ι)V [40, 30]. We
content ourselves with proving one of the least obvious parts of th e proposition, namely that r, deﬁned above,
belongs to Hom(1 ⊗ 1,V ×V ). In other words we must show that r(ω ⊗ι)(1 ⊗ 1) = ( ω ⊗ι ⊗ι)(V ×V )r or
ω(1)r(1) = (ω⊗ι⊗ι)(V ×V )r(1) for allω ∈ ˆA. Write V =∑
kak⊗xk ∈A⊗B(K), soV =∑
kS−1(ak)⊗Jx ∗
kJ −1.
For any ω ∈ ˆA and any elements ej,er in the chosen orthonormal basis for K, we then get
((ω ⊗ι ⊗ι)(V ×V )r(1),J ∗−1ej ⊗er) =
∑
i
((ω ⊗ι ⊗ι)(V 12V13)(Jei ⊗ei),J ∗−1ej ⊗er)
=
∑
ikl
ω(S−1(ak)al)(Jx ∗
kJ −1Jei,J ∗−1ej)(xlei,er) =
∑
ikl
ω(S−1(ak)al)(Jx ∗
kei,J ∗−1ej)(xlei,er)
=
∑
ikl
ω(S−1(ak)al)(ej,x ∗
kei)(xlei,er) =
∑
ikl
ω(S−1(ak)al)(xkej,ei)(xlei,er)
=
∑
kl
ω(S−1(ak)al)(xl
∑
i
(xkej,ei)ei,er) =
∑
kl
ω(S−1(ak)al)(xlxkej,er)
=
∑
kl
ωS −1(S(al)ak)(xlxkej,er) =
∑
kl
ωS −1(a∗
lak)(x∗
lxkej,er)
= ( ωS −1 ⊗ωej,er )(V ∗V ) = ( ω ⊗ωej,er )(1 ⊗ 1) = ω(1)(ej,er)
=
∑
i
ω(1)(Jei,J ∗−1ej)(ei,er) = ( ω(1)r(1),J ∗−1ej ⊗er),
where
ωej,er : B(K) → C, x ↦→(xej,er).
Thus
(ω ⊗ι ⊗ι)(V ×V )r(1) = ω(1)r(1),
completing the proof. ■
Remark 3.24 In the last two results, the conjugates can be expressed alterna tively in terms of the unitary
antipode R and an antiunitary J [5]. ✷
