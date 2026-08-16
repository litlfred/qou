---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic ﬁelds"
section_id: sec-006-52-magnetic-ﬁelds-constructed-from-yang-mills-po
section_title: "Magnetic ﬁelds constructed from Yang-Mills potential s"
section_number: 5.2
pages: 8-11
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magne tic ﬁelds is presented."
---
As mentioned above we now interpret the three components of the non-Abelian
pure gauge Yang-Mills potential A as potentials of three independent, non-vanishing
magnetic ﬁelds. It is suﬃcient to consider only one of the three pote ntials Ai, since
due to ˆni = xi/||x|| and the cyclic symmetry of equation (30) in the indices i,j,k
all three ﬁelds can be obtained from just one ﬁeld by rotations that map the xi-axes
on one another. From equation (30) we calculate the vector poten tial A3 in spherical
coordinatesx =r sinϑ cosϕ,y =r sinϑ sinϕ, andz =r cosϑ. Using unit basis vectors
er, eϑ, eϕ and ﬁxing a value for the “coupling constant” of q = 2, we ﬁnd
A3 = −2π cosϑ
(1 +r2)3/ 2 er + sinϑ
r sin
( 2πr√
1 +r2
)
eϑ − 2 sinϑ
r sin2
( πr√
1 +r2
)
eϕ. (31)
The corresponding magnetic ﬁeld can be calculated from B3 = ∇ × A3. It is easy to
check that the ﬁelds Bi are well deﬁned and scale as ||Bi(x)|| → 4π2 for r → 0 and
as ||Bi(x)|| → r−4 for r → ∞. Hence, they have no singularity and decay suﬃciently
fast for large radii.
Let us note that the ﬁelds Bi are highly symmetric and similar. Looking at the
vector potential A3 we observe that it is independent of the variable ϕ, therefore B3
is invariant under rotations leaving the x3-axis ﬁxed. Since the potentials (30) are
cyclic in i,j,k it follows that each Bi ﬁeld is invariant under rotations about the xi
axis. We have pointed out before that a rotation that maps the Euc lidian basis vector
ﬁeld e1 to e2 also maps B1 to B2 etc. Furthermore, B3 is similar to the total ﬁeld
B = B1 + B2 + B3 in the following sense: Let R be a rotation that maps the Euclidian
basis vector e3 to the vector
√
3R(e3) = e1 + e2 + e3, then B =
√
3R(B3).
The magnetic ﬁelds Bi are only of interest for us if their third-order invariant does
not vanish. Explicitly calculating Ai for i = 1, 2, 3 we ﬁnd, using the main Theorem,
H (3)(B1, B2, B3) =
∫ ∞
0
4π
r2(1 +r2)3/ 2
(
cos( 2πr√
r2 + 1
) − 1
)
dr = −16π2. (32)
The fact that this integral is non-vanishing proves, that the cons tructed invariant
cannot only be applied to all cases for which we where able to calculate the already
Third-order topological invariant 9
existing invariant, i.e. to three mutually unlinked ﬂux tubes, but also t o examples of
triples of ﬁelds not having disjunct support. It is thus a true gener alization of the
existing invariant known from the Massey triple product.
As we have pointed out before, H (3) is related to the vacuum winding number
W (g) of the connection ω =g−1dg. We easily ﬁnd (see also Frankel 1997)
W (g) := 1
24π2
∫
V
tr(g−1dg ∧g−1dg ∧g−1dg)
= − 1
96π2
∫
V
ǫijkAi ∧Aj ∧Ak (33)
= − 1
16π2H (3)(B1, B2, B3),
where the trace term is usually referred to as the Cartan three-f orm on SU (2).
In the general case the cross-helicities of three magnetic ﬁelds, f or which we are
able to ﬁnd potentials such that ∇ · (Ai × Aj) = Bi · Aj − Ai · Bj = 0, do not have to
vanish. In our example we can easily verify that they do vanish, i.e. H(Bi, Bj) = 0 for
i ⁄=j. Of more interest are the three non-trivial self-helicities. If a trip le of magnetic
ﬁelds is derived from a Yang-Mills vacuum, equation (24) together wit hF = 0 implies
dAi + 1
2ǫijkAj ∧Ak = 0.
Using the deﬁnitions Bi = dAi and Gi =Aj ∧Ak we ﬁnd for ( i,j,k ) cyclic
Bi = −Aj ∧Ak = −Gi.
Thus, for i = 1, 2, 3, we observe that
H(Bi, Bi) =
∫
V
Ai · Bi d3x = −
∫
V
Ai · Gi d3x = −H (3)(B1, B2, B3).
Therefore the self-helicities are equal to the value of the third-or der invariant. This is
a peculiarity of all magnetic ﬁeld triples derived from an SU (2) Yang-Mills vacuum.
In our analysis of the three example magnetic ﬁelds we now turn our a ttention to
the topological structure of the ﬁelds and the linkage of individual ﬁ eld lines. Figure 4
and 5 show numerically integrated ﬁeld lines, where the starting point s for integration
are indicated by the foot points of the arrows that give the ﬁeld line d irection. We
observe that all ﬁeld lines are closed and have an elliptical shape. Figu res 2 and 3
visualize the toroidal structure of the individual ﬁelds at the examp le of B3. Using
A3 =A3
r er +A3
ϑ eϑ +A3
ϕ eϕ and ∂
∂ϕ A3 = 0 it follows that B3 can be written
B3 = ∇ × A3 = 1
r sinϑ ∇(r sinϑA3
ϕ ) × eϕ +B3
ϕ eϕ. (34)
Therefore, the ﬁeld lines of B3 lie on ϕ-invariant toroidal surfaces described by
r sinϑA3
ϕ = const. Figure 2 shows the poloidal B3-ﬁeld and contour lines for three
diﬀerent values of r sinϑA3
ϕ . A toroidal surface with r sinϑA3
ϕ = −1.8 and four ﬁeld
lines on it is drawn in Figure 3. The central ﬁeld line, sitting within all tori is
characterized by B3
r = B3
ϑ = 0. In view of the last equation, this is equivalent to
∇(r sinϑA3
ϕ ) = 0 which yields r =
√
1/3 and ϑ = π/2. We observe that all ﬁeld
lines wind around the central ﬁeld line exactly once. From this and the toroidal
structure of B3 we can conclude that any two arbitrary ﬁeld lines l and l′ of B3 have
a Gauß linkage lk(l,l ′) = 1.
Finally let us discuss the linking properties among ﬁeld lines of diﬀerent ﬁ elds.
To give an example, one ﬁeld line of each ﬁeld is plotted in Figure 4. The sy mmetric
Third-order topological invariant 10
appearance is due to the choice of symmetric starting points for th e ﬁeld line
integration. As was stressed above, the magnetic ﬁelds Bi can be obtained from
one another by cyclic permutations of the Cartesian coordinates xi. In the same way
the integration starting points for the ﬁeld lines γ1,γ2 andγ3 where chosen to be the
cyclic permuted coordinate triples (0 , 0.8, 0), (0, 0, 0.8) and (0.8, 0, 0). It is interesting
that the total linkage of the set of ﬁeld lines is lk( γ1,γ 2) + lk(γ2,γ 3) + lk(γ3,γ 1) = −3.
Even though we have seen that the mutual cross-helicities of all th ree ﬁelds vanish,
Figure 2. The vector plot shows the
projection of the B3-ﬁeld onto the x1-
x3-plane. The arrow lengths are not to
scale. The solid lines are contour levels
with values − 0. 5, − 1, − 1. 8 of the plotted
density distribution r sin ϑA 3
ϕ .
Figure 3. The drawn torus is the
surface at which r sin ϑA 3
ϕ = − 1. 8. All
ﬁeld lines of B3 lie on toroidal surfaces
described by r sin ϑA 3
ϕ = const. Four
ﬁeld lines lying on this torus are drawn.
Figure 4. The three ﬁeld lines γ i
belong to the respective ﬁelds Bi. Their
total linkage is lk( γ 1, γ 2) + lk(γ 2, γ 3) +
lk(γ 3, γ 1) = − 3.
Figure 5. For each ﬁeld line γ 1 and
γ 3 there exists a ﬁeld line ˜ γ 1 such that
lk(γ 1, γ 3) + lk(˜γ 1, γ 3) vanishes.
Third-order topological invariant 11
their individual ﬁeld lines, in general, are linked pairwise. To be more pre cise: If
we e.g. ﬁx one ﬁeld line γ3 of B3, then all ﬁeld lines of B1 and B2 are either linked
withγ3 exactly once or they intersect γ3 twice. For reasons of symmetry, there exists
for each ﬁeld line γ1 of B1 a ﬁeld line ˜γ1 of B1, such that we ﬁnd the total linkage
lk(γ1,γ 3) + lk(˜γ1,γ 3) = 0. Hence, the cross-helicity H(B1,γ 3) vanishes, which in
turn implies H(B1, B3) = 0. Figure 5 shows such ﬁeld lines γ1, ˜γ1 and γ3 with
(0, 0.8, 0), (0, −0.8, 0) and (0 .8, 0, 0) as their respective starting points for the ﬁeld
line integration. Finally let us remark that in the same way as we obtaine d ˜γ1 we
can obtain ﬁeld lines ˜ γ2 and ˜γ3, here with integration starting points (0 , −0.8, 0),
(0, 0, −0.8) and ( −0.8, 0, 0). Together, these three ﬁeld lines yield a conﬁguration
complementary to the one shown in Figure 4, which now has a total link age of +3.
