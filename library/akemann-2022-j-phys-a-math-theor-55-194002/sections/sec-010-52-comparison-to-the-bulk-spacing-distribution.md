---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-010-52-comparison-to-the-bulk-spacing-distribution
section_title: "Comparison to the bulk spacing distribution"
section_number: 5.2
pages: 24-27
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
We now turn to the comparison between the hard edge spacing distribution for different param-
eter values k, Nf and ν, and the bulk spacing distribution (A.1). We will also compare with the
Wigner surmise (1), which is often used in comparison to real data, in order to illustrate the
closeness between the hard edge and bulk spacing.
We begin with the quenched spacing between the first two smallest eigenvalues (k = 1) with
proper unfolding, meaning the first moment is unity, see figure 3. The deviations of this level
spacing distribution from the Wigner surmise (1) or from the bulk spacing distribution (A.1) is
about one percent and can be discerned with the bare eye at the maximum of the distribution.
This has to be seen in contrast to the difference between the Wigner surmise and the bulk
spacing distribution which is only about a few per mill, see [12]. As already mentioned at the
end of section 2, the case k = 1 and ν = Nf = 0 will be the one that should show the strongest
deviations.
One approach to the bulk level spacing is certainly given when increasing k, as we literally
move into the bulk. For simplicity we restrict ourselves to the quenched case (Nf = 0) and a
single flavour (Nf = 1), see figure 4. We find, that the deviation from the bulk spacing decreases
very quickly. Already for k = 3 the difference to the bulk spacing distribution is of the same
order as the difference between the bulk level spacing distribution (A.1) and Wigner’s surmise
23
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 3. Left: comparison between the bulk spacing distributions pbulk(s) (see (A.1))
(dashed black, lower curve), and the spacing distribution between 1st and 2nd eigenvalue
at the hard edge ¯p1(s) with k = 1 and Nf = ν = 0 quenched (red, higher curve), see (88)
and (90). Right: their difference Δ¯p(0,0)
1
(s) = ¯p(0,0)
1
(s) −pbulk(s) (red higher curve) is still
considerably larger than the difference between the exact bulk spacing and the Wigner
surmise (black, dashed curve).
(1). This agrees with our observation for the microscopic level density at the end of section 2.
Introducing flavours only suppresses this difference even more.
A warning is in order. The numerical evaluation of the multiple k-fold integral representa-
tion (87) becomes rapidly unstable when going to higher values of k, ν and Nf. One reason is
the increasing number of integrals to be carried out. Another reason is the ratio of the determi-
nants in the integrand, which can become numerically unstable as the size of the determinant
increases. It may happen that big as well as tiny numbers have to cancel. Metropolis-algorithms
are also hard to implement, though they are in principle possible, because the functions in the
integrand are quite involved.
To overcome this problem we have employed Monte-Carlo simulations of the random
matrix ensemble to study the change of the level spacing distribution when increasing k, in
particular for k ⩾4. For this purpose, we only consider parameter sets with Nf = 0, since oth-
erwise we would need to rely on the Metropolis–Hastings algorithm. This again would exceed
feasible computation time for a sufficiently large matrix dimension and number of configura-
tions. Furthermore, due to the duality between Nf and ν, it is equivalent to only consider ν̸ = 0
or Nf̸ = 0 with masses very close to zero, as discussed in section 4.
As the eigenvalue statistics at the hard and the soft edge are fairly different, as can be seen
in figure 1, where the microscopic spectral densities of those two regions of the spectrum are
displayed, we further want to study the level spacings obtained from numerical simulations,
first for relatively small k, and secondly for the transition from the bulk to the soft edge. To
get the clearest signal, we have first considered ν = 0, as for larger ν we are closer to the soft
edge, cf, figure 1.
Figure 4 highlights that for k ⩾3 the deviation between the level spacing distributions at the
hard edge (equation (86)) and those in the bulk (equation (A.1)) is comparable to the deviation
between the latter and the Wigner surmise (1). We have further quantified this result via a χ2-
test in table 1, where we have computed the L2-distance between level spacing distributions
(86) and (A.1) for various k with Monte Carlo simulations.
It can be seen, that for the transition fromthe hard edgeto the bulk region of the spectrum,the
deviation between the level spacing and the bulk spacing decreases, as it should, and increases
again when reaching the upper edge at k = n −1 = 49 which is a soft edge and, thence, has
to follow the Airy statistics.
24
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Table 1. The χ2-test for the level spacing distributions between the kth and (k + 1)st eigenvalue for ν = 0 at matrix dimension n = 50, in
comparison to the bulk spacing distribution (A.1). We have chosen a bin size of roughly 0.2 and an ensemble size nconf. = 106 to keep the
statistical error below one percent.
k
1
2
3
4
24
46
47
48
49
dχ2
0.084 74
0.009 27
0.004 78
0.004 13
0.002 66
0.003 33
0.004 27
0.037 56
0.201 44
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure
4. Left: comparison between hard edge level spacings for increasing
k = 1 (blue), k = 2 (orange), and k = 3 (green), and the bulk spacing distribution for
Nf = 0 (upper plots), and Nf = 1 (lower plots) with mass m = 0.1. Right: their dif-
ferences Δ¯p(0,Nf)
k
(s) = ¯p(0,Nf)
k
(s) −pbulk(s) to the bulk spacing distribution (A.1) for
k = 1 (blue) and k = 2 (orange) decrease rapidly for increasing k, where for compari-
son we also show the difference between the exact bulk spacing and the Wigner surmise
(black, dashed curve).
If we now look at the level spacing distribution at the soft edge (see figure 5) and the tran-
sition from the bulk to the latter, we find this transition to be equally fast. The differences
obtained from the χ2-test between the numerical data and the bulk spacing are of the same
order as for a spacing in the middle of the bulk, from the third spacing k = 3 upwards and
from k = 47 downwards, as can also be seen in table 1.
