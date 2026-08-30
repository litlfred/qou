---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-009-41-the-basics-diagrammatic-categories-additive-c
section_title: "The basics: diagrammatic categories, additive closures and Karoubi envelopes"
section_number: 4.1
pages: 31-48
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
sider diagrammatic categories in the following. We encourage the reader to take a look in the
rather extensive literature (in the authors opinion, a good start is [37, Section 2]). Although these
categories have a natural 2-categorical structure, we phrase everything in terms of 1-categories.
Furthermore, we note that we only use Q(q)-linear categories. Recall that a category C is called
Q(q)-linear if each hom-space HomC(O, O′) for O, O′ ∈ Ob(C) has the structure of a Q(q)-vector
space and the composition of morphisms is Q(q)-bilinear (this includes the existence of a zero
morphism 0). We use Q(q)-linear functors for such categories: functors which induce Q(q)-linear
maps on each hom-space. We, as in Subsection 3.5, only consider (Z-)graded categories.
Deﬁnition 4.1. (Additive closure of C) Given a Q(q)-linear category C, we deﬁne its additive
closure, denoted by Mat(C), to be the Q(q)-linear category consisting of the following.
11The parameter q in the notation of Bernstein-Frenkel-Khovanov comes from the grading.
31
• The objects are ﬁnite (possibly empty), formal direct sums ⊕N
i=1Oi with Oi ∈ Ob(C) (note
that the empty object is the zero object).
• Given two objects O = ⊕N
k=1Ok, O ′ = ⊕N ′
k=1O′
k, then a morphism F ∈ HomMat(C)(O, O′)
is a N × N ′ matrix F = (fi′i) consisting of morphisms fi′i ∈ HomC(Oi, O′
i′).
• One can add the matrices component-wise and scalar multipli cation with elements from
Q(q) is also component-wise.
• Composition of morphisms is multiplication of matrices. ▲
It is easy to check that this deﬁnition gives a category.
Deﬁnition 4.2. (Karoubi envelope of C) Let C be a category and A ∈ Ob(C) be an object of
C. Let e, e′ : O → O denote idempotents in EndC(O). The Karoubi envelope of C, denoted by
Kar(C), is the following category.
• Objects are ordered pairs(O, e) consisting of an objectO and an idempotent e ∈ EndC(O).
• Morphisms f : ( O, e) → (O′, e′) in Kar(C) are all morphisms f : O → O′ of C such that
the equations f = f ◦ e = e′ ◦ f hold.
• Compositions are induced by compositions in C. ▲
Again, it is immediate that this is indeed a category.
The identity on (O, e) is e itself. Moreover, there is a faithful functor im : C → Kar(C), called
the image, that sends A to (O, id) and f : O → O′ to f : ( O, id) → (O′, id). Categories C such that
C ∼
= Kar(C) are called idempotent complete.
We point out that Mat(C) is “combinatorial the same” as C – in contrast to Kar(C) which is
usually very hard to describe combinatorially/diagrammatically.
4.2. The dihedral cathedral D(∞). For the reader familiar with [18]: be careful that Elias’ “root
of unity case” does not correspond to our root of unity case from Section 2. Moreover, we slightly
rescale his “barbell forcing relation”, see BF2 (20).
Following [18], we encode the two different generators of Wl = ⟨s, t⟩ using two colors. Our
convention, that is different from the one used by Elias, is that s is displayed in red and t in green.
The “third color” is for 1 ∈ Wl which is displayed as white colored or empty.
Deﬁnition 4.3. (Soergel graph) A pre-Soergel graph ˜G is a colored, planar graph embedded in
[0, 1] × [0, 1] whose bottom (or source) boundary is in [0, 1] × { 0} and whose top (or target)
boundary is in [0, 1] × {1}. The only vertices are univalent (called dots) or trivalent. The edges
of a Soergel graph are colored by red (or r) and green (or g) such that at each trivalent vertex all
adjacent edges have the same color. We display dots and trivalent vertices locally as
Dots:
l(·) = 1
or
l(·) = 1
Trivalent vertices:
l(·) = −1
or
l(·) = −1
where we tend (as above) not to display the r and g. Moreover, the illustration above is locally
and Soergel graphs also include for example horizontal reﬂe ctions of the ones above. In addition,
given a pre-Soergel graph ˜G, we deﬁne its degree l( ˜G) to be the sum of the local degrees as above.
A Soergel graph G is an equivalence class of pre-Soergel graphs modulo bounda ry preserving
isotopies of colored, planar graphs (which are all locally o f the forms as in (21)). Note that the
degree is still well-deﬁned for a Soergel graph and we denote it by l(G). The empty diagram 0 is
also a Soergel graph and of degree l(0) = 0 .
32
Each Soergel graph gives rise to a bottom sequence b(G) = bi . . . b2b1 and a top sequence
t(G) = ti′ . . . t2t1 of colors bk, tk ∈ { r, g} by reading the colors at the bottom or top boundary
from right to left respectively. We also allow the empty sequence, if the bound ary is empty (at
bottom or top). We call a Soergel graph (or a local piece of it) ﬂoating, if both boundaries are
empty. We call ﬂoating Soergel graphs consisting of only one edge barbells. ▲
Our reading conventions are thus fromright to left (we think of the pictures as applying functors
to a module) andbottom to top. Moreover, we think of Soergel graphs as embedded into a rectangle
(although we never illustrate the rectangle), and thus, it make sense to speak aboutfaces of Soergel
graphs. Each Soergel graph has a unique rightmost face Fr and a unique leftmost face Fl.
Example 4.4. An example of two representatives of a Soergel graph G are
r r r g g r
r g r g r r
Fl Fr =
r r r g g r
r g r g r r
Fl Fr
Here l(G) = 4 , b(G) = rrrggr and t(G) = rgrgrr . The graph above has one (green) barbell. We
have marked the unique right- and leftmost faces with Fr and Fl respectively. ▲
Note that, since G completely determines b(G) and t(G), we do not display these anymore.
Deﬁnition 4.5. (Elias’ dihedral cathedralD(∞)) We consider theQ(q)-linear, graded, monoidal
category called the free dihedral cathedral, denote by D(∞)f, consisting of the following.
• Objects Ob(D(∞)f ) are ﬁnite sequences x = xi . . . x2x1 with xi ∈ {r, g}. Moreover, the
empty sequence ∅ is also an object.
• The space of morphisms HomD(∞)f (x, x′) for x, x′ ∈ Ob(D(∞)f ) is the Q(q)-linear span
of all Soergel graphs G with b(G) = x and t(G) = x′.
• Composition (vertical) of morphisms G′ ◦v G is deﬁned by glueing G′ on top of G.
• The monoidal product (horizontal) ◦h is, for x = xi . . . x2x1 and x′ = x′
i′ . . . x′
2x′
1, given
by concatenation x′ ◦h x = x′x, and for G′ ◦h G via placing G′ to the left of G.
• The spaces HomD(∞)f (x, x′) are graded Q(q)-vector spaces where the degree of a Soergel
graph G is given by l(G).
The category D(∞) is the quotient category of D(∞)f obtained by taking the quotient by the
following local relations and their color-inverted (red⇆green) counterparts.
The two Frobenius relations:
(18) Frob1 :
= , Frob2 : = =
The needle relation:
(19) Needle : = 0
33
The barbell forcing relations:
(20) BF1 : = 2 · − , BF2 : = + 2 · − 2 ·
Note that the isotopy invariance can be locally displayed via the isotopy relations:
(21) Iso1 : = = , Iso2 : = =
together with a horizontal reﬂection of the two relations.
We also note that all relations are homogeneous with respect to l(G) and thus, D(∞) inherits
the grading from D(∞)f. The monoidal product ◦h also carries over toD(∞) without difﬁculties.
Moreover, we use the following convention: we call elements of HomD(∞)f (x, x′) Soergel
graphs and, on the other hand, elements of HomD(∞)(x, x′) Soergel diagrams (for all possible
x, x′ ∈ Ob(D(∞)f ) = Ob( D(∞))). We call a face of a Soergel diagram empty if it has no
internal ﬂoating Soergel diagrams (as for example barbells). ▲
Example 4.6. An example of two representatives of Soergel diagrams are
= 2 · −
Here we used the left (green) barbell forcing relation (20) on the marked piece. ▲
Lemma 4.7. A Soergel diagram G with an internal cycle which bounds an empty face is zero. □
Proof. Use repeatedly the ﬁrst Frobenius relations (18) as illustr ated below (note that each step
reduces the number of adjacent edges of the face and we have in dicated where to use the ﬁrst
Frobenius relation Frob1 (18) in the last step)
· · ·
Frob1
=
Frob1
=
Frob1
=
Frob1
=
Needle
= 0
until we can use the needle relation (19) to see that we get zero. ■
A tree is a connected Soergel graph G with no cycles. We call a Soergel diagram reduced if all
of its connected components are trees or barbells and all barbells are in the rightmost face.
The following is [18, Proposition 5.19] converted to our conventions.
Proposition 4.8. Each Soergel diagram can be written as a Q(q)-linear sum of reduced Soergel
diagrams. Thus, reduced Soergel diagrams form spanning sets of the hom-spaces of D(∞). □
34
Proof. Note that it follows from a repeated application of the Frobe nius relations (18) that all
ﬂoating trees are barbells and, by combining Lemma 4.7 with BF1 and BF2 (20), all other ﬂoating
Soergel diagrams are Q(q)-linear combinations of barbells.
Thus, we can restrict to Soergel diagrams whose only ﬂoating components are barbells.
Now, given a Soergel diagramG, we can ﬁrst useBF1 and BF2 (20) to express G as a direct sum
of Soergel diagrams Gi (with i = 1, . . . , k) with only barbells in the rightmost face. By Lemma 4.7
all Soergel diagrams Gi with an internal cycle are zero now. ■
We point out the following corollary. This can be compared to [18, Corollary 5.20] and the
corresponding statement, in our case for Tgr, will later be completely different, see Lemma 4.18.
For this purpose, denote by Q(q)[br, bg] the graded Q(q)-algebras of polynomials in br, bg, with the
generators br, bg being of degree 2.
Corollary 4.9. We have Q(q)[br, bg] ∼
= EndD(∞)(∅) as graded Q(q)-algebras. □
Proof. By Proposition 4.8 the map that sends br ↦→“red barbell” and bg ↦→“green barbell” is an
isomorphism of graded Q(q)-algebras. To see this note that a bunch of barbells do not sat isfy any
extra relations (the barbell forcing relations (20) do not give anything new). ■
Lemma 4.10. Soergel diagrams satisfy= 1
2 · + 1
2 · and = 1
2 · + 1
2 ·
□
Proof. Use Frob1 (18) on the right side followed by BF1 (20) for the middle edge. ■
This implies the useful fact that we can focus on alternating sequences (the case where the
sequence is a reduced word in D(∞)) of red and green if we go to Mat(D(∞)) (where we use ◦
for the matrix multiplication).
Lemma 4.11. We have
rr ∼
= r⟨−1⟩ ⊕ r⟨+1⟩ and gg ∼= g⟨−1⟩ ⊕ g⟨+1⟩.
which are isomorphisms in Mat(D(∞)). □
Proof. The isomorphism for the red case is induced by
rr






