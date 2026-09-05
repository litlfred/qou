---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-045-83-action-on-a-subfactor-equation-73-suggests-th
section_title: "Action on a subfactor. Equation (73) suggests the following deﬁnition of"
section_number: 8.3
pages: 35-36
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
the action of B on M1.
Proposition 8.3.1. The map ⊲ :B ⊗CM1 →M1 :
b⊲x =λ−1EM1 (bxe2)(74)
deﬁnes a left action of B on M1 (cf. [S], Proposition 17).
Proof. The above map deﬁnes a left B-module structure on M1, since 1⊲x =x and
b⊲ (c⊲x ) = λ−2EM1 (bEM1 (cxe2)e2) = λ−1EM1 (bcxe2) = (bc)⊲x.
Next, using equation (73) we get
b⊲xy = λ−1EM1 (bxye2) = λ−2EM1 (b(1)xe2)EM1 (b(2)ye2)
= ( b(1)⊲x )(b(2)⊲y ).
By [NV2], 4.4 and properties of SB we also get
S(b)†⊲x ∗ = λ−1EM1 (S(b)†x∗e2) = λ−1EM1 (SB(w)−1SB(wbw−1)∗SB(w)x∗e2)
= λ−1EM1 (SB(b∗)x∗e2) = λ−1EM1 (e2x∗b∗)
= λ−1EM1 (bxe2)∗ = (b⊲x )∗.
Finally,
b⊲ 1 = λ−1EM1 (be2) = λ−1EM1 (λ−1EM1 (be2)e2) = εt(b)⊲ 1,
and b⊲ 1 = 0 iﬀ εt(b) = λ−1EM1 (be2) = 0.
Proposition 8.3.2. M B
1 =M , i.e. M is the ﬁxed point subalgebra of M1.
36 DMITRI NIKSHYCH AND LEONID V AINERMAN
Proof. If x ∈ M1 is such that b⊲x = εt(b)⊲x for all b ∈ B, then EM1 (bxe2) =
EM1 (εt(b)xe2) = EM1 (be2)x. Taking b =e2, we get EM (x) = x which means that
x ∈M . Thus, M B
1 ⊂M .
Conversely, if x ∈M , then x commutes with e2 and
b⊲x =λ−1EM1 (be2x) = λ−1EM1 (λ−1EM1 (be2)e2x) = εt(b)⊲x,
therefore M B
1 =M .
Proposition 8.3.3. The map θ : [ x ⊗ b] ↦→xS(w)1/2bS(w)−1/2 deﬁnes a von
Neumann algebra isomorphism between M1>⊳B and M2.
Proof. By deﬁnition of the action ⊲ we have :
θ([x(z⊲ 1) ⊗b]) = xS(w)1/2λ−1EM1 (ze2)bS(w)−1/2
= xS(w)1/2zbS (w)−1/2 =θ([x ⊗zb]),
for all x ∈ M1, b∈ B, z ∈ Bt, so θ is a well deﬁned linear map from M1>⊳B =
M1 ⊗BtB to M2. It is surjective since an orthonormal basis of B =M ′ ∩M2 over
Bt = M ′ ∩M1 is also a basis of M2 overM1 ([Po], 2.1.3). Finally, one can check
thatθ is a von Neumann algebra isomorphism ([NV2], 6.3).
Remark 8.3.4. (i) The action of B constructed in Proposition 8.3.1 is minimal,
since we have M ′
1 ∩M1>⊳B =M ′
1 ∩M2 =Bs by Proposition 8.3.3.
(ii) If N ′ ∩M = C, then B is a usual Kac algebra (i.e., a Hopf C∗-algebra) and
we recover the well-known result proved in [S], [L], and [D].
(iii) It is known ([Po], Section 5) that there are exactly 3 non-isomorp hic subfactors
of depth 2 and index 4 of the hyperﬁnite II 1 factorR such that N ′ ∩M ⁄= C.
One of them is R ⊂ R ⊗C M2(C), two others can be viewed as diagonal
subfactors of the form
{
(
x 0
0 α(x)
)
|x ∈R} ⊂ R ⊗M2(C),
where α is an outer automorphism of R such that α2 = id, resp. α2 is inner
and α2 ⁄= id.
An explicit description of the corresponding quantum groupoids can be
found in ([NV1], 3.1, 3.2), ([NV2], 7). Also, in ([NV2], 7) we describe the
C∗-quantum groupoid B = M2(C) ⊕M3(C) corresponding to the subfactor
with the principal graph A3 ([GHJ], 4.6.5) having the index λ−1 = 16 cos4 π
5 .
