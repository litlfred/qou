---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model"
section_id: sec-009-q-shells
section_title: "Q-shells"
section_number: null
pages: 24-40
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
doc_brief: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model — 11 sections: Introduction; The Lagrangian and Euler-Lagrange ; Radial reduction"
---
The Q-shell solutions are characterized by an internal vacuum region and possess an expansion
around the inner radius,R in, given by:
f(r) =b 2(r−R in)2−b 3(r−R in)3 +b 4(r−R in)4 +...
where the coefficientsb 2,b 3, andb 4 are determined by Equations (IV.1)-(IV.3), with the external
radiusR out formally replaced by the internal radiusR in.
(a)
 (b)
 (c)
FIG. 8.CP 5 Q-shells
As a first example, we present threeCP 5 Q-shell solutions in FIG. 8 . These Q-shells are
characterized by a very small inner radius,Rin. By increasing parameters derived from the coupling
constants of the quartic terms, we obtain a solution that develops an additional peak in the energy
density, as shown in FIG. 8(b) and 8(c). These solutions are particularly interesting because they
are qualitatively different from those previously discussed within theCP N model with a sharp
potential. When these shell-like solutions are coupled to gravity, their spherical configuration and
significant concentration of energy in an outer shell make them viable candidates for boson stars.
In FIG. 9, we plot other Q-shell solutions, specifically those corresponding to higher odd values
ofN. These solutions exhibit an inner radius,R in, that is significantly larger than theR in found
for theCP 5 Q-shells. We have studied numerous solutions of this kind and observed that it is
more difficult to obtain an additional energy density peak for Q-shells associated with a high value
ofN. While the Q-shell in FIG. 9(a) has a dominant contribution to its energy density from
the quadratic terms, the solutions shown in FIG. 9(b) and 9(c) contain a significant contribution
originating from the quartic terms.
To this point, we have focused on specific examples of compact Q-balls, highlighting the behavior
of their profile functions and energy density distributions. In the next section, we provide a more
systematic numerical investigation of both Q-balls and Q-shells across a broader parameter space
and varying coupling constants. Furthermore, we analyze the functional relationship between the
25
(a)
 (b)
 (c)
