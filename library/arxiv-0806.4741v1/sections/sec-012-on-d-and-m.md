---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane P. Bieliavsky G´ eom´ etrie et Physique math´ ematique Universit´ e Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louva"
section_id: sec-012-on-d-and-m
section_title: "On D and M"
section_number: null
pages: 22-26
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane P. Bieliavsky Géométrie et Physique mathématique Université Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louvain-la-Neuve, Belgium — We"
---
1 Group type structures. To obtain the expressions (33) and (34), we proceed as follows. Consider
for instance the hyperbolic plane D = SL2(R)/SO(2) =: G/K. Consider the following usual presentation
of g := sl2(R) as generated over R by the elements E,F,H with table [ E,F ] = H, [H,E ] = 2 E and
[H,F ] =−2F . Then one may set k := R.(E−F ), a := R.H⊂ p =: k⊥ and ln := R.E. The group S may
then be realized as the connected Lie subgroup of G admitting s := a⊕ n as Lie algebra. Within these
22
notations, the Iwasawa decomposition G = SK yields the above-mentioned identiﬁcation S = D and the
following global coordinate system:
s−→ S : (a,𝓁 ) :=aH +𝓁E↦→ exp(aH) exp(𝓁E). (156)
In this simple group context, the involution ˜ σ of G is nothing else than the Cartan involution associated
with the data of K. The symmetry at the base point K ofG/K therefore readssK(gK) := ˜σ(g)K which for
a∈A := exp(a) and n∈N := exp(n) corresponds to ˜σ(an)K = a−1˜σ(n)K. Observing that σ(E) =−F , a
small computation then yields exp( 𝓁F ) exp(− 1
2 log(1 +𝓁2)H) exp(−𝓁E)∈ K hence the above expression of
ΨD. The case of the Poincar´ e orbit is similar, details can be found in [38].
A.2 Co-adjoint orbits of iso(1, 1): the Poincar´ e plane
Let us emphasize that when the Lie group under consideration is not semi-simple (e.g. the Poincar´ e group
Iso(1, 1), in opposition to the SL(2, R) group), only the co-adjoint orbits make sensea priori in the framework
of subsection (2.1). An elementary calculation shows that onIso(1, 1) the co-adjoint orbits consist generically
into hyperbolic cylinder sheets, otherwise remain four planes and a line of ﬁxed point. If we denotes by b,
e0 and e1 a basis of generators of iso(1, 1) that obey the commutation relations:
[b,e 0] =e1 , [b,e 1] =e0 , [e0,e 1] = 0 , (157)
and by β, ε0 and ε1 a basis of the dual space iso∗(1, 1), the co-adjoint orbits are
the generic ones: x =k
{ vβ + cosh(α)ε0− sinh(α)ε1 ,
vβ− sinh(α)ε0 + cosh(α)ε1
k⁄= 0, v ∈ R, a∈ R (158)
the four null ones: x =vβ±α(ε0±ε1) , v ∈ R, α∈ R+
0 (159)
the pointlike ones: x =vβ , v =Cte∈ R. (160)
The ﬁrst ones are coset of the Poincar´ e group by the subgroup of translations in time (or in space); the second
ones are coset obtained by dividing by light-like translation; both are topologically R2, α and v providing
coordinates on them. The fundamental vector ﬁelds, on a generic orbit, are given by (denoting a point x by
its coordinates α and v):
b∗
(α,v) =∂α , e ∗
0(α,v) =− sinhα∂l , e ∗
1(α,v) = coshα∂l , (161)
b∗
(α,v) =∂α , e ∗
0(α,v) = coshα∂v , e ∗
1(α,v) =− sinhα∂v , (162)
and the symplectic form is given by:
ω(α,v) =dα∧dv . (163)
In terms of the ( a,l ) = ( α/2,v )-coordinates (32) used throughout this paper, these fundamental vector
ﬁelds would be re-expressed as H∗ =−∂a, E∗ =−e−2a∂l =−(e∗
0(a,l) +e∗
1(a,l)) and F∗ =−ke 2a∂l =
±k(e∗
0(a,l)−e∗
1(a,l)).
An aﬃne, torsion free, connection will be Iso(1, 1) invariant if its coeﬃcients verify the two sets of
equations:
Γα
βγ = Γα
γβ (164)
ξµ∂µΓα
βγ−∂µξαΓµ
βγ +∂βξµΓα
µγ +∂γξµΓα
βµ +∂βγξα = 0 , ξ =β, ε0, ε1 (165)
These equations imply that in (v,α ) coordinates, only two connection coeﬃcients are non vanishing, depend-
ing on two constants A and B:
Γv
α,α =−v +A , Γα
α,α =B (166)
If we moreover require the connection to be symplectic ( ∇ω = 0), this implies that only Γ v
α,α =−v +A is
non zero.
Finally imposing that the symmetry transformations (38) preserve the connection imposes that A = 0.
On a symplectic manifold (M,ω,s ) such a connection: torsionless, preserving the two-form ω, and invariant
23
with respect to the symmetries s is unique.It constitute the so-called Loos connection ([34]), intrinsically
deﬁned by
ωx(∇XY,Z ) = 1
2Xxωx(Y +sx⋆Y,Z ) (167)
or in terms of the symmetry expressed in coordinates xρ as xρ[sP (Q)] = sρ(xµ[P ],xν[Q]):
Γρ
στ (xµ[P ]) = ∂2sρ(xµ[P ],xν[Q])
∂xσ[Q]∂xτ[Q]
⏐⏐⏐⏐
Q=P
The geodesic diﬀerential equations are
¨a = 0 , ¨𝓁− 4𝓁 ˙a2 = 0 (168)
from which we infer immediately the equations of the aﬃne geodesic curves (in term of an aﬃne parameter
s, starting from the point of coordinates ( a0,𝓁 0) with tangent vector, in natural components, ( p0,q 0):
a =p0s +a0 , 𝓁 =𝓁0 cosh(2p0s) +q0
sinh(2p0s)
2p0
. (169)
From these we may recover the symmetry (38) and mid-point (39) equations; but let us emphasize that these
are deﬁned directly in terms of the group action (32) and the involution (33).
References
[1] F. Bayen, M. Flato, C. Fronsdal, A. Lichnerowicz, and D. Sternheimer, “Deformation theory and
quantization I and II,” Ann. Phys. 111 (1978) 61–151.
[2] De Wilde, Marc; Lecomte, Pierre B. A. Existence of star-products and of formal deformations of the
Poisson Lie algebra of arbitrary symplectic manifolds. Lett. Math. Phys. 7 (1983), no. 6, 487–496.
[3] Fedosov, B. V. Formal quantization. (Russian) Some problems in modern mathematics and their
applications to problems in mathematical physics (Russian), 129–136, vi, Moskov. Fiz.-Tekhn. Inst.,
Moscow, 1985.
[4] Omori, Hideki; Maeda, Yoshiaki; Yoshioka, Akira Weyl manifolds and deformation quantization. Adv.
Math. 85 (1991), no. 2, 224–255.
[5] Bertelson, M´ elanie; Cahen, Michel; Gutt, Simone Equivalence of star products. Geometry and physics.
Classical Quantum Gravity 14 (1997), no. 1A, A93–A107.
[6] R. Nest and R. Tsygan, “Algebraic index theorem,” Comm.Math.Phys. 172 (1995) 223–262.
[7] F. Hansen, “Quantum mechanics in phase space,” Rep. Math. Phys. 19(3) (1984) 361–381.
[8] Bertelson, M´ elanie; Bieliavsky, Pierre; Gutt, Simone Parametrizing equivalence classes of invariant
star products. Lett. Math. Phys. 46 (1998), no. 4, 339–345.
[9] N. Seiberg and E. Witten, “String theory and noncommutative geometry,” JHEP 09 (1999) 032,
hep-th/9908142.
[10] A. Connes, M. R. Douglas , A. S. Schwarz, “Noncommutative geometry and matrix theory: Compact-
iﬁcation on tori”, JHEP 9802:003,1998, hep-th/9711162.
[11] V. Schomerus, “D-branes and deformation quantization”, JHEP 06 (1999), 030.
[12] A. Y. Alekseev, A. Recknagel, and V. Schomerus, “Brane dynamics in background ﬂuxes and non-
commutative geometry,” JHEP 05 (2000) 010, hep-th/0003187.
[13] A. Y. Alekseev, A. Recknagel, and V. Schomerus, “Open strings and non-commutative geometry of
branes on group manifolds,” Mod. Phys. Lett. A16 (2001) 325–336, hep-th/0104054.
24
[14] A. Y. Alekseev, A. Recknagel, and V. Schomerus, “Non-commutative world-volume geometries: Branes
on SU(2) and fuzzy spheres,” JHEP 09 (1999) 023, hep-th/9908040.
[15] V. Schomerus, “Lectures on branes in curved backgrounds,” Class. Quant. Grav. 19 (2002) 5781–5847,
hep-th/0209241.
[16] P. Bieliavsky, C. Jego, and J. Troost, Nucl.Phys.B782:94-133,2007, hep-th/0610329.
[17] A. Hashimoto and K. Thomas, “Non-commutative gauge theory on d-branes in melvin universes,”
JHEP 01 (2006) 083, hep-th/0511197.
[18] A. Hashimoto and S. Sethi, “Holography and string dynamics in time-dependent backgrounds,” Phys.
Rev. Lett. 89 (2002) 261601, hep-th/0208126.
[19] S. Halliday and R. J. Szabo, “Noncommutative ﬁeld theory on homogeneous gravitational waves,” J.
Phys. A39 (2006) 5189–5226, hep-th/0602036.
[20] W. Behr and A. Sykora, “Construction of gauge theories on curved noncommutative spacetime,” Nucl.
Phys. B698 (2004) 473–502, hep-th/0309145.
[21] R.-G. Cai, J.-X. Lu, and N. Ohta, “Ncos and d-branes in time-dependent backgrounds,” Phys. Lett.
B551 (2003) 178–186, hep-th/0210206.
[22] R.-G. Cai and N. Ohta, “Holography and d3-branes in melvin universes,” Phys. Rev. D73 (2006)
106009, hep-th/0601044.
[23] R.-G. Cai and N. Ohta, “On the thermodynamics of large n non-commutative super yang-mills theory,”
Phys. Rev. D61 (2000) 124012, hep-th/9910092.
[24] S. Halliday and R. J. Szabo, “Isometric embeddings and noncommutative branes in homogeneous
gravitational waves,” Class. Quant. Grav. 22 (2005) 1945–1990, hep-th/0502054.
[25] R. J. Szabo, “Symmetry, gravity and noncommutativity,” Class. Quant. Grav. 23 (2006) R199–R242,
hep-th/0606233.
[26] J. M. Maldacena and H. Ooguri, “Strings in AdS(3) and SL(2,R) WZW model. I,” J. Math. Phys. 42
(2001) 2929–2960, hep-th/0001053.
[27] J. Teschner, “On structure constants and fusion rules in the SL(2,C)/SU(2) WZNW model,”Nucl.
Phys.B546 (1999), 390-422, hep-th/9712256.
[28] C. Bachas and M. Petropoulos, JHEP 0102 (2001) 025 [arXiv:hep-th/0012234].
[29] P. Bieliavsky, S. Detournay, P. Spindel, and M. Rooman, “Star products on extended massive non-
rotating BTZ black holes,” JHEP 06 (2004) 031, hep-th/0403257.
[30] P Bieliavsky Non-formal deformation quantizations of solvable Ricci-type symplectic symmetric spaces;
2008, J. Phys.: Conf. Ser. 103.
[31] A. et J. Unterberger, Quantiﬁcation et analyse pseudo-diﬀ´ erentielle.,Ann. Scient. Ec. Norm. Sup. 4e
s´ erie, t.21 (1988) 133–158.
[32] A. et J. Unterberger, La s´ erie discr` ete de SL(2,R) et les op´ erateurs pseudo-diﬀ´ erentiels sur une demi-
droite, Ann. Scient. Ec. Norm. Sup. 4e s´ erie, t.17 (1984) 83–116.
[33] A. Weinstein, “Traces and triangles in symmetric symplectic spaces,” Contemp. Math. 179 (1994)
262–270.
[34] P. Bieliavsky; Espace sym´ etriques symplectiques, PhD. thesis, ULB 1995.
[35] B. Kostant, Quantization and unitary representations ; Lectures in modern analysis and applications,
III, pp. 87–208. Lecture Notes in Math., Vol. 170, Springer, Berlin, 1970.
25
[36] Kirillov, A. A. Elementy teorii predstavleni˘ ı. (Russian) [Elements of the theory of representations]
Izdat. “Nauka”, Moscow, 1972.
[37] S. Helgason, “Diﬀerential Geometry, Lie Groups, and Symmetric Spaces,” Academic Press, 1978.
[38] P. Bieliavsky, “Strict quantization of solvable symmetric spaces,” J. Sympl. Geom. 1, no 2 (2002)
269–320.
[39] Bieliavsky, Pierre; Bonneau, Philippe; Maeda, Yoshiaki Universal deformation formulae, symplectic
Lie groups and symmetric spaces. Paciﬁc J. Math. 230 (2007), no. 1, 41–57.
[40] Bieliavsky, Pierre; Bonneau, Philippe “On the geometry of the characteristic class of a star product
on a symplectic manifold.” Rev. Math. Phys. 15, no. 2 , (2003) 199–215.
[41] G. N. Watson, A treatise on the Theory of Bessel Function – second edition, Cambridge Univ. Press.
(1966)
[42] Connes, Alain; Moscovici, “Henri Rankin-Cohen brackets and the Hopf algebra of transverse geome-
try”. Mosc. Math. J. 4 (2004), no. 1, 111–130.
[43] Zagier, D. Modular forms and diﬀerential operators. K. G. Ramanathan memorial issue, Proc. Indian
Acad. Sci. Math. Sci. 104 (1994), no. 1, 57–75.
[44] P. Bieliavsky and M. Massar, “Oscillatory integral formulae for left-invariant star products on a class
of Lie groups.,” Lett. Math. Phys. 58 (2001) 115–128.
26
