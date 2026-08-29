---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-011-3-symmetries-of-simplicial-invariants
section_title: "Symmetries of simplicial invariants"
section_number: 3
pages: 8-14
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
In this section, we deﬁne the data for a state sum model given a strict non-
degenerate spherical category C. Then we show that the simplicial invariant of
labelled manifolds has the property that it depends only on the isomorphism class
of the labelling of each edge. Then it is shown that the invariant depends only on
the underlying combinatorial structure of the simplicial complex.
The data for a state sum model is constructed as follows. The label set I is the
set of simple objects in the category. For each ordered triple ( a,b,c ) of labels, the
vector space H(a,b,c ) is deﬁned to be Hom(b,a⊗c)( s e eF i g u r e2 ) .
For the partition function of the tetrahedron A labelled by e01 = a, e02 = b,
e12 =c, e23 =d, e13 =e, e03 =f, ﬁrst deﬁne a linear functional on the space
Hom(d⊗c,e )⊗ Hom(f,d⊗b)⊗ Hom(e⊗a,f )⊗ Hom(b,c⊗a).
The linear functional is deﬁned to be
α⊗β⊗γ⊗δ↦→ trL(β(1⊗δ)(α⊗ 1)γ)
(Figure 3). This linear functional determines a unique linear map
{abc
def
}
+
:H o m (f,d⊗b)⊗ Hom(b,c⊗a)→ Hom(e,d⊗c)⊗ Hom(f,e⊗a)
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4005
b
20
c
a
1
Figure 2
bd
c f
a
e
Figure 3
using the non-degenerate pairings
Hom∗(d⊗c,e )∼= Hom(e,d⊗c)a n d H o m ∗(e⊗a,f )∼= Hom(f,e⊗a).
For the partition function of−A labelled in the same way, the linear functional
on
Hom(e,d⊗c)⊗ Hom(d⊗b,f )⊗ Hom(f,e⊗a)⊗ Hom(c⊗a,b )
deﬁned by
α⊗β⊗γ⊗δ↦→ trL(γ(α⊗ 1)(1⊗δ)β).
likewise determines a unique linear map
{
abc
def
}
−
:H o m (e,d⊗c)⊗ Hom(f,e⊗a)→ Hom(f,d⊗b)⊗ Hom(b,c⊗a)
Deﬁnition 3.1. Given isomorphismsφa : a→a′,φb : b→b′ andφc :c→c′,t h e r e
is an induced isomorphism
Hom(b,a⊗c)→ Hom(b′,a′⊗c′)
given byα↦→φ−1
b α(φa⊗φc).
4006 JOHN W. BARRETT AND BRUCE W. WESTBURY
Lemma 3.2. Given any ordered 6-tuple of elements of I, (a,b,c,d,e,f ),a n da n
ordered 6-tuple of isomorphisms, (φa,φb,φc,φd,φe,φf ),w h e r eφa : a→a′,... ,φf : f
→f′, then the following diagram commutes:
Hom(f,d⊗b)⊗ Hom(b,c⊗a) −−−−→ Hom(f′,d′⊗b′)⊗ Hom(b′,c′⊗a′)


abc
def



+
↓
↓



a′ b′ c′
d′ e′ f′



+
Hom(e,d⊗c)⊗ Hom(f,e⊗a)−−−−→ Hom(e′,d′⊗c′)⊗ Hom(f′,e′⊗a′)
Also, the diagram for the opposite orientation commutes:
Hom(f,d⊗b)⊗ Hom(b,c⊗a) −−−−→ Hom(f′,d′⊗b′)⊗ Hom(b′,c′⊗a′)


abc
def



−
↑
↑



a′ b′ c′
d′ e′ f′



