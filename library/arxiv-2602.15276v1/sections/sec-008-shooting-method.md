---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model"
section_id: sec-008-shooting-method
section_title: "Shooting method"
section_number: null
pages: 17-24
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
doc_brief: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model — 11 sections: Introduction; The Lagrangian and Euler-Lagrange ; Radial reduction"
---
To determine the radial profile function, we numerically integrate the radial equation (II.14),
starting from either the center (r= 0) or the inner radius (r=R in). The resulting numerical
solution is dependent on a single free parameter:a 0 forl= 0,a 1 forl= 1, orR in forl≥2. By
selecting an appropriate value for this parameter, the radial function can simultaneously satisfy
the external compacton boundary conditions,f(R out) = 0 andf ′(Rout) = 0.
It is important to note that the numerical value of the parameterωis significant. As with
theCP N model, not all values ofωare permissible. For certain values, the radial function may
become unbounded, which indicates a non-physical solution. Our analysis will focus exclusively on
finite-energy solutions.
18
B.CP 1 Q-balls
When the leading behavior of the radial functionf(r) in the vicinity of the origin (r= 0) is
described by a parabolic function,f(r) =a 0 +a 2r2 +..., we can search for compact Q-balls similar
to the establishedCP 1 Q-balls discussed in [36]. This approach is particularly relevant as the model
approaches the limit 1/e 2→0,β→0, andγ→0. However, being interested in a wider range
of coupling constants, we analyze several cases, including those with non-trivial parameter values
where the quartic terms play an active role. Given the extensive size of the complete parameter
space, a detailed study of the entire region is beyond the scope of this paper. Instead, our aim
is to highlight a few interesting cases that differ significantly from established models, thereby
demonstrating the specific influence of the quartic terms in the Lagrangian.
Before discussing compactons, we present three characteristic examples of radial functions ob-
tained by numerically integrating the radial equation as a function of the free parametera 0. For
the first case, depicted in panel (a) of Figure 2, the radial curve exhibits a positive second deriva-
tive at the center (a 2 >0). This results in a curve that never reaches the vacuum value off= 0.
Consequently, the solution is physically unacceptable as it corresponds to infinite total energy.
The stationary constant solution,f 0, is depicted by the red dashed line in the figure. It is
determined as the solution to the algebraic equation derived from the constant-field limit of the
radial equation:
1−f 2
0
(1 +f 2
0 )3/2f0 = ˜µ2
8ω2.
The exact analytic solution forf 0 was used to plot this line; however, due to its highly complex
nature, it will not be presented here. For small values off 0, the solution can be accurately
approximated by the simpler linear relationf 0≈ ˜µ2
8ω2 .
(a)
 (b)
 (c)
