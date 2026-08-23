---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-050-c-convention-convention
section_title: "C Convention convention"
section_number: null
pages: 82-87
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
We summarize here some conventions used in this and our preceding papers.
1. Homology classes on the IR (Seiberg-Witten) curve Σ are denoted in this paper
by ¯a∈ Γij′(z,z′). In our previous paper [5] they were denoted by γij′. They are
represented by paths oriented from z(i) to z′(j′). Thus ∂γij′ = z′(j′)−z(i). The
sum γij′ +γj′k′′∈ Γik′′ is thus oriented from z(i) to z′′(k′′). Note that the + is not
commutative: the sum in the opposite order γj′k′′ +γij′ in general does not make
sense.
2. Oriented open paths on the UV curve C are generally denoted by ℘, and often the
initial point is z1 and the ﬁnal point is z2. If ℘′ is another such path, with initial and
ﬁnal points z′
1 andz′
2, respectively, andz2 =z′
1 and moreover the canonical lifts of ℘
and ℘′ to ˜C can be concatenated, then we denote by ℘℘′ the composed path, which
goes from z1 to z′
2. Note the “later” path is written to the right.
3. Zγ = 1
π
∮
γλ is the central charge of a 4d state, Z¯a = 1
π
∫
¯aλ is the central charge of a
2d soliton for ¯a∈ Γij(z,z ), i⁄=j, and the same expression is also the central charge
of a framed 2d-4d state with ¯a∈ Γ(z1,z 2). If ¯a∈ Γij(z1,z 2) we can regard Z¯a as a
function onUi×Uj, whereUi is a suﬃciently small open region around z(i)
1 andUj is
a suﬃciently small open region around z(j)
2 . In this case d Z¯a = 1
π(λ(j)−λ(i)).
4. For an ordered pair ( i,j ) of sheets, BPS walls of type ij are deﬁned by e−iϑZγij < 0
with µ(γij)⁄= 0. Therefore they are oriented on C so that e−iϑ⟨λ(i)−λ(j),∂t⟩ > 0,
where ∂t is a tangent vector to the wall in the direction of the orientation. Note
that this implies that the integral e−iϑ∫z(t)λ(i)−λ(j) =−e−iϑ∫
γij
λ increases asz(t)
moves along the direction of the orientation of the wall.
5. The mass of a soliton with charge ¯a∈ Γij(z,z ) is M(z) =−e−iϑ
π
∫
¯aλ.
6. Lifting to the circle bundle of directions in the tangent bundle is denoted by a tilde.
Thus ˜Σ is the circle bundle of tangent directions over Σ, and so forth.
– 80 –
7. F (℘,ϑ ), F(℘,W) and F( ˜℘,W,∇ab) all compose in the same way we compose paths
in item 2 above: F (℘,·)F (℘′,·) =F (℘℘′,·).
8. The parallel transport F( ˜℘,W,∇ab)∈ Hom(E˜z1,E ˜z2) if ℘ goes from z1 to z2. In [5]
ˆE was denoted by V ,Li was denoted by Vi, and F (℘,Wϑ,∇ab) was denoted ⟨L℘⟩
and expanded in Yγij′∈ Hom(Li,Lj′). (The conventions of §5 of [5] are opposite to
those of§§7-9 of [5]; we use the conventions of §§7-9.)
9. We compose linear transformations on the right so that the composition of linear op-
erators T1∈ Hom(V1,V 2) and T2∈ Hom(V2,V 3) is written T1T2∈ Hom(V1,V 3). The
parallel transport of a section s(z) from z1 to z2 by the connection∇ = ΨW(∇ab) is
thus given bys(z2) =s(z1)F( ˜℘,W,∇ab). This diﬀers from the more usual convention
and in particular diﬀers from [5]. In a local trivialization we can write this as
s(z2) =s(z1)Pexp
(
−
∫ z2
z1
A
)
(C.1)
whereA is the gl(K, C)-valued 1-form representing∇.
10. In [5], equations (5.31) and (5.32), we introduced ﬂat sectionsYγij′(z,z′) of the vector
bundle ˆE∗⊗ ˆE onC×C obtained by projection and parallel transport. For a homology
class a∈ Γ(˜z, ˜z′) connecting ˜z(i) and ˜z′(j′) we deﬁneYa to be parallel transport with
respect to ∇ab along a from ˜z(i) to ˜z′(j′). The two notions coincide for z,z′ away
fromS-walls if we make use of the isomorphism (10.10). From either point of view
we have, in local coordinates
∂zYγij′−AzYγij′ = 0,
∂z′Yγij′ +Yγij′Az′ = 0.
(C.2)
11. The map between solutions ( ϕ,A ) of Hitchin equations and ﬂat connections A (used
in [3, 5, 17, 21] although not in this paper) is A = R
ζϕ +A +Rζϕ.
12. The WKB asymptotics of ﬂat sections are formally given by
Yγij∼ expπR
ζ Zγij +··· (C.3)
This implies that if ζ lies in the half-plane Hϑ, thenYγij(z) is exponentially small as
ζ→ 0 when z lies on a wall of type ij supporting the charge γij.
Acknowledgements
We would like to thank P. Boalch, T. Bridgeland, A. Goncharov, N. Hitchin, S. Keel, I.
Smith and E. Witten for discussions, and T. Mainiero for pointing out several typos in a
previous preprint version.
GM and AN thank the KITP for hospitality, where some of this work was done.
GM would also like to thank the Institute for Advanced Study and the Ambrose Monell
– 81 –
Foundation for partial support during part of this research. This research was supported
in part by DARPA under grant HR0011-09-1-0015 and by the NSF under grant PHY05-
51164. The work of DG is supported in part by NSF grant PHY-0969448 and in part by
the Roger Dashen membership in the Institute for Advanced Study. The work of GM is
supported by the DOE under grant DE-FG02-96ER40959. The work of AN is supported
by the NSF under grant DMS-1006046.
References
[1] E. Witten, “Solutions of four-dimensional ﬁeld theories via M-theory,” Nucl. Phys. B500
(1997) 3–42, hep-th/9703166.
[2] D. Gaiotto, “N = 2 dualities,” 0904.2715.
[3] D. Gaiotto, G. W. Moore, and A. Neitzke, “Wall-crossing, Hitchin Systems, and the WKB
Approximation,” 0907.3987.
[4] D. Gaiotto, “Surface Operators in N = 2 4d Gauge Theories,” 0911.1316.
[5] D. Gaiotto, G. W. Moore, and A. Neitzke, “Wall-Crossing in Coupled 2d-4d Systems,”
1103.2598v1.
[6] A. Klemm, W. Lerche, P. Mayr, C. Vafa, and N. P. Warner, “Self-dual strings and N = 2
supersymmetric ﬁeld theory,” Nucl. Phys. B477 (1996) 746–766, hep-th/9604034.
[7] A. Brandhuber and S. Stieberger, “Self-dual strings and stability of BPS states in N = 2
SU (2) gauge theories,” Nucl. Phys. B488 (1997) 199–222, hep-th/9610053.
[8] O. Aharony, A. Hanany, and B. Kol, “Webs of ( p,q ) 5-branes, ﬁve dimensional ﬁeld theories
and grid diagrams,” JHEP 01 (1998) 002, hep-th/9710116.
[9] M. Kontsevich and Y. Soibelman, “Stability structures, motivic Donaldson-Thomas
invariants and cluster transformations,” 0811.2435.
[10] M. Alim, S. Cecotti, C. Cordova, S. Espahbodi, A. Rastogi, and C. Vafa, “BPS Quivers and
Spectra of CompleteN = 2 Quantum Field Theories,” 1109.4941.
[11] M. Alim, S. Cecotti, C. Cordova, S. Espahbodi, A. Rastogi, and C. Vafa, “ N = 2 Quantum
Field Theories and Their BPS Quivers,” 1112.3984.
[12] V. V. Fock and A. B. Goncharov, “Cluster ensembles, quantization and the dilogarithm,”
Ann. Sci. ´Ec. Norm. Sup´ er. (4)42 (2009), no. 6, 865–930, math/0311245.
[13] V. Fock and A. Goncharov, “Moduli spaces of local systems and higher Teichm¨ uller theory,”
Publ. Math. Inst. Hautes ´Etudes Sci. (2006), no. 103, 1–211, math/0311149.
[14] V. V. Fock and A. B. Goncharov, “The quantum dilogarithm and representations of
quantum cluster varieties,” math/0702397.
[15] A. Goncharov. To appear.
[16] N. J. Hitchin, “The self-duality equations on a Riemann surface,” Proc. London Math. Soc.
(3) 55 (1987), no. 1, 59–126.
[17] D. Gaiotto, G. W. Moore, and A. Neitzke, “Four-dimensional wall-crossing via
three-dimensional ﬁeld theory,” Commun. Math. Phys. 299 (2010) 163–224, 0807.4723.
– 82 –
[18] ´E. Delabaere, H. Dillinger, and F. Pham, “R´ esurgence de Voros et p´ eriodes des courbes
hyperelliptiques,” Ann. Inst. Fourier (Grenoble) 43 (1993), no. 1, 163–199.
[19] A. Voros, “The return of the quartic oscillator: the complex WKB method,” Ann. Inst. H.
Poincar´ e Sect. A (N.S.)39 (1983), no. 3, 211–338.
[20] T. Aoki, T. Kawai, S. Sasaki, A. Shudo, and Y. Takei, “Virtual turning points and
bifurcation of Stokes curves for higher order ordinary diﬀerential equations,” J. Phys. A 38
(2005), no. 15, 3317–3336, math-ph/0409005.
[21] D. Gaiotto, G. W. Moore, and A. Neitzke, “Framed BPS States,” 1006.0146v1.
[22] A. Zorich, “Flat surfaces,” math/0609392.
[23] M. Kontsevich and Y. Soibelman, “Aﬃne structures and non-Archimedean analytic spaces,”
in The unity of mathematics , vol. 244 of Progr. Math., pp. 321–385. Birkh¨ auser Boston,
Boston, MA, 2006. math.ag/0406564.
[24] D. Auroux, “Mirror symmetry and T -duality in the complement of an anticanonical divisor,”
J. G¨ okova Geom. Topol. GGT1 (2007) 51–91.
[25] M. Gross and B. Siebert, “From real aﬃne geometry to complex geometry,” math/0703822.
[26] M. Gross, R. Pandharipande, and B. Siebert, “The tropical vertex,” 0902.0779.
[27] M. Gross, P. Hacking, and S. Keel, “Mirror symmetry for log Calabi-Yau surfaces I,”
1106.4977.
[28] C. Fraser and T. J. Hollowood, “On the weak coupling spectrum of N=2 supersymmetric
SU(n) gauge theory,” Nucl.Phys. B490 (1997) 217–238, hep-th/9610142.
[29] B. J. Taylor, “On the strong coupling spectrum of pure SU(3) Seiberg-Witten theory,”
JHEP 0108 (2001) 031, hep-th/0107016.
[30] B. J. Taylor, “On the moduli space of SU(3) Seiberg-Witten theory with matter,” JHEP
0212 (2002) 040, hep-th/0211086.
[31] H.-Y. Chen, N. Dorey, and K. Petunin, “Moduli Space and Wall-Crossing Formulae in
Higher-Rank Gauge Theories,” JHEP 1111 (2011) 020, 1105.4584.
[32] D. Gaiotto, G. W. Moore, and A. Neitzke, “Spectral networks and snakes.” To appear.
[33] L. F. Alday, D. Gaiotto, S. Gukov, Y. Tachikawa, and H. Verlinde, “Loop and surface
operators in N=2 gauge theory and Liouville modular geometry,” JHEP 1001 (2010)
0909.0945.
[34] T. Dimofte, S. Gukov, and Y. Soibelman, “Quantum Wall Crossing in N=2 Gauge
Theories,” 0912.1346.
[35] S. Cecotti and C. Vafa, “BPS Wall Crossing and Topological Strings,” 0910.2615.
[36] S. Cecotti and C. Vafa, “2d Wall-Crossing, R-twisting, and a Supersymmetric Index,”
1002.3638.
[37] S. Cecotti, P. Fendley, K. A. Intriligator, and C. Vafa, “A new supersymmetric index,”
Nucl.Phys. B386 (1992) 405–452, hep-th/9204102.
[38] S. Cecotti and C. Vafa, “On classiﬁcation of N = 2 supersymmetric theories,” Commun.
Math. Phys. 158 (1993) 569–644, hep-th/9211097.
[39] D. Gaiotto and E. Witten, “Knot invariants from four-dimensional gauge theory,”
– 83 –
1106.4789.
[40] F. Denef and G. W. Moore, “Split states, entropy enigmas, holes and halos,” JHEP 1111
(2011) hep-th/0702146.
[41] E. Andriyash, F. Denef, D. L. Jaﬀeris, and G. W. Moore, “Bound state transformation
walls,” 1008.3555.
[42] E. Andriyash, F. Denef, D. L. Jaﬀeris, and G. W. Moore, “Wall-crossing from
supersymmetric galaxies,” JHEP 1201 (2012) 1008.0030.
[43] D. Gaiotto, G. W. Moore, and A. Neitzke, “Spectral network movies.” Viewable at
http://www.ma.utexas.edu/users/neitzke/spectral-network-movies/ as of April 2012.
[44] K. Strebel, Quadratic diﬀerentials, vol. 5 of Ergebnisse der Mathematik und ihrer
Grenzgebiete (3) [Results in Mathematics and Related Areas (3)] . Springer-Verlag, Berlin,
1984.
[45] N. Seiberg and E. Witten, “Electric-magnetic duality, monopole condensation, and
conﬁnement inN = 2 supersymmetric Yang-Mills theory,” Nucl. Phys. B426 (1994) 19–52,
hep-th/9407087.
[46] D. Galakhov, P. Longhi, T. Mainiero, G. W. Moore, and A. Neitzke, “Wild Wall Crossing
and BPS Giants,” 1305.5454.
[47] A. D. Shapere and C. Vafa, “BPS structure of Argyres-Douglas superconformal theories,”
hep-th/9910182.
[48] S. Cecotti, A. Neitzke, and C. Vafa, “R-Twisting and 4d/2d Correspondences,” 1006.3435.
[49] R. Donagi, “Spectral covers,” in Current topics in complex algebraic geometry (Berkeley,
CA, 1992/93), vol. 28 of Math. Sci. Res. Inst. Publ. , pp. 65–86. Cambridge Univ. Press,
Cambridge, 1995.
[50] R. Donagi and D. Gaitsgory, “The gerbe of Higgs bundles,” math/0005132.
[51] M. F. Atiyah and R. Bott, “The Yang-Mills equations over Riemann surfaces,” Philos.
Trans. Roy. Soc. London Ser. A 308 (1983), no. 1505, 523–615.
[52] P. P. Boalch, Symplectic Geometry and Isomonodromic Deformations . PhD thesis, Wadham
College, Oxford, 1999.
[53] S. Alexandrov, D. Persson, and B. Pioline, “Wall-crossing, Rogers dilogarithm, and the
QK/HK correspondence,” JHEP 1112 (2011) 1110.0466.
[54] S. Cecotti and M. Del Zotto, “On Arnold’s 14 ‘exceptional’ N = 2 superconformal gauge
theories,” JHEP 1110 (2011) 099, 1107.5747.
[55] M. F. Atiyah, The geometry and physics of knots . Lezioni Lincee. [Lincei Lectures].
Cambridge University Press, Cambridge, 1990.
[56] K. Corlette, “Flat G-bundles with canonical metrics,” J. Diﬀerential Geom. 28 (1988), no. 3,
361–382.
[57] S. K. Donaldson, “Twisted harmonic maps and the self-duality equations,” Proc. London
Math. Soc. (3) 55 (1987), no. 1, 127–131.
[58] C. Simpson, “Harmonic bundles on noncompact curves,” J. Amer. Math. Soc. 3 (1990)
713–770.
[59] O. Biquard and P. Boalch, “Wild nonabelian Hodge theory on curves,” math/0111098.
– 84 –
[60] C. M. Bender and T. T. Wu, “Anharmonic oscillator,” Phys. Rev. 184 (1969) 1231–1260.
[61] J. Zinn-Justin, “Instantons in quantum mechanics: Numerical evidence for a conjecture,” J.
Math. Phys. 25 (1984) 549.
[62] H. L. Berk, W. M. Nevins, and K. V. Roberts, “New Stokes’ line in WKB theory,” Journal
of Mathematical Physics 23 (1982), no. 6, 988–1002.
[63] C. Simpson, “Asymptotics for general connections at inﬁnity,” math/0311531.
[64] C. Simpson, Asymptotic behavior of monodromy , vol. 1502 of Lecture Notes in Mathematics .
Springer-Verlag, Berlin, 1991.
– 85 –
