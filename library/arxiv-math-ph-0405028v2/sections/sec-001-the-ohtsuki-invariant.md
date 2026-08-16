---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INV ARIANT FOR THE BRIESKORN HOMOLOGY SPHERES KAZUHIRO HIKAMI"
section_id: sec-001-the-ohtsuki-invariant
section_title: "The Ohtsuki Invariant"
section_number: null
pages: 20-26
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES KAZUHIRO HIKAMI — We study an exact asymptotic behavior of the Witten–Reshet ikhin–Turaev SU(2) in- variant for the Brieskorn homology"
---
τ∞
(
Σ( p1, p2, p3)
)
=
∞∑
n=0
λn
(
Σ( p1, p2, p3)
)
· (q − 1)n (7.3)
Inﬁnite series in eqs. (7.1) and (7.2) originate from an asym ptotic expansion of the integral
r(1,1,1)
p (1/N; 0) deﬁned in eq. (4.21), which appears as a tail of the nearly modular property of
the Eichler integral. It is noted that an integral formula fo r the Ohtsuki invariant was studied in
Refs. 21, 39 by a different method.
To compute an explicit form of λn(M), we use the Stirling number of the ﬁrst kind deﬁned by
n−1∏
j=0
(x − j) =
n∑
m=0
S(m)
n xm (7.4)
As the Stirling number satisﬁes (see, e.g., Ref. 1)
(log q)m
m! =
∞∑
n=m
S(m)
n
(q − 1)n
n! (7.5)
we can easily obtain the following expression.
20
Theorem 15. Let the function Λ n(p1, p2, p3) be deﬁned by
Λ n(p1, p2, p3) = 1
2
1
(n + 1)!
n+1∑
m=1
S(m)
n+1
( 2 − φ(p1, p2, p3)
4
) m
×
m∑
k=0
(
m
k
)( 1
P (2 − φ(p1, p2, p3))
) k
L(−2 k, χ(1,1,1)
2P ) (7.6)
Then the invariant λn(M) is computed as follows;
λn
(
Σ( p1, p2, p3)
)
=





