---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-006-8-working-with-cyclic-ordering
section_title: "Working with cyclic ordering"
section_number: 8
pages: 47-51
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
In the following we assume that our projection K is based and we consider
the cyclic ordering with respect to the basing. This deﬁnes a bijection
V ↔ c− 1 with c denoting the number of crossings. The base vertex on the
ﬁrst component is labelled 0 by the order because it is deleted in reduced
graphs. We will usually identify vertices with their order labeling. The
parametrization of the set of states is now given by integer valued vectors
j = (j0,...,j c−1), possibly with components removed, or just set equal to 0,
in the reduced case. The vector i = (i0,...,i c−1) is similarly deﬁned.
With respect to this ordering the undercrossing map has a simple de-
scription σ is now given by
σ(k) =k + 1 mod (c− 1),
where we will as usual think of amod b for integers a,b and b > 0 as an
element in b ={0, 1,...,b − 1}. Theorem 7.1 can be rewritten, now writing
ik,jk,ε (k) etc. for iv,jv,ε (v) if v is the vertex k. The jump map τ now
becomes a map
τ : c→ c.
Recall that this a bijection if and only if K is an alternating projection.
In the case of a link of µ > 1 components some more notation will
be necessary. Suppose that the number of overcrossing arcs on the 𝓁-th
component is c(𝓁). Then deﬁne
d(𝓁) := c(1) +··· + c(𝓁)
for𝓁 = 1,...,µ , and let c(0) := 0. Then we enumerate the overcrossing arcs
on the 𝓁-th components in the following way
d(𝓁− 1), d(𝓁− 1) + 1,..., d(𝓁)− 1
In the reduced case we have i0 = 0 and ic(𝓁−1) =β𝓁 is determined by the
potential for 𝓁 = 2,...,µ . As explained in section 7 we can determine the
colors ik from the vector
j = (j1,...,j c−1)
Note that he vector is partitioned by components into j = (j(1),..., j(µ))
with
j(1) = (j1,...,j d(1)−1)
and for 𝓁≥ 2,
j(𝓁) = (jd(𝓁−1),...,j d(𝓁)−1) (26)
47
We always have to take into account theµ−1 cycle relations. In order to
determine these we have to ﬁrst ﬁnd for each 1≤𝓁≤µ those numbersk for
which the corresponding overcrossing arc ends at a crossing of distinct com-
ponents, say for a ﬁxed 𝓁 these are k1,...,k ρ. Finally we have to determine
for which overcrossing arcs k, τ−1(k) is an overcrossing arc of a component
distinct from the 𝓁-th, say those are m1,...,m ρ′. Then the cycle relation
for the 𝓁-th component is
ρ′
∑
r=1
jτ−1(mr)−
ρ∑
r=1
jkr = 0
Note that ρ +ρ′ is always an even number. The system of equations to
ﬁnd i from j, given ic(k−1) for k = 2,...,µ is given by the ﬂow equations,
equalities to determine the contributing states then are found as explained
in section 7.
We will now brieﬂy show how to ﬁnd the set of contributing states for
a 2-component alternating braid projection K = ˆβ. We assume that the
ﬁrst appearance of the braid generator σ1 will be corresponding to vertex 0
and comes as σ−1
1 . This will allow us to work with the reduced graph. Let
τ−1(0) =:κ.
We have crossings 0, 1,..., c(1)− 1 along the ﬁrst component, and
c(1),..., c− 1 with c = c(1) +c(2) along the second component, the number
of crossings of K. The potential is given by ( j,β 2) and we assume that
β2 = ic(1). Fiigure 21 shows the arc-graph for a 2-component alternating
link.
Figure 21
We havei0 =ic(1)−1 =j0 =jκ = 0 by the choice of braid. Furthermore
we have ﬂow equations (13) for k = 0,... c(1)− 1, and as before from the
48
vertices of the ﬁrst component, see equation ((15)):
c(1)−1∑
k=1
jτ−1(k−1)−jk = 0.
In the alternating 2-component case this is not obvious, even though τ
is a bijection of c. This is because when the ﬁrst component overcrosses the
second component at vertex k thenτ−1(k)∈ c(1) + c(2) ={c(1),..., c− 1},
while at an undercrossing of the second component τ(k)∈ c(1) + c(2). But
the above relation holds anyway because of the cycle condition. Thus i0 = 0
still implies
ik =
k∑
𝓁=1
jτ−1(𝓁)−j𝓁 (27)
for k = 1,... c(1)− 2, and ic(1)−1 = 0. Finally the ﬂow equations and
base value at the vertices corresponding to the second component will give
ic(1) =β2 and
ik =ic(1) +
k∑
𝓁=c(1)+1
jτ−1(𝓁)−j𝓁
for k = c(1) + 1,..., c− 1. Again, the cycle equation is necessary to show
that the solution of the system of ﬂow equations is consistent. Note that
ﬂow equation at the ﬁrst vertex of the second component holds
β2 =ic(1) =ic−1 +jτ−1(c(0)−jc(0)
because of the cycle relation, compare the arguments following Deﬁnition
3.3, where we explain how a state is deﬁned from the potential. Note that
withj0 =jκ = 0 we reduce the red colors at arc-graph vertices corresponding
to the ﬁrst component to c(1)− 2. Now we have a choice of β2 and a cycle
relation for the red colors at arc-graph vertices of the second component.
Usually this will allow to eliminate of those red colors from the cycle relation
and end up with a total of c− 2 colorings determining a contributing state,
of course with restrictions given by 0≤ i + j≤ n as before. But if the two
components split and have no crossings this is not the case, in this case we
need c− 1 colors. Also if one of the components is completely crossing over
the other component the red colors for those crossings all have to be 0. In this
case we only need c′−1 = c′(1)+ c′(2)−1 colors to determine a contributing
state, where c′(𝓁) is the number of self-crossings of the 𝓁-th component for
𝓁 = 1, 2. Note that the requirement 0≤ j≤ n in combination with cycle
49
conditions will often reduce the dimension of the space of red colors giving
contributing states. But e. g. the case of the Hopf link σ−2
1 shows that the
answer in general can be c− 1.
Example. Let β = σ−6
1 and s = 2. Then K = β∧ is a 2-component link
projection for a link with linking number −3. Note that ω(K) =−6. The
set of contributing states then can be described as the set of ( j1,j 3,j 5,β )
such that 0≤j3,β≤n and
max(0,j 3−β)≤j1≤j5≤ min(n +j1−j3,n−β)
It is interesting to count the contributing states for ﬁxedβ = 0, 1,...,n . For
example when β =n it follows that j1 =j5 = 0 but j3 can take any values
0, 1,...n , so we have n + 1 states. On the other hand when β = 0 then the
inequalities reduce to 0≤j3≤j1≤j5≤n. So there are 1
6(n+1)(n+2)(n+3)
states for β = 0. (Here we use the usual way to enumerate the overcrossing
arcs).
50
Figure 22
