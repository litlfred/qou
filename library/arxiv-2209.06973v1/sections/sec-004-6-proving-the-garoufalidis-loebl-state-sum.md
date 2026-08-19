---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-004-6-proving-the-garoufalidis-loebl-state-sum
section_title: "Proving the Garoufalidis-Loebl state-sum"
section_number: 6
pages: 23-38
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
We will now rewrite the usual state-sum contributions as described in [4]
into the Garoufalidis Loebl state-sum contributions using the above identi-
ties and the ﬂow Lemma. There two important steps: The ﬁrst will be to
transform the formulas in the last section into formulas for the (+)-model
(increasing colors on overcrossing arcs at overcrossings). The second is to
rewrite the two functions f± into a single vertex contribution formula, de-
pending on the crossing sign.
Our convention at crossings will be:
b a
a − r b + r
ε = +1
a b
b + r a − r
ε = −1
23
Figure 10
Note that in order to apply the formulas from section 5 we change the
orientation of the projection. It is known that a change of orientation does
not change the colored Jones polynomial. There will be though a change in
rotation numbers, which will show up in deﬁning rot( f) for a state on GK
in this section, and it will appear in the deﬁnition of δ′(K,n ), which is a
global power of t for the state-sum contributions. We also point out that
there are diﬀerent conventions with respect whether right or left oriented
extrema introduce the terms b𝓁(s) in equation (3).
ln the following we consider nowa,b,r,ε as functions on the set of cross-
ings and often omit the argument in formulas. Then the vertex state-sum
contribution at c is given by (4) and (5), with the variable v replaced by
the variable t = v2. We also use here the symmetry of the quantum bino-
mials. The following expression is immediate by substituting formulas (2)
and (1) and using Lemma 5.1. It gives a single expression to be evaluated
at each crossing with the sign of the crossing contained in the deﬁnitions of
the q-algebra symbols.
(−1)(1+ε) r
2t−ε/2((n−2b−(1−ε)r)( n
2−a+ 1
2 (1−ε)r)+ r(r−1)
2 )
·tε/2·br
(b +r
r
)
t−ε
· (−1)(1+ε) r
2t−ε( (n+r−a)r
2 − r(r−1)
4 ){n +r−a}r,tε
Using that 1 + ε∈{ 0, 2} to eliminate the sign dependence, and cancelling
the r(r− 1)/4-terms, we see that the vertex contribution function is given
by
tε/2·(−n2/2+nρ+σ)− 1
2τ·
(b +r
r
)
t−ε
·{n +r−a}r,tε (6)
with the two functions, deﬁned for each crossing:
ρ =b +a−r
σ =−2ab + (b−a)r +br− (r−a)r +r2
τ =r(b−a +r)
Here we also used 1
2(1−ε)2 = (1−ε). If we let a =r +R then
σ =−2ar− 2aR + (b−a)r +br−r2 +ar +r2 = 2b(r−a) =−2bR
The crucial geometric statements leading to the Garoufalidis-Loebl formula
are contained in the following two propositions. As noted above we usually
omit the arguments of the functions deﬁned on the set of crossings.
24
Proposition 6.1. For each Z-coloring of a chord graph, respectively the
corresponding coloring of a part arc-graph inducing this coloring,
∑
c
r(a−b−r) = 0
Proof. The formula is equivalent to:
∑
c
r(a−b) =
∑
r2 (7)
We will ﬁrst show the equation for chords only between distinct compo-
nents. As a ﬁrst step we consider the abstract chord graph with exactly one
chord for each 1≤j <k≤𝓁 directed from thek-th to thej−th component
with chord color rj,k. In this case the sum ∑
cr(a−b) is easily computed
as follows. The contribution of rjk in the sum is
rjk(−
∑
1≤i≤j−1
rij +
∑
j<i≤k
rji +
∑
1≤i≤j
rik) (8)
Figure 11
By using the cycle relation for thej-th component, the ﬁrst two sums can
be replaced by −∑
k<i≤µrji and so the contribution from rjk is (those be
read from the incoming chords of thej-th component and the corresponding
values on the k-th component):
rjk(rjk +
∑
1≤i<j
rik−
∑
k<i≤µ
rji) =r2
jk +rjk(
∑
1≤i<j
rik−
∑
k<i≤µ
rji) (9)
25
Figure 12
Thus it suﬃces to prove the claim:
∑
1≤j<k≤µ
rjk(
∑
1≤i<j
rik−
∑
k<i≤µ
rji) = 0 (10)
Now we can deﬁne a skew-symmetric matrix µ×µ-matrix (rjk) with the
coeﬃcients rjk for j < kgiven by chord colors of the chord graph. The µ
cycle relations then exactly say that the sum of columns of this matrix is
the zero-vector. In this case, the claim follows from the lemma below. The
chord graphs resulting from actual link projections diﬀer from the standard
graph considered above by doubling of chords and switching the order of
attachment to the circles. We will show that the relation of the proposi-
tion remains true in this case. Also note since the relation holds for chord
colorings by arbitrary integers and changing chord orientation and color by
multiplication by−1 we ﬁnally prove the result for arbitrary chord graphs
and thus arbitrary part arc-graphs.
We calculate the sums∑r(a−b) for chord graphs diﬀering locally only
by the following chord respectively two chords as in the picture
Figure 13
Then the contribution to the sum from the chord in the left picture is
(r +r′)(a− (b− (r +r′)) = (r +r′)2 + (r +r′)(a−b)
26
while the contribution from the two chords on the right is
r(a− (b−r)) +r′(a−r− (b−r−r′)) =r2 +r′2 + (r +r′)(a−b)
Note that the contributions from all other chords are unchanged. In going
from formula (1) to formula (3) above we eliminate copies of r2 and both
sides and then justify that the remaining sum on the left of the equation is
0. But this means that in the speciﬁc situation above we subtract ( r +r′)2
for the above sum and speciﬁc chord andr2 +r′2 for the doubled chord. The
result is the same in each case as our computation shows. Because for the
chord coloredr +r′ we know from before that the sum is 0 it will also follow
for the doubled chord.
Next, adding chords attached to single circles, so corresponding to self-
crossings in the part arc-graph, we ﬁrst attach a chord just in the special
way:
Figure 14
Note that this will change∑r(a−b) by a contributionr(c−(c−r)) =r2
so the result is true in this case. It suﬃces at this point to show that
the relation remains true under arbitrary switches in the way the chords
are attached to the circles. It will suﬃce to consider the following case of
two consecutive chords. There will other chords attached to the circles not
shown.
27
Figure 15
The contribution to ∑r(a−b) for the above picture is
r(a +b−r) +r′(a +r +r′−b′)
and after switching the endpoints of chords:
r′(a +r′−b′) +r(a +r +r′−b),
which in each case is r2 +r′2 +rr′ +r(a−b) +r′(a−b′), so the sum is not
changing. But any possible constellation of chords joining distinct compo-
nents of the chord graph can be reached by sequences of those switches.
Lemma 6.1. Let A = (ajk) be an µ×µ skew-symmetric matrix (over Z
(the argument works in fact over any commutative ring with 1) such that
for A = (a1,...,a µ) we have the sum of column vectors ∑µ
j=1aj is the
zero-vector. Deﬁne for each j <k,
sjk =
∑
1≤i<j
aik−
∑
k<i≤µ
aji.
Then
(∗)
∑
1≤j<k≤µ
ajksjk = 0
Proof. The setAµ of skew symmetric µ×µ matrices with zero column sum
is a submodule of the module of all skew symmetric matrices. Note that
the skew symmetry implies the zero row sum condition. It is easily proved
28
by induction that the following set of elementary matrices Ejk deﬁned for
1≤j <µ andj <k≤µ is a generating set ofAµ. Let (j,k ) be the position
of the upper left entry of the 2 × 2-matrix
( 1 −1
−1 1
)
for k>j + 1
in a skew symmetric matrix with only the entries for ( j,k ), (j,k + 1), (j +
1,k ), (j + 1,k + 1) above the diagonal are non-zero and given by the 2 × 2
matrix, and the entries below the diagonal are such that the matrix is skew-
symmetric. Similarly, we position the 2 × 2-matrix
(1 −1
0 1
)
for k =j + 1
above the diagonal with the 0 on the diagonal, and deﬁne the entries below
the diagonal to get a skew-symmetric matrix. For example, when 𝓁 = 3
there is only the matrix
E23 =


0 1 −1
−1 0 1
1 −1 0

,
corresponding to dimAµ = 1. Note that for µ = 0, 1,Aµ ={0}. For µ> 3
we can proceed inductively to prove that the matrices Ejk generate:
A =a12E12 + (a12 +a13)E13 +··· + (a12 +··· +a1,µ−1)E1,µ−1 +A′,
with A′∈A µ a matrix with ﬁrst row and column 0 because ∑µ
i=2a1i = 0.
To prove the lemma it thus suﬃces to show that for each A∈A µ satisfying
(∗), als B =A +Ejk satisﬁes (∗). It suﬃces to consider A +Ejk, the result
for A−Ejk is obvious because if A satisﬁes (∗) also−A satisﬁes (∗). For
k > j+ 1 this is easily checked. Note that the coeﬃcients of B are only
changed in the 2× 2-submatrix with upper left position at ( j,k ), and there
it will be ( ajk + 1 aj,k+1− 1
aj+1,k− 1 aj+1,k+1 + 1
)
Contributions in (∗) for B from ai𝓁 with 𝓁<k and i =j,j + 1, ori>j + 1
and 𝓁 = k,k + 1 will not change because ±1 cancel out in si𝓁. So it suf-
ﬁces to consider how (∗) is changing considering the products of bi𝓁 with the
corresponding si𝓁 and i∈{ j,j + 1},𝓁 ∈{ k,k + 1}. Finally, new contribu-
tions in the products (aj,k + 1)(−(aj,k+1− 1)), (aj+1,k− 1)(−(aj+1,k+1 + 1)),
29
(aj+1,k− 1)(ajk + 1) and (aj+1,k+1 + 1)(aj,k+1− 1) will cancel as is easily
checked. The casek =j+1 is similar but involves both the zero column sum
and skew symmetry. In order to avoid too many index consideration we will
discuss the caseµ = 5 andE23 because it shows all necessary considerations.
In this case the upper diagonal part of the matrix B is given by


0 a12 a13 a14 a15
0 a23 + 1 a24− 1 a25
0 a34 + 1 a35
0 a45
0


In this case multiplying out just terms in ajk and sjk within the changed
2× 2-submatrix gives
(a23 + 1)(−(a24− 1)) =−a23a24 +a23−a24 + 1
(a34 + 1)(a24− 1) =a34a24−a34 +a24− 1
Note that the ±a24 and±1 cancel out, the −a23a24 and a34a24 are in the
(∗)-summation for A, so there is a contribution of a23−a34. But the +1 in
the upper left contributes an additional a13, the +1 in the lower right an
additional−a35. So the change in (∗) is given by
a13 +a23− (a34 +a35) = 0,
which follows by considering the zero row sum relation in column 3. The
general argument is completely analogous with a13 and a35 contributions
replaced by corresponding sums.
Proposition 6.2. For each Z-coloring of a signed chord graph, respectively
the corresponding coloring of a part arc-graph inducing this chord graph
coloring,
1
2
∑
c
ε(b +a−r) =
∑
c
εb,
or equivalently ∑
c
ε(a−b) =
∑
c
εr.
Proof. We will consider the equivalent statement for states on signed chord
graphs. The argument will proceed as follows: First the claim is proved for
part arc-graphs without chords joining distinct circles, but allowing distinct
30
components. This corresponds to considering the horizontal multiplication
of braids. Then we will argue that for general chord graphs we can assume
for components j > ithat at all crossings of j and i the component j will
overcross component i. This corresponds to a change of the sign of the
crossing. Finally we will argue that the equation to be proved remains valid
under braid moves corresponding to speciﬁc Reidemeister II and III moves.
This will extend the claim to the general link case. We will work in the free
abelian group generated by variables r representing the chord colors. Then
we can deﬁne an element in the free abelian group for each circle segment
representing a part-arc. The following ﬁgure shows a component with a
self-chord colored r and sign ε. We chose a speciﬁc orientation of the chord
but the computation is similar if the orientation is reversed.
Figure 16
The contribution in the left sum for the chord labeledr isd−(c−r) =r+(d−
c), with c,d not containing anyr, so the contribution of r in∑ε(a−b) isr.
Now the variabler is carried along the segments following the orientation of
the circle in the chord graph. But note that each incoming positive/outgoing
negative chord will both contribute +r and move the horizontal position to
the right. In the same way each outgoing positive/incoming negative chord
will contribute −r while moving to the left. Because we start and end at
k +ε these contributions of r will cancel. This proves the result in the knot
case or more generally in the case of arbitrary braid closures where diﬀerent
components have no crossings. Please check some of the arguments given
in the example tbelow to see e. g. that the choice of β in the potential does
31
not change the equation. In order to discuss the non-trivial link case note
that we can always change crossings and assume that component j always
overcrosses component i for j > i(see the argument in section 4). It will
suﬃce to show that the equation is preserved under special Reidemeister
II braid moves involving distinct components, and arbitrary Reidemeister
III braid moves. Consider the following Reidemeister II move of distinct
components.
Figure 17
If one of the strands is not included at any further mixed crossings then the
corresponding cycle relation is r +s = 0. In the ﬁgure we have a bottom
negative crossing and the top crossing is positive. If we calculate ∑εr the
contribution will be−r +s = 2s =−2r. The contribution in ε(a−b) is
−[(d +r)− (c−r)] + (d−c) =−2r.
If both components of the Reidemeister II move are included in crossings
with distinct components then we can change r1,r 2 to r′
1,r′
2 such that the
equation will hold for the new diagram. We ignore the consideration of any
self-crossings here. Note that the signs at the crossing slabeled r1,r 2 does
not matter. Again it can be checked that the equation will hold for the
right diagram if and only if it holds for the left diagram. The discussion of
Reidemeister III moves is in fact easier because all what has to be made sure
is that the positions of r1,r 2,r 3 in a diagram before a move and after the
move are chosen correctly so that the contributions coincide. The remaining
details are left to the reader.
Example. Figure 18 shows the projection of the long component 2-component
link closure for β =σ1σ−2
2 σ−1
1 σ2.
32
Figure 18
The cycle relation is r1−r2 +r3 +r4 = 0. There are four crossings of
the two components and one self-crossing of the second component. The
base value of the part-arc at the base ∗2 of the second component is set to
0. It is easy to see that changing this value to c⁄= 0 will not change the
computation in the two sums considered in Proposition 6.2. Note that the
signs at the ﬁve crossings from bottom to top are (+ ,−,−,−, +). There
will be a contribution of c in∑ε(a−b) at each mixed crossing at which the
second component crosses from the right and a−c if it crosses from the left.
In fact, the sign of ±c does not depend on the sign of the crossing. If we
change the sign of a crossing then the roles of a and b in the computation
change. At the self-crossing c appears in both a and b. So the reason is
just that we always can set c = 0 is that the crossing number of the second
33
component with the ﬁrst component is even. We calculate
∑
c
ε(a−b) = + [r1− (−r1)]
− [−r1 +r2−r4 +r)− (r1−r2)]
− [(r1−r2 +r3)−r]
− [0− (−r1−r4)]
+ [(−r1−r4 +r− 0]
= r1−r2−r3 +r4 +r
=
∑
c
εr
We were lucky in that we did not have to use the cycle relation again to
get the correct result. Of course we already used it at the third crossing to
simplify. Note that r appears three times but the contributions from a−b
calculated at crossings diﬀerent from the one colored r cancel out.
The statements in the proposition above are non-trivial. They apply
to each state-sum contribution individually. Thus we get the following
strengthened result of Garoufalidis and Loebl including the statement that
the understanding that the two state-sums are equivalent in the sense of
Deﬁnition 2.2. Now consider the arc-graph corresponding to K and the col-
oringf from the set of edges into N0 corresponding to 4.1. The contributing
states are given by restricting values to f(v)∈ n for each vertex v of GK
(see 2.3).
The quantity−ε
2σ =bR is the local excess, and the sum over all vertices
is the excess of the state.
The ﬂow lemma identiﬁes the coloring b in Figure 10 with f(eb
v), and
f(er
v) is the jump r in colors at a crossing c. Recall that overcrossing arcs
are identiﬁed with vertices at their endpoints, so
∑
c
εb =
∑
v
ε(v)f(eb
v).
IdentifyingR =∑
e<erv
f(e) we deﬁne
exc(f) :=
∑
v
ε(v)f(eb
v)
∑
e<erv
f(e),
where we identity R =∑
e<erv
f(e) at each vertex. We use here that R =
a−r. Finally following the deﬁnition of rotation of a statef in [7], Deﬁnition
34
B.6, we deﬁne
rot(f) :=
s∑
i=2
βi(s) =
∑
e′∈T (e)
f(e′).
Here T (e)⁄=∅ only for eb
v,er
v for vertices corresponding to braid generators
at the top of the braid. For eb
v we have T (e) ={eb
v} while for er
v we have
{e : e < er
v}∪{ er
v}. In each case this determines the color of the part arc,
which is a closure arc of the braid diagram. Recall that the βi are the colors
on the part-arcs at the top (or bottom) of the braid-closure diagram. See
also the comments about rotation following the statement of Theorem 6.2.
Finally note that ∑
vε(v) = ω(K) is the writhe of the projection. Let
δ(f) :=−(exc(f) + rot(f)). It follows now from equation (24) and (3) that
each state has an addition total multiplicative contribution of
δ′(K,n ) :=−n2
4 ω(K) +n
2 (s− 1) (11)
Next recall that f(v) =f(eb
v) +f(er
v)
For each braid projectionK of a framed link K and δ(K),δ (f) as above
we letF∗
n(GK)⊂F n(GK) be the set of n-ﬂows, which will induce 0 for the
part arc framing of that part arc, which is the closure arc of the ﬁrst braid
string. This implies f(eb
w) = f(e) = 0 for w the overcrossing arc preceding
the overcrossing arc v containing the bottom part arc of the ﬁrst string.
Heree runs through all red edges preceding the +-marker on the fat vertex
v corresponding tov. If the closure part arc is on an overcrossing circle then
the base value of this circle and all incoming red edge colorings are 0. Now
the following theorem has been proved:
Theorem 6.2. (see [7] for 0-framed long knot projections) The framed
colored Jones polynomial can be calculated from a braid projection K by
the following state-sum:
J′
n(K) =tδ′(K,n) ∑
f∈F∗n(GK)
tδ(f )∏
v
tnε(v)f (eb
v)
(f(v)
f(ebv)
)
t−ε(v)
·
·{n−
∑
e<erv
f(e)}f (erv),tε(v)∈ Z[t±1/4]
(12)
Moreover, each state-sum contributions for this state-sum corresponds to
the state-sum contribution for the state-sum deﬁned for PK deﬁned in [4]
under the bijection of states deﬁned in the ﬂow lemma 4.1. Thus the R-
matrix state model [7] is equivalent to the state models on arc graphs [7] as
deﬁned in 2.2. □
35
For simplicity we have given the proof of the Garoufalidis-Loebl formula
[7] for braid projections. The proof immediately generalizes to all Morse
projections of links. The main diﬃculty is the extension of rotation numbers
to Morse projections following [24], see also [7], Deﬁnition B.6. Each Morse
projection deﬁnes a Gauss map onK by the unit tangent vectors of the
immersions along the components ofK. We know that the value 1∈S1 is a
regular value with preimages the local maxima and minima. The Gauss map
restricts to maps on part arcs and deﬁnes the rotation numbers in{0,±1}
for each part arc with ±1 according to right oriented maxima respectively
minima [25]. If the rotation number of a part arc is ⁄= 0 then we will
indicate this by ± in the boundary of the fat vertex corresponding to the
overcrossing arc containing that part arc. Note that there can be several
part arcs with nontrivial rotation number on a given overcrossing arc. The
inclusion of only right oriented extrema comes from the more general ribbon
functor deﬁnition of sl(2 , C) because those correspond to the insertion of
right oriented evaluation and coevaluation maps. For each state on GK, or
PK, the part arcs carrying nonzero rotation numbers will contribute factors
of t exponentiated by the part arc color for this state. In order to prove
the formula (12) we ﬁrst consider special Morse projections for which at
crossings all strings are directed upwards. Special Morse projections have
additional properties with respect to extrema, e. g. a right going maximum
is immediately followed by a right or left directed minimum on the same
part arc. Which situation occurs is given by the rotation number of that
part arc. So the rotation data controls left-right position on a grid, which
is necessary to generalize the proof of Proposition 6.2 beyond the case of
braid projections. Finally we use that every Morse projection easily can
be isotoped by planar isotopy into a special Morse projection using local
rotations at crossings. It is easy to see that the state-sum contributions will
not change under those rotations.
Remark. (a) For 0-framed links K, J′
n(K)∈ Z[t±1/2]. This follows easily
by the change of variables in Examples 1 and 2 above. Recall that for each
framed link K andr∈ Z we let K(r) denote the link with framing changed
byr twists. Then we have
J′
n(K(r)) =t−r( n2
4 + n
2 )J′
n(K)
For a framed link K with projection and corresponding writhe ω(K) the
writhe is the total framing, and
J′
n(K(−ω(K)) =tω(K)( n2
4 + n
2 )J′
n(K).
36
The unframed (or better framing corrected) version of the colored Jones
polynomial thus is computed from an arbitrary projection by the relation
Jn(K) :=tω(K)( n2
4 + n
2 )J′
n(K).
If we deﬁne
δ(K,n ) :=δ′(K,n ) +ω(K)(n2
4 + n
2 )
= n
2 (ω(K) + s− 1))
and replace δ′(K,n ) by δ(K,n ) we get the state-sum formula for the un-
framed colored Jones polynomial from the theorem. It follows that Jn(K)∈
Z[t±1/2].
Forn = 1 we have the skein relations for framed links:
t−1/4J′(K+)−t1/4J(K−) = (t−1/2−t1/2)J(K0)
and the corresponding writhe normalized for the unframed version:
t−1J(K+)−tJ(K−) = (t−1/2−t1/2)J(K0).
This is not the standard relation for the Jones polynomial derived from
the Kauﬀman bracket but diﬀers by a relative sign of the two sides. It
corresponds to the relation in [7], Appendix B, and [22], Theorem 4.2.1.
Because the number of components of K± and K0 diﬀers by v1 modulo 2
for each skein triple it follows that the corresponding invariants only diﬀer
by sign.
In fact, for the standard skein relation the Jones polynomials of even
number component links carry an additional − sign if the normalization on
the unknot is kept. Since the colored Jones polynomial can be calculated
from n-parallels the sign correction will only occur for n odd (like in the
classical case).
In fact, the mod 2 number of components is nicely related to δ(K,n ) as
follows: Let K = ˆβ and|K| the number of components of K. We assume
that β is a s-braid. Note that the mod 2 number of transpositions in the
permutation carried byβ is equal toω(K), while the number of cycles in the
disjoint cycle decomposition is K. Let 𝓁i be the length of the i-th cycle and
recall that each cycle of length𝓁i can be written with𝓁−i−1 transpositions.
Thus we have the equations:
|K|∑
i=1
(𝓁i− 1)≡ω(K),
|K|∑
i=1
𝓁i = s
37
It follows that if n is even, or |K| + 1≡ ω(K) + s− 1≡ 0 mod 2, or the
number of components of K is odd, then δ(K,n )∈ Z and it follows that
Jn(K)∈ Z[t±1]. On the other hand, if n and|K| are odd then Jn(K)∈
t1/2Z[t±1]. This coincides with the skein relation deduced of J =J1 above.
b) For sl(N + 1) in the fundamental representations the quantum invari-
ants determine the HOMFLY polynomial. In this case the st-condition
translates to ﬂows on GK satisfying the condition: If f(er
v) ⁄= 0 then
f(eb
v) =∑
e<erv
f(e) for N-ﬂows.
(c) LetK be the reﬂected link andK be correspondingly the reﬂected projec-
tion. Then G+K = (G−K), where the bar over the graph denotes switching
the signs of the vertices.
Using this and Jn(K)(t) = Jn(K)(t−1), it is easy to derive a formula
calculating Jn(K) from G−K. It should be noted that the graphs GK and
G(K) are usually very diﬀerent as oriented graphs and thus give rise to
very diﬀerent state-sums calculating the same link polynomial, up to t↦→
t−1. A trivial component contributes t1/2 +t−1/2 for our skein relation but
−(t1/2 +t−1/2) in the standard case.
(d) It should have become clear by now that the arc graph is just an equiv-
alent representation of exactly the data necessary to be taken from the part
arc-graph necessary to deﬁne either of the two state-sums. In fact, after
labeling the overcrossing arcs in cyclic way all what is needed are the jumps
at the crossings for f(er
v) and the part-arc colors of outgoing undercrossing
part arcs for f(eb
v). The real assertion of formula 6.2, or its generalization
to Morse projection, is contained in Propositions 6.1 and 6.2, which are
generalizations of Lemma B.5 in [7] or Lemma 2.1-2.4 in [18]. The main
arguments for n = 1 here are already contained in [24], sections 5 and 6.
It seems that the integration of certain state-sum contributions simpliﬁes
the computation using formula 6.2 over the usual R-matrix formula. The
remaining steps are just rewriting of quantum algebra expressions.
