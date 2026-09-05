---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-010-31-classical-homology-theories
section_title: "Classical homology theories"
section_number: 3.1
pages: 35-38
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
Recall from §1 the tangent classiﬁer functor Mﬂd(B)
τ
− →PShv(B), which is symmetric monoidal
with respect to coproduct of presheaves (see Construction 2.1) .
To state the next result, for C an∞-category we denote the full∞-subcategory C⊂ PShvInd-ﬁn(C)⊂
PShv(C) which is the smallest that is closed under the formation of ﬁnite colimit s and ﬁltered col-
imits.
Proposition 3.1 (§3.3 of [AFT]) . The symmetric monoidal functor Mﬂd(B)
τ
− →PShv(B) is a
homology theory, and it factors through PShvInd-ﬁn(B).
Corollary 3.2. Let V be an∞-category that admits pushouts and ﬁltered colimits, which we regard
as a symmetric monoidal ∞-category whose symmetric monoidal structure is given by co product.
Let F : PShvInd-ﬁn(B)→ V be a symmetric monoidal functor that preserves pushouts and ﬁltered
colimits (so F is the left Kan extension of its restriction F|B). Then the composition
Fτ : Mﬂd(B)
τ
− →PShvInd-ﬁn(B)
F
− →V
is a homology theory.
Example 3.3.
• The underlying space functor Mﬂd(B)→ Spaces is a homology theory – here, we are equip-
ping the target with the symmetric monoidal structure given by cop roduct. The restriction
of this functor to Mﬂd(B)ﬁn (see§1.1) factors through Spacesﬁn .
• The underlying space of the ‘frame bundle’ functor Mﬂd(B)→
(
Spaces/|B|
)
is a homol-
ogy theory – here, we are equipping the target with the symmetric m onoidal product
given by coproduct. Note that the restriction of this functor to Mﬂd(B)ﬁn factors through(
Spaces/|B|
) ﬁn
.
• Let V be a presentable ∞-category. Consider a functor E : B→ V. Use the same notation
E : PShv(B)→ V for the left Kan extension. This left Kan extension preserves copr oducts,
and therefore deﬁnes a symmetric monoidal functor, which we aga in give the same notation,
between their coCartesian symmetric monoidal strutures: E : PShv(B)∐−→ V∐. We obtain
a composite symmetric monoidal functor
Mﬂd(B)
τ
− →PShv(B)∐ E
− →V∐ .
35
In§3.3 of [AFT] we show that τ carries collar-gluings to pushouts and sequential open covers
to sequential colimits. Using this, and because this left Kan extensio n E preserves sifted
colimits, this symmetric monoidal functor Eτ is a homology theory.
Should V be equipped with an auxiliary symmetric monoidal structure that dist ributes over
colimits, and should the original functor E : B→ V factor through the full ∞-subcategory
Vdual⊂ V consisting of the dualizable objects, then the restriction of this ho mology theory
Eτ to Mﬂd(B)ﬁn factors through Vdual.
– Let E be a spectrum. The assignment X ↦→E∧X+ depicts a homology theory
Mﬂd(B)→ Spectra, where the latter is equipped with wedge sum as its symmetric
monoidal structure. Should E be dualizable with respect to smash product, then
the restriction of this homology theory to Mﬂd(B)ﬁn factors through Spectradual. In
particular, the suspension spectrum Σ ∞
+X of the underlying space of a ﬁnitary stratiﬁed
space X is dualizable.
– Let V be a chain complex over a commutative ring k. The assignment X↦→C∗(X;V )
depicts a homology theory Mﬂd(B)→ Chk, where the latter is equipped with direct sum
as its symmetric monoidal structure. Should V be dualizable with respect to tensor
products over k, then the restriction of this homology theory to Mﬂd(B)ﬁn factors
through Chdual
k .
3.2. 1-point compactiﬁcations
We will make use of the concept of a zero-pointed embedding from [A F2]. There is a Kan-enriched
functor
ZEmb : Snglrop× Snglrop−→ Kan∗
to pointed Kan complexes, given as follows. Its value on ( X,Y ) is the simplicial set, written as
ZEmb(X+,Y +), for which a p-simplex is a diagram of conically smooth open embeddings among
submersions over ∆ p
e
X× ∆ p
e
fX
−−−→W
fY
←−−−Y× ∆ p
e
witnessing an open cover of W – the simplicial structure maps are evident, and the distinguished
point is the case where W is the disjoint union. That this simplicial set is a Kan complex as claimed
follows from a similar argument for why the simplicial set Snglr(X,Y ) is a Kan complex which is
explained in [AFT]; details for ZEmb can be found in [AF2]. The action Snglr(X,X ′)×Snglr(Y,Y ′)×
ZEmb(X ′
+,Y ′+)→ ZEmb(X+,Y +) is given on p-simplices as
(
g,h ; (X ′× ∆ p
e
fX′
−−→W ′ fY ′
←−−Y ′× ∆ p
e)
)
↦→
(
X× ∆ p
e
fX′ g
−−−→fX ′(g(X))∪fY ′ (h(Y ))
fY ′ h
←−−−Y× ∆ p
e
)
,
which is quickly noticed to be compatible with the simplicial structure ma ps. It is manifest that this
action is compatible with the composition among conically smooth open e mbeddings. Equipping
all stratiﬁed spaces present in the deﬁnition of the functor ZEmb with a B-structure, and each map
as one of B-manifolds, enhances ZEmb to a functor
Mﬂd(B)op× Mﬂd(B)op→ Spaces∗
to based spaces. The restricted adjoint to this functor is the 1-point compactiﬁed tangent classiﬁer
(3.2.1) τ + :
(
Mﬂd(B)ﬁn ) op
→ PShvﬁn
∗ (B) , X ↦→
(
Entr(X)+ τX+
−−−−→B
)
,
where the target is endowed with the symmetric monoidal structur e given by coproduct, written
here as right ﬁbrations (details and context can be found in [AF2]).
Here is a relative version of the functor τ +. Let X be a B-manifold. Let us deﬁne the following
functor:
τ X +
: Mﬂd(B)/X−→ PShv∗(B)/Entr(X +) , (O⊂X)↦→
(
Entr(OX + )
τ X+
O
−−−→B
)
.
36
Let O⊂X be an open subspace of the underlying stratiﬁed space. Consider t he sub- Kan-enriched
functor ZEmb(−+,O X + )⊂ ZEmb(−+,X +) : Bscop→ Kan whose value on U is the sub-simplicial
set of ZEmb(U,X ) consisting of those U× ∆ p
e
fU
− − →W
fX
←−−X× ∆ p
e for which fU∐ (fX )|O→W is an
open cover – easy to check is that this simplicial set is indeed a Kan com plex. Again, equipping each
suchW with a B-structure and each map as one of B-manifolds, there is the presheaf Bop→ Spaces∗.
We will use the notation Entr(OX + )→ B for the associated right ﬁbration, which is equipped with
a section. The assignment ( O⊂ X)↦→
(
Entr(OX + )
τ X+
O
−−−→B
)
depicts the desired functor. Notice
that this functor τ X +
canonically extends as a map of ∞-operads, where the target is equipped
with coproduct as its symmetric monoidal structure.
Lemma 3.4. Let X∼= X−
⋃
R×X0
X+ be a collar-gluing among ﬁnitary B-manifolds. Then, in the
canonical diagram of pointed presheaves on B
Entr
(
(R×X0)X +
) /d47/d47
/d15/d15
Entr
(
(X+)X +
) /d47/d47
/d15/d15
Entr
(
(X+)+)
=
/d15/d15
Entr
(
(X−)X +
) /d47/d47
/d15/d15
Entr(X +)
/d15/d15
/d47/d47 Entr
(
(X+)+)
Entr
(
(X−)+) = /d47/d47 Entr
(
(X−)+)
the upper left square is a pushout, and the linear sequences o f maps are coﬁbration sequences.
Proof. The appearance of B is superﬁcial, and so the statement is equivalent to the one with
B = Bsc.
Because the collar-gluing, written as a constructible bundle X
f
− →[−1, 1], is one among ﬁnitary
stratiﬁed spaces, it can be extended, up to non-canonical isotop y, to a collar-gluing X
~f
− →[−1, 1]
among stratiﬁed spaces with boundary , with X compact. By composing ~f with the constructible
bundle [−1, 1]→ [−1, 1] determined by declaring its restriction to ( − 1
2, 1
2 ) to be an orientation
preserving isomorphism onto (−1, 1), we can assume that the closure of the image of R×X 0֒→X
intersects∂X as R×∂X 0.
Let O⊂ X be a sub-stratiﬁed space with boundary, and choose a collar-neigh borhood [0, 1)×
∂O⊂O. We claim that the canonical morphism of pointed presheaves on Bsc
∗
∐
Entr(0,1)×∂O)
Entr(O)
≃
−−→Entr(OX + )
is an equivalence. This is the case if and only if for each singularity type [U ], the likewise map of
pointed spaces
∗
∐
Entr[U ]((0,1)×∂O)
Entr[U](O)
≃
−−→Entr[U](OX + )
is an equivalence. Write U∼= Ri× C(Z), and use the notation U := [0, 1)× Ri−1× C(Z) for the
basic with boundary and ∂U := Ri−1× C(Z) for its boundary. Developments of [AFT] give that
the lefthand space in this last expression is canonically identiﬁed as th e pushout
∗
∐
((0,1)×∂O)[U ]
O[U]
37
in terms the underlying spaces of the [ U ]- and [ ∂U ]-strata. Along the same lines, the righthand
pointed space in that expression is canonically identiﬁed as the pusho ut
∗
∐
(∂O)∂[U]
O[U]≤[U ]
in terms of the underlying spaces of the ([ U ]≤ [U ])- and [∂U ]-strata. That the the map of pointed
spaces in that expression is an equivalence follows by inspection: ((0 , 1)×∂O)[U] = R× (∂O)[∂U]≃
(∂O)[∂U ], and the inclusion O[U]⊂ O[U]≤[U] induces a weak homotopy equivalence of underlying
topological spaces.
Developments in [AFT] give that each of the two squares of preshea ves on Bsc
Entr
(
R×X0
) /d47/d47
/d15/d15
Entr
(
X+
)
/d15/d15
Entr
(
X−
) /d47/d47 Entr(X)
and
Entr
(
R× (0, 1)×∂X 0
) /d47/d47
/d15/d15
Entr
(
(0, 1)×∂X +
)
/d15/d15
Entr
(
(0, 1)×∂X −
) /d47/d47 Entr((0, 1)×∂X)
are pushouts. The latter maps to the former upon consistent cho ices of collars of the respective
boundaries. By taking the levelwise mapping cones of this map of squa res, the result follows then
from the ﬁrst paragraph, after observing a standard strata-p reserving homeomorphism ( X−)+∼=(
X −\ R>−1×X 0
)
/∂, where ∂ =
(
∂X −
⋃{−1}× X 0
)
\ R>−1×X 0, and likewise for ( X+)+.
□
