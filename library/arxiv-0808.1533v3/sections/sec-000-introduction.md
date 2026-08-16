---
doc_id: arxiv-0808.1533v3
doc_title: "The third order helicity of magnetic ﬁelds via link maps. R. Komendarczyk ∗†"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-21
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
doc_brief: "The third order helicity of magnetic fields via link maps. R. Komendarczyk ∗† — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us"
---
A purpose of this paper is to develop a particular formula for the thir d order helicity on
certain invariant sets of a volume preserving vector ﬁeld B. The third order helicity, [3], is
an invariant of B under the action of volumorphisms isotopic to the identity (denoted here
by SDiﬀ 0(M)). Importance of such invariants stems from the basic fact that the evolution
of the vorticity in the ideal hydrodynamics or of the magnetic ﬁeld B0 in the ideal magne-
tohydrodynamics (MHD), occurs along a path t − →g(t) ∈ SDiﬀ 0(M), [3, p. 176]. Namely,
B(t) = g∗(t)B0 which is a direct consequence of Euler’s equations:
d
dt B + [v, B] = 0 , d
dt g(t) = v. (1.1)
One often says that the magnetic ﬁeld B is frozen in the velocity ﬁeld v of plasma, and the
action by SDiﬀ 0(M) is frequently referred to as frozen-in-ﬁeld deformations. A fundamental
example of such invariant deﬁned for a general class in SVect( M) is the helicity H12(B1, B2)
deﬁned for a pair of vector ﬁelds B1 and B2 on M = S3 or a homology sphere. Helicity has
∗ 2000 Mathematics Subject Classiﬁcation . Primary: 76W05,57M25, Secondary: 58F18,58A10
†This project is supported by DARPA, #F A9550-08-1-0386.
1
been ﬁrst introduced by Woltjer, [39], in the context of magnetic ﬁe lds, and is a measure
of how orbits of B1, and B2 link with each other. This topological interpretation of helicity
has been made precise by Arnold, who introduced the concept of th e average asymptotic
linking number of a volume preserving vector ﬁeld B on M, [2]. The subject has been further
investigated in [1, 5, 25, 36] (see [3] for additional references), where authors approach higher
helicities via the Massey products under various assumptions about the vec tor ﬁelds or their
domains (work in [16, 35, 37] concerns yet other approaches to th e problem). Extensions of
the helicity concept to higher dimensional foliations can be found in [18 , 33, 23] and recently
in [10].
In this paper we present an alternative to these approaches, whic h is a natural extension
of the notion of the linking number as a degree of a map, and exploits r elations to the
homotopy theory of certain maps associated to the link. The paper has two parts.
In the ﬁrst part we show how the Milnor ¯ µ123-invariant: ¯µ123(L) of a parametrized Bor-
romean link L in S3 can be obtained as a Hopf degree of an associated map to the conﬁg u-
ration space of three points in S3. The presented approach to link homotopy invariants of
3-component links has been proposed in [20] for n-component links in R3, and conveniently
simpliﬁed for 3-component links in S3 in the joint work [12], where the full correspondence
between ¯µ123(L) and the Pontryagin-Hopf degree is proved. In Section 2 we prese nt the orig-
inal proof of this correspondence in the Borromean case, which is s uﬃcient for our purposes.
The second part of the paper is discusses a new deﬁnition of the thir d order helicity
denoted here by H123(B; T ), where B is a volume preserving vector ﬁeld having an invariant
unlinked domain T ⊂ S3. The simplest of such domains are three invariant handlebodies
in S3 which have pairwise unlinked cycles in the ﬁrst homology. This includes t he case of
Borromean ﬂux tubes already investigated in [5, 25]. In Section 5 we d evelop an ergodic
formulation of H123(B; T ) as an average asymptotic ¯ µ123-invariant, in the spirit of Arnold’s
average asymptotic linking number, which allows us to extend the deﬁ nition of the invariant
to topologically more complicated unlinked domains. We also derive, in Se ction 7, a lower
bound for the L2-energy of B in terms of H123(B; T ).
Acknowledgements: The inspiration for the presented approach to the link homotopy in-
variants comes from the paper of Toshitake Kohno [20], and I am gra teful to him for the
valuable e-mail correspondence. I have enjoyed conversations w ith many colleagues at the
University of Pennsylvania, who have inﬂuenced this work. I wish to t hank Herman Gluck
for weekly meetings and his interest in this project, Frederic Cohen , Dennis DeTurck, Charlie
Epstein, Paul Melvin, Tristan Rivi` ere, Clay Shonkwiler, Jim Stasheﬀ , David Shea Vick for
the valuable input. I am also grateful to my advisor Robert Ghrist wh o introduced me to
the subject long time ago. After posting recent joint results in [12] we were informed by
Paul Kirk about related works of Urlich Koschorke in [21, 22], on homo topy invariants of
link maps and Milnor ¯µ-invariants. The author acknowledges ﬁnancial support of DARPA ,
#F A9550-08-1-0386.
2
2 The Milnor ¯µ123-invariant and the Hopf degree.
The ¯µ-invariants of n-component links in S3 have been introduced by Milnor in [28, 29] as
invariants of links up to link homotopy . Recall that the link homotopy is a deformation of
a link in S3 which allows each component to pass through itself but not through a diﬀerent
component. Clearly, this is a weaker equivalence than the equivalenc e of links up to isotopy
where components are not allowed to pass through themselves at a ll. The fundamental
example of a ¯µ-invariant is the linking number (denoted by ¯µ12) which is a complete invariant
of the 2-component links up to link homotopy. In the realm of 3-comp onent links the relevant
invariants are the pairwise linking numbers ¯ µ12, ¯µ23, ¯µ32, and the third invariant ¯ µ123 in
Zgcd(¯µ12,¯µ23,¯µ32), which is a well deﬁned integer, if and only if, ¯ µ12 = ¯µ23 = ¯µ32 = 0. In the
second part of the paper we will interpret this statement as a topo logical condition on the
invariant set of a vector ﬁeld. A precise deﬁnition of ¯ µ-invariants is algebraic and involves the
Magnus expansion of the lower central series of the fundamental group: π1(S3 −L) of the link
complement. We refer the interested reader to the works in [28, 2 9]. In the remaining part
of this section we will prove that ¯µ123(L) is a Hopf degree for an appropriate map associated
to the link L, provided that the link is Borromean, i.e. the pairwise linking numbers are zero
(note that the Borromean links are more general then Brunnian link s, [28]).
Let us review basic facts about the Hopf degree H (f ) of a map f : S3 − →S2, (see
e.g. [6]). A well known property of the Hopf degree is that H : f − →H (f ) provides an
isomorphism between π3(S2) and Z. Recall that up to a constant multiple we may express
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
α ∧ dα, (2.1)
where ν is the area 2-form on S2, and α satisﬁes ω = f ∗ν = dα. Notice that f ∗ν is always
exact since the cohomology of S3 in dimension 2 vanishes. We may also interpret H (f ) as
an intersection number, [6, 30]. Namely, consider two regular values p1 and p2 ∈ S2 of the
map f , then l1 = f −1(p1) and l2 = f −1(p2) form a link in S3, and the integral formula (2.1)
can be interpreted, as the intersection number of l1 with the Seifert surface spanning l2:
H (f ) = lk( l1, l2) . (2.2)
If we replace S3 with an arbitrary closed compact orientable 3-dimensional manifold M, we
may still obtain an invariant of f : M − →S2 this way, provided that the condition f ∗ν = dα
holds.
Proposition 2.1. Let M be a closed Riemannian manifold, and ν ∈ Ω 2(S2) the area form on
S2. The formula (2.1) provides a homotopy invariant for a map f : M − →S2, if the 2-form
f ∗ν is exact. Up to a constant multiple this invariant can be calc ulated as an intersection
number deﬁned in (2.2), where l1 = f −1(p1) and l2 = f −1(p2) form a link in M, where both
l1 and l2 are null-homologous.
3
Proof. Given a homotopy F : I × M ↦→S2, f1 = F (1, · ), f0 = F (0, · ), we deﬁne ˆω = F ∗ν.
We have
ˆω = F ∗ν = d ˆα, ω 1 = f ∗
1 ν = i∗
1 F ∗ν = d α1, ω 0 = f ∗
0 ν = i∗
0 F ∗ν = d α0,
where i0 :֒→ M × I, i0(x) = ( x, 0), i1 :֒→ M × I, i1(x) = ( x, 1) are appropriate
inclusions. Potentials: ˆα
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
therefore the Stokes Theorem immediately implies that Formula (2.1) is independent of the
choice of the potential. For the proof of invariance under homotop ies we revoke the standard
argument in [6, p. 228]
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
The interpretation of H (f ) as the intersection number (2.2) is the same as in [6, p. 230].
Given a 3-component parametrized link L = {L1, L2, L3} in S3 we wish to associate a certain
map FL : S1 × S1 × S1 ↦→S2 to it, and interpret its Hopf degree as the Milnor ¯ µ123-invariant.
Recall the deﬁnition of the conﬁguration space of k points in M:
Confk(M) := {(x1, x2, . . . , xk) ∈ (M)k | xi ⁄= xj, for i ⁄= j}.
As an introduction to the method we review the Gauss formula for th e linking number
of a 2-component link L = {L1, L2} in R3. Denote parameterizations of components by
L1 = {x(s)}, L2 = {y(t)} and consider the map
FL : S1 × S1 L
− →Conf2(R3)
r
− →S2, L (s, t) = ( x(s), y(t)) .
where r(x, y) = x−y
‖x−y‖ is a retraction of Conf 2(R3) onto S2. It yields the classical Gauss
linking number formula:
¯µ12(L) = lk( L1, L2) = deg( FL), deg(FL) =
∫
S1×S1
F ∗
L(ν),
where ν ∈ Ω 2(S2) is the area form on S2. Consequently, the linking number lk( L1, L2), also
known as the Milnor ¯ µ12-invariant, can be obtained as the homotopy invariant of the map
FL associated to L. Observe that homotopy classes [ S1 × S1, S2] are isomorphic to Z and
deg : F → deg(F ) provides the isomorphism, we also point out that as sets: [ Sk, Confn(R3)] =
4
L1 L2
L3
}n
Figure 1: left: ¯ µ123 = ±1 and right: ¯µ123 = ±n.
πk(Confn(R3)), and [ Sk, Confn(S3)] = πk(Confn(S3)) (c.f. [17, p. 421]). Thus considering
the based homotopies, in context of the link homotopy of Borromea n links, and base point
free homotopies is equivalent in this setting.
In [20, 21], authors consider a natural extension of this approach to n-component parame-
trized links L in R3 by considering maps FL : S1×. . .×S1 − →Confn(R3) and their homotopy
classes, we refer to this type of maps loosely as link maps, (c.f. [21]). In particular, Kohno [20]
proposed speciﬁc representatives of cohomology classes of the b ased loop space of Conf n(R3)
as candidates for appropriate link homotopy invariants of L. It has been observed, in [12],
that in the 3-component case it is beneﬁcial to consider Conf 3(S3), and L ⊂ S3, since the
topology of Conf 3(S3) simpliﬁes dramatically (in comparison to Conf 3(R3)). We review this
simpliﬁcation in the following paragraph as it is essential for the proof of the main theorem
in this section.
Consider a 3-component link L = {L1, L2, L3} in S3 parametrized by {x(s), y(t), z(u)}
and the following map
FL : S1 × S1 × S1 L
− →Conf3(S3)
H
− →S2, L (s, t, u) = ( x(s), y(t), z(u)), (2.3)
where we denote by H : S3 × R3 × (R3 \ {0}) ↦→S2 the projection on the S2 factor, ﬁrst
concluding that Conf 3(S3) ⊂ S3 × S3 × S3 is diﬀeomorphic to S3 × Conf2(R3) = S3 × R3 ×
(R3 \ {0}), and consequently deformation retracts onto S3 × S2. Considering S3 as unit
quaternions, the map H can be expressed explicitly by the formula, [12]:
Conf3(S3) ∋ (x, y, z)
H
− → pr(x−1 · y) − pr(x−1 · z)
‖pr(x−1 · y) − pr(x−1 · z)‖ ∈ S2, (2.4)
where · stands for the quaternionic multiplication, −1 is the quaternionic inverse, and pr :
S3 − →R3 the stereographic projection from 1. As a result one has the follow ing particular
expression for FL:
FL(s, t, u) = pr(x(s)−1 · z(u)) − pr(x(s)−1 · y(t))
‖pr(x(s)−1 · z(u)) − pr(x(s)−1 · y(t))‖. (2.5)
5
At this point we note that one has a freedom in choosing the deforma tion retraction
H in (2.4), but the above particular formula makes the proof of the ma in theorem of this
section possible. Let T = S1 × S1 × S1 denote the domain of FL, notice that, thanks to (2.5),
restricting FL to the subtorus T23 in the second and third coordinate ( t, u) of T, we obtain
the usual Gauss map of the 2-component link {x−1 · L2, x−1 · L3}. Since the diﬀeomorphism
x−1· of S3 is orientation preserving we conclude deg( FL|T23) = lk( L2, L3). We claim that for
any 2-component sublink {Li, Lj} of L:
deg(FL|Tij ) = ±lk(Li, Lj), 1 ≤ i < j ≤ 3, (2.6)
where i, j index the coordinates of T. Indeed, since already true for i = 2 and j = 3, the
general case follows by applying a permutation σ ∈ Σ 3 of coordinate factors in Conf 3(S3) ⊂
(S3)3. Notice that σ is a diﬀeomorphism of Conf 3(S3) ⊂ (S3)3 either preserving or reversing
the orientation (which explains the sign in (2.6)). We infer (2.6) becau se σ induces an
isomorphism on homotopy groups of Conf 3(S3).
L1
L2
L3
A2
A1
Figure 2: The model of LBorr parametrized by {L1 = pr(x(s)), L2 = pr(y(t)), L3 = pr(z(u))}.
Arc A1 is a part of the unit circle on xy-plane, A2 is a part of circle of radius 1 + ǫ.
The main theorem of this section is
Theorem 2.2. Let L = {L1, L2, L3} be a 3-component Borromean link in S3, consider the
associated map FL deﬁned in (2.3). The Hopf degree of this map satisﬁes
H (FL) = ±2 ¯µ123, (2.7)
where the sign depends on the choice of orientations of compo nents of L.
Proof. By the Borromean rings we understand any 3-component link with ¯µ123 = ±1. Every
such link is link homotopic to the diagram presented on Figure 1 (where the sign can be
determined from the orientation of components). The proof of th e theorem can be reduced
to the case of Borromean rings LBorr, as follows: if L and L′ are link-homotopic then FL
and FL′ are homotopic maps. By the Milnor classiﬁcation of 3-component links up to link
6
s = 3π
2
s = π
s = π
2
s = 0
Figure 3: Four positions corresponding to angles: s = 0 , π
2 , π, 3π
2 , small arrows next to N
and S indicate a motion as s ր.
homotopy (see [28]), every 3-component link L with zero pairwise linking numbers and
¯µ123 = ±n is represented by the right diagram on Figure 1. Consequently, up t o homotopy,
the associated map FL can be obtained from FLBorr by covering one of the S1 factors in T,
n-times. Therefore, in order to prove the claim it suﬃces to show
H (FLBorr) = ±2 . (2.8)
According to Proposition 2.1, H (FL) is well deﬁned for a link L ⊂ S3 provided F ∗
Lν ∈ Ω 2(T)
is trivial in H 2(T), which is true thanks to (2.6) and because the pairwise linking numbe rs
of L are zero. The method of proof relies on a direct calculation of H (FLBor), for a carefully
chosen parametrization of LBor in S3. This calculation is achieved by visualization of the
link lS,N = lS ∪ lN in T, and application of Formula (2.2), where
lS := F −1
LBor(S), l N := F −1
LBor(N)
are preimages of the North pole N = (0 , 0, 1) and South pole S = (0 , 0, −1) in S2 ⊂ R3.
Notice that [ F ∗
Lν] = 0 in H 2(T), if and only if, [ lS] = 0 and [ lN ] = 0 in H1(T).
We begin by identifying S3 with the set of unit quaternions in R4 with standard coordi-
nates:
(w, x, y, z) = w + x i + y j + z k,
and choosing a speciﬁc parametrization of the Borromean rings LBor in S3. That is, deﬁne
the L1 component of LBor to be the great circle in S3 through 1 and k, parametrized as
x(s) = cos( s) + sin(s) k,
(
x(s)−1 = cos(s) − sin(s) k
)
.
Observe that pr( x(s)) parameterizes the z-axis in R3. Figure 2 shows how to deﬁne the
second and the third component {L2, L3} of the Borromean rings LBorr in R3 considered as
an image of S3 − {1} under the stereographic projection pr : S3 ⊂ R4 − →R3 from 1 ∈ S3.
L2 will bound the annuli with a rounded wedge removed, i.e. an arc A1 of the circle of radius
1. The arc A2 belongs to the circle of radius rǫ = (1 + ǫ) in the ( x, y)-plane. The component
L3 is chosen to be a vertical ellipse linking with L2.
7
π
2
π
2
(A) (B)
(C) (D)
Figure 4: Projection of lS,N on the su-face and st-face of T. The strands lS (solid line) and
lN (dashed line) are oppositely oriented since lS and lN are null homologous in T.
Next we focus on the Formula (2.5), observe that multiplication by x(s)−1 has an eﬀect of
a rotation by angle s in (w, z)-plane and ( x, y)-plane of R4, which can be directly calculated:
x(s)−1 · (w, x, y, z) =
(
cos(s)w + sin(s)z, cos(s)x + sin(s)y,
cos(s)y − sin(s)x, cos(s)z − sin(s)w
)
.
The ﬂow deﬁned by this S1-action is tangent to the great circles of S3, thus the projected
ﬂow on R3, via the stereographic projection pr, presents the standard pic ture of the Hopf
ﬁbration. Let us call an invariant Hopf torus an r-torus, if and only if, it contains a circle
of radius r in the ( x, y)-plane. Without loss of generality we assume that L2 on Figure 2
belongs to the rǫ/2-Hopf torus. Every point on a r-torus traces a (1 , 1)-curve under the S1-
action. For suﬃciently small ǫ, this motion can be regarded as a composition of the rotation
by angle s in both the direction of the meridian and the longitude of a r-torus. Therefore,
for diﬀerent values of s the S1-action “rotates” the components L2 and L3, by sliding along
the Hopf tori by angle s in the meridian and the longitudinal direction. We denote resulting
link components by
Ls
2(t) = pr( x−1(s) · y(t)), and Ls
3(u) = pr( x−1(s) · z(u)).
The unit circle on ( x, y)-plane is left invariant under this action and therefore can be cons id-
ered as the “axis of the rotation”. This justiﬁes the choice of the p articular shape of LBorr
pictured on Figure 2. Next, we seek to visualize the projection of lS,N = lS ∪lN on the su-face
8
and st-face of the domain T of FLBor parameterized by ( s, t, u) ∈ T, (it is convenient to think
about T as a cube in ( s, t, u)-coordinates, see Figure 4). For example when s = 0, ( x(0) = 1),
a point (0 , t0, u0) belongs to lN , if and only if, the vector v0 = pr( y(t0)) − pr(z(u0)) points
in the direction of N = (0 , 0, 1), analogous condition holds for direction S = (0 , 0, −1), and
lS. In order to determine a diagram of lS,N , we must keep track of the “head” and “tail” of
the vector vs = Ls
2(t) − Ls
3(u), for various values of s and record values of t and u for which
vs points “North” and “South” (Figure 3). This reads as the following c ondition
(s, t, u) ∈ lS,N , if and only if , vs ‖ S or N. (2.9)
Without loss of generality we assume that Ls
2 is parametrized by the unit t-interval, and Ls
3
is parametrized by the unit u-interval. The process of recording values of u and t such that
(2.9) holds is self-explanatory and is shown on Figure 2 for values s = 0 , π
2 , π, 3π
2 , which is
suﬃcient to draw projections of lS and lN on st- and tu-faces of T. Collecting the information
on Figure 3, we draw the projection of lS,N on the su-face of T represented by square (A) in
Figure 4. Analogously, the projection of lS,N on the st-face of T is obtained and pictured in
square (B). In order to obtain the diagram of lS,N we resolve the double points of Diagram
(A) into crossings. For example, let us resolve the “circled” double p oint on (A), which
occurs at s = π
2 in the left two stands of lS,N . It suﬃces to determine the value of the
t-coordinate at this point. Diagram (B) tells us that lS is below lN , because T is oriented so
that the t-axis points above the su-face (see Figure 4). Resolving the remaining crossings in
a similar fashion leads to a diagrams of lS,N presented in squares (C) and (D). Clearly, the
linking number of lS and lN is equal to ±2 in Diagram (C), (as the intersection number of e.g.
lS with the obvious annulus on Diagram (C)). This justiﬁes (2.8), and en ds the proof.
Results of Theorem 2.2 and Proposition 2.1 combined with Formula (2.1) allow us to express
¯µ123(L) of a Borromean link L as
¯µ123(L) =
∫
T
F ∗
Lν ∧ α =
∫
T
L∗ω ∧ α,
for F ∗
Lν = dα, ω = H ∗ν ∈ Ω 2(Conf3(S3)),
(2.10)
where ν is the area form on S2, and H : Conf 3(S3) − →S2 is the deformation retraction (as
e.g. in (2.4)). Alternatively, we may view ω as a 2-form on ( S3)3 which is singular along
the diagonals ∆ ⊂ (S3)3, and the singularity is of order O(r2), where r is a distance to ∆ .
Consequently, ω is integrable but not square integrable on ( S3)3.
Remark 2.3. Notice that the integral formula (2.10) exhibits the following proper ty of ¯µ123:
¯µ123(L1, L2, L3) = sign( σ)¯µ123(Lσ(1), Lσ(2), Lσ(3)), σ ∈ Σ 3 .
9
3 Invariants of volume preserving ﬂows. Helicities.
Given ﬁnitely many volume preserving vector ﬁelds B1, B2, . . . Bk ∈ SVect(M) on M = S3
or a homology 3-sphere one seeks quantities I(B1, B2, . . . , Bk) invariant under the action of
volumorphisms isotopic to the identity g ∈ SDiﬀ 0(M), commonly known as helicities or
higher helicities :
I(B1, B2, . . . , Bk) = I(g∗B1, g∗B2, . . . , g∗Bk), for all g ∈ SDiﬀ 0(M), (3.1)
where g∗ is a push-forward by a diﬀeomorphism g. To distinguish the case of a single vector
ﬁeld B (i.e. B = B1 = . . . = Bk) we often refer to I(B) = I(B, B, . . . , B) as self helicity .
We elucidated in the introduction a fundamental example of such inva riant is the ordinary
helicity H(B1, B2) of a pair of vector ﬁelds. In the remaining part of this section we re view
well known formulations of the helicity, which will later help us to point o ut analogies to
the proposed formulation of the 3rd order helicity. Let T = T1 ∪ T2 represent two invariant
subdomains (not necessarily disjoint) under ﬂows of B1 and B2 in S3 and let
T = T1 × T2 ⊂ Conf2(M) ⊂ M × M.
Recall that the formula for H(B1, B2), from [19, 38], specialized to invariant subdomains
T = T1 ∪ T2 may be expressed as
H12(B1, B2) =
∫
T1×T2
ω ∧ ιB1µ ∧ ιB2µ, (3.2)
where ω is known as the linking form on M ×M. When T = M ×M this formula is equivalent
to a more commonly known expression: H(B1, B2) =
∫
M ιB1µ ∧ d−1(ιB2µ) (because ω also
represents the integral kernel of d−1). Philosophically, H(B1, B2) can be derived (c.f. [2])
from the linking number of a pair of closed curves, which is expressed by Arnold’s Helicity
Theorem. For orbits {O 1(x), O 2(y)} of B1 and B2 through x, y ∈ M, we introduce the
following notation for the long pieces of closed up orbits
O Bi
T (x) = {Φ i
t(x) | 0 ≤ t ≤ T } ⊂ O i(x), i = 1, 2
¯O i
T (x) := O i
T (x) ∪ σ(x, Φ i(x, T )). (3.3)
where σ(x, y) denotes a short path, [38], connecting x and y in M (see Section 5). Para-
phrasing [2] we state (for the proof also see [38]),
Theorem 3.1 (Arnold’s Helicity Theorem, [2]) . Given B1, B2 ∈ SVect(M), The following
limit exists almost everywhere on M × M:
¯mB1B2(x, y) = lim
T →∞
1
T 2 lk( ¯O 1
T (x) × ¯O 2
T (y)) . (3.4)
Moreover, ¯mB1B2 is in L1(M × M), and
H12(B1, B2) =
∫
M ×M
¯mB1B2(x, y) µ(x) ∧ µ(y) . (3.5)
10
The function ¯mB1B2 represents an asymptotic linking number of orbits {O 1(x), O 2(y)}, and
the identity (3.5) tells us that the helicity H12(B1, B2) is equal to the average asymptotic
linking number. In coming paragraphs, we will demonstrate, how this philosophy is applied
to obtain the asymptotic ¯µ123-invariant for 3-component links and the third order helicity.
4 Deﬁnition of “ ¯µ123-helicity” on invariant unlinked han-
dlebodies.
In this section we apply the formulation of the ¯ µ123-invariant for the 3-component links in
S3, obtained in Section 2, to deﬁne the third order helicity of a volume pr eserving vector
ﬁeld B on certain invariant sets T of B in S3. In the following paragraphs as a “warm-up”
to a more general case treated in Section 5, we consider the case o f three disjoint unlinked
handlebodies: T = T1 ∪ T2 ∪ T3 in S3 each of genus g(Ti). Henceforth, we use “unlinked” to
mean “with pairwise unlinked connected components”. When T represents three unlinked
tubes (also known as ﬂux tubes [3]) in R3, the third order helicity has been developed by
several authors [5, 27, 25] via Massey product formula for the ¯ µ123-invariant, we compare
our approach to these known works in Section 8.
T Borr
T2
T3
T1
Figure 5: The simplest unlinked handlebodies: ﬂux tubes T Borr modeled on the Borromean
rings (left), and unlinked genus 2 handlebodies (right).
Assume Tis have smooth boundary and B to be tangent to ∂Ti, we set
Bi := B
⏐
⏐
Ti
, i = 1, 2, 3,
and denote the ﬂow of B on S3 by Φ, and ﬂows of restrictions Bi by Φ i. Clearly, such T is
an invariant set of B. Given any domain T with three connected components {Ti} we may
11
always associate a product domain in Conf 3(S3) as follows
T := T1 × T2 × T3 ⊂ Conf3(S3) ⊂ S3 × S3 × S3 . (4.1)
Notice that T is a domain with corners in Conf 3(S3), and we use the same notation for the
product of Ti as for the union in S3. Wherever needed, we also assume that ( S3)3 is equipped
with a product Riemannian metric. Let a domain T deﬁned in (4.1), where Ti ∩ Tj =Ø, i ⁄= j
and each Ti is a handlebody in S3 be called unlinked handlebody, if and only if, the 2-form
ω ∈ Ω 2(Conf3(S3)) deﬁned in Equation (2.10) is exact on T , i.e. ω has a local potential
αω ∈ Ω 1(T ):
ω = dαω . (4.2)
Denote a volume preserving vector ﬁeld B and an unlinked handlebody T as a pair ( B; T ).
Remark 4.1. Since ω is a dual cohomology class to the S2 factor in Conf 3(S3) ∼= S3 × S2,
ω does not admit a global potential.
Because each handlebody Ti has a homotopy type of a bouquet of circles, there is a natural
choice of the basis for H1(Ti) which consists of cycles {Lk
i }k=1,...,g(∂Ti) corresponding to the
circles. We have the following practical characterization of unlinked handlebodies:
Lemma 4.2. T is an unlinked handlebody, if and only if,
lk(Lk
i , Lr
j) = 0 , for all i, j, i ⁄= j (4.3)
Proof. The standard integral pairing, [6], H 2(T ) ×H2(T ) − →R implies that a closed k-form
is exact, if and only if, it evaluates to zero on all k-cycles of the domain. By the K¨ unneth
formula H2(T ) = H2(T1 × T2 × T3) is generated by Lk
i ⊗ Lr
j, and by (2.6):
lk(Lk
i , Lr
j) =
∫
Lk
i ×Lr
j
ω i ⁄= j.
Therefore the condition (4.3) is necessary and suﬃcient for ω to be exact on T .
We deﬁne the ¯µ123-helicity of ( B; T ) denoted by H123(B; T ) or H123(B1, B2, B3) as follows:
H123(B; T ) = H123(B1, B2, B3)
def.
=
∫
T
(
αω ∧ dαω
)
∧ ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3, (4.4)
where µi denotes the pull-back of the volume form µ on S3 under the projection
πi : S3 × S3 × S3 − →S3, π i(x1, x2, x3) = xi, (4.5)
and ιBi is a contraction by a vector ﬁeld Bi. Our notational convention is to denote by ιBiµi
both the forms on the base of πi and the pullbacks: π∗
i
(
ιBiµi
)
. Notice that µ = µ1 ∧ µ2 ∧ µ3
is a volume form on the product: S3 × S3 × S3. There are obvious analogies between
12
Formula (4.4) above, Formula (3.2) for H12(B; T ), and the integral formula (2.10) for the
¯µ123-invariant. The 3-form:
γω := αω ∧ dαω = αω ∧ ω,
plays a role of the linking form as ω in Formula (3.2). The main motivation behind deﬁnition
(4.4) is the ergodic interpretation of H123(B; T ) as an average asymptotic ¯ µ123-invariant of
orbits of B, which will become apparent in Section 5. Formula (4.4) can be also reg arded as
the third order helicity of three distinct vector ﬁelds Bi, supported on the handlebodies Ti.
In Section 7, we indicate how to construct the potential αω from the basic elliptic theory of
diﬀerential forms.
Theorem 4.3 (Helicity Invariance Theorem). On every unlinked invariant handlebody T in
S3, H123(B; T ) is
(i) independent of a choice of the potential αω,
(ii) invariant under the action of SDiﬀ 0(S3), i.e. for every g ∈ SDiﬀ 0(S3):
H123(B; T ) = H123(g∗B; g(T )) . (4.6)
Proof. To prove ( i) observe for every other potential α′
ω of ω, the diﬀerence β = αω − α′
ω is
a closed 1-form on T (since ω = dαω = dα′
ω). Therefore,
H123(B; T ) − H′
123(B; T ) =
∫
T
(β ∧ ω) ∧ ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3
(1)
=
∫
T
d
(
β ∧ αω ∧ ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3
)
=
∫
∂T
β ∧ αω ∧ ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3
(2)
= 0 ,
where in (1) we applied d(ιBiµi) = 0 (since Bi’s are divergence free), and in (2):
ιBiµi
⏐
⏐
∂Ti
= 0,
(because each vector ﬁeld Bi is tangent to the boundary ∂Ti), where
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
The proof of ( ii) is in the style of [5, 27], but adapted to our setting. For any given g ∈
SDiﬀ(S3), by deﬁnition, there exists a path t − →g(t) ∈ SDiﬀ 0(S3), such that
g(0) = id S3, g (1) = g .
Denote by V the divergence free vector ﬁeld on S3, given by V (x) = d
dt g(t, x)|t=0, i.e. g(t) is
a ﬂow of V , and push-forward ﬁelds Bi by
Bt
i := g(t)∗Bi .
13
It is well known (see Appendix A, or [15, p. 224]) that 2-forms: ιBt
i
µ are frozen in the ﬂow
of V , i.e.
d
dt
(
g(t)∗ιBt
i
µ
)
= (∂t + LV )ιBt
i
µ = 0. (4.7)
We also have a path ˆg(t) = ( g(t), g(t), g(t)) in SDiﬀ 0(S3 × S3 × S3), which analogously leads
to the vector ﬁeld ˆV = (V, V, V ). (Recall that a tangent bundle T (S3)3 has a natural product
structure). Equation (4.7) implies
(∂t + L ˆV )
(
π∗
i ιBt
i
µ
)
= (∂t + L ˆV )ιBt
i
µi = 0 . (4.8)
(In the second equation we merely revoke our notational convent ions: ιBt
i
µi ≡ π∗
i
(
ιg(t)∗Biµ
)
).
Let T (t) = ˆg(t)(T (0)) ⊂ Conf3(S3), we must show d
dtH123(Bt
1, Bt
2, Bt
3) = 0. Notice that for
small enough ǫ and t ∈ (t0 − ǫ, t0 + ǫ) we can assume, by ( i), that αω is a time independent
potential obtained from slightly bigger domain ~T which deformation retracts on T (t0), and
satisﬁes
T (t) ⊂ ~T , for t ∈ (t0 − ǫ, t0 + ǫ) .
Without loss of generality set t0 = 0, and ˆg(0) = id (S3)3, at t0 we calculate:
d
dt
(
H123(g(t)∗B1, g(t)∗B2, g(t)∗B3)
)
= d
dt
∫
T (t)
αω ∧ dαω ∧ ιBt
1
µ1 ∧ ιBt
2
µ2 ∧ ιBt
3
µ3
=
∫
T (0)
d
dt ˆg(t)∗(
αω ∧ dαω ∧ ιBt
1
µ1 ∧ ιBt
2
µ2 ∧ ιBt
3
µ3
)
=
∫
T (0)
(
L∂t+ ˆV (αω ∧ dαω)
)
∧ ιBt
1
µ1 ∧ ιBt
2
µ2 ∧ ιBt
3
µ3,
where in the last identity we applied (4.8) and the product rule for the Lie derivative. Now
because ω ∧ αω is time independent (for t ∈ (t0 − ǫ, t0 + ǫ)), Cartan magic formula yields
L∂t+ ˆV (αω ∧ dαω) = L ˆV (αω ∧ dαω) = ι ˆV d(αω ∧ dαω) + d(ι ˆV (αω ∧ dαω))
= d(ι ˆV (αω ∧ dαω)),
where d(αω ∧ dαω) = ω ∧ ω = 0. Since Bt
i are tangent to the boundary of Ti(t), the same
argument as in the proof of ( i) shows that the right hand side of the previous equation
vanishes.
Remark 4.4. Notice that the above argument indicates that if we replace αω ∧ dαω by
virtually any closed 3-form η on Conf 3(S3) (or ( S3)3) we obtain some invariant under frozen-
in-ﬁeld deformations. If η is exact we obtain trivial invariants, therefore the only sensible
candidates here are cohomology classes of Conf 3(S3) ∼= S3 × S2. In dimension 3 it leaves
us with a dual to the S3 factor in Conf 3(S3). Based on the considerations in Section 2 one
may argue that an invariant obtained this way is trivial. Indeed, the c ohomology class η
evaluated on any 3-torus obtained from a 3-component link in S3 via the map L in (2.3) is
14
zero. Therefore, one could apply the ergodic approach of Section 5 to show that
∫
η ∧ ιBµ1 ∧
ιBµ2 ∧ ιBµ3 deﬁnes a trivial invariant. The crucial obstacle in extending the for mula in (4.4)
to encompass the whole ( S3)3 is the fact that the potential αω cannot be globally deﬁned on
Conf3(S3).
5 The ergodic interpretation of H123(B; T )
The following statement is often seen in literature [8, 9]:
Helicity measures the extent to which vector ﬁelds twist and coil around each
other.
A beauty of Arnold’s ergodic approach to the helicity H12(B) is that it makes this statement
precise, by interpreting H12(B) as an average asymptotic linking number of orbits of B. But,
it also has a practical application as it allows us to extend our approac h to certain invariant
sets of B. In this section we apply this philosophy to our newly deﬁned invariant H123(B; T ),
and interpret it as the average asymptotic ¯ µ123-invariant of orbits of B in T . Moreover, this
ergodic interpretation leads us to an alternative, more intuitive pro of of Helicity Invariance
Theorem 4.3.
We begin by observing that given a volume preserving vector ﬁeld B on M and its ﬂow
Φ t, we may regard B as three vector ﬁelds on ( M)3. Thus, (Φ , Φ , Φ) induces a natural R3
action deﬁned as follows:
Φ : R3 × (M)3 − →(M)3,
(
(s, t, u), x, y, z
) Φ
− →(Φ( s, x), Φ( t, y), Φ( u, z)). (5.1)
Observe that Φ is a volume preserving action on ( M)3. Our analysis is rooted in techniques
developed in [2, 24, 25, 38], the main tool is the following
Theorem 5.1 (Multi-parameter Ergodic Theorem, [4]) . For any real valued L1-function F
on (M)3, the time averages under the action in (5.1):
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
converge almost everywhere. In addition, the limit functio n ¯F satisﬁes
(i) ‖ ¯F ‖L1((M )3) ≤ ‖F ‖L1((M )3),
(ii) ¯F is invariant under the Φ -action,
(iii) if (M)3 is of ﬁnite volume then
∫
(M )3
¯F =
∫
(M )3
F . (5.2)
15
Deﬁnition 5.2. Deﬁne invariant unlinked domain T of B as an arbitrary Φ -invariant set,
with topological closure T which belongs to a larger product of open sets ~T = ~T1 ×~T2 ×~T3 in
Conf3(S3), satisfying the following
(A) ~T admits a short path system S,
(B) Equation (4.2) holds on ~T ,
where by a system of short paths on ~T , [38, 3], we understand a collection of curves S =
{σi(x, y)} on each open set ~Ti such that
(a) for every pair of points x, y ∈ ~Ti there is a connecting curve σi(x, y) : I ↦→~Ti in S,
σi(0) = x and σi(1) = y,
(b) the lengths of paths in S are uniformly bounded above by a common constant.
Topologically, every Φ -invariant set is a union of products of orbits of B in (S3)3. It is often
convenient to think of the orbits Φ -action as a foliation of ( S3)3. Then Φ -invariant sets
are just union of leaves of this foliation. A fundamental example of a n invariant unlinked
domain is the case of Φ -invariant set T contained in the product ~T = ~T1 ×~T2 ×~T3 of disjoint
open unlinked handlebodies ~Ti. Note that in this case we do not require B to be tangent to
∂~Ti, and ~T always admits a short path system as we describe in the following
Remark 5.3. In [38], Vogel shows that on a closed manifold M, geodesics always provide
a short path system. When T is contained in the product of unlinked handlebodies ~T we
may easily construct such system on ~T as follows Because Ti are proper subsets of S3 we
generally do not want to use ambient geodesics from S3 as they may not lie entirely in Ti.
To obtain S one puts an artiﬁcial Riemannian metric on each ~Ti which makes ∂~Ti totally
geodesic, and choose S to be geodesics on such Riemannian manifold. Observe that applying
a diﬀeomorphism g ∈ Diﬀ(~T ) to S results in the system gS on g(~T ).
The following result is an analog of Arnold’s Helicity Theorem in our settin g,
Theorem 5.4 (Ergodic interpretation of H123(B; T )). Given (B; T ), the following limit
(asymptotic ¯µ123-invariant of orbits) exists for almost all (x, y, z) ∈ T :
¯mB(x, y, z) = lim
T →∞
1
T 3 ¯µ123
(¯O B1
T (x), ¯O B2
T (y), ¯O B3
T (y)
)
. (5.3)
Moreover,
H123(B; T ) =
∫
T
¯mB(x, y, z) µ(x) ∧ µ(y) ∧ µ(z) . (5.4)
16
Proof. The proof is similar to the one in e.g. [38]. Before we start, we must po int out the
following identity (valid for any 3-form β on M × M × M and vector ﬁelds B1, B2, B3 on M)
(ιB3ιB2ιB1β) ∧ µ1 ∧ µ2 ∧ µ3 = β(B1, B2, B3) µ1 ∧ µ2 ∧ µ3
= β ∧ ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3 . (5.5)
The ﬁrst equation follows from the deﬁnition, the second one is a con sequence of the fact
that ιB is an antiderivation i.e.
ιB(α ∧ β) = ( ιBα) ∧ β + (−1)|α|α ∧ (ιBβ), (5.6)
and ιBiµj = 0, for i ⁄= j (see Appendix A). As a result,
H123(B1, B2, B3) =
∫
T
(
αω ∧ dαω
)
∧ ιB1µ1 ∧ ιB2µ2 ∧ ιB3µ3
=
∫
T
(
ιB3ιB2ιB1
(
αω ∧ dαω
))
µ1 ∧ µ2 ∧ µ3
=
∫
T
mB1,B2,B3(x, y, z) µ1 ∧ µ2 ∧ µ3,
where mB1,B2,B3 := αω ∧ dαω(B1, B2, B3). For convenience, let us set (see (3.3)):
¯O(x, y, z; T ) := ¯O B1
T (x) × ¯O B2
T (y) × ¯O B3
T (y) .
Observe that if the orbit ¯O(x, y, z; T ) is nondegenerate, it represents a Borromean link and
we may apply Formula (2.10) to get
¯µ123
(¯O B1
T (x), ¯O B2
T (y), ¯O B3
T (y)
)
=
∫
¯O(x,y,z;T )
αω ∧ dαω
=
∫
O(x,y,z;T )
αω ∧ dαω + (I),
where the term ( I) involves integrals over short paths in S, (see Appendix B). For degenerate
orbits (such as ﬁxed points etc.), the above formula still makes sen se because ¯µ123 is a
homotopy invariant of the associated map as proven in Section 2. Fo r every ( x, y, z) :
DΦ (x,y,z)[∂i] = Bi, i = 1, 2, 3,
where ∂1 := ∂s,∂2 := ∂t,∂3 := ∂u, thus we obtain
Φ ∗
(x,y,z)(αω ∧ dαω) = ( αω ∧ dαω(B1, B2, B3)(Φ 1(x, s), Φ 2(y, t), Φ 3(z, u)) ds ∧ dt ∧ du
= mB1,B2,B3(Φ 1(x, s), Φ 2(y, t), Φ 3(z, u)) ds ∧ dt ∧ du .
17
Therefore,
∫
O(x,y,z;T )
αω ∧ dαω =
∫ T
0
∫ T
0
∫ T
0
mB1,B2,B3(Φ 1(x, s), Φ 2(y, t), Φ 3(z, u)) ds ∧ dt ∧ du .
Function mB1,B2,B3 is smooth bounded on T and hence L1. Because short paths do not
contribute to the time average (see Appendix B):
lim
T →∞
1
T 3 (I) = 0 .
Theorem 5.1 applied to the function mB1,B2,B3 yields almost everywhere existence of the limit
(5.3). Hence we obtain the invariant L1-function ¯mB := ¯mB1,B2,B3 on T . The identity (5.4)
follows from ( iii) of Theorem 5.1.
Theorem 5.5 (Helicity Invariance Theorem-ergodic version) . On every unlinked domain T
in S3, (i) and (ii) of Theorem 4.3 hold for H123(B; T ).
Proof. The proof of ( i) immediately follows from independence of the limit (5.3) of the choice
of the potential αω. For the proof of ( ii) we must show the following
∫
T
mB1,B2,B3 µ1 ∧ µ2 ∧ µ3 =
∫
g(T )
mg∗B1,g∗B2,g∗B3 µ1 ∧ µ2 ∧ µ3 .
Theorem 5.1 tells us that mB1,B2,B3 and mg∗B1,g∗B2,g∗B3 admit L1-averages ¯mB1,B2,B3 and
¯mg∗B1,g∗B2,g∗B3, under actions of Bi and g∗Bi respectively. It suﬃces to show the following
identity
¯mB1,B2,B3(x, y, z) = ¯mg∗B1,g∗B2,g∗B3(g(x), g(y), g(z)), a.e. (5.7)
then (4.6) is an immediate consequence of Equation (5.2), change of variables for integrals,
and the fact that g preserves volume (i.e. µi = g∗µi). Borrowing notation from the previous
theorem set
g ¯O(x, y, z; T ) := g( ¯O B1
T (x)) × g( ¯O B2
T (y)) × g( ¯O B3
T (z))
= ¯O g∗B1
T (g(x)) × ¯O g∗B2
T (g(y)) × ¯O g∗B3
T (g(z)),
where the second identity is a consequence of the fact that the ﬂo w of g∗Bi is obtained as
a composition of g and the ﬂow of Bi. Since g is isotopic to the identity, ¯O(x, y, z; T ) and
g ¯O(x, y, z; T ) are homotopic as link maps (for nondegenerate orbits they are in f act isotopic
Borromean links in S3) and by theorems of Section 2, we have
¯µ123( ¯O(x, y, z; T )) = ¯µ123(g ¯O(x, y, z; T )).
As a result of the above identity and (5.3) we derive a.e.
¯mB1,B2,B3(x, y, z) = lim
T →∞
1
T 3 ¯µ123( ¯O(x, y, z; T ))
= lim
T →∞
1
T 3 ¯µ123(g ¯O(x, y, z; T )) = ¯mg∗B1,g∗B2,g∗B3(g(x), g(y), g(z)).
18
Notice that in the last equation we used the “pushed forward” shor t paths system: gS. Since
the lengths of paths in gS are bounded as well, they do not contribute to the limit. This
proves the identity (5.7), and consequently (4.6).
Notice that the above argument does not require the Stokes Theo rem, and as such may lead
to further generalizations. Clearly, for H123(B; T ) to be nontrivial T must be of nonzero
measure.
6 Flux formula for H123(B; T ).
The following formula is a well known property of the ordinary helicity H12(B; T ) of the ﬂux
tubes T modeled on a 2-component link L = {L1, L2} (see e.g. [24, 7])
H12(B; T ) = H12(B1, B2) = lk( L1, L2) Flux(B1) Flux(B2). (6.1)
Here we show an analogous property for H123(B; T ), when T is an invariant unlinked han-
dlebody. Recall that {Lk
i }k=1,...,g(∂Ti) denotes the basis of H1(T ) deﬁned in Lemma 4.2.
Proposition 6.1. H123(B1, B2, B3) on invariant unlinked handlebodies T satisﬁes the fol-
lowing formula
H123(B1, B2, B3) =
∑
i,j,k
¯µ123(Li
1, Lj
2, Lk
3) FluxΣ i(B1) FluxΣ j (B2) FluxΣ k(B3), (6.2)
where {Li
1 ⊗ Lj
2 ⊗ Lk
3} is a basis of H3(T ), Flux (Bi) stands for the ﬂux of Bi through a cross
sectional surface Σ k of Ti, which represents the homology Poincar ´ edual of Lk
i in H2(Ti, ∂Ti).
Proof. Recall that the ﬂux Flux Σ k (Bi) of a vector ﬁeld Bi though a cross-sectional surface
Σ k in Ti is given by:
FluxΣ k(Bi) =
∫
Σ k
ιBiµ =
∫
Ti
hk ∧ ιBiµ
=
∫
Ti
ιBihk ∧ µ =
∫
Ti
hk(Bi),
(6.3)
where 1-forms hk represent cohomology Poincar´ e duals of Σ k, and we applied (5.6) in the
third equation. For every closed curve γ ⊂ T hk satisﬁes
∫
γ
hk = #(γ, Σ k) = deg( γ, Lk),
where deg( γ, Lj
k) measures how many times γ “wraps around” the cycle Lj
k.
For simplicity, we ﬁrst assume that T is modeled on a Borromean link L = {L1, L2, L3}
(such as T Borr on Figure 5). Then, h = h1 ∧ h2 ∧ h3 ∈ Ω 3(T ) is a cohomology class dual to
the cycle L1 ⊗ L2 ⊗ L3 in H3(T ). Deﬁne
H := ιB3ιB2ιB1h = h(B1, B2, B3),
19
which is a smooth function, and let ¯H be the time average of H as in Theorem 5.1. It suﬃces
to show
¯mB1,B2,B3 = ¯µ123(L) ¯H, a.e. (6.4)
Analogously, as in the proof of Theorem 4.3, Equation (6.4) immediate ly implies Formula
(6.2). Assume the notation of Theorem 4.3, for given T consider ¯O(x, y, z; T ). Thanks to
Theorem 2.2 (see the ﬁrst paragraph of the proof) we have
¯µ123( ¯O(x, y, z; T )) = ¯ µ123(L)
(
deg( ¯O B1
T (x), L1) deg( ¯O B2
T (y), L2) deg( ¯O B3
T (x), L3)
)
= ¯ µ123(L)
∫
¯O(x,y,z;T )
h .
Therefore,
¯mB1,B2,B3(x, y, z) = lim
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
From the product structure of T and ( iii) of Theorem 5.1 we get
∫
T
¯H =
∫
T
H =
(∫
T1
h1(B1)
)(∫
T2
h2(B2)
)(∫
T3
h3(B3)
)
,
which combined with Equation (6.3) for ﬂuxes concludes the proof in t he case of Borromean
ﬂux tubes. The proof in the case of a general handlebody is analogo us, once we show the
following
Lemma 6.2. Let O = {O1, O2, O3} be a 3-component link in S3 such that Oi ⊂ T i for each
i. Then O is Borromean and
¯µ123(O) =
∑
i,j,k
¯µ123(Li
1, Lj
2, Lk
3) deg(O1, Li
1) deg(O2, Lj
2) deg(O3, Lk
1) . (6.5)
Proof. Thanks to the interpretation of the ¯ µ123-invariant in Section 2, it is not only a link
homotopy invariant, but also a homotopy invariant of the associate d map FO deﬁned in (2.3).
Observe that each component Oi can be homotoped inside of its handlebody Ti to become a
bouquet of circles ˆOi ∼= S1 ∨ S1 ∨ . . . ∨ S1 so that each factor in ˆOi is a multiple of the cycle
represented by {Lj
i }in H1(Ti). As a result, we obtain the associated map F bO, and
¯µ123(O) = 1
2 H (F bO).
Interpreting H (F bO) as the intersection number and summing up intersection numbers w e
conclude (6.5).
20
In the case of Borromean ﬂux tubes, Formula (6.1) reduces to
H123(B1, B2, B3) = ¯µ123(L) FluxΣ 1(B1)FluxΣ 2(B2)FluxΣ 3(B3), (6.6)
where Σ i denotes homology Poincar´ e duals to Li in H2(Ti, ∂Ti).
Since the ﬂuxes are invariant under frozen-in-ﬁeld deformations, Formula (6.1) is yet
another proof of Theorem 4.3 in the setting of invariant unlinked han dlebodies. In [25]
the authors develop the same formula for the Borromean ﬂux tube s. This clearly must be
the case, as we work with the same topological invariants of links via a diﬀerent approach.
Additional advantage of our formulation is that we do not have to se parately deal with null
points of vector ﬁelds as in [25].