FIG. 2. Radial solutions for theCP 1 model are characterized by the value ofa 0. The solutions fall into
three categories: (a) those witha 2 >0, (b) those witha 2 <0 and (c) the compacton case, where the radial
function and its derivative simultaneously vanish at the external radius, i.e.,f(R out) = 0 =f′(Rout).
For the second case, depicted in panel (b) of FIG. 2, the solution is characterized by a negative
value for the second derivative (a2<0). The radial curve shown, however, still does not represent
an acceptable physical solution.
Finally, the third panel (c) represents a curve for which the value ofa 0 has been precisely
adjusted (via the shooting method) to satisfy the compacton boundary conditions:f(R out) = 0
19
andf ′(Rout) = 0. In this case, the non-trivial solution can be smoothly matched with the constant
vacuum solution,f(r) = 0. This type of solution, understood as a weak solution to the differential
equation, possesses a finite energy value and is therefore physically acceptable. The matching point
is denoted byR out and is referred to as the outer radius of the compacton.
In the example provided, a compacton solution can be obtained for a specific value of the
parameterω. However, this is not a general case. For certain values ofω, it is possible that as the
central field valuea 0 is increased, and the first local minimum approaches the horizontal axis, the
second derivative at the center,f′′(0), may reach negative infinity before the fieldf(r) reaches zero
at the radiusRdetermined by the conditionf ′(R) = 0. Consequently, a more detailed analysis of
the central coefficienta 2, as given by Equation (IV.6), is necessary to precisely define the parameter
regions where physical solutions exist.
In FIG. 3, we plot the coefficienta 2 as a function of the central amplitudea 0, varying the
frequencyωwhile keeping all other coupling constants fixed. To improve the clarity of the anal-
ysis, we also plot the numerator and the denominator of the expression fora 2 (Equation (IV.6))
separately. For better visibility in the plot, the denominator has been scaled by a factor of 48.
FIG. 3. The dependence of the coefficienta 2 on the parametera 0 is shown for increasing values ofωfor the
CP 1 case.
The top-left panel of FIG. 3 illustrates the coefficienta 2 for a low frequency, specificallyω=
0.624, wherea 2 is strictly positive (a2>0). In this case, both the numerator and the denominator
of Equation (IV.6) are positive for all relevanta 0. We therefore do not expect a compacton solution
for parameter values that result in a positivea 2. Asωincreases, we observe that the numerator
becomes a function exhibiting two zeros. Due to the complexity of the equation, we cannot provide
an exact analytic expression for these zeros. Asωincreases, the range ofa 0 for whicha 2 is negative
also expands. It is possible for this region to contain a compact solution, provided that, within the
admissible values ofa 0, there exists one for which the profile functionf(r) and its first derivative
20
f′(r) simultaneously vanish at some radiusR out. This situation is depicted in the top-right panel.
For higher values ofω, the situation changes further, as the denominator also develops a negative
part. The zeros of the denominator lead to vertical asymptotes fora 2. This scenario is depicted
in the bottom-left panel. The zeros of the denominator are given by the expression:
a(±)
0 =
s
−(2 +α)±
p
α(4 +α)
2 , α≡κω 2(βe2−4) (V.1)
where the existence of real solutions requiresα≤−4, providing that:
κω2≤− 4
βe2−4 .(V.2)
We note thata (−)
0 <a (+)
0 , and we have omitted the unphysical solutions corresponding to negative
values ofa 0. Further increasingωcauses the left zero of the denominator (a (−)
0 ) to become smaller
than the right zero of the numerator. As a consequence, a window wherea 2 >0 is created. This
window expands asωincreases, progressively excluding more values ofa 0 from the set of permissible
initial conditions that could yield a compact solution. The bottom-right panel illustrates this
situation. It is important to note that condition (V.2) establishes a limit on the relationship
between parametersκandω. For a fixed coupling constantκ, for instance, the parameterωhas a
minimum permissible value given byω min = 2√
−κ(βe2−4).
The conditionα≤−4 is not a significant restriction on the parameter space; it simply corre-
sponds to the existence of vertical asymptotes in the plot ofa 2. When the parameter is in the
range−4< α≤0, the denominator ofa 2 has no real zeros, and consequently, the formula (V.1)
does not apply. This latter scenario arises in the limit where the quartic terms decouple, leading
back toward the pureCP N model.
In FIG. 4, we plot the sign of the coefficienta 2 as a function of the central amplitudea 0 and
the frequencyω, for several fixed values of the couplingκ. The gray color denotes the region where
sgn(a2) =−1. These regions are the only parts of the parameter space that may contain compacton
solutions, although their existence is not guaranteed. In the third panel, we plot horizontal lines
that correspond to the specific values ofωused to generate FIG. 3. This composite figure clearly
demonstrates that the parameterωalways has a minimum permissible value (ω min), below which
no compact solutions exist.
The behavior of both the numerator and the denominator ofa 2 (Equation (IV.6)) is highly
dependent on the model’s parameters. For instance, when we change the coupling constant to
βe2 = 6.0 (compared toβe 2 = 5.0 used in the example shown in FIG. 3), the denominator reaches
zero before the numerator asωis increased. This shift alters the range ofa 0 that can yield compact
solutions. While a detailed parameter map covering all possible solutions is desirable, obtaining
such a map is far beyond the scope of this paper.
Returning to the case withβe 2 = 5.0 andκ=−5.0, we vary the parametera 0 in an attempt
to obtain compact Q-balls. The first scenario, illustrated in the top-right panel of FIG. 3, does
not yield acceptable compact solutions. For this case, the values ofa 0 that result in a negativea 2
form a very shallow minimum, and within this permissible range, the minimum off(r) is unable to
21
FIG. 4. The sign of the coefficienta 2 is shown as a function of the parametersa 0 andωfor theCP 1 case
withβe 2 = 5.0 andγe 2 =−2.5. The gray color indicates regions where sgn(a 2) =−1. The horizontal lines
that correspond to the values of the parameterωused to generate Fig. 3, specificallyω= 0.624,ω= 0.854,
ω= 0.906 andω= 0.94.
reach zero. Similarly, for the case shown in the bottom-left panel, we also did not obtain a solution
that satisfies the compacton criteria. Finally, we consider the case illustrated in the bottom-right
panel of FIG. 3. Forω= 0.94, we are still unable to obtain the desired solution. However, as
ωis increased further, the left vertical asymptote shifts towarda 0 = 0. This allows the negative
coefficienta 2 to reach larger absolute values for smalla 0, which in turn enables the minimum of
f(r) to reach zero. An example of a Q-ball obtained forω= 3.0 is shown in FIG. 5(a). The upper
panel displays the functionsf(r) andf ′(r), while the bottom panel shows the total energy density,
eH(r). Additionally, the contributions from the quadratic and potential terms, eH02(r), and the
quartic terms, eH4(r), which constitute the total energy density, are plotted separately. It is worth
noting that there are two values ofa 0 for whicha 2 has the same negative value. The compacton
was obtained for the smaller of these two values. For the larger value, we were unable to obtain a
compact solution.
In the example presented in FIG. 5(a), the contribution of the quartic terms is minimal. To
investigate a more significant influence from these terms, we increase the magnitude of the coupling
constantκ. For instance, settingκ=−11 yields another compact solution. However, to obtain this
solution, the value of the frequencyωmust be increased. This adjustment is necessary because,
at lower frequencies (e.g.,ω= 3.0), the second derivativef ′′(0) approaches negative infinity before
the local minimum off(r) reaches the required zero value for a compacton. This new solution,
depicted in FIG. 5(b), demonstrates a more pronounced contribution of the quartic terms, eH4(r),
to the energy density. A notable difference, when compared to solutions in models lacking quartic
interactions, is the presence of a shallow local minimum in the total energy density located precisely
at the center of the Q-ball. The necessity of increasingωcan be understood by examining the top
panel of FIG. 5(c). The maximum permissible value of the shooting parametera 0 is constrained
by a vertical asymptote, whose position shifts to higher values asωincreases. For certain values
ofω, the second derivative of the radial function becomes singular before the compacton condition
(f(R out) =f ′(Rout) = 0) can be satisfied. The position of the left asymptote,a (−)
0 , as defined in
Equation (V.1), is further illustrated as a function ofωfor several values of the parameterκin the
bottom panel of FIG. 5(c).
22
(a)
 (b)
 (c)
