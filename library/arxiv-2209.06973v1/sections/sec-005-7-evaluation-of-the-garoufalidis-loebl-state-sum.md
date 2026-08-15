---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-005-7-evaluation-of-the-garoufalidis-loebl-state-sum
section_title: "Evaluation of the Garoufalidis-Loebl state-sum"
section_number: 7
pages: 38-47
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
Note that the arc-graphs are abstract enhanced graphs representing the data
necessary to calculate the state-sum (12). For explicit computations it will
be helpful to present the data in non-geometritc way so that it can easily
be implemented as an algorithm.
Suppose thatGK is deﬁned from a Morse projectionK without overcross-
ing circles. The case including overcrossing circles can easily be described
but requires to consider vertices corresponding to the circles separately. For
38
the moment we will work with non-reduced graphs.
The enhanced arc-graphGK can be encoded by a graph sextuple G′K :=
(V,ε,σ,τ, o, r). Here V is the set of vertices of GK and ε is the function
assigning the crossing sign to each vertex (i. e. overcrossing arc) of GK. At
each vertex of GK we have a unique outgoing blue edge eb
v and red edge
er
v. Let σ(v) respectively τ(v) be the endpoints of those directed edges in
GK. This deﬁnes maps σ,τ : V → V , with σ a bijection. We call σ the
undercrossing map and τ the jump map.
Remark. τ is a bijection if and only of K is an alternating projection, in
particular τ−1(v)⁄=∅ for each vertex v in this case, and the inverse map is
deﬁned.
Next, o = (ov)v∈V is a total ordering ov on each of the sets τ−1(v) for
eachv∈V . Note that the order ov also deﬁnes a total ordering on the set of
all incoming edges of the fat vertexv ofGK with the convention thateb
σ−1(v)
precedes er
w for each w∈τ−1(v). Also note that V =⊔vτ−1(v) is a disjoint
union. This is the ordering, which is used in the Pochhammer symbol in
(12). If τ−1(v) =∅ then the overcrossing arc corresponding to v is a part
arc. But if τ−1(v)⁄=∅ then a choice of element w∈τ−1(v) determines the
unique part arc on the boundary of the fat vertex v following the edge er
w,
and thus a unique part arc of PK.
Finally, r is given by two functions rσ, rτ :V →{− 1, 0, 1}. These are the
sums of the rotation numbers of all part-arcs following the transitions σ,τ
from the vertexv. So for σ this is the rotation number of the overcrossing arc
σ(v), for τ this is the sum of the rotation numbers of all part arcs following
v∈τ−1(τ(v)) in the order of τ−1(τ(v)). Consider the left part in Figure 19
below, with v replaced byτ(v). A non-decorated part arc will have rotation
number 0. See 3.1.
Remark. (a) Each part arc-graph or arc-graph determines a quintuple as
above. But not each such quintuple will determine an arc-graph induced
from a part arc-graph.
(b) The unique cycle decomposition of σ will determine the number of com-
ponents ofK. Let µ be the number of cycles in this decomposition.
(c) We let eτ−1(v) :={er
w :τ(w) =v}, and this will be ∅ if τ−1(v) =∅.
(d) Note that at this point we will not work with any particular order on
the vertex set V .
Suppose that the cycle length of the i-th cycle is c(i) for i = 1,...,µ .
Note that c = ∑µ
i=1 c(i) is the number of elements in V , and we let V =
⊔µ
𝓁=1V𝓁 be with V𝓁 be the set of vertices corresponding to the overcrossing
39
arcs of the 𝓁-th component. In order to state the cycle equations from
G′K we need to identify the overcrossings and undercrossings of the 𝓁-th
component with all other components. In fact
⋃
k⁄=𝓁
⋃
v∈V𝓁
τ−1(v)∩Vk
will be the set of vertices corresponding to overcrossings of some overcrossing
arc in V𝓁 with distinct components. Note that these are not vertices in V𝓁.
Similarly
{v∈V𝓁 :τ(v) /∈V𝓁}
corresponds to the set of all crossings at which the component𝓁 undercrosses
a distinct component.
We will next describe how to use the data G′K to construct the set of
contributing states on GK, which we know in natural one-to-one correspon-
dence with the contributing states onPK by the ﬂow lemma 4.1. Next recall
that a potential will be an ordering of the components and a choice of vertex
vi for i = 1,...µ on each cycle of the cycle decomposition of σ, a function
j : V → n + 1, and values βi∈ n + 1 for i = 1, 2,...,µ . We assume that
the function j satisﬁes the cycle equations. For a state f of GK we use the
notation jv := f(er
v), iv := f(eb
v), jτ−1(v) :=∑
w,τ (w)=vf(er
w). Then Figure
19 shows the local picture at each vertex:
Figure 19
The ﬂow equation using the above notation now is
iv +jv =iσ−1(v) +jτ−1(v) (13)
40
This is a recursion to calculate the state colorings from the potential,
for each cycle of σ at a time. We show how to use the recursion to ﬁnd the
function i :V → N0 in the cycle case. Below we will show for a 2-component
example how to ﬁnd the functioni from the function j with base values (0,β )
for the two components.
Now suppose µ = 1 and let c =|V| be the number of crossings of K.
Then for eachv∈V letkv∈ c be the unique number such thatσ−kv(v) =v1.
Suppose that iv1 =β1 is given. Then
iv =iv1 +
kv−1∑
k=0
jτ−1σ−k(v)−jσ−k(v) (14)
The recursion will start with equation (13):
iv =iσ−1(v) +jτ−1(v)−jv
and then substitute the recursion with v replaced by σ−1(v) to substitute
for iσ−1(v):
iv =iσ−2(v) + (jτ−1σ−1(v)−jσ−1(v)) + (jτ−1(v)−jv)
Afterkv steps we have the solution forv. This solution is in fact compatible
because if we apply to v1 the recursion step c times, recall that σ−c(v) =v
since σc = id, then we get
iσ−c(v1) =iv1 +
c−1∑
k=0
jτ−1σ−k(v1)−jσ−k(v1) =iv1
This follows from
c−1∑
k=0
jτ−1σ−k(v) =
c−1∑
k=0
jσ−k(v) (15)
because{σ−k(v) : k = 0,..., c− 1} = V and V =⊔τ−1(v) as we observed
above. Note that formula (14) just formally states how to calculate the part
arc colors from a potential, just following along a component. In the link
case, the above discussion has to be done for each cycle of σ separately, not-
ing that the ﬁnal argument uses the cycle conditions. In fact, in the process
of computing the part arc color by following a component, overcrossings of
distinct components are in the left sum while undercrossing a distinct com-
ponent is in the right hand sum, and those contributions cancel for each
41
component. Thus for each v∈V such that σ−kvv =v𝓁 with 𝓁∈{ 1,...,µ }
we have
iv =β𝓁 +
kv−1∑
k=0
jτ−1σ−k(v)−jσ−k(v) (16)
The contributing states are determined by the n-ﬂow conditions 2.3 for
colorings of GK, and are
iv,jv≥ 0 and iv +jv≤n
for all v ∈ V . These conditions are equivalent, see the proof of 4.1 to
the ﬂows on PK being n-bounded, i. e. all part arc colors take values in
{0,...,n }, see 2.3. Obviously the equations are satisﬁed if for all v∈V :
jv≥ 0,iσ−1(v)≥ 0 and iσ−1(v) +jτ−1(v)≤n,
because the part arc colors along the overcrossing arc v are increasing from
iσ−1(v) to iσ−1(v) +jτ−1(v), then jump down to iv. The last inequalities are
equivalent to
jv,iv≥ 0 and iv≤n−jv
So, using the recursion (16) we get the system of inequalities for each v∈V
in terms of the potential, for all v𝓁⁄=v∈V , 𝓁∈{ 1,...,µ } depending on v,
0≤jv≤β𝓁 +jτ−1(v) +
kv−1∑
k=1
jτ−1σ−k(v)−jσ−k(v)≤n
0≤jv𝓁,β𝓁 and β𝓁 +jv𝓁≤n for the starting vertex v𝓁
(17)
Note that the part arc coloring preceding the base vertex on the 𝓁-th
component isiσ−1(v𝓁) +jτ−1(v𝓁)≤n becauseiσ−1(v𝓁) +jτ−1(v𝓁)−jv𝓁 =β𝓁 and
the part arc color following the crossing v𝓁 is just β𝓁.
Deﬁnition 7.1. A return loop at the self-crossing v∈ V𝓁 is a loop in PK
starting at vertexv on the overcrossing arc in the direction of the orientation,
following the link until it returns to v. The number of overcrossing arcs
except the one at which the loop starts is the number k (modulo c(𝓁)) in
σkτ(v) = v ⇐⇒v = τ−1σ−k(v). For k = 0 the return loop follows an
overcrossing arc until its return to v. This is a circle in PK, which could be
eliminated by isotopy,
Figure 20 shows three return loops.
42
Figure 20
Note that for k = 0 the inequality
jv≤av +j1 +... +js≤n
holds. For k> 0 such an equation is
jv≤av +j1 +...j s− (j′
1 +...j ′
k≤n
Ofjs =j′
t can occur (likej2 =j′
1 in the right ﬁgure of Figure 20). Then there
will be a shorter return loop contained in the original loop. Aminimal return
loop is a loop, which does not contain shorter return loops. The system of
inequalities for contributing states seems to contain geometric information
about return loops in the part arc graph. The study of the geometry of
43
return loops reminds of the purely inductive arguments in [20] proving the
existence of the Homﬂypt polynomial.
In order to determine F∗
nGK in 6.2 for a long component projection,
note that the part arc color 0 on the part arc corresponding to the long
half arcs in general does not imply β1 = 0 if we take for the base vertex
on the ﬁrst component, which we choose to be the long one, but in fact it
will imply that the vertex preceding this bottom vertex has color 0. This
follows because overcrossing can only increase the colors. So depending on
the projection this will imply that the jumps are zero up this part-arc. To
simplify, and actual be able to work with the reduced graph we assume that
the ﬁrst crossing of the bottom long arc is an undercrossing and is the base
vertex of the ﬁrst cycle. This will imply β1 = 0 because at the base crossing
the value can only decrease. This implies jv1 = 0 and by the ﬂow condition
of course also that iσ−1(v1) =jτ−1(v1) = 0. Note that jτ−1(v) = 0⇐⇒jw = 0
for all w∈ τ−1(v). But note that iw ⁄= 0 is possible for w∈ τ−1(v) in
this case (and thus also iσ−1(w) and jτ−1(w) can be nonzero for w∈ τ−1(v)
in this case), so these vertices cannot be discarded. If we delete the base
vertex on the long component including all edges of GK incident to that
vertex we will not change state contributions because 0-colorings factor in
as multiplication by 1. While computationally comfortable, some of the
symmetry is lost because τ is no longer deﬁned for the vertices in τ−1(v1).
Also σ will no longer be deﬁned on σ−1(v1) if we delete the base vertex v1.
In all recursively deﬁned formulas we will still include the base vertex v1 so
that the maps σ,τ are always deﬁned.
Let V∗ := V \ ({v1}∪ τ−1(v1)) and V′ := V \{v1}. Then we can
parametrize the set of contributing states as follows:
F∗
nGK↔{ j := (jv,β𝓁) :v∈V∗,𝓁 = 2,...µ, (17), cycle relations 3.3} (18)
In order to write formula 6.2 for the data G′K from a long component pro-
jection we need to determine the contributions from right oriented extrema.
For this let v∈V∗ deﬁne
rot(v, j) = rτ(v)jv + rσ(v)iv (19)
and
rot(j) :=
∑
v∈V∗
rot(v, j)
Remark. In order to see that rot(j) for a state determined byj and Deﬁnition
(19) determines the contributions resulting from right oriented extrema,
44
consider ﬁrst a right oriented extremum on an overcrossing arc σ(v), and
assume that this is the only right oriented extremum on the overcrossing
arc. The part arc color of the part arc containing the maximum is given by
iv +∑jw, where the sum runs through those w∈τ−1(σ(v)) preceding the
maximum. Recall from above that a choice of element in τ−1(v) determines
a unique part arc if τ−1(v)⁄=∅, and otherwise there is only one part-arc on
the given overcrossing arc. The contribution iv = rσ(v)iv, while the jw are
contributions rτ(w)jw for the w along the overcrossing arc σ(v) preceding
the maximum. It is not hard to see that the result for the rotation of a
state persists, even though contributions for individual extrema will show
up diﬀerently in the formula for rot( j) given above. For example, if right
oriented maximum is followed by an right oriented minimum, then the part
arc color before the maximum will count with factor +1 while the part arc
color before the minimum will contribute with factor−1 in the deﬁnition by
ribbon functor [17]. In the formula for rot(j) given above this will be counted
correctly because in this case, if no further right oriented extrema follow on
the part arc considered, the rotation numbers of part arcs preceding the
maximum will be 0. In the braid projection case this cannot occur but it
is possible to have overcrossing arcs rotating through several maxima, in
which case the above analysis similarly proceeds.
Finally the last item to be considered is the excess of a state in terms of
the potential. We will use the following deﬁnition for v∈V :
˜jv :=
∑
w∈τ−1(τ (v))
w<v
jw +iσ−1(τ (v)) (20)
Then
exc(j) :=
∑
v∈V∗
ε(v)iv˜jv (21)
Let
δ(j) :=−(exc(j) + rot(j). (22)
We can now restate Theorem 6.2 using the graph sextuple G′K. Note
that this description does not use any ordering of the vertex set V . For a
long component projection rot(K) let the rotation number ofK be the sum
of the rotation numbers of all components. This is a sum over the rotation
numbers of all part arcs and thus is also the sum of the rotation numbers of
all circle components resulting from smoothing all crossings. Let
δ′(K,n ) :=−n2
4 ω(K) +n
2 rot(K). (23)
45
Note that our rotation numbers are positive in clockwise direction.
Theorem 7.1. LetK be a long component projection of an oriented link K
with data quintuple G′K and δ′(K,n ) deﬁned in equation (23). Let
βn(j) =
∏
v∈V′
βn(j,v )
for j∈F∗
nGK as deﬁned in (18), and for each v∈V∗
βn(j,v ) =tnε(v)iv
(iv +jv
iv
)
t−ε(v)
{n− ˜jv}jv,tε(v) (24)
with ˜jv deﬁned in (20). Then
J′
n(K) =tδ′(K,n) ∑
j∈F∗nGK
tδ(j)βn(j) (25)
Remark. (a) The appearence of n
2 rot(K) is a consequence of evaluation maps
at extrema, see e. g. the deﬁnition of the endomorphism K in [4], p. 1264 or
Theorem 5.3.2 in [3].
(b) Note that the representation of the colored Jones polynomial in 7.1
references only the vertex set of GK, which is identiﬁed with the crossings
ofK and deﬁned by overcrossing arcs of PK. We did reduce the reference
to edge colorings to the computation of blue edge colors from the potential.
(c) Note that the Potts model on a graph is deﬁned from colorings of vertices.
Even though the
(d) We have purposefully not introduced any ordering of vertices in this
section. Given an ordering and basing of the components of a projection
there is a natural cyclic ordering by running along components starting
from the basepoint. Also, if the projection is a closed braid projection in
the plane starting from a given braid word then the crossings are naturally
ordered by each braid generator corresponding to a crossing. If O is any
ordering of V then there is a natural K-twisting of this order given by the
orderings ov for each v∈ V . If O orders the vertices as {v1,...,v c} then
the ordering is given by the elements in τ−1(vi) ordered by ovi as above
preceding the elements in τ−1(vi+1) ordered by ovi+1. This could be related
to Deﬁnition 5.1 in [7].
(e) IfK is an alternating link projection then, in the non-reduced descrip-
tion, τ−1(v) consists of a single element and the orderings oi are trivial. In
particular in the alternating case the ˜jv reduces to ˜jv = iσ−1(τ (v)) so that
the Pochhammer symbol and also the excess are easier to calculate.
46