FIG. 9.CP 11 Q-shells
total energy (E) and the Noether charge (Q(m)
t ) to characterize the stability and properties of these
compact solutions.
E. Energy , Noether charge and radius of the compactons forl= 0,1,2,5
The solutions of the ordinary differential equation (II.23) were obtained using a shooting method
combined with a fourth-order explicit Runge–Kutta method with step size ∆r= 10 −4. The radial
coordinaterwas restricted to the interval [R in,R out], with compacton widthR≡R out−R in≤
20. For fixed coupling constants andω, the solutions are obtained by varying a single shooting
parameterp(0), defined asf(0) forl= 0,f ′(0) forl= 1, andR in forl≥2, until the boundary
conditions|f(R out)|<10 −12 and|f ′(Rout)|<10 −5 are satisfied. The parameterωvaries from 0
to 100 with a step size of ∆ω= 0.02. Solutions exist only forωabove a lower boundω c, which
depends on the model parameters. Note thatω c, determined within our discreteωgrid and limited
by the numerical accuracy of the method, should be regarded as an upper estimate of the true
critical value. Our approach first varies the initial parameterp(0) from 0 (undershoot) up to the
first value corresponding to an overshoot configuration by increasing it successively in small steps
∆p, and then applies binary search to find the value ofp(0) that satisfies the boundary conditions. 1
The fractional powernthat best linearizes the relationship betweenE 1/n andQ (m)
t is determined
by minimizing the residuale P = 1−|rP|via simulated annealing. Here,r P is the Pearson correlation
coefficient defined as:
rP =
PNP
i=1(Q(m)
t (ωi)− Q(m)
t )(E1/n(ωi)− E1/n)
σQ(m)
t
σE1/n
,
1 In cases with multiple solutions, some of which may be unphysical, this approach selects the smallest value of the
parameter that satisfies the boundary conditions. Typically, the maximum value of the shooting parameter starts
(forω= 0) atp max = 1, although it depends on the values ofκ,βe 2 =−2γe 2, andl, and ∆p=p max/600 or even
smaller. After finding the lower value ofωthat leads to a solution, for each larger value ofωthe value ofp max is
updated to twice the value ofp(0) obtained forω−0.02, which also updates the corresponding step size ∆p.
26
where the mean Xand the variationσ X are given by:
X≡ 1
NP
NPX
i=1
X(ωi) andσ X≡
vuut
NPX
i=1
(X(ωi)− X)2,
forX∈{Q (m)
t ,E 1/n}.
The indexilabels the discrete values ofωfor which solutions were obtained. These are restricted
to the rangeQ (m)
t ≤120, resulting in a total ofN P solutions for each set of parameters{l,κ,βe 2 =
−2γe2}. By definition, the coefficient satisfies|r P|≤1. The identity|r P|= 1 (corresponding to
eP = 0) holds if and only if there exists an exact linear relationshipE 1/n =a+bQ (m)
t with real
parametersaandb(b̸= 0). In our analysis,N P is typically on the order of 4800, and the maximum
value ofe P across all studied cases is less than 3×10 −5.
The procedure described above is repeated for three distinct subsets of the data:ω≥20,ω≥50,
and the intervalω c≤ω≤ω c + 2, yielding the exponentsn ω≥20,n ω≥50, andn S, respectively. The
values ofn ω≥20 andn ω≥50 provide estimates fornasωapproaches the large-ωregime, whereas
nS characterizesnin the lowest accessible frequency region. Although these results suggest that
nmay vary across different regimes, a sufficiently small variation allows the power lawE∼Q n to
be maintained as a robust approximation of the energy–Noether charge relation. 2
Assume thatE=α(Q (m)
t )n holds locally near each grid point, with the parametersnandα
varying slowly. To capture the local variation ofnacross differentωregimes more explicitly, we
introduce an effective exponent:n eff = dlnE
dlnQ (m)
t
. For the numerical evaluation, we apply a natural
cubic spline to the data points (x i,yi), wherex i = lnQ (m)
t (ωi) andy i = lnE(ω i). On each sub-
interval, the spline is represented by the polynomialy= P3
j=0bj
i(x−x i)j. Once the real-valued
coefficientsb j
i are determined, the effective exponent at each point is simply given by the first-order
coefficient:n eff(xi) = dy
dx

x=xi
=b 1
i .
FIG. 10 shows that the values ofn,n S,n ω≥20, andn ω≥50 are consistently less than unity,
oscillating within the range 0.79−0.89 for all combinations of the parametersβe 2 =−2γe 2 ∈
{0.1,1,5,40},κ∈{−0.1,−1,−5,−10,−40,−200}, andl∈{0,1,2,5}. Generally, the values of
nclosely track those ofn S. Furthermore, sincenvaries only weakly andE 1/n is approximately
linear inQ(as illustrated in FIGS. 13, 15, 17, and 19), the scaling relationE∼Q n provides a
robust approximation. Although the relation is not exact, the Pearson residuale P remains small.
Consequently, becauseE∼(Q (m)
t )n withn≤1, all Q-balls and Q-shells are stable. Indeed, the
maximum deviation ofn S from the large-ωlimit of 5/6–defined as ∆n≡|n S−5/6|–is 0.05169
(approximately 6%). This peak deviation occurs for the configurationl= 0,βe 2 = 0.1, and
κ=−200, wheren S = 0.88502.
For all casesl∈{0,1,2,5}, the profile functionf(r) becomes small throughout its domain. This
is indirectly indicated by the simultaneous decrease in compacton width (R=R out−R in), energy,
and Noether charge within the large-ωregime. As shown in FIG. 10, all curves in this regime
2 In certain cases, theω-interval associated withn S may overlap with those defined for the large-ωregimes?for
instance, whenω c >20, as observed in configurations with large values ofβe 2 and|κ|. Nevertheless, the interval
corresponding ton S remains more restrictive, provided thatω c <98. This latter condition is satisfied across all
configurations examined in this study.
27
 0.79
 0.8
 0.81
 0.82
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
0.1 1 5 40
β e2
n (l=0)
κ =-0.1
κ =-1
κ =-5
κ =-10
κ =-40
κ =-200
n=5/6
0.1 1 5 40
nS (l=0)
0.1 1 5 40
nω  ≥  20 (l=0)
0.1 1 5 40
nω  ≥  50 (l=0)
 0.79
 0.8
 0.81
 0.82
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
0.1 1 5 40
β e2
n (l=1)
0.1 1 5 40
nS (l=1)
0.1 1 5 40
nω  ≥  20 (l=1)
0.1 1 5 40
nω  ≥  50 (l=1)
 0.79
 0.8
 0.81
 0.82
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
0.1 1 5 40
β e2
n (l=2)
0.1 1 5 40
nS (l=2)
0.1 1 5 40
nω  ≥  20 (l=2)
0.1 1 5 40
nω  ≥  50 (l=2)
 0.79
 0.8
 0.81
 0.82
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
0.1 1 5 40
β e2
n (l=5)
0.1 1 5 40
nS (l=5)
0.1 1 5 40
nω  ≥  20 (l=5)
0.1 1 5 40
nω  ≥  50 (l=5)
FIG. 10. The values ofn,n S,n ω≥20 andn ω≥50 that minimizese P for Q-balls (l= 0,1) and Q-shells
(l= 2,5), for some values ofκandβe 2 =−2γe 2.
28
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
 0.9
 0  0.2  0.4  0.6  0.8  1
