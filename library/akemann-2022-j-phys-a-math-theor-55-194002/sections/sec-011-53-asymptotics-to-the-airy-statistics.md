---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-011-53-asymptotics-to-the-airy-statistics
section_title: "Asymptotics to the Airy statistics"
section_number: 5.3
pages: 27-30
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
Another limit is the large-ν limit which should approach the level spacing distributions at the
soft edge. Actually this also holds when the number of flavours Nf is sent to infinity, while
the corresponding masses are of the order of 1/√n, as we have exploited this scaling in our
computations. In general, we can understand the effect of non-vanishing flavours and topology
as follows. Both push the eigenvalues further away from the origin, making the effect of the
hard wall less relevant.
In the top plots of figure 6 we have numerically evaluated (86) for k = 1, Nf = 0 and
ν = 0, 1, 2. Hence, it is the level spacing between the two smallest eigenvalues for a differ-
ent number of zero eigenvalues. As mentioned before, we are unable to go much beyond this
setting. Thence, we have generated Monte Carlo simulations with matrix size n = 100 for
larger values of ν. Those are fairly good approximations of the asymptotic result, as the rate
of convergence for the unfolded spacing distribution is 1/n2 at the hard edge, cf [46]. As all
26
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 5. The level spacing distribution (left) and the cumulative density function
(right), respectively, of the largest two eigenvalues of large random matrices generated
via Monte Carlo simulations with n = 50, ν = 0, k = 49, with nconf. = 106 configura-
tions and bin size of about 0.2. Because we compare to the spacing of a specific level
k, here and in the following the number of level spacings is always equal to the num-
ber of configurations. The dashed curves are the bulk spacing distribution (A.1) and its
cumulative density F(x).
unfolded level spacing distributions are very close together, compare the upper left plot in
figure 6, we have studied the differences to the bulk spacing distribution pbulk(s), see (A.1), as
a function of ν. For the histograms from the Monte Carlo simulations one needs to integrate
pbulk(s) over the length of the bins, so that one can take such a difference. Thus, the general pro-
cedure has been as follows: (1) creating the histogram of the level spacing distribution ¯p(ν,0)
1
(s)
of the simulation; (2) unfold it via the formula (44); (3) use the unfolded bins to create a similar
histogram of (A.1); (4) finally take the difference Δ¯p(ν,0)
1
(s) = ¯p(ν,0)
1
(s) −pbulk(s).
One can readily see in figure 6 (bottom plots), that the distance between the level spac-
ing distribution of the two smallest eigenvalues and the one in the bulk first decreases with
increasing ν (left plot). However, at about ν = 15 it again increases as the distribution slowly
approaches the level spacing distribution of the soft edge, which we have added for compar-
ison, see lower right plot in figure 6. The spacing distribution of the two largest eigenval-
ues is also Monte Carlo simulated for the matrix dimension n = 100. However, one needs
to be careful with this result, as the finite size error is quite big at the soft-edge. In [47] it
was found that the optimal rate of convergence is n−2/3. Thus, in the present case the sys-
tematic error is about 20% and, therefore, much larger than the deviations to the bulk level
spacing distribution (A.1) we are comparing with. To have it of the same order one needs
to generate matrices of the size n = 105 which is out of reach for our modest computing
power.
As already discussed in section 1, it is well known [39], that for large ν the Bessel-kernel
converges to the Airy-kernel, as the hard edge of the Marchenko–Pastur law deforms into a
second soft edge. To get a statistical quantification of this effect, we have performed another
Monte Carlo simulation of the random matrix ensemble with ν ∼n for increasing ν, and cal-
culated their spacings, differences to the bulk and empirical densities to observe this effect (see
figure 7). We further quantify this transformation again in terms of the χ2-test comparing the
statistics to the bulk spacing in table 2. In the latter, it becomes apparent, that the deviation
to the bulk spacing increases rapidly for decreasing values of q = n/(n + ν), which shows a
rapid deformation of the hard edge into a soft edge. This has been already seen in figure 1 for
the microscopic level density, when ν = 20.
27
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 6. Top: level spacing distribution (86) (left plot) and its difference to the bulk
spacing distribution (A.1) (right plot) for Nf = 0, k = 1 and ν = 0 (green solid curves),
ν = 1 (red finely dashed curves), and ν = 2 (blue coarsely dashed curves). The black
curve in the left plot is the bulk spacing distribution (A.1) and the one in the right plot
is the difference of the Wigner surmise (1) to the bulk spacing distribution as refer-
ences. Bottom: difference Δ¯p(ν,0)
1
(s) = ¯p(ν,0)
1
(s) −pbulk(s) of the unfolding (44) of the
level spacing distribution p(ν,0)
1
(see (86)), and the bulk spacing distribution pbulk(s)
(see (A.1)) for the two smallest eigenvalues at Nf = 0 and various ν. All histograms
are generated by Monte Carlo simulations with 107 configurations, a matrix dimen-
sion n = 100 and a bin size of roughly 0.15. The values of ν are as follows: Left:
ν = 0 (black solid histogram, solid curve is the analytical result (86)), ν = 5 (roughly
dashed red), ν = 10 (dashed blue), ν = 15 (finely dashed green); Right: ν = 15 (finely
dashed green), ν = 20 (dashed blue), ν = 25 (roughly dashed red). For comparison, the
unfolded level spacing distribution between the largest two eigenvalues Δp(0,0)
49 (s) (solid
black) is added, corresponding to limν→∞Δp(ν,0)
1
(s). We have plotted ν = 15 in both
plots as a reference value for the transition.
If we compare this to spacings at the soft edge for ν = 0 (table 1), we find distances of the
same order from the χ2-test, which shows that for larger ν the hard edge transforms into a soft
edge.
In figure 7 as well as figure 6, it becomes apparent, that when moving from the hard to the
soft edge the peak of the spacing shifts from the right to the left of the maximum of the bulk
spacing distribution. This is expected as a stiffer level spacing, as it is the case for the hard
edge, should have a maximum closer to 1. In contrast, for a softer level spacing, like for the
Airy statistics, the eigenvalueshave more freedom to move,which shows in a maximum further
away from 1. Since this effect is barely noticeable, the value of the χ2-test is additionally given
in figure 7. We omitted to show the difference to the bulk spacing distribution as the number of
generated configurations is smaller here. This is because the matrix size in the second setting
of Monte Carlo simulations has been increased already. This results in a statistical error of one
percent, which strongly overshadows the deviation from the bulk statistics.
28
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 7. The level spacing distributions (left column) and cumulative densities (right
column) of the smallest two eigenvalues (k = 1) generated via Monte Carlo simulations
for N = 200, ν = 4 (top), N = 600, ν = 12 (middle) and N = 1000, ν = 20 (bottom).
The number of configurations is nconf. = 105, as the matrix size is already very big, and
the bin size varies about 0.15–0.2 due to different rescaling from the unfolding for each
parameter set. In the insets we have given the L2 distance to the bulk spacing distribution
(A.1) and also its cumulative density, which are drawn as dashed curves.
