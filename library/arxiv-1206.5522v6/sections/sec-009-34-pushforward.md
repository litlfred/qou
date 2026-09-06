---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-009-34-pushforward
section_title: "Pushforward"
section_number: 3.4
pages: 19-23
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
instance of a general paradigm: pushforward.
The following technical lemma is the crux of the later results of this pa per. An earlier treatment,
not in terms of the pushforward, is in [Fra2]; a generalization of this result to structured stratiﬁed
spaces is given in §2 of [AFT2]. We state the the lemma now, and prove it at the end of th is section.
Lemma 3.18. For V a symmetric monoidal ∞-category which is ⊗-presentable, factorization ho-
mology valued in V satisﬁes⊗-excision: for any DiskB
n -algebra A in V, and for any collar-gluing
M ′ ⋃
M0×R
M ′′∼= M among B-framed n-manifolds, the canonical morphism in V
∫
M ′
A
⨂
∫
M0×R
A
∫
M ′′
A
≃
−−→
∫
M
A
is an equivalence.
We give the following n = 1 example to indicate the utility of ⊗-excision as well as some intuition
about how factorization homology behaves. See [Lu2] for a diﬀeren t proof of the following result.
Theorem 3.19. For an associative algebra A in a symmetric monoidal ∞-category V which is
⊗-presentable, there is an equivalence ∫
S1
A ≃ HC∗(A)
between the factorization homology of the circle with coeﬃc ients in A and the Hochschild complex
of A.
Proof. Regard the associative algebra A as a symmetric monoidal functor A : Diskor
1 → V, as in
Section 3.2. Consider the standard collar-gluing R ⋃
R⊔R
R∼= S1 by hemispheres. Lemma 3.18, which
states that factorization homology staisﬁes ⊗-excision, determines the ﬁrst of the equivalences in
the expression: ∫
S1
A ≃
∫
R
A
⨂
∫
S0×R
A
∫
R
A ≃ A
⨂
A⊗Aop
A ≃ HC∗(A) .
The second equivalence is by inspecting values, and the ﬁnal equivale nce is deﬁnitional.
19
□
The next deﬁnition makes use of the multi-functor f −1 : Disk∂,or
k/N→ MﬂdB
n/M of Construction 2.21
associated to each continuous map M→ N for which each of the restrictions, M|N /integerdivide∂N→ N /i⋉tegerdivide∂N
and M|∂N→ ∂N , are manifold bundles.
Deﬁnition 3.20. Let M be an B-framed n-manifold, and let N be an oriented k-manifold, possibly
with boundary. For f : M→ N a map such that the restrictions of f over each of the interior of
N and of the boundary of N is a ﬁber bundle, the ∞-category Diskf is the limit of the diagram
among∞-categories
DiskB
n/M
/d37/d37❏❏❏❏❏❏❏❏❏ Ar(MﬂdB
n/M)
ev0
/d120/d120qqqqqqqqqq
ev1
/d38/d38▼▼▼▼▼▼▼▼▼▼ Disk∂,or
k/N
f −1
/d122/d122ttttttttt
MﬂdB
n/M MﬂdB
n/M
where Ar(MﬂdB
n/M) is the ∞-category of functors [1] → MﬂdB
n/M.
Informally, Diskf consists of compatible triples (֒→f −1U ) such that: U is an open
submanifold of N that is homeomorphic to a disjoint union of Euclidean spaces; V is an open
submanifold of M that is homeomorphic to a disjoint union of Euclidean spaces; the emb edding
֒→f −1U is compatible with the embeddings f −1֒→M and֒→M . The relevance of the
∞-category Diskf is the following technical result.
Lemma 3.21. In the situation of Deﬁnition 3.20, the functor ev0 : Diskf→ DiskB
n/M is ﬁnal.
Proof. After Lemma 2.5, it will suﬃce to prove the result for the case B = BTop(n), and so we omit
B from the notation and discussion. The functor ev0 is a Cartesian ﬁbration of ∞-categories. Thus,
to check ﬁnality, by Lemma 4.1.3.2 of [Lu1], it suﬃces to show that, for each (֒→M )∈ Diskn/M,
the ﬁber ∞-category ev−1
0 V has contractible classifying space. That is, we show that the ∞-
category (Diskk/N)V /, of k-disks U in N equipped with an embedding֒→f −1U , has a contractible
classifying space.
There is an identiﬁcation of spaces
B
(
Diskk/N
) U/
≃ colim
(֒→N )∈Diskk/N
MapMﬂdn/M (U, f −1V ) .
Formally, the sequence of maps
MapMﬂdn/M (U, f −1V ) −→ MapMﬂdn (U, f −1V ) −→ MapMﬂdn(U, M)
is a ﬁber sequence (here the ﬁber is taken over any implicit morphism֒→M , thereby giving
meaning to the lefthand space). So we seek to show the map from th e colimit
colim
(֒→N )∈Diskk/N
MapMﬂdn (U, f −1V ) −→ MapMﬂdn (U, M)
is an equivalence of spaces. We recognize this map of spaces as the m ap of ﬁbers over U∈ Diskn of
the map of right ﬁbrations over Diskn:
colim
(֒→N )∈Diskk/N
Diskn/f −1V −→ Diskn/M .
Being right ﬁbrations, it is enough to show that this functor is an equ ivalence on maximal ∞-
subgroupoids. Using Lemma 2.12 which identiﬁes these maximal ∞-subgroupoids, this is the prob-
lem of showing, for each ﬁnite set J, that the map of spaces
colim
(֒→N )∈Diskk/N
Conf J
(
f −1V
)
Σ J
−→ ConfJ (M )Σ J
is an equivalence.
20
Lemma 2.19 implies the functor Diskk/N→ Diskk/N is ﬁnal, and so the forgetful map
colim
(֒→N )∈Diskk/N
ConfJ
(
f −1V
)
Σ J
≃
−−→ colim
(֒→N )∈Diskk/N
Conf J
(
f −1V
)
Σ J
is an equivalence of spaces. Now notice that, for each (֒→N )∈ Diskk/N , the map ConfJ (f −1V )→
Conf J (M ) an open embedding. Also, for each point c :֒→M the image f
(
c(J)
)
⊂ N has
cardinality at most J. So there is an object (֒→N ) of Diskk/N whose image contains the subset
f
(
c(J)
)
. We see then that the collection of open embeddings
{
ConfJ (f −1V )Σ J֒→Conf J (M )Σ I| (֒→N )∈ Diskk/N
}
forms an open cover.
Because N is a manifold, the collection of open embeddings from Euclidean spaces into N form a
basis for the topology of N . It follows that the collection of (at most) |J|-tuples of disjoint open disks
in N forms an open cover of N in such a way that any ﬁnite intersection of such is again covered
by such. This is to say that this collection of open embeddings forms a hypercover of Conf J (M )Σ J .
Corollary 1.6 of [DI] gives that the map
colim
(֒→N )∈Diskk/N
Conf J
(
f −1V
)
Σ J
≃
−−→Conf J (M )Σ J
is an equivalence of spaces, which completes the proof.
□
Here is an important technical property of the ∞-category of disks over a manifold. (See also
Proposition 5.5.2.16 of [Lu2].)
Corollary 3.22. For M a B-framed n-manifold, the ∞-category DiskB
n/M is sifted.
Proof. The∞-category DiskB
n/M is evidently nonempty, as it contains the object ( ∅֒→M ). We
must then prove that the diagonal functor DiskB
n/M→ DiskB
n/M× DiskB
n/M is ﬁnal. This diagonal
functor ﬁts into a diagram among ∞-categories
Disk∇
ev0 /d47/d47
ev1
/d15/d15
DiskB
n/M⊔M
DiskB
n/M
diag /d47/d47 DiskB
n/M× DiskB
n/M
≃ ⊔
/d79/d79
that we now explain. The upper left ∞-category is that of Deﬁnition 3.20 applied to the fold map
∇ : M⊔ M→ M ; it is equipped with the indicated projection functors. The right ver tical arrow is
induced by the symmetric monoidal structure on MﬂdB
n , which is disjoint union. This right vertical
arrow is an equivalence; an inverse is given by declaring its projection to each factor to be given
by intersecting with the corresponding cofactor of the disjoint un ion. Therefore, to prove that the
diagonal functor is ﬁnal it is suﬃcient to prove that both of the pro jection functors ev1 and ev0 are
ﬁnal. The ﬁnality of ev0 is Lemma 3.21.
We explain that ev1 is ﬁnal. Note that the functor ∇−1 : DiskB
n/M→ MﬂdB
n/M⊔M factors through
the full∞-subcategory DiskB
n/M⊔M . As so, there is a canonical identiﬁcation between ∞-categories
Disk∇ ≃ DiskB
n/M ×
DiskB
n/M⊔M
Ar(DiskB
n/M⊔M )
over DiskB
n/M. Through this identiﬁcation, the composite functor
DiskB
n/M
∇
−−→DiskB
n/M⊔M
const
−−−−→Ar(DiskB
n/M⊔M )
determines a right adjoint to the functor ev1. The ﬁnality of ev1 thereby follows.
□
21
The pushforward property for factorization homology immediately follows from Lemma 3.21, as
the next result articulates. We will use the notation
f∗A : Disk∂,or
k/N
f −1
/d47/d47 MﬂdB
n/M
∫ A /d47/d47 V
for the composite functor, where f −1 is as in Construction 2.21.
Proposition 3.23. Let M be a B-framed n-manifold, N an oriented k-manifold, possibly with
boundary, and f : M → N a map which ﬁbers over the interior and boundary of N . For A a
B-framed n-disk algebra in V, a symmetric monoidal ∞-category which is ⊗-presentable, then the
canonical morphism in V ∫
N
f∗A
≃
−−→
∫
M
A
is an equivalence.
Proof. After Proposition 3.9, we can assume that B is equivalent to BTop(n), and so we omit it
from the notation and discussion. We will explain the string of canonic al equivalences in V:
∫
N
f∗A ≃
Def 3.2
colim
U∈Disk∂,or
k/N
f∗A(U )
≃
Def f∗
colim
U∈Disk∂,or
k/N
∫
f −1U
A
≃
Def 3.2
colim
U∈Disk∂,or
k/N
colim
V ∈Diskn/f −1U
A(V )
≃
(1)
colim
(U,V )∈Diskf
A(V )
≃
− →
(2)
colim
V ∈Diskn/M
A(V )
≃
Def 3.2
∫
M
A .
The only equivalences that are not deﬁnitional are (1) and (2). The equivalence (2) is a direct
application of Lemma 3.21, which states that the functor ev0 : Diskf→ Diskn/M is ﬁnal. Consider
the left Kan extension (non-commutative) diagram among ∞-categories:
Diskf /d47/d47
ev1
/d15/d15
ev0 /d47/d47 Diskn/M /d47/d47 Diskn
A /d47/d47 V
Disk∂,or
k/N
LKan
/d51/d51❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣ ,
which exists because V is presentable. By construction, the functor ev1 : Diskf → Disk∂,or
k/N is a
coCartesian ﬁbration. In particular, for each object U∈ Disk∂,or
k/N, the inclusion of the ﬁber into the
over∞-category
ev−1
1 (U )−→ (Diskf )/U
is ﬁnal. Therefore, the value of LKan on U∈ Disk∂,or
k/N is the colimit over the ﬁber:
colim
V ∈Diskn/f −1U
A(V ) ≃
Def 3.20
colim
V ∈ev−1
1 U
A(V )
≃
−−→LKan(U ) .
So the colimit of LKan is the codomain of (1). The equivalence (1) follows from Proposition 4 .3.3.7
of [Lu1], which implies the colimit of a left Kan extension agrees with the c olimit because they both
satisfy the same universal property.
□
22
Proof of Lemma 3.18. Given a collar-gluing f : M→ [−1, 1], there are canonical morphisms in V
∫
M ′
A
⨂
∫
M0×R
A
∫
M ′′
A−→
∫
[−1,1]
f∗A−→
∫
M
A .
The lefthand morphism is an equivalence by Lemma 3.12, which shows th at factorization homology
over the closed interval is equivalent to the bar construction, and inspection of the functor f∗A.
The righthand morphism is an equivalence by Proposition 3.23, which gr ants that factorization
homology pushes forward along M
f
− →[−1, 1].
□
