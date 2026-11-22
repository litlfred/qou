---
doc_id: lattice2021-543
doc_title: "The neutron-proton mass diﬀerence"
section_id: sec-004-details-of-simulation-and-analysis
section_title: "Details of simulation and analysis"
section_number: null
pages: 7-8
source_pdf: LATTICE2021_543.pdf
source_sha256: 3a255daa50ebd5a4
toc_source: outline
doc_brief: "The neutron-proton mass difference — 9 sections: Front matter; QCD+QED at LO; Introduction"
---
Details of simulation and analysis
Our correlators are evaluated over the 푁푓= 2 + 1 + 1 ETMC gauge conﬁgurations [7] with
twisted mass quarks at maximal twist. We adopt a unitary setup in the light sector, and a mixed action
approach for the strange and charm quarks which in the valence are regularized as Osterwalder-
Seyler fermions [18]. In tab. (1) are reported the ensembles details. The statistical uncertainty on
our observables was propagated using the jackknife re-sampling technique with 15 jackknifes for
each ensemble. Gaussian smearing was applied to quark ﬁelds according to [4], with the parameter
훼푔optimized as in [19]. Some numerical testing lead us to the choice of 푛푔= 50 steps on the
source of our correlators, as an appropriate middle ground for a soon plateau and moderate noise
in the signal. In order to reduce the noise in our correlator, we used 16 stochastic sources [20] for
the numerical inversion of the Dirac operator, compatibly with our computational resources.
7
PoS(LATTICE2021)543
푀푛−푀푝in Lattice QCD+QED at LO in IB
Simone Romiti
The isosymmetric limit of hadronic masses 푀퐻are found from the large time behavior of
®푝= ®0 correlators with 푀(0)
퐻as the ground state. These values are found from a ﬁt to a constant of
the eﬀective mass curves [17] in their plateau intervals 1, and we do the same also for the eﬀective
slopes curves (see sec. (2)).
Our lattice ensembles are not at the physical point, requiring to extrapolate among the en-
sembles. This is done in an hadronic scheme, in terms of the ratios deﬁned in eq. (15). 푀Ω−,
(푀2
휋+ + 푀2
휋+), 푀2
퐾+ and 푀2
퐾0 are used to tune the parameters 푎, 푎푚푢, 푎푚푑and 푎푚푠, with the
counterterms 푎Δ푚푓deﬁned at the isoQCD physical point (see sec. (3)). The lattice spacings
푎훽(푖) = 0.1011(10), 0.09029(77), 0.06834(63) fm at 훽= 1.90, 1.95, 2.10 respectively, are found
from the extrapolation of 푎푀Ω−among the ensembles, whose values are ﬁtted with the following
polynomial ansatz:
(푎푀Ω−)푖(퐿, 푟ℓ) = 푎훽(푖) 푀(exp)
Ω−
h
1 + 푐퐿
훼EM
퐿3 + 푐ℓΔ푟ℓ+ 푐(2)
ℓ
Δ푟2
ℓ
i
.
(21)
Δ푟ℓ= 푟ℓ−푟(exp)
ℓ
and 푐퐿, 푐ℓ, 푐(2)
ℓ
and the 푎훽(푖) (푖= 1, 2, 3) are free parameters of the ﬁt. The
numerically leading FVE is taken into account with the ∼1/퐿3 term, coming from the residual
QED FVEs in 푎Δ푚푠and Δ푀EMC
Ω−
.
Each observable is extrapolated among 2 values of 푎푚푠and the 푎푚ℓof tab. (1) to the isoQCD
physical point in terms of the ratios 푟푠and 푟ℓof eq. (15). FVEs are ﬁtted using asymptotic formulas
from ChPT (isoQCD FVEs) [22–24] and QED at ﬁnite volume [3, 13–15], while discretization
eﬀects are included with 푂(푎2) terms in virtue of the 푂(푎) improvement provided by maximal
twist.
