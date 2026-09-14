---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THEM ÖBIUS-PLATEAU ENERGY"
section_id: sec-004-33-convergence-in-the-interior
section_title: "Convergence in the Interior"
section_number: 3.3
pages: 5-11
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
doc_brief: "STATIONARY CURVES UNDER THEM ÖBIUS-PLATEAU ENERGY — Plateau problems with elastic boundary energies have been of recent theoretical and applied interest."
---
after passing to a subsequence, uk ⇀ u∗ weakly in W 1,2(D, R3) for some u∗, not necessarily equal to u∞,
and
e(u∗)≤ lim inf
j→∞
e(uj).
Furthermore, from Proposition 1, {uj} is equicontinuous on ∂D and by Arzela-Ascoli, a subsequence {uj}
(not relabelled) converges uniformly on∂D. Since each uj is harmonic, we have from the maximum principle
that
sup
D
|uj−uk| = max
∂D
|uj−uk|.
Thus{uj} converges uniformly on D to u∗. Moreover, uniform convergence implies that u∗ : ∂D→ γ∞ is
monotone and onto, so therefore u∗∈D γ∞. We thus obtain the desired inequality,
e(u∞) = inf
u∈Dγ∞
e(u)≤ e(u∗)≤ lim inf
j→∞
e(uj).
With this, we have established the lower semicontinuity of E, and γ∞∈A is an energy minimizer. We
can thus arrive at the main theorem for this section:
Theorem 10. There exists γ∞∈A which minimizes E.
6 MAX LIPTON AND GOKUL G. NAIR
4. Necessary Conditions of M ¨obius-Plateau Critical Helix Pairs
In this section, we alter the problem slightly to consider the M¨ obius energy of links, whereγ1,γ 2 : R→ R3
are disjoint locally rectifiable curves. The M¨ obius energy of the link is defined as
EM(γ1,γ 2) =
Z
R×R
| ˙γ1(u)|| ˙γ2(v)|dudv
|γ1(u)−γ2(v)|2 .(8)
In the link case, we do not subtract an intrinsic distance term in the integrand, as it is not needed for
the integral to converge. At a given point γ1(u), the L2 gradient of the M¨ obius energy is given by the
vector-valued integral
Gγ1,γ2(u) = 2
Z
R
2P ˙γ1(u)⊥(γ2(v)−γ1(u))
|γ2(v)−γ1(u)|2 − Nγ1(u)
 | ˙γ2(v)|dv
|γ2(v)−γ1(u)|2.(9)
The derivation of the variational equation for the M¨ obius energy of knots is given in [FHW94], and He [He02]
showed the equation also holds in the case of links. Here, P ˙γ1(u)⊥ refers to the projection onto the plane
normal to the tangent vector at γ1(u), and Nγ1(u) refers to the normal vector in the Frenet frame along γ1.
The gradient is defined similarly along γ2 by switching u and v.
A rough heuristic for interpreting (9) is that curves with large M¨ obius gradient are those in which many
rescaled pairwise difference vectors are close to Frenet binormals. The integral projects a rescaled difference
vector onto the curve’s normal plane, and subtracts the Frenet normal, leaving only the binormal. The
rescaling obeys an inverse quartic law, so difference vectors between nearby points of the curve which ap-
proximate the binormal well will contribute greatly to the gradient integral. The binormal of a helix points
roughly in the direction of its axis, hinting that helices provide a fruitful set of examples in studying the
dynamics of the M¨ obius energy. Using explicit helix parametrizations turns (9) into an improper trigono-
metric integral, which we analyze with power series and elementary estimates. In a forthcoming paper, the
first author analyzes the M¨ obius variations for helix pairs using complex variable techniques distinct from
the methods in this section.
Whilst both energies are infinite, the variational equation describing critical parametrizations remains
well-defined. Let ν be the oriented unit surface normal to Σ. Now, the direction of the L2 gradient of the
Plateau energy at γ1(u) (resp. γ2(v)) is the unit conormal n =−T× ν (resp. T× ν). This unit vector
is oriented so that it is pointing away from the surface at each of the boundary components, which in turn
defines the orientation of ν. The derivation of the gradient for the Plateau energy is a standard calculation
which can be found in Prop. 1 of [GPT21]. Thus, the variational equation for the M¨ obius-Plateau energy is
αGγ1,γ2 =−βn.(10)
A general helicoid Σ = Σ(ω) has parametrization