β e2 = 0.1
neff
1/ω
κ =-0.1
κ =-1
κ =-5
κ =-10
κ =-40
κ =-200
neff=5/6
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
 0.9
 0  0.1  0.2  0.3  0.4  0.5  0.6  0.7
β e2 = 0.1
neff
f(0)
 0.82
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
 0.9
 0  0.2  0.4  0.6  0.8  1
β e2 = 5
neff
1/ω
 0.82
 0.822
 0.824
 0.826
 0.828
 0.83
 0.832
 0.834
 0.836
 0  0.1  0.2  0.3  0.4  0.5  0.6
β e2 = 40
neff
1/ω
FIG. 11. The effectiveCP 1 exponentn eff as a function of 1/ωforβe 2 =−2γe 2 = 0.1,5,40, and as a
function off(0) forβe 2 =−2γe 2 = 0.1, both for some values ofκ, restricted toω≤50 andQ (m)
t ≤120.
converge towardn≈5/6, thereby reproducing the energy–Noether charge relationE∼(Q (m)
t )5/6
characteristic of the pureCP N model with aV-shaped potential (i.e., in the absence of quartic
terms), as derived in [36]. This behavior arises because, asf(r) remains small everywhere in
the large-ωlimit, contributions from higher-order terms are effectively suppressed. For example,
in the casel= 0,βe 2 =−2γe 2 = 1, andκ=−0.1, the fitted value for the full dataset is
n= 0.86804 (e P∼10−5). Restricting the analysis to solutions withω≥10 yieldsn ω≥10 = 0.83336,
which deviates from 5/6 by only 0.003%, with an extremely low residuale ω≥10
P ∼10−12. In this
configuration,f(0) = 6.9879×10 −3 atω= 10 and continues to decrease asωincreases, confirming
the suppression of the nonlinear profile.
FIG. 11 displaysn eff as a function off(0) forβe 2 = 0.1 andl= 0, as well asn eff versus
1/ωforβe 2∈{0.1,5,40}. The corresponding results forβe 2 = 1 are presented in FIG. 12 for
l∈{0,1,2,5}. Across all cases studied,n eff converges to approximately 5/6 in the large-ωregime
(1/ω→0). In this limit, the profile function at the origin,f(0), becomes small–a behavior
explicitly demonstrated by the correlation betweenn eff andf(0) for theβe 2 = 0.1 case.3 For the
other studied values ofβe 2 withl= 0, the smallness off(0) in this regime can be inferred by
3 To construct then eff plots, we refined the numerical sampling by reducing the step size from ∆ω= 0.02 to
∆ω= 0.002 within the intervalω c≤ω≤ω c + 2. This increased resolution targets the region whereEandQ
attain their maximum values. For the large-frequency regime (ω≥10), a spatial step size of ∆r= 10 −5 was
employed. Furthermore, we imposed the constraintQ≤120 to maintain consistency with the criteria used for
the globalnvalues (see Fig. 10). The analysis was also restricted toω≤50 to exclude solutions with vanishingly
small energy and charge, as such points would otherwise introduce significant numerical uncertainty into the
determination ofn eff.
29
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
 0  0.2  0.4  0.6  0.8  1
