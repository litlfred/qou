---
doc_id: arxiv-2202.01613v1
doc_title: "The neutron-proton mass diﬀerence"
section_id: sec-004-4-details-of-simulation-and-analysis
section_title: "Details of simulation and analysis"
section_number: 4
pages: 7-8
source_pdf: 2202.01613v1.pdf
source_sha256: b8768b78fe84c86a
toc_source: outline
doc_brief: "The neutron-proton mass difference — 9 sections: Front matter; QCD+QED at LO; Introduction"
---
Details of simulation and analysis
Our correlators are evaluated over the 𝑁𝑓= 2 + 1 + 1 ETMC gauge conﬁgurations [7] with
twisted mass quarks at maximal twist. We adopt a unitary setup in the light sector, and a mixed action
approach for the strange and charm quarks which in the valence are regularized as Osterwalder-
Seyler fermions [18]. In tab. (1) are reported the ensembles details. The statistical uncertainty on
our observables was propagated using the jackknife re-sampling technique with 15 jackknifes for
each ensemble. Gaussian smearing was applied to quark ﬁelds according to [4], with the parameter
𝛼𝑔optimized as in [19]. Some numerical testing lead us to the choice of 𝑛𝑔= 50 steps on the
source of our correlators, as an appropriate middle ground for a soon plateau and moderate noise
in the signal. In order to reduce the noise in our correlator, we used 16 stochastic sources [20] for
the numerical inversion of the Dirac operator, compatibly with our computational resources.
7
𝑀𝑛−𝑀𝑝in Lattice QCD+QED at LO in IB
Simone Romiti
The isosymmetric limit of hadronic masses 𝑀𝐻are found from the large time behavior of
®𝑝= ®0 correlators with 𝑀(0)
𝐻as the ground state. These values are found from a ﬁt to a constant of
the eﬀective mass curves [17] in their plateau intervals 1, and we do the same also for the eﬀective
slopes curves (see sec. (2)).
Our lattice ensembles are not at the physical point, requiring to extrapolate among the en-
sembles. This is done in an hadronic scheme, in terms of the ratios deﬁned in eq. (15). 𝑀Ω−,
(𝑀2
𝜋+ + 𝑀2
𝜋+), 𝑀2
𝐾+ and 𝑀2
𝐾0 are used to tune the parameters 𝑎, 𝑎𝑚𝑢, 𝑎𝑚𝑑and 𝑎𝑚𝑠, with the
counterterms 𝑎Δ𝑚𝑓deﬁned at the isoQCD physical point (see sec. (3)). The lattice spacings
𝑎𝛽(𝑖) = 0.1011(10), 0.09029(77), 0.06834(63) fm at 𝛽= 1.90, 1.95, 2.10 respectively, are found
from the extrapolation of 𝑎𝑀Ω−among the ensembles, whose values are ﬁtted with the following
polynomial ansatz:
(𝑎𝑀Ω−)𝑖(𝐿, 𝑟ℓ) = 𝑎𝛽(𝑖) 𝑀(𝑒𝑥𝑝)
Ω−
h
1 + 𝑐𝐿
𝛼𝐸𝑀
𝐿3
+ 𝑐ℓΔ𝑟ℓ+ 𝑐(2)
ℓ
Δ𝑟2
ℓ
i
.
(21)
Δ𝑟ℓ= 𝑟ℓ−𝑟𝑒𝑥𝑝
ℓ
and 𝑐𝐿, 𝑐ℓ, 𝑐(2)
ℓ
and the 𝑎𝛽(𝑖) (𝑖= 1, 2, 3) are free parameters of the ﬁt. The
numerically leading FVE is taken into account with the ∼1/𝐿3 term, coming from the residual
QED FVEs in 𝑎Δ𝑚𝑠and Δ𝑀EMC
Ω−
.
Each observable is extrapolated among 2 values of 𝑎𝑚𝑠and the 𝑎𝑚ℓof tab. (1) to the isoQCD
physical point in terms of the ratios 𝑟𝑠and 𝑟ℓof eq. (15). FVEs are ﬁtted using asymptotic formulas
from ChPT (isoQCD FVEs) [22–24] and QED at ﬁnite volume [3, 13–15], while discretization
eﬀects are included with 𝑂(𝑎2) terms in virtue of the 𝑂(𝑎) improvement provided by maximal
twist.
