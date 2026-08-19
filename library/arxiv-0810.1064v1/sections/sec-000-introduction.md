---
doc_id: arxiv-0810.1064v1
doc_title: "Multiple polylogarithm values at roots of unity Jianqiang Zhao"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 0810.1064v1.pdf
source_sha256: b2d7514c5382ceaa
doc_brief: "Multiple polylogarithm values at roots of unity Jianqiang Zhao — For any positive integer N let µ N be the group of the N th roots of unity."
---
Double shuﬄe relations have played signiﬁcant roles in the study of mu ltiple zeta values in recent years.
These relations can be easily generalized to the special values of mult iple polylogarithms at roots of unity
(MPV for short):
Lis1,...,sn (ζ1, . . . , ζn) :=
∑
k1>···>kn>0
ζk1
1 · · · ζkn
n
ks1
1 · · · ksn
n
, (s1, ζ1) ⁄= (1, 1), (1)
where ζj are all N th roots of unity for j = 1, . . . , n. We call N the level and w := s1 + · · ·+ sn the weight.
One of our major interests is to ﬁnd the dimension d(w, N ) of the Q-vector space MPV (w, N ) spanned
by these values.
In [7], Racinet listed the following relations: double shuﬄe relations and their regularized versions (by
regularizing both the divergent integrals and divergent series repr esenting MPVs), (regularized) distribu-
tions, and weight one relations. We will call these standard relations. By intensive MAPLE computation
it is shown [8] that in many cases these relations cannot produce all t he possible Q-linear relations. For
example, standard relations imply only d(3, 4) ≤ 9 which is one more than the bound given by [4, 5.25].
Concretely, from standard relations MAPLE conﬁrms the following
Fact: Every MPV of weight 3 and level 4 can be written explicitly
as a linear combination of the nine MPVs appearing in (2),
(∗)
and no further Q-linear relations between these values can be deduced from the sta ndard relations. But
by GiNac [6] and EZface [1] the following is found numerically (see [8, Rem ark 10.1])
5Li1,2(−1, −i) = 46 Li1,1,1(i, 1, 1) − 7Li1,1,1(−1, −1, i) − 13Li1,1,1(i, i, i) + 13Li1,2(−i, i)
− Li1,1,1(−i, −1, 1) + 25Li1,1,1(−i, 1, 1) − 8Li1,1,1(i, i, −1) + 18Li2,1(−i, 1). (2)
In this note, we shall prove (2) from the explicit relations in ( ∗) by using the octahedral symmetry of
P1 − ({0, ∞} ∪ µ 4) where µ N denotes the set of N th roots of unity. We can treat the weight 4 and level
4 case in a similar fashion.
1
The result above in level four case shows that the standard relatio ns are not always suﬃcient to
determine d(w, N ). On the other hand, Deligne and Goncharov [4] ﬁnd some closed fo rmulae for upper
bounds of d(w, N ) for all w and N by studying the motivic fundamental group of P1 − ({0, ∞} ∪ µ N ) in
the framework of mixed Tate motives over the ring of S-integers of a number ﬁeld.
Proposition 1. ([4, 5.25]) Let N be a positive integer. Let ϕ be the Euler’s totient function and ν(N )
be the number of prime factors of N . Then d(w, N ) ≤ D(w, N ) where D(w, N ) are deﬁned by the formal
power series
1 +
∞∑
w=1
D(w, N )tw =





(1 − t2 − t3)−1, if N = 1;
(1 − t − t2)−1, if N = 2;(
1 −
( ϕ(N )
2 + ν(N )
)
t +
(
ν(N ) − 1
)
t2) −1
, if N ≥ 3.
As an example one can ﬁnd the bound d(w, 4) ≤ 2w for all weight w and by a variant of a conjecture
of Grothendieck it can be deduced that for N = 4 equality should always hold. Further, Goncharov [4]
has deﬁned some pro-nilpotent Lie algebra D graded by weight and depth using standard relations and
then related D to the motivic fundamental Lie algebra in lower depth cases. Using th is we shall improve
the bounds in the above proposition for all levels N = p and N = p2 (p ≥ 5 a prime) in the last section.
From this improved bound we ﬁnd that when 7 < N < 50 standard relations are incomplete if N is a
power of 2 or 3, or N has at least two prime factors, though we don’t know how to ﬁnd miss ing relations
explicitly.