1 ·
1
2 ·






/d47/d47 r⟨−1⟩ ⊕ r⟨+1⟩
(
1
2 · 1 ·
)
/d47/d47 rr,
where we check (with Lemma 4.10 for “right ◦left” and Lemma 4.7 together with BF1 (20) for
“left◦right”) that the two matrices above are inverses. The green case works analogous. ■
Deﬁnition 4.12. (Jones-Wenzl projectors) Denote by xk−tst a sequence xk . . . x2x1 of length k
that alternates in the colors red and green and starts with x1 = g (thus, ends in r iff k is even).
We deﬁne for each i ≥ 0 the i-th green Jones Wenzl projector JWg
i recursively as the element
of EndD(∞)(xi−tst) obtained via the convention that JWg
0 is 0 : ∅ → ∅ , JWg
1 is id : g → g, JWg
2 is
35
id : rg → rg and recursion rule for i > 2 given by
. . .
. . .
JWg
i =
. . .
. . .
JWg
i−1 − i − 2
i − 1 ·
. . .
. . .
. . .
. . .
JWg
i−3
JWg
i−1
JWg
i−1
Here we have only illustrated the case for odd i. Similar for even i and red projectors JWr
i . ▲
Example 4.13. The ﬁrst four (green) Jones-Wenzl projectors are
JWg
0 = 0, JWg
1 =
, JWg
2 =
, JWg
3 =
− 1
2
as follows by an easy calculation. ▲
For each i′ > 2 we call a diagram of the form
a green alternating i′-pitchfork (here i′ = 7 ). We denote it by P g
i′ and similarly for P r
i′, which
is the i′-th red alternating pitchfork . We note that b(P g
i′ ) as well as b(P r
i′) consist of i′ elements.
Moreover, we write Di(P g
i′ ) for a bigger diagram with i ≥ i′ > 2 which somewhere at the bottom
has a green alternating pitchfork, i.e.
(22) Di(P g
i′ ) = D ◦ (idx P g
i′ idx′)
for some sequences x, x′ and some diagram D. Similarly for red again.
Lemma 4.14. Let i ≥ i′ > 2. Then Di(P g
i′ ) ◦ JWg
i = 0. Similarly for red. □
Proof. This follows recursively. To see the ﬁrst step i = i′ = 3 , we compose P g
3 with the second
term of JWg
3 from Example 4.13 and obtain by using BF2 (20) and Lemma 4.7 for the ﬁrst step
and Frob2 (18) for the second:
−1
2 · = −1
2 · 2 · = −
giving minus the composition of P g
3 with the ﬁrst term of JWg
3. Thus, D3(P g
3 ) ◦ JWg
3 = 0.
36
Now we use induction on i and ﬁx i′ = 3 . If i > 3 and Di(P g
3 ) has x ⁄= ∅ (see (22)), then the
recursion rule from Deﬁnition 4.12 (the 3-pitchfork is on top of the smaller box that corresponds
to the i − 1-th Jones-Wenzl projector) shows by induction that we get zero. If, on the other hand,
x = ∅, then we can use a similar argument as above. Hence, we always have Di(P g
3 ) ◦ JWg
i = 0.
But the case i′ = 3 sufﬁces as the following illustrates.
= 1
2 · + 1
2 ·
Here we used Frob2 (18) “backwards” on a bigger alternating pitchfork followe d by BF1 (20).
We see now two smaller pitchforks and thus, the case i′ = 3 sufﬁces to verify the lemma. ■
Lemma 4.14 holds, mutatis mutandis, by attaching horizonta lly reﬂected pitchforks form the
bottom as well. Moreover, it is easy to deduce that the Jones- Wenzl projectors are (degree zero)
idempotents of xi−tst and xi−sts, respectively. We associate these to the corresponding alternating
sequences. Furthermore, by Lemma 4.11, we can, by going to Mat(D(∞)), associate to each
x ∈ Ob(D(∞)) a (shifted) direct sum of Jones-Wenzl projectors. We denotethis sum that consists
of these projectors for x by JWx. This motivates the following category.
Deﬁnition 4.15. Denote by Mat( ˆD(∞)) the full subcategory of Kar(Mat(D(∞))) generated
by im(JWx) for all x ∈ Ob(D(∞)). ▲
Diagrammatically Mat( ˆD(∞)) is given similarly to Mat(D(∞)), but has some extra rela-
tions. For example, Lemma 4.14 says that, whenever we see a pi tchfork at the bottom (or its
reﬂection at the top) boundary, then the corresponding Soergel diagram is zero.
4.3. The quotient QD(∞). We are now able to deﬁne the category whose combinatorics and
diagrammatic govern the tilting category Tgr. We call it for short the quotient.
Deﬁnition 4.16. (The quotient ) We denote by QD(∞)f the Q(q)-linear full subcategory of
D(∞), called “free quotient”, consisting of the following.
• Objects Ob(QD(∞)f ) are ﬁnite sequences x = xi . . . x2x1 with xk ∈ { r, g}. Moreover,
the empty sequence ∅ is also an object.
• The hom-space HomQD(∞)f (x, x′) for x, x′ ∈ Ob(QD(∞)f ) is the Q(q)-linear span of
all Soergel graphs G with b(G) = x and t(G) = x′ whose rightmost face is marked with
the dead-end symbol.
• Composition G′ ◦v G is deﬁned by glueing G′ on top of G. The dead-end symbol is just
a marker and behaves as an idempotent under composition and can not be moved from the
rightmost face.
• The morphisms in HomQD(∞)f (x, x′) satisfy the relations of the corresponding morphisms
(without the dead-end marker) is HomD(∞)(x, x′) given in Deﬁnition 4.5.
• The spaces HomQD(∞)f (x, x′) are graded Q(q)-vector spaces with degree given by l(G).
The quotient QD(∞) is the quotient of QD(∞)f by the following extra relations which we
call the dead-end relations:
(23) DE1 : = 0, DE2 : = 0
37
We stress that we do not allow the color inverted counterpart s of (23). All relations are homo-
geneous with respect to l(G) and thus, QD(∞) inherits the grading from D(∞). We call the
morphisms in QD(∞) marked Soergel diagrams. ▲
Example 4.17. An example of a Soergel diagram that is zero as a marked Soergel diagrams is
= 2 · − = 0
Here the middle diagrams is zero due to DE2 and the right-hand due to DE1. ▲
Let reduced, marked Soergel diagrams be the evident analogues of reduced Soergel diagrams.
Lemma 4.18. Each marked Soergel diagram can be written as a Q(q)-linear sum of marked, re-
duced Soergel diagrams. Thus, marked, reduced Soergel diagrams without barbells form spanning
sets of the hom-spaces of QD(∞). The right action of EndD(∞)(∅) by placing barbells in the
rightmost face is the trivial action. □
Proof. Use repeatedly BF1 and BF2 (20) to shift all existing barbells to the rightmost region.Then
use the two dead-end relations DE1 and DE2 (23) to see that only terms without barbells are not
killed. The remaining diagrams are reduced by Proposition 4.8. ■
Note that, as a consequence of Lemma 4.18, a marked, reduced S oergel diagram does not have
any ﬂoating components anymore.
Deﬁnition 4.19. Denote by Mat( ˆQD(∞)) the full subcategory of Kar(Mat(QD(∞))) gener-
ated by im(JWx) for all x ∈ Ob(QD(∞)). ▲
Thus, by using Lemma 4.11 andDE1 (23), we usually can focus on alternating sequencesx that
start with g in the following.
Given a marked, reduced Soergel diagram G, we call two edges E1, E2 face sharing , if E1
and E2 are adjacent to some common face. Marked, reduced Soergel di agrams G (with color
alternating boundary) with face sharing edges of the same color come in four types, where we, by
Lemma 4.14, ignore diagrams with pitchforks. The ﬁrst two types are
(24) Type 1 :
...
...
...
...
...
/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
k≥1
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownrightk′≥1
, Type 2 :
...
...
...
...
...
/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
k≥2
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownrightk′≥2
where the dots · · · mean an arbitrary (possible empty) diagram in between and wedo not require
the picture to by symmetric. Moreover, k, k′ are odd in Type 1 and even in Type 2. We should
note that only the ﬁrst edge has to be green, but we allow possible color inversion of the rest of the
38
picture (that is, after the rightmost dots). The other two types are
(25) Type 3 :
... ...
...
... ...
/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
k≥2
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownrightk′≥0
, Type 4 :
...
...
The difference between the types 1,2 and 3,4 is that 1,2 have face sharing edges for a non-extremal
face, while 3,4 have face sharing edges for the leftmost face . We note that Type 3 should also
include the horizontal reﬂection (ﬁxing the dead-end symbol) of the ﬁrst diagram in (25).
Lemma 4.20. If a marked, reduced Soergel diagram G ∈ HomMat(ˆQD(∞))(x, x′) has two face
sharing edges of one of the three types 1,2 or 3, then it is zero. □
Proof. A case-by-case check. We assume that there is at least one such face.
Type 1. This follows via
...
...
...
...
... = 1
2 ·
...
...
...
...
...
pitchfork
+ 1
2 ·
...
...
...
...
...
pitchfork
That both diagrams are zero follows from Lemma 4.14 (recalling that we have restricted ourself to
alternating sequences of colors), since the marked faces above are, by (18), pitchforks.
Type 2. This follows similarly to Type 3 below.
Type 3. Note that the number of bottom edges at the end does not matte r and we thus, by
simplicity, assume that there are none of these. In addition , we only illustrate the case with two
dotted edges at the top since all the others will be similar. A nd, without loss of generality, we
assume that this is the only face with adjacent edges of the same color.
We proceed by induction on j, where j > 0 is the minimal number of cuts that a line drawn
from the rightmost face to the face in question needs. The case j = 1 can be deduced via
= = 1
2 · + 1
2 ·
Note that the rightmost diagram is zero by Lemma 4.14. Thus, we continue as
1
2 · = −1
2 · + = = 0
39
where the last diagram is zero due to DE1 (23).
This shows that our starting diagram was already zero. The in duction j > 1 works now in a
similar fashion where we perform the same sequence of moves u ntil we are in a situation as the
last step above. Then we can use induction, since we have crea ted a face with edges of the same
color, but “closer” to the rightmost face. This ﬁnishes the proof. ■
Corollary 4.21. Let i, i′ ∈ Z≥0. Then we have the following for i, i′ ⁄= 0.
HomMat(ˆQD(∞))(xi−tst, xi′−tst) ∼=









