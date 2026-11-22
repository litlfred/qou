---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-023-62-loop-spaces-and-horocycle-correspondences
section_title: "Loop spaces and horocycle correspondences"
section_number: 6.2
pages: 38-39
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
tween Hecke categories and loop spaces. It is an abstraction of the horocycle correspondence from
representation theory. We will continue with the assumptions that p : X →Y is proper and X has
smooth diagonal δ : X →X × X.
Consider the fundamental correspondence
LY = Y ×Y ×Y Y
LY ×Y X = X ×X×Y X
q
o
ǫ
/ X ×Y X.
where q is a base change of p, and ǫ is a base change δ.
Deﬁne the functor
F : D(X ×Y X)
ǫ!
/ D(LY ×Y X)
q∗
/ D(LY )
Since q is a base change of p and hence proper, there is an adjunction (q∗, q!), and since ǫ is a base
change of δ and hence smooth, of relative dimension −dim X, there is an equivalence ǫ∗≃ǫ![2 dim X]
and an adjunction (ǫ∗, ǫ∗). Thus there is the continuous right adjoint
F r : D(LY )
q!
/ D(LY ×Y X)
ǫ∗[−2 dim X] / D(X ×Y X)
Let I(F) ⊂D(LY ) denote the cocompletion of the image of F. It is naturally equivalent to the
left orthogonal ⊥K(F r) ⊂D(LY ) to the kernel of F r. Since q! satisﬁes descent, both in turn are
naturally equivalent to the full subcategory of D(LY ) of objects whose image under q! is in the
cocompletion of the image of ǫ!.
Theorem 6.6. There is a natural commutative diagram
D(X ×Y X)
⊥K(F r)
F r
O
∼
/ Z(D(X ×Y X))
z
h◗◗◗◗◗◗◗◗◗◗◗◗
Proof. For notational convenience, set A = D(X ×Y X) and B = D(X). Observe that pushforward
along the relative diagonal B →A is monoidal, and thus we may regard A as an algebra in B-
bimodules. Given an algebra A in B-bimodules, we have its relative bar resolution
A ≃

A⊗B(•+2)

which can be used to calculate its center
Z(A) = HomA⊗Aop(A, A) = HomA⊗Aop(

A⊗B(•+2)

 , A) = Tot {HomB⊗Bop(A⊗B•, A)}
We will access the center as the totalization of the cosimplicial object
C• = HomB⊗Bop(A⊗B•, A)
38
Unwinding the notation and using the canonical identity D(X)⊗k ≃D(Xk), we ﬁnd the cosim-
plicial category
C• ≃FunL
D(X×X)(D((X ×Y X)×X•), D(X ×Y X))
Using the canonical identiﬁcation of functors with integral transforms of Proposition 5.7, we have
a level-wise fully faithful map of cosimplicial diagrams
C•
/ D(X×Y (•+1) ×Y LY )
where the cosimplicial structure maps on the latter are given by !-pullback functors.
Thus the center Z(A) is equivalent to the full subcategory of D(LY ) of objects whose image
under q! is in the cocompletion of the image of ǫ!.
□
Corollary 6.7. There is a natural commutative diagram
D(X ×Y X)
tr
v♠♠♠♠♠♠♠♠♠♠♠♠♠
F

Tr(D(X ×Y X))
∼
/ I(F)
Proof. We have seen that D(X ×Y X) is semi-rigid and pivotal, and hence its center and trace
are equivalent. More precisely, the augmented semi-cosimplicial diagram calculating the center can
be obtained from the augmented semi-simplicial diagram calculating the trace by passing to right
adjoints. In particular, the universal central functor can be obtained as the right adjoint of the
universal trace. Thus passing to left adjoints in the diagram of the previous theorem provides the
diagram of the corollary.
□
