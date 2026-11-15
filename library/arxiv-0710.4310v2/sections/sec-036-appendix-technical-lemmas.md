---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-036-appendix-technical-lemmas
section_title: "Appendix: Technical Lemmas"
section_number: null
pages: 43-46
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Appendix: Technical Lemmas
The following lemmas provide the foundation for the construction of the 2-
category S2(M), deﬁned for any smooth manifold M. Speciﬁcally, lemma 52 is
used to prove that the vertical composition of 2-tracks is well deﬁned; see 1.3.3.
Lemma 51 Let M be a smooth manifold. Let f : S2 →M be a smooth map.
Consider a handle decomposition H of M. Let Hi be the i-skeleton of H; in
other words Hi is the handlebody made from the handles of H of index less than
or equal to i, where i = 0, 1, . . . , dim(M). There exists an ambient isotopy of
M, sending H to a handle decomposition I of M, such that f(S2) ⊂I2, the
2-skeleton of the handle decomposition I.
Proof. Let m = dim(M).
Let J be the handle decomposition of M which is dual to H. If m = 2 there
is nothing to prove. Otherwise f(S2) is a compact set with zero measure in M,
by Sard’s theorem; see [H]. Therefore, there exists an ambient isotopy of M,
sending J to a handle decomposition J0 of M, such that the 0-handles of J0
are contained in M \ f(S2), a non-empty open set of M. If m = 3, taking the
dual handle decomposition of J0, yields a handle decomposition I of M with
f(S2) ⊂I2.
Suppose that m > 3. Let {h1
i } be the set of handles of J0 of index 1. Then
each 1-handle h1
i is of the form h1
i = D1
i × Dm−1
i
, and attaches to the 0-skeleton
J0
0 of J0 along S0
i × Dm−1
i
.
For each i, let p1
i : h1
i →Dm−1
i
be the obvious
projection.
Here Dm is the m-disk.
Then p1
i can be extended to a smooth
map q1
i : V 1
i
→Rm−1, where V 1
i
is an open neighbourhood of h1
i in M. For
each i, let A1
i = f −1(V 1
i ) ⊂S2. It is an open set in S2. Since m −1 > 2,
the set (q1
i ◦f)(A1
i ) ⊂Rm−1 has measure zero, for q1
i is smooth. Therefore
p1
i (f(S2)) ⊂(q1
i ◦f)(A1
i ) has measure zero in Dm−1
i
.
Choose an (m −1)-ball cm−1
i
⊂Dm−1
i
, not intersecting p1
i (f(S2)); note that
p1
i (f(S2)) is compact. There exists an ambient isotopy of M, which restricts
to an ambient isotopy of J0
0 (the 0-skeleton of J0), whilst sending each h1
i =
D1
i ×Dm−1
i
to D1
i ×cm−1
i
. Let J1 be the handle decomposition of M to which J0
is sent by the ambient isotopy. By construction J1
1 ∩f(S2) = ∅. If dim(M) = 4,
43
taking the dual handle decomposition to J1, yields the handle decomposition I
of M, and by construction f(S2) ⊂I2.
Suppose m > 4. The argument is the same. As above, let {h2
i } be the set
of 2-handles of J1. Then, for any i, h2
i = D2
i × Dm−2
i
, and h2
i attaches to J1
1
along S1
i × Dm−2
i
. For each i, let p2
i : h2
i →Dm−2
i
be the obvious projection.
As before, since m −2 > 2, the set p2
i (f(S2)), which is compact, has zero
measure in Dm−2
i
. Therefore, there exists an (m −2)-ball cm−2
i
⊂Dm−2
i
such
that p2
i (f(S2)) ∩cm−2
i
= ∅. There exists an ambient isotopy of M, restricting
to an ambient isotopy of J1
1, and sending h2
i = D2
i × Dm−2
i
to D2
i × cm−2
i
, for
each i. Let the handle decomposition J2 be the image of J1 under the ambient
isotopy. As before, by construction, J2
2 ∩f(S2) = ∅. If m = 5, letting I be the
handle decomposition of M dual to J2, then we have that f(S2) ⊂J2.
An obvious inductive argument will ﬁnish the proof for any m ∈N.
Lemma 52 Let f : ∂(D3) →M be a smooth map such that Rank(Dvf) ≤
1, ∀v ∈∂(D3). Here D3 = [0, 1]3. Suppose that f is constant in a neighbourhood
of each vertex of ∂(D3).
In addition, suppose also that in a neighbourhood
I × [−ǫ, ǫ] of each edge I of ∂(D3), f(x, t) = φ(x), where (x, t) ∈I × [−ǫ, ǫ] and
φ: I →M is smooth. Then f can be extended to a smooth map F : D3 →M
such that Rank(DwF) ≤2, ∀w ∈D3. Moreover we can choose F so that it has
a product structure close to the boundary of D3.
Proof. The conditions of the statement imply that f is of the form f ′ ◦r,
where f ′ : S2 →M is a smooth map and r: ∂(D3) →S2 is some smooth
homeomorphism.
By using the previous lemma, we can see that there exists a handle decom-
position of M such that f(∂(D3)) is contained in the 2-skeleton M 2 of M (the
handlebody made from the 0-,1- and 2-handles of M). Let us prove that we can
suppose further that f(∂(D3)) is contained in the 1-skeleton M 1 of M. This
will be completely analogous (though dual) to the proof of the previous lemma.
Let n = dim(M). Suppose that n ≥2. Let {hi} be the set of 2-handles
of M. Therefore, for each i, hi = D2
i × Dn−2
i
, and hi attaches to M 1 along
S1
i × Dn−2
i
= (∂D2
i ) × Dn−2
i
. It suﬃces to prove that for each i there exists an
xi ∈D2
i (thus an open 2-ball) such that f(∂D3) does not intersect {xi} × Dn−2
i
.
Let pi : hi = D2
i × Dn−2
i
→D2 × {0} be the obvious projection. Given that
Rank(Dvf) ≤1, ∀v ∈∂D3, it follows that Zi = pi(hi∩f(∂D3)) has zero measure
in D2, thus that we can choose an xi in the interior of D2 not intersecting Zi.
Therefore, some open ball in D2 containing xi does not intersect Zi. This proves
that there exists a handle decomposition of M such that f(∂D3) is contained in
the interior of the 1-skeleton M 1 of M, analogously to the proof of the previous
lemma.
Consider the universal cover N
p−→M 1 of M 1. It is a contractible smooth
manifold. We can lift f as f = p ◦g′, where g′ : ∂D3 →N is a smooth map,
such that Rank(Dvg′) ≤1, ∀v ∈∂D3, since p is a local diﬀeomorphism. Let
c: N ×[0, 1] →N be a smooth contraction of N to a point of it. We can suppose
that there exists an ǫ > 0 such that c does not depend on t for t ∈[0, ǫ]∪[1−ǫ, 1].
44
The smooth homotopy g(v, t) = p(c(g′(v), t)) where t ∈[0, 1] and v ∈∂(D3) will
permit us to extend f : ∂(D3) →M to a smooth map F : D3 →M, with a
product structure close to the boundary of D3. By construction we also have
that Rank(DwF) ≤2, ∀w ∈D3.
References
[B]
Baez J.C.: Higher Yang-Mills Theory, arXiv:hep-th/0206130.
[BC] Baez J.C.; Crans A.S.: Higher-dimensional algebra. VI. Lie 2-algebras.
Theory Appl. Categ. 12 (2004), 492–538 (electronic)
[BL] Baez J.C.; Lauda A.D.: Higher-dimensional algebra. V. 2-groups. Theory
Appl. Categ. 12 (2004), 423–491 (electronic)
[BS]
Baez J.C.; Schreiber U.:
Higher Gauge Theory:
2-Connections on
2-Bundles. arXiv:hep-th/0412325;
see also:
Higher Gauge Theory,
arXiv:math/0511710; Categories in algebra, geometry and mathematical
physics, 7–30, Contemp. Math., 431, Amer. Math. Soc., Providence, RI,
2007
[BM] Barrett J.W.; Mackaay M.: Categorical representations of categorical
groups. Theory Appl. Categ. 16 (2006), No. 20, 529–557 (electronic).
[BT] Bott R.; Tu L.: Diﬀerential forms in algebraic topology. Graduate Texts
in Mathematics, 82. Springer-Verlag, New York-Berlin, 1982.
[BrMe] Breen L.; Messing W.: Diﬀerential geometry of gerbes. Adv. Math. 198
(2005), no. 2, 732–846.
[Br]
Brown K.S.: Cohomology of groups. Corrected reprint of the 1982 original.
Graduate Texts in Mathematics, 87. Springer-Verlag, New York, 1994.
[BHKP] Brown R.; Hardie K. A.; Kamps K. H.; Porter T.: A homotopy double
groupoid of a Hausdorﬀspace. Theory Appl. Categ. 10 (2002), 71–93
(electronic).
[BH] Brown R., Higgins P.J.: On the connection between the second relative
homotopy groups of some related spaces. Proc. London Math. Soc. (3) 36
(1978), no. 2, 193–212.
[BHS] Brown R., Higgins P.J., Sivera R.: Nonabelian algebraic topology, (in
preparation). Part I downloadable.
[BMo] Brown R.; Mosa G.H.: Double Categories, 2-Categories, Thin Struc-
tures and Connections. Theory Appl. Categ. 5 (1999), No. 7, 161-275
(electronic).
[CP] Caetano A.; Picken R. F.: An axiomatic deﬁnition of holonomy. Internat.
J. Math. 5 (1994), no. 6, 815–848.
45
[EML] Eilenberg S, MacLane S.: Determination of the Second Homology and
Cohomology Groups of a Space by Means of Homotopy Invariants, Proc.
Nat. Acad. Sci. U. S. A. 12, (1946). 277–280.
[HKK] Hardie K. A.; Kamps K. H.; Kieboom R. W.: A Homotopy 2-Groupoid
of a HausdorﬀSpace. Papers in honour of Bernhard Banaschewski (Cape
Town, 1996). Appl. Categ. Structures 8 (2000), no. 1-2, 209–214.
[H]
Hirsch M.W.: Diﬀerential topology. Graduate Texts in Mathematics, No.
33. Springer-Verlag, New York-Heidelberg, 1976
[K]
Knapp A.W.: Lie groups beyond an introduction. Progress in Mathemat-
ics, 140. Birkhuser Boston, Inc., Boston, MA, 1996.
[KH] Khokhlov Yu. S.: Stable distributions on the Heisenberg group. Stability
problems for stochastic models. J. Soviet Math. 47 (1989), no. 5, 2796–
2798.
[KN] Kobayashi S.; Nomizu K.: Foundations of diﬀerential geometry. Vol I. In-
terscience Publishers, a division of John Wiley & Sons, New York-London
1961.
[ML] Mac Lane S.: Categories for the working mathematician. Second edition.
Graduate Texts in Mathematics, 5. Springer-Verlag, New York, 1998.
[MP] Mackaay M.; Picken R.F.: Holonomy and parallel transport for abelian
gerbes. Adv. Math. 170 (2002), no. 2, 287-219.
[M]
Mackaay M.: A note on the holonomy of connections in twisted bundles.
Cah. Topol. G´eom. Diﬀ´er. Cat´eg. 44 (2003), no. 1, 39–62.
[P]
Porter T.: Crossed modules in Cat and a Brown-Spencer theorem for 2-
categories. Cahiers Topologie G´eom. Diﬀ´erentielle Cat´eg. 26 (1985), no.
4, 381–388.
[Po]
Postnikov, M.: Le¸cons de G´eometrie. (French) [Lectures in geometry]
G´eom´etrie Diﬀ´erentielle. [Diﬀerential geometry] Translated from the Rus-
sian by Irina Petrova. Traduit du Russe: Math´ematiques. [Translations of
Russian Works: Mathematics] ´Editions Mir, Moscow, 1990.
46
