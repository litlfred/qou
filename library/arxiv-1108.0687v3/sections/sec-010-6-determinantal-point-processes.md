---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-010-6-determinantal-point-processes
section_title: "Determinantal point processes"
section_number: 6
pages: 18-23
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
---
We consider here only simple point processes and often assume EN <∞ as well. If ρk : (Rd)k → R+
are measurable functions, then the simple point process Z is said to have joint intensities {ρk} if for
anyk and any family D1,...,D k of disjoint Borel subsets of Rd,
E


k∏
j=1
Z(Dj)

 =
∫
∏
j Dj
ρk(x1,...,x k)dx1 · · ·dxk.
In particular,
EN =
∫
Rd
ρ1(x)dx
so under the assumption EN <∞, we see that ρ1(x)dx is a ﬁnite measure on Rd. If ρ1 is not ﬁnite,
we will assume it is σ-ﬁnite. In any case, ρ1 is called the ﬁrst intensity measure ; see [HKPV09,
Sections 1.2 and 4.2] for further discussion of joint intensities and d eterminantal measures.
Deﬁnition 6.1 (determinantal point process) . A point process Z is said to be determinantal if it
has joint intensities {ρk} and there is a measurable kernel K : (Rd)2 → C such that
ρk(x1,...,x k) = det (K(xi,x j))1≤i,j≤k . (6.2)
If K(y,x ) = K(x,y ) for every x,y , then the process is said to be Hermitian. When discussing
determinantal processes below, we will always assume they a re Hermitian.
Stochastic covering carries over to the continuous case. To stat e the relevant results we invoke
the notion of the Palm process . This is a version of the process conditioned on the (measure zero)
event of a point at a speciﬁed location, x. It may be obtained by conditioning on there being a point
within distance ǫ of a given location x, then taking a weak limit. A more complete treatment may
be found in [Kal86]. The following proposition is proved in [Gol10].
Proposition 6.2 ([Gol10]). Suppose Z is a determinantal point process with continuous kernel K
and ﬁnite trace. Fix x and let Zx denote the Palm process that conditions on a point at x. Let Z ′
x
denote the result of removing the point at x from Zx. Then
(i) Whenever K −L is positive semi-deﬁnite, the process with kernel K stochastically dominates
the process with kernel L (this is [Gol10, Theorem 3]).
(ii) Z ′
x is determinantal with kernel L such that K −L is positive semi-deﬁnite.
(iii) Consequently, Z ≽ Z ′
x.
17
The continuous analogue of Proposition 2.3 is
Proposition 6.3. Let Z be a determinantal point process with ﬁnite mean EN =µ< ∞. Then for
any k for which P(N = k + 1) and P(N = k) are both nonzero, the conditional distributions of Z
given N satisfy
(Z |N =k + 1)⊲ (Z |N =k).
Proof: The following facts may be found in [HKPV06, Theorem 7]. A determina ntal point process
Z with mean µ <∞ has a kernel K whose spectrum is countable, contained in [0 , 1], and sums to
µ. Furthermore, Z may be represented as a mixture of homogeneous determinantal p rocesses as
follows. Let {λi :i ≥ 1} enumerate the eigenvalues with multiplicities and let {φi} be a corresponding
eigenbasis. For each i, ﬂip an independent coin with success probability λi. Let I denote the set
of i for which the coin-ﬂip was successful. Let KI be the (random) projection operator onto the
subspace spanned by the eigenvectors φi for which the coin-ﬂip was successful. Then KI is almost
surely a projection of ﬁnite dimension |I| and is the kernel of a |I|-homogeneous determinantal point
process. Choosing KI at random and then sampling from the corresponding process reco vers the
law of Z.
Several consequences are apparent. First, conditioning on N =k is the same as conditioning on
exactly k successes among the Bernoulli trials. Secondly, the conditional law of I given |I| =k + 1
stochastically dominates the conditional law of I given |I| = k. When the number of Bernoullis
is ﬁnite, this follows from the strong Rayleigh property for independ ent Bernoullis; an easy limit
argument extends the conclusion to the inﬁnite case. This fact abo ut stochastic domination is equiv-
alent to saying that the conditional law of the random subspace KI given |I| =k + 1 stochastically
dominates the conditional law of the random subspace KI given |I| =k, in the sense that the two
laws can be coupled as ( K,K ′) so that K ′ ⊆K. When K ′ ⊆K, the operator πK −πK ′ is positive
semi-deﬁnite. By ( ii) of Proposition 6.2, we conclude that ( Z |N =k + 1) ≽ (Z |N =k) which is
equivalent to stochastic covering in this case. □
Proof of Theorems 3.5:
With f as in the statement of the theorem, and I the collection of indices described in the
previous proposition, deﬁne ψ(I) to be the expectation of f applied to a conﬁguration chosen from
the determinantal process with kernel KI . Recall the notation N = |I|.
The event {f − Ef >a} is contained in the union of three events:
{
N >µ + a
2
}
∪
{
ψ(I) − Ef >a
2
}
∪
{
f −ψ(I)> a
2, N≤µ + a
2
}
.
Thus P(f − Ef > a) is bounded above by the sum of the corresponding probabilities. Ea ch of the
ﬁrst two pieces is bounded above by exp[ −a2/(4(a + 2µ))]: the ﬁrst follows from Lemma 4.2 and
the second follows from the proof of Lemma 4.4 because ψ is Lipschitz in the Bernoulli variables
18
Yi := 1i∈I . The last piece is bounded above by exp[ −a2/(16(a+2µ))]. To see this, apply Theorem 3.4
to the homogenous determinantal processes PI with kernels KI , obtaining, when |I| =k, that
PI
(
f −ψ(I)> a
2
)
≤ exp
(
− (a/2)2
8k
)
≤ exp
(
− a2
16(a + 2µ)
)
.
Reassembling these gives the upper bound
P
(
f −ψ(I)> a
2, N≤µ + a
2
)
≤ exp
(
− a2
16(a + 2µ)
)
.
The rest of the argument is identical to the conclusion of the proof of Theorem 3.2. □
Example 6.4 (Ginibre’s translation invariant process) . Ginibre [Gin65] considers the distribution
of eigenvalues of an k × k matrix with independent complex Gaussian entries. In the li mit as
k → ∞ , the density becomes constant over the whole plane. The limi ting process Z turns out to be
a (Hermitian) determinantal point process with kernel
K(z1,z 2) := 1
πez1z2 exp
(
− |z1|2 + |z2|2
2
)
;
see, e.g. [Sos00, (2.16)]. The process Z is ergodic and invariant under all rigid transformations of
the plane. It was suggested [LCH90] to use this process as the set of centers for a random Voronoi
tesselation because the mutual repulsion of the points make s the resulting tesselation more realistic
than the standard Poisson-Voronoi tesselation for many pur poses. Some rigorous results along these
lines were obtained in [Gol10].
The mean number of points in any region D is 1/π times the area |D|, so the restriction of ZD
to such a region of ﬁnite area is a determinantal process with ﬁnite mean number of points. Fix a
ﬁnite region, D, and let f count the number of “lonely” points in D, these being such that no other
point of Z in D is within distance 1. We claim that f is Lipschitz with constant equal to 6. Clearly
if a point z is added to the conﬁguration η then f can increase by at most 1. It is well known that
the maximum number of points in a unit disk that can be at mutua l distance of at least 1 from one
another is 6, which implies that the addition of z can result in the loss of at most 6 lonely points.
Applying Theorem 3.5 to f/ 6 yields the concentration inequality
P(|f − Ef | ≥ a) ≤ 5 exp
(
− a2
96(a + 12|D|/π)
)
.
Example 6.5 (Zeros of random polynomials) . Let {Xn} be IID standard complex Gaussian random
variables and deﬁne the random power series
h(z) :=
∞∑
n=0
Xnzn.
It is easy to see that h is almost surely analytic on the open unit disk and the number of zeros on
any disk of radius ρ <1 has ﬁnite mean. The remarkable properties of the point proce ss Z on the
19
unit disk that is the zero set of h are detailed in [PV05]. It is a determinantal process whose k ernel
is the Bergman kernel π−1(1 −zw)−2. It is invariant under M¨ obius transformations of the unit d isk
and has intensity measure π−1/(1 − |z|2)2. Endowing the unit disk with the hyperbolic metric, the
M¨ obius transformations become isometries, whenceZ is hyperbolic isometry invariant.
Fix ρ< 1 and r> 0 and let f count the number of zeros of the restriction Zρ of Z to the disk of
radius 1 −ρ that are “hyperbolically lonely”, meaning that no other poi nt of Zρ is within a hyperbolic
distance r. Let cr denote the maximum number of points at mutual hyperbolic dis tance r that may
be be placed in a disk of hyperbolic radius r. Arguing as in Example 6.4 we see that f is Lipschitz
with constant cr. The mean number of points in Zρ isρ2/(1 −ρ2) which for simplicity we can bound
from above by 1/(1 −ρ2). An application of Theorem 3.5 to f/c r now yields
P(|f − Ef | ≥ a) ≤ 5 exp
(
− a2
16cra + 32c2r(1 −ρ2)−1
)
.
Acknowledgments
We thank Subhroshekhar Ghosh and an anonymous referee for de tailed comments leading to the
correction and improvement of the exposition and results.
References
[AS08] N. Alon and J. Spencer. The probabilistic method . John Wiley & Sons, Hoboken, New
Jersey, third edition, 2008.
[BBL09] J. Borcea, P. Br¨ and´ en, and T. Liggett. Negative depen dence and the geometry of poly-
nomials. J. AMS , 22:521–567, 2009.
[BP93] R. Burton and R. Pemantle. Local characteristics, entrop y and limit theorems for uniform
spanning trees and domino tilings via transfer-impedances. Ann. Probab., 21:1329–1371,
1993.
[Che52] H. Chernoﬀ. A measure of asymptotic eﬃciency for tests o f a hypothesis based on the
sum of observations. Ann. Math. Statist. , 23:493–507, 1952.
[DR98] D. Dubhashi and D. Ranjan. Balls and bins: a study in negative dependence. Rand.
Struct. Alg. , 13:99–124, 1998.
[Dur04] R. Durrett. Probability: Theory and Examples . Duxbury Press, Belmont, CA, third
edition, 2004.
20
[Far08] A. Farcomeni. Some ﬁnite sample properties of negatively de pendent random variables.
Theor. Prob. Math. Statist. , 77:155–163, 2008.
[FM92] T. Feder and M. Mihail. Balanced matroids. Annual ACM Symposium on Theory of
Computing, pages 26–38, 1992.
[Fre75] D. Freedman. On tail probabilities for martingales. Ann. Probab., 3:100–118, 1975.
[Gin65] J. Ginibre. Statistical ensembles of complex, quaternion, an d real matrices. J. Math.
Phys., 6:440–449, 1965.
[Gol10] A. Goldman. The palm measure and the Voronoi tesselation fo r the Ginibre process.
Ann. Appl. Prob. , 20:90–128, 2010.
[GSS11] S. Gharan, A. Saberi, and M. Singh. A randomized rounding a pproach to the Traveling
Salesman Problem. In 2011 IEEE 52nd Annual Symposium on Foundations of Computer
Science, pages 550–559. IEEE Computer Science: Los Alamitos, CA, 2011.
[HKPV06] J. B. Hough, M. Krishnapur, Y. Peres, and B. Virag. Dete rminantal processes and
independence. Probability Surveys, 3:206–229, 2006.
[HKPV09] J. B. Hough, M. Krishnapur, Y. Peres, and B. Virag. Zeros of Gaussian analytic functions
and determinantal point processes , volume 51 of University Lecture Series . American
Mathematical Society, Providence, RI, 2009.
[Hoe63] W. Hoeﬀding. Probability inequalities for soums of bounded ra ndom variables. J. Amer.
Stat. Assoc. , 58:13–30, 1963.
[Joh03] K. Johansson. Discrete polynuclear growth and determina ntal processes. Comm.
Math.Phys., 242:277–329, 2003.
[Kal86] O. Kallenberg. Random measures. Academic Press, London, fourth edition, 1986.
[KM59] S. Karlin and J. McGregor. Condidence probabilities. Paciﬁc J. Math. , 9:1141–1164,
1959.
[LCH90] G. Le Caer and J. S. Ho. The Voronoi tesselation generate d from eigenvalues of complex
random matrices. J. Phys. A Math. Gen. , 23:3279–3295, 1990.
[Lig77] T. Liggett. The stochastic evolution of an inﬁnite system of in teracting particles. In Ecole
de Probabilites de Saint Flour VI, 1976 , volume 598 of Lecture notes in Mathematics ,
pages 187–248. Springer-Verlag, New York, 1977.
[Lyo03] R. Lyons. Determinantal probability measures. IHES, 98:167–212, 2003.
[McD89] C. McDiarmid. On the method of bounded diﬀerences. In J. S iemons, editor, Surveys
in Combinatorics, volume 41 of London Mathematical Society Lecture Note Series , pages
148–188. Cambridge University Press, Cambridge, 1989.
21
[Pem00] R. Pemantle. Toward a theory of negative dependence. J. Math. Phys. , 41:1371–1390,
2000.
[PS97] A. Panconesi and A. Srinivasan. Randomized distributed edg e coloring via an extension
of the Chernoﬀ–Hoeﬀding bounds. SIAM J. Comput. , 26:350–368, 1997.
[PV05] Y. Peres and B. Virag. Zeros of the i.i.d. Gaussian power series : a conformally invariant
determinantal process. Acta Math., 194:1–35, 2005.
[Sos00] A. Soshnikov. Determinantal random point ﬁelds. Uspekhi Mat. Nauk , 55:107–160, 2000.
[Tut71] W. Tutte. Introduction to the Theory of Matroids , volume 37 of Modern Analytic and
Computational Methods in Science and Mathematics . American Elsevier, New York,
1971.
[Wag11] D. G. Wagner. Multivariate stable polynomials: theory and ap plication. Bull. Amer.
Math. Soc. , 48:53–84, 2011.
22
