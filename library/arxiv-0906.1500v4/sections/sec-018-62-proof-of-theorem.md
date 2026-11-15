---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-018-62-proof-of-theorem
section_title: "Proof of Theorem"
section_number: 6.2
pages: 16-19
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
and some notation.
Let C∗= C∗(M; sl2(C)ρ) and C∗(t) = C∗(M; sl2(C(t))ρ). We deﬁne a pair of com-
plexes (C′
∗, C′
∗(t)) as follows. The complex C′
∗is deﬁned as a subchain complex of C∗
which is a lift of the homology group Hρ
∗(M) = H∗(M; sl2(C)ρ). This is a “degener-
ated complex” in the sense that the boundary operators are all zero. More precisely,
C′
3 = C′
0 = 0 for conventions, C′
2 is spanned (over C) by {P ρ
ℓ⊗T 2
ℓ| 1 ⩽ℓ⩽b}, and
C′
1 is spanned (over C) by {P ρ
ℓ⊗λℓ| 1 ⩽ℓ⩽b}. Similarly as C∗(t), we deﬁne C′
∗(t) by
changing the coeﬃcient from sl2(C) to sl2(C(t)) = C(t) ⊗sl2(C), in particular C′
1(t) is
spanned by {1 ⊗P ρ
ℓ⊗λℓ| 1 ⩽ℓ⩽b} and C′
2(t) is spanned by {1 ⊗P ρ
ℓ⊗T 2
ℓ| 1 ⩽ℓ⩽b}.
Observe that C′
∗(t) is a subchain complex of C∗(t). More precisely, one has:
(17)
C′
∗(t) = 0 →C′
3(t) →C′
2(t)
∂′
−→C′
1(t) →C′
0(t) →0
where the boundary operator ∂′ works as follows:
∂′ : (1 ⊗P ρ
ℓ) ⊗T 2
ℓ7→(tai −1) · (1 ⊗P ρ
ℓ) ⊗λℓ.
Finally, we deﬁne C′′
∗as the quotient complex C∗/C′
∗and C′′
∗(t) = C∗(t)/C′
∗(t). Hence
we have the two following exact sequence of complexes:
(18)
0 →C′
∗→C∗→C′′
∗→0.
(19)
0 →C′
∗(t) →C∗(t) →C′′
∗(t) →0.
As we already observe, the complexes C′
∗, C∗are not acyclic and we completely know
their homology groups. The homology of C′′
∗is given in the following claim.
Lemma 7. The complex C′′
∗is acyclic.
Proof of the claim. Write down the long exact sequence in homology associated to the
short exact sequence (18) :
· · · →Hi(C′
∗) →Hi(C∗) →Hi(C′′
∗) →Hi−1(C′
∗) →Hi−1(C∗) →· · · .
Observe that Hi(C′
∗) ≃Hi(C∗) by deﬁnition of C′
∗. Thus Hi(C′′
∗) = 0.
□
Remark 10. We think of C′′
∗as the original complex C∗in which we have “killed” the
homology.
The homology groups of the complexes C′
∗(t), C∗(t) and C′′
∗(t) are given in the follow-
ing claim.
Lemma 8. The complexes C′
∗(t), C∗(t) and C′′
∗(t) are acyclic.
Proof of the claim. According to Proposition 1, C∗(t) = C∗(M; sl2(C(t))ρ) is acyclic.
One can observe that the map ∂′ is invertible, thus C′
∗(t) is acyclic. And ﬁnally C′′
∗(t) =
C∗(t)/C′
∗(t) is also acyclic (as a quotient of two acyclic complexes).
□
We endow the complexes in Sequence (19) with compatible bases in order to compute
the torsions. From the deﬁnition, C′
∗is endowed with a distinguished basis c′∗given by

P ρ
1 ⊗T 2
1 , . . . , P ρ
b ⊗T 2
b , P ρ
1 ⊗λ1, . . . , P ρ
b ⊗λb
	