Q(q)i ⊕ Q(q)εi, if |i − i′| = 0,
Q(q)ui, if i′ − i = 1,
Q(q)di, if i − i′ = 1,
0, if |i − i′| > 1,
with diagrams for i = 1, 2, . . . (and possible color inverted left sides)
i =
...
...
xi xi−1 x1
xi xi−1 x1
, ε i = 1
2i ·
...
...
xi xi−1 x1
xi xi−1 x1
, u i−1 =
...
...
xi−1 x1
xi xi−1 x1
, d i = 1
2i ·
...
...
xi xi−1 x1
xi−1 x1
of degree l(i) = 0 , l(ui) = l(di) = 1 and l(εi) = 2 . In addition, HomMat(ˆQD(∞))(∅, ∅) is one
dimensional and spanned by the empty diagram 0 of degree l(0) = 0 . □
Proof. A case-by-case check using Lemma 4.20. That HomMat(ˆQD(∞))(∅, ∅) ∼= Q(q)0 follows
from DE1 and DE2 (23) since no ﬂoating diagrams can exist.
If |i − i′| > 1, then each Soergel diagram has a pitchfork or is of Type 3 (25). Both are zero
by Lemmas 4.14 and 4.20. If |i − i′| = 1, then, by Lemma 4.20 again, only diagrams of the form
ui or di as above can be non-zero and these are clearly non-zero. If |i − i′| = 0 , then, again by
Lemma 4.20, only diagrams of the form i or εi as above can be non-zero (which they clearly are).
All these diagrams are linearly independent for degree reasons. ■
Remark 4.22. Let C be a category given by generators and relations. Usually it is very hard to see
“by hand” that the calculus provided by C does not collapse. A way to show that this is not the
case is to represent C on a category “under control”, e.g. on module categories.
We formally have to do the same to see that the four maps from above are indeed non-zero. What
we use in our case is Lemma 4.26 which identiﬁes the four maps with the evident Uq-intertwiners
(we point out that we do not need Corollary 4.21 to prove Lemma 4.26). ▲
Proposition 4.23. We have
ui ◦ ui−1 = 0 = di ◦ di+1, i = 1, 2, . . . , d i+1 ◦ ui = εi = ui−1 ◦ di, i = 1, 2, . . .
d1 ◦ u0 = 0,
where we use the notation from Corollary 4.21. □
40
Proof. The relation d1 ◦ u0 is DE2 (23). For ui ◦ ui−1 = 0 the corresponding diagrams are
...
...
◦
...
...
=
...
...
= 0
The relation di ◦ di+1 = 0 follows similar and ui−1 ◦ di = εi can be veriﬁed directly as
...
...
◦ 1
2i ·
...
...
= 1
2i ·
...
...
while di+1 ◦ ui = εi follows via
1
2i+1 ·
...
...
◦
...
...
= 1
2i+1 ·
...
...
= 1
2i ·
...
...
where we use BF2 (20) together with Lemma 4.20 to see that the only surviving t erm is the “bro-
ken” one from BF2 (20). This ﬁnishes the proof. ■
4.4. QD(∞) and the tilting category Tgr. Given a sequence x ∈ Ob(QD(∞)) of the form
xi . . . x2x1 with xk ∈ { r, g} we denote by ˜ℓ(x) the number of color changes (including the ﬁrst
from empty to green), e.g. ˜ℓ(g) = ˜ℓ(gg) = 1 , ˜ℓ(ggrgrgrr ) = 6 and ℓ(x) = ˜ℓ(x) iff x is alternating.
Deﬁnition 4.24. (Diagrammatic presentation) Deﬁne a Q(q)-linear functor
D∞ : Mat( ˆQD(∞)) → Tgr
λ
of graded categories by the following convention.
On objects (we treat degree shifted objects in the evident way):
• Send the empty sequence ∅ to Tq(0). If x ∈ Ob(QD(∞)) is of the form xi . . . x2x1 with
xk ∈ {r, g}, then deﬁne
D∞(x) = pTq(λ˜ℓ(x)) ◦ Θ xi ◦ · · · ◦ Θ x2 ◦ Θ x1Tq(0),
where we use the convention r = s, g = t and pTq(λ˜ℓ(x)) projects to the Tq(λ˜ℓ(x)) part.
• Send a general x ∈ Ob(Mat( ˆQD(∞))) to the direct sum of the images of its components.
All marked Soergel diagrams are compositions of diagrams of the form D′GD with identity
diagrams D and D′ and a generator G in between. On morphisms:
• We describe the image of marked Soergel diagrams inductively from right to left. That is,
we describe what the functor does if one has already an identi ty diagram D : x → x and
D∞(D) : Mk → Mk (with D∞(x) ∼= Mk) and one adds a generator to the left.
41
• By construction of the image on objects and Corollaries 2.35 and 3.25, Mk will be just
one Tq(λk) with some multiplicity and grading shifts and some k ∈ { 0, . . . , i} giving two
cases, namely k = ˜l(x) even or odd. That is, we have
Mk = Tq(λk)⟨s1⟩ ⊕ · · · ⊕ Tq(λk)⟨sk′⟩.
Note that the translation functors Θ s and Θ t act on the summands as in Corollaries 2.35
and 3.25 separately. To simplify notation, we write Θ t(Mk) = Mk+1 if k is even and
Θ t(Mk) = Mk⟨−1⟩ ⊕ Mk⟨+1⟩ = ˜Mk if k is odd and vice versa for Θ s. Moreover, in the
case k = 0 we send any red generator to zero.
• The inductive description has four cases. We call these green-even, green-odd, red-even
and red-odd where we only give the list for the ﬁrst two since the other two are similar
with exchanged conventions for even and odd. Each case has ﬁv e sub-cases (for the ﬁve
generators) giving twenty cases in total. We write D0 (even) and D1 (odd) for the two
different cases. Since the Mk’s could already consist of multiple, shifted copies ofTq(i)’s,
the entries in the matrices below are shorthand notations for matrices themselves.
• Basic pieces: send the empty sequence 0 to id : Tq(0) → Tq(0). Moreover, for a green
identity we assign
D0 ↦→id : Mk+1 → Mk+1, D1 ↦→
(
id 0
0 id
)
: ˜Mk → ˜Mk
For the up dotted edge we assign (recalling the rescaling ˜εk = 2 kεk)
D0 ↦→uk : Mk → Mk+1, D1 ↦→
(
˜εk
id
)
: Mk → ˜Mk
For the down dotted edge we assign (recalling the rescaling ˜dk = 2 kdk)
D0 ↦→˜dk+1 : Mk+1 → Mk, D1 ↦→
(id ˜ εk
)
: ˜Mk → Mk
For the merges and splits in the even case we assign
D0 ↦→
(0 id )
: ˜Mk+1 → Mk+1, D0 ↦→
(
id
0
)
: Mk+1 → ˜Mk+1
For the merges in the odd case we assign
D1 ↦→
(
0 0 id 0
0 0 0 id
)
: ˜
˜Mk → ˜Mk
(with ˜
˜Mk = Mk⟨−2⟩ ⊕ Mk⟨0⟩ ⊕ Mk⟨0⟩ ⊕ Mk⟨+2⟩) and last but not least
D1 ↦→




