---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-011-44-higher-order-expansion-for-free-cumulants
section_title: "Higher order expansion for free cumulants"
section_number: 4.4
pages: 33-42
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
present a method of enumerating all evercrossing partition s with a given
genus. The main concept is to simplify a given evercrossing p artition by
a number of steps. After these simpliﬁcations we obtain an ev ercrossing
pair partition (with some extra properties) which can be enu merated eas-
ily. By reversing the process of simpliﬁcations we shall therefore obtain all
evercrossing partitions with a given genus.
4.4.1. Simpliﬁcation, step 1. Let an evercrossing partition be given. In the
ﬁrst step we remove all its trivial blocks. For example, Figu re 4.3 depicts
the outcome of this step performed on an evercrossing partition from Figure
4.1. In fact we do not really care what are the labels of vertices and it would
be a good idea not to write them down at all; in this example we d o write
them down for the reason of clarity.
4.4.2. Simpliﬁcation, step 2. In the second step of simpliﬁcation, we con-
sider the fat partition corresponding to the outcome of the ﬁ rst step (cf ex-
ample on Figure 4.4). In other words, we perform the operation depicted on
Figure 4.5 on each of the blocks.
4.4.3. Simpliﬁcation, step 3. The outcome of the second step is a pair par-
tition. In the third step of the simpliﬁcation algorithm we p erform the op-
eration depicted on Figure 4.6. To be precise: for n ≥ 2 let (p1, . . . , p n)
34 PIOTR ´SNIADY
FIGURE 4.4. Partition from Figure 4.1 after the second step
of the simpliﬁcation algorithm.
FIGURE 4.5. Elementary operation of step 2 of the simpli-
ﬁcation algorithm: one of the blocks is replaced by its fat
version.
and (qn, q n− 1, . . . , q 1) be two sequences of consecutive vertices of this
pair partition such that pk is connected with qk. We remove all vertices
p2, p 3, . . . , p n, q 2, q 3, . . . , q n and leave vertices p1 and q1 unchanged. We
iterate this removal of vertices as long as it is possible (cfexample on Figure
4.7).
A careful reader might observe that after rotating the Figur e 4.6 upside–
down the roles played by p1, q1 are interchanged with qn and pn therefore
the above rule is not very precise which labels should be carr ied by the
vertices of the surviving block; but in fact we do not really care about these
labels. In particular, we do not care which of the labels is th e smallest,
therefore we identify pair partitions which are cyclic rotations of each other.
4.4.4. Outcome of the simpliﬁcation algorithm.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 35
FIGURE 4.6. The elementary operation of step 3 of the sim-
pliﬁcation algorithm: a number of parallel lines is replace d
by a single one.
FIGURE 4.7. The outcome of the step 3 of the simplifying
algorithm for partition from Figure 4.1.
Theorem 4.10. The outcome of the simpliﬁcation algorithm from Sections
4.4.1–4.4.3 is an evercrossing pair–partition which has the same genus and
free index as the original partition.
Let n denote the number of vertices of the outcome pair partition π. If
genusπ ⁄= 0 then
(4.15) n ≤ 12 genusπ − 6.
Proof. In order to show that all three steps of the simpliﬁcation alg orithm
preserve the genus of a partition, it is enough to notice that the surface
without the boundary we constructed in Section 3.1.3 change s in each of
the steps into a homeomorphic one.
We shall prove now that all three steps preserve the free inde x of a par-
tition. Let π be a partition of some set X, let x / ∈ X, then π ′ = π ∪ {x}is
36 PIOTR ´SNIADY
a partition of the set X ∪ {x}which has an additional trivial block. Observe
that every partition ρ ′ ≤ π ′ must have a form ρ ′ = ρ ∪
{
{x}
}
where ρ ≤ π.
Therefore
Iπ ′ =
∑
ρ ′∈NC(X∪{x})
ρ ′≤π ′
Moebρ ′ =
∑
ρ∈NC(X)
ρ≤π
Moebρ = Iπ .
It follows that two partitions which differ with one trivial block have the
same free index and, by iterating, the ﬁrst step preserves the free index.
The second and the third step can be divided into a number of elementary
operations (for the second step the elementary operation is the replacement
of only one of the blocks of the original partition by the corr esponding ‘fat
block’, cf Figure 4.5, for the third step the elementary operation is the per-
formance of only one operation from Figure 4.6). Our goal is t o prove that
every elementary operation preserves the free index. Let π be a partition
and let π ′ be an outcome of one of the elementary operations performed on
π. We can decompose π = σ ∪ τ, π ′ = σ ′ ∪ τ (we use the notations of
Lemma 4.6), where τ ∈ P(T ) is the set of blocks of π not changed by the
elementary operation. One can easily check that for both elementary opera-
tions σ ∈ NC(S) and σ ′ ∈ NC(S ′) are non–crossing partitions, furthermore
for every ρ ∈ P(T ) we have that (σ ∧ ρcomp) ∈ NC(S) is trivial if and only
if (σ ′ ∧ ρcomp) ∈ NC(S ′) is trivial. From Lemma 4.6 applied to π and π ′ it
follows that
Iπ =
∑
ρ∈NC(T),
ρ≤τ,
(σ ∧ ρcomp) is trivial
Moebρ =
∑
ρ∈NC(T),
ρ≤τ,
(σ ′∧ ρcomp) is trivial
Moebρ = Iπ ′
and hence both elementary operations preserve the free index.
Observe also, that the ﬁrst and the third step of the algorith m preserve
clearly the partition property of being evercrossing. It should be clear from
the graphical interpretation that also the second step preserves this property;
nevertheless we provide a more detailed proof below. Let a partition π be an
outcome of the ﬁrst step of the algorithm. Any pair connected by π fat must
be of the form (π ′
s,t , π s,t +1) (we use the notation from Section 2.2.2). As an
outcome of the ﬁrst step of the simpliﬁcation algorithm,π contains no trivial
blocks hence π s,t ⁄= π s,t +1. Since π is evercrossing, there exist b, d ∈ π u,
u ⁄= s, such that π s,t , b, π s,t +1, d are ordered up to a cyclic rotation. In
other words: on the graphical representation on a circle, el ements of the
block π u are not all on the same side of the line which passes through π s,t
and π s,t +1. Therefore there must be some consequent elements π u,v , π u,v +1
of the block π u such that π s,t , π u,v , π s,t +1, π u,v +1 are ordered up to a cyclic
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 37
rotation. It is easy to see that b = π ′
u,v and d = π s,t +1 are the vertices
required by the property of π fat to be evercrossing.
Let π be the outcome of the simpliﬁcation algorithm and such that
genusπ ⁄= 0. We keep notation from Section 3.1.3, i.e. r = n
2 denotes
the number of blocks of π and t denotes the number of cycles of π fat ◦ c (or,
alternatively, the number of holes after gluing the ﬁrst col lection of discs).
Observe that on the boundary of every hole there must be at lea st three in-
tervals which touch some discs from the ﬁrst collection (if s ome hole does
not touch any discs then π = ∅ and genusπ = 0; if some hole touches only
one disc we denote by a, c the only two vertices which are on the boundary
of the hole and clearly (a, c ) is a pair of vertices required for π to be non–
evercrossing; if some hole touches exactly two discs then it is possible to
perform some simpliﬁcations of step 3; a careful reader migh t observe that
it is possible and perfectly legal for a hole to touch some of the discs twice,
cf the left–hand side partition on Figure 4.10). Since π is a pair partition,
every disc of the ﬁrst collection touches the holes on exactl y two intervals.
It follows that n = 2r ≥ 3t. Equation (3.4) implies that
n ≤ 12 genusπ − 6
which ﬁnishes the proof. □
4.4.5. Interpretation of the free index? Free index of a partition is a quite
strange combinatorial object. We can think that it measureshow far a given
partition is away from non–crossing partitions or how much it is evercross-
ing. Its particularly interesting feature appears in Theor em 4.10, namely
that it is being preserved by a number of operations one can pe rform on a
partition. The list of such operations is far from being comp lete and we
leave it as an exercise to the reader to ﬁnd at least one such operation which
does not appear in the simpliﬁcation algorithm. Suppose we h ave com-
pleted such a list of natural operations preserving free ind ex; now we can
treat them as analogues of Reidemeister moves in the knot the ory and say
that two partitions are isotopic when one can be obtained fro m another by
a sequence of such elementary operations. Of course free ind ex will be an
invariant of the isotopy class but we should not expect that i t will always
be able to distinguish different isotopy classes. A questio n arises: is there
some natural (geometric?) interpretation of such isotopy?
4.5. The second main result: the second–order expansion of free c u-
mulants and characters.
4.5.1. Evercrossing partitions with genus 1. Theorem 4.10 allows us to
enumerate (in ﬁnite time) all possible outcomes of the simpl ifying algo-
rithm for a ﬁxed genus of the original evercrossing partitio n. By reversing
38 PIOTR ´SNIADY
FIGURE 4.8. General pattern of evercrossing partitions with
genus 1 and free index equal to − 1 (only non–trivial blocks
were shown).
FIGURE 4.9. General pattern of evercrossing partitions with
genus 1 and free index equal to − 2 (only non–trivial blocks
were shown).
all three steps of the simplifying algorithm we are able to wr ite a number
of “templates” which describe all evercrossing partitions with a prescribed
genus. Let us have a look on an example.
Theorem 4.11. Every evercrossing partition with genus1 must be either of
the form depicted on Figure 4.8 (in this case it has the free in dex equal to
− 1) or Figure 4.9 (in this case it has the free index equal to − 2). On both
ﬁgures only non–trivial blocks were shown.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 39
FIGURE 4.10. The only two possible outcomes of the sim-
pliﬁcation algorithm for an evercrossing partition with genus
1. The pair partition on the left–hand side has free index
equal to − 1 and the pair partition on the right–hand side has
free index equal to − 2.
Proof. Theorem 4.10 implies that an outcome of the simpliﬁcation al go-
rithm obtained for an evercrossing partition with genus1 must have at most
6 vertices. By direct inspection of all such pair partitions o ne can ﬁnd that
there are only two possible outcomes of the simplifying algorithm and they
are depicted on Figure 4.10.
By reverting the third step of the simplifying algorithm we s ee that the
outcome of the ﬁrst two steps of the simplifying algorithm mu st be a pair
partition either of the form from Figure 4.8 or Figure 4.9. For Figure 4.9 we
have to study 24 cases now: each of the numbers p, q, r can be either even
or odd, we also have to guess which of the vertices carry primed and which
carry non–primed labels (we have two possibilities); the case of Figure 4.8
is slightly simpler. For each of the 24 cases we try to reverse the second
step of the algorithm (and for most of the cases it is not possi ble; a less
patient reader will ﬁnd easily arguments which would allow to ﬁnd only the
few cases when it is possible). It turns out that after the ﬁrs t step of the
simpliﬁcation algorithm must be a pair partition either of the form depicted
on Figure 4.8 or on Figure 4.9. Reverting the ﬁrst step means t hat we are
allowed to add any number of trivial blocks, which ﬁnishes the proof. □
4.5.2. Second–order asymptotics of free cumulants. We leave the proof of
the following simple lemma to the reader.
Lemma 4.12. For any y, n ∈ N there are
( y− 1
n− 1
)
solutions of the equation
x1 + · · · + xn = y if we require x1, . . . , x n to be positive integers.
40 PIOTR ´SNIADY
Theorem 4.13. For every n ∈ N we have
(4.16)
RJM
n = Σ n− 1 −
∑
m 2,m 3, ···≥0
2m 2 +3m 3+4m 4+···=n− 2
n(n − 1)(n − 2)
24
( m2 + m3 + · · ·
m2, m 3, . . .
)
×
∏
s≥2
(
(s − 1)
) m s
Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m2 times
, 2, . . . , 2
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m3 times
, 3, . . . , 3
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m4 times
,... +
(terms of degree at most n − 4)
Proof. The highest–order term in expansion (4.10) was already foun d in
Theorem 4.7. The next highest–order terms correspond to evercrossing par-
titions with genus1. We shall calculate ﬁrst the contribution of the partitions
of the form depicted on Figure 4.8.
For the partition from Figure 4.8 the tuple (k1, . . . , k p+q − 1) given by the
algorithm from Section 3.1.1 is equal to
(4.17)
( (
(as+1 − as) + (cs − cs+1) − 1
)
s=1,2,...,p − 1,
(
(b1 − ap) + (cp − bq ) + (dq − c1) + (a1 − d1)
)
− 3,
(
(bs+1 − bs) + (ds − ds+1) − 1
)
s=1,2,...,q − 1
)
.
Here and in the following, the subtraction is taken modulo n, i.e.
y − x =
{
y − x if y > x,
(y + n) − x if y < x.
This subtraction has a natural interpretation as the number of elements be-
tween x and y going counterclockwise from x to y.
Let m2, m 3, . . . be a sequence of nonnegative integers such that 2m2 +
3m3 + · · · = n − 2. We shall count now for how many different parti-
tions of the form depicted on Figure 4.8 the tuple (4.17) is eq ual (up to a
permutation) to
(4.18) (k ′
1, k ′
2, . . . , k ′
p+q − 1) = ( 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m 2 times
, 2, . . . , 2/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
m 3 times
, 3, . . . , 3/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
m 4 times
. . . ).
Firstly, observe that all the numbers (as), (bs), (cs), (ds) are uniquely de-
termined by a1 and the collection of increments
(4.19) (as+1 − as)s=1,...,p − 1, (b1 − ap), (bs+1 − bs)s=1,...,q − 1,
(cp− bq ), (cs− cs+1)s=1,...,p − 1, (dq − c1), (ds− ds+1)s=1,...,q − 1, (a1− d1),
where numbers (4.19) are positive integers the sum of which is equal to n.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 41
Every partition of the form depicted on Figure 4.8 has free index equal to
(− 1). There are n choices of a1. There are
( m 2+m 3+···
m 2 ,m 3,...
)
different permuta-
tions of the tuple (4.18). We need to specify1 ≤ p ≤ m2 + m3 + · · ·. Now
we count in how many different ways every of the numbers (4.17 ) can be
written as a sum of two speciﬁed elements of (4.19) minus 1 except for one
of the numbers (4.17) which should be written as a sum of four s peciﬁed
elements of (4.19) minus 3; the position of this exceptional number is spec-
iﬁed by the index p. Finally, we have to take into account the symmetry
factor 1
4 of Figure 4.8 since for every partition of this form we can cho ose
sequences (as), (bs), (cs), (ds) in four different ways corresponding to four
cyclic rotations of the template. From Lemma 4.12 it follows that the con-
tribution of partitions from Figure 4.8 to the summand Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m2 times
, 2, . . . , 2
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m3 times
,...
is equal to
(4.20) (− 1) 1
4n
( m2 + m3 + · · ·
m2, m 3, . . .
) ∑
1≤p≤m 2+m 3+···
( k ′
p + 2
3
) ∏
p′⁄=p
( k ′
p′
1
)
.
By very similar considerations one can easily show that the c ontribution
of partitions from Figure 4.9 to the summand Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m2 times
, 2, . . . , 2
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m3 times
,... is equal
to
(4.21) (− 2) 1
6 n
( m2 + m3 + · · ·
m2, m 3, . . .
)
×
∑
1≤p1 < p2 ≤m 2 +m 3+···
( k ′
p1 + 1
2
)( k ′
p2 + 1
2
) ∏
p′⁄=p1 ,p 2
( k ′
p′
1
)
.
By an application of Leibnitz rule we see that the sum of (4.20) and (4.21)
can be written in a compact form as
[x−( 2m 2+3m 3+··· )− 2zm 2
2 zm 3
3 · · · ] (− 1)n
24 ×
d2
dx2
( ∑
s
(s − 1)zsx− s
) m 2 +m 3+···
=
[zm 2
2 zm 3
3 · · · ] (− 1)n(n − 1)(n − 2)
24
( ∑
s
(s − 1)zs
) m 2+m 3 +···
=
(− 1)n(n − 1)(n − 2)
24
( m2 + m3 + · · ·
m2, m 3, . . .
)
1m 22m 33m 4 · · ·
which ﬁnishes the proof. □
42 PIOTR ´SNIADY
4.5.3. Second–order expansion of characters. The following result was
conjectured by Biane [Bia03].
Theorem 4.14. For every n ≥ 2 we have
Σ n− 1 = RJM
n +
∑
m 2,m 3, ···≥0
2m 2+3m 3 +···=n− 2
1
4
( n
3
)( m2 + m3 + · · ·
m2, m 3, . . .
) ∏
s≥2
(
(s − 1)RJM
s
) m s
+
(terms of degree at most n − 4).
Proof. In (4.16) we use (4.14) to express Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m2 times
, 2, . . . , 2
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
m3 times
,... in terms of
RJM
2 , R JM
3 , . . . . □
