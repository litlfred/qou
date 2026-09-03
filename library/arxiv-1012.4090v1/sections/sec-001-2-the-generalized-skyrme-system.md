---
doc_id: arxiv-1012.4090v1
doc_title: "Generalized Skyrme Crystals"
section_id: sec-001-2-the-generalized-skyrme-system
section_title: "The Generalized Skyrme System"
section_number: 2
pages: 1-5
source_pdf: 1012.4090v1.pdf
source_sha256: 02fe4a5eb36ff0ed
doc_brief: "Generalized Skyrme Crystals — This letter deals with triply-periodic (crystalline) solutions in a family of Skyrme systems, namely where the ﬁeld takes values in the squashed 3-sphere."
---
In this section, we give some details of the one-parameter
interpolating family of Skyrme systems. The ﬁeld is de-
noted Φβ = (Φ1, Φ2, Φ3, Φ4), where each component Φβ is
a function of the spatial coordinates xj = (x1,x 2,x 3) =
(x,y,z ), and the constraint Φ βΦβ = 1 is imposed. The
energy density for the system, parametrized by α∈ [0, 1],
is
E =λ2[(∂jΦβ)(∂jΦβ)−αPjPj]+λ4[2(1−α)Fj
βγFj
βγ+αQjQj],
(1)
Preprint submitted to Physics Letters B April 21, 2022
arXiv:1012.4090v1  [hep-th]  18 Dec 2010
where
Pj = Ω βγΦβ∂jΦγ,
Fj
βγ = 1
2εjkl(∂kΦβ)(∂lΦγ),
Qj = Ω βγFj
βγ,
with Ωβγ being a symplectic form with non-zero compo-
nents Ω 12 = −Ω21 = −Ω34 = Ω 43 = 1. The coupling
constants λ2 and λ4 can be scaled as desired, by chang-
ing the units of energy and length; in what follows, we
shall use the ‘geometrical’ choice λ2 = 1/[4π2(3−α)] and
λ4 = 1/[4π2(3− 2α)] as in [8]. The eﬀect of this is that
the energy of a 1-skyrmion on R3 is approximately inde-
pendent of α (E1≈ 1.22).
If we are thinking of the Skyrme model as a nonlin-
ear theory of pions, then the deformation when α becomes
positive may be viewed as putting one of the three pions on
a diﬀerent footing from the other two. To see this explic-
itly, we impose the boundary condition Φ µ→ (0, 0, 0, 1)
as|xj|→∞ , and identify (Φ1, Φ2, Φ3) as the pion ﬁelds in
the usual way. Then in the asymptotic region the energy
density (1) becomes
E≈ λ2[(∂jΦ1)2 + (∂jΦ2)2 + (1−α)(∂jΦ3)2]. (2)
If α = 1, then one of the ﬁelds becomes non-dynamic.
This amounts to passing from the original target space
S3∼= SU(2) to the quotient space S2∼= SU(2)/U(1), by
the Hopf projection
ψ1 = 2(Φ 1Φ3− Φ2Φ4),
ψ2 = 2(Φ 2Φ3 + Φ1Φ4),
ψ3 = Φ 4
3 + Φ2
4− Φ2
1− Φ2
2. (3)
The relevant ﬁeld is then the unit 3-vector ⃗ψ, and the
energy density (1) becomes
E = 1
32π2
[
(∂j⃗ψ)2 + 1
4(Gjk)2
]
, (4)
whereGjk = ⃗ψ·(∂j⃗ψ)×(∂k⃗ψ). This is the Skyrme-Faddeev
energy [11].
The energy E[Φ] is the integral of (1) over R3, or
over a fundamental cell if one is dealing with periodic
ﬁelds. There is a Bogomolny-type lower bound [9] on
the energy of ﬁelds with topological charge N, namely
E≥ 6N√λ2λ4 vol (Σ). Using the fact that the volume of
the squashed 3-sphere is 2 π2√1−α, and with our choice
of λ2 and λ4, this gives
EN≥
√1−α√
(1−α/3)(1− 2α/3)
. (5)
In the limit α = 1, the bound (5) becomes trivial.
There are various nontrivial bounds in this case. For iso-
lated Hopf solitons on R3, we know that EN ≥ cN−1/4,
where c is a constant; it is conjectured that this bound
holds for c = 1 [12]. This bound is not valid for triply-
periodic ﬁelds Φ : T 3 → S2; but in that case there is
another lower bound, which follows from the general for-
mula given in [13]: if Φ is triply-periodic, and L is the
largest of its periods, then its normalized energy satisﬁes
EN≥π/(2L).
Forα = 0, the expression (1) gives the standard static
Skyrme energy, and it has an obvious O(4) symmetry. For
α⁄= 0, the symmetry is broken to U(2), this being the
subgroup of O(4) which preserves the symplectic form Ω.
In this letter, we are focusing on crystalline conﬁgura-
tions, so the ﬁelds are periodic in (x1,x 2,x 3) with periods
(L1,L 2,L 3) respectively. In eﬀect, Φ is a map from T 3 to
S3, and it is classiﬁed topologically by its degree N∈ Z.
The topological classiﬁcation of maps fromT 3 toS2, which
is relevant to the α = 1 case, is more complicated. But
if we restrict to ﬁelds which are algebraically inessential,
meaning that the 2-form Gjk belongs to the trivial coho-
mology class in H 2(T 3, Z), then the classiﬁcation remains
a single integer N∈ Z (cf. [14]). The Hopf charge of the
Hopf projection ⃗ψ of Φ is equal to the degree of Φ, so it is
consistent to let N denote either.
3. Crystals in the Generalized Skyrme F amily
In this section, we investigate various triply-periodic
solutions in the family of generalized Skyrme systems para-
metrized byα. There are many of these, corresponding to
diﬀerent local minima of the energy, and we shall describe
only some of them.
The results that follow are obtained by numerical min-
imization of the energy functional E[Φ]. More speciﬁcally,
the expression for the energy is replaced by a second-
order ﬁnite-diﬀerence approximation on a rectangular lat-
tice with periodic boundary conditions, and the minima
are found by conjugate-gradient relaxation. Testing with
various diﬀerent values of the lattice spacing indicates that
the accuracy, for example in the energy E, is better than
1%. As remarked above, there are many local minima, and
the initial conﬁguration determines which one of these is
obtained after ﬂowing down the energy gradient. We also
vary the side-lengths L1, L2 and L3 of the fundamental
cell, so as to get the lowest possible value of E[Φ].
In the original Skyrme system ( α = 0), the lowest-
energy crystal is a cubic lattice [1]. Its unit cell contains
eight half-skyrmions, and has N = 4. We begin by taking
this as the initial conﬁguration, and minimizing E[Φ] for
various values of α.
In the α = 0 case, the minimum occurs at L1 =L2 =
L3 = 4.7; but the side-lengths cease to be all equal when
α> 0. This occurs because the system has less symmetry
than when α = 0; in particular, one of the spatial direc-
tions, which we take to be the x3-direction, is now on a
diﬀerent footing from the other two. For α >0, the half-
skyrmions become elongated in the x3-direction, and the
optimal side-lengths satisfy L1 =L2 >L 3. These aspects
2
are illustrated in Figure 1. The upper-left plot shows the
optimal (minimal-energy) values of L1 = L2 and L3, as
functions of α, in the range 0 ≤ α≤ 0.9. We see that in
Figure 1: The V+AV+V+AV solution. Optimal values of L1 =L2,
and L3; and the energy density for α = 0.3, 0.6, 0.9.
the Skyrme case α = 0, we have L1 = L2 = L3 = 4.7, as
noted above; but as α increases, the lattice cells are com-
pressed in the x3-direction and expanded in the x1- and
x2-directions. The behaviour in the α = 1 limit will be
discussed in more detail below. The other three pictures
in Figure 1 plot the energy density E, or more precisely
the surfaces whereE equals 0.7 times its maximum value,
for three values of α ranging from 0.3 to 0.9. We see that
as α increases, the half-skyrmions join up pairwise in the
x3-direction, to form four parallel vortices; these are in
fact two vortices and two antivortices, and so this ﬁeld
is called the V+AV+V+AV solution. In the α→ 1 limit,
the vortices become homogeneous in thex3-direction; such
vortices will be discussed in more detail below.
The symmetries of theα> 0 ﬁelds depicted in Figure 1
are a subset of the α = 0 skyrme-crystal symmetries [1],
and are generated by
xj↦→Lj−xj, Φ4↦→− Φ4 for j = 1, 2, 3; (6)
xj↦→Lj/2−xj, Φj↦→− Φj for j = 1, 2, 3; (7)
(x1,x 2,x 3) ↦→ (x2,−x1,x 3),
(Φ1, Φ2, Φ3, Φ4) ↦→ (Φ2, Φ1, Φ3,−Φ4). (8)
The normalized energy of these solutions is plotted in
Figure 2, as a function ofα. The other plots in Figure 2 are
the Bogomolny bound (5), and the energies of two other
triply-periodic solutions which will be described below.
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
0.5
0.6
0.7
0.8
0.9
1
1.1
α
EN
Normalized energy of crystal solutions
 
 
Bound
V+AV+V+AV
2V+2AV
Multi−sheet
Figure 2: Normalized energy EN of crystalline solutions, versus α.
At this point, let us say more about x3-homogeneous
vortices. The ﬁeld of ap-vortex with unitx3-twist, located
on the x3-axis, can be put in the form
Φ1 + iΦ2≈ (x1 + ix2)p, Φ3 + iΦ4≈ exp (2πix3/L3) (9)
near that axis. If p > 0, we refer to it as a p-vortex,
whereas if p < 0 we refer to it as a p-antivortex. If we
restrict the Hopf projection ψ of Φ to the planex3 = 0, we
get a map fromT 2 toS2; the degree of this map is the total
vortex number in the x3-direction (taking the multiplicity
p of each vortex into account). This total vortex number
has to be zero, since it is the degree of a Hopf projection. In
other words, there have to be an equal number of vortices
and antivortices. The topological charge N is the sum of
the absolute values of the vortex numbers; in other words,
vortices and antivortices both contribute positively to N.
Theα = 0.9 ﬁeld illustrated in Figure 1 is close to an N =
4 multi-vortex conﬁguration, with two 1-vortices and two
1-antivortices, and hence is referred to as V+AV+V+AV.
It is worth noting that analogous V+AV+V+AV con-
ﬁgurations can appear in the α = 0 case, for values of the
side-lengths Lj which diﬀer from the optimal ones [15].
Skyrme vortices, or more precisely vortex-antivortex
pairs, were discussed in [16]. In particular, it was shown
there that if one has a parallel vortex-antivortex pair sep-
arated by a (large) distance D, then there is an attractive
force between them, the leading term of which is propor-
tional to 1 /D. In our α-family, the expression for the
attractive force is the same, except that it acquires a fac-
tor of 1 −α. In other words, vortices and antivortices
attract one another, as long as α< 1. In the α→ 1 limit,
however, the leading-order term vanishes. It is not known
whether there is still an attractive vortex-antivortex force
in this limit, but numerical experiments suggest that the
force becomes repulsive. In particular, the two vortices
and two antivortices in our picture repel each other when
α = 1, and therefore L1,L 2→∞ as α→ 1, consistent
with the upper-left plot in Figure 1.
The second vortex-type solution featuring in Figure 2
3
is 2V+2AV, and it consists of a 2-vortex and a parallel
2-antivortex. Its energy is plotted for α≥ 0.6, and it is
apparent that in this range, its energy is less than that of
V+AV+V+AV. In this case, the numerical evidence again
suggests that L1,L 2→∞ as α→ 1, implying that the 2-
vortex and the 2-antivortex repel each other in that limit.
The four pictures in Figure 3 plot the energy density iso-
surfaces whereE equals 0.8 times its maximum value, for
four values of α ranging from 0.6 to 0.99.
Figure 3: The 2V+2AV solution: energy densities for α =
0.6, 0.7, 0.8, 0.99.
Note that in the α = 1 (Skyrme-Faddeev) system, we
can have vortices without antivortex partners — the re-
striction of the net vortex number being zero does not
apply in this case. Such Hopf-vortex ﬁelds have been the
subject of several studies, such as [17, 5, 7]. The results
described above suggest that in the Skyrme-Faddeev sys-
tem, the normalized energy of a p-vortex decreases as p
increases. This indeed turns out to be the case, as we now
explain in more detail.
Consider ﬁelds⃗ψ with energy density (4) onR2×S1. So
⃗ψ is periodic inx3 with periodL, and it satisﬁes the bound-
ary condition ⃗ψ→ (0, 0, 1) as ρ→∞ , where x1 + ix2 =
ρeiθ. More speciﬁcally, consider rotationally-symmetric p-
vortices centred on the x3-axis: these will have the form
ψ1 + iψ2 = sin (f) exp(ipθ + 2πix3/L), ψ 3 = cos (f),
(10)
wheref =f(ρ) satisﬁesf(0) =π andf(ρ)→ 0 asρ→∞ .
Finding the minimal energy E(p) for various values of the
vortex number p is a straightforward numerical computa-
tion, and this was done for p = 1,..., 5. Let us, as usual,
normalize the energy E(p) by dividing it by the topologi-
cal charge p. The result is that E(p) depends linearly on
1/p:
E(p)≈ 0.338/p + 0.551;
and it is this value (with, respectively, p = 1 and p = 2)
which is used for the α = 1 ends of the V+AV+V+AV
and 2V+2AV plots in Figure 2.
In view of the above, it seems likely that triply-periodic
solutions with even lower values ofEN than V+AV+V+AV
and 2V+2AV could be constructed by assembling parallel
arrays of p-vortices and p-antivortices for p≥ 3; but this
has not been investigated further.
The solutions corresponding to the ﬁnal plot in Fig-
ure 2, referred to as “multi-sheet”, have a lower value of
energy-per-charge than the others mentioned previously if
α≥ 0.9, and do not resemble parallel vortex-antivortex
conﬁgurations for α close to 1. Figure 4 shows the energy
density isosurfaces whereE equals 0.8 times its maximum
value, for four values of α ranging from 0.6 to 0.99. As
Figure 4: The “multi-sheet” solution: energy densities for α =
0.6, 0.8, 0.9, 0.99.
α approaches 1, they are closely approximated by ﬁelds
which are homogeneous in x1 and x2, in fact of the form
Z1 := Φ1 + iΦ2 = sin( f) exp(2πiε2x2/L2), (11)
Z2 := Φ4 + iΦ3 = cos( f) exp(2πiε1x1/L1), (12)
where ε1 =±1, ε2 =±1, and f = f(x3). Their energy
density depends only on x3, and is peaked on sheets or-
thogonal to the x3-axis. Such ﬁelds arise if we impose the
symmetries generated by
x1↦→x1 +c, (Z1,Z 2)↦→ (Z1,Z 2 exp(2πiε1c/L1)); (13)
x2↦→x2 +c, (Z1,Z 2)↦→ (Z1 exp(2πiε2c/L2),Z 2); (14)
(x1,x 2)↦→ (−x1,−x2), (Z1,Z 2)↦→ (Z1,Z2). (15)
Note that such transformations on ( Z1,Z 2) preserve the
energy (1). In other words, translations in x1 or x2, and
an inversion, can be compensated by a symmetry trans-
formation of the ﬁeld.
In order to have periodicity in x3, and for the topo-
logical charge N to be nonzero, we need to arrange things
rather carefully. A periodic ﬁeld with N = 4 is obtained
by imposing f(kL3/4) =kπ/2 for k = 0, 1, 2, 3, 4, and
(ε1,ε 2) =