id 0
0 id
0 0
0 0



 : ˜Mk → ˜
˜Mk.
42
• “Fill up the generators to the left”: for each red identity st rand to the left of the local
generators from above apply a Θ s to the elements of the matrices component-wise and
likewise for green strands and Θ t. This can be made explicit as explained in Example 3.15.
• If f is a homomorphismf ∈ Hom(QD(∞)), then decompose it into generators and deﬁne
D∞(f ) to be the composition of its local pieces.
We extend linearly for a general F ∈ Hom(Mat( ˆQD(∞))). ▲
Example 4.25. It is easy to see how the assignment is for alternating sequences. For example
↦→u0 : Tq(0) → Tq(1), ↦→˜d1 : Tq(1) → Tq(0)
and similar for all other diagrams of this kind. Furthermore, we have
↦→
(0 id )
: Tq(1)⟨−1⟩ ⊕ Tq(1)⟨+1⟩ → Tq(1)
↦→
(
id
0
)
: Tq(1) → Tq(1)⟨−1⟩ ⊕ Tq(1)⟨+1⟩
where we see that the degree is preserved. Moreover, the entr ies in the matrices of the list above
are in general already matrices. For example, the matrix that corresponds to (here M1 = Tq(1))
↦→
(
id ˜ ε1 0 0
0 0 id ˜ ε1
)
: ˜
˜M1 → ˜M1
Likewise for the horizontally ﬂipped diagram. ▲
Lemma 4.26. D∞ : Mat( ˆQD(∞)) → Tgr
λ is well-deﬁned, Q(q)-linear and degree preserving.□
Proof. It is immediate that D∞ is Q(q)-linear and degree preserving.
Moreover, note that, by part (b) of Corollary 2.35 and part (c ) of Corollary 3.25, the assign-
ment is well-deﬁned on objects x, since we send x to a repeated application of Θ s and Θ t to the
trivial Uq-module Tq(0) together with a projection onto the leading factor Tq(i). Thus, without
taking relations into account, we get a well-deﬁned functor from Mat(D(∞)f ) to Tgr
λ since our
assignment for the generating Soergel diagrams are all Uq-intertwiners.
Thus, the main part is to show that the relations are satisﬁed . This is now a case-by-case check
where we only do a few as examples and leave the rest to the reader.
Frobenius and isotopy relations: we do not have to check the Frobenius relations Frob1 and
Frob2 (18) and the isotopy relations Iso1 and Iso2 (21), since, by part (a) of Corollary 3.25, we
see that Θ s and Θ t are (graded) self-adjoint functors. By a more general princ iple such functors
always give rise to a Frobenius structure, see e.g. [46, Lemma 3.4].
43
Needle: for simplicity of notation, we assume that we are in the even case. We show
D∞








