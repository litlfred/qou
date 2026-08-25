---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-007-8-combinatorics-for-tilting-modules
section_title: "Combinatorics for tilting modules"
section_number: 8
pages: 22-27
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick id eals."
---
By theorem 7.3 thek-negligible ideals are deﬁned for modular and quan-
tum tilting modules. Contrary to the case of Deligne categor ies, not every
thick ideal is one of the Nk. We would like to understand the negligible
idealsNk for modular and quantum tilting modules. In both cases the th ick
ideals are governed by the intricated Kazhdan-Lusztig cell theory of the
aﬃne Weyl group which is largely not understood in the modula r case. In
the following we try to give a more direct geometric descript ion of these
cells. While the results in the current section are general, we focus on type
A in section 9.6.
8.1. Classiﬁcation of thick ideals. We ﬁrst recall the classiﬁcation of the
thick ideals due to Ostrik and Achar-Hardesty-Riche.
8.1.1. Ostrik’s classiﬁcation.
Deﬁnition 8.1. ([
O97] [ An04]) For λ,µ ∈X + write λ ≤q µ if there exists
Q ∈ Tilt (Uq(g), Q(q)) such that T (λ) is a summand of T (µ) ⊗Q. If both
λ ≤q µ and µ ≤q λ write λ ∼q µ. The equivalence classes are called weight
cells.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 2 3
We remark that for any λ ∈X + we have λ +ν ≤q λ for all ν ∈X + since
T (λ +ν) is a summand of T (λ) ⊗T (ν). The fundamental alcove Cℓ is the
unique maximal weight cell in the ≤q ordering. For a weight cell c we denote
by
T (≤q c)
the subcategory of objects in Tilt (Uq(g), Q(q)) whose objects are direct sums
of T (λ) with λ in a cell c′ satisfying c′ ≤q c. Then T (≤q c) is a thick ideal
in Tilt (Uq(g), Q(q)).
The division of X + into weight cells gives a division of W +
ℓ . Recall that
Lusztig and Xi have deﬁned a partition of W +
ℓ into right cells along with a
right order ≤R on the set of right cells.
Theorem 8.2. ([O97]) The weight cells in X + (and therefore the thick
ideals in Tilt (Uq(g), Q(q))) correspond to the right cells in W +
ℓ , i.e. for any
right cellA ∈W +
ℓ the full subcategoryTilt (Uq(g), Q(q))≤A ⊂Tilt (Uq(g), Q(q))
of direct sums of tilting modules T (λ) for
λ ∈
⋃
w∈B≤RA
Cw
is a thick ideal.
By [ O97, Remark 5.6] every thick ideal is a sum of ideals of the form
Tilt (Uq(g), Q(q))≤A for a right cell A so that this theorem yields the classi-
ﬁcation of thick ideals in Tilt (Uq(g), Q(q)).
8.1.2. Thick ideals in the modular case. The notion of a weight cell can be
deﬁned in complete analogy to the quantum case in section 8.1.1. We denote
the modular analog of the preorder and the equivalence class es by ≤T and
∼T . An equivalence class is called a modular weight cell andCp is the largest
modular weight cell. Contrary to the quantum case there are i nﬁnitely many
modular weight cells (see section 7.5.1). Any modular weight cell c deﬁnes
a thick ideal
T (≤T c).
Ostrik’s classiﬁcation carries over to the modular case if w e replace right
cells by right p-cells (also called anti-spherical right p-cells).
Theorem 8.3. ([AHR17, Theorem 7.7, Corollary 7.8] ) The modular weight
cells in X + (and therefore the thick ideals in Tilt (G,k )) correspond to the
right p-cells in W +
p , i.e. for any right p-cell A ∈ W +
p the full subcategory
Tilt (G,k )≤A ⊂Tilt (G,k ) of direct sums of tilting modules T (λ) for
λ ∈
⋃
w∈B≤R,p A
C w
is a thick ideal.
As in the quantum case, every thick ideal is a sum of ideals att ached to
rightp-cells.
24 THORSTEN HEIDERSDORF AND HANS WENZL
Example 8.4. By [
An04] the set
cr
1 = (pr − 1)ρ +Xpr +prCp
is a weight cell which contains Str. We call this weight cell the r-th Steinberg
cell. We have an equality of thick ideals <St r >=T (≤c
r
1).
Remark 8.5. Since every thick ideal in the quantum and modular case is
a sum of thick ideals attached to right cells, the nullity of a tilting module
is constant on an alcove. Indeed, if T (λ) is a tilting module in a thick ideal
I and T (λ) is contained in an alcove A, the entire alcove is contained in I
since the ideal is a union of weight cells.
8.2. Aﬃne W eyl groups. We review some basic combinatorics in connec-
tion with aﬃne Weyl groups and tilting modules. See [
J03], [ Ja77] , [ A03],
[S1], [S2] and the literature quoted in these papers for more details. The use
of facets for Kazhdan-Lusztig combinatorics already appea red before e.g. in
[GW01].
Let Xn be a ﬁnite root system, and let X (1)
n be the root system of the
corresponding untwisted aﬃne Weyl group. It has a faithful r epresentation
in h∗, where the generating reﬂections for Xn act as usual, and the additional
generator acts via the reﬂection in the hyperplane given by ( θ,γ ) = ℓ, where
ℓ is a positive integer, θ is the long resp short root of greatest length if d|ℓ
respd ∤ℓ; here d is the ratio of the square length of a long and a short root.
We obtain a system of hyperplanes on h∗ from the orbits of the generating
hyperplanes under the aﬃne Weyl group. They can be described explicitly
by
Hα,k = {x ∈ h∗ | (x,α ) = kℓ}, α ∈ ∆ +,k ∈ Z,
if d|ℓ. If d ∤ ℓ, we just replace the roots α by coroots in the deﬁnition
above. The positive and negative sides of these hyperplanes are deﬁned
in the obvious way, replacing the equal sign in the deﬁnition by inequality
signs. These hyperplanes make h∗ into a cell complex as follows: We call
an intersection of k hyperplanes maximal if it has dimension n −k, and we
denote by h∗(n −k) the union of all maximal intersections of k hyperplanes.
The set ofj-cells then is given by all connected components of h∗(j)\h∗(j−1),
with h∗(−1) being the empty set.
8.3. Alcoves and facets. As usual, we call the n-cellsalcoves, and lower-
dimensional cells facets . The (n−1)-cells which are in the closure of a given
alcoveA are called the walls ofA. The fundamental alcove Cℓ is deﬁned to
be the unique alcove in the dominant Weyl chamber whose closu re contains
the origin 0. We say that a wall of Cℓ corresponds to the simple reﬂection si
if it is ﬁxed by it. This deﬁnes a 1-1 correspondence between t he walls of Cℓ
and the simple reﬂections. We can now deﬁne a 1-1 corresponde nce between
the alcoves and the elements w of the aﬃne Weyl group as well as a labeling
of the walls via simple reﬂections by induction on the length ofw as follows:
The element 1 corresponds to Cℓ. If the alcove A corresponds to the element
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 2 5
w, and si is a simple reﬂection such that wsi has greater length than w, then
the alcove A′ =Asi corresponding to wsi is obtained by reﬂecting A in the
wall labeled by si. This reﬂection also deﬁnes the labeling of the walls of
A′. Moreover, the action of the si deﬁnes a right action of the aﬃne Weyl
group on the alcoves. The alcoves in the dominant Weyl chambe r are in 1-1
correspondence with the shortest elements of the cosets of t he ﬁnite Weyl
group in the aﬃne Weyl group. The Bruhat order then has the geo metric
interpretation that u<w is equivalent to the fact that whenever u(Cℓ) and
v(Cℓ) lie on opposite sides of a hyperplane, u(Cℓ) must be on the negative
and w(Cℓ) must be on the positive side of that hyperplane. We similarl y
deﬁne for two facets F1 and F2 that F1 <F 2 if F2 lies in or on the positive
side of any hyperplane which contains F1.
For a given facet F , the stabiliser group W (F ) is the group generated by
the reﬂections in the hyperplanes which contain F . We denote by Cℓ(F ) the
unique alcove whose closure contains F , and which is on the positive side of
every hyperplane which contains F . The set ∆( F ) denotes the positive roots
corresponding to the hyperplanes which contain F and a wall of Cℓ(F ). By
deﬁnition, Cℓ(F ) is on the positive side of each of these hyperplanes. We
call the reﬂections corresponding to the roots in ∆( F ) the simple reﬂections
of W (F ), and the roots in ∆ F the simple roots of W (F ). We also deﬁne
the positive cone C+(F ) to be the region which is above all hyperplanes
corresponding to the roots in ∆( F ).
8.4. Tilting modules and linkage. If the context is not speciﬁed, the
statement holds for tilting modules of quantum groups at roo ts of unity as
well as for tilting modules of algebraic groups in character isticp. Let T (λ) be
the unique indecomposable tilting module up to isomorphism whose highest
weight is λ. We will use the well-known fact that if the Weyl module V (λ)
is simple, it coincides with T (λ) and with the simple module L(λ) of highest
weightλ.
Theorem 8.6. (Linkage Principle) The Weyl module V (µ) appears in a
ﬁltration of the tilting module T (λ) only if µ is in the orbit of λ under the
aﬃne Weyl group and µ ≤λ in Bruhat order.
8.5. Minimal facets. The following lemma describes some tilting modules
which are simple. We call a facet F minimal if it lies in the interior of the
dominant Weyl chamber C and no other facet in its orbit which also lies in
the interior of C can be smaller than it in Bruhat order. We then have the
following easy lemma:
Lemma 8.7. LetF be a minimal facet and let λ be an integral dominant
weight such that λ +ρ ∈F .
(a) In both the quantum group case and in the modular case, we ha ve
T (λ) = V (λ) and the nullity of T (λ) is equal to k(F ), the number of hyper-
planes in which F lies.
26 THORSTEN HEIDERSDORF AND HANS WENZL
(b) Consider the modular case in characteristic p. Let λ(r) = prλ +
(pr−1 − 1)ρ. Then T (λ(r)) = V (λ(r)) and the nullity of T (λ(r)) is equal to
r|R+| +k(F ).
Proof. By deﬁnition of minimal facet and the linkage principle, the re
exists no dominant integral weight µ in the orbit of λ such that µ < λin
Bruhat order. Hence the only Weyl module which appears in the ﬁltration
of T (λ) is V (λ) itself. The statement about the nullity is a direct conse-
quence of the dimension formula (for p>h in the modular case). The same
argument also works for case (b), using Lemma 7.10.
8.6. Thick tensor ideals. Let I(F ) be the thick ideal generated by the
tilting modules T (λ) with λ +ρ ∈F . Recall that C+(F ) is the region con-
sisting of all points x ∈ h∗ which are on the positive side of any hyperplane
which contains F .
Proposition 8.8. LetF be a minimal facet, and let λ and λ(r) be as in
Lemma 8.7.
(a) In the quantum group case, the ideal I(F ) contains all modules T (ν)
with ν +ρ in C+(F ). Any module in I(F ) has nullity ≥k(F ).
(b) In the modular case, the ideal I(F (r)) generated by all T (λ(r)) with
λ +ρ ∈ F contains all modules T (ν) with ν ∈ λ(r) +X+, where X+ is the
set of all dominant all dominant integral weights. Any modul e in I(F (r))
has nullity at least r|R+| +k(F ).
Proof. Assumeν +ρ ∈C+(F ). Then we can ﬁnd a dominant integral weight
λ such that λ +ρ ∈ F and ν −λ is a dominant weight. Hence the tensor
product T (λ) ⊗T (ν −λ) has highest weight ν. It follows that Tν ∈ I (F ),
and hence has at least the nullity of F . □
Example 8.9. In the modular situation, the case λ = 0 corresponds to the
Steinberg representations Str.
In order to get a more concrete description of these tensor id eals, it will be
important to determine when two diﬀerent facets generate the same tensor
ideal.
Deﬁnition 8.10. Let F1 and F2 be minimal facets. We say that they are
tensor equivalent if I(F1) = I(F2).
Lemma 8.11. Let I be the tensor ideal generated by the simple objectT ,
and let S be an object in I with the same nullity as T . Then also S generates
I. In particular, if F1 and F2 are tensor equivalent minimal facets, then
k(F1) = k(F2).
Proof. By assumption, there exists an object W such that S ⊂ T ⊗W .
There exist maps
ι : 1 →W ⊗W ∗, d :W ⊗W ∗ → 1
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 2 7
such that d ◦ι = dim(W ). Moreover, by assumption, there exist morphisms
ιS :S →T ⊗W anddS :T ⊗W →S such thatdS ◦ιS =idS. Let a ∈ End(S)
such that Tr (a) has minimal nullity. We then deﬁne maps u :T →S ⊗W ∗
and v :S ⊗W ∗ →T by
u = (dS ⊗idW ∗) ◦ (idT ⊗ι), v = (idT ⊗d) ◦ (ιSa ⊗idW ∗).
It follows that vu is an endomorphism of the simple object T , and hence
vu = αidT for some scalar α. By functoriality of the trace operation, it
follows from the deﬁnitions
α dim(T ) = Tr (vu) = Tr (uv) = Tr (a).
As Tr (a) and dim( T ) have the same nullity, it follows that α is invertible.
But then α−1uv is an idempotent in End( S ⊗ ¯W ) whose image is isomorphic
to T . □
Corollary 8.12. IfF1 >F 2 and they have the same nullity, then I(F1) =
I(F2) and C+(F1) ⊂C+(F2).
Remark 8.13. 1. In our cases, the nullity of the tensor ideal would cor-
respond to the length of the longest element of the stabilize r of F . On the
other hand, it is well-known that the longest element w0 of a parabolic sub-
group is in a cell for which the a-function is equal to the length of w0. For
rank 2 and for type An, these exhaust all two-sided cells.
2. All thick ideals are explicitly known in type A, see [ Shi]. Each of them
can be associated to a parabolic subgroup, and hence to a face t. However,
there already seems to be a left cell for type D4 whose value of thea-function,
seven, would not be the length of the longest element of a para bolic subgroup
of aﬃne D4, see [ DJ], [ CCD].
