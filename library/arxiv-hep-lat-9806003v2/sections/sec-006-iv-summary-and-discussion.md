---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-006-iv-summary-and-discussion
section_title: "SUMMARY AND DISCUSSION"
section_number: IV
pages: 10-12
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
---
After summarizing our results in Sec. IV A, we discuss our ﬁndings in Sec. IV B.
A. Summary
We presented a detailed analysis of statistical properties of complete eigenvalue spectra for staggered fermions for
SU(2) lattice gauge theory for various couplings and lattice volumes. Unfolding the data posed certain diﬃculties which
are not encountered in other systems. The staircase function found by an average over the ensemble diﬀers in most
cases from the smooth staircase of one speciﬁc conﬁguration. The deviations are as large as ⟨N(λ)⟩−N(λ) = O(101)
for V = 164. Varying the unfolding approach leads to diﬀerent results for large scales. In particular, there is a drastic
diﬀerence between ensemble and conﬁguration unfolding.
Using ensemble unfolding, we ﬁnd a range of validity of RMT, giving λRMT/D = C
√
V . The numerical constant
is approximately given as C ≈0.3. which is compatible with the result obtained in [18] for the microscopic region
where the scaling λRMT/D ∼0.3 . . . 0.7
√
V was found. The same results are obtained if we use windowing, but with
less statistical signiﬁcance.
By unfolding each conﬁguration separately, we do not see any scaling of this type. This procedure obviously removes
the ﬂuctuations of the staircase function relative to the ensemble average seen in Fig. 2. We notice that ﬂuctuations
over the ensemble can already be observed in the integrated level density. But there are still deviations depending on
the unfolding approach used. In particular there is an overshoot for polynomial unfolding at large L. The reasons for
this lies in special features of the average level density, which consists of at least two parts: a smooth polynomial–like
and an oscillatory part. Hence the Thouless energy is due to the ﬂuctuations in the ensemble.
We want to clarify the diﬀerence in the notion of ergodicity used in spectral analysis and in lattice calculations,
respectively. Concerning the analysis of spectra, a system is called ergodic if spectral and ensemble average yield
the same results. It can be proven rigorously that random matrices have this property in the limit of large matrix
dimension. However, here we face a diﬀerent situation. We emphasize that these issues do not aﬀect the notion of
ergodicity as used in connection with lattice simulations. The latter is deﬁned by the requirement that the space of
possible lattice conﬁguration is explored reasonably fast by the simulation algorithm. We emphasize that the time
history of the spectra is not of importance for the calculation of the spectral observable of Sec. III, because it is only
relevant that the conﬁgurations used, see Table I, are representative members of the ensemble, i.e. ergodicity in the
sense of lattice simulations is fulﬁlled. This is ensured by our algorithms as described in Sec. II. Furthermore, this is
supported by the observation that our results do not change if we take arbitrary subsets of conﬁgurations, only the
scattering of the data points increases.
Furthermore we analyzed the nearest neighbor–spacing distribution, skewness and excess for small L. Due to the
large amount of data, our results achieved a quality never reached before. Due to translational invariance in the bulk of
the spectra the general tendency for all of the observables can already be seen for one speciﬁc conﬁguration. Averaging
over all conﬁgurations increases the statistical signiﬁcance of the results. The results for small values L considerably
improve the statistical signiﬁcance of previous analyses [11,12]. To the best of our knowledge, we presented the ﬁrst
statistically highly signiﬁcant analysis of bare two– and, importantly, three–point spectral correlators. Very good
agreement between lattice data and RMT predictions is found. We ﬁnd minor deviations for the three–point cluster
functions. In our opinion, their origin are probably very small point–deviations of the two–point functions.
B. Discussion
Some scenarios for the level statistics are shown in Fig. 16. There the spectral rigidity is plotted. The two solid
lines represent Poisson and RMT behavior, ∆3(L) ∼L and ∆3(L) ∼log L, respectively. The dashed lines represent
10
schematically two diﬀerent cases. Case ‘A’ correspond to a scenario known from systems with few degrees of freedom.
The shortest periodic orbit in phase space sets a scale which forces ∆3(L) to saturate at a certain LA [33]. But by
increasing the degrees of freedom of the system, this scale become ever larger and is hard to be seen. As we may view
lattice gauge theory as a many body problem or disordered system, we do not expect to see this scale in the level
statistics. Therefore one should not be tempted to conclude that the saturation seen in Figs. 9,15 is the analogue of
“saturation of ﬂuctuation measures” which was observed in the energy level statistics for classically chaotic systems
and was interpreted by Berry in terms of shortest periodic orbits [33]. Unlike in the case of quantum billiards where
an analytic expression for the average spectral density exists, the Nave(λ) that we obtained in our analysis was only
a numerical result. Most likely all three approaches, i.e. Gauss, local and modiﬁed polynomial, ﬁt also parts of the
universal ﬂuctuations which shows up as a saturation of the statistics ∆3(L) and Σ2(L).
Another scenario is given by case ‘B’ which lies between Poisson and RMT behavior. It can arise in three diﬀerent
physical situations [1]:
1. Systems in few degrees of freedom between regularity and chaos. The spectral rigidity lies between the Poisson
limit, which applies to regular systems and the RMT limit which applies to chaotic systems, provided the scale
LA is much larger than LB.
2. Disordered systems in d dimensions. The time tc for the classical diﬀusion through the system of size Ld
S where
LS is the size in each dimension determines an energy scale
Ec = ¯h/tc ,
(31)
the Thouless energy. This in turn sets the scale λRMT/D where D is the single particle mean level spacing.
For energy separations in units of D smaller than this scale, RMT ﬂuctuations are seen. For larger energy
separation, deviations as sketched in Fig. 16 occur.
3. Many body systems such as nuclei, molecules or complex atoms. In the language of condensed matter physics,
these systems are zero–dimensional. Consider the Hamiltonian of such a system H = H0 + H1 where H0 has
a certain property and H1 breaks this property. The inﬂuence of H1 on the statistics of the spectrum of H0 is
measured in terms of the spreading width
Γ = 2π⟨H2
1⟩/D0
(32)
where D0 is the mean level spacing of H0 and ⟨H2
1⟩the mean square matrix element of H1. In particular, if H0
has Poisson statistics and H1 RMT statistics the spectral rigidity acquires the form of Fig. 16 and Γ sets the
scale λRMT/D.
As discussed above, situation 1. is not likely to apply. We emphasize that the Thouless energy Ec and the spreading
width Γ deﬁned in 2. and 3. are closely related concepts. Actually, in his original paper, Thouless [13] deﬁned Ec as
a special kind of spreading width. The precise relation between λRMT/D and Ec has been studied in great detail in
the framework of RMT [34]. We notice that the deﬁnition in 2. which is most commonly used in condensed matter
physics, relates Ec to dimensionality, whereas Γ is deﬁned in zero dimensions. Thus, the sheer existence of a scale
λRMT/D can imply, but does not necessarily imply that the deviation from RMT is related to a diﬀusion in a d
dimensional disordered system.
Recent theoretical studies aim at establishing [15–17] a link between disordered systems and QCD. In these works,
a range of validity λRMT of applicability of RMT was considered. Using the Gell-Mann-Oakes-Renner relation, it
should be determined by the pion decay constant Fπ and the chiral condensate Σ,
λRMT ∼
F 2
π
Σ
√
V
.
(33)
In the microscopic region the mean level spacing is D = π/(ΣV ), so that Eq.(33) can be rewritten as
λRMT
D
∼F 2
π
π
√
V .
(34)
The predicted scaling behavior was found very recently in the microscopic region [18]. There a crossover from RMT
to non–universal behavior was found with the scaling Eq.(34). As argued in Ref. [16], a similar relation should also be
seen in the bulk of the spectrum. Here, however, the mean level spacing D is that of the bulk. In the present work, we
have shown that, ﬁrst, the scale λRMT/D exists in the bulk, and, second, that it shows the predicted scaling behavior.
11
The latter observation is a support for the ideas that link QCD to disordered systems and thus to a diﬀusion in a d
dimensions. However, as outlined above, our ﬁndings are necessary but not suﬃcient for this conclusion. They do not
rule out other physical mechanisms that lead to a spreading width or Thouless energy. This underlines the strength of
our analysis: it does not depend in any way on a model for this mechanism. It is a self–consistent statistical method
to ﬁnd the scale λRMT/D.
We hope that the identiﬁcation of this scale λRMT/D can help to improve our understanding of certain features of
QCD as it may allow one to separate the stochastic noise of the short range ﬂuctuations from the true dynamics of
the QCD vacuum. Most desirably, these results could help to design eﬀective models or to simplify the presently used
simulation algorithms in lattice gauge theories.
