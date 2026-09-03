---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model"
section_id: sec-010-acknowledgmets
section_title: "Acknowledgmets"
section_number: null
pages: 40-44
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
doc_brief: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model — 11 sections: Introduction; The Lagrangian and Euler-Lagrange ; Radial reduction"
---
This study was financed in part by the Coordena¸ c˜ ao de Aperfei¸ coamento de Pessoal de N´ ıvel
Superior – Brasil (CAPES) – Finance Code 001. N.S. was supported in part by JSPS KAKENHI
Grant No. JP23K02794. L.R.L. is supported by the grant 2025/20538-2, S˜ ao Paulo Research
Foundation (FAPESP).
Appendix A
Many simplifications follow directly from the addition theorem for spherical harmonics:
Pl(cosγ) = 4π
2l+ 1
lX
m=−l
Y∗
lm(θ′,ϕ′)Ylm(θ,ϕ),
where cosγ= cosθcosθ ′ + sinθsinθ ′ cos(ϕ−ϕ ′). In particular, whenθ=θ ′ andϕ=ϕ ′ (which
impliesγ= 0), this equality yields
lX
m=−l
(l−m)!
(l+m) [Pl(cosθ)] 2 = 1.
Taking the derivative with respect toθon both sides of the last equality gives
lX
m=−l
(l−m)!
(l+m) Pl(cosθ)∂θPl(cosθ) = 0.(A.1)
Applying the ansatz from equation (II.13)results in the following expressions:
u†·∂tu=iωf 2 u†·∂ru=f ′f u †·∂θu= 0u †·∂ϕu= 0
∂θu†·∂θu= l(l+ 1)
2 f 2 ∂ru†·∂ru=f ′2 ∂tu†·∂ru=−iωf ′f ∂ θu†·∂ϕu= 0
∂ϕu†·∂ϕu= l(l+ 1)
2 sin2θf 2 ∂tu†·∂tu=ω 2f 2 ∂ru†·∂αu= 0∂ tu†·∂αu= 0
41
Appendix B
The expressions forK σ are given by:
K(m)
σ :=u∗
m
lX
m′=−l
∆2
mm′∂σum′ (B.1)
=u∗
m
lX
m′=−l
h
(1 +u†·u)δmm′−umu∗
m′
i
∂σum′
= (1 +u†·u)u ∗
m∂σum−|um|2
lX
m′=−l
u∗
m′∂σum′.(B.2)
Expression (B.1) is more convenient when∂ tum′ =iωu m′ and∂ rum′ = f′
fum′, asu ′
m is an eigen-
vector of the matrix ∆ 2
mm′um′, with an eigenvalue ofλ= 1. For the case whereσ=θ, the
term Pl
m′=−lu∗
m′∂θum′ vanishes according to equation (A.1). Similarly, forσ=ϕ, one obtainsPl
m′=−lu∗
m′∂ϕum′ =i Pl
m′=−l|um′|2 = 0. In these instances, it is more convenient to apply ex-
pression (B.2). This leads to the following results:
K(m)
t =iωf 2 (l−m)!
(l+m)! (Pm
l )2,
K(m)
r =f′f (l−m)!
(l+m)! (Pm
l )2,
K(m)
θ =f 2(1 +f 2)(l−m)!
(l+m)! Pm
l ∂θPm
l ,
K(m)
ϕ =imf 2(1 +f 2)(l−m)!
(l+m)! (Pm
l )2.
Appendix C
The sum Pl
m=−lωQ(m)
t is given by a radial integral, and this quantity can be expressed as a
volume integral of some density. This yields:
lX
m=−l
ωQ(m)
t =
Z
R3
d3ξ√−g
"
A
z }| {
4ω2f 2
(1 +f 2)2 +κ 4ω2f 2
(1 +f 2)2F1 +
C
z }| {
κ 12ω2f′f
(1 +f 2)2F3
#
(C.1)
A similar approach provides the expression for Pl
m=−lmQ(m)
ϕ in the form:
lX
m=−l
mQ(m)
ϕ =
Z
R3
d3ξ√−g
"
B
z }| {
l(l+ 1)
r2
4f 2
1 +f 2−κl(l+ 1)
r2
4f 2
1 +f 2F4
#
.(C.2)
42
The total energy is given by:
E=
Z
R3
d3ξ√−g
"
A
z }| {
4ω2f 2
(1 +f 2)2 +
B
z }| {
l(l+ 1)
r2
4f 2
1 +f 2
#
+
Z
R3
d3ξ√−g
 4f′2
(1 +f 2)2 + ˜µ2V

+
Z
R3
d3ξ√−g
"
κ 6ω2f 2
(1 +f 2)2F1(r)−κ 2f′2
(1 +f 2)2F2(r)
+
C
z }| {
κ 12ω2f′f
(1 +f 2)2F3(r)−κl(l+ 1)
r2
2f 2
1 +f 2F4(r)
#
(C.3)
This can also be cast in the form:
E=
lX
m=−l

ωQ(m)
t +mQ (m)
ϕ

+
Z
R3
d3ξ√−g
 4f′2
(1 +f 2)2 + ˜µ2V

+
Z
R3
d3ξ√−g
"
κ 2ω2f 2
(1 +f 2)2F1−κ 2f′2
(1 +f 2)2F2 +κ l(l+ 1)
r2
2f 2
1 +f 2F4
#
.(C.4)
[1] Peter W. Higgs, “Broken symmetries and the masses of gauge bosons,” Phys. Rev. Lett.13, 508–509
(1964).
[2] V. L. Ginzburg and L. D. Landau, “On the Theory of superconductivity,” Zh. Eksp. Teor. Fiz.20,
1064–1082 (1950).
[3] WJ Zakrzewski, Low dimensional sigma models, Tech. Rep. (Los Alamos National Laboratory (LANL),
Los Alamos, NM (United States), 1988).
[4] L. D. Faddeev, “Quantization of Solitons,” in 18th International Conference on High-Energy Physics
(1975).
[5] L. D. Faddeev, 40 years in mathematical physics (1995).
[6] Richard A. Battye and Paul M. Sutcliffe, “Knots as stable soliton solutions in a three-dimensional
classical field theory.” Phys. Rev. Lett.81, 4798–4801 (1998), arXiv:hep-th/9808129.
[7] Paul Sutcliffe, “Knots in the Skyrme-Faddeev model,” Proc. Roy. Soc. Lond. A463, 3001–3020 (2007),
arXiv:0705.1468 [hep-th].
[8] L. D. Faddeev and Antti J. Niemi, “Partial duality in SU(N) Yang-Mills theory,” Phys. Lett. B449,
214–218 (1999), arXiv:hep-th/9812090.
[9] Holger Gies, “Wilsonian effective action for SU(2) Yang-Mills theory with Cho-Faddeev-Niemi-
Shabanov decomposition,” Phys. Rev. D63, 125023 (2001), arXiv:hep-th/0102026.
[10] L. A. Ferreira, “Exact vortex solutions in an extended Skyrme-Faddeev model,” JHEP05, 001 (2009),
arXiv:0809.4303 [hep-th].
[11] L. D. Faddeev and Antti J. Niemi, “Decomposing the Yang-Mills field,” Phys. Lett. B464, 90–93
(1999), arXiv:hep-th/9907180.
[12] Kei-Ichi Kondo, Toru Shinohara, and Takeharu Murakami, “Reformulating SU(N) Yang-Mills theory
based on change of variables,” Prog. Theor. Phys.120, 1–50 (2008), arXiv:0803.0176 [hep-th].
[13] L. A. Ferreira and P. Klimas, “Exact vortex solutions in aCP N Skyrme-Faddeev type model,” JHEP
10, 008 (2010), arXiv:1007.1667 [hep-th].
43
[14] L. A. Ferreira, P. Klimas, and W. J. Zakrzewski, “Some properties of (3+1) dimensional vortex solutions
in the extendedCP N Skyrme-Faddeev model,” JHEP12, 098 (2011), arXiv:1111.2338 [hep-th].
[15] L. A. Ferreira, J. Jaykka, Nobuyuki Sawado, and Kouichi Toda, “Vortices in the Extended Skyrme-
Faddeev Model,” Phys. Rev. D85, 105006 (2012), arXiv:1112.1085 [hep-th].
[16] Nobuyuki Sawado and Yuta Tamaki, “Exact, molecular-shaped vortices with fractional and integer
charges in the extended Skyrme-Faddeev model,” (2013), arXiv:1309.6004 [hep-th].
[17] Yuki Amari, Pawel Klimas, Nobuyuki Sawado, and Yuta Tamaki, “Potentials and the vortex solutions
in theCP N Skyrme-Faddeev model,” Phys. Rev. D92, 045007 (2015), arXiv:1504.02848 [hep-th].
[18] T.D Lee and Y Pang, “Nontopological solitons,” Physics Reports221, 251–350 (1992).
[19] G. H. Derrick, “Comments on nonlinear wave equations as models for elementary particles,” J. Math.
Phys.5, 1252–1254 (1964).
[20] T. D. Lee and Y. Pang, “Nontopological solitons,” Phys. Rept.221, 251–350 (1992).
[21] Gerald Rosen, “Particlelike Solutions to Nonlinear Complex Scalar Field Theories with Positive-Definite
Energy Densities,” J. Math. Phys.9, 996 (1968).
[22] J. Werle, “Dirac Spinor Solitons Or Bags,” Phys. Lett. B71, 357–359 (1977).
[23] H. Arodz, P. Klimas, and T. Tyranowski, “Field-theoretic models with V-shaped potentials,” Acta
Phys. Polon. B36, 3861–3876 (2005), arXiv:hep-th/0510204.
[24] H. Arodz, P. Klimas, and T. Tyranowski, “Scaling, self-similar solutions and shock waves for V-shaped
field potentials,” Phys. Rev. E73, 046609 (2006), arXiv:hep-th/0511022.
[25] H. Arodz and J. Lis, “Compact Q-balls in the complex signum-Gordon model,” Phys. Rev. D77,
107702 (2008), arXiv:0803.1566 [hep-th].
[26] H. Arodz, J. Karkowski, and Z. Swierczynski, “Spinning Q-balls in the complex signum-Gordon model,”
Phys. Rev. D80, 067702 (2009), arXiv:0907.2801 [hep-th].
[27] H. Arodz and J. Lis, “Compact Q-balls and Q-shells in a scalar electrodynamics,” Phys. Rev. D79,
045002 (2009), arXiv:0812.3284 [hep-th].
[28] R. D. Richtmyer, Principles of Advanced Mathematical Physics (Springer Verlag, Berlin, 1978) Chap.
17.3.
[29] L. C. Evans, Partial Differential Equations (American Mathematical Society, Providence, 1998).
[30] P. Tchofo Dinda and M. Remoissenet, “Breather compactons in nonlinear klein-gordon systems,” Phys.
Rev. E60, 6218–6221 (1999).
[31] C. Adam, J. Sanchez-Guillen, and A. Wereszczynski, “A Skyrme-type proposal for baryonic matter,”
Phys. Lett. B691, 105–110 (2010), arXiv:1001.4544 [hep-th].
[32] Betti Hartmann, Burkhard Kleihaus, Jutta Kunz, and Isabell Schaffer, “Compact (A)dS Boson Stars
and Shells,” Phys. Rev. D88, 124033 (2013), arXiv:1310.3632 [gr-qc].
[33] H. Arodz, P. Klimas, and T. Tyranowski, “Compact oscillons in the signum-Gordon model,” Phys.
Rev. D77, 047701 (2008), arXiv:0710.2244 [hep-th].
[34] C. Adam, D. Foster, S. Krusch, and A. Wereszczynski, “BPS sectors of the Skyrme model and their
non-BPS extensions,” Phys. Rev. D97, 036002 (2018), arXiv:1709.06583 [hep-th].
[35] P. Klimas, J. S. Streibel, A. Wereszczynski, and W. J. Zakrzewski, “Oscillons in a perturbed signum-
Gordon model,” JHEP04, 102 (2018), arXiv:1801.05454 [hep-th].
[36] P. Klimas and L. R. Livramento, “Compact Q-balls and Q-shells in CPN type models,” Phys. Rev. D
96, 016001 (2017), arXiv:1704.01132 [hep-th].
[37] Luiz A. Ferreira and Erica E. Leite, “Integrable theories in any dimension and homogeneous spaces,”
Nucl. Phys. B547, 471–500 (1999), arXiv:hep-th/9810067.
[38] H. Eichenherr and M. Forger, “More about non-linear sigma models on symmetric spaces,” Nuclear
Physics B164, 528–535 (1980).
44
[39] L. A. Ferreira and David I. Olive, “Noncompact Symmetric Spaces and the Toda Molecule Equations,”
Commun. Math. Phys.99, 365 (1985).