and we equip C′
∗(t) with the corresponding distinguished basis 1 ⊗c′∗improperly de-
noted again for simplicity c′∗. Similarly, we endowed the quotient C′′
∗= C∗/C′
∗with a
distinguished basis c′′∗, and the same for C′′
∗(t). Using the exact sequence (19), we ﬁnally
endowed C∗(t) with the compatible basis c′∗∪c′′∗obtained by lifting and concatenation
(here again our notation is improper). Note that this last basis is diﬀerent from the
distinguished geometric basis c∗of C∗(t) = C∗(M; sl2(C(t))ρ) described in Subsection 3.
16
From now on, we write Tor(C∗(t), c∗, ∅) (resp. Tor(C′
∗(t), c′∗, ∅), Tor(C′′
∗(t), c′′∗, ∅))
for the Reidemeister torsion of C∗(t) (resp. C′
∗(t), C′′
∗(t)) computed in the basis c′∗∪
c′′∗(resp. c′∗, c′′∗); whereas we write Tor(C∗(M; sl2(C(t))ρ), c∗, ∅) for the torsion of
C∗(t) = C∗(M; sl2(C(t))ρ) but computed in the geometric basis c∗.
Using the basis
change formula (see [Por97, Proposition 0.2]), we have:
Tor(C∗(M; sl2(C(t))ρ), c∗, ∅) = Tor(C∗(t), c′∗∪c′′∗, ∅) ·
Y
i
[ci/c′i ∪c′′i](−1)i.
Hence from the deﬁnition of the polynomial torsion, we have:
∆ϕ⊗Ad◦ρ
M
(t) = τ0 · Tor(C∗(M; sl2(C(t))ρ), c∗, ∅)
=
Y
i
[ci/c′i ∪c′′i](−1)i · τ0 · Tor(C∗(t), c′∗∪c′′∗, ∅)
(20)
where τ0 = sgn (Tor(C∗(M; R), c∗
R, h∗
R)), see Section 3.
Applying the Multiplicativity Lemma to the exact sequence in Equation (19) we get:
(21)
Tor(C∗(t), c′∗∪c′′∗, ∅) = (−1)α · Tor(C′
∗(t), c′∗, ∅) · Tor(C′′
∗(t), c′′∗, ∅)
where α ≡P
j αj−1(C′
∗(t))αj(C′′
∗(t)) mod 2. We ﬁrst compute the sign in Equation (21):
Lemma 9. The sign (−1)α in Equation (21) is given by α ≡b · dim C3 mod 2.
Proof of Lemma 9. It is easy to see from the deﬁnition that:
dim C′′
∗(t) = dim C∗(t) −dim C′
∗(t).
Moreover, dim C′
0(t) = 0 = dim C′
3(t) and dim C′
1(t) = dim C′
2(t) = 3b, where b is the
number of boundary components of M. Thus, reduced modulo 2, αj(C′
∗(t)) are all zero
except α1(C′
∗(t)) ≡b mod 2. As a consequence,
α ≡
X
j
αj−1(C′
∗(t))αj(C′′
∗(t))
≡α1(C′
∗(t))α2(C′′
∗(t))
≡b · (dim C0 + dim C1 + dim C2)
mod 2.
Since the Euler characteristic of M is equal to zero, we have that α ≡b · dim C3 mod 2.
□
Next we compute the torsion of C′
∗(t) (with respect to the basis c′
∗).
Lemma 10. We have:
(22)
Tor(C′
∗(t), c′∗, ∅) =
b
Y
ℓ=1
(taℓ−1).
Proof of Lemma 10. It is easy to observe that (see Complex (17)):
Tor(C′
∗(t), c′∗, ∅) = det ∂′ =
b
Y
ℓ=1
(taℓ−1).
□
If we substitute Equation (22) into Equation (21), we obtain:
(23)
Tor(C′′
∗(t), c′′∗, ∅) = (−1)α Tor(C∗(t), c′∗∪c′′∗, ∅)
Qb
ℓ=1(taℓ−1)
.
Now we consider the limit of Equation (23) as t goes to 1 and prove the following
lemma which gives a relation between the torsion of C′′
∗(t) and the non–abelian torsion
of M in the adjoint representation.
17
Lemma 11. Let δ0 = τ0 ·
Y
i⩾0
[ci/c′i ∪c′′i](−1)i+1. We have the following identity
(24)
lim
t→1 Tor(C′′
∗(t), c′′∗, ∅) = (−1)b+α · δ0 · TM
λ (ρ).
Proof of Lemma 11. We begin the proof by some considerations on the complexes C′′
∗(t)
and C∗(t) and their respective “limits” C′′
∗and C∗when t goes to 1.
Return to the deﬁnition of the complex C′′
∗(t) = C∗(t)/C′
∗(t). If t goes to 1, then the
acyclic complex C′
∗(t) changes into the “degenerated” complex C′
∗in the sense that the
map ∂′ becomes the zero map. Hence C′
1 ≃H1(C∗) and C′
2 ≃H2(C∗). Like C′′
∗(t), the
complex C′′
∗is acyclic (see Lemma 8); more precisely if t goes to 1, then we get in fact
a complex related to the complex C∗(M; sl2(C)ρ) but without homology, together with
a distinguished basis diﬀerent form the geometric one. Repeat again that the twisted
homology groups Hρ
∗(M) = H∗(M; sl2(C)ρ) are endowed with the following distinguished
bases (coming from the ones of C′
∗, in fact it is not exactly a basis but a lift of the basis
into C∗):
(1) Hρ
1(M) is endowed with h1 = c′1 = {[[P ρ
1 ⊗λ1]], . . . , [[P ρ
b ⊗λb]]},
(2) Hρ
2(M) is endowed with h2 = c′2 =