l = 0
neff
1/ω
κ =-0.1
κ =-1
κ =-5
κ =-10
κ =-40
κ =-200
neff=5/6
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0.89
 0  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9  1
l = 1
neff
f(0)
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0  0.2  0.4  0.6  0.8  1
l = 2
neff
1/ω
 0.83
 0.84
 0.85
 0.86
 0.87
 0.88
 0  0.2  0.4  0.6  0.8  1
l = 5
neff
1/ω
FIG. 12. The effective exponentn ef f as a function of 1/ωforβe 2 =−2γe 2 = 1 andl= 0,1,2,5, for some
values ofκ, restricted toω≤50 andQ (m)
t ≤120.
cross-referencing FIGS. 14 and 13. Specifically, FIG. 14 indicates that large values ofωcorrespond
to the lowest obtained values of the Noether charge, which in turn correspond to the lower values
off(0) shown in FIG. 13. A similar behavior is observed in FIG. 12 for the cases whereβe 2 = 1
andκ∈{−0.1,−1,−5,−10,−40,−200}acrossl∈{0,1,2,5}. Consequently, the analysis ofn eff is
consistent with and reproduces the results obtained from the study ofn,n S,n ω≥20, andn ω≥50.
FIGS. 11 and 12 also demonstrate thatωc–corresponding to the maximum value of 1/ωat which
the curves terminate–tends to increase with larger values of|κ|orβe 2. Consequently, for large|κ|
andβe 2, the domain of existence in 1/ωcan shrink substantially, as exemplified by theβe 2 = 40
plot in FIG. 11. This contraction of the domain helps explain the reduced variation ofn eff observed
in this regime. For instance, in the casel= 0,βe 2 = 40, andκ=−200, the threshold frequency
reachesω c>50. This leads to the identityn ω≥20 =n ω≥50, as illustrated in FIG. 10.
Across all parameter sets examined, solutions exist forω≥ω c. However, for a fixed relation
βe2 =−2γe 2, variations inκcan lead to significant differences in the threshold frequencyω c.
Under these conditions, the maximum values of the energy and Noether charge often vary by
several orders of magnitude. This wide disparity in scales can render certain curves less prominent
in the figures, as seen, for example, in the configurations withκ=−200 (see FIGS. 13–20).
Regarding theCP 3 solutions illustrated in FIGS. 15 and 16, it should be noted that for high
values of|κ|and small values ofβe 2, the solution curves are confined to the regime of small Noether
30
charges. To ensure these features are discernible, a magnified view is provided in the upper-left
panel of FIG. 15. Furthermore, it should be noted that theCP 3 Q-ball solution exhibits a higher
sensitivity to variations in the parametera 1 than the solutions presented in [36]. In the latter
case, the quadratic coefficient is constant, specificallya 2 = eµ2
32 . However, the inclusion of quartic
terms–under the conditionβe 2 =−2γe 2 modifies this coefficient to:
a2 = eµ2
32
1
1−2κ(βe 2−1)a 1
.
Consequently,a 2 becomes explicitly dependent ona 1 for all cases whereβe 2̸= 1, introducing a
coupling between these expansion coefficients that is absent in purely quadratic models.
The energy, Noether charge, and the maximum value of the profile functionf(r) within the
compacton domain (R in≤r≤R out) can vary by several orders of magnitude asωincreases from
the thresholdω c to the maximum considered value ofω= 100. Specifically, these quantities tend to
decrease monotonically with increasingω. For example, in the casel= 0,βe 2 = 1, andκ=−0.1,
the value at the origin isf(0) = 0.73799 atω= 0.94; this value decreases to 7.0040×10 −5 by
ω= 100.
In the large-ωregime, differences in physical quantities such as the Noether charge and com-
pacton width (see FIGS. 13–20) become less pronounced for a fixed value ofl, provided thatβe 2
andκare not varied drastically. For example, withl= 0 andβe 2 = 1 atω= 30, one finds
f(0) = 7.7803×10 −4 forκ=−0.1 andf(0) = 7.3264×10 −4 forκ=−200; this represents a
reduction of only approximately 5.8% relative to theκ=−0.1 case. In contrast, atω= 1.40, the
values aref(0) = 0.338301 forκ=−0.1 andf(0) = 0.229725 forκ=−200, a significantly larger
reduction of about 32.1%. This behavior is expected, as the diminishing field amplitudes at largeω
effectively suppress the contribution of the quartic terms, leading to a convergence of the solutions.
The energy and Noether charge decrease monotonically withωfor every parameter set
{l,κ,βe 2 =−2γe 2}examined. In the low-ωregime–whereωapproaches the thresholdω c and
1/ωconsequently reaches its maximum–the Noether charge increases rapidly, as illustrated in
FIGS. 13, 15, 17, and 19. Conversely, the critical valueω c tends to increase with the magnitude
of|κ|orβe 2 across all cases (l∈{0,1,2,5}). Indeed, theQ (m)
t curves shift toward smaller values
of 1/ωas|κ|increases, indicating that the system enters the critical regime at higher frequencies.
This behavior is explicitly demonstrated in the plots forβe 2 =−2γe 2 ={5,40}, where theQ (m)
t
versus 1/ωcurves are seen to terminate. These plots clearly demonstrate that the curves terminate
at progressively smaller values of 1/ωas|κ|increases.
FIGS. 14, 16, 18, and 20 demonstrate that the compacton widthRincreases more rapidly at
low Noether charge (the low-ωregime), whereas this growth rate diminishes at larger values of
the charge. In the large-ωregime, theRversusQ (m)
t curves tend to converge, making the differ-
ences between them less pronounced. In this limit, the compacton width decreases monotonically,
becoming significantly smaller asωcontinues to increase.
31
 0
 300
 600
 900
 0  20  40  60  80  100
