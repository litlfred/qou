---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-021-61-one-shock
section_title: "One shock"
section_number: 6.1
pages: 32-36
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
First, we will consider the time evolved thermoﬁeld double state perturbed by a single
precursor smeared over the entire boundary sphere
e−iHLtLe−iHRtRW (tw)|TFD⟩. (6.2)
This state is dual to an eternal black hole geometry with a spherically symmetric shock
wave emerging from the boundary at time tw. We will restrict to tw < 0 and tL,tR > 0
so that we study the complexity of the state to the future of the shock wave.
The construction of these geometries has now been covered many places (see, e.g.
[7]), so we will give only a minimal review. We will consider perturbations of global-AdS
black hole geometries inD dimensions. It is convenient to consider Kruskal coordinates,
where the metric is given by
ds2 = −A(uv) 2dudv +B(uv)dΩ2
D−2 + 2A(uv)hδ (u)du2, (6.3)
A(uv) =− 2
uv
f(r)
f′(rh)2, B (uv) =r2, (6.4)
f(r) = 1− 8π
(D− 2)ΩD−2
2GM
rD−3 + r2
𝓁2
AdS
, (6.5)
31
where rh is the horizon radius, and the last term is an ansatz for the backreaction
of the perturbation. The relationship between Kruskal coordinates and Schwarzschild
coordinates is given by
uv =−e
4π
β r∗(r), u/v =−e− 4π
β t, β = 4π𝓁2
AdS
rh(D− 1) + (D− 3)
𝓁2
AdS
rh
, (6.6)
with dr∗ =dr/f (r).
The shock wave is created by acting with the scalar operator W at time tw < 0
smeared over the entire boundary. For large |tw|, this creates a particle of null matter
traveling along u = 0 in the bulk. The expectation value of the stress tensor in this
state is
Tuu = E
𝓁D
AdS
e2π|tw|/βδ(u), (6.7)
with the dimensionless constantE related to theO(1) asymptotic energy of the particle
(see e.g. the Appendix of [53] for details). Plugging Eq. 6.5 and Eq. 6.7 into Einstein’s
equations, we ﬁnd a solution
h∼e
2π
β (|tw|−t∗) (6.8)
where we have deﬁned the fast scrambling time t∗ = β
2π log
𝓁D−2
AdS
G . The main point is
that since boundary time evolution acts as a boost near the horizon, the G suppression
can be overcome by pushing tw further into the past. In this way, a small asymptotic
perturbation can have a large backreaction on the geometry and a large eﬀect on the
complexity of the state. Finally, we note that the metric Eq. 6.5 implies that the
constanth has the interpretation of a shift in the v coordinate byδv =h from crossing
the shock. This means, among other things, that the left and right v = 0 horizons no
longer meet at u = 0.
The Kruskal diagram of this geometry is shown in Fig. 8. 11 The left ﬁgure shows a
geometry with a small shifth, and the right ﬁgure shows a larger shift. The shock wave
is shown as double black lines along u = 0. The Wheeler-DeWitt patch W is drawn in
blue, and the intersection of W and the black hole interior shown is light gray. 12 The
shape of this region (and whether it touches the bottom singularity) is determined by
the boundary times tL,tR and the shift h. Geometrically, we see that for u−1
0 +h<v 0
11Fig. 8 is only really appropriate for D = 2 + 1. For D > 3, the left and right boundaries of
the Kruskal diagram are no longer at uv =−1 [54]. Since this complication does not change the
asymptotic value of the complexity of the state, it will be neglected.
12In this section, we will be interested only in the intersection of W and the Einstein-Rosen bridge.
The portion of W outside of the black hole interior is time independent and divergent. Therefore,
dropping this region is a consistent regularization of the complexity for all of the states that we
consider.
32
Figure 8: Kruskal diagram of one-shock geometries with diﬀerent size shifts. The
double black line along u = 0 is the shock wave. The blue lines show the boundary of
W. The light gray shaded region is the intersection of W and the black hole interior.
The action in this gray region determines the complexity. Left: small shift h with
|tw|− t∗≤tR. Right: large shift h with|tw|− t∗≥tR .
the past going light rays meet in the interior, and for u−1
0 +h > v0 they intersect the
singularity. Here, we have used the deﬁnition of the Kruskal coordinates to deﬁne
u0 =e
2π
β tL, v 0 =e
2π
β tR. (6.9)
Since we are assuming tL > 0, u−1
0 is exponentially small and from now on will be
neglected. This lets us express the condition for W to intersect the past singularity as
|tw|− t∗≥tR.
The complexity will be a function of u0,v 0, and h, since these are the parameters
of the state Eq. 6.2 in reference to the thermoﬁeld double. The geometry of the causal
wedge is diﬀerent depending on the value of these parameters, with a transition at
|tw|−t∗ =tR orh =v0. We expect that the complexityC will be a piecewise continuous
function due to the transition of the geometry of the W at the point h = v0. Using
the results from §3, we could easily compute the rate of change of complexity for
each of tL,tR,tw and then integrate to get the overall complexity. Instead, we will
take a slightly diﬀerent approach. From Fig. 8, we see that either the intersection
ofW with the black hole interior creates a diamond-shaped region bounded on two
sides by the horizons and on two sides by the Wheeler-DeWitt patch or it creates a
ﬁve-sided region bounded by the two horizons, the two edges of the patch, and the
singularity. These two shapes, denoted I and II in Fig. 8, are shown in Fig. 9. Since
v−1
0 =e−2πtR/β≪ 1, the diamond region I is exponentially small Eq. 6.9 and will have
33
Figure 9: Left: diamond-shape region bounded on the top by the horizons and on
the bottom by edges of W. This region will always have vanishing action. Right:
ﬁve-sided region bounded on the bottom by the horizons, on the sides by edges of W,
and on the top by the singularity. The only signiﬁcant contribution to action is from
regions with this shape.
a vanishing contribution to the action. The only important contribution to the action
will come from the ﬁve-sided region II bounded by the singularity.
To proceed, we will compute the action of region II for arbitraryW edges u1,v 1.
Since tL,tR,|tw| > 0, we can safely assume u1,v 1 ≫ 1. The bulk contribution is
straightforward, and we ﬁnd
Abulk =−ΩD−2rD−1
h
πG𝓁2
AdS
β
2π logu1v1. (6.10)
The boundary contributions are from the horizon and the singularity. The edges of W
do not contribute. A calculation similar to that in §3 gives
Aboundary =
[
−
(D− 1
D− 2
)
M + ΩD−2rD−3
8πG
(
(D− 2) + (D− 1) r2
𝓁2
AdS
)]rh
0
β
2π logu1v1,
(6.11)
and the total action in region II is
AII = 2M β
2π logu1v1. (6.12)
With this result in hand, let us consider the one shock geometry with small shift
|tw|− t∗≤ tR (left side of Fig. 8). The only contribution is from the top ﬁve-sided
region II . We can simply plug u1 =u0 and v1 =v0 +h into Eq. 6.12. Using the fact
that v0 >h , we ﬁnd
A|tw|−t∗≤tR = 2M (tL +tR), (6.13)
that is, as if the shock wave wasn’t even there. This is easy to understand; for large
tR we have evolved the state to a region where the backreaction of the perturbation
34
is negligible. The complexity is simply given by the time evolution of the thermoﬁeld
double state.
Now, let’s consider the geometry with large shift|tw|−t∗≥tR (right side of Fig. 8).
Now we have two ﬁve-sided region II s. We get the contribution from the top region
as before by plugging u1 = u0 and v1 = v0 +h into Eq. 6.12. Similarly, we get the
contribution from the bottom region by again using Eq. 6.12, but with u1 =−v−1
0 and
v1 =−u−1
0 −h. (It’s OK to ﬂip it upside down.) This time using the fact that v0 >h
and u−1
0 ≈ 0, we ﬁnd
A|tw|−t∗≥tR = 2M
[
tL−tR + 2(|tw|− t∗)
]
. (6.14)
In this case, the shift h is large, the backreaction of W (tw) is not negligible, and the
perturbation makes a huge contribution to the complexity. Furthermore, the growth of
complexity intw is twice the rate of growth in tL. We can think of this as coming from
the fact thatW (tw) =eiHLtwWe−iHLtw is made up of two time evolution operators each
of which accrues complexity linearly with time.
Additionally, we see that the growth of complexity in tw is delayed by a scrambling
timet∗. From the bulk perspective, this is the fact that we need to push the time of the
shock very far into the past in order to overcome theG gravitational suppression. From
the boundary/complexity perspective, this has been called the “switchback” eﬀect [6].
If W were the identity operator, the two time evolution operators on either side of
W (tw) would cancel. W is not the identity; it is a very simple operator (e.g. a
perturbation of only one of the N 2 degrees of freedom in a lattice site). While the
perturbation is still growing, there will be cancellation between the two time evolution
operators. Fast scrambling dynamics dictate that the inﬂuence of this perturbation
will grow exponentially, covering all N 2 degrees of freedom in a time t∗ = β
2π logN 2.
Since the growth is exponential, almost none of the degrees of freedom are inﬂuenced
until the very end. Thus, there is a delay of t∗ until the complexity can grow. This
was predicted and matched [6] for CV-duality, and here we are showing how simply it
arises for the complexity equals action prescription.
In the next subsections, we will give extensions and related results for complexity
growth in shock wave geometries. However, many of the details of these calculations
will be left to the references and/or the reader.