x(s,t )
y(s,t )
z(s,t )

 =


s cos(ωt)
s sin(ωt)
t

.(11)
Definition 1. A helicoidal strip is the parametrized surface in (11) with A≤s≤B,t∈ R, for prescribed
A<B . A helicoidal screw corresponds to the case where A and B have opposite signs, and a helicoidal
ribbon corresponds to the case where A and B have the same signs.
The two boundary curves γ1 and γ2 of a helicoidal strip are found by setting s =A and s =B. We will
parametrize the curves with u and v respectively.
Remark. In the prior sections, we were careful in considering the possibility of sudden transitions in the
Plateau solutions induced by small variations of the boundary curve. As the frequency parameter of a helix
changes, there can be a so-called “Courant headphone transition” where the area-minimizing surface jumps
from a helicoid to a surface between the vertical layers resembling a telephone cord. In Courant’s time,
headphone cords probably looked like this, hence the name. The transition parameters are discussed in
[Cou40] and [MAGP16]. As this section is concerned with necessary conditions for critical helix pairs, we
do not take these transitions into account. As we will see later, numerical searches for critical helix pairs
bounding a ribbon show their widths are orders of magnitude smaller than the frequency, precluding the
possibility of a headphone transition. In other words, the Plateau solution for the critical helix pair is their
common helicoid.
STATIONARY CUR VES UNDER THE M ¨OBIUS-PLATEAU ENERGY 7
The space of helicoidal screws and ribbons are given by the three parameters A,B, and ω. A helicoidal
strip is a screw if and only if it contains the helical axis, and otherwise it is a ribbon. For given α and
β, we seek to find the values of A,B, and ω which satisfy the variational equation of the M¨ obius-Plateau
energy. The variational equations for stationary helix pairs differs in the case of screws and ribbons, because
of the differing orientations of N, which we will see results in two trigonometric integrals that nominally
look similar, but greatly vary in how the signs of their evaluations depend on their parameters.
For fixedω, the boundary helices are invariant under “screw” transformations which rotate the xy-plane
by angle ωt whilst translating in the z direction by t. As the screw transformations are a subgroup of
Euclidean isometries (and also of the larger M¨ obius group of R3), the gradient flow of the M¨ obius energy
starting at a helix preserves symmetries under the screw transformations (cf. p.42 of [FHW94]). Therefore,
Gγ1,γ2 is tangent to Σ(ω), and to calculate the entire M¨ obius gradient vector fields alongγ1 andγ2, it suffices
to compute them at two particular points along the boundary curves and then apply screw transformations.
The same symmetry rule also holds for computing the Plateau gradient vector fields along the helices, as the
Plateau energy is invariant under Euclidean isometries.
Observe that
˙γ1(u) =


−ωA sin(ωu)
ωA cos(ωu)
1

,
and that| ˙γ1(u)| =
√
ω2A2 + 1 for all u. We also have| ˙γ2(u)| =
√
ω2B2 + 1 for all v. Furthermore,
¨γ1(u) =


−ω2A cos(ωu)
−ω2A sin(ωu)
0

.
Next, for given surface parameters s and t, the tangent plane to Σ is given by
T Σ = span
(
∂s


x
y
z

,∂t


x
y
z


)
= span
(

cos(ωt)
sin(ωt)
0

,


−ωs sin(ωt)
ωs cos(ωt)
1


)
.
So at u = 0, we have the following:
γ1(0) =


