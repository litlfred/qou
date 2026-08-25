---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S3 R. Komendarczyk ∗"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-23
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
A purpose of this paper is to develop a particular formula for the thir d order helicity on
certain invariant sets of a volume preserving vector ﬁeld X. The third order helicity, [3],
is an invariant of X under the action of volumorphisms isotopic to the identity (denoted
here by Diﬀ vol
0 (M)). Importance of such invariants stems from the basic fact that e.g. the
evolution of the vorticity in the ideal hydrodynamics or the magnetic ﬁeld B0 in the ideal
magnetohydrodynamics (MHD), occurs along a path t − →g(t) ∈ Diﬀ vol
0 (M), [3, p. 176].
Namely, B(t) = g∗(t)B0 which is a direct consequence of Euler’s equations:
d
dt B + [v, B] = 0 , d
dt g(t) = v. (1)
One often says that the magnetic ﬁeld B is frozen in the velocity ﬁeld v of plasma, the
action by Diﬀ vol
0 (M) is often referred to as frozen-in-ﬁeld deformations. The fundamental
example of such invariant deﬁned for a general class in Vect vol(M) is the helicity H12(X1, X2)
deﬁned for a pair of vector ﬁelds X1 and X2 on M = S3 or a homology sphere. Helicity has
∗ Department of Mathematics, University of Pennsylvania; e-mail: rako@math.upenn.edu. This project is
supported by DARPA, #F A9550-08-1-0386.
1
been ﬁrst introduced by Woltjer, in the context of magnetic ﬁelds, and is a measure of how
orbits of X1, and X2 link with each other. This topological interpretation of helicity has
been made precise by Arnold, who introduced (in [2]) the concept of t he average asymptotic
linking number of orbits for a pair volume preserving vector ﬁelds on M and proved that
it is equal to their helicity. The subject has been further developed in [5, 1, 28, 20] (see [3]
for additional references), where authors approach higher helicities via the Massey products
under various assumptions about the vector ﬁelds or their domains (work in [16, 29] con-
cerns other approaches to the problem). In this paper we presen t an alternative to these
approaches, which is a natural extension the notion of the linking nu mber as a degree of a
map, and exploits relations to the homotopy theory of certain maps associated to the link.
The paper has two parts:
In the ﬁrst part we show how the Milnor ¯ µ123-invariant: ¯µ123(L) of a parametrized bor-
romean link L in S3 can be obtained as a Hopf degree of an associated map to the conﬁg u-
ration space of three points in S3. The presented approach to link-homotopy invariants of
3-component links has been proposed in [18] for n-component links in R3, and conveniently
simpliﬁed for 3-component links in S3 in the joint work [13], where the full correspondence
between ¯µ123(L) and the Pontryagin-Hopf degree is proved. In Section 2 we prese nt the orig-
inal proof of this correspondence in the borromean case, which is s uﬃcient for our purposes.
The second part of the paper is concerned with a new deﬁnition of th e third order helicity
denoted here by H123(X; T ), where X is a volume preserving vector ﬁeld having an invariant
unlinked domain T ⊂ S3. The simplest of such domains are three invariant handlebodies
in S3 which have pairwise unlinked cycles in the ﬁrst homology. This includes t he case of
borromean ﬂux tubes already investigated in e.g. [5, 20]. In Section 5 we develop an ergodic
formulation of H123(X; T ) as an average asymptotic ¯ µ123-invariant in the spirit of Arnold’s
asymptotic linking number, which allows us to extend the deﬁnition of t he invariant to
topologically more complicated unlinked domains. We also indicate that H123(X; T ) provides
a lower bound for the L2-energy of X.
Acknowledgements: My inspiration for the presented approach to the link-homotopy inv ari-
ants comes from the Toshitake Kohno paper, [18], whom I am grate ful for the valuable
e-mail correspondence. I have enjoyed conversations with many colleagues at the University
of Pennsylvania, who have inﬂuenced this work. I wish to thank Herm an Gluck for weekly
meetings and his interest in this project, Frederic Cohen, Dennis De Turck, Charlie Epstein,
Paul Melvin, Tristan Rivi` ere, Clay Shonkwiler, Jim Stasheﬀ, David Sh ea Vick for the valu-
able input. I am also grateful to my advisor Robert Ghrist who introd uced me to the subject
long time ago.
The author acknowledges ﬁnancial support from DARPA, #F A9550 -08-1-0386.
2 The Milnor ¯µ123-invariant and the Hopf degree.
The ¯µ-invariants of n-component links in S3 have been introduced by Milnor in [23, 24]
as invariants of links up to link-homotopy, recall that the link homotopy is a deformation
2
of a link in S3 which allows each component of the link to pass through itself but not
through a diﬀerent component. Clearly, this is a weaker equivalence than the equivalence
of links up to isotopy where components are not allowed to pass through themselves at a ll.
The fundamental example of a ¯ µ-invariant is the linking number (denoted by ¯ µ12) which
is a complete invariant of the 2-component links up to link homotopy. I n the realm of
3-component links the relevant invariants are the pairwise linking num bers ¯µ12, ¯µ23, ¯µ32,
and the third invariant ¯µ123 in Zgcd(¯µ12,¯µ23,¯µ32), which is a well deﬁned integer if and only if
¯µ12 = ¯µ23 = ¯µ32 = 0. In the second part of the paper we will interpret this statemen t as a
topological condition on the invariant set of a vector ﬁeld. A precise deﬁnition of ¯µ-invariants
is algebraic and involves the Magnus expansion of the lower central s eries of the fundamental
group: π1(S3 − L) of the link complement. We refer the interested reader to the wor ks in
[23, 24]. In the remaining part of this section we will prove that ¯ µ123(L) is a Hopf degree for
an appropriate map associated to the link L, provided that the link is borromean, i.e. the
pairwise linking numbers are zero (note that the borromean links are more general then so
called Brunnian links, [23]).
Let us review basic facts about the Hopf degree H (f ) of a map f : S3 − →S2, (see e.g.
[6]). The well known property of the Hopf degree is that H : f − →H (f ) provides an
isomorphism between π3(S2) and Z. Recall that, up to a constant multiple, we may express
H (f ) as ( M = S3)
H (f ) =
∫
M
α ∧ f ∗ν =
∫
M
α ∧ ω =
∫
M
α ∧ dα, (2)
where ν is the area 2-form on S2, and α satisﬁes ω = f ∗ν = dα. Notice that f ∗ν is always
exact since the cohomology of S3 in dimension 2 vanishes (i.e. H 2(S3) = 0). We may also
interpret H (f ) as an intersection number, [6, 25]. Namely, consider two regular va lues p1
and p2 ∈ S2 of the map f , then l1 = f −1(p1) and l2 = f −1(p2) form a link in S3, and the
integral formula (2) can be interpreted, as the intersection numb er of l1 with the Seifert
surface spanning l2:
H (f ) = lk( l1, l2) . (3)
If we replace S3 with an arbitrary closed compact orientable 3-dimensional manifold M, we
may still obtain an invariant of f : M − →S2 this way, provided that the condition f ∗ω = dα
holds.
Proposition 2.1. Let M be a closed Riemannian manifold, and ν ∈ Ω 2(S2) the area form
on S2. The formula (2) provides a homotopy invariant for a map f : M − →S2, if the 2-form
f ∗ν is exact. Up to a constant multiple this invariant can be calc ulated as an intersection
number deﬁned in (3), where l1 = f −1(p1) and l2 = f −1(p2) form a link in M, where both l1
and l2 are null-homologous.
Proof. Given a homotopy F : I × M ↦→S2, f1 = F (1, · ), f0 = F (0, · ), we deﬁne ˆω = F ∗ν.
3
We have
ˆω = F ∗ν = d ˆα,
ω1 = f ∗
1 ν = i∗
1 F ∗ν = d α1,
ω0 = f ∗
0 ν = i∗
0 F ∗ν = d α0,
where i0 :֒→ M × I, i0(x) = ( x, 0), i1 :֒→ M × I, i1(x) = ( x, 1) are appropriate
inclusions. The “potentials”: ˆα
⏐
⏐
{0}×M , α0, and ˆα
⏐
⏐
{1}×M , α1 diﬀer by a closed form
ˆα
⏐
⏐
{0}×M −α0 = β0, ˆα
⏐
⏐
{1}×M −α1 = β1, dβ 0 = dβ1 = 0,
therefore the Stokes Theorem immediately implies that Formula (2) is independent of the
choice of the potential. For the proof of invariance we repeat the s tandard argument in [6,
p. 228]
0 =
∫
F (M ×I)
ν ∧ ν =
∫
M ×I
ˆω ∧ ˆω =
∫
M ×I
ˆω ∧ d ˆα
=
∫
M ×I
d(ˆω ∧ ˆα) =
∫
∂(M ×I)
ˆω ∧ ˆα .
Thus,
0 =
∫
∂(M ×I)
ˆω ∧ ˆα =
∫
M
ω1 ∧ α1 −
∫
M
ω0 ∧ α0
=
∫
M
dα1 ∧ α1 −
∫
M
dα0 ∧ α0 = H (f1) − H (f0).
The interpretation of H (f ) as the intersection number (3) is the same as in [6, p. 230].
Given a 3-component parametrized link L = {L1, L2, L3} in S3 we wish to associate a certain
map FL : S1 × S1 × S1 ↦→S2 to it, and interpret its Hopf degree as the Milnor ¯ µ123-invariant.
Recall, the deﬁnition of the conﬁguration space of k points in M:
Conf(M, k) := {(x1, x2, . . . , xk) ∈ (M)k | xi ⁄= xj, for i ⁄= j}.
As an introduction to the method we review the Gauss formula for th e linking number
of a 2-component link L = {L1, L2} in R3. Denote parameterizations of components by
L1 = {x(s)}, L2 = {y(t)} and consider the map
FL : S1 × S1 L
− →Conf(R3, 2)
r
− →S2, L (s, t) = ( x(s), y(t)) .
where r(x, y) = x−y
‖x−y‖ is a retraction of Conf( R3, 2) onto S2. It yields the classical Gauss
linking number formula, up to a constant multiple:
lk(L1, L2) = deg( FL), deg(FL) =
∫
S1×S1
F ∗
L(ν),
4
where ν ∈ Ω 2(S2) is the area form on S2. Consequently, the linking number lk( L1, L2), also
known as the Milnor ¯ µ12-invariant, can be obtained as the homotopy invariant of the map
FL associated to L. Notice that homotopy classes [ S1 × S1, S2] are isomorphic to Z and
deg : F → deg(F ) provides the isomorphism. In [18], Kohno proposed a natural ext ension
of this approach to n-component parametrized links L in R3 by considering maps FL : S1 ×
. . . × S1 − →Conf(R3, n) and their homotopy classes. More speciﬁcally, he proposed speciﬁ c
cohomology classes of the based loop space of Conf( R3, n) as candidates for appropriate link-
homotopy invariants of L. In [13], it has been observed that, in the 3-component case it is
beneﬁcial to consider Conf( S3, 3), and L ⊂ S3, since the topology of Conf( S3, 3) simpliﬁes
dramatically (in comparison to Conf( R3, 3)). We review this simpliﬁcation in the following
paragraph as it is essential for the proof of the next theorem.
Consider a 3-component link L = {L1, L2, L3} in S3 parametrized by {x(s), y(t), z(u)}
and the following map
FL : S1 × S1 × S1 L
− →Conf(S3, 3)
H
− →S2, L (s, t, u) = ( x(s), y(t), z(u)) . (4)
In order to explain the map H : Conf( S3, 3) − →S2, one must notice that Conf( S3, 3) ⊂
S3 × S3 × S3 is diﬀeomorphic to S3 × Conf(R3, 2) = S3 × R3 × (R3 \ {0}), and consequently
deformation retracts onto S3 × S2. Denote by H : S3 × R3 × (R3 \ {0}) ↦→S2 the projection
on S2 factor. Considering S3 as unit quaternions, the map H can be expressed explicitly by
the formula, [13]:
Conf(S3, 3) ∋ (x, y, z)
H
− → pr(x−1 · y) − pr(x−1 · z)
‖pr(x−1 · y) − pr(x−1 · z)‖ ∈ S2, (5)
where · stands for the quaternionic multiplication, −1 is the quaternionic inverse, and pr :
S3 − →R3 the stereographic projection from 1. As a result one has the follow ing particular
expression for FL:
FL(s, t, u) = pr(x(s)−1 · z(u)) − pr(x(s)−1 · y(t))
‖pr(x(s)−1 · z(u)) − pr(x(s)−1 · y(t))‖.
At this point we note that one has a freedom in choosing the deforma tion retraction H in (5)
but this particular formula makes the proof of the main theorem of t his section possible. By
the borromean rings we understand any 3-component link with ¯ µ123 = ±1 link homotopic
to a link with diagram presented on Figure 4 (where the sign can be det ermined from the
orientation of components).
Theorem 2.2. Let LBor = {L1, L2, L3} be a 3-component link in S3 link homotopic to the
Borromean rings, and consider the associated map FLBor : S1 × S1 × S1 − →S2 deﬁned in
(4). Then the Hopf degree of the map FLBor satisﬁes
H (FLBor) = ±2, (6)
where the sign depends on the choice of orientations.
5
Proof. According to Proposition 2.1, H (FL) is well deﬁned for a link L ⊂ S3 provided
F ∗
Lν ∈ Ω 2(T) is trivial in H 2(T), T = S1 × S1 × S1. This fact will follow from the proof,
but we will show in Corollary 2.5, that it holds if and only if the pairwise linkin g numbers
of L are zero. The method relies on a direct calculation of H (FLBor), for a carefully chosen
parametrization of LBor in S3. This calculation is achieved by visualization of the link
lS,N = lS ∪ lN in T, and application of Formula (3), where
lS := F −1
LBor(S), l N := F −1
LBor(N)
are preimages of the North pole N = (0 , 0, 1) and South pole S = (0 , 0, −1) in S2. Notice
that [ F ∗
Lν] = 0 in H 2(T) if and only if [ lS] = 0 and [ lN ] = 0 in H1(T).
We identify S3 with the set of unit quaternions in R4 with standard coordinates:
(w, x, y, z) = w + x i + y j + z k,
and choose a speciﬁc parametrization of the Borromean rings LBor in S3, as follows: deﬁne
the L1 component of LBor to be the great circle through 1 in S3, parametrized as
x(s) = cos( s) + sin(s) k,
(
x(s)−1 = cos(s) − sin(s) k
)
.
Notice that pr( x(s)) parameterizes the z-axis in R3. Because
x(s)−1 · (w, x, y, z) =
(
cos(s)w + sin(s)z, cos(s)x + sin(s)y,
cos(s)y − sin(s)x, cos(s)z − sin(s)w
)
,
we observe that multiplication by x(s)−1 is a rotation by angle s in ( w, z)-plane and ( x, y)-
plane of R4 , and the ﬂow deﬁned by this S1-action is tangent to the great circles of S3.
Consequently, the projected ﬂow on R3 via the stereographic projection pr : S3 ⊂ R4 − →R3
presents the standard picture of the Hopf ﬁbration, and the S1-action “pushes” points in R3
along Hopf circles.
Let us call a Hopf torus in R3 the r-torus if and only if it contains a circle of radius r
in the ( x, y)-plane and is invariant under the S1-action. Figure 1 shows how to deﬁne the
second and the third component {L2, L3} of the Borromean rings LBorr in the stereographic
projection. L2 will be the annuli with a rounded wedge removed, i.e. an arc A1 of the
circle of radius 1 and A2 arc belongs to the circle of radius rǫ = (1 + ǫ) in the ( x, y)-plane.
The component L3 is chosen to be a vertical ellipse linking with L2, which belongs to the
rǫ/2-torus, and projects on the ( x, y)-plane as a segment. Recall that every point on an
r-torus traces a (1 , 1)-curve under the S1-action. This motion, for suﬃciently small ǫ, can
be regarded as a composition of the rotation by angle s in both the direction of the meridian
and the longitude of an r-torus. Therefore for diﬀerent values of s the S1-action “rotates”
the components L2 and L3, by sliding along the Hopf tori by angle s in the meridian and
the longitudinal direction, we denote links obtained this way by
Ls
2(t) = pr( x−1(s) · y(t)), and Ls
3(u) = pr( x−1(s) · z(u)).
Let us collect useful information below
6
L1
L2
L3
A2
A1
Figure 1: The model of LBorr parametrized by {L1 = pr(x(s)), L2 = pr(y(t)), L3 = pr(z(u))}.
Arc A1 is a part of the unit circle on xy-plane, A2 is a part of circle of radius 1 + ǫ.
(i) The z-axis stays invariant under the S1-action.
(ii) A2 slides, under the S1-action, on the rǫ-torus, A1 simply rotates around the z-axis in
the ( x, y)-plane.
(iii) We can disregard the longitudinal rotation (i.e. pretend that the o bserver sits on the
unit circle) the motion of arcs: Ls
3, As
2 together with the connecting segments is simply
a full rotation around the unit circle on the ( x, y)-plane (which can be thought of as
the “axis of rotation”). Stages of this motion are pictured on the lo wer part of Figure
2.
We seek to visualize the projection of lS,N = lS ∪ lN on the su-face and st-face of the
domain T = S1 × S1 × S1 of FLBor parameterized by ( s, t, u) ∈ T, (it is convenient to think
about T as a cube in ( s, t, u)-coordinates, see Figure 3).
For example when s = 0, ( x(0) = 1), a point (0 , t0, u0) belongs to lN , if and only if
the vector v0 = pr( y(t0)) − pr(z(u0)) “points North”, i.e. in the direction of N = (0 , 0, 1),
analogous condition holds for S = (0, 0, −1), and lS. Thus in order to determine a diagram
of lS,N , we must keep track of the “head” and “tail” of the vector vs = Ls
2(t) − Ls
3(u), for
various values of s and record values of t and u for which vs points “North” and “South”
(Figure 2). We have the following condition
(s, t, u) ∈ lS,N if and only if , vs ‖ S or N. (7)
An alternative way to view this condition is the following: for a given valu e of s the coor-
dinates u and t of points in lS,N can be identiﬁed with points on Ls
2 and Ls
3, which come
from the intersection points in π(Ls
3 ∪ Ls
2), under the projection π(x, y, z) = ( x, y), onto the
(x, y)-plane (see the bottom part of Figure 2). These intersection poin ts are simply crossings
in the diagram of the link {Ls
2, Ls
3} on the ( x, y)-plane. Points N and S can be assumed
7
to be regular values of FLBorr because π(Ls
2(t)) and π(Ls
3(u)) always intersect transversely
(bottom of Figure 2), which is persistent under small perturbation s of the parametrization
of LBorr.
The main task ahead is to visualize lN and lS. For a ﬁxed s = s0 we draw arrows:
N and S (Figure 2) which lie directly above the crossings of the diagram of {Ls0
2 , Ls0
3 } on
the ( x, y)-plane. Next, we trace each component Ls0
2 and Ls0
3 and record values of t and u
parameter for which the condition (7) holds, without loss of genera lity we assume that Ls
2
is parametrized by the unit t-interval, and Ls
3 is parametrized by the unit u-interval. This
process is elucidated below for s = 0 , π
2 , π, 3π
2 , which is suﬃcient to draw projections of lS
and lN (each position is pictured on Figure 1) on st and tu-faces of T. We describe each case
separately,
(s = 0): This is the initial position, where L0
3 is vertical. We mark the initial point L0
3(0) on
the top of L0
3 and orient L0
3 counter-clockwise, the initial point L0
2(0) on L0
2 is chosen
in the middle of the left segment connecting A1 and A2, and the middle point L0
2( 1
2) is
located the middle of the left segment connecting A1 and A2. Points in lS are marked
by × and points in lN , are marked by •. In this conﬁguration there are four vertical
arrows, two pointing North and two South, this gives us four points along the t-interval
ordered as N SSN , ( | − • − × − × − • − |) and four points along the u-interval ordered
(| − (×•) − −(•×) − |), where ( ×•) indicates the “collision” i.e. common value of u
for both lS and lN .
The remaining cases are self-explanatory, see Figure 1,
(s = π
2 ): Ls
3 is horizontal, and t-coordinates of lS,N are colliding ( | − (•×) − (×•) − |). Ls
2 is
vertical and u-coordinates of lS,N are ordered as ( N N SS), ( | − • − × − × − • − | ).
(s = π): Ls
3 is vertical again, and t-coordinates of lS,N are ordered : SN N S, (|−×−•−•−×−| ).
Ls
2 is horizontal and u-coordinates of lS,N are colliding, ( | − (•×) − −(×•) − |).
(s = 3π
2 ): Ls
3 is horizontal, and t-coordinates of lS,N are colliding ( | − (×•) − (•×) − |). Ls
2 is
vertical and u-coordinates of lS,N are ordered as ( N N SS), ( | − × − × − • − • − | ).
Collecting this information, we may draw the projection of the link lS,N on the su-face of T,
which is represented by square (A) in Figure 3. Analogously, the pro jection of lS,N on the
st-face of T, is represented by square (B). The dashed line indicates the lN component of
lS,N and the solid line indicates lS. In order to obtain the diagram of lS,N we will resolve the
double points on Diagram (A) into crossings, ((B) can be resolved an alogously). For example
let us resolve the “circled” double point on (A), which occurs for s = π
2 , of the left two stands
of lS,N . It suﬃces to determine the value of the t-coordinate at this point. Diagram (B) tells
us that lS is below lN because T is oriented so that the t-axis points above the su-face (see
top of Figure 3). Resolving the remaining crossings in a similar fashion le ads to a diagrams
of lS,N presented in squares (C) and (D). Diagram (C) is easier to use for t he calculation of
H (FLBor) = lk( lS, lN ) as an intersection number of e.g. lS with a Seifert surface spanning
8
s = 3π
2
s = π
s = π
2
s = 0
Figure 2: Four positions corresponding to angles: s = 0, π
2 , π, 3π
2 , small arrows next to N and
S indicate a motion as s ր. Several phases of the rotation by s are pictured on the bottom
four drawings. 9
s
s
s
s
π
2
π
2
u (D)(C) t
u(A) t(B)
Figure 3: Projection of lS,N on the su-face and st-face of T. The strands lS and lN are
oppositely oriented since lS,N is null homologous in T.
10
lN . Observe that strands in lS and lN are oppositely oriented, which follows from the fact
that they are null-homologous in H 1(T), there are an obvious annuli bounding lS and lN on
Diagram (C). Clearly, the linking number of lS and lN is equal to ±2, since the intersection
number of e.g. lS with the obvious annulus on Diagram (C) is ±2. This proves (6).
}n
Figure 4: left: ¯ µ123 = ±1 and right: ¯µ123 = ±n.
Corollary 2.3. If L = {L1, L2, L3} is a 3-component link with vanishing pairwise linking
numbers then
H (FL) = ±2 ¯µ123
Proof. Clearly, if L and L′ are link-homotopic then FL and FL′ are homotopic maps. By the
Milnor classiﬁcation of 3-component links up to link homotopy (see [23 ]), every 3-component
link L with zero pairwise linking numbers and ¯µ123 = ±n is represented by the right diagram
on Figure 4. Consequently, up to homotopy, the associated map FL can be obtained from
FLBorr by covering one of the S1 factors in T, n-times.
Lemma 2.4 ([11]). We have the following isomorphisms
π2(Conf(R3, 3)) ∼= Z ⊕ Z ⊕ Z, π 2(Conf(S3, 3)) ∼= Z,
and the induced homomorphism i∗ : π2(Conf(R3, 3)) ↦→π2(Conf(S3, 3)), from i : R3 ↦→
R3 ∪ {∞} ∼= S2, maps the generators Aij, 1 ≤ i ≤ j ≤ 3, to ± α, where α is the single
generator of π2(Conf(S3, 3)).
Proof. The Hurewicz Theorem tells us that H2(Conf(R3, 3)) ∼= π2(Conf(R3, 3)). The 2-
skeleton of Conf( R3, 3) has a homotopy type of S2 ∨ S2 ∨ S2 and H2(Conf(R3, 3)) is generated
by Aij : S2 ↦→Conf(R3, 3), 1 ≤ i < j ≤ 3 representing each 2-sphere in the 2-skeleton (c.f.
[12]). The group of permutations S3 acts on Conf( R3, 3) by permuting coordinates. As a
consequence of this we obtain the action on generators of H2(Conf(R3, 3)) by permutation.
We have seen that Conf( S3, 3) has the homotopy type of S3 × S2 thus π2(Conf(S3, 3)) = Z,
and let us denote the generator by α. Now, i∗Aij = k α, k ∈ Z, notice that i∗A23 = α since
i ◦ A23 = id S2, using the action by permutations we obtain i∗Aij = α.
11
Corollary 2.5. Denote by F kl
L = FL
⏐
⏐
S1
k×S1
l
restriction of FL deﬁned in (4) to the kl-torus
k, l ∈ {s, t, u}, k ⁄= l. Then
deg(F kl
L ) = lk(Lk, Ll), (8)
where lk (Lk, Ll) is the linking number between the components parameterized by k, and l.
Proof. By deﬁnition
deg(S1
i × S1
j
Lij
− →Conf(R3, 3)
πij
− →Conf(R3, 2) ∼= S2) = lk( Li, Lj),
thus on the cohomology level lk( Li, Lj) = L∗
ij[Aij] = ( F ij
L )∗(α).
Results of Theorem 2.2 and Proposition 2.1 combined with Formula (2) a llow us to express
¯µ123(L) of a borromean link L as
¯µ123(L) =
∫
T
F ∗
Lν ∧ α =
∫
T
L∗ω ∧ α, (9)
for F ∗
Lν = dα, ω = H ∗ν ∈ Ω 2(Conf(S3, 3)),
where ν is the area form on S2, and H : Conf( S3, 3) − →S2 is the deformation retraction
(as e.g. in (5)). Alternatively, we may view ω as a 2-form on ( S3)3 which is singular along
the diagonals ∆ ⊂ (S3)3, and the singularity is of order O(r2), where r is a distance to ∆ .
Consequently, ω is integrable but not square integrable on ( S3)3. We also point out that the
2-form ω can be replaced with any other cohomologus 2-form in Conf( S3, 3).
Remark 2.6. Notice that the integral formula (9) is antisymmetric in the following s ense
¯µ123(L1, L2, L3) =
∫
S1s
∫
S1
t
∫
S1u
ω ∧ α(˙x(s), ˙y(t), ˙z(u)) ds ∧ dt ∧ du
=
∫
S1s
∫
S1
t
∫
S1u
−ω ∧ (−α)(˙y(t), ˙x(s), ˙z(u)) ds ∧ dt ∧ du
=
∫
S1
t
∫
S1s
∫
S1u
ω ∧ α(˙y(t), ˙x(s), ˙z(u))(− dt ∧ ds ∧ du) = −¯µ123(L2, L1, L3)
where in the second identity the potential changes sign because th e domain changes orien-
tation.
3 Invariants of volume preserving ﬂows. Helicity.
Given ﬁnitely many volume preserving vector ﬁelds X1, X2, . . . Xk ∈ Vectvol(M) on M = S3
or a homology 3-sphere one seeks quantities I(X1, X2, . . . , Xk) invariant under the action of
volumorphisms isotopic to the identity g ∈ Diﬀ vol
0 (M), commonly known as higher-helicities:
I(X1, X2, . . . , Xk) = I(g∗X1, g∗X2, . . . , g∗Xk), for all g ∈ Diﬀ vol
0 (M), (10)
12
where g∗ is a push-forward by a diﬀeomorphism g. To distinguish the case of a single vector
ﬁeld X (i.e. X = X1 = . . . = Xk) we often refer to I(X) = I(X1, X2, . . . , Xk) as self-helicity.
We elucidated in the introduction a fundamental example of such inva riant is the ordinary
helicity H(X1, X2) of a pair of vector ﬁelds. In the the remaining part of this section w e
review well known formulations of the helicity, which will later help us to point out analogies
to the proposed formulation of the 3rd order helicity. Let T = T1 ∪T 2 represent two invariant
subdomains (not necessarily disjoint) under ﬂows of X1 and X2 in S3 and let
T = T1 × T2 ⊂ Conf(M, 2) ⊂ M × M.
Recall that the formula for H(X1, X2), from [17, 30], specialized to invariant subdomains
T = T1 ∪ T2 may be expressed as
H12(X1, X2) =
∫
T1×T2
ω ∧ ιX1µ ∧ ιX2µ, (11)
where ω is so called linking form on M × M. When T = M × M this formula is equivalent
to a more commonly known expression: H(X1, X2) =
∫
M ιX1µ ∧ d−1(ιX2µ) (because ω also
represents the integral kernel of d−1).
Philosophically, H(X1, X2) can be derived (c.f. [2]) from the linking number of a pair of
closed curves, which is expressed by Arnold’s Helicity Theorem. For o rbits {O 1(x), O 2(y)}
of X1 and X2 through x, y ∈ M, we introduce the following notation for the long pieces of
closed up orbits
O i
T (x) = {Φ i
t(x) | 0 ≤ t ≤ T } ⊂ O i(x), i = X, Y, (12)
¯O i
T (x) := O i
T (x) ∪ σ(x, Φ i(x, T )). (13)
where σ(x, y) denotes a short path, [30], connecting x and y in M (see Section 5).
Theorem 3.1 (Arnold’s Helicity Theorem, [2]) . Given X1, X2 ∈ Vectvol(M), The following
limit exists almost everywhere on M × M:
¯mX1X2(x, y) = lim
T →∞
1
T 2 lk( ¯O 1
T (x) × ¯O 2
T (y)) . (14)
Moreover, ¯mX1X2 is in L1(M × M), and
H12(X1, X2) =
∫
M ×M
¯mX1X2(x, y) µ(x) ∧ µ(y) . (15)
The function ¯mX1X2 represents an asymptotic linking number of orbits {O 1(x), O 2(y)}, and
the identity (15) tells us that the helicity H12(X1, X2) is equal to the average asymptotic
linking number. We will demonstrate, in coming paragraphs, how this p hilosophy is applied
to obtain the asymptotic ¯µ123-invariant for 3-component links and the third order helicity.
13
4 Deﬁnition of “ ¯µ123-helicity” on invariant unlinked han-
dlebodies.
In this section we apply the formulation of the ¯ µ123-invariant for the 3-component links in
S3, obtained in Section 2, to deﬁne the third order helicity of a volume pr eserving vector ﬁeld
X on certain invariant domains T in S3. As a “warm-up” to a more general case presented
in Section 5, in the following paragraphs we consider the case of thre e disjoint unlinked
handlebodies: T = T1 ∪ T2 ∪ T3 each of genus g(Ti) in S3. When T represents three unlinked
tubes (so called ﬂux tubes , [3]) in R3, the third order helicity has been developed by several
authors [5, 22, 20] via the Massey product formula for the ¯ µ123-invariant, we compare our
approach to these known works in Section 7.
We consider Ti to have smooth boundary and the vector ﬁeld X to be tangent to ∂Ti, set
Xi := X
⏐
⏐
Ti
, i = 1, 2, 3,
denote the ﬂow of X on S3 by Φ, and ﬂows of restrictions Xi by Φ i. Clearly, T is an invariant
set of X. Given for any domain T with three connected components {Ti} we may always
associate a product domain in Conf( S3, 3) as follows
T := T1 × T2 × T3 ⊂ Conf(S3, 3) ⊂ S3 × S3 × S3 . (16)
Notice that T is a domain with corners in Conf( S3, 3), and we use the same notation for the
product of Ti as for the union in S3. Wherever needed we also assume that ( S3)3 is equipped
with a product Riemannian metric. A domain T deﬁned in (16), where Ti ∩ Tj = Ø, i ⁄= j
and each Ti is a handlebody in S3 is called unlinked handlebody if and only if the 2-form
ω ∈ Ω 2(Conf(S3, 3)) deﬁned in Equation (9) is exact on T , i.e. ω has a local potential
αω ∈ Ω 1(T ):
ω = dαω . (17)
Denote a volume preserving vector ﬁeld and an unlinked handlebody T as ( X; T ).
Remark 4.1. Notice that since ω is a dual cohomology class to the S2 factor of Conf(S3, 3) ∼
=
S3 × S2, thus ω does not admit a global potential.
Because each handlebody Ti has a homotopy type of a bouquet of circles H1(Ti) is generated
by cycles {Lk
i }k=1,...,g(∂Ti) corresponding to the circles, which we call basic cycles . We have
the following practical characterization of unlinked handlebodies:
Lemma 4.2. T is an unlinked handlebody if and only if
lk(Lk
i , Lr
j) = 0 , ∀ i, j, i ⁄= j (18)
Proof. The standard pairing, [6], H 2(T ) × H2(T ) − →R implies that a closed k-form is exact
if and only if it evaluates to zero on all k-cycles of the domain. By the K¨ unneth formula
H2(T ) = H2(T1 × T2 × T3) is generated by Lk
i ⊗ Lr
j. Corollary 2.5 implies (for i ⁄= j) that
lk(Lk
i , Lr
j) =
∫
Lk
i ×Lr
j
ω .
14
Therefore the condition (18) is necessary and suﬃcient for ω to be exact on T .
Figure 5: The simplest unlinked handlebody: ﬂux tubes T Borr modeled on the borromean
rings.
Let X be a volume preserving vector ﬁeld on S3 which admits an unlinked domain T which
is invariant under its ﬂow. We deﬁne the ¯ µ123-helicity of ( X; T ) denoted by H123(X; T ) or
H123(X1, X2, X3) as follows:
H123(X; T ) = H123(X1, X2, X3)
def.
=
∫
T
(
αω ∧ dαω
)
∧ ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3, (19)
where µi denotes the pull-back of the volume form µ on S3 under the projection
πi : S3 × S3 × S3 − →S3, π i(x1, x2, x3) = xi, (20)
and ιXi is a contraction by a vector ﬁeld Xi, our notational convention is to denote by ιXiµi
both the forms on the base of πi and the pullbacks: π∗
i
(
ιXiµi
)
. Notice that µ = µ1 ∧ µ2 ∧ µ3
is a natural volume form on the product: S3 × S3 × S3.
There are obvious analogies between the formula above, the formu la for the helicity
H12(X; T ) and the integral formula for the ¯ µ123-invariant (9). Clearly, the 3-form
γω := αω ∧ dαω = αω ∧ ω,
plays a role of the linking form as ω in the formula (11) for H12(X; T ). The main motivation
behind this deﬁnition is the ergodic interpretation of H123(X; T ) as an average asymptotic
15
¯µ123-invariant of orbits of X, and will become apparent in Section 5. Formula (19) can be
also regarded as the third order helicity of three distinct vector ﬁe lds Xi, supported on the
handlebodies Ti. In Section 6 we indicate how to construct the potential αω from the basic
elliptic theory of diﬀerential forms.
Theorem 4.3 (Helicity Invariance Theorem). On every unlinked invariant handlebody T in
S3, H123(X; T ) is
(i) independent of a choice of the potential αω.
(ii) invariant under the action of Diﬀ vol
0 (S3), i.e. for every g ∈ Diﬀ vol
0 (S3):
H123(X; T ) = H123(g∗X; g(T )) . (21)
Proof. To prove ( i) observe for every other potential α′
ω of ω, the diﬀerence β = αω − α′
ω is
a closed 1-form on T (since ω = dαω = dα′
ω). Therefore
H123(X; T ) − H′
123(X; T ) =
∫
T
(β ∧ ω) ∧ ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3
(1)
=
∫
T
d
(
β ∧ αω ∧ ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3
)
=
∫
∂T
β ∧ αω ∧ ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3
(2)
= 0 ,
where in (1) we applied d(ιXiµi) = 0 (since Xi’s are divergence free), and in (2):
ιXiµi
⏐
⏐
∂Ti
= 0,
(because each vector ﬁeld Xi is tangent to the boundary ∂Ti), and
∂T =
(
∂T1 × T2 × T3
)
∪
(
T1 × ∂T2 × T3
)
∪
(
T1 × T2 × ∂T3
)
.
Next we show ( ii), the proof is in the style of [5, 22], but adapted to our setting. For any
given g ∈ Diﬀ vol(S3), there exists a path t − →g(t) ∈ Diﬀ vol
0 (S3), such that
g(0) = id S3, g (1) = g .
Denote by V the divergence free vector ﬁeld on S3, given by V (x) = d
dt g(t, x)|t=0, i.e. g(t) is
a ﬂow of V , and push-forward ﬁelds Xi by
X t
i := g(t)∗Xi .
It is well known (see Appendix B, or [15, p. 224]) that 2-forms: ιX t
i
µ are frozen in the ﬂow
of V , i.e.
d
dt
(
g(t)∗ιX t
i
µ
)
= (∂t + LV )ιX t
i
µ = 0. (22)
16
We also have a path ˆ g(t) = ( g(t), g(t), g(t)) in Diﬀ vol
0 (S3 × S3 × S3). Analogously for the
volume preserving ﬂow ˆg(t) we obtain the vector ﬁeld ˆV = ( V, V, V ) (recall that a tangent
bundle T (S3)3 has a natural product structure). Equation (22) implies
(∂t + L ˆV )
(
π∗
i ιX t
i
µ
)
= (∂t + L ˆV )ιX t
i
µi = 0 . (23)
(in the second equation we merely revoke our notational conventio ns: ιX t
i
µi ≡ π∗
i
(
ιg(t)∗Xiµ
)
).
Let T (t) = ˆg(t)(T (0)) ⊂ Conf(S3, 3) we must show d
dt H123(X t
1, Xt
2, Xt
3) = 0 at every t = t0.
Notice that for small enough ǫ and t ∈ (t0 − ǫ, t0 + ǫ) we can assume, by ( i), that αω is a
time independent potential obtained from slightly bigger domain ~T which satisﬁes
T (t) ⊂ ~T , ∀t ∈ (t0 − ǫ, t0 + ǫ),
and is a deformation retraction of T (t0). Without loss of generality we assume t0 = 0,
ˆg(0) = id (S3)3, and calculate at t0:
d
dt
(
H123(g(t)∗X1, g(t)∗X2, g(t)∗X3)
)
= d
dt
∫
T (t)
αω ∧ dαω ∧ ιX t
1
µ1 ∧ ιX t
2
µ2 ∧ ιX t
3
µ3
=
∫
T (0)
d
dt ˆg(t)∗(
αω ∧ dαω ∧ ιX t
1
µ1 ∧ ιX t
2
µ2 ∧ ιX t
3
µ3
)
=
∫
T (0)
(
L∂t+ ˆV (αω ∧ dαω)
)
∧ ιX t
1
µ1 ∧ ιX t
2
µ2 ∧ ιX t
3
µ3,
where in the last identity we applied (23) and the product rule for the Lie derivative. Now
because ω ∧ αω is time independent (for t ∈ (t0 − ǫ, t0 + ǫ)) by the Cartan magic formula we
obtain
L∂t+ ˆV (αω ∧ dαω) = L ˆV (αω ∧ dαω) = ι ˆV d(αω ∧ dαω) + d(ι ˆV (αω ∧ dαω))
= d(ι ˆV (αω ∧ dαω)),
since d(αω ∧ dαω) = ω ∧ ω = 0. Now, the same argument as in the proof of ( i) shows that
the right hand side of the previous equation is zero, because X t
i are tangent to the boundary
of Ti(t).
Remark 4.4. Notice that the above argument shows that if we replace αω ∧dαω by virtually
any closed 3-form η on Conf( S3, 3) (or ( S3)3) we obtain some invariant under frozen-in-
ﬁeld deformations. Clearly, if η is exact we obtain trivial invariants, therefore the only
candidates are cohomology classes of Conf( S3, 3) ∼= S3 × S2. In dimension 3, the only
candidate cohomology class of Conf( S3, 3) is a dual of S3. Based on the considerations in
Section 2 one may argue that an invariant obtained this way is trivial. I ndeed the cohomology
class η evaluated on any 3-torus obtained from a 3-component link in S3 via the map L in
(4) is zero. Therefore one could apply the approach via the Ergodic Theorem (as in Section
5) to show that
∫
η ∧ ιX µ1 ∧ ιXµ2 ∧ ιX µ3 deﬁnes a trivial invariant. The crucial obstacle in
extending the formula in (19) to encompass the whole S3 is the fact that the potential αω
cannot be globally deﬁned on Conf( S3, 3).
17
5 The ergodic interpretation of H123(X; T )
The following statement is often seen in literature [8, 9]:
Helicity measures the extend to which vector ﬁelds twist and coil around each
other.
A beauty of Arnold’s ergodic approach to the helicity H12(X) is that it makes this statement
precise, by interpreting H12(X) as an average asymptotic linking number of orbits of X. But
it also has a practical application as it allows us to extend our approac h to certain invariant
sets of X. In this section we apply this philosophy to our newly deﬁned invariant H123(X; T ),
and interpret it as the average asymptotic ¯µ123-invariant of orbits of X. Moreover this ergodic
interpretation leads us to an alternative, more intuitive proof of He licity Invariance Theorem
4.3.
We begin by observing that given a volume preserving vector ﬁeld X on M and its ﬂow
Φ t, we may regard X as three vector ﬁelds on ( M)3. Therefore (Φ , Φ , Φ) induces a natural
R3 action deﬁned as
Φ : R3 × (M)3 − →(M)3 :
(
(s, t, u), x, y, z
) Φ
− →(Φ( s, x), Φ( t, y), Φ( u, z)). (24)
Observe that Φ is a volume preserving action on ( M)3. Our analysis is rooted in techniques
developed in [2, 19, 20], the main tool is the the following
Theorem 5.1 (Multi-parameter Ergodic Theorem, [4]) . For any real valued L1-function F
on (M)3, the time averages under the action in (24):
¯F (x, y, z) = lim
T →∞
1
T 3
∫ T
0
∫ T
0
∫ T
0
F (Φ( x, s), Φ( y, t), Φ( z, u)) ds dt du
converge almost everywhere. Moreover, the limit function ¯F satisﬁes
(i) ‖ ¯F ‖L1((M )3) ≤ ‖F ‖L1((M )3),
(ii) ¯F is invariant under the Φ -action,
(iii) if (M)3 is of ﬁnite volume then
∫
(M )3
¯F =
∫
(M )3
F . (25)
We may now deﬁne invariant unlinked domain T of X as an arbitrary Φ -invariant set, with
topological closure T which belongs to a larger product of open sets ~T = ~T1 × ~T2 × ~T3 in
Conf(S3, 3), satisfying the following
(A) ~T admits a short path system S,
18
(B) Equation (17) holds on ~T .
By a system of short paths on ~T , [30, 3], we understand a collection of curves S = {σ(x, y)}
on each open set ~Ti such that
(a) for every pair of points x, y ∈ ~Ti there is a curve σ(x, y) : I ↦→~Ti in S, such that
σ(0) = x and σ(1) = y,
(b) the lengths of paths in S are uniformly bounded above by a common constant.
Topologically, every Φ -invariant set is a union of products of orbits of X in ( S3)3, it is
often convenient to think of the orbits Φ -action as a foliation of ( S3)3, then Φ -invariant sets
are just union of leaves of such foliation. A fundamental example of an invariant unlinked
domain is the case of Φ -invariant set T contained in the product ~T = ~T1 ×~T2 ×~T3 of disjoint
open unlinked handlebodies ~Ti. Notice that we do not require X to be tangent to ∂~Ti in this
case, and ~T always admits a short path system as we describe in the following
Remark 5.2. In [30], Vogel shows that on a closed manifold M, geodesics always provide
a short path system. When T is contained in the product of unlinked handlebodies ~T we
may easily construct such system on ~T . Because Ti are proper subsets of S3 we generally do
not want to use ambient geodesics from S3 as they may not lie entirely in Ti. To obtain S
one may always put an artiﬁcial Riemannian metric on each ~Ti which makes it a complete
Riemannian manifold (e.g. by making ∂~Ti totally geodesic) and choose S to be geodesics
on such Riemannian manifold. We also observe that one may apply a diﬀe omorphism g ∈
Diﬀ(~T ) to S which results in the new system gS on g(~T ).
Next theorem shows that the deﬁnition of H123(X; T ) in Equation (11) is valid for invariant
unlinked domains of X and is an analog of Arnold’s Helicity Theorem in our setting
Theorem 5.3 (Ergodic interpretation of H123(X; T )). Given (X; T ), the following limit
(asymptotic ¯µ123-invariant of orbits) exists for almost all (x, y, z) ∈ T :
¯mX (x, y, z) = lim
T →∞
1
T 3 ¯µ123
(¯O X1
T (x), ¯O X2
T (y), ¯O X3
T (y)
)
. (26)
Moreover,
H123(X; T ) =
∫
T
¯mX(x, y, z) µ(x) ∧ µ(y) ∧ µ(z) . (27)
Proof. The proof is similar to the one in e.g. [30]. Before we start we must poin t out the
following identity (valid for any 3-form γ on M × M × M and vector ﬁelds X1, X2, X3 on M)
(ιX1ιX2ιX3γ) ∧ µ ∧ µ ∧ µ = γ(X1, X2, X3) µ ∧ µ ∧ µ = γ ∧ ιX1µ ∧ ιX2µ ∧ ιX3µ .
The ﬁrst equation follows from the deﬁnition, the second equation is a consequence of the
fact that ιX is an antiderivation i.e.
ιX (α ∧ β) = ( ιX α) ∧ β + (−1)|α|α ∧ (ιX β), (28)
19
and ιXiµj ≡ 0 for i ⁄= j. As a result
H123(X1, X2, X3) =
∫
T
(
αω ∧ dαω
)
∧ ιX1µ1 ∧ ιX2µ2 ∧ ιX3µ3
=
∫
T
(
ιX1ιX2ιX3
(
αω ∧ dαω
))
µ1 ∧ µ2 ∧ µ3
=
∫
T
mX1,X2,X3(x, y, z) µ1 ∧ µ2 ∧ µ3,
where mX1,X2,X3 := αω ∧ dαω(X1, X2, X3). For convenience let (see (12))
¯O(x, y, z; T ) := ¯O X1
T (x) × ¯O X2
T (y) × ¯O X3
T (y) .
Clearly, every link ¯O(x, y, z; T ) is borromean and by Formula (9) we obtain
¯µ123
(¯O X1
T (x), ¯O X2
T (y), ¯O X3
T (y)
)
=
∫
¯O(x,y,z;T )
αω ∧ dαω
=
∫
O(x,y,z;T )
αω ∧ dαω + (I)
where the term ( I) involves integrals over short paths in S, (see Appendix B). Next, notice
that for every ( x, y, z) : DΦ (x,y,z)[∂i] = Xi, i = s, t, u we obtain
Φ ∗
(x,y,z)(αω ∧ dαω) = ( αω ∧ dαω(X1, X2, X3)(Φ 1(x, s), Φ 2(y, t), Φ 3(z, u)) ds ∧ dt ∧ du
= mX1,X2,X3(Φ 1(x, s), Φ 2(y, t), Φ 3(z, u)) ds ∧ dt ∧ du .
Thus
∫
O(x,y,z;T )
αω ∧ dαω =
∫ T
0
∫ T
0
∫ T
0
mX1,X2,X3(Φ 1(x, s), Φ 2(y, t), Φ 3(z, u)) ds ∧ dt ∧ du .
Function mX1,X2,X3 is smooth on T and therefore L1. Because short paths do not contribute
to the time average i.e.
lim
T →∞
1
T 3 (I) = 0
(see Appendix B), Theorem 5.1 applied to the function mX1,X2,X3 yields almost everywhere
existence of the limit (26) and the invariant L1-function ¯mX := ¯mX1,X2,X3 on T . The identity
(27) follows from ( iii) of Theorem 5.1.
Theorem 5.4 (Helicity Invariance Theorem-ergodic version) . On every unlinked domain T
in S3, (i) and (ii) of Theorem 4.3 hold for H123(X; T ).
Proof. The proof of ( i) immediately follows from independence of the limit (26) on the choice
of the potential αω. For the proof of ( ii) we must show the following
∫
T
mX1,X2,X3 µ1 ∧ µ2 ∧ µ3 =
∫
g(T )
mg∗X1,g∗X2,g∗X3 µ1 ∧ µ2 ∧ µ3 .
20
Theorem 5.1, tells us that mX1,X2,X3 and mg∗X1,g∗X2,g∗X3 admit L1-averages ¯mX1,X2,X3 and
¯mg∗X1,g∗X2,g∗X3, under actions of Xi and g∗Xi respectively. If the following holds:
¯mX1,X2,X3(x, y, z) = ¯mg∗X1,g∗X2,g∗X3(g(x), g(y), g(z)), a.e., (29)
then (21) is an immediate consequence of (25), change of variables for integrals, and the fact
that g preserves the volume, i.e. µi = g∗µi. Borrowing notation from the previous theorem
we set
g ¯O(x, y, z; T ) := g( ¯O X1
T (x)) × g( ¯O X2
T (y)) × g( ¯O X3
T (z))
= ¯O g∗X1
T (g(x)) × ¯O g∗X2
T (g(y)) × ¯O g∗X3
T (g(z)),
where the second identity is a consequence of the fact that the ﬂo w of g∗Xi is obtained as
a composition of g and the ﬂow of Xi. Since g is isotopic to the identity, ¯O(x, y, z; T ) and
¯O(x, y, z; T ) are isotopic borromean links in S3, and for every T :
¯µ123( ¯O(x, y, z; T )) = ¯µ123(g ¯O(x, y, z; T )).
As a result of the above identity and (26) we derive a.e.
¯mX1,X2,X3(x, y, z) = lim
T →∞
1
T 3 ¯µ123( ¯O(x, y, z; T ))
= lim
T →∞
1
T 3 ¯µ123(g ¯O(x, y, z; T )) = ¯mg∗X1,g∗X2,g∗X3(g(x), g(y), g(z)).
Notice that in the last equation we used in the “pushed forward” sho rt paths system: gS.
But since lengths of paths in gS are bounded as well, they do not contribute to the limit.
This proves the identity (29), and consequently (21).
Notice that the above argument does not require the Stokes Theo rem, and thus may lead
to further generalizations. Clearly, for H123(X; T ) to be nontrivial T must be of nonzero
measure.
The following formula is a well known property of the ordinary helicity H12(X; T ) of the
ﬂux tubes T modeled on a 2-component link L = {L1, L2} (see e.g. [19, 7])
H12(X; T ) = H12(X1, X2) = lk( L1, L2) Flux(X1) Flux(X2). (30)
Next we show that an analogous property holds H123(X; T ), for invariant unlinked handle-
bodies T investigated in the previous section.
Proposition 5.5. H123(X1, X2, X3) on invariant unlinked handlebodies T satisﬁes the fol-
lowing formula
H123(X1, X2, X3) =
∑
i⁄=j⁄=k
¯µ123(Li
1, Lj
2, Lk
3) FluxΣ i(X1) FluxΣ j (X2) FluxΣ k(X3) . (31)
where {Li
1 ⊗ Lj
2 ⊗ Lk
3} is a basis of basic cycles of H1(T1) ⊗ H1(T2) ⊗ H1(T3), Flux (Xi) stands
for the ﬂux of Xi through a cross sectional surface Σ k of Ti, which represents a homology
Poincar´ edual of Lk
i in H2(Ti, ∂Ti).
21
Proof. Recall that a ﬂux Flux Σ k(Xi) of a vector ﬁeld Xi though a cross-sectional surface Σ k
is given by:
FluxΣ k(Xi) =
∫
Σ k
ιXiµ =
∫
Ti
hk ∧ ιXiµ
=
∫
Ti
ιXihk ∧ µ =
∫
Ti
hk(Xi),
where 1-forms hk represent cohomology Poincar´ e duals of Σ k and we applied (28) in the
third equation. Clearly, hi ∈ Ω 1(Ti) satisfy
∫
γ
hk = #(γ, Σ k) = deg( γ, Lk),
where deg( γ, Lj
k) measures how many times γ “wraps around” in the cycle Lj
k.
For simplicity we ﬁrst assume that T is modeled on a borromean link L = {L1, L2, L3}
(see Figure 5). Then h = h1 ∧ h2 ∧ h3 ∈ Ω 3(T ) is a cohomology class dual of the cycle
L = L1 × L2 × L3 in T . We set
H := ιX1ιX2ιX3h = h(X1, X2, X3),
which is a smooth function, and let ¯H be the time average of H as in Theorem 5.1. It suﬃces
to show
¯mX1,X2,X3 = ¯µ123(L) ¯H, a.e. (32)
Analogously as in Theorem 4.3, Equation (32) immediately implies Formula (31). Assume
the notation of Theorem 4.3, for given T consider ¯O(x, y, z; T ). By the fundamental property
of the ¯µ123-invariant (see Corollary 2.3) we have
¯µ123( ¯O(x, y, z; T )) = ¯ µ123(L)
(
deg( ¯O X1
T (x), L1) deg( ¯O X2
T (y), L2) deg( ¯O X3
T (x), L3)
)
= ¯ µ123(L)
∫
¯O(x,y,z;T )
h .
Thus we obtain
¯mX1,X2,X3(x, y, z) = lim
T →∞
1
T 3 ¯µ123( ¯O(x, y, z; T ))
= ¯ µ123(L) lim
T →∞
1
T 3
∫
¯O(x,y,z;T )
H
= ¯ µ123(L) ¯H(x, y, z),
where the last equality is again the consequence of short paths not contributing to the limit.
Now, from the product structure and ( iii) of Theorem 5.1 we have
∫
T
¯H =
∫
T
H =
(∫
T1
h1(X1)
)(∫
T2
h2(X2)
)(∫
T3
h3(X3)
)
.
The proof in the case of a general handlebody is analogous, once we show the following
22
Lemma 5.6. Let O = {O1, O2, O3} be a 3-component link in S3 such that Oi ⊂ T i for each
i. Then O is borromean and
¯µ123(O) =
∑
i⁄=j⁄=k
¯µ123(Li
1, Lj
2, Lk
3) deg(O1, Li
1) deg(O2, Lj
2) deg(O3, Lk
1) . (33)
Proof. Notice that thanks to our new interpretation, the ¯ µ123-invariant is not only a link
homotopy invariant but a homotopy invariant of the associated map FO deﬁned in (4).
Observe that each component Oi can be homotopied inside of its handlebody Ti to be come
a bouquet of circles ˆOi ∼= S1 ∨ S1 ∨ . . . ∨ S1. Such that each factor in ˆOi is a basic cycle in
H1(Ti). As a result we obtain the associated map F bO, and
¯µ123(O) = 1
2 H (F bO).
Interpreting, H (F bO) as the intersection number and summing up intersection numbers w e
conclude (33).
In the case of borromean ﬂux tubes modeled on L, (30) reduces to
H123(X1, X2, X3) = ¯µ123(L) FluxΣ 1(X1)FluxΣ 2(X2)FluxΣ 3(X3), (34)
where Σ i denotes homology Poincar´ e duals to Li in H2(Ti, ∂Ti).
Since the ﬂuxes are invariant under frozen-in-ﬁeld deformations F ormula (30) is yet an-
other proof of Theorem 4.3 in the setting of invariant unlinked handle bodies. In [20] the
authors develop the same formula for the borromean ﬂux tubes. T his clearly must be the
case as we deal with the same topological invariants of links via a diﬀer ent approach. Ad-
ditional advantage of our formulation is that we do not have to sepa rately deal with null
points of vector ﬁelds as in [20]. We also note that in [20] the authors prove the helicity
invariance only via Formula (34).
