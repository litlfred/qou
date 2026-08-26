---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-024-51-the-tube-algebra
section_title: "The ‘Tube algebra’"
section_number: 5.1
pages: 30-31
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
By deﬁnition [38] of E, every simple B−B morphism is contained in J(X ⊠Y op)J for some
simple X, Y . In view of Lemma 4.8 every simple B − B-morphism is in fact contained in
J(X ⊠ 1)J for some simple X ∈ C (as well as in J(1 ⊠ X
op
)J). Deﬁning
ˆYL =
⨁
i∈Γ
Xi ⊠ 1, ˆYR =
⨁
i∈Γ
1 ⊠ X op
i ,
we conclude that either of J ˆYLJ, J ˆYRJ contains all simple B − B-morphisms. With
Ξ L = End E (J ˆYLJ), Ξ R = End E (J ˆYRJ)
we thus have a one-to-one correspondence between isomorphi sm classes of simple B − B-
morphisms and minimal central idempotents in Ξ L or, equivalently, in Ξ R. From now on
we will stick to Ξ L. By construction of E we have Ξ L = Hom A( ˆYLQ, Q ˆYL) as a vector
space. Thus
Ξ L ∼=
⨁
i,j,k,l
HomA(XiXj ⊠ X op
j , XkXl ⊠ X op
k )
∼=
⨁
i,j,k,l
HomC(XiXj, XkXl) ⊗F HomCop(X op
j , Xop
k )
∼=
⨁
i,j,l
HomC(XiXj, XjXl).
We therefore have
EndE (J ˆYLJ) ≡ HomA( ˆYLQ, Q ˆYL) ∼=
⨁
i,j,k
HomC(XiXj, XjXk), (5.1)
and in complete analogy to the proof of (4.7) one shows that th e multiplication in Ξ L is
given by
(v • u)[i, j, k] = ( djλ)−1 ∑
l,m,n∈Γ
N j
mn∑
α=1
dmdn
Xj Xk
t′jα
mn ☛ ✟
XmXn
v[l, n, k]
Xl
u[i, m, l]
XmXn
✡ ✠tjα
mn
Xi Xj
(5.2)
Remark 5.1 1. We observe that up to a diﬀerent normalization (5.1) and (5. 2) coincide
with Ocneanu’s deﬁnition of the ‘tube algebra’, cf. [45, 15, 19]. (The ( ij|X|jk) of Izumi
corresponds to our u[i, j, k] · dj
λ .) Note, however, that we derive (5.1, 5.2) from an intrinsic
deﬁnition of the algebra Ξ L = End E (J ˆYLJ), which makes the correspondence between
30
the minimal central idempotents of Ξ L and the isomorphism classes of simple objects
in B completely obvious. (Compare this to the laborious proof in [19].) The above
considerations therefore completely clarify the rˆ ole of t he tube algebra. We suspect that
Ocneanu arrived at his deﬁnition of the tube algebra by simil ar considerations.
