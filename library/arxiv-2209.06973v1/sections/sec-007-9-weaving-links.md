---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-007-9-weaving-links
section_title: "Weaving links"
section_number: 9
pages: 51-58
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
Recall our notation for a a positive integer, a :={0, 1,...,a − 1}.
In this section we consider only braids with zero writhe and three strands.
In this case the framed and unframed colored Jones polynomial coincide.
The colored Jones polynomial will take values in Z[t±1/2], in fact in Z[t±1]
in the case of knots or n even. For s = 3 we have:
δ(K,n ) =δ′(K,n ) =n.
and vertex contributions for states as in equation (24).
51
We will consider those weaving links, which are deﬁned by the following
alternating 3-braid closures:
(
(σ−1
1 σ2)m)∧
=W (3,m ).
For m≡ 1 mod 3 and m≡ 2 mod 3 the closure of the braid is a knot,
for m≡ 0 mod 3 the closure is a 3-component link. Note that all links
K =W (3,m ) are amphichiral and therefore Jn(K) =Jn(K). Note that for
m = 3𝓁+1 the induced cycle permutation is (132) respectively form = 3𝓁+2
it is (123). In the case of weaving links the cyclic order of overcrossing arcs
byk∈ 2m− 1 will be such that ε(k) = (−1)k+1.
In the following we will focus on an explicit description of the jump maps
τ, rotation and excess, because these are the main ingredients to apply 7.1.
The braid projections are alternating and thus τ is a bijection. For small
𝓁 we can explicitly describe the recursion to determine i from j, and the
inequalities for the sets of contributing states. But in general, it seems
better to just refer to the general formula (17).
(a) Let 𝓁≥ 1 and
K =
(
(σ−1
1 σ2)3𝓁+1
)∧
=W (3, 3𝓁 + 1)
with corresponding long component projection K with 6𝓁 + 2 crossings. For
𝓁 = 0 we have σ−1
1 σ2, which is braid representation of the unknot. It is a
nice exercise to check that the formula gives the polynomial 1 in this case.
We can work with the reduced arc graph and thus describe a contributing
state (in our case τ−1(0) = 2𝓁).
j = (j1,j 2,...,j 6𝓁+1),j 2𝓁 = 0
and
i = (i1,i 2,...,i 6𝓁)
We have fork∈ 6𝓁 + 1:
τ(k) =k + 4𝓁 + 2 mod (6𝓁 + 2),
the modulus is deﬁned in 6 𝓁 + 1, or τ−1(k) = k + 2𝓁 mod(6𝓁 + 2). Re-
call that we set i0 = j0 = 0. The contributing states are described by a
vector of length 6 𝓁 with entries in n subject to 6 𝓁− 1 double inequalities
for contributing states (17). But there is only one inequality for vertex 2 𝓁,
i2𝓁−1 +j4𝓁≤n.
52
Figure 23
We have rot(f) = (i2𝓁 +j4𝓁+1) +i4𝓁+1 and
exc(f) =−
6𝓁+1∑
k=1
(−1)k+1ikiτ (k)−1.
See Figure 21 for the rotation and see the arc graph for the braid projec-
tion of W (3, 4) below in Figure 22. Thus δ(j) = −(i2𝓁 +j4𝓁+1 +i4𝓁+1) +∑6𝓁+1
k=1 (−1)kikiτ (k)−1.
53
Figure 24
For𝓁 = 1 we are calculat-
ing the colored Jones poly-
nomial of the weaving knot
W (3, 4), which is the knot
818. The ﬁgure shows the
long braid representation of
this knot and coloring ac-
cording to [4].
Figure 21 shows the cor-
responding arc graph-graph
according to [7] with color-
ings. Note that it is our spe-
ciﬁc choice of braid (start-
ing with a negative braid
generator and ending with
a positive braid generator),
which allows to discard the
ﬁrst overcrossing arc (which
we label 0). The system of
equations restricting the val-
ues of the vector j by the
non-negativity of the vector
i andn are now obvious from
the ﬁgure. We would like to
point out that working out
the restriction to contribut-
ing states seems the most challenging piece of the computation. In the case
of weaving links this can be reduced to periodicity according to the value of
𝓁. In general we will get a linear system of inequalities restricting the values
to an intersection of half-spaces. For 𝓁 = 1 the system of inequalities can be
reduced in the following way for the coeﬃcients of the vector (see (17)):
j′ = (j1,j 3,j 4,j 5,j 6,j 7)∈ (n + 1)6
j1≤ min{j3,j 4 +j5.j5 +j6}
max{j3 +j4,j 4 +j5,j 5 +j6}≤ n
The main question seems to be to get a direct geometric understanding of
those inequalities in terms of the geometry of the links.
54
Figure 25
(b) Let 𝓁≥ 0 and consider the knots
K =
(
(σ−1
1 σ2)3𝓁+2
)∧
=W (3, 3𝓁 + 2)
with corresponding braid projection K. For 𝓁 = 0 we have (σ−1
1 σ2)2, which
is the ﬁgure eight knot. The next knot in this series is W (3, 5), which is the
knot 10 123. The description of the set of contributing states is very similar
to (a):
j = (j1,...,j 6𝓁+3) with j4𝓁+2 = 0
with i = (i1,...,i 6𝓁+2)∈ (n + 1)6𝓁+2 is determined by (27) with
τ(k) =k + 2𝓁 + 2 mod (6𝓁 + 4)
and the inequalities determining the contributing states are given by (17).
Note that the braid word contains 6 𝓁 + 4 braid generators. Taking into
account j4𝓁+2 = 0 we describe states by vectors with values in n + 1 of
length 6𝓁 + 2. We have
rot(f) = (i4𝓁+2 +j2𝓁+1) +i2𝓁+1
and
exc(f) =
6𝓁+2∑
k=1
(−1)kikiτ (k)−1,
and thus δ(j) =−(i4𝓁+2 +j2𝓁+1 +i2𝓁+1) +∑6𝓁+2
k=1 (−1)kikiτ (k)−1.
(c) Now for m = 3𝓁 and 𝓁≥ 1 we consider the weaving links W (3, 3𝓁) with
3 components. The corresponding braid word includes 6 𝓁 braid generators.
The resulting links are Brunnian, in fact W (3, 3) is the Borromean classical
rings link.
55
The non-negativity requirement for contributing states and basing of 0
on the long strand immediately implies j0 = j6𝓁−2 = 0. The following two
cycle relations have to hold for each coloring (note that the relation for the
ﬁrst component follows from the other two as we know):
j1 +j2 +··· +j2𝓁−1 =j2𝓁 +j2𝓁+1 +··· +j4𝓁−2 +j4𝓁−1
j2𝓁 +j2𝓁+1 +··· +j4𝓁−2 +j4𝓁−1 =j4𝓁 +j4𝓁+1 +··· +j6𝓁−1
We use the equations to eliminate j2𝓁 and j4𝓁 but will use them in sub-
sequent inequalities:
j2𝓁 =j1 +··· j2𝓁−1− (j2𝓁+1 +··· +j4𝓁−1)
respectively
j4𝓁 =j2𝓁 +··· j4𝓁−1− (j4𝓁+1 +··· j6𝓁−1)
=j1 +··· j2𝓁−1− (j4l+1 +··· +j6𝓁−3,j 6𝓁−1)
56
Figure 26
Just like in the knot cases
we can determine the set of
contributing statesF∗
n(GK).
Each contributing state is
determined by a vector
j = (j(1), j(2), j(3),β 1,β 2)
with components in n + 1.
We c(1) = c(2) = c(3) =
2𝓁. The vector i determined
from the system of equations
(27).
Using the base value on
the ﬁrst component and the
two cycle relations above we
can omit the ﬁrst compo-
nents in the vectors j(𝓁), and
so have
j(1) = (j1,...,j 2𝓁−1)
j(2) = (j2𝓁+1,...,j 4𝓁−1)
j(3) = (j4𝓁+1,...,j 6𝓁−3,j 6𝓁−1)
We havej6𝓁− =jτ−1(0) = 0.
These vectors satisfy a
system of inqualities see (17)
determining the contributing
states, in fact one system for
each cycle.
Figure 27 shows the cor-
responding arc-graph.
57
Figure 27
The jump map is given by:
τ(k) =
{
k + 2𝓁 mod 6𝓁 if k = 1,..., 4𝓁− 1
k + 2𝓁 + 2 mod 6𝓁 if k = 4𝓁,..., 6𝓁− 1
Remark. The classical Jones polynomials J(W (3,m )) have also been re-
cently computed by Mishra and Staﬀeldt in [21] using recursion in the Hecke
algebra.
