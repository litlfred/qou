---
doc_id: kuperberg-1996-cmp-180-109-spiders
doc_title: "Spiders for Rank 2 Lie Algebras"
section_id: sec-002-6-equinumeration
section_title: "Equinumeration"
section_number: 6
pages: 27-40
source_pdf: kuperberg-1996-cmp-180-109-spiders.pdf
source_sha256: b6c94630554cc15a
toc_source: inferred
doc_brief: "Spiders for Rank 2 Lie Algebras — A spider is an axiomatization of the representation theory of a group, quantum group, Lie algebra, or other group or group-like object."
---
6. Equinumeration
6.1. The A2 case
Theorem 6.1. Let C be an A2 clasp sequence and let wt C be the corresponding
sequence of weights. Then the vector spaces W(C) and Inv(F(wt C)) have the
same dimension.
One of the main steps of the proof of Theorem 6.1 is the same as that of the
proof of Theorem 2.3: Given two clasp sequences C and D, there is a decomposition
of vector spaces
Inv(F(wt C) 0 V(wtD)) ^ 0 Inv(Ύ(wtS) 0 V(μ)) 0 Inv(Ύ(μ)* 0 V(wtD)) .
μ
We wish to prove the corresponding decomposition of sets of basis webs:
Theorem 6.2. Given two clasp sequences C and D,
B(CD)^{J(B(Ccλ)xB(ctD)),
λ
where for each weight λ, cχ is some clasp with weight λ.
Theorem 6.2 is more complicated than its analogue for the A\ spider, because
there is no longer always a unique minimal cut path separating the clasp sequences
C and D:
Although the two cut paths in this example have the same weight, they have different
transverse strand types and they yield webs in different clasped web spaces. Yet not
every ordering of the strands is always possible. Nevertheless, there is a way to
reconcile these different decompositions and ameliorate the ordering problem.
Indeed, order independence is a large part of the combinatorial content of
Theorem 6.1. For example, it implies the following result, which has an independent
proof that is another warm-up to the proof of Theorem 6.1.
Theorem 6.3. If two sign strings s\ and s2 of the unclasped A2 spider differ only
in order, then B(s\) and B(s2) are equinumerous.
Proof. The web
is the H-web. It suffices to consider the case in which s\ and s2 are the same except
for one pair of transposed signs at adjacent positions p and q. Then there is a
136 G Kuperberg

bijection A: B(s;) — B(sz) that has the following effect on non-elliptic webs. If a
web w connects p to q by a bare strand, h(w) is the same web with the orientation
of the strand reversed:

eae

If there is an H-web attached at p and q, h(w) is w with the H-web removed:

+
+ + - +
) :
+ + + +

If there is no H-web, then A(w) is w with an H-web attached:

+ +
+ + + +
»)
_ + + _
It is easy to check that A(w) is non-elliptic if w is, and that A has an inverse. In
fact, the inverse is also an A-map. 0

In the notation of the above proof, we also say that w and h(w) differ by an
H-move.

Lemma 6.4. If « is a minimal cut path of w € B(ST) separating S from T, it
divides w into two parts w; € B(Sc) and wz € B(c*T) with non-convex clasps c
and c*.

Proof. If ¢ were convex in w), w; would have a cut path «’ whose weight is lower
than that of c, the same as the weight of «. But «’ is also a cut path in w and has
the same endpoints as «, contradicting the hypothesis that « is minimal:

wt.

ri

Lemma 6.5. If « and B are cut paths from p to q of a basis web w and « is
minimal, then the weight of « is less than or equal to (and not incomparable to)
Spiders for Rank 2 Lie Algebras 137

the weight of B. If B is also minimal, the two parts of w cut by B are the same
as those of w cut by « up to H-moves.