Λ n(p1, p2, p3) for 1
p1
+ 1
p2
+ 1
p3
< 1
Λ n(2, 3, 5) + (−1)n+1 for the Poincar´e homology sphere
(7.7)
We note that a value of the L-function, which is given by eq. (4.18), can be computed easi ly
from a generating function for a case of (ℓ1, ℓ2, ℓ3) = (1 , 1, 1);
−2 ch( z) + 2 sh(6 z) sh(10 z)
ch(15 z) = −2 ch(9 z) ch(5 z)
ch(15 z)
=
∞∑
n=0
L(−2 n, χ(1,1,1)
60 )
(2 n)! z2n (7.8)
and in a case of 1
p1
+ 1
p2
+ 1
p3
< 1 we have
4 sh(p1 p2 z) sh( p1 p3 z) sh( p2 p3 z)
sh(p1 p2 p3 z) =
∞∑
n=0
L(−2 n, χ(1,1,1)
2P )
(2 n)! z2n (7.9)
See Table 1 for explicit values of λn(M) for some Brieskorn spheres.
We can rewrite eq. (7.7) for the ﬁrst three terms as follows;
λ0
(
Σ( p1, p2, p3)
)
= 1 (7.10)
λ1
(
Σ( p1, p2, p3)
)
= −1
4
(
φ + P
(
1 − 1
p 2
1
− 1
p 2
2
− 1
p 2
3
) )
(7.11)
λ2
(
Σ( p1, p2, p3)
)
= 1
12
(
3 φ2 + 12 φ − 4
8 + 3 P
4 (φ + 2)
(
1 −
3∑
j=1
1
p 2
j
)
+ P 2
8
(
2
(
1 −
3∑
j=1
1
p 4
j
)
+ 5
(
1 −
3∑
j=1
1
p 2
j
) 2
))
(7.12)
where we mean φ = φ(p1, p2, p3) deﬁned in eq. (2.12). As was proved in Refs. 27, 28 we see that
λ0
(
Σ( p1, p2, p3)
)
= 1 (7.13)
λ1
(
Σ( p1, p2, p3)
)
= 6 λC
(
Σ( p1, p2, p3)
)
(7.14)
21
M λ 0 λ 1 λ 2 λ 3 λ 4 λ 5 λ 6 λ 7 λ 8
Σ(2 , 3, 5) 1 −6 45 −464 6224 −102816 2015237 −45679349 1175123730
Σ(2 , 3, 7) 1 −6 69 −1064 20770 −492052 13724452 −440706098 16015171303
Σ(2 , 3, 11) 1 −12 198 −4564 136135 −4979568 215636785 −10785653847 611802510704
Σ(2 , 3, 13) 1 −12 246 −6916 248171 −10848488 559466999 −33256127501 2238888918356
Σ(2 , 3, 17) 1 −18 459 −16404 757689 −42883758 2872307319 −222158381412 19483805436567
Σ(2 , 3, 19) 1 −18 531 −21660 1131375 −72097914 5424649644 −470672677647 46266101270760
Σ(2 , 5, 7) 1 −12 222 −5596 179985 −7054432 326278974 −17397305298 1050720467092
Σ(2 , 5, 9) 1 −18 411 −12900 523445 −26063974 1537243785 −104755839122 8097415424747
Σ(2 , 5, 11) 1 −18 531 −21180 1074975 −66390674 4834590264 −405657513711 38541528405358
Σ(2 , 7, 13) 1 −36 1674 −106884 8799855 −887883368 106042462590 −14627548503126 2288188525438231
Σ(2 , 7, 15) 1 −36 2010 −152244 14703739 −1730017752 240158450652 −38429255864768 6964744996791857
Σ(2 , 11, 17) 1 −72 6948 −918744 156141090 −32466056280 7983578235864 −2266232536578132 729278178446689719
Σ(2 , 11, 19) 1 −78 8481 −1261160 240437790 −56007699396 15418103295783 −4897366295772501 1763003584636961535
Σ(2 , 11, 21) 1 −90 10695 −1742580 365286685 −93734684478 28454533630530 −9972833783229875 3962937841176563555
Σ(3 , 4, 5) 1 −12 198 −4324 119455 −4012828 159008935 −7263759799 375878922067
Σ(3 , 4, 7) 1 −18 411 −12420 476645 −22300734 1232660885 −78624211186 5684458291305
Σ(3 , 4, 11) 1 −30 1065 −49960 2988770 −218577416 18915594545 −1890831231245 214380047624390
Σ(3 , 4, 13) 1 −30 1305 −74680 5390950 −472424616 48786184083 −5804487459615 781992244219680
Σ(3 , 4, 23) 1 −60 4470 −441740 55544845 −8523297832 1546017437658 −323709524734970 76844211062714480
Σ(3 , 4, 25) 1 −60 4950 −540140 74583605 −12524972472 2481232929734 −566688382409942 146614680355157664
Σ(3 , 5, 7) 1 −24 684 −25640 1222766 −71219336 4906476652 −390356879176 35220329064877
Σ(3 , 5, 8) 1 −24 804 −35360 1961016 −132053796 10481576931 −958711945083 99307064129868
Σ(3 , 5, 11) 1 −36 1626 −96756 7300091 −671133288 72881361140 −9132371657296 1297049789194653
Σ(3 , 5, 13) 1 −42 2247 −158396 14146195 −1538635378 197615046741 −29280417770120 4916816674605230
Σ(4 , 5, 7) 1 −30 1185 −60880 3934980 −308750176 28560576934 −3045183200982 367764306523118
Σ(4 , 7, 9) 1 −60 4230 −385820 44419865 −6227423152 1031445122700 −197181302142540 42735797918044660
Table 1: λ n
(
Σ( p1, p 2, p 3)
)
22
where λC(M) is the Casson invariant (4.12) for M. It is noted that λ2
(
Σ( p1, p2, p3)
)
is calculated
in Ref. 40.
8. D ISCUSSIONS
We have studied the Witten–Reshetikhin–Turaev invariant f or the Brieskorn homology
spheres (2.11) by use of properties of the Eichler integral o f the half-integral weight based on
the method of Ref. 23. The WRT invariant coincides with a limiting value of the Eichler integral at
τ → 1/N for N ∈ Z, and the nearly modular property (4.17) of the Eichler integral gives an exact
asymptotic behavior of the WRT invariant (5.7) and (5.8). Wi th the correspondence between the
modular form and the quantum invariant, we can give an interpretation for the invariants of mani-
fold such as the Chern–Simons invariant, the Ohtsuki invariant, the Casson invariant, Reidemeister
torsion, and the spectral ﬂow from a point of view of the modul ar form. Especially the number
of the non-vanishing Eichler integrals at τ → N ∈ Z is related to the Casson invariant, and there
exists a correspondence with an irreducible SU(2) represen tation of the fundamental group. In
our previous papers [10–12], we revealed a relationship bet ween a speciﬁc value of the colored
Jones polynomial for the torus knot and link, Ts,t and T2,2m, and the Eichler integral of the half-
integral weight modular form. Therein shown was that an exact asymptotic behavior has a form of
eqs. (5.7) and (5.8), and that a generating function of a tail polynomial part, or the Ohtsuki invari-
ant, is an inverse of the Alexander polynomial A1/2−A−1/2
∆( A) . So we may conclude that the left hand
side of eq. (7.9) plays a role of the inverse of the Alexander p olynomial. In the same manner, we
may deﬁne an analogue of the Casson invariant by a minus half of the number of the non-vanishing
Eichler integrals at τ ∈ Z. We collect these correspondence in the SU(2) quantum invar iants in
Table 2.
torus link T2,2m torus knot Ts,t Σ( p1, p2, p3)
d 1 2 3
“Casson” λC −1
2 (m − 1) −1
4 (s − 1) (t − 1) −1
2 γ(p1, p2, p3)
“Alexander”∆( A) Am − A−m
A
1
2 + A− 1
2
(A
st
2 − A− st
2 ) (A
1
2 − A− 1
2 )
(A
s
2 − A− s
2 ) (A
t
2 − A− t
2 )
(A
1
2 − A− 1
2 )2
∏ 3
j=1(A
1
2pj − A
− 1
2pj )
Table 2: We give an interpretation for the “Casson invariant” and the“Alexander polynomial” from the view point of
the modular forms. “Dimension” d denotes that the number of the modular form is related to the n umber of
the integral lattice point in d-dimensional space.
23
In Ref. 23 discussed also is a relationship between the WRT invariant for the Poincar´ e homology
sphere and the Ramanujan mock theta function. We hope to repo rt on the q-series identity asso-
ciated with the quantum invariant for the Brieskorn homolog y sphere using a surgery description
with an expression of the colored Jones polynomial for the to rus knot given in Ref. 8 (see also
Ref. 24).
ACKNOWLEDGMENTS
The author would like to thank H. Murakami for useful discuss ions and encouragements. This
work is supported in part by Grant-in-Aid for Young Scientis ts from the Ministry of Education,
Culture, Sports, Science and Technology of Japan.
REFERENCES
[1] M. Abramowitz and I. A. Stegun, eds., Handbook of Mathematical Functions with Formulas, Graphs,and Math-
ematical Tables, Dover, New York, 1972.
[2] M. F. Atiyah, The Geometry and Physics of Knots, Cambridge Univ. Press, Cambridge, 1990.
[3] A. A. Belavin, A. M. Polyakov, and A. B. Zamolodchikov, Inﬁnite conformal symmetry in two-dimensional
quantum ﬁeld theory, Nucl. Phys. B 241, 333–380 (1984).
[4] R. Fintushel and R. Stern, Instanton homology of Seifert ﬁbered homology three spheres, Proc. Lond. Math. Soc.
61, 109–137 (1990).
[5] D. S. Freed, Reidemeister torsion, spectral sequences, and Brieskorn spheres, J. Reine Angew. Math.429, 75–89
(1992).
[6] D. S. Freed and R. E. Gompf, Computer calculation of Witten’s 3-manifold invariant, Commun. Math. Phys.
141, 79–117 (1991).
[7] S. Fukuhara, Y . Matsumoto, and K. Sakamoto, Casson’s invariant of Seifert homology 3-spheres, Math. Ann.
287, 275–285 (1990).
[8] K. Hikami, Difference equation of the colored Jones polynomial for the torus knot, Int. J. Math. 15, 959–965
(2004).
[9] ———, q-series and L-functions related to half-derivatives of the Andrews–Gor don identity , Ramanujan J.
(2004), to appear.
[10] ———, Quantum invariant for torus link and modular forms, Commun. Math. Phys. 246, 403–426 (2004).
[11] K. Hikami and A. N. Kirillov, Torus knot and minimal model, Phys. Lett. B 575, 343–348 (2003).
[12] ———, Hypergeometric generating function of L-function, Slater’s identities, and quantum knot invarian t,
math-ph/0406042 (2004).
[13] L. C. Jeffrey, Chern–Simons–Witten invariants of lens spaces and torus bundles, and the semiclassical approxi-
mation, Commun. Math. Phys. 147, 563–604 (1992).
[14] V . F. R. Jones,A polynomial invariant for knots via von Neumann algebras, Bull. Amer. Math. Soc.12, 103–111
(1985).
[15] R. Kirby and P. Melvin, The 3-manifold invariants of Witten and Reshetikhin–Turaev for sl(2, C ), Invent. Math.
105, 473–545 (1991).
[16] ———, Dedekind sums, µ-invariants and the signature cocycle, Math. Ann. 299, 231–267 (1994).
[17] P. A. Kirk and E. P. Klassen, Chern–Simons invariants of 3-manifolds and representation spaces of knot groups,
Math. Ann. 287, 343–367 (1990).
[18] S. Lang, Introduction to Modular Forms, vol. 222 of Grund. math. Wiss., Springer, Berlin, 1976.
[19] R. Lawrence, Asymptotic expansions of Witten–Reshetikhin–Turaev invariants for some simple 3-manifolds , J.
Math. Phys. 36, 6106–6129 (1995).
24
[20] ———, Witten–Reshetikhin–Turaev invariants of 3-manifolds as h olomorphic functions , in J. E. Andersen,
J. Dupont, H. Pedersen, and A. Swann, eds., Geometry and Physics, vol. 184 of Lect. Notes Pure Appl. Math. ,
pp. 363–377, Dekker, New York, 1996.
[21] ———, On Ohtsuki’s invariants of homology3-spheres, J. Knot Theory Ramif. 8, 1049–1063 (1999).
[22] R. Lawrence and L. Rozansky, Witten–Reshetikhin–Turaev invariants of Seifert manifolds, Commun. Math. Phys.
205, 287–314 (1999).
[23] R. Lawrence and D. Zagier, Modular forms and quantum invariants of 3-manifolds , Asian J. Math. 3, 93–107
(1999).
[24] T. T. Q. Le, Quantum invariants of 3-manifolds: Integrality, splittin g, and perturbative expansion , Topology
Appl. 127, 125–152 (2003).
[25] J. Milnor, On the 3-dimensional Brieskorn manifolds M (p, q, r ), in L. P. Neuwirth, ed., Knots, Groups, and
3-Manifolds, pp. 175–225, Princeton Univ. Press, 1975, papers Dedicated to the Memory of R. H. Fox.
[26] L. J. Mordell, Lattice points in a tetrahedron and generalized Dedekind su ms, J. Indian Math. Soc. (NS) 15,
41–46 (1951).
[27] H. Murakami, Quantum SU(2)-invariants dominate Casson’s SU(2)-invariant, Math. Proc. Camb. Phil. Soc.115,
253–281 (1993).
[28] ———, Quantum SO(3) invariants dominate the SU(2) invariant of Casson and Walker, Math. Proc. Cambridge
Philos. Soc. 117, 237–249 (1995).
[29] T. Ohtsuki, A polynomial invariant of integral homology 3-spheres , Math. Proc. Camb. Phil. Soc. 117, 83–112
(1995).
[30] ———, A polynomial invariant of rational homology 3 spheres, Invent. Math. 123, 241–257 (1996).
[31] H. Rademacher, Topics in Analytic Number Theory, vol. 169 of Grund. Math. Wiss., Springer, New York, 1973.
[32] H. Rademacher and E. Grosswald, Dedekind Sums, no. 16 in Carus Mathematical Monographs, Mathematical
Association of America, Washington DC, 1972.
[33] N. Y . Reshetikhin and V . G. Turaev,Invariants of 3-manifolds via link polynomials and quantum groups, Invent.
Math. 103, 547–597 (1991).
[34] L. Rozansky, A large k asymptotics of Witten’s invariant of Seifert manifolds, Commun. Math. Phys. 171, 279–
322 (1995).
[35] ———, A contribution of the trivial connection to Jones polynomia l and Witten’s invariant of 3d manifolds I,
Commun. Math. Phys. 175, 275–296 (1996).
[36] ———, A contribution of the trivial connection to Jones polynomia l and Witten’s invariant of 3d manifolds II,
Commun. Math. Phys. 175, 297–318 (1996).
[37] ———, Residue formulas for the large k asymptotics of Witten’s invariants of Seifert manifolds. t he case of
SU(2), Commun. Math. Phys. 178, 27–60 (1996).
[38] ———, Witten’s invariants of rational homology spheres at prime values of K and trivial connection contribu-
tion, Commun. Math. Phys. 180, 297–324 (1996).
[39] ———, The trivial connection contribution to Witten’s invariantand ﬁnite type invariants of rational homology
spheres, Commun. Math. Phys. 183, 23–54 (1997).
[40] C. Sato, Casson–Walker invariant of Seifert ﬁbered rational homolo gy spheres as quantum SO(3)-invariant , J.
Knot Theory Ramif. 6, 79–93 (1997).
[41] N. Saveliev, Lectures on the Topology of 3-Manifolds: An Introduction to the Casson Invariant , Walter de
Gruyter, Berlin, 1999.
[42] K. Walker, An Extension of Casson’s Invariant, vol. 126 of Ann. Math. Stud., Princeton Univ. Press, Princeton,
1992.
[43] E. Witten, Quantum ﬁeld theory and Jones’ polynomial, Commun. Math. Phys. 121, 351–399 (1989).
[44] D. Zagier, Vassiliev invariants and a strange identity related to the Dedekind eta-function, Topology40, 945–960
(2001).
25
DEPARTMENT OF PHYSICS , G RADUATE SCHOOL OF SCIENCE , U NIVERSITY OF TOKYO , H ONGO 7–3–1,
BUNKYO , T OKYO 113–0033, J APAN.
URL: http://gogh.phys.s.u-tokyo.ac.jp/˜hikami/
E-mail address: hikami@phys.s.u-tokyo.ac.jp
26
