---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-023-c-hunter-guerrieri-algorithm
section_title: "C Hunter-Guerrieri algorithm"
section_number: null
pages: 45-52
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
Hunter-Guerrieri algorithm
The Hunter-Guerrieri algorithm [87] is concerned with the following problem. Let p(ζ) be a
function analytic at the origin which has the following expansion
p(ζ) =
∞
X
n=0
pnζn.
(C.1)
Let us suppose that the singularities of p(ζ) which are closest to the origin are located at ζω and
ζ∗
ω, which are complex conjugate to each other. Suppose that, at these two singular points, p(ζ)
has the following expansion
p(ζω + ξ) =(−ξ/ζω)−νr(ξ) + regular,
(C.2a)
p(ζ∗
ω + ξ) =(−ξ/ζ∗
ω)−νr∗(ξ) + regular,
ν̸ ∈Z,
(C.2b)
– 44 –
where
r(ξ) =
∞
X
k=0
bkξk
(C.3)
Darboux’ theorem [98, 99] implies that the large order behavior of pn is controlled by bk in the
following manner
pn ∼
∞
X
k=0
2(−1)kRk−nΓ(n + ν −k)Bk
n!Γ(ν −k)
cos((n −k)θ −βk),
(C.4)
where we use the notation
ζω = Reiθ,
bk = Bkeiβk.
(C.5)
Imagine now that we have a long sequence of values of pn. The problem is whether it is possible
to extract bk from this sequence by using the formula (C.4).
The solution to this problem is of great interest for doing concrete calculations in the theory
of resurgence introduced in Section 2.2. In that context, p(ζ) is the Borel transform bϕ(ζ) of
certain Gevrey-1 series ϕ(z), and pn are the coeﬃcients an/n!. r(ξ) is the Borel transform of
the resurgent function ϕω(z) at the singularity ζω, and the coeﬃcients bk are related to the an,ω
appearing in the expansion (2.16) of ϕω(z), by
bk =
ζ−ν
ω
2i sin πν
ak,ω
Γ(k + 1 −ν).
(C.6)
When two nearest singularities conjugate to each other are present in the Borel plane, the large
order behavior of an is given by (3.128) which is a consequence of (C.4). In this case, it is in
general a diﬃcult problem to extract information on ak,ω from a sequence of an, as the usual
method of Richardson extrapolation does not work.
Hunter and Guerrieri solved this problem beautifully in [87]. The ﬁrst key step is to use the
following composite and symmetric representation of p(ζ)
p(ζ) =
∞
X
k=0
(ck + dkζ) [(1 −ζ/ζω)(1 −ζ/ζ∗
ω)]−ν+k + regular
(C.7)
where the coeﬃcients ck, dk are real. We can relate the real coeﬃcients ck, dk to the complex
coeﬃcients bk by expanding (C.7) near ζ = ζω
p(ζ) ∼eiν(π/2−θ)
(2 sin θ)ν

1 −ζ
ζω
−ν
∞
X
k=0
((ck + dkζω) + dk(ζ −ζω))
·
∞
X
ℓ=0
(2i sin θ)k−ℓΓ(k −ν + 1)
ℓ! Γ(k −ν −ℓ+ 1)
ζ −ζω
R
k+ℓ
,
(C.8)
and comparing coeﬃcients with (C.2a). For instance, at leading order we have
c0 + d0ζω = (2 sin θ)νeiν(θ−π/2) b0.
(C.9)
– 45 –
In general, we have the relation
bn =eiν(π/2−θ)
(2 sin θ)ν R−n
"
(cn + dnζω)(2i sin θ)n
+
n−1
X
k=0