Proof. The proof is by induction on the complexity of w; assume that w is a
minimal counterexample. Assume also that, having chosen w, a and f are transverse
and intersect minimally. First, we can discard any structure of w not bounded by
a U B; the new web has no clasps and is non-elliptic since w is non-elliptic. Second,
we claim that « and B do not intersect except at their endpoints. Otherwise, let «’
be a segment of « between two consecutive intersections x; and x2, and let p’ be
the arc of 8 from x; to x2 (which are not necessarily consecutive along £). Then the
region between «’ and f’ is either empty, in which case «’ and f’ do not intersect
minimally; or it constitutes a smaller counterexample than w for some choice of a’;
or B’; or « and B have comparable weight:

A

x,=p
a,

wart BB
Mx, .

Third, w must be connected, for if one of its connected components meets « but
not £, « is not a minimal cut path; if one of its components meets f but not «, it
may be discarded to produce a smaller counterexample; and if all components meet
both « and f£, one of them is a smaller counterexample:

Finally, if e; and e2 are adjacent endpoints of w, define the exterior curvature of
the arc @]@2 to be 180° — n60°, where n is the number of vertices of w connecting
e; to e:

The total exterior curvature of w is at least 360° since w is non-elliptic. Moreover,
the curvature at the arcs containing p and q is at most 120°, for if it were 180°,
either w would be disconnected or it would be a single strand. Therefore there must
138 G Kuperberg

be a segment +» of either « or with positive curvature. There are three possibilities
for the edges of w that bound a face together with y:

if) - i -

1 3

1. A “U.” In this case, w is either disconnected or a single strand.

2. A “Y.” If y lies on a, then « is not minimal. If y lies on £, then an isotopy
of B across the “Y” produces a smaller counterexample.

3. An “H.” In this case, an isotopy of either « or B produces a smaller coun-
terexample by an H-move.

This eliminates all possibilities for the least counterexample. O

Lemma 6.6. Let C be a sequence of clasps, let c be an arbitrary clasp, and let
w € B(Cc) be a basis web. There is a cut path y that separates c such that any
other such cut path lies between y and c.

Proof. If « and $ are two transverse, minimal cut paths that separate c and p
and g are two consecutive transverse intersection points along either path, then the
weight of the arc of « from p to q must equal the weight of the arc of 6 from p
to q, for otherwise one path would provide a short-cut for the other and either « or
B would not be minimal. Thus the path y that follows the perimeter of «U 6 must
also be minimal:

If we partially order cut paths by their distance from c, there is a unique maximal
element. DO

Given w as in Lemma 6.6, define the core of w relative to c to be the web
w’ € B(Cc’) obtained by cutting away c along the cut path y guaranteed by the
lemma. Here c’ is another clasp with the same weight as c. Let B(C; A) be the set
of all cores of webs w € B(Cc) for all clasps c of weight A. Note that, since c is
non-convex in w, one of the minimal cut paths that separates c is parallel to c.
Therefore, by Lemma 6.5, w differs from its core by H-moves. Note also that the
core w’ has the property that no H-webs are attached at c’, and that any web with
this property is its own core.

We describe how an arbitrary basis web extends from one of its cores. Consider
the following stair-step construction of a basis web from a core. Suppose that
w € B(C[s]) is a core relative to a clasp [s] of weight A = ad, + bd2, and suppose
that [s’] is an arbitrary clasp of the same weight. Then the strings s and s’ each
Spiders for Rank 2 Lie Algebras 139

represent paths p and p’ from the the upper left corner to the lower right corner of
an a x b rectangle, where each “+” in s or s’ is a step to the right and each “—”
is a step down:

+ + P
‘Ott
S=t+----++ p' Br
soa +--+ -tt- | +
ASA

If an H-web is placed in each square as indicated, the two paths p and p’ delineate
a sequence of connected webs, separated by points or segments where p and p’
meet and may or may not cross. We attach each web bounded below by p to w,
and we invert and reverse the arrows of each web bounded above by p and then
attach it to w. The result is a web w’ € B(C[s’]) with core w:

cad
|