◦








= 0
This follows from
Mk+1

id
0


/d47/d47 ˜Mk+1
(
0 id
)
/d47/d47 Mk+1
The odd case is similar. This clearly implies the needle relation.
The dead-end relations 1+2: DE1 follows by construction. The DE2 relation is
D∞



◦


 = 0
This follows from
Tq(0)
u0 /d47/d47
Tq(1)
˜d1 /d47/d47 Tq(0)
which is the dead-end relation in the tilting case.
Barbell forcing 1: we only do one case (the one with equal colors) and leave the other (similar)
case to the reader. Again, for simplicity of notation, we focus on
D∞








◦








= 2 · D∞








◦








− D∞








◦








The general case follows completely similar. We have alread y explained in Example 4.25 how to
obtain the left two matrices. Thus, we obtain
(
id ε1 0 0
0 0 id ˜ ε1
)
◦




ε1 0
id 0
0 ˜ ε1
0 id



 =
(
2˜ε1 0
0 2˜ ε1
)
for the left side. The middle (without the factor 2) can be directly read off as
(
˜ε1
id
)
◦
(id ˜ ε1
)
=
(
˜ε1 0
id ˜ ε1
)
The rightmost term is the result of applying Θ t to 2˜ε1 (which is the composite of the diagram for
the ﬁrst two strands). This can be computed as explained in Section 3. Thus, we obtain
(
2˜ε1 0
0 2˜ ε1
)
= 2 ·
(
˜ε1 0
id ˜ ε1
)
−
(
0 0
2 · id 0
)
44
Barbell forcing 2: this is very similar to BF1 (only two terms are different) and we only sketch
it here. As before we only consider one particular case (the s ame as above for BF1) and leave the
others for the reader to verify. The different two terms are now
D∞








