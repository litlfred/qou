---
doc_id: arxiv-2302.08363v2
doc_title: "Prepared for submission to JHEP On the structure of trans-series in quantum field theory"
section_id: sec-010-numerical-analysis
section_title: "Numerical analysis"
section_number: null
pages: 29-31
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Using these recursion relations, the coefficients a0,ℓ can be obtained analytically, order by order.
However, their expressions are very intricate and a general closed formula is unreachable.
One straightforward approach is to obtain the coefficients as exact functions ofN. This way,
one can quickly generate data for different values of N, but it takes significant time to compute
the series. We calculated 20 exact coefficients in this form. In a similar strategy to previous cases,
we estimated the radius of convergence R with the 17-th coefficient of the second Richardson
transform of a0,ℓ/a0,ℓ+1. The convergence error is below 1%. In Fig. 7, we plot this estimate
with all values of N between 6 and 25, as well as from 30 to 100 with steps of 10 and then from
100 to 1000 with steps of 100. In the large N limit we seem to have R(0) = 1, which agrees
with the explicit large N solution, as we explain below. Extrapolating to non-integer values of
N, the radius seems to diverge at ∆ = 1 /3 (N = 5). This is consistent with the fact that the
trans-series vanishes at N = 5 (there is only perturbation theory and the IR renormalon).
More efficiently, one can calculate the coefficients numerically from the onset. Taking 200
digits of precision in the calculation of the ¯ρn, one can generate 200 coefficients at fixed ∆ in a few
minutes. We can obtain more precise estimates for the radius this way, see table 3. We estimate
the error from the convergence of successive Richardson transforms. Strikingly, the convergence
is much faster than in the case of bosonic models. We do not compute the radius of convergence
for the subleading series in this model, since we already know that it is identical to R due to
(5.109).
– 28 –
0.00 0.05 0.10 0.15 0.20 0.25
Δ
0.9
1.0
1.1
1.2
1.3
1.4
1.5
1.6
R(Δ)
Figure 7 . Estimates for the radius of convergence R as a function of ∆ = (N− 2)−1.
N R R h/m b 0
6 1 .588595196530307661805628(3± 7) 0.71482 ... 2.500000(0± 4)
7 1 .0901795077562836000(83± 13) 0.80858 ... 2.500000(2± 7)
8 0 .969970536544952097(5± 4) 0.85994 ... 2.5000(0± 5)
9 0 .92721010523279402(59± 35) 0.89194 ... 2.499(99± 10)
10 0 .9101379331724643(0± 8) 0.91349 ... 2.500(0± 8)
11 0 .903644442840670(26± 11) 0.92881 ... 2.50(00± 14)
12 0 .90204273932404(39± 22) 0.94016 ... 2.5(00± 22)
1000 0 .997821(23± 14) 0.99997 ... 2.4(9± 2)
T able 3. Estimated radius as a function of N, using 200 numeric coefficients. R is the radius in the
y-plane, while Rh is the radius in the h-plane.
It is also instructive to write the radius in terms of the variable h, which can be related to
y through (5.73). The radius in the h-plane, Rh, is related to the radius in the y plane by
Rh =mΓ(1− ∆)
(2e)∆ R− 1
2 (1−2∆). (5.110)
The exact solution F(h) is expected to be singular around its zero at h = m, hence one could
conjecture that the radius of convergence of the trans-series in the h-plane should be m. This is
not the case for our radius estimate Rh, except at large N, as can be seen in table 3. However,
as we previously discussed, this radius is simply an approximation of the radius of convergence
of the full trans-series.
Lastly, assuming the form (2.8), we can estimate b0 by evaluating the auxiliary series on the
l.h.s. of (5.63) for n = 0, where we must plug in the estimate for the radius in table 3. Our
results suggest that b0 = 5/2 and b1 = 3/2 independently of ∆. Like in the case of bosonic
models, one must account for the error both from the convergence of the sequence and from the
estimate of R.
– 29 –