If s; and s2 are arbitrary strings of the same weight, we can set s’ to either in
the stair-step construction, which implies that any core w of a web in B(C[s;]) is
also a core of a web in B(C[s2]). Moreover, it is easy to check that, if w is fixed,
the collection of webs so produced is closed under H-moves. Since every basis web
is related to its core by H-moves, the stair-step construction produces all webs in
B(Cc) for all c with weight A. In particular, we have demonstrated the following
lemma:

Lemma 6.7. Let C be a sequence of clasps and let c be a clasp of weight 2.
If w € B(C[c]), let f(w) be its core. Then the map f : B(C[c]) — B(C;4) is a
bijection.

Using the above lemmas, we can prove Theorem 6.2:

Proof. Let w; € B(C; A) and w2 € B(D; 4*), and let c; and c2 be the clasps of w;
and w2 of weight 2 and 4*. Then we can either extend w; to a basis web in B(Cc})
or extend w2 to a basis web in B(Dc;) and then sew the two webs together; by the
symmetry of the stair-step construction, the resulting web w € B(CD) is the same
140 G. Kuperberg

in both cases. Define

f:U (B(C; A) x BID; 4")) > B(CD)
A

by the above operation on pairs of cores. By Lemma 6.5 and the fact that H-moves
preserve cores, there is also a map

g : BCD) > L (B(C; 4) x B(D; 4")
vi

given by splitting w along a minimal cut path and taking the cores of the two
halves. By Lemma 6.7, f and g are inverses. Using Lemma 6.7 again, we can see
g as the bijection claimed by the theorem. O

To prove Theorem 6.1, we need one additional lemma. Say that a sign string s
is segregated if it is of the form

tHe pore;

a sign string with only +’s or only —’s is automatically segregated. Likewise, say
that a clasp is segregated if it is of the form [s] for a segregated sign string s.

Lemma 6.8. Let c and d be segregated clasps of weight 4 and yu. Then the web
basis set B([+]ed) has one element if and only if #* =m+A,, wh =A+A, or
A* = p+, —A/1, and is empty otherwise.

Proof. Consider first three segregated clasps c, d, and e (one of which might be
empty) of arbitrary weight, and let w € B(cde). We claim that w must consist of a
number of bare strands plus a flat component, as in the following example:

The argument is similar to the proof of Lemma 6.5. Assume first that w is not
connected. If p and q are adjacent endpoints of w, we define the curvature of the
segment of the boundary of w from p to qg as in Lemma 6.5. Since w is non-elliptic,
it must on the one hand have total exterior curvature at most 360°. On the other
hand, there can be no “U” or “Y” attached along c, d, or e, and in there is only
one place along each clasp where an H is possible. The curvature at this H, if it
is present, is at most 60°, and the curvature elsewhere along the clasps is at most
0°. Moreover, unless w is a bare strand, the curvature at the segments between the
clasps is at most 60° also. The largest possible total is 360° exactly, so that w is
Spiders for Rank 2 Lie Algebras 
141
flat and its boundary is qualitatively a hexagon:
If w is not connected, then the above argument applies to each connected component
of w, with the additional observation that at most one component of w can meet all
three clasps c, d, and e. A component that only meets two clasps is necessarily a
bare strand.
In the case of interest, e = [+]. In this case, w might consist entirely of bare
strands, or it might have a component in the shape of a parallelogram or a trapezoid:
C
 
c
These possibilities exactly match the restrictions on the weights of c and d. 
D
Finally, we prove Theorem 6.1:
Proof. Let Λ+ be the set of all weights λ = aλ\ -f bλ2 with α,ό € Z^ 0 
Con-
sider the abelian group %[Λ+] of formal sums of elements v(λ) for each λ e Λ+.
Then we can define a product in Z[A+] using the dimensions of the clasped web
spaces:
where in the sum each C{ is some clasp of weight λ(. By Theorem 6.2, there exist
bijections
U (B(c,c2d) x B(c3c4d*)) 9έ B(Cιc2c3c4) 
9έ (\jB(c2c3d) 
x B(c4Cιd*)) 
.
d 
\ d 
/
These bijections imply that multiplication is associative, and therefore Z[A+] is
a ring. To establish Theorem 6.1, it suffices to check that the map v(λ) \—> V(λ)
induces an isomorphism from Z|yl+] to the Grothendieck ring of A2. Using induc-
tion, it suffices to check that for all λ e A+,
v(0)v(λ) = v(λ),
v(λι )v(λ) = v(λ + λι) 4- v(λ - λx + λ2) + v(λ - λ2),
v(λ2)v(λ) = υ(λ + λ2) + v(λ -λ2 + λι) + 
υ(λ-λι),
142 
G Kuperberg
where v(λ) is defined as 0 for λ$Λ+, 
because similar relations hold in the
Grothendieck ring. (Note that we cannot argue from an a priori hypothesis that
Z[Λ+] is the Grothendieck ring of a category, because such a construction assumes
the existence of internal clasps, which in turn depends on Theorem 6.1.) In terms
of webs, the first relation states that if c and d are two segregated clasps, then
B(cd) is empty unless c = d*, in which case it has one element. This follows from
Lemma 6.5 or from arguments similar to those of Lemma 6.8. Similarly, the other
relations are equivalent to Lemma 6.8. D
6.2. The B2 and G2 cases
Theorem 6.9. Let C be a B2 clasp sequence and let wt C be the corresponding
sequence of weights. Then the vector spaces W{C) and Inv(F(wt C)) have the
same dimension.
Theorem 6.10. Let C be an G2 clasp sequence and let wt C be the corresponding
sequence of weights. Then the vector spaces W(C) and Inv(F(wt C)) have the
same dimension.
To establish these two results we mainly need to alter various technical defini-
tions given for the A2 case; most of the lemmas leading up to Theorem 6.2 and
the proof of the theorem then carry over word-for-word. An H-web in the B2 or G2
spider is the web:
x
In both the B2 and G2 spiders, one can define an H-move on a basis web w with
two adjacent endpoints labelled 1 and 2. An H-move at two such endpoints consists
of attaching an H-web to w, provided that this operation does not create an elliptic
face, and then replacing an internal double edge by a tetravalent vertex in the B2
spider or by a perpendicular single edge in the G2 spider:
y=\ 
* 
X 
0B2case),
(G, case) . 
(7)
X
If attaching an H-web would result in an elliptic face, then there are two alternatives:
Either an H-web can be removed (possibly after introducing an internal type 2 strand
by the above operations), or the two endpoints make a "Y:"
>C
Spiders for Rank 2 Lie Algebras 143

or, in the G2 case, they make an “H” with only one type 2 strand:

In each of these exceptional cases, the operation indicated is the H-move.

The operation of cutting along a minimal path is slightly more complicated than
before, because the path might cut diagonally across a vertex in the B) spider or
contain a type 1 edge in the G2 spider. The operation is defined by first introducing a
type 2 edge, as is sometimes also necessary for an H-move, by reversing the contrac-
tion operation of Fig. (7). A core is defined in the same way for all three rank 2 spi-
ders. The stair-step construction is essentially the same as before. Each square is an
H-web, with the result that sewing together two cores with stair steps in between re-
sults in many internal type 2 strands, which are removed by the operation of Fig. (7).

The biggest difference between the three rank 2 cases is in the statement and
proof of the analogues of Lemma 6.8. We wish to check that, if s € {1,2} and c
and d are arbitrary clasps of weight 2 and y, then

|B([s]ed)| = dim Inv(V; @ V(A) ® V(u)) . (7)

For this purpose, one would like to argue that an element of B([s]cd) has no hyper-
bolic faces. As before, it is convenient to consider segregated clasps, where here a
clasp is segregated if it is of the form 11...122...2, as well as reverse segregated
clasps of the form 22...211...1. In the By case, it is easy to enumerate the elements
of B([1]cd) if c is segregated and d is reverse segregated, as well as the elements
of B([2]cd) if c is reverse segregated and d is segregated. A web w in such a basis
web set cannot have negative curvature, and after removing bare strands, it is either
empty or the shape of its boundary is one of the following (possibly with c and d

switched):
c a eG
g d d

In the G2 case, the computation is again simpler if one of c and d is segregated and
the other is reverse segregated. No webs in B([1]cd) have any negative curvature,
but a web in B([2]cd) might have one negatively curved face, namely one with
three type 2 strands and one type 1 strand incident to it:

———

Cc
144
G Kuperberg
All other G2 webs in B([2]cd) are flat. An exhaustive enumeration of such webs in
both spiders verifies Eq. (7). The details are left to the reader.
Finally, in the G2 spider, unlike in the A2 and B2 spiders, web with a partly con-
vex clasp does not necessarily vanish in the clasped web space ^([si]^] 
[sn])
Recall that the clasped web space is defined as the subspace of the unclasped web
space W(s\s2 
sn) spanned by non-elliptic webs with non-convex clasps and no
internal type 2 edges, and that there is also a kernel /(|>i]|>2] 
[sn]) spanned by
webs w such that there is a cut path transverse to all edges of w which cuts off a
clasp of lower weight. In order to show that the G2 spider is well-defined, we need
the following lemma:
Lemma 6.11. The spaces I([s\][s2]'
in W(sιs2- 
sn).
[sn]) and W([s\][s2]" [sn]) are transverse
Proof. Rank the webs in W{s\s2 
—sn) first by the number of vertices, and second
by the sum of the weights of minimal cut paths cutting off each string Sf. We
consider a change of basis which is lower-triangular with respect to this ranking:
For each web w e W(s\s2 
-sn), choose a minimal cut path pt cutting off each 57 as
close as possible to the boundary. The cut paths are unique by the G2 analogue of
Lemma 6.6, and they cannot cross, although they could in principle share segments.
Recall the equation for a double edge from Eqs. (4), rearranged slightly:
1
-2
1
q + l + q -1 K
Applying this equation, we can convert every single edge contained in a path pi to
a transverse double edge; the other terms are all lower with respect to the ranking
of webs. This produces a new basis for W(s\s2 
sn) in which /([.SΊ]^] 
* [
sn])
and ^([silfe] 
[sn]) are manifestly complements. D
7. Explicit Formulas for A2 Clasps
Although internal clasps must exist by Sect. 5, the argument given there is too
indirect for practical computations. In this section, we give explicit formulas for A2
clasps. Note first that clasps are sent to each other by composition with H webs:
+ - 
+ -
K
Thus, it suffices to derive a formula for segregated clasps.
Spiders for Rank 2 Lie Algebras 145

