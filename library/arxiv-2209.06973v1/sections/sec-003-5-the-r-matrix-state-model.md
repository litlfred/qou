---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-003-5-the-r-matrix-state-model
section_title: "The R-matrix state model"
section_number: 5
pages: 17-23
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
We review and reformulate the state model for the framed colored Jones
polynomial Jn as deﬁned in [4]. Recall that n labels the (n + 1)-dimensional
standard irreducible representation of sl(2, C), or the corresponding type 1
Uq(sl(2, C)-module, see [12], 5.2. Our normalization will coincide with [7] so
that n = 1 corresponds to the trivial 2-dimensional representation and the
classical Jones polynomial. Link components will all be colored by the same
representation. We will use the word coloring for the edge-colorings of the
projection graphs only. Throughout ε(v) will denote the sign of the crossing
v (vertex of the part arc-graphPK). Moreover, in [4] a variable v is used for
Jn while we will use the variable v2 =t in this paper, which corresponds up
to a change fromt tot−1 to the variablet in [7]. So our variablet corresponds
toq in [4] andt−1 in [7]. While describing the state-sum formula of [4] we will
already rewrite all formulas to variable t. This includes rewriting quantum
symbols in corresponding crossing-sign dependent functions, which are used
in [7].
Let a,b∈ Z. Then
{a} :=va−v−a =v−a(v2a− 1) = (ta/2−t−a/2 =t−a/2(ta− 1).
and
[a] ={a}
{1} = va−v−a
v−v−1 =va−1(1 +v−2 +··· +v−2(a−1))
This corresponds to
[a] =t
a−1
2 (1 +t−1 +··· +t−(a−1).
This is mostly important for normalization. The n-th colored Jones poly-
nomial of the unknot will be [ n + 1]. In fact if a framed link L contains k
trivially framed unknotted and unlinked components then JL = [n + 1]kJL′,
whereL′ is the link deﬁned from L by omitting the unknotted and unlinked
components, see [4].
17
Forb≥ 0 we deﬁne the Pochhammer symbol
{a}b ={a}{a− 1}···{ a−b + 1}
=t−ab/2+b(b−1)/4(ta− 1)(ta−1− 1)··· (ta−b+1− 1)
= (−1)bt−ab/2+b(b−1)/4(1−ta)(1−ta−1)··· (1−ta−b+1)
=tab/2−b(b−1)/4(1−t−a)(1−t−(a−1))··· (1−t−(a−b+1))
and for b <0,{a}b := 0. We will relate the above deﬁnition to the sign-
dependent Pochhammer symbol (not used by [7] but we will use in rewriting
their formula) deﬁned by
{a}b,t :=
b−1∏
s=0
(1−ta−s)
with ε∈{± 1}.
{a}b = (−1)(1+ε) b
2t−ε( ab
2− b(b−1
4 ){a}b,tε (1)
It follows for b≥ 0 from the deﬁnitions in [4]:
(a
b
)
:={a}b
{b}b
=tb(b−a)/2 (ta− 1)··· (ta−b+1− 1)
(tb− 1)··· (t− 1)
Note that the expression on the right hand side is not deﬁned for b = 0,
and is deﬁned to be 1 in this case. As above these quantum binomials are
related to the sign-dependent versions in [7] as follows: ( a)t := ta−1
t−1 and
(a)t! := (1)t(2)t··· (a)t and
(a
b
)
t
:= (a)t!
(b)t!(a−b)t! = (ta− 1)··· (ta−b+1− 1)
(tb− 1)··· (t− 1)
and thus (a
b
)
=tεb(b−a)/2
(a
b
)
tε
(2)
This follows because
(a
b
)
t−1
= (t−a− 1)··· (t−(a−b+1)− 1)
(t−b− 1)··· (t−1− 1)
= t−(a+(a−1)+···(a−b+1))
t−(b+(b−1)+···+1)
(a
b
)
t
=tb(b−a)
(a
b
)
t
18
We will use the following well-known lemma for the symmetry of quan-
tum binomials:
Lemma 5.1. Forc,d nonnegative integers we have
(c +d
c
)
=
(c +d
d
)
Proof of lemma. We have the formula:
(c +d
c
)
=t−cd/2 (tc+d− 1)··· (td+1− 1)
(tc− 1)··· (t− 1)
If c≤ d, multiplying both numerator and denominator on the right hand
side by
(td− 1)··· (tc+1− 1)
and noting that d(d− (c +d)) = c(c− (c +d)) the result follows. If d < c
both numerator and denominator contain the product
(tc− 1)··· (td+1− 1),
so after cancellation the result follows in this case too.
Note that by formula (2),
(c +d
c
)
=t−εcd/2
(c +d
c
)
tε
and (c +d
d
)
=t−εdc/2
(c +d
d
)
tε
so that symmetry of quantum binomials also holds for the sign-dependent
versions.
The formula in Proposition 3.7 of [4] generalizes to link projections, as
described in [4], Remark 3.5, in the following way: Let Fn
−,∗ be the set of
all colorings (−) of the part arc-graph PK of a link projection K as deﬁned
in section 2. We we assume that the ﬁrst strand of the braid projection is
colored 0 at the bottom, which is indicated by ∗. Let J′
n(K) be the framed
colored Jones-polynomial [4], we will discuss more details in section 6. Let
s be the number of braid strings and let {c1,...c c} be the set of crossings
in the braid projection. Then
J′
n(K) =
∑
s∈F n
−,∗
F (n,s )
19
where F (n,s ) is the product
F (n,s ) :=
s∏
𝓁=2
v−n+2b𝓁(s)
c∏
k=1
fε(ck)(n,i (k,s ),j (k,s ),r ). (3)
Here i(s),j (s) are the colors at the crossing ck determined by the state s
and the following convention (colors are decreasing on overcrossings):
j + r i − r
i j
ε = +1
j − r i + r
i j
ε = −1
Figure 8
with the functions f± are deﬁned by (see [7], 3.1, [11], Chapter 3, and
[16], 2.32 and 2.34)
f+(n,i,j,r ) := (−1)rv−((n−2i)(n−2j)+r(r−1))/2
(j +r
r
)
{n +r−i}r (4)
while the contribution at a negative crossing will be
f−(n,i,j,r ) :=v((n−2i−2r)(n−2j+2r)+r(r−1))/2
(i +r
r
)
{n +r−j}r. (5)
Remark. (a) What is called state s in [4] in the long knot case we call a
potential inducing the state on the part arc-graph with part arc colorings
(i(s),j (s)) on part arcs labeled by the crossings. In order to be able to
include overcrossing circles without crossings in the link case restrict the
values of r,βj to n so that the colorings at extrema are in n.
(b) Some care has to be taken when considering the above formula for the
state-sum with Proposition 3.7 in [7] for the long knot case. Garoufalidis and
Loebl sum over all possible nonnegative jumps at vertices, noticing that the
quantum algebra deﬁnitions will set state-sum contributions to 0 if colorings
of part arcs are > n. This will not be true in the link case because of the
bi(s) in the formula because there can be overcrossing circles such that the
20
maximim is not connected to a crossing at which the label bi(s) appears.
We have to restrict the state space so that all part arc colors are ≤ n, or
only consider projections without overcrossing circles. Note that the set of
contributing states is usually much more restricted by the requirement that
all induced part arc colors c (deﬁned from a given potential) satisfy c∈n.
The following examples will show the dependence of state-sums on the fram-
ing. We will also be able to state the skein relation of the classical Jones
polynomial in the framed case, which is of course related to a modiﬁcation
of the Kauﬀman bracket.
Example. If we represent the unknot by the empty braid then there is a
unique state with color 0 on the single strand, and the state-sum gives
J′
n(U) = 1 for all n. The corresponding vertex product is empty because
there is no crossing. It is known that the colored Jones polynomial is changed
by a power of v if we change the framing in the ﬁrst component of a link
(see [17], (1.7)). If we use the closure of the braid σ1 to represent the unknot
U(1) with framing +1 the decreasing condition at the single vertex implies
that the only state is the all-0 state and J′
n(U(1)) =v−n2/2−n. On the other
hand if we use σ−1
1 to represent U(−1), the−1-framed unknot, then we get
states labeled by 0≤r≤n for a single crossing.
Figure 9
Using
(r
r
)
= 1 the following state-sum results for U(−1):
J′
n(U(−1)) =
∑
0≤r≤n
v−n+2rv(n(n−2r)+r(r−1))/2{n}r
=vn2/2−n ∑
0≤r≤n
vr(2−n)+ r(r−1)
2 {n}r,
and thus the following identity for the well-known q-Pochhammer symbol:
21
∑
0≤r≤n
vr(2−n)+ r(r−1)
2 {n}r =v2n,
which is easily proved by induction using{n+1}r+1 = (vn+1−v−(n+1)){n}r.
Forn = 1 and{1}0 = 1 (empty product) and{1}1 =v−v−1 the right hand
side is
1 +v(v−v−1) =v2
The induction step gives:
1 +
∑
1≤r≤n+1
vr(2−(n+1))+ r(r−1)
2 {n + 1}r
=1 +
∑
0≤r≤n
v(r+1)[2−(n+1)]+ r(r+1)
2 (vn+1−v−(n+1)){n}r
=1 +v2·v2n−v−2n·v2n
=v2(n+1)
Example. We consider the casen = 1. The framed Jones polynomial J′ =J′
1
deﬁned by the state-sum [4] above satisﬁes the skein relation
v−1/2J′(K+)−v1/2J′(K−) = (v−1−v)J′(K0)
andJ′(U) = 1 forU the trivially framed unknot (represented by the 1-braid
closure of a single strand), J′(K⊔U) = (v−1 +v)J′(K) for each non-empty
framed link K, and
J′(K(1)) =v−3/2J′(K).
It is a good exercise to check the skein relation follows directly from the
formula above: For n = 1 only r = 0 and r = 1 are possible values at a
crossing. For a given K and crossing we can divide the set of states at a
crossing intoF(±,r) withr∈{ 0, 1}. Forr = 0 there are all colors 0 or 1 states
possible for both the positive and negative crossing. Forr = 1 the sign of the
crossing determines the possible part arc colorings at the crossing. For the
Conway smoothing K0 at the crossing the states are naturally divided into
subsets by the two part arcs colored as (left , right): (0, 0), (0, 1), (1, 0) and
(1, 1). Now the all 0, respectively all 1-states, in F(±,0) correspond to (0, 0)
and (1, 1)-states of the smoothing. The vertex contribution of the crossing
at the positive crossing isv−1 while the contribution at the negative crossing
is v, corresponding to the states on K0 multiplied by v−1−v. Recall that
{1}1 =v−v−1. For r = 1 admissibility reduces the colorings at the positive
22
crossing toi = 1 andj = 0 and the formula forf+ shows vertex contribution
(−1)1v−(1−2)/2{1}1, which multiplied by v−1/2 contributes the factor−(v−
v−1 =v−1−v for each corresponding (1, 0)-state of the smoothing, while the
formula for f− shows vertex contribution v(1−2)/2{1}1, which multiplied by
−v1/2 also contributes v−1−v as a factor but this time to the (0 , 1) states
on K0. If we use the usual writhe normalization we have the deﬁnition of
the unframed Jones polynomial
J(K) =v
3
2ω(K)J′(K)
Substituting in the skein relation for framed links above and using ]ω(K±) =
ω(K0)± 1 where we use the notation for the link instead of the projection,
we get
v−2J(K+)−v2J(K−) = (v−1−v)J(K0)
Remark. We note that in the formula for F in [4], Proposition 3.7 the vari-
ablev has to be replaced byq and thus we have a factor 2 additionally. This
for example can easily be seen from the calculations of J′
n for the examples
above.