FIG. 5.CP 1 Q-balls. (a) Radial profiles and energy density for a solution with a minimal contribution
from quartic terms. (b) Radial profiles and energy density for a solution with a significant contribution from
quartic terms, demonstrating a shallow local minimum at the origin. (c) The top panel shows the coefficient
a2 as a function ofa 0 in the region wherea 0 <a (−)
0 . The bottom panel shows the position of the left vertical
asymptote,a (−)
0 , as a function ofω.
We also examined numerical solutions based on the expansionf(r) =a 0 +a 1r+..., wherea 1
is given by Equation (IV.7). Despite the existence of this linear expansion around the center, we
were unable to obtain compact solutions (Q-balls) in this scenario. Many of the numerical curves
generated in this case grew indefinitely with radius, rendering them unphysical.
C.CP 3 Q-balls
In this section, we present some compact Q-ball solutions for theCP 3 case (corresponding to
l= 1 orN= 3). The radial solution for these Q-balls exhibits a dominant linear behavior at the
center, specificallyf(r) =a 1r+a 2r2 +..., where the coefficienta 2 is determined by Equation
(IV.8).
The Q-ball solution presented in FIG. 6(a) is qualitatively similar to those found in theCP N
model with a sharp potential, where the initial contribution from the quartic term to the energy
density is small. However, increasing the coupling constant (κ) for the quartic terms significantly
modifies the energy density plot, as shown in FIG. 6(b). Further increases to the coupling constants
lead to the development of an extra peak in the energy density, clearly visible in FIG. 6(c) . This
characteristic behavior of the energy density, including the formation of additional peaks, is a direct
consequence of the quartic terms present in the model’s Lagrangian.
The requirement for the positive definiteness of the energy density led us to impose the con-
straintβe 2+2γe 2 = 0, which explicitly eliminates the term proportional to 2κ(βe2+2γe 2) 3ω4f2−f′4
(1+f2)4
from the Hamiltonian density. However, this eliminated term does not always result in a negative
contribution to the energy, as its sign depends on the relative magnitudes of 3ω4f 2 andf ′4. There-
23
(a)
 (b)
 (c)
FIG. 6.CP 3 Q-balls satisfying the constraintβe 2 + 2γe2 = 0. The discontinuity of the second derivative,
f′′(R) precisely matches the discontinuity caused by the signum function in the field equation.
(a)
 (b)
,
(c)
FIG. 7.CP 3 Q-balls forβe 2 + 2γe2̸= 0
fore, some solutions that do not satisfy this constraint (βe 2 + 2γe2 = 0) may still be considered
physically acceptable provided the total energy density remains positive. We present a few such
solutions in FIG. 7. In the first example, shown in FIG. 7(a), the coupling constants of the quartic
terms are relatively small; however, the contribution to the energy density originating from these
terms is already dominant. This signifies that the term proportional toβe 2 + 2γe2 provides the
main contribution. Increasing the absolute values of the parametersκ,βe 2, andγe 2 leads to a
further increase in the contribution from the quartic terms, as shown in FIG. 7(b) and 7(c) . This
example successfully demonstrates that it is reasonable to explore compact solutions within the
shadowed region below the lineβe 2 + 2γe2 = 0, as shown in FIG. 1, broadening the permissible
parameter space.
24
