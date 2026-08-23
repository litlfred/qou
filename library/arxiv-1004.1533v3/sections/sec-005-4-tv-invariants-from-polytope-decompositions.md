---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-005-4-tv-invariants-from-polytope-decompositions
section_title: "TV invariants from polytope decompositions"
section_number: 4
pages: 15-20
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
In this section, we recall the deﬁnition of Turaev–Viro (TV) invarian ts of 3-
manifolds. Our exposition essentially follows the approach of Barret t and West-
bury [BW1996]; however, instead of triangulations we use more gene ral polytope
decompositions as deﬁned in the previous section.
Let C be a spherical fusion category as in Section 1, and M — a combinatorial
3-manifold. We denote by E the set of oriented edges (1-cells) of M. Note that
each 1-cell of M gives rise to two oriented edges, with opposite orientations.
Deﬁnition 4.1. An labeling of M is a map l : E → Obj C which assigns to every
oriented edge e of M an object l(e) ∈ Obj C such that l(e) = l(e)∗. A labeling is
called simple if for every edge, l(e) is simple.
Two labelings are called equivalent if l1(e) ≃l2(e) for every e.
Given a combinatorial 3-manifold M and a labeling l, we deﬁne, for every ori-
ented 2-cell C, the state space
(4.1) H(C,l ) = ⟨l(e1),l (e2),...,l (en)⟩, ∂C =e1 ∪e2 · · · ∪en
where the edges e1,...,e n are taken in the counterclockwise order on ∂C as shown
in Figure 15.
X1
X2
X3
X4
X5
H(C,l ) = ⟨X1,X 2,...,X 5⟩
Figure 15. Deﬁning the state space for a 2-cell
Note that by (1.3), up to a canonical isomorphism, the state space only depends
on the cyclic order of e1,...,e n (which is deﬁned by C) and does not depend on
the choice of the starting point.
If N is an oriented 2-dimensional combinatorial manifold, we deﬁne the st ate
space
H(N,l ) =
⨂
C
H(C,l )
where the product is over all 2-cells C, each taken with orientation induced from
orientation of N .
16 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
Finally, we deﬁne
(4.2) H(N ) =
⨁
l
H(N,l ),
where the sum is over all simple labelings up to equivalence.
In the case when N is a triangulated surface, this deﬁnition coincides with the
one in [BW1996].
Note that it is immediate from (1.7) that we have canonical isomorphis m
(4.3) H(N ) = H(N )∗.
Next, we deﬁne the TV invariant of 3-manifolds. Let M be a combinatorial
3-manifold with boundary. Fix a labeling l of edges of M. Then every 3-cell F
deﬁnes a vector
Z(F,l ) ∈H(∂F,l )
deﬁned as follows. Recall that F is an inclusion F : (0, 1)3 →M . The pullback of
the polytope decomposition of M gives a polytope decomposition of ∂(0, 1)3 ≃S2.
Consider the dual graph Γ of this decomposition and choose an orien tation for every
edge of this dual graph (arbitrarily) as shown in Figure 16.
− →
Figure 16. The dual graph on the boundary of a 3-cell
Note that a labeling l of M deﬁnes a labeling of edges of this dual graph as
shown in Figure 17. Moreover, choose, for every face C ∈ ∂F , an element ϕ C ∈
H(C,l )∗ = ⟨l(en)∗,...,l (e1)∗⟩. Then this collection of morphisms deﬁnes a coloring
of vertices of Γ.
By Theorem 1.4, we get an invariant ZRT (Γ) ∈ k, which depends on the choice
of labeling of edges l and on the choice of morphisms ϕ C . We deﬁne Z(F,l ) ∈
⊗CH(C,l ) by
(4.4) ( Z(F,l ), ⊗ϕ C ) = ZRT (Γ,l, {ϕ C}).
Again, if F is a tetrahedron, then this coincides with the deﬁnition in [BW1996];
if C is the category of representations of quantum sl2, these numbers are the 6 j-
symbols.
We can now give a deﬁnition of the TV invariants of combinatorial 3-ma nifolds.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 17
X1X2
X3
X4
X5
X ∗
1
X2
X3
X ∗
4
X5
ϕ C
X ∗
1
X2
X3
X ∗
4 X5
ϕ C ∈H(C,l )∗ = ⟨X ∗
5,X ∗
4,...,X ∗
1 ⟩
Figure 17. Coloring of the dual graph
Deﬁnition 4.2. Let M be a combinatorial 3-manifold with boundary and C – a
spherical category. Then for any coloring l, deﬁne a vector
ZT V (M,l ) ∈H(∂M,l )
by
ZT V (M,l ) = ev
(⨂
F
Z(F,l )
)
where
• F runs over all 3-cells in M , each taken with the induced orientation, so
that
⨂
F
Z(F,l ) ∈
⨂
F
H(∂F,l ) = H(∂M,l ) ⊗
⨂
c
H(c′,l ) ⊗H(c′′,l )
(compare with Lemma 3.2)
• c runs over all unoriented 2-cells in the interior of M , c′,c ′′ are the two
orientations of such a cell, so that c′ =c′′.
• ev is the tensor product over all c of evaluation maps H(c′,l ) ⊗H(c′′,l ) =
H(c′,l ) ⊗H(c′,l )∗ → k
Finally, we deﬁne
ZT V (M) = D−2v(M) ∑
l
(
ZT V (M,l )
∏
e
dne
l(e)
)
where
• the sum is taken over all equivalence classes of simple labelings of M,
• e runs over the set of all (unoriented) edges of M
• D is the dimension of the category C (see (1.1)), and
v(M) = number of internal vertices of M + 1
2 (number of vertices on ∂M)
• dl(e) is the categorical dimension of l(e) and
18 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
ne =
{
1, e is an internal edge
1
2, e ∈∂M
It is easy to see that in the special case of triangulated manifold, th is coincides
with the construction in [BW1996].
Theorem 4.3. IfM is a PL manifold without boundary, then the number ZT V (M ) ∈
k deﬁned in Deﬁnition 4.2 does not depend on the choice of polytope decomposition
of M : for any two choices of polytope decomposition, the resulti ng invariants are
equal.
The proof of this theorem will be given in Section 5.
These invariants can be extended to a TQFT. Namely, let M be a combinato-
rial 3-cobordism between two 2-dimensional combinatorial manifold s N1, N2, i.e a
combinatorial manifold M with boundary such that ∂M =
N1 ⊔ N2 (note that the
combinatorial structure on M automatically deﬁnes a combinatorial structure on
∂M ). Then H(∂M) = H(N1)∗ ⊗H(N2) = Hom k(H(N1),H (N2)), so Deﬁnition 4.2
deﬁnes an element Z(M) ∈ Homk(H(N1),H (N2)), i.e. a linear operator
Z(M) :H(N1) →H(N2).
Theorem 4.4.
(1) So deﬁned invariant satisﬁes the gluing axiom: if M is a combinatorial
3-manifold with boundary ∂M = N0 ∪ N ∪ N , and M′ is the manifold
obtained by identifying boundary components N, N of∂M with the obvious
cell decomposition, then we have
ZT V (M′) = ev H(N )ZT V (M) =
∑
α
(ZT V (M),ϕ α ⊗ϕ α ),
where ev is the evaluation map H(N ) ⊗H(N ) → k, and ϕ α ∈ H(N ),
ϕ α ∈H(N ) are dual bases.
(2) If a M is a 3-manifold with boundary, and M′, M′′ are two polytope de-
compositions of M which agree on the boundary, then Z(M′) = Z(M′′) ∈
H(∂M′) = H(∂M′′).
(3) For a combinatorial 2-manifold N , deﬁne AN : H(N ) →H(N ) by
(4.5) AN =ZT V (N × I)
Then AN is a projector: A2
N =AN .
(4) For a combinatorial 2-manifold N , deﬁne the vector space
(4.6) ZT V (N ) = Im(AN : H(N ) →H(N ))
where A is the projector (4.5). Then the space ZRT (N ) is an invariant
of PL manifolds: if N ′, N ′′ are two diﬀerent polytope decompositions of
the same PL manifold N , then one has a canonical isomorphism Z(N ′) ≃
Z(N ′′).
(5) The assignments N ↦→ZT V (N ), M ↦→ZT V (M ) give a functor from the
category of PL 3-cobordisms to the category of ﬁnite-dimens ional vector
spaces and thus deﬁne a 2 + 1-dimensional TQFT.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 19
Proof. Part (1) is immediate from the deﬁnition.
Part (2) will be proved in Section 5.
To prove part (3), note that gluing of two cylinders again gives a cylin der, so (3)
follows from (1) and (2).
To prove (4), let N ′, N ′′ be two diﬀerent polytope decompositions of N . Con-
sider the cylinder C = N ×I and choose a polytope decomposition of C which
agrees with N ′ on N × { 0} and agrees with N ′′ on N × { 1} (existence of such
a decomposition follows from Theorem 3.4). Consider the correspon ding operator
F1 =Z(C) :H(N ′) →H(N ′′). In a similar way, deﬁne an operator F2 : H(N ′′) →
H(N ′). Then it follows from (2) that F1F2 =AN ′′ , and F2F1 =AN ′ . Thus, F1,F 2
give rise to mutually inverse isomorphisms ZT V (N ′) →ZT V (N ′′).
Part (5) follows immediately from (1)–(4).
□
Note that in the PL category, gluing along a boundary component is w ell de-
ﬁned: gluing together PL manifolds results canonically in a PL manifodl (unlike
the smooth category).
Example 4.5. LetG be a ﬁnite group and C = VecG — the category of G-graded
vector spaces, with obvious tensor structure. Then a simple labelin g is just labeling
of edges of M with elements of the group G, and for a 2-cell C, we have
H(C,l ) =
{
k, ∏
∂C l(e) = 1
0, otherwise
Thus, we see that in this case the state space H(N ) is the space of ﬂat G—
connections (which depends on the choice of polytope decompositio n!). It is well-
known that in this case the projector A =ZT V (Σ ×I) is the operator of averaging
over the action of the gauge group Gv(N ), where v(N ) is the set of vertices of N .
Thus the space Z(N ) is the space of gauge equivalence classes of G–connections.
Example 4.6. We verifyZT V (S2) = k as is required by the deﬁnition of a TQFT.
We pick the polytope decomposition of S2 consisting of one vertex, one edge and two
faces as shown in Figure 18. Using the fact that for Xi,Xj simple Hom(Xi,X j) =
Figure 18. The polytope decomposition of S2
δijk, it is easy to see that H(S2) = ⨁
i⟨Xi⟩ ⊗ ⟨X ∗
i ⟩ = k. It remains to show
that A : H(S2) → H(S2) is the identity map or equivalently, the induced map
H(S2) ⊗H(S2)∗ → k equals the canonical pairing deﬁned in Section 1. Consider
the cylinderS2×I with cell decomposition as in Figure 19. Note that both boundary
edges must be labeled by 1. The computation is then straightforward:
20 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
Figure 19. The cylinder over S2
1
D2
∑
X∈Irr(C)
dX ϕ
1
1
X
· ϕ ∗
1
1
X ∗
= 1
D2
∑
X∈Irr(C)
X
·
X ∗
= 1
D2
∑
X∈Irr(C)
d2
X = 1.
The ﬁrst equality follows from the normalization of the pairing. The ot her two
equalities are obvious.
