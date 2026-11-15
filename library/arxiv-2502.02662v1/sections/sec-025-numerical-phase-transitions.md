---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-025-numerical-phase-transitions
section_title: "Numerical Phase Transitions"
section_number: null
pages: 30-34
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
toc_source: outline
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
Numerical Phase Transitions
At present, computing double Hurwitz numbers remains largely outside the scope of analytical
methods.
Numerically, disconnected double Hurwitz numbers can be computed for small
values of the degree using the definition of Hurwitz numbers in terms of conjugacy classes.
However, computing the free energy (C.13) of the deformed extended Hurwitz theory remains
hard. In the case of Yang-Mills, one expects that the qualitative behavior of the phase diagram
of the theory is also encoded in the behavior of its one-point functions [33]. Therefore, we
shall compute certain one-point functions of the deformed extended Hurwitz theory. We will
then attempt to draw lessons concerning the phase diagram of the free energy of the chiral
Yang-Mills theory. The one-point function of the chiral Yang-Mills theory on the sphere, or
equivalently the free energy on the disk, reads
F0( ˆA¯r; q, t, u) =
X
d
qd X
α⊢d
(−1)ℓ(ρ)+ℓ(α)
(ℓ(ρ) + ℓ(α) −2)!tℓ(ρ)+ℓ(α)−2u|α|H◦
0,d(Cρ, Cα, Cℓ(ρ)+ℓ(α)−2
2
) . (C.14)
The operator ˆA¯r may be thought of as a complicated insertion in the chiral Yang-Mills theory.
Note that by trading the sphere for a disk, we have traded an infinite sum over all conjugacy
classes for a single class insertion. Nevertheless, the above expression cannot easily be com-
puted in all generality, since it still features a sum over double Hurwitz numbers. We thus
restrict our attention to the insertion of the renormalized identity and transposition classes.
We write
F0( ˆA∅; q, t, u) =
X
d
qd X
α⊢d
(−1)ℓ(α)+d
(ℓ(α) + d −2)!tℓ(α)+d−2u|α|H◦
0,d(Cα, Cℓ(α)+d−2
2
)
(C.15)
F0( ˆA2; q, t, u) = −
X
d
qd X
α⊢d
(−1)ℓ(α)+d
(ℓ(α) + d −3)!tℓ(α)+d−3u|α|H◦
0,d(Cα, Cℓ(α)+d−2
2
) .
(C.16)
Only connected, single Hurwitz numbers at genus 0 appear in these expressions and they
admit the following exact expression [35,36]:
H◦
0,d(Cα, Cd+ℓ(α)−2
2
) = (d + ℓ(α) −2)!
|Aut(α)|
ℓ(α)
Y
i=1
ααi
i
αi! dℓ(α)−3.
(C.17)
Furthermore, given that we are interested in the case where u̸ = 0, we may exploit the
symmetry (C.3) to reduce the number of parameters that each one-point function depends
on. We write
F0( ˆA∅; q, t, u) = u−2 X
d
(qu2)d X
α⊢d
(−1)ℓ(α)+d(t/u)ℓ(α)+d−2 ·
1
|Aut(α)|
ℓ(α)
Y
i=1
ααi
i
αi! dℓ(α)−3.
(C.18)
F0( ˆA2; q, t, u) = −u−3 X
d
(qu2)d X
α⊢d
(−1)ℓ(α)+d(t/u)ℓ(α)+d−3 · d + ℓ(α) −2
|Aut(α)|
ℓ(α)
Y
i=1
ααi
i
αi! dℓ(α)−3 .
(C.19)
The overall factors of u are irrelevant to the study of the radius of convergence of the partition
functions since u̸ = 0. Therefore, we focus on the sums and define the new parameters q′ = qu2
and t′ = t/u. The partition functions start to oscillate with increasing magnitude when q′
and t′ become large enough, indicating that the one-point function becomes divergent in this
region. We plot here the regions in coordinate space for which the partition functions seem
to converge.
Figure 1: The domains of convergence of the renormalized identity one-point function (on the
left) and of the renormalized transposition one-point function (on the right).
The line in parameter space corresponding to chiral Yang-Mills theory is (q′ = e−t′/2, t′).
We plot the correlation function of the renormalized identity class as a function of the area t
of the target space sphere on the Yang-Mills line of parameter space.
Figure 2: The one-point function for a renormalized identity class insertion as a function of t.
The partition function appears to converge for small and large values of the area, and
exhibits rapid, high amplitude oscillations in an intermediate range, indicating a divergence.
This strongly suggests that the chiral Yang-Mills theory exhibits three phases, in accordance
with [12]. The phase transitions occur around t ∼0.8 and t ∼10, respectively.20 Figure 1
therefore constitutes a qualitative phase diagram for the generalization of the chiral Yang-Mills
theory that we have defined.
References
[1] G. ’t Hooft, “A Planar Diagram Theory for Strong Interactions,” Nucl. Phys. B 72 (1974),
461 doi:10.1016/0550-3213(74)90154-0.
[2] D. J. Gross, “Two-dimensional QCD as a string theory,” Nucl. Phys. B 400 (1993),
161-180 doi:10.1016/0550-3213(93)90402-B [arXiv:hep-th/9212149 [hep-th]].
[3] D. J. Gross and W. Taylor, “Two-dimensional QCD is a string theory,” Nucl. Phys. B
400 (1993), 181-208 doi:10.1016/0550-3213(93)90403-C [arXiv:hep-th/9301068 [hep-th]].
[4] D. J. Gross and W. Taylor, “Twists and Wilson loops in the string theory of two-
dimensional QCD,” Nucl. Phys. B 403 (1993), 395-452 doi:10.1016/0550-3213(93)90042-
N [arXiv:hep-th/9303046 [hep-th]].
[5] S. Cordes, G. W. Moore and S. Ramgoolam, “Lectures on 2-d Yang-Mills theory, equiv-
ariant cohomology and topological field theories,” Nucl. Phys. B Proc. Suppl. 41 (1995),
184-244 doi:10.1016/0920-5632(95)00434-B [arXiv:hep-th/9411210 [hep-th]].
[6] P. Horava, “Topological strings and QCD in two-dimensions,” [arXiv:hep-th/9311156
[hep-th]].
[7] S. Cordes,
G. W. Moore and S. Ramgoolam,
“Large N 2-D Yang-Mills the-
ory and topological string theory,” Commun. Math. Phys. 185 (1997), 543-619
doi:10.1007/s002200050102 [arXiv:hep-th/9402107 [hep-th]].
20Playing with the degree to which the computation is carried out suggests that these are rough values,
and only the qualitative behavior of the one-point functions should be trusted.
[8] O. Aharony, S. Kundu and T. Sheaffer, “A String Theory for Two Dimensional Yang-Mills
Theory I,” [arXiv:2312.12266 [hep-th]].
[9] A. Okounkov and R. Pandharipande, “Gromov-Witten theory, Hurwitz theory, and
completed cycles,” Ann. Math. 163 (2006), 517-560 doi:10.4007/annals.2006.163.517
[arXiv:math/0204305 [math]].
[10] L. Benizri and J. Troost, “Symmetric Group Gauge Theories and Simple Gauge/String
Dualities,” [arXiv:2404.12543 [hep-th]].
[11] M. R. Douglas and V. A. Kazakov, “Large N phase transition in continuum QCD in
two-dimensions,” Phys. Lett. B 319 (1993), 219-230 doi:10.1016/0370-2693(93)90806-S
[arXiv:hep-th/9305047 [hep-th]].
[12] W. Taylor, “Counting strings and phase transitions in 2-D QCD,” [arXiv:hep-th/9404175
[hep-th]].
[13] M. J. Crescimanno and W. Taylor, “Large N phases of chiral QCD in two-dimensions,”
Nucl. Phys. B 437 (1995), 3-24 doi:10.1016/0550-3213(94)00561-R [arXiv:hep-th/9408115
[hep-th]].
[14] R. Dijkgraaf and E. Witten, “Topological Gauge Theories and Group Cohomology,”
Commun. Math. Phys. 129 (1990), 393 doi:10.1007/BF02096988.
[15] V. Ivanov, S. Kerov, “The algebra of conjugacy classes in symmetric groups and partial
permutations,” Journal of Mathematical Sciences, 107 (5), 4212-4230 (2001).
[16] O. Aharony and E. Y. Urbach, “Type II string theory on AdS3×S3×T4 and symmet-
ric orbifolds,” Phys. Rev. D 110 (2024) no.4, 046028 doi:10.1103/PhysRevD.110.046028
[arXiv:2406.14605 [hep-th]].
[17] E. Witten, “On the Structure of the Topological Phase of Two-dimensional Gravity,”
Nucl. Phys. B 340 (1990), 281 doi:10.1016/0550-3213(90)90449-N
[18] R. Dijkgraaf, H. L. Verlinde and E. P. Verlinde, “Notes on topological string theory and
2-D quantum gravity,” PUPT-1217.
[19] K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil and
E. Zaslow, “Mirror symmetry,” American Mathematical Society, 2003, Clay Mathematics
Monographs Volume 1.
[20] A. Pakman, L. Rastelli and S. S. Razamat, “Diagrams for Symmetric Product Orbifolds,”
JHEP 10 (2009), 034 doi:10.1088/1126-6708/2009/10/034 [arXiv:0905.3448 [hep-th]].
[21] A. Okounkov and R. Pandharipande, “The Equivariant Gromov-Witten theory of P**1,”
[arXiv:math/0207233 [math.AG]].
[22] J.
Novak,
“On
the
2D
Yang-Mills/Hurwitz
Correspondence,”
[arXiv:2401.00628
[math.CO]].
[23] E. Witten, “On quantum gauge theories in two-dimensions,” Commun. Math. Phys. 141
(1991), 153-209 doi:10.1007/BF02100009
[24] I. Runkel and L. Szegedy, “Area-Dependent Quantum Field Theory,” Commun.
Math. Phys. 381 (2021) no.1, 83-117 doi:10.1007/s00220-020-03902-1 [arXiv:1807.08196
[math.QA]].
[25] M. Blau and G. Thompson, “Quantum Yang-Mills theory on arbitrary surfaces,” Int. J.
Mod. Phys. A 7 (1992), 3781-3806 doi:10.1142/S0217751X9200168X.
[26] R. Cavalieri and E. Miles, “Riemann Surfaces and Algebraic Curves,” A First Course in
Hurwitz Theory, Cambridge University Press, 2016.
[27] W.
Lerche,
“Gromov-Witten/Hilbert
versus
AdS3/CFT2
Correspondence,”
[arXiv:2310.15237 [hep-th]].
[28] S. Li and J. Troost, “The Topological Symmetric Orbifold,” JHEP 10 (2020), 201
doi:10.1007/JHEP10(2020)201 [arXiv:2006.09346 [hep-th]].
[29] R. Dijkgraaf, E. P. Verlinde and H. L. Verlinde, “Matrix string theory,” Nucl. Phys. B
500 (1997), 43-61 doi:10.1016/S0550-3213(97)00326-X [arXiv:hep-th/9703030 [hep-th]].
[30] L. Eberhardt, “A perturbative CFT dual for pure NS–NS AdS3 strings,” J. Phys. A 55
(2022) no.6, 064001 doi:10.1088/1751-8121/ac47b2 [arXiv:2110.07535 [hep-th]].
[31] J. Kim and M. Porrati, “On the central charge of spacetime current algebras and cor-
relators in string theory on AdS3,” JHEP 05 (2015), 076 doi:10.1007/JHEP05(2015)076
[arXiv:1503.07186 [hep-th]].
[32] L. Eberhardt, “Partition functions of the tensionless string,” JHEP 03 (2021), 176
doi:10.1007/JHEP03(2021)176 [arXiv:2008.07533 [hep-th]].
[33] D. J. Gross and A. Matytsin, “Instanton induced large N phase transitions in
two-dimensional and four-dimensional QCD,” Nucl. Phys. B 429 (1994),
50-74
doi:10.1016/S0550-3213(94)80041-3 [arXiv:hep-th/9404004 [hep-th]].
[34] A. Okounkov, “Toda equations for Hurwitz numbers,” Math. Res. Lett. 7 (2000) no.4,
447-453 doi:10.4310/MRL.2000.v7.n4.a10 [arXiv:math/0004128 [math]].
[35] A. Hurwitz, “Ueber Riemann’sche Fl¨achen mit gegebenen Verzweigungspunkten”, Math.
Ann. 39 (1891), no. 1, 1.
[36] S. K. Lando, “Hurwitz numbers: on the edge between combinatorics and geometry”,
Proceedings of the International Congress of Mathematicians 2010 (ICM 2010), June
2011, 2444-2470.
