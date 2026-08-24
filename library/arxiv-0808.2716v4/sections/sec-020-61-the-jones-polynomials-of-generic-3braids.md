---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-020-61-the-jones-polynomials-of-generic-3braids
section_title: "The Jones polynomials of generic 3–braids"
section_number: 6.1
pages: 34-40
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
a 3–braid, we need to relate the Jones polynomial to the Schre ier normal form of the braid.
(See Theorem 5.1.) Here, we will concern ourselves with 3–br aids whose Schreier normal
forms are generic. That is, we will consider braids b ∈B3 written in the form
b =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
where pi,q i,k ∈ Z, with pi,q i> 0, and C := (σ1σ2σ1)2. We set
p :=
s∑
i=1
pi, and q :=
s∑
i=1
qi.
The exponent eb of a braid b is the signed sum of its powers. Thus for an alternating braid
a, ea = p − q, and if b =C ka, then eb = 6k + p − q = 6k +ea. The exponent eb is closely
related to the writhe of a diagram, namely the algebraic sum of oriented crossings . Because
both of the generators σ1 and σ2 depicted in Figure 1 are negative crossings, the writhe of
the standard diagram of a closed 3–braid is w(Db) = −eb.
For a braid b ∈B3, let ˆb denote the closure of b. Let K denote the link type represented
by ˆb and let JK(t) denote the Jones polynomial of K. We write
(8) JK (t) = αKtM (K) +βKtM (K)−1 +... +β′
Ktm(K)+1 +α′
Ktm(K),
so that M (K) is the highest power of t inJK (t) and m(K) is the lowest power of t inJK (t).
Now the second and next-to-last coeﬃcients of JK (t) are βK and β′
K, respectively.
We will also need the following deﬁnitions. Associated to a l ink diagram D and a crossing
of D are two link diagrams, each with one fewer crossing than D, called the A–resolution
and B–resolution of the crossing. See Figure 11.
B− resolutionA− resolution
Figure 11. Resolutions of a crossing
Starting with any D, let sA(D) (resp. sB(D)) denote the crossing–free diagram obtained
by applying the A–resolution (resp. B–resolution) to all the crossings of D. We obtain
graphs GA(D), GB(D) as follows: The vertices of GA(D) are in one-to-one correspondence
with the components of sA(D). For every crossing of D, we add an edge between the vertices
of GA(D) that correspond to the components of sA(D) at that crossing. In a similar manner,
construct the B–graph GB by considering components of sB(D). A link diagram D is called
adequate if the graphs GA(D), GB(D) contain no 1–edge loops, i.e. if there are no edges
with both ends at the same vertex.
CUSP AREAS OF F AREY MANIFOLDS 35
LetvA(D),eA(D) (resp. vB(D),eB(D)) denote the number of vertices and edges of GA(D)
(resp. GB(D)). The reduced graph G′
A(D) is obtained from GA(D) by removing multiple
edges connected to the same pair of vertices; similarly one h as the reduced graph G′
B(D).
Let e′
A(D) (resp. e′
B(D)) denote the number edges of G′
A(D) (resp. G′
B(D)).
The following results about Jones polynomials of adequate k nots are well known.
Lemma 6.1. LetD be an adequate diagram of a link K, whose Jones polynomial is written
as in equation (8). Then the top and bottom coeﬃcients of JK(t) satisfy
αK = (−1)vB (D)+w(D)−1, β K = (−1)vB (D)+w(D)(e′
B(D) −vB(D) + 1),
α′
K = (−1)vA(D)+w(D)−1, β ′
K = (−1)vA(D)+w(D)(e′
A(D) −vA(D) + 1).
Proof. Let Z[A, A−1] denote the ring of Laurent polynomials in a variable A, with integer
coeﬃcients. Recall that the Kauﬀman bracket of the diagram D, denoted by ⟨D⟩, is an
element in Z[A, A−1] such that
(9) JKa(t) = ( −A)−3w(D) ⟨D⟩
⏐
⏐
⏐A =t−1/ 4 ,
where w(D) is the writhe of D, or the algebraic sum of crossings. Now, Kauﬀman showed
that the ﬁrst and last coeﬃcients of ⟨D⟩ are (−1)vA(D)−1 and (−1)vB (D)−1, respectively. (See
[20, Theorem 6.1] for a proof.) Meanwhile, Stoimenow showed [54] that the second coeﬃcient
is given by ( −1)vA(D)(e′
A(D) −vA(D) + 1), and similarly the next–to–last coeﬃcient is given
by ( −1)vB (D)(e′
B(D) −vB(D) + 1). See [20, Corollary 6.3] for an alternate proof.
Next, we multiply ⟨D⟩ by ( −A)−3w(D). As a result, all the coeﬃcients are multiplied by
(−1)−3w(D) = ( −1)w(D). Finally, to recover the Jones polynomial, we substitute A =t−1/ 4.
As a result, the highest powers of A will correspond to the lowest powers of t, and vice versa.
Thus the top and bottom coeﬃcients of JK(t) are as claimed. □
Given a condition R, let δR be the characteristic function of R: its value is 1 when R is
true, and 0 when R is false. The characteristic functions εp :=δp≤2 and εq :=δq≤2 will be
particularly useful for expressing the Jones polynomials o f 3–braids.
Lemma 6.2. Suppose that a link Ka is the closure of an alternating 3-braid
a =σp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
with pi,q i > 0. Suppose as well that p> 1 and q> 1. Then the following hold:
(a) The highest and lowest powers of t in JKa(t) are
M (Ka) = 3q − p
2 and m(Ka) = q − 3p
2 .
(b) The ﬁrst two and last two coeﬃcients in JKa(t) are
αKa = (−1)p, β Ka = (−1)p+1(s −εq), β ′
Ka = (−1)q+1(s −εp), α ′
Ka = (−1)q,
whereεp equals 1 if p = 2 and 0 if p> 2, and similarly for εq.
(c) The third and third-to-last coeﬃcients in JKa(t) satisfy
1 ≤ (−1)pγKa ≤ s(s + 3)
2 and 1 ≤ (−1)qγ′
Ka ≤ s(s + 3)
2 .
These upper bounds are attained when s >1 and pi,q i > 1 for all i. See Equation
(14) for a precise formula for γKa.
36 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Proof. Consider the link diagram D := ˆa obtained as the closure of a. Note that the diagram
D is alternating and reduced, i.e. it contains no nugatory cro ssings (here, we are using the
hypothesis that if s = 1, then p1 = p > 1 and q1 = q > 1). This implies that D is an
adequate diagram (compare [39, Proposition 5.3]). Thus we m ay use Kauﬀman’s work to
ﬁnd the highest and lowest powers of A, and Lemma 6.1 to ﬁnd the coeﬃcients.
Kauﬀman showed that the highest and lowest powers of A in the bracket polynomial ⟨D⟩
are c(D) + 2vA(D) − 2 and −c(D) − 2vB(D) + 2, respectively. (See [39] for an exposition.
A proof from the graph theoretic viewpoint can be found in [19 , Proposition 7.1].) In our
setting, the crossing number is c(D) = p + q, vA(D) = p + 1, and vB(D) = q + 1. Thus the
highest and lowest powers of A in ⟨D⟩ are 3 p + q and −3q − p, respectively.
By equation (9) we multiply ⟨D⟩ by (−A)−3w(D) = (−A)−3q+3p. (Recall that for a closed
3–braid, w(D) = −ea = q − p.) Thus the highest power of A becomes 6 p − 2q, and the
lowest becomes 2 p − 6q. Then to obtain JKa(t), replace A byt−1/ 4. Thus the highest power
of t in JKa(t) corresponds to −1/4 times the lowest power of A, and vice versa:
M (Ka) = −(2p − 6q)
4 = 3q − p
2 and m(Ka) = q − 3p
2 .
Next, we turn our attention to the top and bottom coeﬃcients o f JKa. In the following
calculation, we focus on the ﬁrst three coeﬃcients αKa βKa, and γKa. By Lemma 6.1 and
[21, 54], these top coeﬃcients only depend on the B–resolution of D. To ﬁnd the last three
coeﬃcients, one merely needs to interchange p with q in all the formulas.
From the B–resolution of the diagram D, one can readily compute that vB(D) = q + 1.
Thus, by Lemma 6.1, αKa = ( −1)2q−p = ( −1)p. The total number of edges of GB is
eB(D) = p + q, the number of crossings in D. Out of this total number, the p edges
corresponding to the powers of σ1 will become identiﬁed to s classes of edges in e′
B (with
one edge for each σ1–twist region. The q edges corresponding to the powers of σ2 all survive
in e′
B, except in the special case when q = 2, when a loop of two edges running all the
way around the braid counts for only a single reduced edge in e′
B. Putting it together, the
number of reduced edges will be e′
B(D) = q −εq +s, hence
(10) βKa = (−1)2q−p+1(e′
B −vB + 1) = ( −1)p+1(s −εq).
To ﬁnd γKa, we must calculate the third-to-last coeﬃcient of the Kauﬀma n bracket
⟨D⟩, and then multiply by ( −1)w(D) = ( −1)q−p. Thus γKa is the third-to-last coeﬃcient
of ⟨D⟩, which was computed in closed form by Dasbach and Lin [21, The orem 4.1] and
ozawa:adequate [54, Proposition 3.3]. According to their f ormula,
(11) γKa = ( −1)p
(|βKa|(|βKa| + 1)
2 −θ +µ −τ
)
,
whereθ,µ, andτ are deﬁned as follows. The quantity θ is always zero for reduced alternating
diagrams; this is because the circles sB do not nest on the projection plane. The quantity
µ is the number of edges in the reduced graph G′
B whose multiplicity in GB is greater than
one. By the argument preceding equation (10),
(12) µ = # {i :pi> 1} +εq = s − #{i :pi = 1} +εq.
Finally, the quantity τ is deﬁned to be number of loops in G′
B that consist of exactly 3
edges. In our context, one of these loops (surrounding a regi on of the diagram D) typically
arises for any i where qi = 1. However, in the special case when s = q = 2, two of these
regions involve the same triple of vertices in GB, and account for the same loop in G′
B.
CUSP AREAS OF F AREY MANIFOLDS 37
Furthermore, a loop of length 3 goes all the way around the bra id when q = 3. All together,
(13) τ = #{i :qi = 1} −δs=q=2 +δq=3.
Thus, plugging equations (10), (12), (13) into equation (11 ) gives
(−1)pγKa = (s −εq)(s −εq + 1)
2 +µ −τ
= s2 +s − 2sεq
2 +s − #{i :pi = 1} − #{i :qi = 1} +εq +δs=q=2 −δq=3
= s2 + 3s
2 − (s − 1)εq +δs=q=2 − #{i :pi = 1} − #{i :qi = 1} −δq=3
= s2 + 3s
2 − #{i :pi = 1} − #{i :qi = 1} −δq=3.(14)
The last equality holds because both ( s − 1)εq and δs=q=2 must be 0 for s ⁄= 2, while on
the other hand δs=q=2 = εq for s = 2. Thus, since all terms of (14) after ( s2 + 3s)/2 are
non-positive, ( −1)pγKa is always bounded above by ( s2 + 3s)/2. This upper bound will be
attained whenever s> 1 and pi,q i > 1 for all i, for then all correction terms must be 0.
For the lower bound on ( −1)pγKa, observe that each of # {i :pi = 1} and # {i :qi = 1} is
at most s. In fact, each of these quantities is 0 when s = 1 (by hypothesis). Furthermore,
#{i :qi = 1} +δq=3 ≤s when s = 2. Thus
(−1)pγKa ≥ s2 + 3s
2 − 1 ≥ 1 when s = 1,
(−1)pγKa ≥ s2 + 3s
2 − 2s ≥ 1 when s = 2,
(−1)pγKa ≥ s2 + 3s
2 − 2s − 1 ≥ 2 when s ≥ 3. □
Let Z[t, t−1] denote the ring of Laurent polynomials with integer coeﬃci ents and G(2,t )
the group of 2 × 2 matrices with entries in Z[t,t −1]. The Burau representation ψ : B3 →
G(2,t ) is deﬁned by
(15) ψ(σ−1
1 ) =
[
−t 1
0 1
]
, ψ (σ−1
2 ) =
[
1 0
t −t
]
.
See [9, 33] for more details. 2
For a braid b ∈ B3, let ˆb denote the closure of b and let eb denote the exponent of b.
As calculated in [33] (the formula is also given and used in th e papers [10] and [35] where
properties of the Jones polynomial of 3–braids are discusse d), the Jones polynomial of ˆb is
given by
(16) Jˆb(t) = ( −
√
t)−eb · (t +t−1 + trace(ψ(b))).
Lemma 6.3. Suppose that a link Kb is the closure of a generic 3–braid
b =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
2Our deﬁnition of the braid generator σ i, depicted in Figure 1, corresponds to Jones’ deﬁnition of σ − 1
i
[33]. The literature contains many examples of both convent ions: compare [10, 16] to [35, 46]. Replacing σ i
with σ − 1
i produces the mirror image of a link, and aﬀects the Jones poly nomial by replacing t with t− 1.
38 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
withpi,q i> 0. Let Ka denote the alternating link represented by the closure of th e alternating
braida :=σp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 . If JKa(t) andJKb(t) denote the Jones polynomials of Ka and
Kb respectively, then
JKb(t) = t−6kJKa(t) + (−
√
t)−ea
(
t +t−1)(
t−3k −t−6k
)
,
whereea is the braid exponent of a.
Proof. An easy calculation, using equation (15), will show that
ψ(C) = ψ((σ1σ2σ1)2) =
[
t−3 0
0 t−3
]
,
and thus
(17) trace( ψ(b)) = t−3k trace(ψ(a)).
The braid exponents eb and ea satisfy eb = 6k +ea. Thus, by equations (16) and (17),
(18) JKb(t) = t−3k(−
√
t)−ea
(
t +t−1 +t−3k trace(ψ(a))
)
,
and
(19) JKa(t) = ( −
√
t)−ea
(
t +t−1 + trace(ψ(a))
)
.
By eliminating trace(ψ(a)) from equations (18) and (19) we obtain
(20) JKb(t) = t−6kJKa(t) + (−
√
t)−ea
(
t +t−1)(
t−3k −t−6k
)
,
as desired. □
We are now ready to estimate certain outer coeﬃcients of the J ones polynomial for any
generic closed 3–braid.
Deﬁnition 6.4. Let K be a link in S3. From the Jones polynomial JK (t), we deﬁne the
following quantities. Let
ζK =
{
βK, if |αK | = 1
0, otherwise and ζ ′
K =
{
β′
K, if |α′
K | = 1
0, otherwise.
Note that by Lemma 6.1, adequate links will satisfy ζK =βK and ζ ′
K =β′
K . This deﬁnition
gives a way to generalize approximately the same quantity.
Proposition 6.5. Let Kb be the closure of a generic 3–braid b = C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
with pi,q i > 0. Deﬁne ζKb and ζ ′
Kb as in Deﬁnition 6.4. Then
s − 1 ≤ max
{
|ζKb|,
⏐
⏐ζ ′
Kb
⏐
⏐}
≤s + 1.
Proof. For the majority of this argument, we will work under the hypo thesis that p> 1 and
q> 1. At the end of the proof, we will consider the (simpler) case when p = 1 or q = 1.
So: assume that p> 1 and q> 1, and let a =σp1
1 σ−q1
2 · · ·σps
1 be the alternating part of b.
Consider JKb(t), as expressed as a sum of two terms in equation (20). By Lemma 6.2, the
ﬁrst term, t−6kJKa(t), is
t−6kJKa(t) = ( −1)p t(3q−p)/ 2−6k + (−1)p+1(s −εq)t(3q−p)/ 2−6k−1 + · · ·(21)
+(−1)q+1(s −εp)t(q−3p)/ 2−6k+1 + (−1)q t(q−3p)/ 2−6k.
Meanwhile, the second term on the right hand side of equation (20) expands out to
(22) ( −1)ea
(
t−ea/ 2−3k+1 +t−ea/ 2−3k−1 −t−ea/ 2−6k+1 −t−ea/ 2−6k−1
)
.
CUSP AREAS OF F AREY MANIFOLDS 39
If k = 0, then the expression in (22) vanishes, and the link Kb is alternating. Thus
ζKb =βKb and ζ ′
Kb =β′
Kb, and the desired result is true by Lemma 6.2.
Next, suppose that k ⁄= 0. We claim that no generality is lost by assuming that k > 0.
Otherwise, if k< 0, the mirror image Kd of the link Kb can be represented by the braid word
d =C −kσqs
1 σ−p1
2 σq1
1 · · ·σ−ps
2 , so the power of C will now be positive. The Jones polynomial
JKd can be obtained from JKb by interchangingt andt−1, so ζKb =ζ ′
Kd andζ ′
Kb =ζKd, with
the maximum of the two values unaﬀected. Thus we may assume k> 0.
If k > 0, the monomials of (22) are listed in order of decreasing pow ers of t, and each
monomial has a coeﬃcient of ±1. Furthermore, we claim that the degree of any term in
(22) is strictly higher than the degree of the lowest term in ( 21). This is because the last
monomial of (22) has degree −ea/2 − 6k − 1 = ( q − p)/2 − 6k − 1, and
(23) p ≥ 2 is equivalent to q − p
2 − 6k − 1 ≥ q − 3p
2 − 6k + 1.
Thus the lowest–degree term of JKb(t) is ( −1)q t(q−3p)/ 2−6k, and α′
Kb = (−1)q.
From equation (23), we can also conclude that the last monomi al of (22) only aﬀects the
next-to-last monomial of (21) if p = 2. When p is even, the signs of these two monomials
are ( −1)q+1 and ( −1)ea+1 = ( −1)p−q+1 = ( −1)q+1: they have the same sign. Thus when
p = 2, the last monomial of (22) will contribute 1 to |β′
Kb|; when p> 2, no monomial of (21)
aﬀects |β′
Kb| at all. We conclude that when k> 0,
ζ ′
Kb = β′
Ka + (−1)q+1εp = ( −1)q+1(s −εp +εp) = ( −1)q+1s.
Next, consider how the top two terms of (21) might interact wi th the monomials of (22).
If the top degree of (22) is lower than the top degree of (21), w e will have αKb = (−1)p and
ζKb =βKb will be oﬀ by at most 1 from βKa. In particular, s − 2 ≤ |ζKb| ≤ s + 1. If the top
degree of (22) is higher than the top degree of (21) by 2 or more , we will have αKb = (−1)ea
and ζKb = βKb = 0. If the top degree of (22) is higher by exactly 1, then we wil l have
αKb = ( −1)ea and ζKb = βKb = ( −1)p. If the top degree of (22) is exactly equal to the
top degree of (21), then the two monomials either add or cance l. If the top monomials add,
αKb = (−1)p · 2 and ζKb = 0 by Deﬁniton 6.4. Thus, in all cases when the top monomials o f
(21) and (22) do not cancel, we have 0 ≤ |ζKb| ≤ s + 1.
If the top monomials of (21) and (22) cancel (which can occur: see Proposition 6.7), we
have
3q − p
2 − 6k = −ea
2 − 3k + 1, which simpliﬁes to q = 3k + 1,
since ea = p − q. In particular, it follows that q ≥ 4. Then αKb = βKa = ( −1)p+1s. So,
if s ≥ 2, we have |αKb| ≥ 2, and again ζKb = 0 by Deﬁniton 6.4. Thus when s ≥ 2, we get
0 ≤ |ζKb| ≤ s + 1 in all cases. Since |ζ ′
Kb| is always equal to s if k >0, we conclude that
s − 1 ≤ max
{
|ζKb|,
⏐
⏐ζ ′
Kb
⏐
⏐}
≤s + 1 whenever s ≥ 2.
Note that the lower bound of s − 1 is only achieved when k = 0 and s = p = q = 2, i.e.,
when Kb is the ﬁgure–8 knot.
If s = 1 and the top monomials of (21) and (22) cancel, then αKb =βKa = ( −1)p+1 and
ζKb =βKb =γKa + (−1)p+1, where γKa is the third coeﬃcient of JKa(t) and ( −1)p+1 comes
from the second monomial of (22). By Lemma 6.2(c),
|ζKb| = |γKa| − 1 ≤ s(s + 3)
2 − 1 = 1 .
40 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Since we get 0 ≤ |ζKb| ≤ s + 1 whenever the top monomials do not cancel, and since |ζ ′
Kb| is
always equal to s if k >0, we conclude that
s − 1 ≤ max
{
|ζKb|,
⏐
⏐ζ ′
Kb
⏐
⏐}
≤s + 1 whenever s = 1 and p, q ≥ 2.
To complete the proof, we need to consider the case when p = 1 or q = 1, hence s = 1.
Without loss of generality, we may assume that p ≥ q = 1 (otherwise, take the mirror image
of Kb, as above). Then Ka is the (2 , p) torus link. By direct computation (for example,
using [39, Theorem 14.13] or [17, Proposition 2.1 and Exampl e 3]), it follows that
JKa(t) = ( −1)p+1
(
t−(p−1)/ 2 +t−(p+3)/ 2 −t−(p+5)/ 2 +t−(p+7)/ 2 −... + (−1)pt−(3p−1)/ 2
)
.
In particular, the second coeﬃcient of JKa(t) is 0 and every other coeﬃcient is ±1. If k ⁄= 0,
we may still use Lemma 6.3 to compute the Jones polynomial JKb(t). Thus, after multiplying
JKa(t) by t−6k and adding in the four monomials of (22), it will follow that e very coeﬃcient
of JKb(t) is 0, ±1, or ±2. Thus
0 ≤ max
{
|ζKb|,
⏐
⏐ζ ′
Kb
⏐
⏐}
≤ 2 whenever p = 1 or q = 1,
which is exactly what the proposition requires for s = 1. □