β e2 = 0.1
E1/n
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 0.2
 0.4
 0.6
 0  20  40  60  80  100
β e2 = 0.1
f(0)
Qt
(m)
 0
 300
 600
 900
 0  20  40  60  80  100
β e2 = 1
E1/n
Qt
(m)
 0
 0.2
 0.4
 0.6
 0  20  40  60  80  100
β e2 = 1
f(0)
Qt
(m)
 0
 0.1
 0.2
 0.3
 0.4
 0  0.01  0.02  0.03  0.04  0.05
β e2 = 5
E1/n
Qt
(m)
 0
 600
 0  100
 
  0
 0.02
 0.04
 0.06
 0.08
 0.1
 0  0.01  0.02  0.03  0.04  0.05
β e2 = 5
f(0)
Qt
(m)
0
0.03
0 10-3
 
 
0
7 × 10-6
0 10-6
β e2 = 40
E1/n
Qt
(m)
 0
7 × 10-3
 0 10-3
 
 0
5 × 10-3
0 10-5
β e2 = 40
f(0)
Qt
(m)
0
7 × 10-4
0 2 × 10-8
 
 
FIG. 13.CP 1 Q-ball fractional energy powerE 1/n andf(0) as functions ofQ (m)
t , for some values ofκand
βe2 =−2γe 2. The corresponding values ofnare shown in FIG. 10.
32
 0
 2
 4
 6
 8
 10
 0  20  40  60  80  100
β e2 = 0.1
R
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 0.1
Qt
(m)
1/ω
 0
 2
 4
 6
 8
 10
 0  20  40  60  80  100
β e2 = 1
R
Qt
(m)
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 1
Qt
(m)
1/ω
 0
 0.5
 1
 1.5
 0  0.01  0.02  0.03  0.04  0.05
β e2 = 5
R
Qt
(m)
 0
 6
 0  100
 
  0
 0.01
 0.02
 0.03
 0.04
 0.05
 0  0.05  0.1  0.15  0.2  0.25  0.3  0.35
β e2 = 5
Qt
(m)
1/ω
 0
 100
 0  1
 
 
 0
 0.06
 0.12
 0.18
 0.24
0 10-6
β e2 = 40
R
Qt
(m)
 0
 1
0 10-3
 
  0