−
Hom(e,d⊗c)⊗ Hom(f,e⊗a)−−−−→ Hom(e′,d′⊗c′)⊗ Hom(f′,e′⊗a′)
Proof. First, in the diagram
Hom(e,d⊗c)
α↦→trL(α−)
−−−−−−−→Hom∗(d⊗c,e )
↓
↓
Hom(e′,d′⊗c′)
α↦→trL(α−)
−−−−−−−→Hom∗(d′⊗c′,e′)
the horizontal arrows are deﬁned by the pairings, the left vertical arrow by the
induced isomorphism of the previous deﬁnition, and the right vertical arrow by
the adjoint of the map β↦→ (φe⊗φa)βφ−1
f . This diagram, and a similar diagram
obtained by replacing e,d,c with f,e,a , commute. These diagrams are used to
compute the action of the isomorphisms of the statement of the lemma on the
linear functionals in the deﬁnition of the partition function.
The ﬁrst diagram in the statement of the lemma commutes as a consequence of
the identity
trLφ−1
f β(φd⊗φb)(1⊗ (φ−1
b δ(φc⊗φa)))(((φd⊗φc)−1αφe)⊗ 1)(φe⊗φa)−1γφf
=t rL(β(1⊗δ)(α⊗ 1)γ).
The proof that the second diagram commutes is similar.
Proposition 3.3. Let M be a closed simplicial manifold. Let l1 and l2 be two
labellings such that the two labels associated to any edge are isomorphic. Then,
Z(M,l 1)= Z(M,l 2).
Proof. According to the previous lemma, the mapV (M)→V (M) is conjugated by
the induced isomorphism on the state space of each triangle. The invariant Z(M)
is the trace of this map and is invariant under conjugation by a linear map.
Next, we determine the behaviour of the simplicial invariantZ(M) under combi-
natorial maps. For this, it is necessary to use the properties of duals in the spherical
category.
Deﬁnition 3.4. Let f : M → N be a combinatorial isomorphism of simplicial
complexes. Let e be any edge of M, labelled by a,a n dl e tb be the label of edge
f(e)i n N.T h e nf is compatible with these labellings if b = a in the case that
f preserves the orientation of the edge, and b =ˆa in the case that f reverses the
orientation.
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4007
b
a
c
Figure 4
Note that, given f and a labelling of M, there is a unique compatible labelling
ofN.
Now the properties of the state space of a triangle under combinatorial isomor-
phisms are described. The combinatorial isomorphisms are just permutations in
S3. For the standard triangle T (a,ˆb,c ), labelled by ∂0T↦→a, ∂1T↦→ ˆb, ∂2T↦→c,
the labelling is permuted by ( a,b,c )↦→ σ+(a,b,c ) for an even permutation σ+,
and (a,b,c )↦→ σ−(ˆa, ˆb, ˆc) for an odd permutation σ−. For this reason, it is more
convenient to use the notationV (a,b,c )=H(a,ˆb,c ) for the state space of a labelled
triangle when the symmetry properties are considered.
There is a canonical map V (a,b,c )→V (b,c,a ), i.e.,
Hom(ˆb,a⊗c)→ Hom(ˆc,b⊗a),
deﬁned by mapping f : ˆb→a⊗c to the following composite:
ˆc
=
−→e⊗ ˆc
ϵ(b)⊗1
−−−−→b⊗ ˆb⊗ ˆc
1⊗f⊗1
−−−−→b⊗a⊗c⊗ ˆc
1⊗1⊗ˆϵ(c)
−−−−−−→b⊗a⊗e
=
−→b⊗a.
This corresponds to the graph in Figure 4.
There is also a canonical pairing V (a,b,c )×V (ˆc, ˆb, ˆa)→F, i.e.,
Hom(ˆb,a⊗c)× Hom(b, ˆc⊗ ˆa)→F.
Let f : ˆb→a⊗c and g :b→ ˆc⊗ ˆa. Then the pairing is deﬁned by
⟨f,g⟩ =t rL(f ˆg).
Equivalently, it is determined by the closed tangle in Figure 5.
Deﬁnition 3.5. For every ordered triple, (a,b,c ), of elements of I and every even
permutationσ+∈S3, there is an isomorphism
θ(σ+): V (a,b,c )→Vσ +(a,b,c ).
For (a,b,c )↦→ (b,c,a ), this is the canonical map just deﬁned. Repeating this gives
the isomorphism for (a,b,c )↦→ (c,a,b ). The identity is associated to the identity.
For every ordered triple, (a,b,c ), of elements of I, and every odd permutation
σ−∈S3, there is a non-degenerate pairing, ⟨−,−⟩σ− ,
V (a,b,c )⊗Vσ−(ˆa, ˆb, ˆc)→F.
Forσ− the odd permutation (a,b,c )↦→ (c,b,a ), this is the pairing deﬁned above.
The pairings for the other two odd permutations can be deﬁned by the formula
⟨v1,v 2⟩σ− =⟨v1,θ (σ+)v2⟩σ−σ+ .
4008 JOHN W. BARRETT AND BRUCE W. WESTBURY
b
a c
Figure 5
Lemma 3.6. For all even permutations σ+
1 ,σ +
2 , odd permutations σ−,l a b e l sa, b
and c and all v1∈V (a,b,c ) and v2∈Vσ−(ˆa, ˆb, ˆc):
θ(σ+
1 σ+
2 )= θ(σ+
1 )θ(σ+
2 ),
⟨v1,v 2⟩σ− =
⟨
v1,θ (σ+)v2
⟩
σ−σ+ ,
⟨v1,v 2⟩σ− =⟨v2,v 1⟩σ− .
Also, the pairings are non-degenerate bilinear forms.
Proof. The ﬁrst two relations follow from the fact that the following composite is
the identity map:
V (a,b,c )→V (b,c,a )→V (c,a,b )→V (a,b,c ).
This condition is the relation shown in Figure 6, which is satisﬁed in any pivotal
category, by Lemma 2.3.
The pairings are non-degenerate since the spherical category is non-degenerate
andˆ is an isomorphism on spaces of morphisms. The pairing trL(f ˆg) is symmetric
since
trL(g ˆf)=t rL(ˆg ˆf)=t rL(f ˆg).
The symmetry of the other pairings is equivalent to the relations
trL((θ(σ+)v2)ˆv1)=t rL((θ(σ+)v1)ˆv2).
This follows from the relations in a spherical category, as can be seen by the isotopy
equivalence of the corresponding diagrams.
The union of the spaces {V (a,b,c )∐V∗(a,b,c )| (a,b,c )∈ I×I×I} forms a
vector bundle over I×I×I×{±} . The permutation group, S3, acts on the base
space by
σ+ :( a,b,c, ±)↦→ (σ+(a,b,c ),±),
σ− :( a,b,c, ±)↦→ (σ−(ˆa,ˆb, ˆc),∓).
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4009
b
a
c =
a
b
c
Figure 6
Deﬁnition 3.7. For each triple of labels, (a,b,c ), and each permutation σ+ orσ−
there are linear isomorphisms
V (a,b,c )
θ(σ+)
−−−→Vσ +(a,b,c ),
V∗(a,b,c )
θ∗−1(σ+)
−−−−−−→V∗σ+(a,b,c ),
if σ+ is even, and
V (a,b,c )
θ(σ−)
−−−−→V∗σ−(ˆa,ˆb, ˆc),
V∗(a,b,c )
θ∗−1(σ−)
−−−−−−→Vσ−(ˆa,ˆb, ˆc),
if σ− is odd. The maps θ(σ−) are deﬁned using the pairings.
Lemma 3.8. These linear maps determine an action of the group S3 on this vector
bundle, or, in other words, this is an S3-equivariant vector bundle. Furthermore,
the action of any permutation on elements of V∗(a,b,c ) is the adjoint of the inverse
of the action on V (a,b,c ).
Proof. These are equivalent to the conditions in Lemma 3.6.
Theorem 3.9. Let f : M→ N be a combinatorial isomorphism of labelled mani-
folds. Then the simplicial invariants are equal, Z(M)= Z(N).
Proof. Let V (M)a n dV (N) be the vector spaces described in Deﬁnition 1.6. For
each triangle inM, consider the restriction of f to this triangle. There is a element
σ∈S3 deﬁned by the unique decomposition of this map into a permutation followed
by the simplicial map of the triangle to its image in N.
4010 JOHN W. BARRETT AND BRUCE W. WESTBURY
There is a map
V (M)⊗V∗(M)→V (N)⊗V∗(N)
which is deﬁned by taking the tensor product over the set of triangles of the maps
θ(σ)⊗θ∗−1(σ)
for each triangle, followed by an iteration of the standard twistP which rearranges
the factors in the range of this map to coincide withV (N)⊗V∗(N), as in Deﬁnition
