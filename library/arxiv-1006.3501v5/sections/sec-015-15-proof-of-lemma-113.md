---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-015-15-proof-of-lemma-113
section_title: "Proof of Lemma 11.3"
section_number: 15
pages: 64-69
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
Since k is an algebraically closed ﬁeld, Z(C) is a fusion category. By Section 14.1,
the coend of Z(C) is ⨁
i∈Ii∗⊗i, whereI is a representative set of simple objects
ofZ(C). By [Tu, Chapter IV], for a closed oriented surface Σ of genus g≥ 0,
τZ(C)(Σ) =
⨁
i1,...,ig ∈I
HomZ(C)(1Z(C),i ∗
1⊗i1⊗···⊗ i∗
g⊗ig)
= Hom Z(C)
(
1Z(C),
⨁
i1,...,ig ∈I
i∗
1⊗i1⊗···⊗ i∗
g⊗ig
)
= Hom Z(C)(1Z(C), (
⨁
i∈I
i∗⊗i)⊗g).
Therefore Lemma 11.3 is a direct consequence of the following lemma.
Lemma 15.1. LetC be a spherical fusion category over a commutative ring k such
that dim(C) is invertible in k. Then for any closed connected oriented surface Σ of
genus g≥ 0, the k-module|Σ|C is isomorphic to HomZ(C)(1Z(C), (C,σ )⊗g), where
(C,σ ) is the coend of Z(C).
Proof. For g = 0, the claim of the lemma follows from the computation of Sec-
tion 9.5. Suppose that g≥ 1. By the deﬁnition of the monoidal product of Z(C),
we have (C,σ )⊗g = (C⊗g,σ g), where σg ={σg
X :C⊗g⊗X→X⊗C⊗g}X∈Ob(C) is
the half braiding deﬁned by
σg
X = (σX⊗ idC ⊗(g−1) )··· (idC ⊗(g−2)⊗σX⊗ idC)(idC ⊗(g−1)⊗σX ).
By Lemma 10.2, Hom Z(C)(1Z(C), (C,σ )⊗g) is the image of the involutive endomor-
phism π of Hom C(1C,C ⊗g) carrying any f∈ HomC(1C,C ⊗g) to
π(f ) = (dim(C))−1∑
z∈I
dim(z)
PSfrag replacements
C⊗g
C⊗g
f
z
σg
z
,
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 65
where I is a representative set of simple objects of C. Without loss of generality,
we can assume that 1C∈I. For i = (i1,...,i g)∈I g and j = (j1,...,j g)∈I g, set
dim(i) =
g∏
k=1
dim(ik)
and
Vi,j = Hom C(1C,i ∗
1⊗j∗
1⊗i1⊗j1⊗···⊗ i∗
g⊗j∗
g⊗ig⊗jg).
For an explicit description of the coend ( C,σ ), see Section 14.6. In particular,
Formula (23) implies that
HomC(1C,C ⊗g) =
⨁
i,j∈I g
Vi,j.
Hence π =∑
i,j,k,l∈I gπk,l
i,j , where πk,l
i,j is a k-homomorphism Vi,j→Vk,l. Using the
expression for σ given at the end of Section 14.6, we obtain that for any f∈Vi,j,
πk,l
i,j (f ) = (dim(C))−1 dim(i) dim(l)
∑
z∈I
dim(z) Π k,l
i,j (f ),
where
(24)
Π k,l
i,j (f ) =
∑
α1∈λz⊗k∗
1 ⊗z∗⊗i1
β1∈λz∗⊗j∗
1 ⊗z⊗l1
...
αg ∈λz⊗k∗g ⊗z∗⊗ig
βg∈λz∗⊗j∗g ⊗z⊗lg
PSfrag replacements
i1
i1
j1
j1
k1 k1l1 l1
ig ig jgjg
kg kglg lg
z
z
z z
zz
zz
z
β1β1
α1α1 βgβg
αg αg
f
.
Here, for any X∈ Ob(C), we pick an I-partition (pα
X,q α
X )α∈Λ X of X and denote
by λX the set of all α∈ Λ X such that the target of pα
X is 1C. For α∈ λX , the
morphisms pα
X : X→ 1C and qα
X : 1C→X are depicted respectively as
PSfrag replacements
α
X
and
PSfrag replacements
α
X.
66 V. TURAEV AND A. VIRELIZIER
Let Σ be a closed connected oriented surface of genus g≥ 1. For i = (i1,...,i g)∈
I g and j = (j1,...,j g)∈I g, consider the following I-colored graph Gi,j on Σ:
Gi,j =
PSfrag replacements
i1
j1
i2
j2
ig
jg
.
The underlying oriented graph of Gi,j, denoted G, is a skeleton of Σ. It has one
vertex x of valence 4 g, and its complement in Σ is a disk. The surface Σ can
be obtained from a 4 g-sided polygon by gluing pairs of sides, and the graph Gi,j
corresponds to the union of radii joining the center of the polygon to the centers of
the sides:
PSfrag replacements
i1
j1
i1
j1
i2
j2
i2
j2
ig
jg
ig
jg
a1
a1
b1
b1
a2
a2
b2
b2
ag
ag
bg
bg
.
By deﬁnition, the k-module|Σ|C is isomorphic to the image of the homomorphism
p(G,G ) :|G; Σ|◦→|G; Σ|◦, where
|G; Σ|◦ =⊕i,j∈I gH(Gi,j).
The cone isomorphisms τi,j :H(Gi,j) = Hx(Gi,j)→Vi,j induce an isomorphism
τ =
∑
i,j∈I g
τi,j :|G; Σ|◦→
⨁
i,j∈I g
Vi,j = Hom C(1,C ⊗g).
Consider the automorphism κ =∑
i,j∈I g dim(j) idVi, j of⊕i,j∈I gVi,j. We claim that
(25) κτp (G,G )(κτ )−1 =π.
Hence the images of the projectors p(G,G ) and π are isomorphic. This will imply
the claim of the lemma.
By deﬁnition, p(G,G ) =∑
i,j,k,l∈I gpk,l
i,j , where
pk,l
i,j =|Σ× [0, 1], Σ×{ 0},G i,j×{ 0}, Σ×{ 1},G k,l×{ 1}|C : H(Gi,j)→H(Gk,l).
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 67
To compute pk,l
i,j , consider the C-colored graph
Gk,l
i,j = (Gop
i,j×{ 0})∪ (Gk,l×{ 1})⊂∂(Σ× [0, 1]).
By deﬁnition,
pk,l
i,j = dim(C) (dim(k) dim(l))−1 Υ
(
|Σ× [0, 1],G k,l
i,j|C
)
.
To compute the right-hand side, consider the 2-polyhedron
P = (G× [0, 1])∪ (Σ×{ 1
2})⊂ Σ× [0, 1].
We stratify P by taking as its edges the arcs x× [0, 1
2 ],x× [ 1
2, 1], and the edges of
G×{t} fort∈{ 0, 1
2, 1}. The polyhedron P has 3 vertices x×{t} witht∈{ 0, 1
2, 1}.
We orient the regions of P as shown in the next picture.
P =
PSfrag replacements
k1k1
l1
l1
k1
l1
k2
k2
l2
l2
k2
l2
kg
kg
lg
lg
jg
ig
i1i1
j1
j1
i2
j2
x
v
u
z
.
It is clear that P is a skeleton of the pair (Σ × [0, 1],G k,l
i,j ). The maps Reg( P )→I
extending the coloring of the boundary are numerated by the color z∈ I of the
unique region of P lying in Σ ×{ 1
2}. The link of the vertex ( x, 1
2 ) of P determines
aC-colored graph Γ z in S2:
Γ z =
PSfrag replacements
i1i1 j1 j1
k1 k1 l1l1
igig jgjg
kgkg lglg
z z z z z
z
z
.
Let u,v be the bottom and the top vertices of Γ z, respectively. Then
|Σ× [0, 1],G k,l
i,j|C = (dim(C))−2 ∏
y∈{i,j,k,l}
dim(y)
∑
z∈I
dim(z)µk,l
i,j (z)
68 V. TURAEV AND A. VIRELIZIER
where
µk,l
i,j (z) =∗P (FC(Γ z))∈Hu(Γ z)∗⊗Hv(Γ z)∗.
In graphical notation,
µk,l
i,j (z) = FC


