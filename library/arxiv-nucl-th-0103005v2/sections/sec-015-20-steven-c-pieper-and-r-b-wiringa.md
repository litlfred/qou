---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-015-20-steven-c-pieper-and-r-b-wiringa
section_title: "Steven C. Pieper and R. B. Wiringa"
section_number: 20
pages: 20-20
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
in Ref. (18). The most crucial aspect in choosing Ψ T is that it have the correct
mix of spatial symmetries, i.e., the βLS[n] admixtures. This is because the limited
propagation time is not suﬃcient for the GFMC algorithm to ﬁl ter out low-lying
excitations with the same quantum numbers. This issue is uni mportant in 4He,
where the ﬁrst 0 + excited state is near 20 MeV, but in 6Li, the ﬁrst 1 + excited
state is at only 5.65 MeV; other p-shell nuclei have similar low-lying excitations.
Otherwise, the GFMC algorithm is able to rapidly correct for some very poor Ψ T
whose variational energies are actually positive. However , a good Ψ T helps to
keep the error bars small at larger τ . The most eﬃcient balance between speed
of construction of Ψ T and smallest number of samples needed to achieve a given
error bar seems to be given by Eq.(30). A number of other tests of the GFMC
algorithm and its ability to determine nuclear radii are des cribed in Refs. (18, 19).
The calculations described here are computationally inten se, and would not have
been possible without the advent of parallel supercomputer s. The initial stud-
ies (17) of 6Li required ∼ 2, 000 node hours on an IBM SP1 to propagate 10,000
conﬁgurations to τ = 0.06 MeV −1. Today, with improvements in the algorithm
and after much eﬀort to optimize the computer codes, the same c alculation requires
about 15 node hours on a third generation IBM SP. However, a pr esent calculation
for 8Li, requiring 10,000 conﬁgurations to get a reasonable erro r bar, takes 1,000
node hours, so forefront computer resources remain essenti al for this program.