10-6
0  0.055
β e2 = 40
Qt
(m)
1/ω
0
2 × 10-9
      0.02  0.026
 
 
FIG. 14.CP 1 Q-ball radiusRversus the Noether chargeQ (m)
t , andQ (m)
t versus 1/ω, for some values ofκ
andβe 2 =−2γe 2.
33
 0
 500
 1000
 1500
 2000
 2500
 0  20  40  60  80  100
β e2 = 0.1
E1/n
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
0.06
0 2 × 10-3
 
  0
 0.1
 0.2
 0.3
 0  20  40  60  80  100
β e2 = 0.1
df/dr (0)
Qt
(m)
 0
 500
 1000
 1500
 2000
 2500
 0  20  40  60  80  100
β e2 = 1
E1/n
Qt
(m)
 0
300
0 10
 
  0
 0.5
 1
 1.5
 2
 0  20  40  60  80  100
β e2 = 1
df/dr (0)
Qt
(m)
 0
 50
 100
 150
 200
 0  1  2  3  4  5  6  7  8
β e2 = 5
E1/n
Qt
(m)
 0
 2
 0  0.1
 
  0
 0.1
 0.2
 0.3
 0  1  2  3  4  5  6  7
β e2 = 5
df/dr (0)
Qt
(m)
 0
 0.2
0 0.1
 
 
 0
 2
 4
 6
 8
 10
 12
 0  0.1  0.2  0.3  0.4  0.5
β e2 = 40
E1/n
Qt
(m)
 0
0.2
0 7 × 10-3
 
  0
 0.1
 0.2
 0  0.1  0.2  0.3  0.4  0.5
β e2 = 40
df/dr (0)
Qt
(m)
 0
 0.1
0 7 × 10-3
 
 
FIG. 15.CP 3 Q-ball fractional energy powerE 1/n andf ′(0) =df/dr(0) as functions ofQ (m)
t , for some
values ofκandβe 2 =−2γe 2. The corresponding values ofnare shown in FIG. 10.
34
 0
 2
 4
 6
 8
 10
 0  20  40  60  80  100
β e2 = 0.1
R
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 0.1
Qt
(m)
1/ω
 0
 2
 4
 6
 8
 10
 0  20  40  60  80  100
β e2 = 1
R
Qt
(m)
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 1
Qt
(m)
1/ω
 0
 0.5
 1
 1.5
 2
 2.5
 3
 3.5
 0  0.2  0.4  0.6  0.8  1
β e2 = 5
R
Qt
(m)
 0
 8
 0  100
 
  0
 0.2
 0.4
 0.6
 0.8
 1
 0  0.1  0.2  0.3  0.4  0.5  0.6  0.7
β e2 = 5
Qt
(m)
1/ω
 0
 100
 0  1
 
 
 0
 0.05
 0.1
 0.15
 0.2
 0.25
 0.3
 0.35
0 10-6
β e2 = 40
R
Qt
(m)
 0
 5
 0  10
 
  0
10-6
0  0.07
β e2 = 40
Qt
(m)
1/ω
 0
 10
 1
 
 
FIG. 16.CP 3 Q-ball radiusRversus the Noether chargeQ (m)
t , andQ (m)
t versus 1/ω, for some values ofκ
andβe 2 =−2γe 2
35
 0
 1000
 2000
 3000
 4000
 5000
 6000
 0  20  40  60  80  100
β e2 = 0.1
E1/n
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  20  40  60  80  100
β e2 = 0.1
Rin
Qt
(m)
 0
 1000
 2000
 3000
 4000
 5000
 0  20  40  60  80  100
β e2 = 1
E1/n
Qt
(m)
 0
 0.1
 0.2
 0.3
 0.4
 0  20  40  60  80  100
β e2 = 1
Rin
Qt
(m)
 0
 100
 200
 300
 400
 0  1  2  3  4  5  6  7  8
β e2 = 5
E1/n
Qt
(m)
 0
 10
 0  0.2
 
  0
 0.1
 0  1  2  3  4  5  6  7
β e2 = 5
Rin
Qt
(m)
 0
 0.07
0 0.1
 
 
 0
 5
 10
 15
 20
 25
 0  0.1  0.2  0.3  0.4  0.5