A
0
0

, ˙γ1(0) =


0
ωA
1

, ¨γ1(0) =


−ω2A
0
0

.
From this, we can see that Nγ1(0) = (±1, 0, 0), depending on the sign of A. We can also see that
Tγ1(0)Σ = span{(1, 0, 0), (0,ωA, 1)}, and thus ν = 1√
ω2A2+1(0,ωA, 1). Hence, n = (−1, 0, 0).
Next, observe
P ˙γ1(0)⊥
 
γ2(v)−γ1(0)

=
 
γ2(v)−γ1(0)

−⟨γ2(v)−γ1(0), ˙γ1(0)⟩ ˙γ1(0)
| ˙γ1(0)|2
=


B cos(ωv)−A
B sin(ωv)
v

− ωAB sin(ωv) +v
ω2A2 + 1


0
ωA
1


=


B cos(ωv)−A
B sin(ωv)−Aωv
ω2A2+1
v− v+ωAB sin(ωv)
ω2A2+1

.
Finally, it is straightforward to see that|γ2(v)−γ1(0)|2 =A2−2AB cos(ωv)+B2+v2. For now, we will make
the assumption that A <0 < B, which means N = (1, 0, 0). Putting all of this together, the variational
8 MAX LIPTON AND GOKUL G. NAIR
(a) A stationary asymmetric helicoidal screw.
 (b) A stationary symmetric helicoidal screw.
Figure 1. Two stationary helicoidal screws with identical parameters A =−1,ω = 2,
except B≈ 6.15375 in the figure on the left, whilst B = 1 in the figure on the right. In
these examples, we set α = 2,β = 1
equation becomes the system:
2α
Z ∞
−∞
 2 (B cos(ωv)−A)
A2− 2AB cos(ωv) +B2 +v2− 1
 √
ω2B2 + 1
A2− 2AB cos(ωv) +B2 +v2dv =β(12)
Z ∞
−∞
B sin(ωv)− v+ω2A2B sin(ωv)
ω2A2+1
(A2− 2AB cos(ωv) +B2 +v2)2dv = 0
Z ∞
−∞
v− ωAB sin(ωv)+v
ω2A2+1
(A2− 2AB cos(ωv) +B2 +v2)2dv = 0.
The last two integrands are odd functions in v, which means the integrals are always going to be zero, so
only equation (12) relevant to us. Through identical computations by taking v = 0, noting that in this case
we have Nγ2(0) = (−1, 0, 0) and n = (1, 0, 0), we see the first component of the variational equation at γ2(0)
is
2α
Z ∞
−∞
 2 (A cos(ωu)−B)
A2− 2AB cos(ωu) +B2 +u2 + 1
 √
ω2A2 + 1
A2− 2AB cos(ωu) +B2 +u2du =−β.(13)
Relabelling the variable of integration and adding (12) and (13) yields
(14) 4 α
Z ∞
−∞
(A +B)(cos(ωv)− 1)
(A2− 2AB cos(ωv) +B2 +v2)2dv =β
 1√
ω2B2 + 1
− 1√
ω2A2 + 1