PSfrag replacements
i1i1 j1 j1
k1 k1 l1l1
igig jgjg
kgkg lglg
z z
z
z
z
z
zu
v 

,
where the dotted lines represent the tensor contractions. Note that Hu(Γ z) =
H(Gi,j) and Hv(Γ z) = H(Gop
k,l).
Consider the sequence of signed objects of C
S =
(
(k1,−), (l1,−), (k1, +), (l1, +),..., (kg,−), (lg,−), (kg, +), (lg, +)
)
.
Recall the object X =XS∈ Ob(C) deﬁned by (5) and the isomorphism ψS∗ : XS∗→
X ∗ deﬁned in the proof of Lemma 2.3. Consider the cone isomorphisms
τk,l :H(Gk,l)→Vk,l = Hom C(1C,X )
and
τ¯l,¯k :H(Gop
k,l)→V¯l,¯k = Hom C(1C,X S∗ ),
where ¯k = (kg,...,k 1) and ¯l = (lg,...,l 1). For α∈λ =λX , set
aα =τ −1
k,l (qα
X )∈H(Gk,l) and bα =τ −1
¯l,¯k (ψ−1
S∗◦ (pα
X )∗)∈H(Gop
k,l).
Then
Ω =
∑
α∈λ
aα⊗bα∈H(Gk,l)⊗H(Gop
k,l)
is the inverse of the contraction pairing H(Gop
k,l)⊗H(Gk,l)→ k, cf. the proof of
Lemma 4.1(a). Therefore, for any h∈H(Gi,j),
pk,l
i,j (h) = dim(i) dim(j)
dim(C)
∑
z∈I,α∈λ
dim(z)µk,l
i,j (h⊗bα)aα.
For any f∈Vi,j,
κτk,lpk,l
i,j (κτi,j)−1(f ) = dim(i) dim(l)
dim(C)
∑
z∈I,α∈λ
dim(z)µk,l
i,j
(
τ −1
i,j (f )⊗bα
)
τk,l(aα).
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 69
We have
∑
α∈λ
µk,l
i,j
(
τ −1
i,j (f )⊗bα
)
τk,l(aα) =
∑
α∈λ
µk,l
i,j
(
τ −1
i,j (f )⊗τ −1
¯l,¯k (ψ−1
S∗◦ (pα
X )∗)
)
qα
X
=
∑
α1∈λz⊗k∗
1 ⊗z∗⊗i1
β1∈λz∗⊗j∗
1 ⊗z⊗l1
...
αg ∈λz⊗k∗g ⊗z∗⊗ig
βg∈λz∗⊗j∗g ⊗z⊗lg
α∈λ
PSfrag replacements
i1
i1
j1
j1
k1 k1
k1
k1
l1 l1
l1
l1
ig ig jgjg
kg kg
kg
kg
lg lg
lg
lg
z
z
z z
zz
zz
z
β1β1
α1α1 βgβg
αg αg
f
pα
X
qα
X
.
Using (24) and the fact that ∑
α∈λpα
Xqα
Xh =h for all h∈ HomC(1,X ), we obtain
that the latter expression is equal to Π k,l
i,j (f ). Therefore
κτk,lpk,l
i,j (κτi,j)−1(f ) = dim(i) dim(l)
dim(C)
∑
z∈I
dim(z) Π k,l
i,j (f ) = πk,l
i,j (f ).
This proves (25) and concludes the proof of the lemma. □