β e2 = 40
E1/n
Qt
(m)
 0
 0.3
0 7 × 10-3
 
  0
 0.02
 0.04
 0.06
 0  0.1  0.2  0.3  0.4  0.5
β e2 = 40
Rin
Qt
(m)
 0
 0.04
0 7 × 10-3
 
 
FIG. 17.CP 5 Q-shell fractional energy powerE 1/n and the inner radiusR in as functions ofQ (m)
t , for
selected values ofκandβe 2 =−2γe 2. The corresponding values ofnare shown in FIG. 10.
36
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0  20  40  60  80  100
β e2 = 0.1
R
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 0.1
Qt
(m)
1/ω
 0
 2
 4
 6
 8
 10
 0  20  40  60  80  100
β e2 = 1
R
Qt
(m)
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 1
Qt
(m)
1/ω
 0
 1
 2
 3
 4
 0  0.2  0.4  0.6  0.8  1
β e2 = 5
R
Qt
(m)
 0
 9
 0  100
 
  0
 0.2
 0.4
 0.6
 0.8
 1
 0  0.1  0.2  0.3  0.4  0.5  0.6
β e2 = 5
Qt
(m)
1/ω
 0
 100
 0  1
 
 
 0
 0.1
 0.2
 0.3
 0.4
0 10-6
β e2 = 40
R
Qt
(m)
 0
 6
 0  10
 
  0
10-6
 0  0.01  0.02  0.03  0.04  0.05
β e2 = 40
Qt
(m)
1/ω
 0
 10
 1
 
 
FIG. 18.CP 5 Q-shell radiusR≡R out−R in versus the Noether chargeQ (m)
t , andQ (m)
t versus 1/ω, for
some values ofκandβe 2 =−2γe 2.
37
 0
 5000
 10000
 15000
 0  20  40  60  80  100
β e2 = 0.1
E1/n
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 2
 4
 6
 8
 10
 0  20  40  60  80  100
β e2 = 0.1
Rin
Qt
(m)
 0
 5000
 10000
 15000
 0  20  40  60  80  100
β e2 = 1
E1/n
Qt
(m)
 0
 1
 2
 3
 4
 5
 0  20  40  60  80  100
β e2 = 1
Rin
Qt
(m)
 0
 5000
 10000
 15000
 0  20  40  60  80  100
β e2 = 5
E1/n
Qt
(m)
 0
 15
 0  0.1
 
  0
 1
 2
 3
 4
 5
 0  20  40  60  80  100
β e2 = 5
Rin
Qt
(m)
 0
 20
 40
 60
 80
 0  0.1  0.2  0.3  0.4  0.5
β e2 = 40
E1/n
Qt
(m)
 0
 0.1
0 7 × 10-4
 
  0
 0.5
 1
 1.5
 2
 0  0.1  0.2  0.3  0.4  0.5
β e2 = 40
Rin
Qt
(m)
FIG. 19.CP 11 Q-shell fractional energy powerE 1/n and the inner radiusR in as functions ofQ (m)
t , for some
values ofκandβe 2 =−2γe 2. The corresponding values ofnare shown in FIG. 10.
38
 0
 2
 4
 6
 8
 10
 12
 0  20  40  60  80  100
β e2 = 0.1
R
Qt
(m)
κ  = -0.1
κ  = -1
κ  = -5
κ  = -10
κ  = -40
κ  = -200
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 0.1
Qt
(m)
1/ω
 0
 4
 8
 12
 16
 0  20  40  60  80  100
β e2 = 1
R
Qt
(m)
 0
 20
 40
 60
 80
 100
 0  0.2  0.4  0.6  0.8  1
β e2 = 1
Qt
(m)
1/ω
 0
 1
 2
 3
 4
 0  0.2  0.4  0.6  0.8  1
β e2 = 5
R
Qt
(m)
 3
 8
 1  100
 
  0
 0.2
 0.4
 0.6
 0.8
 1
 0  0.1  0.2  0.3  0.4  0.5  0.6
β e2 = 5
Qt
(m)
1/ω
 0
 100
  0.6  1.5
 
 
 0
 0.3
 0.6
 0.9
 1.2
 1.5
 1.8
 2.1
 0  0.01  0.02  0.03  0.04  0.05
