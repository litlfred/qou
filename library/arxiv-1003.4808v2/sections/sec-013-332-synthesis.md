---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-013-332-synthesis
section_title: "Synthesis"
section_number: 3.3.2
pages: 27-32
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
It is fairly clear from the above discussion of quantization that there should be a relation
between the partition function for Chern-Simons theory with compact gauge group G
and the partition function for Chern-Simons theory with complex gauge group GC.
Essentially the same equations (3.40) and (3.45) deﬁne the two partition functions —
though in one case they are diﬀerence equations and in the other they are diﬀerential
equations. This relation was developed in [10, 11], and was recently explained very
concretely in [24] in terms of analytic continuation.
Algebraically, there may be several solutions to the diﬀerence equations (3.40) of
the compact theory. Let us label them as Zα
G(M;u). The exact partition function of
the compact theory ( i.e. the colored Jones polynomial for G = SU (2)) is given as a
linear combination
ZG(M;u; ℏ) =
∑
α
nαZα
G(M;u; ℏ). (3.47)
The ℏ → 0 asymptotics of each component in this sum are then governed by the
corresponding solution Zα
pert(M;u) to the diﬀerential equation (3.45), written in the
26
form (3.43). These are holomorphic pieces of the GC partition function. The physi-
cal statement of the volume conjecture for SU (2) is that the component of the sum
(3.47) with the dominant leading asymptotics corresponds to the SL(2, C) partition
function Zα=hyp
pert (M;u) around the hyperbolic SL(2, C) ﬂat connection. Of all the ﬂat
SL(2, C) connections, this has the largest volume in a neigborhood of the complete
hyperbolic point u =iπ. Therefore, if the solution Zhyp
G (M;u) of the diﬀerence equa-
tions contributes to the colored Jones polynomial in (3.47), it will have the dominant
asymptotic. One must simply assure that
Physical volume conjecture : nhyp⁄= 0. (3.48)
For higher-rank groups, it is again clear that the overall asymptotics of ZG(M;u)
will be controlled by the ﬂat GC connection with the largest volume that makes a
corresponding contribution to (3.47). One may expect by comparison to SU (2) theory
that the connection with the largest overall volume (the analog of the hyperbolic ﬂat
connection) in fact contributes and dominates. This has yet to be explored.
The expansions (3.47) and (3.42) for compact and complex Chern-Simons theory,
and the relation between them, were explained in [24] using analytic continuation of
the Chern-Simons path integral. The path integral provides yet another method for
quantizing a topological quantum ﬁeld theory, with its own inherent advantages. Let
us ﬁnish by saying a few words about this.
The path integral for compact Chern-Simons theory takes the form
ZG(M;u; ℏ) =
∫
DA(u) exp
(ik
4πICS(A)
)
(3.49)
=
∫
DA(u) exp
(
− 1
4ℏICS(A)
)
,
whereICS(A) =
∫
M Tr
(
AdA + 2
3A3)
is the Chern-Simons action as in (1.9) and k∈ Z.
The integral is over all G-connections on M =~M\K, modulo gauge equivalence, with
ﬁxed holonomy eigenvalues eu at the meridian of K. (In order to obtain a nonzero
answer,u/ℏ∼λ∗+ρ∗ must be integral.) For g-values connectionsA, the actionICS(A)
is real. Therefore, for k∈ Z, the integral (3.49) is oscillatory and can be calculated by
appropriately regulating the oscillations asA→∞ . In [24], however, the problem was
posed of analytically continuing to k∈ C. Roughly speaking, to accomplish this one
must also complexify the gauge connection A so that it is gC-valued. When k∈ R,
the integral (3.49) is then interpreted as a holomorphic contour integral along the real
subspace in the space of complex connections. As k is pushed away from the real
line, this integration contour must also move. In general, the appropriate integration
contour for k∈ C is a sum of contours going through the various saddle points of
the complexiﬁed action ICS(A). Each saddle point is a ﬂat GC connection, and an
expression of the form (3.47) results.
27
For complex Chern-Simons theory, the procedure is quite similar. The path integral
is
ZGC(M;u; ℏ, ˜ℏ) =
∫
DA(u)DA(¯u) exp
(iτ
8πICS(A) + i˜τ
8πICS(A)
)
(3.50)
=
∫
DA(u)DA(¯u) exp
(
− 1
4ℏICS(A)− 1
4˜ℏ
ICS(A)
)
,
for a gC-valuedGC-connectionA. The integrand is initially well-deﬁned whenτ +˜τ∈ Z,
and leads to a convergent oscillatory integral when the exponent is imaginary — i.e.
for ˜τ = ¯τ. In order to analytically continue to independent τ, ˜τ∈ C, one must treat
A andA as independent connections and again complexify each of them. One then
deforms the contour of integration away from the “real” subspace when ˜ τ ⁄= ¯τ, and
writes the resulting contour as a sum over pairs of saddle points for A andA. Since
(gC)C≃ gC× gC, however, these are just pairs of saddle points of ﬂat GC-connections.
An expression of the form (3.42) results:
ZGC(M;u; ℏ, ˜ℏ) =
∑
α,¯α
nα,¯αZα
GC(M;u; ℏ)Zα
GC(M; ¯u; ˜ℏ). (3.51)
The functions Zα
GC(M;u; ℏ) and Zα
G(M;u; ℏ) here and in (3.47) should be identical,
since they both correspond to GC connections.
In [24], it is explained how the coeﬃcients nα and nα,¯α may be calculated for
speciﬁc examples, like the trefoil and ﬁgure-eight knot complements. As expected, the
coeﬃcient of the hyperbolic component “ α = hyp” of the SU (2) partition function is
nonzero, leading to another demonstration of the volume conjecture.
The careful reader may still be wondering why it is only the growth of the colored
Jones polynomial at nonrational N/k that shows exponential behavior. The answer
comes from a ﬁnal subtlety in the analytic continuation of the path integral: for k /∈ Z,
the sum (3.47) can have multiple contributions from the same ﬂat connection, diﬀering
by a multiplicative factor e2πik. (If analytically continuing in N as well, factors of
e
2πiu
ℏ may also arise.) This behavior originates from the fact that exp
(ik
4πICS) is not
completely gauge-invariant when k /∈ Z. For example, in the case of the ﬁgure-eight
knot, the actual hyperbolic contribution to (3.47) goes like
(
eiπk−e−iπk)Zhyp
GC (M;u; ℏ), (3.52)
which vanishes at k ∈ Z, leading to polynomial rather than exponential growth of
JN(K;q) for u/iπ∼ N/k∈ Q. It is expected that this feature is fairly generic for
hyperbolic knots.
Acknowledgements
We would like to thank Edward Witten, Don Zagier, and Jonatan Lenells for enlight-
ening discussions on subjects considered in these notes. We would also like to thank
28
the organizers of the workshops Interactions Between Hyperbolic Geometry, Quantum
Topology, and Knot Theory ; Chern-Simons Gauge Theory: 20 years after ; and Low
Dimensional Topology and Number Theory II; and Columbia University, the Hausdorﬀ
Center for Mathematics, and the University of Tokyo, respectively, for their generous
support, accommodations, and collaborative working environment. The work of SG is
supported in part by DOE Grant DE-FG03-92-ER40701, in part by NSF Grant PHY-
0757647, and in part by the Alfred P. Sloan Foundation. Opinions and conclusions
expressed here are those of the authors and do not necessarily reﬂect the views of
funding agencies.
References
[1] R. M. Kashaev, The hyperbolic volume of knots from quantum dilogarithm , Lett.
Math. Phys. 39 (1997) 269–265, [ q-alg/9601025v2].
[2] H. Murakami and J. Murakami, The colored Jones polynomials and the simplicial
volume of a knot , Acta Math. 186 (2001), no. 1 85–104, [ math/9905075v2].
[3] E. Witten, Quantum Field Theory and the Jones Polynomial , Comm. Math.
Phys. 121 (1989), no. 3 351–399.
[4] N. Reshetikhin and V. Turaev, Invariants of 3-manifolds via link polynomials
and quantum groups , Invent. Math. 103 (1991), no. 3 547–597.
[5] R. Kirby and P. Melvin, The 3-manifold invariants of Witten and
Reshetikhin-Turaev for sl (2, C) , Invent. Math. 105 (1991), no. 1 1432–1297.
[6] W. P. Thurston, Three Dimensional Manifolds, Kleinian Groups, and Hyperbolic
Geometry, Bull. AMS 6 (1982), no. 3 357–381.
[7] G. Perelman, Ricci ﬂow with surgery on three-manifolds , math/0303109v1.
[8] E. Witten, 2+1 dimensional gravity as an exactly soluble system , Nucl. Phys.
B311 (1988) 46.
[9] E. Witten, Quantization of Chern-Simons gauge theory with complex gauge
group, Commun. Math. Phys. 137 (1991) 29.
[10] S. Gukov, Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the
A-Polynomial, Commun. Math. Phys. 255 (2005) 577–627, [ hep-th/0306165v1].
[11] T. Dimofte, S. Gukov, J. Lenells, and D. Zagier, Exact Results for Perturbative
Chern-Simons Theory with Complex Gauge Group , Comm. Num. Thy. and Phys.
3 (2009), no. 2 363–443, [ arXiv:0903.2472].
29
[12] D. Coulson, O. Goodman, C. Hodgson, and W. Neumann, Computing arithmetic
invariants of 3-manifolds , Experimental Mathematics 9 (2000), no. 1 127–152.
[13] W. D. Neumann, Extended Bloch group and the Cheeger-Chern-Simons class ,
Geom. Topol. 8 (2004) 413–474, [ math/0307092v2].
[14] C. K. Zickert, The Chern-Simons invariant of a representation ,
arXiv:0710.2049.
[15] H. Murakami, J. Murakami, M. Okamoto, T. Takata, and Y. Yokota, Kashaev’s
conjecture and the Chern-Simons invariants of knots and links , Experiment.
Math. 11 (2002), no. 3 427–435, [ math/0203119v2].
[16] K. Habiro, On the colored Jones polynomials of some simple links ,
Surikaisekikenkyusho Kokyuroku 1172 (2000) 34–43.
[17] L. D. Faddeev and R. M. Kashaev, Quantum Dilogarithm, Modern Phys. Lett.
A9 (1994), no. 5 427–434, [ hep-th/9310070v1].
[18] D. Cooper, M. Culler, H. Gillet, and D. Long, Plane curves associated to
character varieties of 3-manifolds , Invent. Math. 118 (1994), no. 1 47–84.
[19] W. D. Neumann and D. Zagier, Volumes of hyperbolic three-manifolds, Topology
24 (1985), no. 3 307–332.
[20] T. Yoshida, The eta-invariant of hyperbolic 3-manifolds , Invent. Math. 81 (1985)
473–514.
[21] H. M. Hilden, M. T. Lozano, and J. M. Montesinos-Amilibia, On volumes and
Chern-Simons invariants of geometric 3-manifolds , J. Math. Sci. Univ. Tokyo
1996 (3), no. 3 723–744.
[22] H. Murakami, Some limits of the colored Jones polynomials of the ﬁgure-eight
knot, Kyungpook Math. J. 44 (2004), no. 3 369–383, [ math/0308002v1].
[23] H. Murakami and Y. Yokota, The colored Jones polynomials of the ﬁgure-eight
knot and its Dehn surgery spaces , J. Reine Angew. Math 607 (2007) 47–68,
[math/0401084v3].
[24] E. Witten, Analytic Continuation of Chern-Simons Theory , arXiv:1001.2933.
[25] J. Porti, Torsion de Reidemesiter poir les vari´ et´ es hyperboliques, Mem. Amer.
Math. Soc. 128 (1997), no. 612.
[26] H. Murakami, The colored Jones polynomials and the Alexander polynomial of
the ﬁgure-eight knot, J. Geom. Topol. 7 (2007), no. 2 249–269, [ math/0502428v1].
30
[27] S. Gukov and H. Murakami, SL(2,C) Chern-Simons theory and the asymptotic
behavior of the colored Jones polynomial , math/0608324v2.
[28] D. Bar-Natan and E. Witten, Perturbative expansion of Chern-Simons theory
with non-compact gauge group , Comm. Math. Phys. 141 (1991), no. 2 423–440.
[29] D. S. Freed, M. J. Hopkins, J. Lurie, and C. Teleman, Topological Quantum
Field Theories from Compact Lie Groups , ”A Celebration of the Mathematical
Legacy of Raoul Bott” (2009) [arXiv:0905.0731].
[30] M. Atiyah, Geometry and physics of knots , Cambridge Univ. Press (1990).
[31] N. Woodhouse, Geometric quantization, New York: Oxford Univ. Press (1992).
[32] F. Bayen, M. Flato, C. Fronsdal, A. Lichnerowicz, and D. Sternheimer,
Deformation Theory and Quantization. I. Deformations of Symplectic
Structures, Ann. Physics 111 (1978), no. 1 61–110.
[33] M. Kontsevich, Deformation quantization of Poisson manifolds , Lett. Math.
Phys. 66 (2003), no. 3 157–216, [ q-alg/9709040v1].
[34] S. Gukov and E. Witten, Branes and Quantization , arXiv:0809.0305.
[35] S. Cecotti and C. Vafa, Topological antitopological fusion, Nucl. Phys. B367
(1991) 359–461.
[36] B. Dubrovin, Integrable systems in topological ﬁeld theory , Nucl. Phys. B379
(1992) 627–689.
[37] D. A. Vogan, Jr., Singular unitary representations, in Noncommutative harmonic
analysis and Lie groups (Marseille, 1980) (J. Carmona and M. Vergne, eds.),
vol. 880 of Lecture Notes in Math. , pp. 506–535. Springer, Berlin, 1981.
[38] S. Elitzur, G. Moore, A. Schwimmer, and N. Seiberg, Remarks on the canonical
quantization of the Chern-Simons-Witten theory , Nucl. Phys. B326 (1989) 108.
[39] S. Axelrod, S. D. Pietra, and E. Witten, Geometric Quantization of
Chern-Simons Gauge Theory , J. Diﬀ. Geom. 33 (1991) 787–902.
[40] S. Garoufalidis, On the characteristic and deformation varieties of a knot ,
Geometry and Topology Monographs 7 (2004) 291–304, [ math/0306230v4].
[41] S. Garoufalidis and T. T. Le, The colored Jones function is q-holonomic , Geom.
Topol. 9 (2005) 1253–1293, [ math/0309214v3].
[42] S. Garoufalidis and X. Sun, The non-commutative A-polynomial of twist knots ,
arXiv:0802.4074.
31
