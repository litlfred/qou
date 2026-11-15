---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-012-6-comparison-to-data-from-lattice-qcd
section_title: "Comparison to data from lattice QCD"
section_number: 6
pages: 30-32
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
Finally, we would like to compare with edge statistics from data, notably at the hard edge where
we have derived analytical predictions. For that reason we consider empirical data from lattice
QCD Dirac operators.
It is known [17] that strongly interacting quantum field theories in the deepest infrared
limit, the ε-regime, agree with the statistics obtained from random matrix theory. In QCD,
29
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Table 2. The χ2-test for the level spacing of the smallest two eigenvalues for a few
decreasing values of q = n/(n + ν) and increasing matrix dimension. The number of
configurations is varying between nconf. = 105 and nconf. = 106, where for the lowest q
we only went up to n = 200.
q\n
200
600
1000
0.98
0.012 86
0.002 83
0.005 27
0.91
0.035 33
0.0324
0.042 62
0.83
0.010 56
as it appears in the standard model, namely with the gauge group SU(3) in the fundamental
representation and a four dimensional Euclidean space–time, the correspondingrandom matrix
theory is the χGUE. For our purposes this means that the χGUE provides a description for the
statistics of the smallest eigenvaluesand their spacings for the QCD Dirac operator. This carries
over to most lattice discretisations of this theory.
We gathered data from the JLQCD collaboration described in [48]. This data is obtained
from numerical simulations on a Euclidean 163 × 32 space–time lattice at β = 2.30, with a
lattice spacing a ∼0.12 fm, via two different algorithms, namely domain wall and overlap
fermions. From those two algorithms the 50 smallest eigenvalues of the overlap Dirac opera-
tor with a total number of configurations of about nconf. = 1000 were computed for different
values of Fermion masses, where we will focus on the data with Nf = 2, see top part of table 1
in [48].
Although we have derived detailed expressions for the spacing distribution as a function of
the number of flavours Nf and rescaled quark masses μ f (86), we have also seen that the differ-
ence between quenched and unquenched prediction is very small, see figure 4. Furthermore, it
is evident from the seminal paper [9], that even for about 2000 spacings only a rather coarse
comparison to the (bulk) spacing can be made. To further increase the statistics from [48]
which is already exceptionally high for a given set of parameters, we have therefore decided to
average over all given mass configurations resulting in nconf. = 6046. The mass range in units
of lattice spacing of the data [48] is mud = 0.015, 0.025, 0.035, 0.05, 0.07, 0.1,which maps to a
range of about μ f = 1–50. Thus not all of these masses are large enough to apply the quenched
approximation Nf = 0 to the χGUE in (86).
In figure 8, we find a quite large deviation to the quenched spacing distribution (88) at ν = 0
at the hard edge, of up to 8%. The L2-distance given by the χ2-test is given by dχ2 = 0.446 16.
Here, one has to keep in mind, that this is to a certain extend due to the number of configurations
of lattice simulations available—despite averaging over different masses. The statistical error
exceeds by one order of magnitude the difference between the spacing distributions in the bulk,
at the hard and soft edge. Therefore, we can conclude that the level spacing distribution is not
at all a good measure in lattice QCD to discern hard edge from bulk statistics. This is both
because the effect of unquenching is so small and the number of configurations to detect this
is exceedingly high.
Only deviations due to a mobility edge are visible as found in [23, 24, 27, 28]. Here, the
mobility edge denotes the boundarybetween localised states, associated with Poisson statistics,
and delocalised states related to random matrix statistics. In QCD it is reached by increasing
the temperature towards the chiral phase transition, as studied in [23, 24, 27, 28]. Close to the
mobility edge, the global symmetries of the states are a mixture with Poisson statistics, which
30
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 8. Left: the level spacing distribution of the smallest two eigenvalues of the
overlap Dirac operator k = 1 (blue histogram) with Nf = 2 and ν = 0 averaged over
six different degenerate masses, with a total number of configurations of nconf. = 6046.
It compared to the spacing distribution between the two smallest eigenvalues of the
χGUE in the large-n limit for Nf = 0 quenched with ν = 0 (dashed curve). Right: the
cumulative densities of the two distributions, respectively.
diminishes the level repulsion drastically and yields deviations from the bulk level spacing
above the percent threshold, that can be easily discerned by the bare eye.