.
This single equation leaves us with a two parameter family of stationary helicoids controlled by the constants
α andβ. From direct inspection, it is clear thatA =−B is a solution, which we call the symmetric stationary
helicoidal screw. It is straightforward to numerically search for other solutions of (14). For instance, setting
α = 2,β = 1,A =−1,ω = 2, and solving for B gives solutions B = 1 and B≈ 6.15375. The two helicoidal
screws are pictured in 1. In the numerical searches we ran, we generally found that under most choices
of parameters, the symmetric solution had a larger basin of attraction than the asymmetric solution. An
analysis of the attraction properties of the solutions is yet to be done.
The full description of this family, especially with respect to its singularities, is not fully known. When
we tried to find solutions to the variational equation for helicoidal ribbons, derived below, we had difficulties
finding solutions, and we suspected at first that no solutions existed. During our attempt to prove this
lack of solutions, we had difficulty in bounding the negative contribution to the variational integral, and we
later found that solutions do indeed exist, but only under comparatively strict conditions. Furthermore, the
solutions we did manage to find have parameters which differ in orders of magnitude, which contributed to
the difficulty in the numerical search.
STATIONARY CUR VES UNDER THE M ¨OBIUS-PLATEAU ENERGY 9
Theorem 11. A stationary helicoidal ribbon must have high frequency (equivalently, low pitch), very small
width in comparison to the frequency, and remain close to the axis. That is, the following conditions on the
parameters must hold:
(1) ω >1
(2) |B−A|2 <C (α,β )ω
(3) |A +B|< 2.
Remark. We only prove the case when α = β = 1. In the general case, the bounds (20) and (24) are
scaled by powers of α and β, though (16) is unchanged. One may verify these bounds still sum to a
positive number as required in the last step of the proof, but this only further complicates the algebra
without fundamentally altering our reasoning. Our numerical search suggests the second condition could
be considerably strengthened to the form |B−A|k1 < Cβk2
αk3ω, with the optimal exponents ki yet to be
determined. Modifying the bound in (24) is more difficult since we could get a family of rational functions
in ω controlled by α and β, and so a numerical approximation does not rigorously justify a lower bound.
When applying the M¨ obius-Plateau energy to mainstream Euler-Plateau problems, it is likely necessary to
vary the coefficients α and β, so understanding their precise scaling effects is imperative.
Proof. Without loss of generality assume 0<A<B . We may also assumeω >0 because the cosine function
is even. This is tantamount to fixing the chirality of the helicoids under consideration to being right-handed.
Observe Nγ1(0) = (−1, 0, 0), so the−1 term in (12) corresponding to −N becomes a +1 whilst (13) remains
unchanged. Adding these two nontrivial variational equations at γ1(0) and γ2(0) yields
4
Z ∞
−∞
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2
(A2− 2AB cos(ωv) +B2 +v2)2 dv =
 1√
ω2B2 + 1
− 1√
ω2A2 + 1

.(15)
We will show that except in a very limited circumstance, the integrand on the lefthand side of (15) is always
positive. When the integrand can take negative values, we will then show that unless all of the conditions
listed are met, then the integral is positive. The righthand side of (15) is negative, as B >A, so we will get
our desired result.
The denominator is obviously positive. As for the numerator, we break down into cases. Suppose A +
B− 2AB≤ 0. Then
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2≥A2−A +B2 +A +B− 2AB +v2
= (B−A)2 +v2 > 0.
For the remainder of the proof, assumeA+B−2AB >0 and we will break down into further cases. Assume
A +B≥ 2. Then
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2≥A2−A +B2−B− (A +B− 2AB) +v2
= (A +B)(A +B− 2) +v2 > 0.
Next, assume A +B <2 with ω≤ 1. From the Taylor formula, cos(ωv)≥ 1− ω2v2
2 ≥ 1− v2
2 . Now see that
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2≥A2−A +B2−B + (A +B− 2AB)

1− v2
2

