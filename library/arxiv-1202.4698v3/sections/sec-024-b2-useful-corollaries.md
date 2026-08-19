---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-024-b2-useful-corollaries
section_title: "B.2 Useful corollaries."
section_number: null
pages: 25-32
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
For proving the main transformation formula which allows us to get from (2.17) the expression
(2.28) we need following corollaries.
Corollary 1.
I(µ
) = Sb(µ5 +µ6)Sb(2Q −
6∑
i=1
µ6)
∏
1≤i<j≤4
Sb(µi +µj)I(ν), (B.6)
26
where we deﬁne the integralI(µ) as
I(µ) = 1
2
∫ i∞
−i∞
∏ 6
i=1Sb(µi ±u)
Sb(±2u) du. (B.7)
Here we have
[ν1,ν 2,ν 3,ν 4,ν 5,ν 6] = [ µ1 +ξ,µ 2 +ξ,µ 3 +ξ,µ 4 +ξ,µ 5 −ξ,µ 6 −ξ]
and
2ξ = Q −
4∑
i=1
µi.
Later it will be convenient to write 6 variablesµ in the following way
[µ] =
[ µ1 µ2 µ3
µ4 µ5 µ6
]
.
Corollary 2. :
J(µ,ν ) =
3∏
i=1
Sb(µi +ν4)Sb(νi +µ4)I(ρ), (B.8)
with
J(µ,ν ) =
∫ i∞
−i∞
4∏
i=1
Sb(µi −u)Sb(νi +u)du, (B.9)
which has U(1) gauge symmetry, and the balancing condition ∑ 4
i=1(µi +νi) = 2Q. Here we
have
[ρ1,ρ 2,ρ 3,ρ 4,ρ 5,ρ 6] = [ µ1 +ξ,µ 2 +ξ,µ 3 +ξ,ν 1 −ξ,ν 2 −ξ,ν 3 −ξ]
and
2ξ = Q −ν4 −
3∑
i=1
µi = −Q +µ4 +
3∑
i=1
νi.
Again it is useful to have the following notation
[µ
,ν ] =
[ µ1 µ2 µ3 µ4
ν1 ν2 ν3 ν4
]
,
The inversion of Corollary 2 is the following
Corollary 3.
I(ρ) =
∏
1≤i<j≤3
Sb(ρi +ρj)Sb(ρi+3 +ρj+3)J(µ,ν ), (B.10)
27
and the balancing condition∑ 4
i=1µi +νi = 2Q. Here we have
[ µ1 µ2 µ3 µ4
ν1 ν2 ν3 ν4
]
=
[ ρ1 −x ρ 2 −x ρ 3 −x Q −ρ456 −x
ρ4 +x ρ 5 +x ρ 6 +x Q −ρ123 +x
]
,
whereρ123 =ρ1 +ρ2 +ρ3,ρ456 =ρ4 +ρ5 +ρ6, andx is arbitrary.
Corollary 4. :
I(µ
) = Sb(2Q −
6∑
i=1
µi)
∏
1≤i<j≤6
Sb(µi +µj)I(Q/2 −µ). (B.11)
To get the desired transformation formulas one should use the following asymptotic formulas
when some of the parameters go to inﬁnity
lim
u→∞
e
π i
2 B2, 2(u)Sb(u) = 1 , for argb< argu< arg 1/b +π,
lim
u→∞
e− π i
2 B2, 2(u)Sb(u) = 1 , for argb −π <argu< arg 1/b.
By taking different restrictions for the parameters one canget lots of identities from the integral
identity (B.5). Let us take
µ1 →µ1 +µ; µ5 →µ5 −µ
with the following limitµ → ∞. The left hand-side of (B.5) gives
Ih(µ2,µ 3,µ 4,µ 6,µ 7,µ 8) = 1
2
∫ i∞
−i∞
∏ 4
i=2Sb(µi ±z)Sb(µi+4 ±z)
Sb(±2z) dz, (B.12)
without any restrictions for parametersµ2,µ 3,µ 4,µ 6,µ 7,µ 8 and in the right hand-side one needs
to shift the integration variable z → z −µ/2 and afterwards taking the limit µ → ∞ which
gives
∏
2≤i<j≤4
Sb(µi +µj)Sb(µi+4 +µj+4) (B.13)
×
∫ i∞
−i∞
dz Sb(ξ +z + (µ1 +µ5)/2)Sb((µ1 +µ5)/2 −ξ −z)
×
4∏
i=2
Sb(µi +ξ − (µ1 +µ5)/2 −z)Sb(µi+4 −ξ + (µ1 +µ5)/2 +z)dz,
and 2ξ =Q −∑ 4
i=2µi.
Inverting now the equality (B.12)=(B.13) one gets Corollary 3. To get Corollary 1 one takes
the limitµ7,µ 8 → ∞ such thatµ7 −µ8 =O(1) in (B.5).
28
Application of (B.2) twice and thrice gives new integral tra nsformations formulas for (B.1)
while further application of (B.2) does not lead to new integral transformations. It can be shown
[S08]
V (s1,...,s 8) =
∏
1≤i<j≤8
Γ(sisj;p,q )V
(√pq
s1
,...,
√pq
s8
)
, (B.14)
the reduction to the hyperbolic level of which brings to Corollary 4.
In [SV11] other reductions ofV -functions were considered in connections with the so-called
state integral for 41 knot [Hi1] and with the kernel ofS-move [T03].
B.3 Derivation of the indentity (2.28)
Let us start from the expression (2.17) and apply Corollary 2 taking parameters as
[µ
,ν ] =
[ Q ± (αs − Q
2 ) α2 +α4 +αt − Q
2 α2 +α4 −αt + Q
2
−α4 ± (α3 − Q
2 ) Q
2 −α1 −α2 − Q
2 +α1 −α2
]
,
one gets
A1I
( Q−αt−α1−α4
2 +αs
3Q−αt−α1−α4
2 −αs
Q+α1−α4+αt
2 −α3
−Q−α1+α4+αt
2 +α2
Q−α1+α4+αt
2 −α2
−Q+α1−α4+αt
2 +α3
)
(B.15)
with
A1 = Sb(α2 +α3 −αt)Sb(α1 −α2 +αs)Sb(−Q +α1 +α4 +αt)
Sb(±(Q − 2αt))Sb(α2 +αt −α3)Sb(α3 +αt −α2)Sb(α3 −α4 +αs).
The integral in (B.15) is deﬁned for αk ∈ Q/2 + iR by using a contour ~C that approaches
Q
4 + iR near inﬁnity, and passes the real axis in (− Q
4, Q
4 ), and for other values ofαk ∈ Q
2 + iR
by analytic continuation.
Applying Corollary 1 to (B.15) (with the order of parametersas staying in (B.15)) one obtains
A2I
( αs + α3−α2−αt
2 Q −αs + α3−α2−αt
2 α1 + αt−α2−α3
2
α4 −Q + α2+α3+αt
2 Q −α1 + αt−α2−α3
2 −α4 + α2+α3+αt
2
)
, (B.16)
deﬁned by the contour ~C and where
A2 = Sb(α2 +α3 −αt)Sb(−α1 +α2 +αs)Sb(α1 +α4 −αt)Sb(2Q −α3 −α4 −αs)
Sb(±(Q − 2αt))Sb(α3 −α4 +αs)Sb(α3 +α4 −αs) .
On the next step we apply Corollary 4 to (B.16) and get
A3I
(
−αs + Q+α2−α3+αt
2 αs + −Q+α2−α3+αt
2 −α1 + Q+α2+α3−αt
2
−α4 + 3Q−α2−α3−αt
2 α1 + −Q+α2+α3−αt
2 α4 + Q−α2−α3−αt
2
)
, (B.17)
29
with the same contour ~C and
A3 = Sb(α1 −α2 +αs)Sb(α1 −α4 +αt)Sb(α1 +α4 −αt)
Sb(±(Q − 2αt))Sb(α2 −α3 +αt)Sb(α1 +α2 −αs)Sb(2Q −α1 −α4 −αt)
× Sb(2Q −α1 −α2 −αs)Sb(−α1 +α4 +αt)
Sb(−α3 +α4 +αs)Sb(2Q −α2 −α3 −αt)Sb(α1 +α4 −αt)Sb(−α2 +α3 +αt).
Finally, we apply Corollary 3 for (B.17) with slightly permuted parameters (since the integral
hasS6 permutation symmetry over parameters)
A3I
( αs + −Q+α2−α3+αt
2 α1 + −Q+α2+α3−αt
2 −α4 + 3Q−α2−α3−αt
2
−αs + Q+α2−α3+αt
2 −α1 + Q+α2+α3−αt
2 α4 + Q−α2−α3−αt
2
)
,
together with taking
x = − Q+α2+α3+αt
2 −α4
to get (2.28) which proves the identity (2.28) in the main part of the text.
References
[AGT] L. F. Alday, D. Gaiotto, and Y . Tachikawa, Liouville Correlation Functions from Four-
dimensional Gauge Theories, Lett. Math. Phys. 91 (2010) 167–197.
[AGGTV] L. F. Alday, D. Gaiotto, S. Gukov, Y . Tachikawa, H. Verlinde, Loop and surface operators in
N = 2 gauge theory and Liouville modular geometry, J. High Energy Phys. 1001 (2010) 113.
[ALPS] D. Alessandrini, L. Liu. A. Papadopoulos, W. Su, The behaviour of Fenchel-Nielsen distance
under a change of pants decomposition,arXiv:1105.0202.
[AK] J. E. Andersen, R. Kashaev, A TQFT from quantum Teichm¨uller theory,arXiv:1109.6295.
[BMS1] V . V . Bazhanov, V . V . Mangazeev, S. M. Sergeev,Faddeev-Volkov solution of the Yang-Baxter
equation and discrete conformal symmetry, Nucl. Phys. B 784 (2007) 234–258.
[BMS2] V . V . Bazhanov, V . V . Mangazeev, S. M. Sergeev,Quantum geometry of 3-dimensional lattices,
J. Stat. Mech. 0807 (2008) P07004.
[Br] E.W. Barnes: Theory of the double gamma function, Phil. Trans. Roy. Soc. A196 (1901) 265–388.
[Bx] R. J. Baxter, Partition function of the eight-vertex lattice model, Ann. Phys. (NY) 70 (1972) 193–
228.
[BT1] A. G. Bytsko and J. Teschner, R-operator, co-product and Haar-measure for the modular double
of Uq(sl(2, R)), Comm. Math. Phys. 240 (2003) 171–196.
[BT2] A. G. Bytsko and J. Teschner, Quantization of models with non-compact quantum group symme-
try: Modular XXZ magnet and lattice sinh-Gordon model, J. Phys. A A 39 (2006) 12927–12981.
[CF99] V . V . Fock, L. O. Chekhov, Quantum Teichm¨uller spaces, Theor. and Math. Phys. 120 (1999)
1245–1259.
30
[CF00] V . V . Fock, L. O. Chekhov,Observables in 3D gravity and geodesic algebras, Czechoslovak J.
Phys. 50 (2000) 1201–1208.
[DS] J. F. van Diejen and V . P. Spiridonov, Unit circle elliptic beta integrals, Ramanujan J. 10 (2005)
187–204.
[DGLZ] T. Dimofte, S. Gukov, J. Lenells, Don Zagier, Exact Results for Perturbative Chern-Simons
Theory with Complex Gauge Group, Commun. Num. Theor. Phys. 3 (2009) 363–443.
[DiGu] T. Dimofte, S. Gukov, Chern-Simons Theory and S-duality, arXiv:1106.4550
[hep-th].
[DiGG] T. Dimofte, D. Gaiotto and S. Gukov, Gauge Theories Labelled by Three-Manifolds ,
arXiv:1108.4389 [hep-th].
[DSV] F. A. H. Dolan, V . P. Spiridonov and G. S. Vartanov, From 4d superconformal indices to 3d
partition functions, Phys. Lett. B 704 (2011) 234–241.
[DrGG] N. Drukker, D. Gaiotto, and J. Gomis, The Virtue of Defects in 4D Gauge Theories and 2D
CFTs, J. High Energy Phys. 1106 (2011) 025.
[DGOT] N. Drukker, J. Gomis, T. Okuda, J. Teschner, Gauge Theory Loop Operators and Liouville
Theory, J. High Energy Phys. 1002 (2010) 057.
[F2] L. D. Faddeev: Discrete Heisenberg–Weyl group and modular group, Lett. Math. Phys. 34 (1995)
249–254.
[FK2] L.D. Faddeev and R. M. Kashaev: Quantum dilogarithm, Mod. Phys. Lett. A9 (1994) 427–434.
[F99] L. D. Faddeev, Modular double of a quantum group, Confrence Mosh Flato 1999, V ol. I (Dijon),
149–156, Math. Phys. Stud., 21, Kluwer Acad. Publ., Dordrecht, 2000,arXiv:math/9912078.
[Fo97] V . Fock, Dual Teichm¨uller spaces,arXiv:dg-ga/9702018.
[GW] D. Gaiotto and E. Witten, S-Duality of Boundary Conditions In N = 4 Super Yang-Mills Theory,
arXiv:0807.3720 [hep-th].
[HHL1] N. Hama, K. Hosomichi, and S. Lee, Notes on SUSY gauge theories on three-sphere , J. High
Energy Phys. 1103 (2011) 127.
[HHL2] N. Hama, K. Hosomichi, and S. Lee, SUSY gauge theories on squashed three-spheres, J. High
Energy Phys. 1105 (2011) 014.
[Hi1] K. Hikami, Hyperbolic Structure Arising from a Knot Invariant , Int. J. Mod. Phys. A16 (2001)
3309–3333.
[Hi2] K. Hikami, Hyperbolicity of Partition Function and Quantum Gravity , Nucl. Phys. B616 (2001)
537–548.
[Hi3] K. Hikami, Generalized Volume Conjecture and theA-Polynomials – the Neumann-Zagier Poten-
tial Function as a Classical Limit of Quantum Invariant, J. Geom. Phys. 57 (2007) 1895–1940.
[HLP] K. Hosomichi, S. Lee, and J. Park, AGT on the S-duality Wall, J. High Energy Phys. 1012 (2010)
079.
[Ip] I. C. H. Ip, Representation of the Quantum Plane, its Quantum Double, and Harmonic Analysis on
GL+
q (2, R ),arXiv:1108.5365.
31
[IOT] Y . Ito, T. Okuda, M. Taki, Line operators on S1 × R3 and quantization of the Hitchin moduli
space,arXiv:1111.4221.
[J] D. L. Jafferis, The Exact Superconformal R-Symmetry Extremizes Z,arXiv:1012.3210.
[KWY] A. Kapustin, B. Willett, and I. Yaakov,Exact results for Wilson loops in superconformal Chern–
Simons theories with matter, J. High Energy Phys. 1003 (2010) 089.
[K] R. M. Kashaev, The hyperbolic volume of knots from the quantum dilogarithm , Lett. Math. Phys.
39 (1997) 269–275.
[Ka98] R. M. Kashaev, Quantization of Teichm¨uller spaces and the quantum dilogarithm , Lett. Math.
Phys. 43 (1998), no. 2, 105–115.
[K2] R. Kashaev, The quantum dilogarithm and Dehn twists in quantum Teichmller theory, “Integrable
structures of exactly solvable two-dimensional models of quantum ﬁeld theory”, (Kiev, 2000) 211–
221, NATO Sci. Ser. II Math. Phys. Chem., 35, Kluwer Acad. Publ., Dordrecht, 2001.
[MS] G. Moore, N. Seiberg, Classical and quantum conformal ﬁeld theory , Comm. Math. Phys. 123
(1989) 177–254
[MT] S. Mizoguchi and T. Tada, Three-dimensional gravity from the Turaev-Viro invariant, Phys. Rev.
Lett. 68 (1992) 1795–1798.
[MY] J. Murakami and M. Yano, On the volume of a hyperbolic and spherical tetrahedron , Comm.
Anal. Geom. 13 (2005), no. 2, 379–400.
[N] N. A. Nekrasov, Seiberg-Witten prepotential from instanton counting, Adv. Theor. Math. Phys. 7
(2003) 831–864.
[NRS] N. Nekrasov, A. Rosly, S. Shatashvili, Darboux coordinates, Yang-Yang functional, and gauge
theory, Nucl. Phys. Proc. Suppl. 216 (2011) 69–93.
[Pe] V . Pestun, Localization of gauge theory on a four-sphere and supersymm etric Wilson loops ,
arXiv:0712.2824 [hep-th].
[PR] G. Ponzano, T. Regge, Semiclassical limit of Racah coefﬁcients, “Spectroscopic and Group Theo-
retical Methods in Physics”, ed. F. Bloch (North-Holland, Amsterdam, 1968).
[PT1] B. Ponsot and J. Teschner, Liouville bootstrap via harmonic analysis on a noncompact q uantum
group,arXiv:hep-th/9911110.
[PT2] B. Ponsot and J. Teschner, Clebsch-Gordan and Racah-Wigner coefﬁcients for a continuous series
of representations of Uq(sl(2, R)), Commun. Math. Phys. 224 (2001) 613–655.
[Ru] S. N. M. Ruijsenaars: First order analytic difference equations and integrable q uantum systems,
J. Math. Phys. 38 (1997) 1069–1146.
[S01] V . P. Spiridonov,On the elliptic beta function, Uspekhi Mat. Nauk56 (1) (2001) 181–182 (Russian
Math. Surveys 56 (1) (2001) 185–186).
[S03] V . P. Spiridonov, Theta hypergeometric integrals, Algebra i Analiz 15 (6) (2003) 161–215 (St.
Petersburg Math. J. 15 (6) (2004), 929–967).
[S08] V . P. Spiridonov, Essays on the theory of elliptic hypergeometric functions , Uspekhi Mat. Nauk
63 (3) (2008), 3–72 (Russian Math. Surveys 63 (3) (2008), 405–472).
32
[SV10] V . P. Spiridonov and G. S. Vartanov,Superconformal indices for N = 1 theories with multiple
duals, Nucl. Phys. B 824 (2010) 192–216.
[SV11] V . P. Spiridonov and G. S. Vartanov, Elliptic hypergeometry of supersymmetric dualities II.
Orthogonal groups, knots, and vortices,arXiv:1107.5788 [hep-th].
[Sp] M. Spreaﬁco, On the Barnes double zeta and Gamma functions , Journal of Number Theory 129
(2009) 2035–2063.
[TY] Y . Terashima and M. Yamazaki,SL(2, R) Chern-Simons, Liouville, and Gauge Theory on Duality
Walls, J. High Energy Phys. 1108 (2011) 135.
[T01] J. Teschner, Liouville theory revisited, Class. Quant. Grav. 18 (2001) R153–R222.
[T03] J. Teschner, On the relation between quantum Liouville theory and the qua ntized Teichm¨uller
spaces, Int. J. Mod. Phys.A19S2 (2004), 459–477; From Liouville theory to the quantum geometry
of Riemann surfaces, Cont. Math. 437 (2007) 231–246.
[T05] J. Teschner, An analog of a modular functor from quantized Teichm ¨uller theory, “Handbook of
Teichm¨ uller theory”, (A. Papadopoulos, ed.) V olume I, EMSPublishing House, Z¨ urich 2007, 685–
760.
[T08] J. Teschner, Nonrational conformal ﬁeld theory, “New Trends in Mathematical Physics” (Selected
contributions of the XVth ICMP), Vladas Sidoravicius (ed.), Springer Science and Business Media
B.V . 2009.
[TeVa] J. Teschner, G. S. Vartanov, In preparation.
[TuVi] V . G. Turaev, O. Y . Viro,State Sum Invariants of 3-Manifolds and Quantum 6j-Symbols, Topol-
ogy 31 (1992) 865–902.
[V] A. Yu. V olkov: Noncommutative hypergeometry, Commun. Math. Phys. 258 (2005) 257–273.
[Wo] S. L. Woronowicz: Quantum exponential function, Rev. Math. Phys. 12 (2000) 873–920.