β e2 = 40
R
Qt
(m)
 0
 8
 0  100
 
  0
 0.01
 0.02
 0.03
 0.04
 0.05
 0  0.1  0.2  0.3  0.4
β e2 = 40
Qt
(m)
1/ω
 0
 100
 1.2
 
 
FIG. 20.CP 11 Q-shell radiusR≡R out−R in versus the Noether chargeQ (m)
t , andQ (m)
t versus 1/ω, for
some values ofκandβe 2 =−2γe 2.
39
VI. SUMMAR Y AND REMARKS
This paper successfully generalizes the compact Q-ball type solutions for scalar field models
possessing aCP N target space. Specifically, we have investigated the extended Skyrme-Faddeev
(ESF) model, which augments the traditional Skyrme-Faddeev framework with the inclusion of
a potential and quartic interaction terms. The main objective of this study was to analyze the
influence of these quartic terms on the properties of compact Q-balls.
Similar to our previous results for models without quartic terms, we found two qualitatively
distinct types of solutions: Q-balls and Q-shells. These solutions were obtained via a symmetry
reduction of the model, which parameterizes theN= 2l+ 1 complex scalar fieldsu m using the
product of a time-dependent termeiωt, a radial functionf(r), and spherical harmonicsY lm(θ,ϕ). Q-
balls are compact solutions obtained forCP N models containing fields withN= 1 andN= 3. For
higher odd values ofN, the compactons are qualitatively different, possessing a hollow spherical
region at the center where the scalar field assumes the vacuum value. For this reason, these
solutions are designated as Q-shells. The final radial profile was determined by numerically solving
the resulting radial equation of motion.
The increased complexity of the ESF model, particularly due to the presence of terms quadratic
in powers of derivatives compared to the simplerCP N model, introduces three additional coupling
constants (e−2,β, andγ). This higher complexity necessitated an extra analysis regarding the
existence of mathematical solutions and their physical admissibility (specifically, the positive def-
initeness of the energy density). For this reason, our primary focus was on solutions where the
Hamiltonian density is strictly positive definite. However, we also identified cases where solutions
exhibiting non-negative total energy density may still exist, even when the stricter positive-definite
constraint on the Hamiltonian’s quartic terms is not met.
The analysis of the solutions revealed that the existence of compactons satisfying the boundary
conditionsf(R out) = 0 andf ′(Rout) = 0 depends strongly on the intricate interplay between
the model’s coupling constants, the frequency parameterω, and the shooting parameters (a 0,
a1 orR in). We found that acceptable compact solutions often exist within certain windows in
the parameter space, which are separated by ”forbidden regions” where solutions are either non-
compact or singular. Within the range of acceptable solutions, we noted interesting modifications
to the compacton shapes and the energy density profiles that originate directly from the quartic
terms of the model.
The most striking difference observed is the modification of the bell-shaped profiles of the energy
density, which now develop an extra peak localized in the outer region of the compacton (in the
vicinity ofR out). Such solutions are characterized by a high concentration of energy in this region,
which may be interpreted as a ”dense crust.” The presence of a dense crust–characterized by a
localized extra peak in the energy density near the compacton’s boundary (R out)–is a significant
finding that extends to both Q-shells and Q-balls (such as theCP 3 case). When these extended
solutions are coupled to gravity, they become candidates for boson stars. This crust feature is
particularly interesting because it suggests the possibility of self-gravitating objects with distinct
mass-energy layering. Unlike simplified boson star models that often exhibit smoothly decreasing
40
density profiles, the ESF model, via its quartic terms, provides a mechanism for generating stars
with a highly concentrated, dense outer layer or shell structure. This complex internal makeup
could lead to unique astrophysical signatures, such as altered mass-radius relations or distinct
gravitational wave profiles during merger events, thus offering richer theoretical models for exotic
compact objects.
We have also investigated the stability of Q-balls and Q-shells by analyzing the energy–Noether
charge relation, which is well approximated byE∼Q δ. For our numerical solutions, the parameter
δ, which is typically found in the rangeδ≃0.79–0.89, is always significantly smaller than one,
implying the stability of such compactons.
