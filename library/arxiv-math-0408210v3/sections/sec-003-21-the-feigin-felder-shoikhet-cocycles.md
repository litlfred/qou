---
doc_id: arxiv-math-0408210v3
doc_title: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM"
section_id: sec-003-21-the-feigin-felder-shoikhet-cocycles
section_title: "The Feigin-Felder-Shoikhet cocycles"
section_number: 2.1
pages: 3-4
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
doc_brief: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
First, we recall that for any associative algebra A with a unit over a ﬁeld K (of character-
istic zero) we have a chain map φ N from the Hochschild cochain complex C •(A, A∗) with
coeﬃcients in the dual module A∗ to the Lie algebra cochain complex C •(glN (A); glN (A)∗)
with coeﬃcients in glN (A)∗
φ N (ψ )(M1 ⊗a1,...,M k ⊗ak)(M0 ⊗a0)
= 1
k!
∑
ν∈Sk
(−)νψ (aν(1) ⊗... ⊗aν(k))(a0)tr(M0Mν(1)...M ν(k)), (1)
where Ml ∈ glN (K), al ∈ A, and ψ ∈C k(A, A∗) .
Let V be a 2n-dimensional vector space (over C) endowed with a symplectic form B. Let
{y1,...,y 2n} be a basis in V. We denote by ||Bij||, (i,j = 1,..., 2n) the matrix
Bij =B(yi,y j)
of the form B in this basis. Let ε be the completely antisymmetric Liouville tensor whose
components εi1...i 2n are deﬁned in the basis {y1,...,y 2n} as follows
εi1...i 2n = (−1)n
n!
∑
ν∈S2n
(−)νBiν (1)iν (2)...B iν (2n− 1)iν (2n). (2)
3
Deﬁnition 1 The Weyl algebra W associated with the symplectic vector space V is the vector
space C[[V]]((ℏ)) of the formally completed symmetric algebra of V equipped with the following
(associative) multiplication
(a ◦b)(y, ℏ) = exp
( ℏ
2Bij ∂
∂y i
∂
∂z j
)
a(y, ℏ)b(z, ℏ)|y=z. (3)
One can easily see that the multiplication deﬁned by (3) does not depe nd on the choice of a
basis in V. We view W as an algebra over the ﬁeld C((ℏ)) .
The Weyl algebra W is naturally ﬁltered with respect to the degree of monomials 2[ ℏ]+[y]
where [ ℏ] is a degree in ℏ and [y] is a degree in y
... ⊂ W 1 ⊂ W 0 ⊂ W −1... ⊂ W ,
W m = {a =
∑
2k+p≥m
ℏkak;i1...i pyi1...y ip} (4)
This ﬁltration deﬁnes the 2[ ℏ] + [y]-adic topology in W.
In [10] Feigin, Felder, and Shoikhet proposed an explicit expression f or the (2n)th Hoch-
schild (continuous) cocycle of the Weyl algebra W with coeﬃcients in the dual module
W ∗. Their formula is reminiscent of Kontsevich’s construction of the st ructure maps of his
celebrated formality quasi-isomorphism [13]. However, unlike the inte grals in Kontsevich’s
construction [13] the coeﬃcients entering the formula of Feigin, Fe lder, and Shoikhet are
rational.
Following [10] we start with the 2 n-th simplex ∆ 2n = {(u1,...,u 2n) ∈ R2n | 0 ≤u1... ≤
u2n ≤ 1} with the standard orientation and denote by Bbc the action of the form B on the
b-th and c-th components of W ⊗(2n+1)
Bbc(a0 ⊗... ⊗a2n) =
Bij(a0 ⊗... ⊗∂ab
∂y i ⊗... ⊗ ∂ac
∂y j ⊗... ⊗a2n), a b ∈ W .
Furthermore, we denote by π2n the action of the Liouville tensor (2)
π2n(a0 ⊗... ⊗a2n) = εi1...i 2na0 ⊗ ∂a1
∂y i1
⊗... ⊗ ∂a2n
∂y i2n
.
Finally, if we denote by µ the natural projection from ( W ⊗(2n+1)) onto C((ℏ))
µ(a0 ⊗... ⊗a2n) = a0(0)...a 2n(0)
the Feigin-Felder-Shoikhet formula of the 2 n-th Hochschild cocycle τ2n ∈C 2n(W, (W)∗) can
be written as [10]
τ2n(α )(a0) = µ 2n
( ∫
∆ 2n
∏
0≤b≤c≤2n
e
ℏ
