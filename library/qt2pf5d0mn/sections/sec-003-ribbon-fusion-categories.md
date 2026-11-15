---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-003-ribbon-fusion-categories
section_title: "Ribbon Fusion Categories"
section_number: null
pages: 16-32
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
A is denoted by IA or I when it is clear from the context what the sub index should be.
2.1
Ribbon Fusion Categories
In this section, we give a review of monoidal category theories, which are the prelim-
inaries to the concept of G-crossed braided spherical fusion categories. In the following
subsections, we will talk about some basic ingredients such as tensor product, dual,
braiding, fusion, etc.
2.1.1
Monoidal Categories
A bi-functor ⊗on C is a functor ⊗: C×C −→C such that ⊗(ff ′, gg′) = F(f, g)F(f ′, g′).
A bi-functor is usually thought of as a binary operation and ⊗(A, B), ⊗(f, g) are written
as A ⊗B, f ⊗g, respectively. Given A ∈C0, deﬁne A ⊗· : C −→C as a functor by
(A⊗·)(B) := A⊗B and (A⊗·)(f) := IdA ⊗f. The functor ·⊗A is deﬁned analogously.
A monoidal category is a tuple (C, ⊗, 1, α, l, r), where C is a category, ⊗: C ×C −→C
is a bi-functor, 1 ∈C0 is an object, and α, l, r are natural isomorphisms ⊗◦(⊗×IdC) −→
⊗◦(IdC ×⊗), 1⊗· −→IdC, ·⊗1 −→IdC, respectively. Namely, for A, B, C ∈C0, there
are natural isomorphisms αA,B,C : (A ⊗B) ⊗C
≃
−→A ⊗(B ⊗C), lA : 1 ⊗A
≃
−→A, rA :
A ⊗1
≃
−→A. These isomorphisms need to satisfy the Pentagon Axiom and Triangle
Axiom:
7
Section 2.1
Ribbon Fusion Categories
1. Pentagon Axiom:
((A ⊗B) ⊗C) ⊗D
(A ⊗(B ⊗C)) ⊗D
(A ⊗B) ⊗(C ⊗D)
A ⊗((B ⊗C) ⊗D)
A ⊗(B ⊗(C ⊗D))
αA,B,C⊗ID
αA⊗B,C,D
αA,B⊗C,D
αA,B,C⊗D
IA⊗αB,C,D
(2.1)
2. Triangle Axiom:
(A ⊗1) ⊗B
A ⊗(1 ⊗B)
A ⊗B
αA,1,B
rA⊗IB
IA⊗lB
(2.2)
The bi-functor ⊗is called the tensor product functor, and A⊗B, f ⊗g are called the
tensor product of A and B, the tensor product of f and g, respectively.
Thus a monoidal category can be thought of as a generalization (or more precisely,
a categoriﬁcation) of a monoid such that the product and unit are given by the tensor
product functor ⊗and the object 1, respectively, and that the axioms for associativity
and unit hold only up to isomorphisms.
In a monoid (or a group), diﬀerent orders
of multiplying a sequence of elements result in the same answer due to the axioms of
associativity and unit.
In a monoidal category, since associativity only holds up to
isomorphism, we can only expect diﬀerent orders of taking tensor product of a sequence
of objects result in isomorphic objects.
Given a sequence of objects A = (A1, · · · , An), a representation X of A is an ex-
pression obtained by ﬁrst inserting 1 ′s in the sequence A1 · · · An and then putting in
parentheses so that it gives a well-deﬁned order of taking tensor product of the objects.
Denote by ⊗(X) the object resulting from taking tensor product in X. For instance,
X1 = (A1A2)A3 and X2 = (A11)(A2A3) are both representations of (A1, A2, A3). It is an
8
Section 2.1
Ribbon Fusion Categories
elementary fact that one representation can be converted into any other one by ﬁnitely
many local moves:
· · · (A1A2)A3 · · ·
←→
· · · A1(A2A3) · · ·
· · · (1A) · · ·
←→
· · · A · · ·
· · · (A1) · · ·
←→
· · · A · · ·
If X1, X2 are two representations which diﬀer by one of the above local moves, then
there is an isomorphism ⊗(X1) −→⊗(X2) given by one of α, l, r tensoring with some
identity morphisms. Thus if X1, X2 are any two representations, there exists an isomor-
phism ⊗(X1) −→⊗(X2) which is a composition of isomorphisms described above. In the
Pentagon Axiom, there are two sequences of local moves converting ((A1A2)A3)A4 into
A1(A2(A3A4)), and correspondingly there are two isomorphisms ((A1⊗A2)⊗A3)⊗A4 −→
A1⊗(A2⊗(A3⊗A4)), one going along the left and bottom side of the pentagon, the other
going along the right side. The Pentagon Axiom requires that these two isomorphisms
are equal. Similarly, in Triangle Axiom, the two isomorphisms (A⊗1)⊗B −→A⊗B are
also required to be equal. A little surprisingly, these two axioms actually imply that these
isomorphisms are always equal, which is given by the MacLane Coherence Theorem.
Theorem 2.1.1 (MacLane Coherence Theorem) [44] If X1, X2 are any two repre-
sentations of the same sequence of objects in a monoidal category C, then there is a unique
isomorphism between ⊗(X1) and ⊗(X2) consisting of compositions of α, l, r ′s.
We call the unique isomorphism in Theorem 2.1.1 a canonical isomorphism. A monoidal
category (C, ⊗, 1, α, l, r) is sometimes written as C for simplicity.
A monoidal category C is deﬁned to be strict if all the α, l, r ′s are identity maps,
namely, the canonical isomorphism between diﬀerent representations are actually the
9
Section 2.1
Ribbon Fusion Categories
identity. Another theorem of Mac Lane shows that every monoidal category is monoidal
equivalent to a strict monoidal category. The concept of ‘monoidal equivalence ’ is deﬁned
below.
Let C1, C2 be two monoidal categories, and we use the same symbols {⊗, 1, α, l, r} for
C1, C2. A monoidal functor from C1 to C2 is a triple (F, Φ, ψ), where F : C1 −→C2 is
a functor, Φ is a natural isomorphism F ◦(· ⊗·) −→F(·) × F(·), i.e., Φ is a family of
isomorphisms {ΦA,B : F(A ⊗B) −→F(A) ⊗F(B) | A, B ∈C0}, and ψ : F(1)
≃
−→1 is
an isomorphism such that the following diagrams hold:
F((A1 ⊗A2) ⊗A3)
F(A1 ⊗A2) ⊗F(A3)
(F(A1) ⊗F(A2)) ⊗F(A3)
F(A1 ⊗(A2 ⊗A3))
F(A1) ⊗F(A2 ⊗A3)
F(A1) ⊗(F(A2) ⊗F(A3))
F(αA1,A2,A3)
ΦA1⊗A2,A3
ΦA1,A2⊗I
αF (A1),F (A2),F (A3)
ΦA1,A2⊗A3
I⊗ΦA2,A3
(2.3)
F(1 ⊗A)
F(1) ⊗F(A)
1 ⊗F(A)
F(A)
F(A)
F(lA)
Φ1,A
ψ⊗I
lF (A)
I
(2.4)
F(A ⊗1)
F(A) ⊗F(1)
F(A) ⊗1
F(A)
F(A)
F(rA)
ΦA,1
I⊗ψ
rF (A)
I
(2.5)
Roughly speaking, a monoidal functor is a functor which preserves the monoidal
structure.
Deﬁnition 2.1.2 Two monoidal categories C1, C2 are monoidal equivalent if there there
are monoidal functors F : C1 −→C2, G : C2 −→C1, such that F ◦G is equivalent to IdC2
and G ◦F is equivalent to IdC1.
Theorem 2.1.3 [44] Every monoidal category C is monoidal equivalent to a strict monoidal
10
Section 2.1
Ribbon Fusion Categories
category Cstr.
Due to Theorem 2.1.3, we can always assume monoidal categories are strict.
Example 2.1.4
1. Vect : The objects are ﬁnite dimensional vector spaces over C and
morphisms are linear maps between vector spaces. The tensor product functor ⊗is
the usual tensor product, and the unit 1 is C.
2. Given a ﬁnite group G, one can form three monoidal categories.
• VectG : The objects are G-graded vector spaces over C and morphisms are G-
graded linear maps.If V = L
g∈G
Vg, W = L
g∈G
Wg, then V N W = L
g∈G
(V ⊗W)g,
where (V ⊗W)g =
L
g=g1g2
Vg1 ⊗Wg2. The unit 1 = L
g∈G
1g, where 1g = δg,eC.
• G : The objects are members of G. For g, h ∈G, Hom(g, h) = {Ig} if g = h,
and ∅otherwise. The tensor product and unit are the multiplication and unit
in G, respectively.
• Rep(G) : Objects are left modules (representations) of G and morphisms are
G-module morphisms.
3. Rep(H) : the category of representations of a bi-algebra H. The previous example
Rep(G) is a special case corresponding to H = C[G], the group algebra.
4. Aut⊗(C) : The objects are monoidal equivalences of a monoidal category C, and
the morphisms are natural isomorphisms. The tensor product is the composition of
equivalences and the unit is IdC.
In the next few subsections, we are going to introduce some extra structures on a
monoidal category.
In the following, let C be always a monoidal category.
Whether
or not assuming C is strict depends on personal ﬂavors.
If one assumes C is strict,
11
Section 2.1
Ribbon Fusion Categories
many diagrams and equations can be simpliﬁed since the α, l, r ′s are identity maps.
By Theorem 2.1.3, there is no loss of generality for such an assumption. Thus we will
assume C is strict. But one should keep in mind that all the extra structures can be
equally deﬁned in a non-strict category and all commuting diagrams still make sense by
inserting some canonical isomorphisms involving α, l, r ′s at appropriate locations. For
instance, if bA : 1 −→A ⊗A∗, dA : A∗⊗A −→1 are two morphisms, then the following
diagram in a strict category should be replaced by Diagram 2.6 in a general category
instead.
A
A ⊗A∗⊗A
A
bA⊗I
I⊗dA
A
1 ⊗A
(A ⊗A∗) ⊗A
A ⊗(A∗⊗A)
A ⊗1
A
l−1
A
bA⊗I
αA,A∗,A
I⊗dA
rA
(2.6)
2.1.2
Rigid Monoidal Categories
Given an object A, a right dual of A is an object A∗together with two morphisms
bA : 1 −→A ⊗A∗, dA : A∗⊗A −→1 such that (IA ⊗dA) ◦(bA ⊗IA) = IA and
(dA ⊗IA∗) ◦(IA∗⊗bA) = IA∗. The left hand side of the two identities above can be
written as Diagram 2.7 and 2.8, respectively, if there is no assumption of C being strict.
A
1 ⊗A
(A ⊗A∗) ⊗A
A ⊗(A∗⊗A)
A ⊗1
A
l−1
A
bA⊗I
αA,A∗,A
I⊗dA
rA
(2.7)
12
Section 2.1
Ribbon Fusion Categories
A
f
B
a) f
A
b) IA
A
c) bA
A
d) dA
A
e) b′
A
A
f) d′
A
Figure 2.1: Pictures of some morphisms
A∗
A∗⊗1
A∗⊗(A ⊗A∗)
(A∗⊗A) ⊗A∗
1 ⊗A∗
A∗
r−1
A∗
I⊗bA
α−1
A∗,A,A∗
dA⊗I
lA∗
(2.8)
Similarly, a left dual of A is an object A
∗
with b′
A : 1 −→A
∗
⊗A, d′
A : A ⊗A
∗
−→1
such that (d′
A ⊗IA) ◦(IA ⊗b′
A) = IA and (I A
∗
⊗d′
A) ◦(b′
A ⊗I A
∗) = I A
∗.
The conditions deﬁning left and right duals will be easier to memorize with the tools
of pictorial calculus. Here we only give a minimal illustration of using pictorial calculus.
In Section 2.1.4, more details will be ﬁlled in. For a more rigorous treatment of it, see
[45] [14].
A morphism f : A −→B is represented by Figure 2.1 a). If f is the identity map, we
also represent it by Figure 2.1 b). The bA, dA, b′
A and d′
A are represented by Figure 2.1
c), d), e) and f), respectively.
Here are some rules for the representation of morphisms with pictures.
Pictures
consist of arcs and boxes. Arcs are directed as speciﬁed by an arrow, and the segments of
the arc near its ends are required to be vertically aligned. There is an object attached to
each arc. Each end of the arc represents an object. If the segment near one end is directed
downwards, then the object the end represents is the same as the one attached to the
arc; otherwise, it is the the right dual or the left dual. At this point it is not clear which
dual it should be unless we specify it. Later on when more structures are introduced, e.g.
13
Section 2.1
Ribbon Fusion Categories
A
=
A
A
=
A
Figure 2.2: Identities of a right dual
A
=
A
A
=
A
Figure 2.3: Identities of a left dual
pivotal structure, the left dual will be the same as the right dual and thus the ambiguity
will be gone. Composition of two morphisms corresponds to stacking one on top of the
other; tensor products corresponds to juxtaposition. With these conventions, the two
identities deﬁning a right dual are illustrated by pictures in Figure 2.2, and the identities
deﬁning a left dual in Figure 2.3.
The following lemma shows that if a right dual exists, then it is unique up to a unique
isomorphism. In the same way one can also show the left dual is also unique.
Lemma 2.1.5 [41] If (A∗, bA, dA), ( ˜A∗,˜bA, ˜dA) are both right duals of A, then there exists
a unique isomorphism φ : A∗−→˜A∗, such that ˜bA = (I ⊗φ)◦bA and ˜dA = dA ◦(φ−1 ⊗I).
Deﬁnition 2.1.6 A rigid monoidal category is a monoidal category such that there exists
a right dual and a left dual for each object.
In a rigid monoidal category, one can deﬁne the right (resp. left) dual of a morphism.
For f ∈Hom(A, B), the right dual f ∗∈Hom(B∗⊗A∗) is deﬁned as (dB ⊗I)(I ⊗f ⊗
I) ◦(I ⊗bA), or pictorially as Figure 2.4. Similarly, the left dual f
∗
∈Hom( B
∗
, A
∗) is
deﬁned as (I ⊗d′
B) ◦(I ⊗f ⊗I) ◦(b′
A ⊗I), or pictorially as Figure 2.4.
14
Section 2.1
Ribbon Fusion Categories
A
f
B
A
f
B
Figure 2.4: f∗(Left) and f
∗
(Right)
Proposition 2.1.7 The assignment A 7−→A∗, f 7−→f ∗deﬁnes a monoidal functor
(·)∗: C −→Cop,rev. Similarly, (·)
∗
: C −→Cop,rev sending A to A
∗
and f to f
∗
is also a
monoidal functor.
Since (Cop,rev)op,rev = C, (·)∗∗and
(·)
∗∗
are both monoidal functors from C to itself.
2.1.3
Fusion Categories
An abelian category is C-linear if the morphism spaces are vector spaces over C and
compositions of morphisms are C-bilinear. A functor from a C-linear abelian category
to a C-linear abelian category is C-linear if it is a C-linear map restricted on morphism
spaces. All functors on between C-linear abelian categories are assumed to be C-linear.
An object A in a C-linear abelian category is simple if Hom(A, A) ≃C. It can be
shown that if A, B are simple objects that are not isomorphic, then Hom(A, B) = 0. An
abelian category is semi-simple if every object is isomorphic to a direct sum of simple
objects.
If C is semi-simple, denote by L(C) the set of isomorphism classes of simple objects.
Deﬁnition 2.1.8 A fusion category is a semi-simple C-linear rigid monoidal category C
such that 1 is simple and L(C) is ﬁnite.
15
Section 2.1
Ribbon Fusion Categories
2.1.4
Pivotal and Spherical Categories
Let C be a rigid monoidal category. A pivotal structure on C is a natural isomorphism
δ : IdC −→(·)∗∗, namely, for each object A, there is an isomorphism δA : A −→A∗∗,
such that
1. δA⊗B = δA ⊗δB;
2. δ∗
A = δ−1
A∗;
3. δ1 = I1.
Deﬁnition 2.1.9 A pivotal category is a rigid monoidal category with a pivotal structure.
In a pivotal category C, the left dual can be deﬁned in terms of the right dual. Speciﬁcally,
given an object A and its right dual A∗with bA, dA, one can deﬁne b′
A := (I ⊗δ−1
A ) ◦
bA∗, d′
A = dA∗◦(δA ⊗I). It is straight forward to check that (A∗, b′
A, d′
A) satisﬁes the
conditions of a left dual. Thus as an object, the left dual and the right dual are the
same, and in the following we will simply call the dual of an object.
If C is a C-linear pivotal category with 1 simple, we can deﬁne the concept of left
trace and right trace of a morphism. Since Hom(1, 1) ≃C, one can ﬁx an isomorphism
sending I1 to 1 ∈C. Thus every morphism in Hom(1, 1) can be identiﬁed with a scalar
in C.
For f ∈Hom(A, A), deﬁne left trace Trl(f) := dA ◦(I ⊗f) ◦b′
A and the right trace
Trr(f) := d′
A ◦(f ⊗I) ◦bA. Pictorially, these traces are illustrated in Figure 2.5.
The following properties on the left traces explains the notion of a ‘trace ’. The same
properties also hold for right traces.
Proposition 2.1.10
1. Trl(·) is a linear functional on Hom(A, A).
2. Trl(f ◦g) = Trl(g ◦f) for f ∈Hom(A, B), g ∈Hom(A, A).
16
Section 2.1
Ribbon Fusion Categories
A
f
A
A
f
A
Figure 2.5: Trl(f) (Left) and Trr(f) (Right)
3. Trl(f ⊗g) = Trl(f) Trl(g) for f ∈Hom(A, A), g ∈Hom(B, B).
4. Trl(I1) = 1.
Deﬁnition 2.1.11
1. A C-linear pivotal category with 1 simple is spherical if Trl =
Trr.
2. A spherical category C is strict if it is strict as a monoidal category and the pivotal
structure is the identity natural isomorphism, namely, IdC = (·)∗∗.
Thus in a spherical category, we simple use the notion ‘the trace of f ’, and the
notation Tr(f) for either the left trace or the right trace. By [46], every spherical category
is equivalent to a strict spherical category. Therefore, we will assume spherical categories
are strict.
In a spherical category, one can use the trace operator to deﬁne a bilinear pairing.
Explicitly, deﬁne ⟨, ⟩: Hom(A, B) × Hom(B, A) −→C by ⟨f, g⟩= Tr(f ◦g).
Deﬁnition 2.1.12 A spherical category is non-degenerate if the pairing ⟨, ⟩is non-
degenerate for all A, B.
Proposition 2.1.13 Spherical fusion categories are non-degenerate.
Deﬁnition 2.1.14
1. The quantum dimension dA of an object A is dA = Tr(IA).
17
Section 2.1
Ribbon Fusion Categories
2. If C is a spherical fusion category, the total quantum dimension D of C is the
positive square root of D2 :=
P
a∈L(C)
d2
a. The notion ‘positive square root ’ makes
sense by Lemma 2.1.15 below.
Lemma 2.1.15 [42] If C is a spherical fusion category, then dA = dA∗and dA is real.
Note that we have used the same symbol dA for the morphism dA : A∗⊗A −→1 and
the quantum dimension of A, but in most cases it will be clear which quantity we mean
by dA, and otherwise we will point it out explicitly.
If C is a spherical fusion category, then for a, b ∈L(C), we have
a ⊗b =
M
c∈L(C)
N c
ab c.
(2.9)
The N c
ab
′s are non-negative integers, called fusion rules. A category is multiplicity free
if N c
ab is either 0 or 1. Denote by ¯a the dual a∗. The following properties hold.
N b
1a = N b
a1 = δa,b, N c
ab = N
¯b
¯ca = N ¯a
b¯c = N ¯c
¯b¯a
At the end of this subsection, we give a brief introduction on pictorial calculus in a
(strict) spherical category. See [14] for more detailed discussions.
We ﬁrst deﬁne pictures in the plane R2 with the standard orientation. A picture
in R2 is a union of rectangles and directed arcs (open or closed) restricted in R × [0, 1]
subjected to the following conditions:
1. All rectangles are disjoint and all arcs are disjoint. The interior of any arc is disjoint
with any rectangle. The end points of an arc are either on R × {0, 1} or on the
bottom or the top edge of a rectangle. Arcs intersect with R×{0, 1} or a rectangle
transversally.
18
Section 2.1
Ribbon Fusion Categories
A1
· · ·
Am
B1
· · ·
Bn
f
C1
· · ·
Ck
R × {0}
D1
· · ·
Dl
R × {1}
Figure 2.6: A local picture near a rectangle (Left), R × {0} (Middle), R × {1} (Right)
2. Each arc is labelled with an object.
Each rectangle is labelled by a morphism
f : A −→B where the description of f is as follows.
Let the picture around
the rectangle be as shown in Figure 2.6, then A = Aϵ1
1 ⊗· · · ⊗Aϵm
m and B =
Bβ1
1 ⊗· · · ⊗Bβn
n , where ϵi = 1 if the arc labelled by Ai is directed downwards near
the rectangle and ϵ = −1 if it is directed upwards, βj is deﬁned in the same way
depending on the direction of the arc labelled by Bj, and for an object C, C+1 is
C and C−1 is C∗.
Given a picture R, let R be as in Figure 2.6 (Middle) and Figure 2.6 (Right) near
the intersections of R with R × {0} and with R × {1}, respectively. Then deﬁne S(R) =
Cϵ1
1 ⊗· · · ⊗Cϵk
k and T(R) = Dβ1
1 ⊗· · · ⊗Dβl
l , where ϵi and βj are deﬁned in the same
way as above. A picture R can be interpreted as a morphism from S(R) to T(R) by the
following rules.
Interpret the pictures in Figure 2.1 as the morphism below them.
If R1, R2 are
disjoint and put side by side, then R1 ⊔R2 is the tensor product of R1 and R2. If R1, R2
are two pictures such as T(R1) = S(R2), then we can glue R2 on top of R1 along their
common end points and compress the resulting graph to within R×[0, 1]. The morphism
represented by the glued picture is the composition of R1 followed by R2, i.e., R2 ◦R1.
By the above rules, any picture can be interpreted as a morphism which is a composi-
tion of morphisms, each of which is a tensor product of some morphisms from Figure 2.1.
By [14], the morphism thus obtained is well-deﬁned, and if there is an isotopy mapping
one picture to another picture and preserving the labels of arcs, then the two pictures
19
Section 2.1
Ribbon Fusion Categories
represent the same morphism.
Proposition 2.1.16 [14] If C is a spherical category, then
1. If the direction of an arc is reversed and the label attached to that arc is changed
to its dual, then the new picture represents the same morphism as the old picture.
2. Let S2 = R2⊔{∞} be the oriented sphere and naturally embed R2 into S2. If R1, R2
are pictures in R2 that are isotopic in S2, then they represent the same morphism.
2.1.5
Braided Monoidal (Tensor) Categories
A braided monoidal (tensor) category is a monoidal category C, together with a
natural isomorphism c : ⊗−→⊗◦Swap, where Swap is the functor which swaps the
two components of C × C, such that Diagram 2.10 and 2.11 commute. For A, B ∈C0,
denote by cA,B the natural isomorphism, namely,
cA,B : A ⊗B −→B ⊗A.
(A ⊗B) ⊗C
(B ⊗A) ⊗C
A ⊗(B ⊗C)
B ⊗(A ⊗C)
(B ⊗C) ⊗A
B ⊗(C ⊗A)
cA,B⊗I
αA,B,C
αB,A,C
cA,B⊗C
I⊗cA,C
αB,C,A
(2.10)
20
Section 2.1
Ribbon Fusion Categories
B
B
A
A
B
B
A
A
Figure 2.7: cA,B (Left) and c−1
A,B (Right)
B
B
A
A
B
B
A
A
isotopy
=
A
B
Figure 2.8: c−1
A,B ◦cA,B = IA⊗B
(A ⊗B) ⊗C
(B ⊗A) ⊗C
A ⊗(B ⊗C)
B ⊗(A ⊗C)
(B ⊗C) ⊗A
B ⊗(C ⊗A)
c−1
B,A⊗I
αA,B,C
αB,A,C
c−1
B⊗C,A
I⊗c−1
C,A
αB,C,A
(2.11)
The morphisms cA,B and c−1
A,B are represented by the pictures in Figure 2.7 (Left) and
(Right), respectively.
Thus IA⊗B = c−1
A,B ◦cA,B corresponds to the picture of the LHS of Figure 2.8, which
is isotopic to the RHS representing the identity morphism.
With this convention, Diagram 2.10 and 2.11 can be represented as equalities of
pictures shown in Figure 2.9 (Left) and (Right), respectively.
A spherical braided category is called a ribbon category. The picture calculus can
be extend from spherical categories to ribbon categories by adding the convention that
the braiding and its inverse shown in Figure 2.7. Then two pictures represent the same
morphism in a ribbon category if and only if they are related by a regular isotopy.
21
Section 2.1
Ribbon Fusion Categories
B
C
A
=
B
A
C
A
B
C
=
A
B
C
Figure 2.9: Equalities of the braiding
A
Figure 2.10: The twist θA
Let C be a ribbon category, and deﬁne θA : A −→A, called the twist, to be the
isomorphism represented by the picture in Figure 2.10. Note that this picture is not
regular isotopic to a vertical line representing the identity map in the plane.
The following proposition is a summary on properties of the twist.
Proposition 2.1.17 The twist θ(·) deﬁned for each object is a natural isomorphism
IdC −→IdC that satisﬁes the following properties.
1. θA⊗B = (θA ⊗θB) ◦cB,A ◦cA,B;
2. θA∗= (θA)∗;
3. θ1 = I.
22
Section 2.2