+v2
= (B−A)2 + v2
2 (2AB−A−B + 2)
> v2
2 (2AB−A−B + 2)
≥ v2
2 (2AB)≥ 0.
So in all of the cases we have considered for A,B , and ω so far, the integrand in (15) is positive and so the
variational equation will have no solutions.
Now, assume A +B <2 with ω >1. It is only in this scenario that the numerator could take negative
values and possibly lead to the integral in (15) being negative. For instance, when A = 0.1,B = 1,ω = 10,
the integrand takes negative values as shown in Figure 2.
10 MAX LIPTON AND GOKUL G. NAIR
Figure 2. A graph of the integrand in (15) with A = 0.1,B = 1, andω = 10, as a function
of v.
As the integrand is an even function in v, it suffices to prove
Z ∞
0
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2
(A2− 2AB cos(ωv) +B2 +v2)2 dv >0,
when the second condition in our theorem is negated. Our method will be to overestimate the magnitude of
the contribution of the negative part of the integrand whilst underestimating the contribution of the positive
part of the integrand, and show that the positive contribution still outweighs the negative contribution. To
estimate the negative contribution, we integrate the quadratic Maclaurin series over [0, 1
4], and then compute
a lower Riemann sum over{cos(ωv)< 0}∩ [0, 1]. When (B−A)2 >cω , wherec is some constant independent
of the parameters, we get (20) and (24). The computation is detailed in an appendix.
As we saw, for v≥ 1, the integrand is strictly positive. So consider the contribution of the tail
Z ∞
1
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2
(A2− 2AB cos(ωv) +B2 +v2)2 dv >0.
We see that A2− 2AB cos(ωv) +B2 +v2≥ (A +B)2 +v2. Combining this with (21), we can conclude that
the denominator is bounded above by (4 + v2)2. Likewise, we again observe by (22) that the numerator is
bounded below by (A +B)(A +B− 2) +v2. Therefore, the numerator is bounded below by v2− 1. Putting
all this together, we have
Z ∞
1
A2−A +B2−B + (A +B− 2AB) cos(ωv) +v2
(A2− 2AB cos(ωv) +B2 +v2)2 dv≥
Z ∞
1
v2− 1
(4 +v2)2dv
= 1
32 (4 + 3π− 6arccot(2))
≥ 3
10.(16)
By adding our bounds from (20),(24), and (16), we can conclude the integral is positive. □
Negating the second condition was crucial in our proof, as we otherwise would not be able to obtain the
bound in (20), as the coefficient − 1
(B−A)4 tends to−∞ as (B−A)→ 0+, which makes the bound useless in
limiting the contribution of the negative parts of the integrand. We also used this assumption in (23) in order
to force the Riemann sum approximation to be of order O(ω−4). Were we to na¨ ıvely the use the inequality
A2 +B2 +v2≥ 0 +
  π
2ω
2
, our Riemann sum approximation would be of order O(ω4) with a leading negative
coefficient, which tends to−∞ as ω→∞ , again preventing a bound for the negative contribution.
STATIONARY CUR VES UNDER THE M ¨OBIUS-PLATEAU ENERGY 11
Figure 3. Contours in the AB-plane for (15) and (17), with α = β = 1,ω = 10, and
approximate region of integration [−10000, 10000]. The intersection of the contour curves
is (A,B )≈ (0.810515, 0.818991) which is in the valid parameter space {(A,B ) : 0 < A <
B,A +B <2}.
With the restrictions on the parameters in mind, we found approximate numerical solutions to the vari-
ational equations for stationary helicoidal ribbons. Our analysis so far has only dealt with the sum of the
variational equations for γ1 and γ2, so to solve the full variational system, we included the difference of the
two variational equations, which is
4α
Z ∞
−∞
(B−A) cos2 ωv
2

(A2− 2AB cos(ωv) +B2 +v2)2dv =β
 1√
ω2A2 + 1
+ 1√
ω2B2 + 1

.(17)
Both sides of this equation are clearly positive for B >A, and hence there are no further obvious restrictions
on the parameters for A andB, which is why we opted to study (15) in order to characterize the stationary
ribbons.
In our numerical search, we evaluated the integrals corresponding to (15) and (17) on the finite interval
[−10000, 10000] via a Gaussian quadrature with precision set to 10 −6. With α = β = 1 and ω = 10, we
obtained the contour plot depicted in 3. The intersection of the contour lines for (15) and (17) was found
to be (A,B )≈ (0.810515, 0.818991), which corresponds to a width of B−A≈ 0.008476. The effects of this
intersection point under bifurcations of α,β , and ω is yet to be investigated.