[[P ρ
1 ⊗T 2
1 ]], . . . , [[P ρ
b ⊗T 2
b ]]
	
.
With obvious notation, choose a set of vectors b′′i+1 in C′′
i+1 such that ∂′′
i+1(b′′i+1) is
a basis of B′′
i = im(∂′′
i+1 : C′′
i+1 →C′′
i ).
Observe that the set of vectors 1 ⊗b′′i+1 in C′′
i+1(t) generates a subspace on which
the boundary operator ∂i+1 : Ci+1(t) →Ci(t) is injective.
With b′′3 = c′′3 in mind, the torsion of C′′
∗(t) (with respect to the basis c′′∗) can be
computed as follows:
Tor(C′′
∗(t), c′′∗, ∅) =
2
Y
i=0
h
∂′′
i+1(1 ⊗b′′i+1) 1 ⊗b′′i/c′′ii(−1)i+1
=
2
Y
i=0
h
c′i ∪∂i+1(bi+1)bi/c′i ∪c′′ii(−1)i+1
.
Here bi denotes a lift of 1 ⊗b′′i to C∗(t). As a result, we can rewrite
Tor(C′′
∗(t), c′′∗, ∅) =
h
c′2∂3(b3)b2/c′2 ∪c′′2i−1
(25)
·
h
c′1∂2(b2)b1/c′1 ∪c′′1i
·
h
∂1(b1)/c′′0i−1
.
We want now to relate Equation (25) to an expression closer to the torsion of the twisted
complex C∗(M; sl2(C)ρ). For this we permute the vectors of ∂2(b2) and ∂1(b1) with the
ones of c′2 and c′1 in one of the determinants in Equation (25). Each set of c′1 and c′2
consists of b vectors and it is easy to observe that ∂3(b3) consists of dim C3(t)(= dim C3)
vectors and ∂2(b2) consists of rk ∂2 = dim C1(t) −b −dim C0(t) (≡dim C0 + dim C1 + b
mod 2) vectors. Hence the sign arises from the permutation, whose exponent is given by
b(dim C0 + dim C1 + b) + b dim C3. When we write ε = (−1)b(dim C0+dim C1) and (−1)α
for (−1)b dim C3 as in Lemma 9, thus we have:
Tor(C′′
∗(t), c′′∗, ∅) = (−1)b+α · ε ·
h
∂3(b3)c′2b2/c′2 ∪c′′2i−1
(26)
·
h
∂2(b2)c′1b1/c′1 ∪c′′1i
·
h
∂1(b1)/c′′0i−1
.
18
By making a change of basis in Equation (26), we obtain the following expression:
Tor(C′′
∗(t), c′′∗, ∅) = (−1)b+α · (
Y
i⩾0
h
ci/c′i ∪c′′ii(−1)i+1
)
· ε ·
h
∂3(b3)c′2b2/c2i−1
·
h
∂2(b2)c′1b1/c1i
·

∂1(b1)/c0−1 .
(27)
Moreover, using the deﬁnition of the bases c′1 and c′2, it is easy to observe that
lim
t→1 ε ·
h
∂3(b3)c′2b2/c2i−1
·
h
∂2(b2)c′1b1/c1i
·

∂1(b1)/c0−1
= ε ·
h
∂3(b3)˜h2b2/c2i−1
·
h
∂2(b2)˜h1b1/c1i
·

∂1(b1)/c0−1
(28)
= Tor(C∗, c∗, h∗).
The last step in Equations (28) is due to the fact that
(−1)|C∗| = (−1)α1(C∗)β1(C∗) = (−1)(dim C1+dim C0)b = ε.
Hence, combining Equations (27) and (28), we obtain
lim
t→1 Tor(C′′
∗(t), c′′∗, ∅) = (−1)b+α(
Y
i⩾0
[ci/c′i ∪c′′i](−1)i+1 ) · Tor(C∗, c∗, h∗)
which is exactly the desired equality because TM
λ (ρ) = τ0 · Tor(C∗, c∗, h∗).
□
We ﬁnish the proof by combining Equation (23) and (24) and using the deﬁnition of
the polynomial torsion ∆ϕ⊗Ad◦ρ
M
(t) given in Equation (20).