Lemma 7.1. [fs is a segregated sign string and t* is another sign string of lower
or incomparable weight, then a basis web w € B(st) has either a “U” or a “Y”
attached to s.

Proof. The proof is also similar to that of Lemma 6.5. We assume the minimal
counterexample. First, the web w must be connected, for if a connected component
meets ¢ but not s, it may be discarded to produce a smaller counterexample; if it
meets s but not ¢, then it is a smaller counterexample; and if all components meet
both s and ¢, then one of them must be a smaller counterexample. Second, there
can be no “Y” or “H” attached at ¢, for otherwise they may be discarded to pro-
duce a smaller counterexample. (Note that a “U” attached to ¢ has already been
eliminated.)

Since w is non-elliptic, the total exterior curvature is at least 360°. Since there
is no “U,” “Y,” or “H” attached at ¢*, the total curvature along ¢ is at most 0°.
Moreover, unless w is a bare strand (which is not a counterexample), the two arcs
connecting s to ¢ have curvature at most 120°. By the hypothesis that s has no “Y,”
the curvature in each segregated segment of S is at most 0° also. Finally, since s
has no “U,” the curvature at the single arc connecting opposite signs of s is at most
60°, for a total of at most 300°, a contradiction:

By Lemma 7.1, if a web w € W(ss*) annihilates any “U” or “Y,” it satisfies
the annihilation axiom of a clasp. Moreover, among terms in w, only f, (the web
consisting solely of parallel strands) has the weight of s as its cut weight. Therefore
all other terms are annihilated by such w, and the annihilation property implies that
w is an idempotent under concatenation if the coefficient of the leading term B, is
1. Given these facts, an argument by induction (see Wenzl [24] and Ohtsuki and
Yamada [16]) establishes that

146 
G Kuperberg
recursively defines a clasp of weight nλ\, and a computation shows that
a+ 
b-
ks=0 
[a-k]\[b-k]\[a
a- 
b +
I I
α -
defines a segregated clasp of weight aλ\ + Z?A2
8. Applications and Problems
8.1. Higher rank. The main open problem related to the combinatorial rank 2 spi-
ders is how to generalize them to higher rank. A proper generalization would con-
sist of a complete set of generators and relations for the higher-rank spiders; the
strand sets would correspond to the fundamental representations and their tensor
products. It is easy to make a HOMFLY spider which corresponds to the HOM-
FLY polynomial, but this spider describes the invariant theory of An only in the
stable limit of large n\ the Λn web spaces for any fixed n are quotients of the
HOMFLY web spaces. (Recently, Murakami, Ohtsuki, and Yamada [15] have de-
fined the HOMFLY spider in terms of trivalent graphs; this is a step toward an
explicit description of the unstable truncation.) The generalization to a higher-rank
Lie algebra g, if it exists, would also likely involve formal angles related to the
Coxeter geometry of g; note that in both the Λ2 and B2 spiders, a trivalent ver-
tex is dual to a Weyl alcove. Note also that in all three rank 2 spiders, a large,
flat basis web (one with neither elliptic nor hyperbolic faces) coincides with the
Voronoi tiling of the plane given by the weight lattice of the corresponding Lie
algebra.
The bases given by the combinatorial rank 1 spider are dual to Lusztig's canoni-
cal bases [2]. Those of the rank 2 spiders are almost certainly also dual to canonical
bases or are closely related, because canonical bases have the same symmetry of
cyclic permutation of tensor factors, and because of the integrality and positivity
properties of the coefficients in Eqs. (2), (3), and (4).
8.2. Generalized βj symbols. Given four webs wi, W2, W3, and w4 and six clasps
en, C13, c\4, c23, c24, and C34 in some spider, their tetrahedron symbol is defined as
the value of the compound web
Spiders for Rank 2 Lie Algebras
147
provided that the four webs w, are members of the appropriate clasped web spaces.
The tetrahedron symbol is closely related to the 67 symbol, which expresses the
change of basis from
®W(cl2cnCi4)ί
to
via the identification of both with W(c\2c\3C4iC42), where in general c^ — c*;. Up
to normalization, the A\ tetrahedron symbol at q = 1 equals the Racah-Wigner 6/
symbol used in mathematical physics [14]. Using the A\ spider, Masbaum and Vogel
have found a new proof of the Racah formula for the 67 symbol and its quantum
generalization [12]. The combinatorial rank 2 spiders could be equally useful for
understanding the rank 2 generalization of the 67 symbol.
8.3. Practical computation of rank 2 link invariants. If one is interested in
computing link invariants, Eqs. (2), (3), and (4) can be interpreted as inductive
rules for evaluating links and knotted graphs without boundary in the web space
Wφ). Mollard [13] and Sinha [19] have independently written computer implemen-
tations of this algorithm for G2, and there are well-known computer programs to
compute the Jones, HOMFLY, and Kauffman polynomials using the same basic
strategy.
Spiders suggest an alternative method for computing the same invariants which
is more efficient than a direct application of the above rules to closed links and
graphs. The method consists of assembling a link projection, as a web, from
indiviual crossings using spider operations, and reducing intermediate webs to linear
combinations of basis webs. For example, to evaluate the quantum A\ link invariant
(the Jones polynomial) of a figure eight knot, we can decompose the knot as a
148
G. Kuperberg
nested sequence of three tangles a, b, and c:
We recall some basic identities in the A\ spider:
O-
X = -q
/ O - <?
3/4
The tangle a is a right-handed crossing. Its expansion leads to an expansion of the
tangle b:
