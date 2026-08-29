---
doc_id: arxiv-math-9807106v2
doc_title: "An Extension of the Character Ring of sl(3) and Its Quantisat ion"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-17
source_pdf: 9807106v2.pdf
source_sha256: e3cd089e3df5d71f
doc_brief: "An Extension of the Character Ring of sl(3) and Its Quantisat ion — We construct a commutative ring with identity which extends the ring of characters of ﬁnite dimensional representations of sl(3)."
---
The aim of this work is to describe the characters (one-dimen sional representations)
of the fusion algebra of g = ˆsl(n)k WZW conformal models at rational (shifted) level
κ :=k +n =p′/p, for n = 3 = p′, (p, 3) = 1 and their ‘classical’ counterparts.
In [9] we have realised this fusion algebra as a matrix algebr a F ⊂ Matp2(C) with
integer nonnegative structure constants (p)N z
y,x and a basis {Ny, (Ny)z
x = (p)N z
y,x , N 1 =
1p2 }. The labels of the basis run over the highest weights of the adm issible representations
at κ = 3/p [12], which conveniently are parametrised by a subset W (+)
p of the aﬃne Weyl
group W , see the text for precise deﬁnitions. F is a matrix realisation of a commutative,
associative algebra with identity, a distinguished basis, and an involution ∗. The deﬁnition
of the fusion algebra – an example of C-algebra (Character - algebra) in the terminology of
[2], implies that Ny are normal, hence simultaneously diagonalisable by a unita ry matrix
ψ(µ )
y labelled by some set Ep = {µ} of p2 indices,
(p)N z
x,y =
∑
µ ∈Ep
ψ(µ )
x
ψ(µ )
1
ψ(µ )
y ψ(µ ) ∗
z =
∑
µ ∈Ep
χ(p)
x (µ) χ(p)
y (µ) χ(p)
z∗ (µ)
∑
u∈W (+)
p
|χ(p)
u (µ)|2
. (1.1)
The eigenvaluesχ(p)
x (µ) = ψ(µ )
x /ψ(µ )
1 ofNx providep2 linear representationsNy →χ(p)
y (µ),
i.e., characters of F , labelled by the set Ep,
χ(p)
x (µ) χ(p)
y (µ) =
∑
z∈W (+)
p
(p)N z
x,y χ(p)
z (µ). (1.2)
With an appropriate reinterpretation of the labels this is t he general setting for any
RCFT. In particular for WZW models based on the ˆsl(n)k integrable representations (a
subclass of the admissible representations at integer leve l k =p′ −n), both indices of the
unitary matrix ψ(µ )
λ belong to the alcove P k
+, ψ(µ )
λ is a symmetric matrix which coincides
with the modular matrix, ψ(µ )
λ = S(p′)
λµ , while (1.1) reduces to the Verlinde formula [15]
for the fusion rule (FR) multiplicities, i.e., the dimensio ns of the spaces of chiral vertex
operators.
In [9] we have speciﬁed the above general setting to the case o f the generic subseries
κ = 3/p of the admissible representations, describing explicitly one of the fusion matrices,
a ‘fundamental’ fusion matrix Nf . Here f is some analog of the g = sl(3) fundamental
weight ¯Λ 1 = (1, 0), but the product of Nf with any Nx produces generically seven terms,
each appearing with multiplicity one. The numbers (p)N z
f,y = 0, 1 were found by solving
2
a set of algebraic equations coming from the decoupling of si ngular vectors in g = ˆsl(3)k
Verma modules. More precisely the decoupling of the ‘horizo ntal’ singular vectors (which
exist also for generic values of the level, κ ⁄∈Q) determines the generic seven points, while
the additional truncation conditions, including the ones a t rational level, were obtained
making also some assumptions suggested from explicit compu tations at small values of
p. Although Nf together with its conjugate Nf ∗ are not suﬃcient to build up the full
polynomial fusion ring, diagonalising this matrix in an ort honormal basis, i.e., ﬁnding
the eigenvector matrix ψ(µ )
y (common to all fusion matrices) recovers through (1.1) all
FR multiplicities. We called (1.1) Pasquier–Verlinde type formula since similar formulæ
– though with diﬀerent interpretation of the structure cons tants (no more required to be
nonnegative integers), were ﬁrst discussed in [13] in the co ntext of lattice ADE models.
Such formulæ, together with their dual counterparts, descr ibing the structure constants
of a ‘dual’ algebra, have been furthermore exploited in the s tudy of nondiagonal modular
invariants of the integrable WZW conformal models [5], [14] .
Diagonalising a p2 ×p2 matrix becomes a tedious task for big p (we have done this
exercise for p = 4, 5) so it is preferable to have an explicit analytic formula fo r ψ(µ )
y , or
equivalently, for the characters χ(p)
y (µ) of the fusion algebra. The path we follow in this
paper to ﬁnd the characters χ(p)
y (µ) was suggested by the second formula for the admissible
FR multiplicities conjectured (with slightly changed nota tion) in [9],
(p)N z
x,y :=
∑
w′∈W [z]
det(w′) mx
w′ z y −1. (1.3)
This formula is analogous to the formula for the integrable F R multiplicities derived in
[11],[16], [8], which is a truncated version of the classica l Weyl–Steinberg formula for the
tensor product multiplicities of ﬁnite dimensional repres entations of the horizontal subal-
gebra g (with the role of the horizontal Weyl group W taken by the aﬃne Weyl group W ).
In (1.3) the summation runs over the Kac–Wakimoto (KW) aﬃne g roup W [z], generated
by Kac–Kazhdan reﬂections corresponding to singular vecto rs of the g Verma module of
highest weight parametrised by the element z ∈W . In the integrable case the counterpart
of mx
v is the multiplicity mλ
µ of the weight µ of the g ﬁnite dimensional module of highest
weightλ. Here the integers mx
v,x,v ∈W describe a generalised (ﬁnite) weight diagram.
The realisation that one has to generalise the classical not ion of weight diagram in order
to describe the rational level FR was the main lesson of the, o therwise still incomplete,
analysis of the null-decoupling equations of [9]. While the g weight diagrams are subsets
3
of the root lattice Q of g, attached to the highest weight λ, in our case the role of a ‘root
lattice’ is taken by the aﬃne Weyl group W = W ⋉tQ at a generic ( κ ⁄∈Q) level. Now
the question is, can one ﬁnd formal characters encoding this information about the gener-
alised weight diagrams, which furthermore are closed under multiplication and recover a
‘classical’ analogue of (1.3) at generic levels, with the aﬃ ne KW groups replaced by their
horizontal counterparts W
[z]
. Then by analogy with the integrable case one can ‘quantise’
these ‘classical’ characters imposing the periodicity con ditions, accounting for the rational
level, and thus recover the linear representations of F .
Though it is not necessary, to understand our way of reasonin g and the motivating
idea it is helpful to imagine that there is a ﬁnite dimensiona l algebraic object playing the
role of g. The irreps of the assumed hidden algebra are labelled in gen eral by x ∈ ˜W (+),
a fundamental subset of the extended aﬃne Weyl group ˜W = W ⋉tP with respect to
the right action of W (equivalent to the action of the horizontal KW Weyl group, se e [12]
and the text below). The same set also parametrises maximall y reducible Verma modules
of g at generic level and the corresponding irreducible quotien ts. In the simplest ˆsl(2)k
case solved in [1], [6] this intrinsic algebra is the Z2 graded algebra osp(1|2) [7]; the Weyl
groupW ≃ Z2 ofsl(2) distinguishes between even and odd vacuum state ﬁnite di mensional
irreps of osp(1|2). Alternatively mapping ι : ˜W →Q one can use the horizontal subalgebra
g =sl(2) itself, but restricting to its representations with hig hest weights on the root lattice
Q (integer isospins). In general this map ι (see section 2) allows to describe the generalised
modules through subsets of the supports of standard modules of g (with highest weights
of n-ality zero); the case sl(2) is trivial since then Im( ι) ≡Q.
The construction of the ‘classical characters’ at generic l evel, k ⁄∈Q, takes a consid-
erable part of this work and is its main novel result. It is don e in the ﬁrst part of the
paper (sections 2,3,4) by full analogy with the standard cas e starting with some analogs of
the Verma module characters, used as ingredients in a genera lised Weyl character formula.
While the input about the relevant generalised supports of t he ﬁnite or inﬁnite ‘mod-
ules’ (the set of weights and their multiplicities) is essen tially taken over from [9], slightly
rephrased and generalised, the main eﬀort here is to ﬁnd the p roper multiplicative struc-
ture of the formal characters. They are elements of the group ring Z[ ˜W ] of the extended
aﬃne Weyl group of ˆsl(3)k, closed under multiplication. The structure constants of t he
resulting commutative subring ˜W of Z[ ˜W ] satisfy a generalised Weyl-Steinberg formula.
As a side result one obtains an explicit formula for the cardi nality of the generalised weight
4
diagrams, i.e., for the dimensions of the ‘ﬁnite dimensiona l modules’ of the unknown alge-
bra possibly generalising osp(1|2). Some steps of the construction in this ﬁrst part hold,
or are straightforwardly generalisable, for g = ˆsl(n)k, arbitrary n. So we keep the expo-
sition general although we present the details fully for the case g = ˆsl(3)k; the general
case will be elaborated elsewhere. In the second part (secti ons 5,6,7) we consider rational
values κ = 3/p, thus a generic subseries of the admissible representation s of g = ˆsl(3)k.
The formal characters are ‘quantised’ imposing periodicit y constraints and realised as C
- valued functions. They satisfy the orthogonality and comp leteness relations equivalent
to the unitarity of ψ(µ )
y , so that one recovers the Pasquier–Verlinde type formula (1 .1).
Thus given the characters both formulæ for the FR multiplici ties of the admissible repre-
sentations (1.1) and (1.3) derive from the classical analog of the Weyl–Steinberg formula
established in the ﬁrst part of the paper. Furthermore one pr oves a third formula for the
FR multiplicities, conjectured in [9], which also has a ‘cla ssical’ counterpart,
(p)N z
x,y = (3p) ¯N ι(z)
ι(x) ι(y), (1.4)
where (3p) ¯N ι(z)
ι(x) ι(y) are structure constants of the integrable fusion algebra at κ = 3p, while
ι is the map sending ˜W to a subset of the triality zero weights. Presumably the fusi on
rules of ˆsl(n) WZW at κ =n/p are given by the above formula with n substituting 3.
2. Preliminaries.
We start with ﬁxing some notation. Let ∆ , ∆ +, Π = {α1,...,α n−1} be, respectively,
the sets of roots, positive roots, and the simple roots of g = sl(n), and ∆ re, ∆ re
+ =
∆ + ∪ (∆ + Z>0 δ), Π = {α0 =δ − ∑
iαi, Π }, – the set of real roots, real positive roots
and the simple roots of the aﬃne algebra g = ˆsl(n)k. Let Λ i be the fundamental weights
of g, i.e., ⟨Λ i,α j⟩ =δij, with respect to the Killing-Cartan bilinear form ⟨·, ·⟩ on the dual
¯h∗ of the Cartan algebra. With Q = ⊕i Z αi and P = ⊕i Z Λ i we denote the root and
weight lattices of g. Their positive cones are Q+ = ⊕i Z≥0 αi and P+ = ⊕i Z≥0 Λ i. The
negative cone −Q+ is the support of the g Verma module of 0 highest weight, while P+ is
the chamber of integral dominant weights – the highest weigh ts of the ﬁnite dimensional
representations of g. The form ⟨·, ·⟩ extends to ˜h∗ = ¯h∗⊕CΛ 0 ⊕Cδ with ⟨¯h∗, CΛ 0⊕Cδ⟩ = 0,
⟨Λ 0, Λ 0⟩ = 0 = ⟨δ,δ ⟩, ⟨δ, Λ 0⟩ = 1. The fundamental weights of g are {Λ i = Λ 0 + Λ i},
Λ 0 = 0. The ‘horizontal’ projection(·) : ˜h∗ → ¯h∗ is deﬁned as having the kernel Cδ ⊕ CΛ 0.
The Weyl vector is ρ = ∑
j Λ j. The Weyl group W of g is a ﬁnite Coxeter group generated
5
by the simple reﬂections wi = wα i with relations ( wi)2 = 1 = ( wiwi+1)3, wiwj = wjwi,
j ⁄= i ± 1, i,j = 1, 2,...,n − 1. The aﬃne Weyl group W is generated by the simple
reﬂections wj, j = 0, 1,...,n − 1 with the same type of relations (for n> 2), identifying
wn = w0. These groups can be depicted by their Cayley graphs, in whic h the vertices
correspond to elements of the group, edges to the generators , and the elementary polygons
to the relations. E.g., ﬁg. 1 depicts (a ﬁnite part of) the Cay ley graph of the aﬃne Weyl
group W of g = ˆsl(3), presented as {wi : (wi)2 = 1 = ( wiwj)3, {i,j } ⊂ { 0, 1, 2}}, while
any of the ‘12’ elementary hexagons on ﬁg. 1 is the Cayley grap h of the corresponding
horizontal Weyl group W . The labels i on the edges correspond to the generators wi,
i = 0, 1, 2. The ‘origin’ of the graph, the vertex corresponding to the group unit 1 is
denoted by ◭ ◮. The three types of hexagons (‘12’, ‘01’, and ‘20’) correspo nd to the three
Artin type relations among the generators. It is convenient to introduce the following
shorthand notation: wijk... =wiwjwk... .
We will also need the extended aﬃne group ˜W deﬁned as the semi-direct product
˜W =W ⋉tP (while W = W ⋉tQ ), tP being the subgroup of translations in the weight
lattice P . The elements tβ , β∈P, act on ˜h∗ as
tβ (Λ) = Λ + ⟨Λ ,δ ⟩β −
(
⟨Λ ,β ⟩ + 1
2 ⟨β,β ⟩⟨Λ ,δ ⟩
)
δ, (2.1)
and for α ∈ ∆ , lδ −α ∈ ∆ re
+, y ∈ ˜W , β∈P, one has the properties
tlα =wlδ−α wα , yt β y−1 =t¯y(β ), yw α y−1 =wy(α ). (2.2)
We have denoted by overbar the projection of ˜W onto the horizontal subgroup W sending
the aﬃne translations to the unit element.
The group ˜W can be also written as ˜W =W ⋊A, whereA is the subgroup of ˜W which
keeps invariant the set of simple roots Π of g. It is a cyclic group generated by γ =tΛ 1
¯γ,
where ¯γ =w1... wn−1 is a Coxeter element in W generating the cyclic subgroup ¯A ofW .
One has γ(αj) = αj+1 =γj+1(α0) for j = 0, 1, 2, · · ·,n −1 identifyingαn ≡α0. In the case
of g =sl(3) we will think of the Cayley graph of ˜W as a 3-sheeted covering of the graph of
W with, for example, the “ﬁber” over the edge ‘0’ connecting th e vertices 1 and w0 being
the set U = {A,Aw 0} and this part of the graph of ˜W is depicted on ﬁg. 2. The oriented
edges correspond to γ and the squares – to the implementation of the automorphism o f
W , wα →γw αγ−1 =wγ (α ), α∈ Π.
6
Introduce the set P = {Λ = y ·kΛ 0, y ∈ ˜W } where the shifted action of w ∈ ˜W on
˜h∗ is given by w · Λ = w(Λ +ρ) −ρ. In this and the following two sections we shall assume
that the level k is generic, k ⁄∈Q, which in particular ensures that if y ·kΛ 0 = kΛ 0 then
y ≡ 1.
According to the general criterion of Kac-Kazhdan if ⟨Λ + ρ,β ⟩ is a positive integer
for some β ∈ ∆ re
+ the Verma module MΛ , Λ ∈ P , of g is reducible, containing a Verma
submodule Mwβ ·Λ . In particular if for some y = ¯yt −λ ∈ ˜W and α ∈ ∆ + we have y(α) =
⟨λ,α ⟩δ + ¯y(α) ∈ ∆ re
+, then the KK condition is fulﬁlled for Λ = y ·kΛ 0 and the root
β =y(α), and using (2.2)
wy(α ) · Λ = yw α y−1 · Λ = yw α ·kΛ 0 = ¯yw αt−w−1
α (λ ) ·kΛ 0. (2.3)
If y(αi) ∈ ∆ re
+, ∀ αi ∈ ¯Π , the reﬂections wy(α i) generate an isomorphic to W group W
[Λ]
(to be denoted also W
[y]
), introduced by Kac-Wakimoto [12]. We shall refer to these
groups as (horizontal) KW (Weyl) groups. According to (2.3) we can identify the action
of a KW group with the right action of W on ˜W .
Now we introduce the subset P+ ⊂ P of weights Λ such that the corresponding
Verma modules MΛ are maximally reducible. From the above discussion it is cle ar that
P+ = ˜W (+) ·kΛ 0, where
˜W (+) = {y ∈ ˜W |y(αi) ∈ ∆ re
+ for ∀αi ∈ Π }. (2.4)
The Bruhat ordering on the orbit W
[Λ]
·kΛ 0 describes the embedding pattern among the
Verma modules {MΛ ′, Λ ′ ∈W
[Λ]
·kΛ 0}.
Denote W (+) = ˜W (+) ∩W . One has
Proposition 2.1 P+ is a fundamental domain in P with respect to the action of the KW
Weyl groups, or, equivalently, ˜W (+) (W (+)) is a fundamental domain in ˜W (W ) with
respect to the right action of W.
Proof: Let us introduce some notation ﬁrst. Let Hα = {λ ∈ ¯h∗ | ⟨λ, α⟩ = 0 } be the
hyperplane orthogonal to the root α. For w ∈W let I(w) = {i |w(αi)< 0, αi ∈ Π } and
P (w)
+ := {λ ∈P+| ⟨λ,α i⟩> 0, i∈I(w)} =P+\
( (
∪i∈I(w) Hα i
)
∩P+
)
=P+ +
∑
i∈I(w)
¯Λ i.
The deﬁnition (2.4) can be obviously rewritten as
˜W (+) = {y ∈ ˜W |y =wt−λ , w ∈W, λ ∈P (w)
+ }. (2.5)
7
Hence the statement of the Proposition follows from ∪
w∈W
˜W (+)w = ∪
w∈W
∪
w′ ∈W
t−w′(P (w′ )
+ )w′w = ∪
w∈W
t−Pw = ˜W once the following lemma is established:
Lemma 2.2 P = ∪
w∈W
w(P (w)
+ ) is a partition, i.e., a disjoint union.
To prove the lemma one has to exploit several standard proper ties of the Weyl group W
which can be found e.g., in [10], chapter I.
Proof: Any λ′ ∈ P is represented as λ′ = w(λ) for some λ ∈ P+, w ∈ W . Denote
X = Xλ = {i | ⟨λ,α i⟩ = 0 }. According to Proposition 1.10c of [10] the element w splits
uniquely into a product of two elements of W ,w =uv, s.t. v ∈WX (the group generated
by the simple reﬂections labelled by the subset X), and u(αi)> 0, for any i ∈X. We have
v(λ) = λ, I (u) ∩X = ∅, hence λ ∈ P (u)
+ and λ′ = u(λ) ∈ u(P (u)
+ ). This proves that P
is covered by the union of subsets w(P (w)
+ ). The uniqueness of the above splitting proves
also the disjointness. □
We shall refer to ˜W (+) (or, equivalently, P+) as a ‘dominant chamber’. The left action
of the group A (the shifted action of A) keeps ˜W (+) (P+) invariant and ∪a∈Aa W (+) =
˜W (+). Similarly P+ is Z/nZ graded by the n-ality τ (Λ = ¯yt−λ ·kΛ 0) := τ (λ), where
τ (λ) = ∑
i i⟨λ,α i⟩ =n ⟨λ, ¯Λ n−1⟩ mod n is the standard grading in P .
In the case sl(3) the chamber ˜W (+) can be also expressed as ˜W (+) = U t−P+ in terms
of the subset U = {A,Aw 0} ⊂ ˜W ,depicted on ﬁg. 2.
Next we introduce a map ι of ˜W (or P) into Q
ι : ˜W ∋y = ¯yt−λ ↦→nλ + ¯y−1 · 0 = nλ −
∑
β> 0 , ¯y(β )<0
β ∈Q. (2.6)
See [11] (exercise 3.12 of ch. 3) for the last equality. A is mapped by ι to zero.
The map ι has the “twisted log” property
ι(xy) = y−1(ι(x)) +ι(y). (2.7)
Compare with the horizontal projection map
h : ˜W ∋y =yt−λ ↦→h(y) = y ·kΛ 0 =y · (−κλ) ∈κP +W · 0,
h(xy) = h(x) + ¯x(h(y)).
(2.8)
8
The map (2.6) provides another equivalent deﬁnition of the c hamber ˜W (+). Indeed
comparing with (2.5) and using that 1 ≤ ⟨ρ, α⟩ ≤n − 1 for any α ∈ ∆ + one easily checks
˜W (+) = {y ∈ ˜W |ι(y) ∈P+}. (2.9)
The relation (2.7) implies that ι intertwines between the KW action (equivalent ac-
cording to (2.3) to the right action of W on ˜W ) and the ordinary shifted action of W ,
i.e.,
ι(yw) = w−1 ·ι(y), w ∈W . (2.10)
Both subsets of Q, the image Im(ι) and its complement are invariant under the shifted
action of the Weyl group W . The g Verma modules of highest weight ι(y) are reducible
iﬀ the corresponding g Verma modules of highest weight Λ = y ·kΛ 0 are reducible and the
pattern of embeddings of submodules in both cases is identic al.
On ﬁg. 3 we have illustrated the map 1
3ι for the case g = sl(3). It maps the even
(under the gradation det( w) = ±1) elements of W to P and the odd elements to P +θ/3
(θ = α1 +α2) in such a way that the vertices of the Cayley graph (if we make it into a
‘rigid’ geometrical graph by ﬁxing the length of each edge to be of length
√
2/3 assuming
as usual that the roots of sl(3) are of length
√
2) geometrically ‘sit’ at the same places
as the vertices of the two lattices P and P + θ/3. (See the ﬁgure.) In other words
reﬁning by 3 the weight lattice, Λ i → Λ i/3, (or equivalently, rescaling κ → κ/3) the
points of the Cayley graph can be identiﬁed with a subset of th e triality zero weights
{λ = ∑
i 3niΛ i/3} ∪ {λ = ∑
i (3ni + 1)Λ i/3} in the reﬁned lattice, while the “excluded”
triality zero points λ = ∑
i (3ni − 1)Λ i/3 ∈ P −θ/3, correspond to the centers of the
elementary hexagons.
Remark. The above analysis properly extends to the larger than P region
{Λ = y · (λ′ +kΛ 0), y ∈ ˜W , λ′ ∈P ; k ⁄∈Q}.
It contains a subset with y ∈ ˜W (+), λ′ ∈ P+, providing highest weights of ‘maximally
reducible’ g Verma modules. For our purposes it is suﬃcient to choose λ′ = 0 thus
restricting to weights Λ parametrised by y ∈ ˜W .
9
3. Characters.
Let us start by recalling the supports and characters of ordi nary Verma and ﬁnite
dimensional modules of g. The latter characters are elements of the group ring Z[tP ] of
the group of translations by the weight lattice. Keeping wit h tradition, the translations
t−λ from the previous section will be written as formal exponent ials e−κλ ;κ = −1 recovers
the standard notation, see, e.g., [3] for standard deﬁnitio ns. The character of the Verma
module Vλ of highest weight λ is given by
ch(Vλ ) =
∑
µ ∈λ −Q+
K
λ
µ e−κµ = e−κλ ∑
β ∈Q+
Kβ eκβ = e−κλ ∏
α ∈∆ +
(1 − eκα )−1 = e−κ (λ +ρ ) dκ ,
(3.1)
where the multiplicity K
λ
µ of an weight µ is expressed via the Kostant partition function
K
λ
µ :=Kλ −µ ∈ Z≥0, whiledκ is a W invariant (up to a sign) quantity w(dκ ) = det(w)dκ
for w(eκβ ) := eκw (β ). The support of a module is the set of weights µ of nonzero multi-
plicityK
λ
µ , thus suppVλ =λ −Q+.
The irreducible ﬁnite dimensional modules can be resolved i n terms of Verma modules,
i.e., each Verma module Vw·λ , with w ∈ W and λ ∈ P+, contains submodules of weight
Vw′·λ for all w′>w in the Bruhat ordering of W (in a convention in which 1 is the smallest
element) and grading W by the reduced length of words the Verma module inclusions
organize in a BGG (Bernstein–Gelfand–Gelfand) resolution . For the characters χλ ,λ ∈P+
of irreducible ﬁnite dimensional modules the BGG resolutio n gives immediately the Weyl
character formula
χλ =
∑
w∈W
det(w) ch(Vw·λ ) = dκ
∑
w∈W
det(w) e−κw (λ +ρ ) =
∑
µ ∈P
mλ
µ e−κµ ,
mλ
µ =
∑
w∈W
det(w) Kw·λ −µ ,
(3.2)
and from χ1 = 1 the factor dκ is expressed as 1/dκ = ∑
w∈W det(w) e−κw (ρ). The support
(weight diagram) is Γ λ = {µ ∈P |mλ
µ ⁄= 0}. From (3.2) it follows that
w(χλ ) = χλ , mλ
w(µ ) =mλ
µ , (3.3)
and, extending the ﬁrst line of (3.2) to λ ∈P ,
χw·λ = det(w)χλ . (3.4)
10
The map ι introduced in (2.6) establishes a correspondence between ( highest weights of)
Verma modules of the aﬃne algebra g and of the horizontal subalgebra g, with identical
reducibility structure. Now we shall introduce another cla ss of ‘Verma modules’ Vy (of
yet unknown ﬁnite dimensional algebra) described through i ts supports, i.e., weights and
their multiplicities. The supports are parametrised by ele ments of aW ⊂ ˜W (for a ﬁxed
a ∈ A) and mapped by ι into subsets of supports of g Verma modules. Motivated by
the intertwining property (2.10) we shall call such a module reducible if its ι image is
a reducible Verma module. In particular the maximally reduc ible ‘Verma modules’ have
highest weights Λ = y ·kΛ 0,y ∈ ˜W (+), whence the name ‘dominant chamber’ for the latter
subset of ˜W . Furthermore in full analogy with the representation theor y of g we shall
introduce ‘ﬁnite dimensional modules’ obtained factorisi ng maximal ‘Verma submodules’
of reducible ‘Verma modules’ by an analog of the BGG resoluti on in which the role of W is
replaced by the action of the KW group, equivalent according to (2.3) to the right action
of W on ˜W . We have already explained on the example of g =sl(3) this construction in
[9] on the level of multiplicities of weights, here we add a re alisation of the characters of
these ‘Verma- and ﬁnite dimensional modules’. It recovers t he prescribed multiplicities but
furthermore allows to consider a tensor product of ‘ﬁnite di mensional modules’ realised by
a multiplication of their characters. The result is a new com mutative ring which extends
the ring of g characters. It will be used in sections 6,7 as a basis for the c onstruction of
quantised ‘q’-characters which realise the fusion rules of the admissib le representations at
rational level.
We can describe the analogs of the multiplicities in (3.1) vi a the mapι, so what remains
to be done is to generalise the formal exponentials entering (3.1). The naive extension of
the map ι to the characters, thus leading to ordinary formal exponent ials with arguments
involving the weights ι(y) (or the horizontal projections ¯Λ = h(y) ∈ ¯h∗) is possible but is
not consistent (except in the case g = sl(2)) since in general a sum of such weights goes
beyond the image of ι. (This is in agreement with the fact that there is no nontrivi al
subset of the n-ality zero representations of g closed under tensor products). So our main
idea is, instead of exponentials (elements of the group alge bra of the group of translations
tP ) assigned to weights, to consider the elements w e−κλ = y ∈ ˜W, i.e., the generating
elements of the group algebra of the group ˜W (the extension of tP over W ). (We shall
use the same notation for both interpretations denoting as b efore sometimes the aﬃne
11
translations by formal exponentials.) 1 Unlike the formal exponentials these generating
elements do not commute any more (rather satisfy the multipl ication rules of ˜W in (2.2),
but nevertheless the ‘ﬁnite dimensional module’ character s we obtain, do commute and
multiply according to the rules conjectured in our previous paper.
Now we introduce the supports, Vu and Gu, and characters, ch( Vu) and χu, of,
respectively, ‘Verma’ and ‘ﬁnite dimensional modules’. Th e supports are certain inﬁnite
or ﬁnite subsets of the extended aﬃne Weyl group ˜W while the characters are certain
(formal) series or ﬁnite sums with integer coeﬃcients of ele ments of ˜W .
Let Λ = y ·kΛ 0, y ∈aW,a ∈A. We deﬁne
Vy := {z ∈aW |ι(z) ∈ι(y) −Q+} = {xy | x ∈W , ι(x) ∈ −y(Q+)}. (3.5)
Alternatively, using that any ν ∈ Q+ can be represented uniquely as ν = nβ +λ, with
someβ ∈Q+ andλ ∈Q+/nQ+ = {∑ n−1
i=1 kiαi | 0 ≤ki ≤n − 1}, we can bring Vy into the
form
Vy = T yyt Q+ = {tuy(β )uy |u ∈ T y, β ∈Q+}. (3.6)
Here the ﬁnite subsets T y ⊂ W , which project horizontally to W, are subject to the
condition
T y = {u ∈W | − ¯y−1(ι(u)) ∈Q+/nQ+}. (3.7)
E.g., if an element u ∈ T y projects to a reﬂection wα ∈W ,α ∈ ∆ + then it equals u =wα ,
or u =wα t−α =wδ−α if y−1(α) ∈ ∆ +, or y−1(−α) ∈ ∆ +, respectively.
Thus the support Vy in (3.5) naturally generalises the support of a g Verma module,
being deﬁned as a collection of |W | “positive” (for a choice of a set of simple roots)
root lattice cones tu y(Q+) applied to uy ∈ T yy. The two descriptions of Vy reﬂected in
(3.6) and in (3.5) – as a collection of supports of ordinary g modules of highest weights
h(uy ) = uy ·kΛ 0, or as the support of g module of highest weight ι(y) with some ‘excluded’
points, will be both useful in what follows. Next we deﬁne the multiplicity of an weight z
through its ι image,
K y
z :=Kι(y)−ι(z) or K y
xy =K−y−1(ι(x)), (3.8)
1 From now on w eκλ will stand for the multiplication of two elements in the group ring Z[ ˜W ]
; accordingly the standard notation for the action of the (horizontal) Weyl grou p on the formal
exponentials, w(e−κλ ) = e−κw (λ ) , will be replaced by e−κw (λ ) = we−κλ w−1, cf. (2.2).
12
whereKβ is the Kostant partition function in (3.1). Then the charact ers generalising (3.1)
are deﬁned according to
ch(Vy) :=
∑
z ∈ ˜W,zy −1 ∈W
ι(z) ∈ι(y) −Q+
zK y
z =
∑
x ∈W ,
ι(x) ∈ −y(Q+)
xyK −y−1(ι(x)). (3.9)
Equivalently, using that −¯y−1(ι(x)) = −¯y−1(ι(u)) +nβ for xy =uytβ , and denoting
Pr e−κ ρdκ :=
∑
β ∈Q+
Knβ +r eκ β , (3.10)
we rewrite (3.9) as
ch(Vy) =
∑
u∈T y
uyP −¯y−1(ι(u)) e−κ ρdκ . (3.11)
Multiplying both sides of (3.10) by e
κ
n r, summing overr ∈Q+/nQ+ and making a change
of variables nβ +r = β′, we recover in the r.h.s. the factor e− κ
n ρdκ/n , cf. (3.1). Thus
Pr are polynomials of translations in Q+ determined through the quotient of the standard
denominators, dκ/n and dκ .
∑
r∈Q+/nQ +
Pr e
κ
n r = e− κ
n ρdκ/n
e−κ ρdκ
=
∏
α> 0
n−1∑
kα =0
e
κ
n kα α =
∑
µ ∈Q+
(n)Kµ e
κ µ
n , (3.12)
Pr =
∑
ν ∈Q+
(n)Kr+nν eκ ν . (3.13)
The partition function (n)Kµ deﬁned through the last equality in (3.12) is apparently
nonzero for a ﬁnite subset of Q+, i.e., the summation in (3.13) is ﬁnite. The relations
(3.10), (3.13) imply
Knβ +r =
∑
ν ∈Q+
(n)Knν +r Kβ −ν . (3.14)
We have the symmetry properties
ch(Va y ) = a ch(Vy ),
a−1 T aya = T y, P −(ay)−1(ι(aua−1)) =P−¯y−1(ι(u)),
(3.15)
using that ι(a) = 0, ι(a−1xa) = ¯a−1(ι(x)) for a ∈A.
Now consider Λ = y ·kΛ 0 ∈ P +, y ∈ ˜W (+), hence ι(y) ∈ P+. According to our
deﬁnition Vy is reducible with submodules Vyw, w ∈ W, since Vι(y) is reducible with
13
submodules Vw−1·ι(y). In parallel with (3.2) we deﬁne the characters of ‘ﬁnite dime nsional
modules’ by a ‘resolution’ formula with respect to the KW Wey l group
χy :=
∑
w′∈W
[Λ]
det( ¯w′) ch( Vw′ y) =
∑
w∈W
det(w) ch( Vy w) =
∑
z∈ ˜W , zy −1∈W
my
z z. (3.16)
We extend this deﬁnition to the whole ˜W , i.e.,
χyw = det(w)χy, y ∈ ˜W (+), w ∈W . (3.17)
Using (3.8) and the intertwining property (2.10) of the map ι (3.16) gives for the multi-
plicities my
z (cf. (3.2) )
my
z =
∑
w∈W
det(w) K yw
z =
∑
w∈W
det(w) Kι(yw)−ι(z) =
∑
w∈W
det(w) Kw·ι(y)−ι(z) =mι(y)
ι(z).
(3.18)
Having an explicit description for the multiplicities we ca n introduce the supports
Gy of ‘ﬁnite dimensional modules’ as Gy = {z ∈ ˜W |my
z ⁄= 0 }. From (3.18) and from
the deﬁnition of the map ι it follows that these ‘generalised weight diagrams’ have th e
structure of n-ality zero sl(n) weight diagrams Γ ι(y) with the points µ ⁄∈Im(ι) excluded.
Ansl(3) example is illustrated on ﬁg. 4, see [9] for more examples . Let us point out some
symmetry properties of the generalised weight diagrams. We have from (3.15)
χa y =aχ y, a ∈A, (3.19)
which implies that may
az = my
z . The invariance of the g multiplicities mι(y)
¯a(ι(z)) = mι(y)
ι(z) =
mι(y)
ι(a z a−1) ) implies
my
a−1 z a =my
z, a ∈A (3.20)
and hence aχ ya−1 =χy. Forz =at −µ , a∈A, the symmetry property (3.20) extends to
my
a t−w(µ )
=my
a t−µ , w ∈W, (3.21)
using once again (2.7) to obtain ι(awa −1zw−1) = w(ι(z)) as well as the invariance of the
g multiplicitiesmι(y)
w(ι(z)) =mι(y)
ι(z) for any w ∈W .
Now we examine the case g = sl(3) in details. The 6 element sets T y are T ¯a =
aWa −1, while T ¯awθ =a T wθ a−1, and T wθ = {1,w 010,w 020,w 10,w 20,w 0}, see ﬁgs. 5,6,
where the two basic supports are ‘visualized’ as certain sub graphs of the Cayley graph of
14
W .The set of polynomials P−¯y−1(ι(u)) in (3.11) associated with T y and the corresponding
characters for y = 1,w θ read
ch(Vt−λ
) =
∑
w∈W
w P−ι(w) e−κ (λ +ρ ) dκ
=
[
(1 + 2eκθ ) +w12(2 + eκα 1) +w21(2 + eκα 2 )
+w1(1 + eκθ + eκα 2 ) +w2(1 + eκθ + eκα 1 ) + 3wθ
]
e−κ (λ +ρ ) dκ ,
(3.22)
ch(Vwθ t−λ
) =
∑
u∈T wθ
uw θP−θ −1(ι(u)) e−κ (λ +ρ ) dκ
=
[
w0wθ (2 + eκθ ) +w010wθ (1 + 2eκα 2) +w020wθ (1 + 2eκα 1 ) (3 .23)
+w20wθ (2 + eκα 1 ) +w10wθ (2 + eκα 2 ) +wθ (1 + 2eκθ )
]
e−κ (λ +ρ ) dκ .
Now we rewrite the ‘ﬁnite dimensional module’ characters (3 .16) expressing them in
terms of the ordinary sl(3) characters, the elements of A and the ‘class’ element
F ≡
∑
a∈A
aw 0a−1 =w0 +w1 +w2 . (3.24)
Proposition 3.1 For any x =xt −λ =t−νx ∈ ˜W (+), ν =x(λ) we have
χx = det(x)
(
χν +γχν −2Λ 1
+γ−1χν −2Λ 2
+ (F + 2)
(
χν −ρ +γχν −Λ 2
+γ−1χν −Λ 1
) )
=χλ +x−1·0 +γχλ +x−1·(−2Λ 1) +γ−1χλ +x−1·(−2Λ 2)
+ (F + 2)
(
χλ +x−1·(−ρ ) +γχλ +x−1·(−Λ 2) +γ−1χλ +x−1·(−Λ 1)
)
.
(3.25)
Proof: First the ‘Verma module’ characters (3.22), (3 .23) can be rewritten for any x =
xt −µ ∈ ˜W as (recall that γ =w12 e−κ Λ 2 )
ch(Vx) =
[
(1 +γeκ x−1(2Λ 1) +γ−1eκ x−1(2Λ 2))
+ (F + 2)(eκ x−1(ρ) +γeκ x−1(Λ 2) +γ−1eκ x−1(Λ 1))
]
dκ e−κ (µ +x−1(ρ)).
(3.26)
Next apply the ‘resolution’ formula (3.16) in the form
χx =
∑
w′∈W
[x]
det( ¯w′) ch(Vw′ x) =
∑
w∈W
det(w) ch(Vxw t−w−1 (λ )
)
15
= det(x)
∑
w∈W
det(w) ch(Vw t−w−1 (x(λ ))
).
To obtain the second equality in (3.25), i.e., to express the characters in terms of sl(3)
charactersχλ withλ ∈P+, we have used (3.4), so that each term det( x)χν −ν a turns into
χλ +x−1·(−ν a). □
Taking into account the same property (3.4) (which in partic ular implies that χλ = 0
for weights on the shifted reﬂecting hyperplanes, i.e., wα ·λ =λ for some α ∈ ∆ +) some
terms in the general expression (3.25) may vanish or compens ate each other for some
‘boundary’ weights.
The character formula (3.25) can be also rewritten as a decom position over W, or U
χy = ∑
w∈Ww B(w)
y = ∑
u∈Uu C(u)
y with some coeﬃcients B(w)
y (C(u)
y ) given by linear
combinations of sl(3) characters and formal exponentials. From this decompos ition the
multiplicity my
z in (3.18) can be rewritten as a sum of sl(3) multiplicities. E.g., rewrite
(3.25) for the character χx,
χx =
∑
µ ∈P
P λ
µ e−κµ :=
∑
a∈A ,µ ∈P
(
(mλ +x−1·(−ν a)
µ + 2mλ +x−1·(−ν
′
a)
µ )a +mλ +x−1·(−ν
′
a)
µ F a
)
e−κµ
=
∑
a∈A ,µ ∈P
( (
mλ +x−1·(−ν a)
µ + 2mλ +x−1·(−ν
′
a)
µ
)
a +
( ∑
b∈A
mλ +x−1·(−ν
′
b)
µ +µ b,a
)
aw 0
)
e−κµ
=
∑
z =at −µ
a ∈A,µ ∈P
mx
za e−κµ +
∑
z =aw 0t−µ
a ∈A,µ ∈P
mx
z aw 0 e−κµ (3.27)
where the weights νa, ν
′
a ∈P can be read from (3.25), and the polynomials P λ
µ = P λ
w(µ )
are invariant under the nonshifted action of W . The weights µb,a ∈ P+ result from the
resummation of the ‘odd’ term in (3.25), settingwja =bw0t−µ a,b ,b ∈A (since ˜W = U tP ),
which allows comparing the second and the third lines in (3 .27) to get an expression for
the multiplicities mx
z in terms of the sl(3) ones.
Let us give some examples
χa =a, a ∈A,
χw0
= 2 + w0 +w1 +w2 = 2 + F,
χf ≡χt− ¯Λ 1
=χ ¯Λ 1
+ (1 +F )γ−1 =χγ −1 χw20
=γ−1 (w20 +w12 +w01 +w0 +w1 +w2 + 1),
χf ∗ ≡χt− ¯Λ 2
=χ ¯Λ 2
+ (1 +F )γ =χγ χw10
=γ (w10 +w21 +w02 +w0 +w1 +w2 + 1).
(3.28)
16
Finally we deﬁne dimensions of the ‘ﬁnite dimensional modul es’ by setting in (3.16)
every (generating) element w e−κµ in Z[ ˜W ] to 1, i.e., for y = ¯yt −λ ∈ ˜W (+)
Dy =
∑
z∈ ˜W
my
z. (3.29)
Using the decomposition formula (3.25) the dimension can be expressed as a sum of di-
mensions Dλ of sl(3) ﬁnite dimensional representations – the ﬁnal expressio n can be cast
into the form
Dy = 9
∏
α> 0
⟨¯y(λ) + ρ
3, ¯y(α)⟩ + det(¯y)
3
= 1
3
∏
α> 0
⟨ι(y) +ρ, α⟩ + det(¯y)
3 = 2
3Dι(y) + det(¯y)
3 .
(3.30)
Sinceι(a) = 0, a ∈A we haveDy =Da y. Here are the ﬁrst few numbers produced from
(3.30): 1 , 5, 7, 19, 23, 43, 83, 103,....
Remark. In the case g = sl(2) we have ι(W ) ≡ Q = 2P and ˜W (+) ≡ At −P+. The
supports of the ‘Verma modules’ and the weight diagramsGy are isomorphic to the supports
of g = sl(2) Verma modules Vι(y) and weight diagrams Γ ι(y), respectively. Alternatively
the map 1
2ι recovers the supports of modules of highest weight 1
2ι(at −λ ) = λ ∈P+ of the
superalgebra osp(1|2), with a = 1,γ, labelling the two types of modules for a given λ.
One has χa t−λ = a(χλ +γχλ −α/ 2) and we can replace γ simply by a sign ǫ = −1, thus
recovering the supercharacters of the ﬁnite dimensional re presentations of osp(1|2). The
formula (3.30) is replaced by Dy = ⟨ι(y) +ρ, α⟩ = 2 ⟨λ + ρ
2, α⟩, y=at −λ .