(1, 1) for 0 ≤x3 <L 3/4,
(−1, 1) for L3/4≤x3 <L 3/2,
(−1,−1) for L3/2≤x3 < 3L3/4,
(1,−1) for 3 L3/4≤x3 <L 3.
4
Note that the resulting ﬁeld is continuous.
Substituting (11, 12) into the formula (1) for the energy
density gives an expression of the form E = A(f) (f′)2 +
B(f), where f′ = df/dx3. Then a standard Bogomolny
argument implies that, for given values of L1 andL2 (and
α), the normalized energy E attains a minimum value
E(α,L 1,L 2) = 2L1L2
∫ π/2
0
√
ABdf, (16)
when L3 is given by
L3 = 4
∫ π/2
0
√
A/Bdf. (17)
The next step is to minimize (16) with respect to L1 and
L2, which was done using numerical integration. The re-
sulting minimal energy for the ansatz (11, 12) approaches
that of the multi-sheet solution (which is not quite homo-
geneous inx1 andx2) asα→ 1. For example, if α = 0.98,
then the ansatz energy (16) is only 0 .6% higher than that
of the actual multi-sheet solution, and the ﬁelds are almost
identical.
For α≥ 0.9, the multi-sheet solution has the lowest
energy-per-charge of those that we investigated. However,
theα→ 1 limit of this solution, and of the ansatz, is rather
pathological, since the optimal values of L1 =L2 tend to
zero. In fact, the energy (16) equals
E = 2π
∫ π/2
0
√
2λ2
2 sin2(2f)L2
1 + 4π2λ2λ4 sin4(2f)df
(18)
when α = 1 (and where we have put L1 = L2), from
which it is clear that its minimal value is attained when
L1 = 0. At ﬁrst sight, this behaviour may seem paradox-
ical, since the usual view is that the fourth-order Skyrme
term in the energy prevents an object with nontrivial 3-
dimensional topology from shrinking to zero volume. This
view is indeed correct for 0 ≤ α < 1: in particular, if α
lies in this range, then a triply-periodic conﬁguration with
nonzero topological chargeN has an energy which diverges
if any of its periods tends to zero. But in the α = 1 limit,
namely for the Skyrme-Faddeev system, this property no
longer holds. One can see directly from (11, 12), or rather
its Hopf projection, why this is so. If one scales each of the
periods Lj, then each term in the expression of the energy
of ⃗ψ scales diﬀerently. In particular, the term
∫
(G12)2 has
the form
∫
(G12)2dx1dx2dx3 =K L3
L1L2
,
where K is its value when L1 = L2 = L3 = 1. This is
the only term which prevents L1 and L2 from going to
zero simultaneously. But for (11, 12) the quantity G12 is
identically zero, and consequently one can always lower
the energy by reducing L1 and L2.
