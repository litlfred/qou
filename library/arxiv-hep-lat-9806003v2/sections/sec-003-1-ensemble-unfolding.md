---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-003-1-ensemble-unfolding
section_title: "Ensemble unfolding"
section_number: 1
pages: 3-5
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
---
1. Ensemble unfolding
In RMT one deals with an ensemble of matrices, where the matrix elements of each member are chosen randomly.
Spectral observables predicted by RMT are calculated as an average over the ensemble. This ensemble average is
denoted by a bar (. . .). But observables can also be calculated as spectral average, i.e. one performs a running
average over overlapping intervals [α, α + L] of length L in the spectrum of one member. In order to distinguish it
from ensemble average, we denote spectral averaging by angular brackets ⟨. . .⟩. In the limit of large matrix dimension
both averages are equivalent [1]. This property is called ergodicity.
In most experiments, one measures one - preferably long - spectrum. Thus observables are usually calculated from
spectral average. One uses the theoretical concept of ergodicity to compare the RMT predictions with the experimental
results. In our case, however, the data consists of conﬁgurations, i.e. forms an ensemble. Hence, questions related
to ergodicity arise not only for the calculation of observables, but also in the determination of the staircase function,
i.e. in the unfolding procedure. We have in principle two very diﬀerent ways of unfolding our data: ﬁrst, ensemble
unfolding, Nave(λ) = N(λ), i.e. we determine the smooth part of the staircase function by averaging over the ensemble,
and second, conﬁguration unfolding, Nave(λ) = ⟨N(λ)⟩, i.e. we determine the smooth part of the staircase function for
every conﬁguration separately. The results diﬀer considerably, N(λ)̸ = ⟨N(λ)⟩, for most of the conﬁgurations. The
ensemble averaged staircase N(λ) for the lattice QCD Dirac operator is shown in Fig. 1. We ﬁnd N(λ) by dividing
the energy range in m bins with width ∆λ and average the density ρ(λ, λ + ∆λ) for each bin over all conﬁgurations.
We then calculate the staircase function as N(λ) = Pm
i=1 ρ(λi, λi + ∆λ)∆λ, with λm = λ. In Fig. 2, the diﬀerence
between the ensemble averaged staircase function and the conﬁguration wise averaged ones, for V = 164 and β = 2.4,
for 50 arbitrarily chosen conﬁgurations is plotted. Each data point represents the diﬀerence N(λi,j)−⟨N(λi,j)⟩, where
i enumerates the eigenvalues, i = 1, . . . , 32768 and j is the conﬁguration number j = 1, . . . , 50. We plot only every
500th eigenvalue. There are deviations of about N(λ) −⟨N(λ)⟩= O(101) in certain energy ranges.
3
If the spectra are unfolded using the ensemble averaged staircase function N(λ), observables should then also be
calculated as an ensemble average for a ﬁxed value of λ. But we checked that our results do not depend on λ in a wide
range of the bulk. This property is called translational invariance. It is actually not present in the microscopic region,
where it is destroyed by point wise symmetry between positive and negative eigenvalues [18]. Translational invariance
in the bulk allows us to calculate observables from running average over overlapping intervals for each conﬁguration.
We choose an overlap of 90% for two consecutive intervals. Then we average over all conﬁgurations. This improves
the statistics of the result considerably.
2. Conﬁguration unfolding
We now unfold each conﬁguration separately. Observables are then calculated for each conﬁguration by running
spectral average. Thereafter we average over the ensemble. The basic characteristics are already obtained for one
single conﬁguration, though the statistics is considerably improved by ensemble averaging. This is in the same spirit
as it was done in spectra of nuclei [24] and complex atoms [25]. These spectra were unfolded for each nuclei or atom
separately. Then observables were calculated as described above, i.e. ﬁrst taking the spectral and then the ensemble
average. In this case the ensembles consist of nuclei or atoms of diﬀerent types.
Conﬁguration unfolding is, in contrast to ensemble unfolding, not a unique procedure. One has to ﬁnd either ﬁts
to the average staircase function or to smooth it in some way. A priori, there is no criterion whether the numerical
estimated Nave(λ) is close to the real one or not. Thus, we use three diﬀerent approaches and carefully compare them
with one another to eliminate as many sources for mistakes as possible and to obtain consistent results.
First, we ﬁt N(λ) to a polynomial of degree n,
⟨N(λ)⟩= Npoly(λ) =
n
X
j=0
aj λj ,
(7)
where n is a small integer, n = 2, . . . , 5. This approach is motivated by the fact that almost all physical systems
are known to have a level density which is as smooth as a polynomial.
In our case this ansatz is supported by
pertubative calculations. Strong coupling expansions for SU(2) with staggered fermions have been performed [26]
and, furthermore, 1/Nc expansion of the QCD level density [27], both suggesting a smooth level density. The former
gives a semi–circle whereas the latter explicitly predicts a polynomial increase.
Second, we use the Gaussian method which was originally developed by Strutinsky [28]. One replaces the δ–functions
in Eq. (3) by Gaussian functions with a width ∆which yields a smoothed staircase
N∆(λ) =
Z λ
−∞
dλ′
max
X
i=min
1
√π∆e−
1
∆2 (λ′−λi)2.
(8)
The summation runs from the smallest eigenvalue λmin to the largest eigenvalue λmax in the interval under consid-
eration. The limit ∆→0 restores δ–distributed eigenvalues, whereas the ﬂuctuations are smeared out for ﬁnite ∆.
The optimal parameter ∆opt is found by a χ2–ﬁt of N∆(λ) to N(λ). Then we identify
⟨N(λ)⟩= N∆opt(λ) .
(9)
Third, we perform a local unfolding by calculating the unfolded eigenvalues ξi directly with the formula
ξi+1 −ξi = λi+1 −λi
Di
,
(10)
with local mean level spacing
Di =
1
2k + 1
i+k
X
j=i−k
(λj+1 −λj) .
(11)
Here 2k is the number of consecutive level spacings over the running average is performed.
Whatever approach one decides to use, a necessary condition is that on the unfolded scale the average number of
levels in an interval of length L should equal this length. This is a very important requirement because we are also
interested in very large energy scales. This assures that the spectrum on the numerically constructed dimensionless
4
scale ξ has mean level density unity. Consider the interval [α, α + L] which contains nα(L) eigenvalues. Spectral
average ⟨. . .⟩and ensemble average (. . .) have to yield
⟨nα(L)⟩= L .
(12)
In Fig. 3, the diﬀerence between the calculated mean number of eigenvalues ⟨nα(L)⟩and L is plotted as a function
of L. For the Gaussian method the diﬀerence appears to be zero to all scales. While it is small and does only appear
at large L for polynomials ﬁts with n ≥3, strong deviations from the zero line already appear at small L for n = 2.
In the case of local unfolding, the diﬀerence L −⟨nα(L)⟩is positive for small k, i.e. there are on average less levels in
a given interval than there should be. For growing k, it becomes negative with ever stronger deviations from the ﬂat
line. The averaging interval length k for which the diﬀerence equals zero is k ≈100 for V = 164. For other lattice
sizes this averaging interval is slightly smaller. We take this as the optimal parameter for this approach. From Fig. 3
we learn, that the necessary condition (12) is fulﬁlled only for the Gaussian approach, polynomial ﬁt with n ≥3 and
local unfolding with k ≈100 for V = 164, all other choices of the parameters must be rejected.
It should be mentioned that a new artiﬁcial scale both for local and Gaussian approach is introduced, namely the
averaging interval length k and the width ∆, respectively. Therefore, one should be cautious in the interpretation of
eﬀects seen on scales L larger than current value of the corresponding parameter. In units of the mean level spacing
D we ﬁnd a width of the Gaussian as ∆/D ≈100 at a 164 lattice. On the other hand, both approaches have the
advantage that no particular function for the average level density has to be assumed.
We checked all our numerical unfolding approaches with the spectrum of a very diﬀerent system. We used the
spectrum of quantum chaotic billiard that was simulated in a microwave experiment. In billiards, the Weyl formula
gives an analytically expression for the mean level density [29]. With our phenomenological approaches, we indeed
obtained quantitatively the same results.