(ck + dkζω) (2i sin θ)2k−nΓ(k + 1 −ν)
(n −k)!Γ(2k + 1 −n −ν) + Rdk
(2i sin θ)2k+1−nΓ(k + 1 −ν)
(n −k −1)!Γ(2k + 2 −n −ν)
#
,
(C.10)
which can be used to relate the complex coeﬃcient bn and the real coeﬃcients cn, dn, whenever
R, θ, ν, as well as bk, ck, dk for k = 0, 1, . . . , n −1, are already known.
Now the key step is to rewrite (C.7) using the Gegenbauer polynomials, which are deﬁned
by the generating function
(1 −2zs + s2)−σ =
∞
X
n=0
Cσ
n(z)sn.
(C.11)
We ﬁnd
pn ∼R−n
∞
X
k=0
ckCν−k
n
(µ) + R1−n
∞
X
k=0
dkCν−k
n−1(µ),
µ = cos θ.
(C.12)
This can be regarded as a convenient rearrangement of the asymptotic behavior (C.4).
The
Gegenbauer polynomials have very nice recursion relations. By exploiting cleverly these recursion
relations we can deﬁne recursively the following objects,
S0
n(R, µ, ν) =pn,
(C.13)
Sm+1
n
(R, µ, ν) =R2Sm
n (R, µ, ν) −2(n + ν −2m −1)Rµ
n
Sm
n−1(R, µ, ν)
+ (n + 2ν −3m −2)(n −m −1)
n(n −1)
Sm
n−2(R, µ, ν).
(C.14)
so that in the asymptotics of Sm
n the coeﬃcients ck, dk for k = 0, . . . , m −1 have been canceled,
and Sm
n is progressively smaller with increasing m and large ﬁxed n. In fact, one can show
Sm
n (R, µ, ν) ∼O(nν−2m−1).
(C.15)
Then we can solve for the three unknowns R, µ, ν approximately by three equations
Sm
n (R, µ, ν) = Sm
n−ℓ(R, µ, ν) = Sm
n−2ℓ(R, µ, ν) = 0.
(C.16)
The step ℓis usually taken to be 1. The approximation becomes increasingly more accurate with
larger m and n.
There are several comments. First of all, in practice the equations (C.16) are non-linear
equations. It is more convenient to solve them iteratively by the Newton–Raphson method. The
derivatives ∂RSm
n , ∂µSm
n , ∂νSm
n can be constructed recursively alongside Sm
n with (C.13), (C.14).
We take the solutions to S1
n as initial estimates for the Newton-Raphson method. To quickly
solve S1
n, we take four equations
S1
n = S1
n−ℓ= S1
n−2ℓ= S1
n−3ℓ= 0,
(C.17)
– 46 –
and solve them as linear equations for four independent unknowns R2, Rµ, Rµν, ν. The estimates
for R, µ are then obtained by R =
√
R2, µ = Rµ/
√
R2. Note that since these are approximate
solutions they usually do not satisfy the relation
Rµν = Rµ · ν.
(C.18)
Second, the Hunter-Guerrieri algorithm can be slightly modiﬁed to calculate coeﬃcients bk
as well. Once R, µ, ν are known, we move c0, d0 to the left hand side in (C.12)
p(1)
n
∼R−n
∞
X
k=0
ck+1Cν−1−k
n
(µ) + R1−n
∞
X
k=0
dk+1Cν−1−k
n−1
(µ)
(C.19)
where
p(1)
n
:= pn −R−nc0Cν
n(µ) −R1−nd0Cν
n−1(µ).
(C.20)
This indicates that we can do the same construction as (C.13), (C.14) with pn replaced by p(1)
n
and ν reduced by 1. The Sm
n (c0, d0) constructed in this way are functions of c0, d0, and in their
asymptotics the coeﬃcients ck+1, dk+1 for k = 0, . . . , m −1 have been canceled so that they
are progressively smaller with increasing m and large ﬁxed n. We can similarly solve the two
unknowns c0, d0 with two equations
Sm
n (c0, d0) = Sm
n−ℓ(c0, d0) = 0.
(C.21)
Note that Sm
n (c0, d0) are linear in c0, d0, so (C.21) can be solved directly without resort to the
Newton–Raphson method. In general, if we know R, µ, ν as well as cj, dj for j = 0, 1, . . . , k −1,
the coeﬃcients ck, dk can be solved from
Sm
n (ck, dk) = Sm
n−ℓ(ck, dk) = 0.
(C.22)
Here, Sm
n (ck, dk) are constructed by using (C.13), (C.14), where ban are replaced by
p(k)
n
:= pn −R−n
k
X
j=0
cjCν−j
n
(µ) −R1−n
k
X
j=0
djCν−j
n−1(µ)
(C.23)
and ν shifted to ν −k −1. Once ck, dk are known, bk can be obtained by (C.10).
References
[1] E. Witten, Supersymmetry and Morse theory, J. Diﬀ. Geom. 17 (1982) 661–692.
[2] R. Gopakumar and C. Vafa, M-theory and topological strings. 2., hep-th/9812127.
[3] T. Dimofte, D. Gaiotto and S. Gukov, 3-Manifolds and 3d Indices, Adv. Theor. Math. Phys. 17
(2013) 975–1076, [1112.5179].
[4] M. Kontsevich and Y. Soibelman, Stability structures, motivic Donaldson-Thomas invariants and
cluster transformations, 0811.2435.
[5] S. Cecotti and C. Vafa, On classiﬁcation of N=2 supersymmetric theories, Commun. Math. Phys.
158 (1993) 569–644, [hep-th/9211097].
[6] D. Gaiotto, G. W. Moore and A. Neitzke, Four-dimensional wall-crossing via three-dimensional
ﬁeld theory, Comm. Math. Phys. 299 (2010) 163–224.
[7] D. Gaiotto, G. W. Moore and A. Neitzke, Wall-crossing, Hitchin systems, and the WKB
approximation, Adv. Math. 234 (2013) 239–403.
– 47 –
[8] T. Bridgeland, Riemann-Hilbert problems from Donaldson-Thomas theory, Invent. Math. 216
(2019) 69–124, [1611.03697].
[9] M. Mari˜no, From resurgence to BPS states, talk given at the conference Strings 2019, Brussels,
https://livestream.com/accounts/7777696/events/8742238/videos/193704304, 2019.
[10] A. Grassi, J. Gu and M. Mari˜no, Non-perturbative approaches to the quantum Seiberg-Witten curve,
JHEP 07 (2020) 106, [1908.07065].
[11] S. Garoufalidis, J. Gu and M. Mari˜no, The resurgent structure of quantum knot invariants,
Commun. Math. Phys. 386 (2021) 469–493, [2007.10190].
[12] S. Garoufalidis, J. Gu and M. Mari˜no, Peacock patterns and resurgence in complex Chern-Simons
theory, 2012.00062.
[13] M. Kontsevich and Y. Soibelman, Analyticity and resurgence in wall-crossing formulas,
2005.10651.
[14] N. A. Nekrasov and S. L. Shatashvili, Quantization of integrable systems and four dimensional
gauge theories, in 16th International Congress on Mathematical Physics, Prague, August 2009,
265-289, World Scientiﬁc 2010, 2009. 0908.4052.
[15] N. A. Nekrasov, Seiberg–Witten prepotential from instanton counting, Adv. Theor. Math. Phys. 7
(2004) 831–864, [hep-th/0206161].
[16] A. Mironov and A. Morozov, Nekrasov functions and exact Bohr–Sommerfeld integrals, JHEP
1004 (2010) 040, [0910.5670].
[17] M. Mari˜no, Lectures on non-perturbative eﬀects in large N gauge theories, matrix models and
strings, Fortsch. Phys. 62 (2014) 455–540, [1206.6272].
[18] A. Grassi, Y. Hatsuda and M. Mari˜no, Topological strings from quantum mechanics, Annales Henri
Poincar´e 17 (2016) 3177–3235, [1410.3382].
[19] S. Codesido, A. Grassi and M. Mari˜no, Spectral theory and mirror curves of higher genus, Annales
Henri Poincar´e 18 (2017) 559–622, [1507.02096].
[20] M. Mari˜no and P. Putrov, ABJM theory as a Fermi gas, J.Stat.Mech. 1203 (2012) P03001,
[1110.4066].
[21] Y. Hatsuda, S. Moriyama and K. Okuyama, Instanton Eﬀects in ABJM Theory from Fermi Gas
Approach, JHEP 1301 (2013) 158, [1211.1251].
[22] Y. Hatsuda, S. Moriyama and K. Okuyama, Instanton Bound States in ABJM Theory, JHEP 1305
(2013) 054, [1301.5184].
[23] Y. Hatsuda, M. Mari˜no, S. Moriyama and K. Okuyama, Non-perturbative eﬀects and the reﬁned
topological string, JHEP 1409 (2014) 168, [1306.1734].
[24] J. Kallen and M. Mari˜no, Instanton eﬀects and quantum spectral curves, Annales Henri Poincar´e
17 (2016) 1037–1074, [1308.6485].
[25] M.-x. Huang and X.-f. Wang, Topological strings and quantum spectral problems, JHEP 1409
(2014) 150, [1406.6178].
[26] K. Hikami, Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential
function as a classical limit of the partition function, J. Geom. Phys. 57 (2007) 1895–1940.
[27] T. Dimofte, S. Gukov, J. Lenells and D. Zagier, Exact Results for Perturbative Chern-Simons
Theory with Complex Gauge Group, Commun. Num. Theor. Phys. 3 (2009) 363–443, [0903.2472].
[28] J. Ellegaard Andersen and R. Kashaev, A TQFT from Quantum Teichm¨uller Theory,
Commun.Math.Phys. 330 (2014) 887–934, [1109.6295].
[29] R. Couso-Santamar´ıa, J. D. Edelstein, R. Schiappa and M. Vonk, Resurgent transseries and the
holomorphic anomaly, Annales Henri Poincar´e 17 (2016) 331–399, [1308.1695].
[30] R. Couso-Santamar´ıa, J. D. Edelstein, R. Schiappa and M. Vonk, Resurgent transseries and the
holomorphic anomaly: Nonperturbative closed strings in local CP2, Commun. Math. Phys. 338
(2015) 285–346, [1407.4821].
– 48 –
[31] T. Dimofte, D. Gaiotto and S. Gukov, Gauge theories labelled by three-manifolds, Comm. Math.
Phys. 325 (2014) 367–419.
[32] R. Eager, S. A. Selmani and J. Walcher, Exponential Networks and Representations of Quivers,
JHEP 08 (2017) 063, [1611.06177].
[33] S. Banerjee, P. Longhi and M. Romo, Exploring 5d BPS Spectra with Exponential Networks,
Annales Henri Poincare 20 (2019) 4055–4162, [1811.02875].
[34] S. Banerjee, P. Longhi and M. Romo, Exponential BPS graphs and D brane counting on toric
Calabi-Yau threefolds: Part I, 1910.05296.
[35] S. Banerjee, P. Longhi and M. Romo, Exponential BPS graphs and D-brane counting on toric
Calabi-Yau threefolds: Part II, 2012.09769.
[36] P. Longhi, On the BPS spectrum of 5d SU(2) super-Yang-Mills, 2101.01681.
[37] M.-X. Huang, A. Klemm and M. Poretschkin, Reﬁned stable pair invariants for E-, M- and
[p, q]-strings, JHEP 1311 (2013) 112, [1308.0619].
[38] M. Aganagic, V. Bouchard and A. Klemm, Topological Strings and (Almost) Modular Forms,
Commun.Math.Phys. 277 (2008) 771–819, [hep-th/0607100].
[39] S. Codesido, J. Gu and M. Mari˜no, Operators and higher genus mirror curves, JHEP 02 (2017)
092, [1609.00708].
[40] D. Ghoshal and C. Vafa, c = 1 string as the topological theory of the conifold, Nucl. Phys. B 453
(1995) 121–128, [hep-th/9506122].
[41] R. Gopakumar and C. Vafa, On the gauge theory / geometry correspondence, Adv. Theor. Math.
Phys. 3 (1999) 1415–1443, [hep-th/9811131].
[42] M. Mari˜no and S. Zakany, Matrix models from operators and topological strings, Annales Henri
Poincar´e 17 (2016) 1075–1108, [1502.02958].
[43] R. Kashaev, M. Mari˜no and S. Zakany, Matrix models from operators and topological strings, 2,
Annales Henri Poincar´e 17 (2016) 2741–2781, [1505.02243].
[44] I. Aniceto, G. Ba¸sar and R. Schiappa, A primer on resurgent transseries and their asymptotics,
Phys. Rep. 809 (2019) 1–135.
[45] C. Mitschi and D. Sauzin, Divergent series, summability and resurgence. I, vol. 2153 of Lecture
Notes in Mathematics. Springer, 2016, 10.1007/978-3-319-28736-2.
[46] M. Mari˜no, Instantons and large N. An introduction to non-perturbative methods in quantum ﬁeld
theory. Cambridge University Press, 2015.
[47] E. Witten, Analytic Continuation Of Chern-Simons Theory, AMS/IP Stud. Adv. Math. 50 (2011)
347–446, [1001.2933].
[48] S. Garoufalidis and D. Zagier, Knots, perturbative series and quantum modularity, 2111.06645.
[49] S. Garoufalidis, Chern-Simons theory, analytic continuation and arithmetic, 0711.1716.
[50] S. Garoufalidis, J. Gu, M. Mari˜no and C. Wheeler, Resurgence of Chern-Simons theory at the
trivial ﬂat connection, 2111.04763.
[51] R. Lawrence and D. Zagier, Modular forms and quantum invariants of 3-manifolds, Asian Journal
of Mathematics 3 (1999) 93–108.
[52] K. Hikami, On the quantum invariants for the spherical Seifert manifolds, Communications in
Mathematical Physics 268 (2006) 285–319.
[53] K. Hikami, Decomposition of Witten-Reshetikhin-Turaev invariant: Linking pairing and modular
forms, AMS/IP Stud. Adv. Math. 50 (2011) 131–151.
[54] S. Gukov, P. Putrov and C. Vafa, Fivebranes and 3-manifold homology, JHEP 07 (2017) 071,
[1602.05302].
[55] S. Gukov, M. Mari˜no and P. Putrov, Resurgence in complex Chern-Simons theory, 1605.07615.
– 49 –
[56] S. Gukov, D. Pei, P. Putrov and C. Vafa, BPS spectra and 3-manifold invariants, J. Knot Theor.
Ramiﬁcations 29 (2020) 2040003, [1701.06567].
[57] J. E. Andersen and W. E. Misteg˚ard, Resurgence Analysis of Quantum Invariants of Seifert Fibered
Homology Spheres, 1811.05376.
[58] M. Mari˜no, Spectral Theory and Mirror Symmetry, Proc. Symp. Pure Math. 98 (2018) 259,
[1506.07757].
[59] R. Kashaev and M. Mari˜no, Operators from mirror curves and the quantum dilogarithm, Commun.
Math. Phys. 346 (2016) 967, [1501.01014].
[60] R. Couso-Santamar´ıa, M. Mari˜no and R. Schiappa, Resurgence matches quantization, J. Phys. A50
(2017) 145402, [1610.06782].
[61] X. Wang, G. Zhang and M.-x. Huang, New exact quantization condition for toric Calabi–Yau
geometries, Phys. Rev. Lett. 115 (2015) 121601, [1505.05360].
[62] Y. Hatsuda and M. Mari˜no, Exact quantization conditions for the relativistic Toda lattice, JHEP
05 (2016) 133, [1511.02860].
[63] S. Franco, Y. Hatsuda and M. Mari˜no, Exact quantization conditions for cluster integrable systems,
J. Stat. Mech. 1606 (2016) 063107, [1512.03061].
[64] K. Sun, X. Wang and M.-x. Huang, Exact Quantization Conditions, Toric Calabi-Yau and
Nonperturbative Topological String, JHEP 01 (2017) 061, [1606.07330].
[65] A.-K. Kashani-Poor, Quantization condition from exact WKB for diﬀerence equations, JHEP 06
(2016) 180, [1604.01690].
[66] R. M. Kashaev and S. M. Sergeev, Spectral equations for the modular oscillator, Rev. Math. Phys.
30 (2018) 1840009, [1703.06016].
[67] R. Kashaev and S. Sergeev, On the Spectrum of the Local P2 Mirror Curve, Annales Henri
Poincare 21 (2020) 3479–3497, [1904.12315].
[68] A. Grassi and M. Mari˜no, The complex side of the TS/ST correspondence, J. Phys. A 52 (2019)
055402, [1708.08642].
[69] S. Gukov, Three-dimensional quantum gravity, Chern-Simons theory, and the A polynomial,
Commun. Math. Phys. 255 (2005) 577–627, [hep-th/0306165].
[70] R. M. Kashaev, The Hyperbolic volume of knots from quantum dilogarithm, Lett. Math. Phys. 39
(1997) 269–275.
[71] P. L. del ´Angel R., C. Doran, M. Kerr, J. Lewis, J. Iyer, S. M¨uller-Stach et al., Specialization of
cycles and the K-theory elevator, Commun. Number Theory Phys. 13 (2019) 299–349.
[72] S. Pasquetti, Factorisation of N = 2 Theories on the Squashed 3-Sphere, JHEP 04 (2012) 120,
[1111.6905].
[73] C. Beem, T. Dimofte and S. Pasquetti, Holomorphic Blocks in Three Dimensions, JHEP 12 (2014)
177, [1211.1986].
[74] T. Dimofte, Complex Chern-Simons theory at level k via the 3d-3d correspondence, Comm. Math.
Phys. 339 (2015) 619–662.
[75] S. Garoufalidis and R. Kashaev, From state integrals to q-series, Math. Res. Lett. 24 (2017)
781–801.
[76] Y. Terashima and M. Yamazaki, SL(2,R) Chern-Simons, Liouville, and Gauge Theory on Duality
Walls, JHEP 08 (2011) 135, [1103.5748].
[77] E. Witten, Quantum background independence in string theory, hep-th/9306122.
[78] G. Bonelli, A. Grassi and A. Tanzini, Seiberg–Witten theory as a Fermi gas, Lett. Math. Phys. 107
(2017) 1–30, [1603.01174].
[79] G. Bonelli, A. Grassi and A. Tanzini, Quantum curves and q-deformed Painlev´e equations, Lett.
Math. Phys. 109 (2019) 1961–2001, [1710.11603].
– 50 –
[80] M. Alim, Intrinsic non-perturbative topological strings, 2102.07776.
[81] G. Bonelli, F. Del Monte and A. Tanzini, BPS quivers of ﬁve-dimensional SCFTs, Topological
Strings and q-Painlev´e equations, 2007.11596.
[82] I. Coman, E. Pomoni and J. Teschner, From quantum curves to topological string partition
functions, 1811.01978.
[83] I. Coman, P. Longhi and J. Teschner, From quantum curves to topological string partition functions
II, 2004.04585.
[84] M. Bershadsky, S. Cecotti, H. Ooguri and C. Vafa, Holomorphic anomalies in topological ﬁeld
theories, Nucl.Phys. B405 (1993) 279–304, [hep-th/9302103].
[85] M. Bershadsky, S. Cecotti, H. Ooguri and C. Vafa, Kodaira–Spencer theory of gravity and exact
results for quantum string amplitudes, Commun. Math. Phys. 165 (1994) 311–428,
[hep-th/9309140].
[86] B. Haghighat, A. Klemm and M. Rauch, Integrability of the holomorphic anomaly equations, JHEP
0810 (2008) 097, [0809.1674].
[87] C. Hunter and B. Guerrieri, Deducing the properties of singularities of functions from their Taylor
series coeﬃcients, SIAM Journal on Applied Mathematics 39 (1980) 248–263,
[https://doi.org/10.1137/0139022].
[88] N. Takayama, Gr¨obner basis, integration and transcendental functions, in Proceedings of the
International Symposium on Symbolic and Algebraic Computation, ISSAC ’90, (New York, NY,
USA), pp. 152–156, Association for Computing Machinery, 1990. DOI.
[89] N. Takayama, An algorithm of constructing the integral of a module–an inﬁnite dimensional analog
of Gr¨obner basis, in Proceedings of the International Symposium on Symbolic and Algebraic
Computation, ISSAC ’90, (New York, NY, USA), pp. 206–211, Association for Computing
Machinery, 1990. DOI.
[90] C. Koutschan, HolonomicFunctions (user’s guide), Tech. Rep. 10-01, 2010.
[91] C. Koutschan, Advanced Applications of the Holonomic Systems Approach. PhD thesis, RISC,
Johannes Kepler University, Linz, Austria, 2009.
[92] O. Costin and G. V. Dunne, Resurgent extrapolation: rebuilding a function from asymptotic data.
Painlev´e I, J. Phys. A52 (2019) 445205, [1904.11593].
[93] O. Costin and G. V. Dunne, Physical Resurgent Extrapolation, Phys. Lett. B 808 (2020) 135627,
[2003.07451].
[94] M.-x. Huang, A. Klemm and S. Quackenbush, Topological string theory on compact Calabi-Yau:
Modularity and boundary conditions, Lect. Notes Phys. 757 (2009) 45–102, [hep-th/0612125].
[95] S. Pasquetti and R. Schiappa, Borel and Stokes nonperturbative phenomena in topological string
theory and c = 1 matrix models, Annales Henri Poincar´e 11 (2010) 351–431, [0907.4082].
[96] L. Faddeev, Discrete Heisenberg-Weyl group and modular group, Lett.Math.Phys. 34 (1995)
249–254, [hep-th/9504111].
[97] L. Faddeev and R. Kashaev, Quantum Dilogarithm, Mod.Phys.Lett. A9 (1994) 427–434,
[hep-th/9310070].
[98] G. Darboux, M´emoire sur l’approximation des fonctions de tr`es-grands nombres, et sur une classe
´etendue de d´eveloppements en s´erie., Journal de Math´ematiques pures et appliqu´ees (1878) 5–56.
[99] P. Henrici, Applied and computational complex analysis. Vol. 1. Wiley Classics Library. John Wiley
& Sons, Inc., New York, 1988.
– 51 –
