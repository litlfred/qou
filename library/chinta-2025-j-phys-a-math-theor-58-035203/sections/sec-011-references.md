---
doc_id: chinta-2025-j-phys-a-math-theor-58-035203
doc_title: "The discrete analogue of the Gaussian"
section_id: sec-011-references
section_title: "References"
section_number: null
pages: 20-23
source_pdf: Chinta_2025_J._Phys._A__Math._Theor._58_035203.pdf
source_sha256: baba83ca76c773d4
toc_source: outline
---
lent presentation. In practice, as described in [CKS22], one alters the output of a Z-valued
algorithm M which produces results from a given dataset D by adding a random amount. The
main results of [CKS22] are that one can use a discretized Gaussian random (6) (using our ter-
minology) to create algorithms which satisfy differential privacy, and that one can effectively
and efficiently sample from a discretized Gaussian random variable.
It would be interesting to determine if the discrete Gaussian (3) also satisfies the criterion
established in [CKS22] for random ‘noise’ as required by differential privacy. It should be
noted that other authors have pointed out the potential usefulness of (3) and distinguished the
difference between (3) and (6); see section 2.6 of [Li24] who refers to earlier work by the
same author in [Li90]. One can reasonably expect that, indeed, (3) will fulfill the conditions
needed for differential privacy, if for no reason other than the triangle inequality, the results
from [CKS22] and Proposition 1. However, it would be better to establish differential privacy
associated to (3) without appealing to [CKS22]. We will leave this study for a later time.
From the point of view of probability, one can state several advantages that (3) has over (1).
First, we note that the (quite impressive) analysis of [CKS22] includes, for example, estimates
for the moment generating function and variance of the discretized Gaussian (6); see lemma 8
and corollary 9 of [CKS22]. By contrast, note that the characteristic function of (3) is explicitly
computed; see (16). As such, one has elementary closed-form expressions for all moments
of (3). See also [AGMP24]. Second, the sum of two independent discretized Gaussian random
variables (6) is close to, but not equal to, a discretized Gaussian random variable; see the
19
J. Phys. A: Math. Theor. 58 (2025) 035203
G Chinta et al
comment after remark 3.7 in [AA19] and theorem 1.1 of [AR24]. By comparison, the sum
of two independent discrete Gaussians (3) is a discrete Gaussian, and the convolution of the
probability density functions is, in effect, computed in the above-cited Chapman–Kolmogorov
equation; see section 4. Finally, let us point out that one application of theorem 5 is a means
by which one can sample from a discrete Gaussian is a manner similar to a sampling method
for a continuous Gaussian random variable. In doing so, one has, at least the beginning of, an
analogue to the sampling algorithms developed in [CKS22]. Other sampling methods could
be developed based on numerical evaluations of Bessel functions; to this end, we found the
articles [Am74] and [GS81] to be interesting.
Finally, let us note that the articles [AA19] and [AR24] consider discretized Gaussian ran-
dom variables on any d-dimensional lattice Λ in Rd. Certainly, our point of view is amenable
to such a setting; see, for example, [CJK10] and more generally [CJK12]. The probability
density function is simply the heat kernel on Λ, and we assert that one can prove an analogue
of theorem 5. Again, these considerations will be undertaken elsewhere.
Data availability statement
No new data were created or analysed in this study.
ORCID iDs
Gautam Chinta https://orcid.org/0000-0002-2672-3819
Jay Jorgenson https://orcid.org/0000-0002-9765-0944
Anders Karlsson https://orcid.org/0000-0002-1886-6780
Lejla Smajlovi´c https://orcid.org/0000-0002-2709-5535
References
[AGMP24] Abadías L, Gonzalez-Camus J, Miana P and Pozo J 2021 Large time behaviour for the heat
equation on Z, moments and decay rates J. Math. Anal. Appl. 500 125137
[AR24] Aggarwal D and Regev O A note on discrete Gaussian combinations of lattice vectors
(arXiv:1308.2405)
[AA19] Agostini D and Amendola C 2019 Discrete Gaussian distributions via theta functions SIAM
J. Appl. Algebra Geom. 3 1–30
[Am74] Amos D E 1974 Computation of modified Bessel functions and their ratios Math. Comp.
28 239–51
[An58] Anderson P W 1958 Absence of diffusion in certain random lattices Phys. Rev.
109 1492–505
[ADG02] Al-Jarrah A, Dempsey K M and Glasser M L 2002 Generalized series of Bessel functions
J. Comput. Appl. Math. 143 1–8
[At87] Athreya K B 1987 Modified Bessel function asymptotics via probability Stat. Probab. Lett.
5 325–7
[Ba70] Barber M N 1970 Asymptotic results for self-avoiding walks on a manhattan lattice Physica
48 237–41
[Ba49] Bateman H 1943 Some simple differential difference equations and the related functions
Bull. Am. Math. Soc 49 494–512
[CKS22] Canonne C, Kamath G and Steinke T 2022 The discrete Gaussian for differential privacy
J. Privacy Confidentiality 12 784
[Ch84] Chavel I 1984 Eigenvalues in Riemannian Geometry (Academic)
[CJK10] Chinta G, Jorgenson J and Karlsson A 2010 Zeta functions, heat kernels and spectral asymp-
totics on degenerating families of discrete tori Nagoya Math. J. 198 121–72
20
J. Phys. A: Math. Theor. 58 (2025) 035203
G Chinta et al
[CJK12] Chinta G, Jorgenson J and Karlsson A 2012 Complexity and heights of tori. Dynamical
systems and group actions Contemp. Math. vol 567 (American Mathematical Society)
pp 89–98
[CJK15] Chinta G, Jorgenson J and Karlsson A 2015 Heat kernels on regular graphs and generalized
Ihara zeta function formulas Monatsh. Math. 178 171–90
[CJKS24] Chinta G, Jorgenson J, Karlsson A and Smajlovi´c L 2024 The parametrix construction of
the heat kernel on a graph Complex Anal. Oper. Theory 18 176
[CY99] Chung F and Yau S-T 1999 Coverings, heat kernels and spanning trees Electron. J. Combin.
6 21
[CMS00] Cowling M, Meda S and Setti A 2000 Estimates for functions of the Laplace operator on
homogeneous trees Trans. Am. Math. Soc. 352 4271–93
[DH13] Decrouez G and Hall P 2013 Normal approximation and smoothness for sums of means of
lattice-valued random variables Bernoulli 19 1268–93
[Do92] Dowker J S 1992 On Verlinde’s formula for the dimensions of vector bundles on moduli
spaces J. Phys. A 25 2641–8
[DEK12] Dowker F, Elizalde E and Kirsten K 2012 Applications of zeta functions and other spectral
functions in mathematics and physics: a special issue in honour of Stuart Dowker’s 75th
birthday J. Phys. A 45 370301
[Du19] Dubout J Spectral zeta functions of graphs, their symmetries and extended Catalan numbers
(arXiv:1909.01659)
[DD88] Duplanticr B and David F 1988 Exact partition functions and correlation functions of mul-
tiple Hamiltonian walks on the Manhattan lattice J. Stat. Phys. 51 327–434
[El12] Elizalde E 2012 Ten physical applications of spectral zeta functions Lecture Notes in
Physics vol 855, 2nd edn (Springer)
[Fe66] Feller W 1966 Infinitely divisible distributions and Bessel functions associated with random
walks SIAM J. Appl. Math. 14 864–75
[Fe70] Feller W 1970 An Introduction to Probability Theory and Its Applications Vol II, 2dn edn
(Wiley)
[FK17] Friedli F and Karlsson A 2017 Spectral zeta functions of graphs and the Riemann zeta
function in the critical strip Tohoku Math. J. 69 585–610
[GS81] Gatto M A and Seery J B 1981 Numerical evaluation of the modified Bessel functions I and
K Comput. Math. Appl. 7 203–9
[GK24] Gavalakis L and Kontoyiannis I 2024 Entropy and the discrete central limit theorem
Stochastic Process. Appl. 170 10
[GR07] Gradshteyn I S and Ryzhik I M 2007 table of Integrals, Series and Products (Elsevier
Academic)
[Gr23] Greenblatt R L 2023 Discrete and zeta-regularized determinants of the Laplacian on poly-
gonal domains with Dirichlet boundary conditions J. Math. Phys. 64 043301
[GN98] Grigor’yan A and Noguchi M 1998 The heat kernel on hyperbolic space Bull. London Math.
Soc. 30 643–50
[GI02] Grünbaum F A and Iliev P 2002 Heat kernel expansions on the integers Math. Phys. Anal.
Geom 5 183–200
[HK20] Hou Y and Kandel S 2020 Asymptotic analysis of determinant of discrete Laplacian Lett.
Math. Phys. 110 259–96
[IL71] Ibragimov I A Yu. I A and Linnik V 1971 Independent and Stationary Sequences of Random
Variables (Wolters-Noordhoff)
[IK22] Izyurov K and Khristoforov M 2022 Asymptotics of the determinant of discrete Laplacians
on triangulated and quadrangulated surfaces Commun. Math. Phys. 394 531–72
[JKS23] Jorgenson J, Karlsson A and Smajlovi´c L 2024 The resolvent kernel on the discrete circle
and twisted cosecant sums J. Math. Anal. Appl. 538 23
[KS18] Kan N and Shiraishi K 2018 Free energy on a cycle graph and trigonometric deformation
of heat kernel traces on odd spheres J. Phys. A 51 23
[KS23] Kan N and Shiraishi K 2023 Discrete time heat kernel and UV modified propagators with
dimensional deconstruction J. Phys. A 56 16
[K12] Karlsson A 2012 Applications of Heat Kernels on Abelian Groups: ζz(2n), Quadratic
Reciprocity, Bessel Integrals Number Theory, Analysis and Geometry (Springer)
pp 307–20
21
J. Phys. A: Math. Theor. 58 (2025) 035203
G Chinta et al
[KN06] Karlsson A and Neuhauser M 2006 Heat kernels, theta identities and zeta functions on
cyclic groups Topological and Asymptotic Aspects of Group Theory vol 394 (American
Mathematical Society) pp 177–89
[KP23] Karlsson A and Pallich M 2023 Volumes of spheres and special values of zeta functions of
Z and Z/nZ Acta Arith. 208 161–70
[Ka61] Kasteleyn P W 1961 The statistics of dimers on a lattice, I. The number of dimer arrange-
ments on a quadratic lattice Physica 27 1209–25
[Ke00] Kenyon R 2000 Long-range properties of spanning trees J. Math. Phys. 41 1338–63
[Li90] Lindeberg T 1990 Scale-space for discrete signals IEEE Trans. Pattern Anal. Mach. Intell.
12 234–54
[Li24] Lindeberg T Discrete approximations of Gaussian smoothing and Gaussian derivatives
(arXiv:2311.11317)
[Ly05] Lyons R 2005 Asymptotic enumeration of spanning trees Combin. Probab. Comput.
14 491–522
[Mu83] Mumford D 1983 Tata Lectures on Theta I, With the Assistance Progr. Math. vol
28 C Musili, M Nori, E Previato and M Stillman (Birkhäuser Boston, Inc) p xiii+ 235
[NP00] Nesterenko V V and Pirozhenko I G 2000 Spectral zeta functions for a cylinder and a circle
J. Math. Phys. 41 4521–31
[Pa93] Pang M M H 1993 Heat kernels of graphs J. London Math. Soc. 47 50–64
[Pe75] Petrov V V 1975 Sums of Independent Random Variables (Springer)
[RV15] Reshetikhin N and Vertman B 2015 Combinatorial quantum field theory and gluing formula
for determinants Lett. Math. Phys. 105 309–40
[SW00] Shrock R and Wu F Y 2000 Spanning trees on graphs in d dimensions J. Phys. A
33 3881–902
[SS01] Sokal A D and Starinets A O 2001 Pathologies of the large-N limit for RPN−1, CPN−1,
QPN−1 and mixed isovector/isotensor σ-models Nucl. Phys. B 601 425–502
[SW23] Szewczak Z and Weber M 2023 Classical and almost sure local limit theorems
Dissertationes Math. 97 589
[V03] Vassilevich D V 2003 Heat kernel expansion: user’s manual Phys. Rep. 388 279
[Wa44] Watson G N 1995 A Treatise on the Theory of Bessel Functions 2nd edn (Cambridge
University Press) p viii+804
[XZZ22] Xie B, Zhao Y and Zhao Y 2024 Special values of spectral zeta functions of graphs and
Dirichlet L-functions J. Number Theory 256 136–59
22
