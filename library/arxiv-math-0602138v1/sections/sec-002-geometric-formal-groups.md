---
doc_id: arxiv-math-0602138v1
doc_title: "Non-Commutative Formal Groups in Positive Characteristic"
section_id: sec-002-geometric-formal-groups
section_title: "Geometric Formal Groups"
section_number: null
pages: 16-24
source_pdf: 0602138v1.pdf
source_sha256: ed9ade66a774c93e
toc_source: outline
doc_brief: "Non-Commutative Formal Groups in Positive Characteristic — We describe geometric non-commutative formal groups in ter ms of a ge- ometric commutative formal group with a Poisson structure o n its"
---
Although (Prop. 2.4) gives some reasonable control on the algebra structure of
Dist(G), some diﬃculties remain in trying to characterize formal groups in s uch
a manner. First, our construction depended on the choice of an or dered coor-
dinate system. Second, we have yet to address the DVPS-co-alge bra structure
and its compatibility with the algebra structure. For this, we will need to make
an assumption on G, namely that it is “geometric” which loosely means that
one can choose a coordinate system of commutative formal subgr oups. One may
think of this as specifying a “local abelian structure”. In the case w here the
ground ring is a ﬁeld of characteristic zero, the fact that any comm utative formal
group is isomorphic to a product of Ga’s means that there is essentially one local
16
abelian structure. However, in the positive characteristic situatio n, there are
non-isomorphic (commutative) one-dimensional formal groups. M oreover, there
are commutative formal groups which are not the products of one -dimensional
formal groups, even over an algebraically closed ﬁeld.
Deﬁnition 3.1.
3.1.1. Let G be a formal group over R. We say that G is geometric if there are
commutative formal subgroups Hi for i in some indexing set I such that
there is an isomorphism as between G and the product of formal varieties∏
i Hi. We denote a geometric formal group by the data {Hi
⊂ ιi✲ G}i∈I,
or more brieﬂy {Hi, G}i∈I.
3.1.2. A morphism of geometric formal groups:
{Hi, G}i∈I
Φ✲ {H′
j, G′}j∈J
is a morphism of formal groups G
Φ ✲ G′ such that for each i ∈ I
there is some ji ∈ J and some morphism of commutative formal groups
Hi
Φ ji✲ H′
j such that Φ is the morphism induced by the UMP of products
of formal varieties as in the following diagram:
Hi
⊂
ιi ✲ G
H′
ji
Φ ji ❄
G′
ιji ❄✛
∃!
3.1.3. Let {Hi, G}i∈I be a geometric formal group over R. We deﬁne the un-
derlying commutative geometric group as:
Comm(Hi, G) := {Hi, H}
where H := ∏
i Hi is the underlying commutative group and the
product is taken in the category of commutative formal groups.
3.1.4. Let {Hi, G}i∈I be a geometric formal group over R. Let di := dim Hi
and denote by abuse of notation I = |I|, so that we may identify I =
{1, · · · |I|}. Suppose that for each i ∈ I, we have chosen an ordered co-
ordinate system xi,< i = {xi, 1 <i · · · <i xi,d i }. Let us suppose moreover
that we have chosen an ordering < on I. We will call the resulting ordered
coordinate system:
x≪ := {x1, 1 ≪ · · · ≪ x1,d 1 ≪ x2, 1 ≪ · · · xI, 1 ≪ · · · ≪ xI,d I }
=: {x1 ≪ · · · ≪ xn}
17
a geometric coordinate system . We will call the data:
{x≪, Hi, G}i∈I
a geometric formal group law .
Remark 3.2.
3.2.1. Suppose that {Hi, G} is a geometric formal group. Then, each of the
Dist(Hi) carries its own co-multiplication map, say ∆ i, as well as H with
its co-multiplication ∆. However, as we have assumed an isomorphism
of formal varieties G = ∏
i Hi, we have an isomorphism of co-algebras
Dist(Gi) =∏
i Dist(Hi) under which we have ∆ = ∏
i ∆ i.
3.2.2. One sees that the Dist(Hi) are sub-bi-algebras of Dist(G) which gen-
erate Dist(G) as an algebra. The choice of the commutative formal sub-
groups Hi are not unique and, in particular, in positive characteristic may
not be isomorphic.
Example 3.3.
3.3.1. If G is a commutative formal group, then it is geometric with I = {1}
and H1 = G.
3.3.2. Suppose that G is a connected and simply-connected Lie group over a
ﬁeld k. If g is the Lie algebra of G as in (Ex. 2.1.1), then for any
choice of basis k⟨Xi⟩ we can exhibit the formal completion of G as a ge-
ometric formal group via the formal completions of the Lie subgrou ps
Hi = exp(tXi). We have that the Dist(Hi) are exactly the sub-bi-
algebras S{Xi} = Dist(Hi) of Ug = Dist(G). In particular, in char-
acteristic zero all formal groups are geometric.
3.3.3. If k is an algebraically closed ﬁeld of positive characteristic p, then the
formal completion of any reductive algebraic group is geometric with for-
mal subgroups either Ga or Gm.
3.3.4. In general, we may have more than one type of a multiplicative coor-
dinate. For example, consider in the case of SL2, we have coordinates
(w, x, y ) of type ( Ga, Gm, Ga) given by:
( 1 + x y
w 1 + z
)
where 1+ z = 1+yw
1+x . We also have coordinates ( s, t, u ) of type ( Ga, Ga, Ga)
given by: (
1 0
s 1
)(
1 + t t
−t 1 − t
)(
1 u
0 1
)
.
18
Remark 3.4. Let R = k be a ﬁeld of positive characteristic. Let {x≪, Hi, G}i∈I
be a geometric formal group law. We may apply (Prop. 2.4) to each of the
commutative formal subgroups Hi. If we deﬁne for i ∈ I:
Xi := {δxpr
i,k
| 1 ≤ k ≤ di r ≥ 0}
then X = ∐
i Xi. Fixing an ordering < on I, let us write ιx≪ := ι≪ and
˜πx< := ˜π≪ if there is no danger of confusion. As the Hi’s are commutative
formal subgroups, we have that:
F (Xi) ⊆ Dist(Hi)
in other words:
fη ⊆ TXi ⊆ TX ∀ η ∈ X i.
Further, we have that for η, ζ ∈ X i that:
gη,ζ = ηζ − ζη ∈ TXi ⊆ TX
Lemma 3.5. Let us adopt the notation and assumption of (Rmk. 3.4). Then
˜π≪ descends to a strongly ﬁltered, strongly multiplicative Po isson structure π≪
on the splay T of the Dist(Hi).
Proof. By the presentation of Dist(G) as given in (Prop. 2.4), and since we
have ˜π≪(Xi, Xi) = 0, we see that ˜ π≪ descends as we may present T as:
T = TX /
∑
i
(fη , g η,ζ | η, ζ ∈ X i) .
The internal symmetry follows. The strong ﬁltration property follo ws by (Rmk.
2.3.2). As Dist(G) is in fact a bi-algebra, one has by (Rmk. 3.2) the strong
multiplicativity.
Proposition 3.6. Let k be a ﬁeld of characteristic p > 0. Let {Hi, G}i∈I be
a geometric formal group over k. Suppose that x≪ (resp. x′
≪′ ) is a geometric
coordinate systems on G induced by the choice of an ordering < (resp. <′) on I
and ordered coordinate systems xi,< i (resp. x′
i′,< ′
i
) on the Hi. Let π (resp. π ′)
be the resulting Poisson structure on T as in (Lem. 3.5). Then π and π ′ are
equivalent. In particular if <=<′, then Φ = 1 1.
If {Hi, G}i∈I
Φ✲ {H′
j, G′}j∈J is a morphism of geometric formal groups, then
there is an induced Poisson morphism T
Φ✲ T
′
.
Proof. Let us ﬁrst suppose that we are working with a ﬁxed ordering <=<′ on
I. Denote by Φ i the isomorphisms:
Dist(Hi) = k⟨δ
Ji
xi ⟩
Φ i✲ k⟨δ
J ′
i
x′
i
⟩ = Dist(Hi)
19
given by the choices of the two multiplicative bases for the Dist(Hi). Adopting
the notation of (Lem. 2.4) for each of the coordinate systems, we denote the
respective generating sets by X = ∐ Xi and X ′ = ∐ X ′
i . The choice of the
diﬀerent coordinate systems gives two diﬀerent presentations of T as:
T = TX / R +
∑
i
(ηζ − ζη | η, ζ ∈ X i)
T = TX ′/ R′ +
∑
i
(η′ζ′ − ζ′η′ | η′, ζ ′ ∈ X i)
The Φ i induce an isomorphism between these two presentations. The Poiss on
structures under consideration π and π ′ are induced respectively from:
˜π := ι◦ πc for Dist(G) ⊂ ι✲ TX
˜π := ι′ ◦ πc for Dist(G) ⊂ ι′
✲ TX ′.
Our aim is to show that Φ ◦ π = π ′ ◦(Φ ⊗ Φ). First we suppose that we have
ﬁxed coordinate systems xi = xi′ on each of the Hi so that we have only chosen
to change the ordering of <i to <′
i. As the induced multiplicative expansions
of Dist(G) are equal up to recordings within each of the Xi, we see that the
induced map Φ simply induces a change of ordering of the monomials in th e Xi.
The result follows in this setting.
Let us drop the assumption that xi = x′
i. By what we have just said, after a
possible reordering of the coordinates for each of the Dist(Hi), we may assume
that that the orderings <i and <′
i are the same. Recalling that π and π ′ are
deﬁned in terms of πc, where we have:
Φ ◦ πc(η, ζ ) = Φ( η)Φ( ζ) − Φ( η)Φ( ζ)
= πc(Φ( η), Φ( ζ))
the result now follows by (Lem. 1.7), by noticing that the multiplicative expan-
sion of Dist(G) in terms of the coordinates x′ can be obtained from multiplica-
tive expansion of x′ by applying Φ and the relations R′.
Now we only need to illustrate the eﬀect of a change of ordering < on I to
<′. Let us suppose that the ordering < is the usual ordering 1 < 2 < · · · < |I|.
Then, we may view any other ordering <′ on I as being given by <′=<σ for some
permutation σ ∈ Σ I . As the permutations are generated by the transpositions,
we only need consider the case σ = ( i i + 1). In this case, we consider the
automorphism Φ of T induced by Dist(Hj)
Φ j✲ Dist(Hj) where:
Φ j =
{ invj j ∈ {i, i + 1}
1 1 otherwise .
Here, invj is the inverse of Hj. The fact that this gives an equivalence of Poisson
structures follows from the fact that inv is an anti-algebra homomorphism so
20
that for η, ζ ∈ X i ∪ Xi+1:
inv ◦ πc(η, ζ ) = inv(ηζ − ζη)
= inv(η) inv(ζ) − inv(ζ) inv(η)
= πc(inv(ζ), inv(η)).
To obtain the morphism T
Φ ✲ T
′
, we ﬁrst choose an ordering <′ on the
set J. Then we may choose any ordering < on I such that if i1 < i 2 then
ji1 <′ ji2 where the ji’s are as in the deﬁnition of a geometric morphism.
We note that such an ordering exists: We ﬁx a choice of such ji’s and deﬁne
Ij := {i ∈ I | ji = j}. Then as we have I =∐
j∈J Ij , we choose any ordering
<j on the Ij and deﬁne the ordering < on I as i1 < i 2 if either ji1 < j i2 or
j := ji1 = ji2 and i1 <j i2. The result follows readily.
Theorem 3.7. Let {Hi, H} be a commutative geometric formal group. Suppose
that π is a strongly ﬁltered, strongly multiplicative Poisson str ucture on the splay
T of the Dist(Hi). Let J be the ideal in the splay algebra T :
J = (f g − gf − π (f, g ) | f, g ∈ T ).
Then the quotient:
U := T / J
is the distribution algebra of a formal group, G. Moreover, {Hi, G} is a geomet-
ric formal group.
Suppose that T
′
is the splay of a commutative geometric formal group {H′
i, H′}
with a strongly ﬁltered, strongly multiplicative Poisson s tructure π ′. Suppose
that T
Φ✲ T is a Poisson morphism, then there is morphism of geometric
formal groups {Hi, G}
Φ✲ {H′
i, G′}.
Proof. Let us choose an ordering < on I. By the work that we have done in §1
we have a bi-algebra structure on U . Thus, we only need to show that there is
a DVPS algebra structure on U . Let us write:
{x1 ≪ · · · ≪ xn} := {x1, 1 ≪ · · · ≪ x|I|,d |I|}.
For a multi-index J, we deﬁne the following element of U :
δxJ := δxJ1
1
· · · δxJnn
.
If 1 ≤ j ≤ n, let ij ∈ I denote the index such that xj is a coordinate of Hij .
21
Then, as we have taken care of the ordering, and by (Rmk. 3.2), we have:
∆( δxJ ) = ∆ i1 (δxJ1
1
) · · · ∆ in (δxJnn
)
=
( ∑
a1+b1=J1
δxa1
1
⊗ δxb1
1
)
·
( ∑
an+bn=Jn
δxann ⊗ δxbnn
)
=
∑
aj +bj =Jj
δxa1
1
· · · δxann ⊗ δxb1
1
· · · δxbnn
=
∑
A+B=J
δxA ⊗ δxB
as desired. The fact that Φ is a morphism of formal groups is now obv ious.
Example 3.8. We wish to take some time to describe the relevant features of
the above theory in terms of the formal group corresponding to T2, the upper
triangular 2 × 2 matrices of determinant one. Let us choose a coordinate system
as follows: (
1 + x y
0 (1 + x)−1
)
by this we mean that the co-multiplication laws, in these coordinates, are given
by:
x
m✲ x ⊗ 1 + 1 ⊗ x + x ⊗ x
y
m✲ (1 + x) ⊗ y + y ⊗(1 + x)−1
= (1 + x) ⊗ y + y ⊗(1 − x + x2 − x3 + · · · ).
Then x and y are geometric coordinates for the subgroups Gm and Ga, respec-
tively. Although we know that the underlying commutative group is giv en by
Gm × Ga, the PBW-theorem gives in fact a diﬀerent set of coordinates for t his
group. Here, we need to consider the two choices of orderings x < y and x > ′ y,
and then a calculation shows that the resulting PBW-coordinates ar e:
( 1 + x y
0 (1 + x)
) ( (1 + x)−1 y
0 (1 + x)−1
)
x < y x > ′ y.
We give a complete description of T2. From the commutative theory, one
knows that for Gm we have δp
xpr = δxpr and for Ga we have δp
ypr = 0, thus we
22
only need concern ourselves with the commutator relations. Thus w e compute:
δxpr · δyps =
∑
a,b ≥0
⟨m(x)am(y)b, δ xpr ⊗ δyps ⟩δxayb
=
∑
a,b ≥0
⟨(x ⊗ 1)a(1 ⊗ y + x ⊗ y)b, δ xpr ⊗ δyps ⟩δxayb
=
∑
a,b ≥0
⟨
b∑
b′=0
( b
b′
)
xa+b′
⊗ yb, δ xpr ⊗ δyps ⟩δxayb
=
{ δxpr yps r < s
δxpr yps + δxpr−ps yps r ≥ s.
A similar computation shows:
δyps · δxpr =
∑
0≤k≤pr−s
(−1)kδxpr−kps yps
so that we have as commutator:
πc(δxpr , δ yps ) =
{ 2δxpr−ps yps −∑
2≤k≤pr−s (−1)kδxpr −kps yps r ≥ s
0 r < s.
We note that the calculation is valid even for p = 2. The 2 in the commutator
reﬂects the fact that the Lie algebra of T2 is abelian for p = 2.
Finally, we need to express πc in multiplicative coordinates. Taking x < y ,
we only need to apply the following relation recursively:
δxpr δxmyps = ( mr + 1)δxm+pr yps + mrδxmyps
+
∑
m≤k≤pr −ps
( k
k − m
)( m
m + pr − ps − k
)
δxkyps .
Here, m = m0 + · · · mrpr is the p-adic expansion of m where we assume that
mr < p − 1.
References
[1] Braverman, A; Gaitsgory, D; “The Poincare-Birkhoﬀ-Witt theo rem for
quadratic algebras of Koszul type.” hep-th/9411113.
[2] Demazure, M; Gabriel, P; “Introduction to algebraic geometry a nd al-
gebraic groups.” North-Holland Mathematics Studies, 39 North-Holland
Publishing Co., Amsterdam-New York, 1980.
[3] Dieudonn´ e, J; “Introduction to the theory of formal groups .” Pure and
Applied Mathematics, 20 Marcel Dekker, Inc., New York, 1973.
[4] de Graaf, W; “Lie algebras: theory and algorithms.” North-Holland Math-
ematical Library, 56 . North-Holland Publishing Co., Amsterdam, 2000.
23
[5] Fløystad, G; Vatne, J; “PBW-deformations of N-Koszul algebr as.”
math.RA/0505570.
[6] Hazewinkel, M; “Formal groups and applications.” Pure and Applied
Mathematics, 78 Academic Press, Inc. [Harcourt Brace Jovanovich, Pub-
lishers], New York-London, 1978.
[7] Helsloot, I; “Covariant Formal Group Theory and Some Applicatio ns.”
Centrum voor Wiskunde en Informatica Tract 111 Stichting Mathema-
tisch Centrum, Amsterdam, 1991.
[8] Jantzen, J C; “Representations of algebraic groups.” Mathematical Sur-
veys and Monographs, 107 American Mathematical Society, Providence,
RI, 2003.
[9] Korogodski, L; Soibleman, Y; “Algebras of Functions on Quantum
Groups.” Mathematical Surveys and Monographs, 56 American Math-
ematical Society, Providence, RI, 1998.
[10] Lazard, M; “Commutative Formal Groups.” Lecture Notes in Mathemat-
ics, 443 Springer-Verlag, New York, 1975.
[11] Leitner, F; Pawloski, R; “Unital Gr¨ obner Bases over Arbitrar y Commu-
tative Rings.” math.RA/0409565.
[12] Li, H; “Noncommutative Gr¨ obner Bases and Filtered-Graded T ransfer.”
Lecture Notes in Mathematics, 1795 Springer-Verlag, New York, 2002.
[13] Lu, J-H; Weinstein, A; “Poisson Lie Groups, Dressing Transfor mations,
and Bruhat Decompositions.” Journal of Diﬀerential Geometry 31 (1990),
501–526.
[14] Manin, Y; “Theory of commutative formal groups over ﬁelds of ﬁnite
characteristic.” Uspehi Mat. Nauk 18 (1963) no. 6 (114), 3–90.
[15] Mora, T; “An Introduction to Commutative and Noncommutativ e Gr¨ obner Bases.”
Theoretical Computer Science 134 (1994), 131–173.
[16] Serre, J-P; “Lie algebras and Lie groups. 1964 lectures given a t Harvard
University.” W. A. Benjamin, Inc., New York-Amsterdam 1965
24