◦








, D∞








◦








These two cases give the matrices
(
2 · ˜ε1 0
0 2 · ˜ε1
)
and
(
0 0
2 · id 0
)
and the equation BF2 (20) then reads as
(
2 · ˜ε1 0
0 2 · ˜ε1
)
=
(
0 0
2 · id 0
)
+ 2
(
˜ε1 0
id ˜ ε1
)
− 2
(
0 0
2 · id 0
)
This ﬁnishes the proof. ■
Theorem 4.27. (Diagram categories for Tgr
λ ) The functor D∞ : Mat( ˆQD(∞)) → Tgr
λ is an
equivalence of graded categories. □
Proof. We have to show that D∞ is essentially surjective, full and faithful.
Essentially surjective: we have to show that, given some arbitrary object M ∈ Ob(Tgr
λ ), then
there is an object x ∈ Ob(Mat( ˆQD(∞))) such that D∞(x) ∼
= M. To see this, note that, by part
(c) of Proposition 2.20, it is enough to verify this for indec omposable Uq-modules Tq(i) in the
ungraded setting (using Proposition 3.19 the same is still true in the graded setting). Now, because
of our construction and part (b) of Corollary 2.35, we see tha t D∞(xi−tst) ∼= Tq(i) which shows
that the functor is essentially surjective.
Fully faithful: by Lemmas 4.11 and 4.26 it is enough to show that
HomMat(ˆQD(∞))(x, x′) ∼
= HomTgr
λ
(D∞(x), D∞(x′))
holds as graded Q(q)-vector spaces for alternating sequences x = xi−tst and x′
i′−tst. We have
already computed both sides: the right side was computed in C orollary 2.31 and the left in Corol-
lary 4.21. By our construction, the (graded) isomorphism is induced by the assignment i ↦→i,
ui ↦→ui, di ↦→˜di and εi ↦→˜εi whenever this makes sense. ■
Corollary 4.28. The category Mat( ˆQD(∞)) is idempotent complete. □
Proof. This follows from Theorem 4.27 because in Tgr
λ
∼= Tλ every module decomposes into a
direct sum of (shifted copies of) Tq(i)’s. ■
Corollary 4.29. (Diagram categories for the center) The graded Q(q)-algebra Endfs
gr(id) of nat-
ural transformations in pEnd(Tgr
λ ) of the identity functorid is given by the diagonal part of ﬁnitely
supported (only a ﬁnite number of non-zero entries) matrices
(26) F : ∅ ⊕ g ⊕ rg ⊕ grg ⊕ rgrg ⊕ · · · → ∅ ⊕ g ⊕ rg ⊕ grg ⊕ rgrg ⊕ . . .
45
of marked Soergel diagrams with no identity diagram entry. In contrast, Endfs
Uq(Tq(∞ )) ∼= Q∞ is
given by all such matrices and not just the diagonal part. □
Proof. An alternating sequence of red and green of length i corresponds under the equivalence
from Theorem 4.27 to Tq(i), since, by Proposition 4.23, the quiver relations are satis ﬁed. This
module corresponds under the isomorphisms from Corollary 3.28 to iP . Thus, the claim follows by
Theorem 4.27 and Proposition 3.27, since (graded) equivalent categories have (graded) isomorphic
centers and the observation that an F as in (26) is a natural transformation iff it commutes with
all other such F ’s (compare also to (28)). That the center of the matrix ring i s as stated above is
then an easy to deduce fact: the i are not central (as already noted after Deﬁnition 3.1), whil e the
εi compose with everything to zero (and are therefore in the center). ■
Remark 4.30. Relaxing the conditions to work over another ﬁeld and not Q(q) is actually a prob-
lem in Section 2 since the indecomposable tilting modules an d their hom-spaces are much more
complicated in positive characteristic. For the KS quiver a lgebras from Section 3 working over Z
is not a huge problem, while for the diagrammatic categoryQD(∞) we need to work overQ. ▲
4.5. Diagram categories for pEnd(Tgr
λ ). We denote by
Mat(C) literally the same category as
Mat(C), but we allow countable direct sums as objects and ﬁnitely supported matrices as mor-
phisms. We carefully distinguish between red r and green g on one hand and s, t ∈ Wl on the
other. We think of an alternating sequence (of length i ≥ 0) of the former xi−grg to correspond
(under Theorem 4.27) to Tq(i) and of any sequence of the latter x = xi . . . x2x1 to correspond to
Θ x = Θ xi ◦ · · · ◦ Θ x1. Using this interpretation, we are going to make Propositio n 3.27 explicit.
We deﬁne ⃗∞ to be the sequence of alternating xi−grg sequences
⃗∞ = (. . . , rgrg, grg, rg, g, ∅), ⃗∞i = xi−grg for i = 0, 1, . . . ,
where we read the vector from right to left.
Moreover, given a ﬁnite sequence x = xi . . . x2x1 with xi ∈ {s, t} we deﬁne
x · ⃗∞ = (. . . , xrgrg, xgrg, xrg, xg, x ), (x · ⃗∞)i = xxi−grg for i = 0, 1, . . . ,
where each entry is given by concatenation. In addition, we deﬁne
xxi−grg =
⨁
i′
xmi′
i′−grg ⟨si′⟩
where the multiplicity mi′ is the multiplicity of Tq(i′) in Θ x(Tq(i)) given inductively by part c
of Corollary 3.25 (from where we also get the shifts si′). Thus, we see xxi−grg as an object
Ob(Mat( ˆQD(∞))). Note that xx0−grg = 0 if x starts with r because of Θ s(Tq(0)) = 0 .
Deﬁnition 4.31. Denote by Matfs
∞( ˆQD(∞)) the Q(q)-linear, graded category consisting of:
• Objects Ob(Matfs
∞( ˆQD(∞))) are ﬁnite sequences x = xi . . . x2x1 with xi ∈ {s, t} (plus
shifts). Moreover, the empty sequence ∅ is also an object.
• The space of morphisms HomMatfs
∞(ˆQD(∞))(x, x′) for x, x′ ∈ Ob(Matfs
∞( ˆQD(∞))) is the
Q(q)-linear span of ﬁnitely supported (only a ﬁnite number of non-zero entries) matrices
F = (Fk′k)k,k′∈Z≥0 ∈ Hom
Mat(ˆQD(∞))(x · ⃗∞, x′ · ⃗∞)
of marked Soergel graphs Fk′k : ( x · ⃗∞)k → (x′ · ⃗∞)k′.
• The diagonal part of F consists of matrices F i : ( x · ⃗∞)i → (x′ · ⃗∞)i.
• Composition of morphisms is multiplication of matrices.
46
The spaces HomMatfs
∞(ˆQD(∞))(x, x′) are graded Q(q)-vector spaces where the degree is given by
l(Fk′k) (the degree or length from Deﬁnition 4.5) for each entry of matrices F . ▲
Denote by pEndfs
Θ (Tgr
λ ) the full subcategory of pEnd(Tgr
λ ) consisting of only compositions of
Θ s and Θ t (together with the condition of being ﬁnitely supported). Note that, by Proposition 2.39,
we have
Kar(pEndfs
Θ (Tgr
λ )) ∼= pEndfs(Tgr
λ ).
Moreover, we denote by Matfs
∞( ˆQD(∞))c the subcategory of Matfs
∞( ˆQD(∞)) whose hom-
spaces are
(27) HomMatfs
∞(ˆQD(∞))c
(x, x′) = {F ∈ HomMatfs
∞(ˆQD(∞))(x, x′) | F G = G′F },
for G ∈ HomMatfs
∞(ˆQD(∞))(x, x) and G′ ∈ HomMatfs
∞(ˆQD(∞))(x′, x′) such that entry-wise there
exists an Uq-intertwiner f : M → M ′ with D∞(Gi′i) = Θ x(f ) and D∞(G′
i′i) = Θ x′(f ). The
reader may check that Matfs
∞( ˆQD(∞))c is really a subcategory.
Deﬁnition 4.32. We deﬁne a functor
D∞ : pEndfs
Θ (Tgr
λ ) → Matfs
∞( ˆQD(∞))c
on objects (we treat shifts again in the evident way) and morphisms as
Θ x ↦→x, and η : Θ x → Θ x′, η Tq(i) : Θ xTq(i) → Θ x′Tq(i) ↦→diag(F ) = ( F i)i∈Z≥0 : x → x′,
where diag(F ) is a diagonal matrix consisting of the various F i’s and, for each i, the matrix of
marked Soergel diagrams F i is component-wise given by i ↦→i, ui ↦→ui, di ↦→di and εi ↦→εi for
all suitable indices i and marked Soergel diagrams as in Corollary 4.21. ▲
Lemma 4.33. The functor D∞ : pEndfs
Θ (Tgr
λ ) → Matfs
∞( ˆQD(∞))c is a well-deﬁned functor
between Q(q)-linear, graded categories. □
Proof. The Q(q)-linearity is clear. In addition, the assignment is clearly degree preserving and
well-deﬁned component-wise (since the quiver relations are satisﬁed, see Proposition 4.23).
To see that it is well-deﬁned note that ηTq(i) is a matrix consisting of Uq-intertwiners between
the direct summands of Θ xTq(i) and Θ x′Tq(i) (for each Tq(i)). These are sums of i, ui, di and εi
by the isomorphism of Proposition 3.10. To see that the relations are satisﬁed, note that, given any
Uq-intertwiner f : M → M ′, the naturality of a transformation η : Θ x → Θ x′ says that
(28)
Θ xM
Θ xf /d47/d47
ηM
/d15/d15
Θ xM ′
ηM ′
/d15/d15
Θ x′M Θ x′ f
/d47/d47 Θ x′M ′
commutes. Thus, the matrices coming from our assignment satisfy the condition (27). ■
47
Theorem 4.34. (Diagram categories for pEnd(Tgr
λ )) The functor D∞ is a graded equivalence.□
Proof. As in Theorem 4.27, we have to show that D∞ is essentially surjective, full and faithful.
That D∞ is essentially surjective follows from the deﬁnition of theobjects in Matfs
∞( ˆQD(∞))d.
That it is faithful is a direct consequence of Proposition 3. 27 combined with Theorem 4.27. That
D∞ is full is just a direct comparison of (27) and (28). ■
Remark 4.35. A possible generalization of our diagrammatic categories c ould follow from work
of Elias and Libedinsky on Coxeter groups, see [20]. The underlying Coxeter group W will for An
be the afﬁne Weyl group, that is, the one given by the cyclic Dynkin diagram with n + 1-nodes
•
•
•qqqqq
▼▼▼▼▼
n = 2
•
•
•
•
⑧⑧⑧
❄❄❄ ⑧⑧⑧
❄❄❄
n = 3
••
• •
•
✐✐✐
❯❯❯ ✟✟
✻✻
n = 4
••
•
• •
•
✌✌
✶✶ ✌✌
✶✶
n = 5
· · ·
where the green (rightmost) nodes indicate the afﬁne nodes. ▲
