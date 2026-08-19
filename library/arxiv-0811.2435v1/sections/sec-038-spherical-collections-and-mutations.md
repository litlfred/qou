---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-038-spherical-collections-and-mutations
section_title: "Spherical collections and mutations"
section_number: null
pages: 128-136
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
LetC be a 3-dimensional ind-constructible Calabi-Yau category over a ﬁeld
k of characteristic zero. Assume that it is endowed with a ﬁnit e collection of
26Compare with the algebraic series in the Introduction, sect ion 1.4.
128
spherical generators E ={Ei}i∈I ofC deﬁned over k. Then Ext •
C(k)(Ei,Ei)
is isomorphic to H•(S3, k), i∈I. The matrix of the Euler form (taken with
the minus sign)
aij :=−χ
(
Ext•
C(k)(Ei,Ej)
)
is integer and skew-symmetric. In fact, the ind-constructi ble category C
can be canonically reconstructed from the (plain, i.e. not i nd-constructible)
k-linear Calabi-YauA∞-categoryC(k), or even from its full subcategory con-
sisting of the collection E. In what follows we will omit the subscript C(k)
in the notation for Ext •-spaces.
Deﬁnition 20 The collectionE is called cluster if for any i⁄=j the graded
space⊕m∈Z Extm(Ei,Ej) is either zero, or it is concentrated in one of two
degreesm = 1 or m = 2 only.
We will assume that our collection is cluster. In that case K0(C(
k))≃ ZI
with the basis formed by the isomorphism classes [ Ei],i∈I.
With the cluster collection E we associate a quiver Q such that Q does
not have oriented cycles of lengths 1 and 2, and aij /greaterorequalslant0 is the number
of arrows from i to j (we identify the set of arrows from i to j with a
basis in Ext 1(Ei,Ej)). Then the potential for the object E =⊕i∈IEi gives
rise to the potential W = WQ of the quiver Q, i.e. the restriction of the
potential to ⊕i,j∈I Ext1(Ei,Ej). The latter is an inﬁnite linear combination
of cyclic words (see [17], [77] where the potential appears a bstractly without
the relation with Calabi-Yau categories). Any such linear c ombination is
called a potential of Q. In our case the potential is automatically minimal,
i.e. all words have length at least 3. The group of continuous automorphisms
of the completed path algebra of Q preserving the projectors pri, i∈I, acts
on the set of potentials of Q. We call it the gauge action. Let us state the
following general result.
Theorem 9 LetC be a 3-dimensional k-linear Calabi-Yau category gener-
ated by a ﬁnite collection E ={Ei}i∈I of generators satisfying the condition
that
• Ext0(Ei,Ei) = kidEi,
• Ext0(Ei,Ej) = 0 for any i⁄=j,
• Ext<0(Ei,Ej) = 0 , for any i,j .
129
The equivalence classes of such categories with respect to A∞-transformations
preserving the Calabi-Yau structure and the collection E, are in one-to-one
correspondence with the gauge equivalence classes of pairs (Q,W ) where Q
is a ﬁnite oriented quiver (possibly with cycles of length 1 or 2) and W is
a minimal potential of Q (i.e. its Taylor decomposition starts with terms of
degree at least 3).
The case of cluster collections corresponds to quivers with out oriented
cycles of length 1 and 2.
Proof. We will present the proof of the Theorem in the case of the cate gory
with single object E (i.e. A = Hom(E,E ) is a 3 d Calabi-Yau algebra). The
general case can be proved in a similar way.
Let Q be a quiver with one vertex and |J| loops, where J is a ﬁnite
set. We assume that Q is endowed with the potential W0. We would like
to construct a 3 d Calabi-Yau category with a single object E such that
the number of loops in Q is equal to Ext 1(E,E ) and the restriction of the
potential of the category to Ext 1(E,E ) coincides with the given W0. Our
considerations proceed such as follows. Assuming that such a category exists
we will ﬁnd an explicit formula for the potential on A = Hom(E,E ). Then
we simply take this explicit formula as the deﬁnition. If the desired category
is constructed then we can consider the graded vector space E xt•(E,E )[1]
which decomposes as
Ext0(E,E )[1]⊕ Ext1(E,E )⊕ Ext2(E,E )[−1]⊕ Ext3(E,E )[−2] .
The ﬁrst and the last summand are isomorphic to k[1] and k[−2] respectively,
and the middle two summands are dual two each other. We introd uce graded
coordinates on Ext•(E,E )[1] and denote them such as follows:
a) the coordinate α of degree +1 on Ext 0(E,E )[1];
b) the coordinate a of degree−2 on Ext 3(E,E )[−2];
c) the coordinates xi,i∈J of degree 0 on Ext 1(E,E );
d) the coordinates ξi,i∈J of degree−1 on Ext 2(E,E )[−1].
The Calabi-Yau structure on A gives rise to the minimal potential W =
W (α,xi,ξi,a ), which is a series in cyclic words on the space Ext •(E,E )[1].
If it arises from the pair ( Q,W 0), then the restriction W (0,xi, 0, 0) must
coincide with W0 = W0(xi). Furthermore, A deﬁnes a non-commutative
formal pointed graded manifold endowed with a symplectic st ructure (see
[42]). The potential W satisﬁes the “classical BV equation” {W,W} = 0,
where{•,•} denotes the corresponding Poisson bracket.
130
With these preliminary considerations we see what problem s hould be
solved. We need to construct an extension of W0 to the formal series W of
degree 0 in cyclic words on the graded vector space k[1]⊕kJ⊕kJ [−1]⊕k[−2],
satisfying the classical BV-equation with respect to the Po isson bracket
{W,W} =
∑
i
∂W/∂xi∂W/∂ξi +∂W/∂α∂W/∂a.
Here is the construction. Let us start with the potential
Wcan =α2a +
∑
i∈J
(αxiξi−αξixi) .
This potential makes the above graded vector space into a 3 d Calabi-Yau
algebra with associative product and the unit. The multipli cation vanishes
on the graded components
Ext1(E,E )⊗ Ext1(E,E )→ Ext2(E,E )
and is a non-degenerate bilinear form on components
Ext1(E,E )⊗ Ext2(E,E )→ Ext3(E,E )≃ k .
Now we see that starting with an arbitrary minimal potentialW0 on Ext1(E,E )
we can lift it to the minimal potential on Ext •(E,E ) by setting
ˆW :=Wcan +W0.
We claim that{ˆW,ˆW} = 0. Indeed, we have {Wcan,Wcan} ={W0,W 0} = 0.
Moreover,
{Wcan,W 0} =α
∑
i∈J
[xi,∂W 0/∂xi] = 0
(we use here the well-known identity ∑
i∈J [xi,∂W 0/∂xi] = 0).
Next we need to check compatibility of the above constructio n with the
gauge group action. Let G0 be the subgroup of the grading preserving auto-
morphisms of the group of continuous automorphisms of the al gebra of formal
series k⟨⟨α,xi,ξi,a⟩⟩,i∈J. LetJ⊂ k⟨⟨α,xi,ξi,a⟩⟩be a closed 2-sided ideal
generated by α,a and ξi for i∈J. Since every generator of J has non-zero
degree we conclude that the group G0 preservesJ (it can be deduced from
the fact that it transforms generators into series of non-ze ro degrees). There-
fore we obtain a homomorphism of groups G0→ Aut(k⟨⟨xi⟩⟩),i ∈ J. The
131
restriction of the potential W to Ext 1(E,E ) deﬁnes a surjection from the
set of A∞-equivalence classes of 3 d Calabi-Yau algebras to the gauge equiv-
alence classes of ( Q,W 0), where Q is a quiver with one vertex endowed with
the minimal potential W0. Such algebras can be thought of as deformations
of the “ansatz”, which is a 3 d Calabi-Yau algebra Acan corresponding to the
potential Wcan.
Finally we are going to show that the above surjection is in fa ct a bijection.
The latter will follow from the equivalence of the correspon ding deformation
theories. The deformation theory of the Calabi-Yau algebra Acan is controlled
by a DGLA gAcan =⊕n∈Zgn
Acan, which is a DG Lie subalgebra of the DG Lie
algebra
ˆgAcan =
(∏
n/greaterorequalslant1
Cycln((A[1])∗)
)
[−1]
of all cyclic series in the variables α,xi,ξi,a,i ∈J (the Lie bracket is given by
the Poisson bracket and the diﬀerential is given by {Wcan,•}). Namely, the
component of gAcan of degree N consists of all cyclic series which contain at
least 2 + N letters α,xi,ξi,a,i ∈J. We will call the degree deﬁned in terms
of these letter a cyclic degree in order to distinguish it from the cohomological
degreeof complexes. Notice that the set of A∞-equivalence classes of minimal
3d Calabi-Yau agebras can be identiﬁed with the set of gauge equ ivalence
classes of solutions γ∈ g1
Acan to the Maurer-Cartan equation
dγ + 1
2[γ,γ ] = 0 .
Similarly, the set of gauge equivalence classes of minimal p otentials on A1 =
Ext1(E,E ) can be identiﬁed with the set of gauge equivalence classes o f
solutions to the Maurer-Cartan equation in the DGLA h = h0⊕ h1, where
h0 =
∏
n/greaterorequalslant1
((A1)∗)⊗n⊗A1 , h1 =
∏
n/greaterorequalslant3
Cycln((A1)∗) .
Here we identify h0 with the Lie algebra of continuous derivations of the topo-
logical algebra k⟨⟨x1,...,x n⟩⟩preserving the augmentation ideal (x1,...,x n),
and we identify h1 the h0-module of minimal cyclic potentials on A1.
The above construction of the “lifting” ˆW =W0+Wcan can be interpreted
as a homomorphism of DGLAs ψ : h→ gAcan. Namely, h0 is identiﬁed (after
the shift [1]) with the space of such cyclic series in xi,ξi,i∈J which contain
132
exactly one of the variables ξi and at least one of the variables xj for some
i,j ∈J. Similarly h1 is identiﬁed with the space of cyclic series in xi,i∈J
which has terms of degree at least 3.
We claim that ψ induces an epimorphism (previous considerations ensure
that it is a monomorphism) of cohomology groups in degree 1, a nd for both
DGLAs h and gAcan there is no cohomology in degree greater or equal than
2. This would imply the desired surjectivity of ψ.
Notice that the diﬀerential {Wcan,•} preserves the diﬀerence between
cyclic and cohomological degree. It follows that the comple x gAcan is a direct
summand of the complex ˆgAcan. The latter is dual to the cyclic complex
CC•(Acan). Let A+
can⊂ Acan be a non-unital A∞-subalgebra consisting of
terms of positive cohomological degree. Then, one has for th e cyclic ho-
mology: HC•(Acan)≃ HC•(A+
can)⊕HC•(k). In terms of the dual complex
this isomorphism means the decomposition into a direct sum o f the space of
cyclic series in variables xi,ξi,a,i ∈J (corresponds to (HC•(A+
can))∗) and the
space of cyclic series in the variable α of odd cyclic degree (corresponds to
(HC•(k)∗). It is easy to see that the series in the variable α do not contribute
to the cohomology of gAcan⊂ ˆgAcan.
The cohomological degree of series in variables xi,ξi,a,i ∈ I is non-
positive. Recall that we shifted the grading in Lie algebras by 1 with respect
to the cohomological grading. Hence H /greaterorequalslant2(gAcan) = 0. Also, it is immediate
that H 1(gAcan) is isomorphic to the space of cyclic series in the variables
xi,i∈I with terms of degree at least 3. Hence H 1(gAcan)≃ h1≃H 1(h) (the
latter holds since the diﬀerential on h is trivial). This concludes the proof.
■
Next, we will introduce the notion of a mutation on the set of cluster
collections in a given category C. Let us choose an element of I which we
will denote by 0. We are going to write i <0 if ai0 > 0, and i >0 if i⁄= 0
andai0 ⩽ 0. The mutation of E at the object E0 is deﬁned as a new spherical
collectionE′ = (E′
i)i∈I such that:
E′
i =Ei, i< 0,
E′
0 =E0[−1],
E′
i =RE0(Ei), i> 0 .
where RE0(Ei) := Cone(E0⊗ Ext•(E0,Ei)→ Ei) is the reﬂection functor
given by the cone of the natural evaluation map. Explicitly, the object E′
i
133
for i> 0 ﬁts in the exact triangle
Ei→E′
i→E0⊗ Ext1(E0,Ei) .
Notice that all objects E′
i,i ⁄= 0 belong to the abelian category generated
byEi,i∈I. We remark that the spherical collection E′ is not necessarily a
cluster one.
At the level of the lattice Γ := ZI the change of the spherical col-
lectionsE → E′ corresponds to the following relation between the basis
vi := cl k(Ei), i∈I and the mutated basis v′
i = cl k(E′
i), i∈I:
v′
i =vi,i< 0,
v′
0 =−v0,
v′
i =vi−⟨v0,vi⟩v0 =vi +a0iv0,i> 0 .
We recall that aij =−⟨vi,vj⟩. The mutated matrix ( a′
ij) is given by
a′
ij =aij +ai0a0j if i< 0<j,
a′
i0 =−ai0,
a′
0i =−a0i,
a′
ij =aij, otherwise.
Thus we see that the mutation at E0 gives rise to the mutation of the matrix
(aij) in the sense of cluster algebras (see [77]). Notice that at t he categorical
level the mutation is not an involution. The composition of t he mutation at
E0 and of the mutation at E′
0 =E0[−1] is the reﬂection functor RE0 applied
to all elements of the cluster collection.
Identifying Calabi-Yau categories endowed with cluster co llections with
quivers with potentials we obtain the well-known notion of m utation of a
quiver with potential (see [77]). Then we have the following result.
Theorem 10 In the scheme (an inﬁnite-dimensional aﬃne space) of poten-
tialsPT there is a countable set of algebraic hypersurfaces Xi,i /greaterorequalslant1 invariant
under the gauge group action, such that for any potential bel onging to the set
PT\∪ i/greaterorequalslant1Xi one can make mutations indeﬁnitely, obtaining each time a po -
tential from PT \∪i/greaterorequalslant1Xi. In particular, all corresponding quivers do not
have oriented cycles of length one or two.
Sketch of the proof. The mutated spherical collection fails to be cluster if
for some i⁄=j we have simultaneously Ext 1(E′
i,E′
j)⁄= 0 and Ext 2(E′
i,E′
j)⁄=
134
0. This property is not stable under deformations of 3-dimen sional Calabi-
YauA∞-category, since we can add a quadratic term to the potential WE′
i⊕E′
j
reducing the dimension of Ext 1(E′
i,E′
j) and Ext 2(E′
i,E′
j). Therefore, the
property that the mutated collection is also a cluster one ho lds on a Zariski
open non-empty subset of the space of all potentials. Moreov er, the mu-
tation induces a birational identiﬁcation between varieti es (maybe inﬁnite-
dimensional) of gauge equivalence classes of generic poten tials for quivers
corresponding to skew-symmetric matrices ( aij) and (a′
ij). ■
Any cluster collectionE ={Ei}i∈I deﬁnes an open domain UE⊂Stab(C, cl),
where Γ = K0(C(
k)), cl = id. Namely, for any collection zi∈ C, Imzi > 0,i∈
I we have a stability condition σ(zi) := σ(zi)i∈I with the t-structure deﬁned
by (Ei)i∈I and the central charge Z such that Z(Ei) := Z(cl(Ei)) = zi,i∈I.
The heart of the t-structure is an abelian category AE generated by (Ei)i∈I,
which is artinian with simple objects Ei,i ∈ I. This abelian category is
equivalent to the category of continuous ﬁnite-dimensiona l representations
of the algebra BW whereW is the potential of the path algebra of the quiver
Q. If E′ is a cluster collection obtained from E by the mutation at E0 then
the domainsUE andUE ′ do not have common interior points, but have a com-
mon part of the boundary which is the wall of second kind. The c ommon
boundary corresponds to the stability structure with Z(E0)∈ R<0.
r❳❳❳❳❳❳❳❳❳ ②
❳❳❳❳❳❳❳❳❳ ③
❈
❈
❈
❈
❈
❈
❈
❈ ❖
✂
✂
✂
✂
✂
✂
✂✂ ✍✻
Z(E0)
Z(E0[−1])
Z(Ei), i⁄= 0
135
CategoryAE ′ is obtained from AE by tilting. Namely, any object M of
AE admits a unique presentation as an extension
0→nE0→M→N→ 0
where N∈B :={E∈AE| Hom(E,E 0) = 0}. Similarly, any object M′ of
AE ′ admits a unique presentation as an extension
0→N→M′→nE0[−1]→ 0
with N∈B .
