---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-022-c-quantum-lagrangian-calculations
section_title: "C Quantum Lagrangian calculations"
section_number: null
pages: 71-79
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
Here we calculate explicitly the quantum Lagrangian operators ˆLM that annihilate a few
indices, as promised in Section 4.5. We follow the computational framework delineated in
Section 4.5, or in [31].
Bipyramid
Let’s begin with the operators for the bipyramid theory. If we build the bipyramid from two
tetrahedra, we can start with two pairs of operators ˆ r′′
± + ˆr−1
± − 1, ˆs′′
± + ˆs−1
± − 1 that both
annihilate the product index I∆(mR,eR)I∆(mS,eS), as in Section 4.2. We could write this
somewhat more suggestively as
ˆr′′
± + ˆr−1
± − 1≃ 0, ˆs′′
± + ˆs−1
± − 1≃ 0, (C.1)
where by “≃” we mean “annihilates an appropriate index when acting on the left.” To be
completely explicit, the fundamental generators ˆr± = exp( ˆR±), ˆs± = exp( ˆS±), etc. act as
ˆR± = ℏ
2mR∓∂eR
ˆS± = ℏ
2mS∓∂eS,
ˆR′′
± = ℏ
2eR±∂mR
ˆS′′
± = ℏ
2eS±∂mS,
cf. (2.29). (These (ˆr, ˆr′′) and (ˆs, ˆs′′) are taking the place of what was called (ˆx, ˆp) in Step 1
above.) Now, in accordance with the change of polarization (4.7), we change variables to
ˆX1± = ˆR± + ˆS′′
±, ˆX2± = ˆR′′
± + ˆS±, ˆP1± = ˆR′′
±, ˆP2± = ˆS′′
±. (C.2)
Then the properly polarized index of the bipyramid,Ibip(m1,m 2,e 1,e 2) =I∆(m1−e2,e 1)I∆(m2−
e1,e 2) (4.8), is annihilated by
ˆL(1)
bip = ˆp1± + ˆx−1
1±ˆp2±− 1≃ 0, ˆL(2)
bip = ˆp2± + ˆx−1
2±ˆp1±− 1≃ 0. (C.3)
This is an obvious quantization of the bipyramid Lagrangian, given for example in Section 2
of [19]. There are no internal edges, so we are done.
Alternatively, we can use three tetrahedra. We start with three equations 36
ˆz′′ + ˆz−1− 1≃ 0, ˆw′′ + ˆw−1− 1≃ 0, ˆy + ˆy′−1− 1≃ 0, (C.4)
where for clarity we just use the ‘+’ operators and remove the subscript ±. In parallel to the
change of polarization (4.11), we change variables to
ˆX1 = ˆZ, ˆX2 = ˆW, ˆC = ˆZ + ˆW + ˆY ,
ˆP1 = ˆZ′′ + ˆY′, ˆP2 = ˆW′′ + ˆY′, ˆΓ =− ˆY′.
36Remember from Section 3.2 that the operator for a tetrahedron theory is cyclically invariant under per-
mutations of the shape parameters. Thus we can freely write the y equation using (ˆy′, ˆy) instead of (ˆy, ˆy′′), as
we did here.
– 70 –
Note that ˆp1ˆx1 = qˆx1ˆp1, ˆp2ˆx2 = qˆx2ˆp2, and ˆγˆc = qˆcˆγ. In terms of exponentiated operators,
the equations (C.4) become
ˆγ ˆp1 + ˆx−1
1 − 1≃ 0, ˆγ ˆp2 + ˆx−1
2 − 1≃ 0, ˆc ˆx−1
1 ˆx−1
2 + ˆγ− 1≃ 0. (C.5)
By multiplying on the left and taking diﬀerences of these equations, we can eliminate ˆγ from
(C.5), leaving two equations that only involve ˆ xi, ˆpi, ˆc. Setting ˆc→ q in these equations
recovers the Lagrangian operators (C.3).
Figure-eight knot
In order to build the operator for the ﬁgure-eight knot, it suﬃces to use the decomposition
into two tetrahedra. Let’s again just focus on ‘+’ operators. We start with ˆ z′′ + ˆz−1− 1≃ 0
and ˆw′′ + ˆw−1− 1≃ 0, and change variables to
ˆU = ˆZ− ˆW′′, ˆC = ˆZ′′ + ˆW′′− ˆZ− ˆW + 2πi + ℏ, ˆv = ˆZ′′− ˆZ, ˆΓ =− ˆW′′.
According to (semi)standard conventions in the mathematics literature, let us deﬁne ˆM =e ˆU
and ˆ𝓁 =−eˆv. The the two tetrahedron Lagrangians can then be rewritten as 37
−q
1
2
ˆM ˆ𝓁
ˆγ + ˆγ
ˆM
− 1≃ 0, 1
ˆγ−q− 1
2
ˆc ˆγ
ˆ𝓁
− 1≃ 0. (C.6)
Eliminating ˆγ from these equations is not entirely trivial, but can be done by hand. After
doing so and setting ˆc→ 1, what results is a single operator
ˆL41 =
(
q
1
2 ˆM−q− 1
2 ˆM−1)
𝓁−1−
( ˆM− ˆM−1)( ˆM−2− ˆM−1−q−q−1− ˆM+ ˆM 2)
+
(
q− 1
2 ˆM−q
1
2 ˆM−1)ˆ𝓁,
(C.7)
which annihilates the ﬁgure-eight knot index I41(m,e ) in (4.18). Here ˆM and ˆ𝓁 act in the
‘+’ representation, so that
ˆM =e
ˆU = exp
( ℏ
2m−∂e
)
, −ˆ𝓁 =eˆv = exp
( ℏ
2e +∂m
)
. (C.8)
The complementary ‘−’ operator is obtained from (C.7) by sending ˆM→ ˆM−, ˆ𝓁→ ˆ𝓁−, and
q→q−1.
The quantum Lagrangian (C.7) is well known in knot theory and Chern-Simons theory
as the “quantum A-polynomial” of the ﬁgure-eight knot [29, 31, 52]. 38
Trefoil
The quantum Lagrangian for the trefoil can be similarly obtained using our gluing rules, but
we can also just take the known result from knot theory. In terms of longitude and meridian
37One must be careful with factors of q in these equations when de-exponentiating. For example ˆ z′′ =
exp( ˆU + ˆv− ˆγ) =q
1
2 ˆM ˆ𝓁ˆγ−1 =q− 1
2 ˆ𝓁 ˆM ˆγ−1.
38It is easiest to compare (C.7) to the conventions of [29] or [31]. For example, (C.7) is identical to Eqn.
(1.8) of [31] upon setting ˆM→ ˆm2.
– 71 –
holonomy eigenvalues 𝓁 =−ev and M = eU, the classical Lagrangian ( i.e. the nonabelian
A-polynomial) for the trefoil is simply 𝓁 +M 3, which becomes quantized as
ˆL31 = ˆ𝓁 +q
3
2 ˆM 3. (C.9)
It is easy to check that this annihilates the delta-function index for the trefoil, I31(m,e ) =
δe,3m, with ˆ𝓁 and ˆM acting just as in (C.8). The index is also annihilated by the ‘ −’ version
of (C.9), namely ˆL31− = ˆ𝓁− +q− 3
2 ˆM 3
−.
D Tentacles and diﬀerence equations
In this appendix, we seek to motivate the relation between tentacles of a classical amoeba of
LM and “linear growth” in the index, as discussed in Section 4.6. We show how these two
phenomena are connected via quantized diﬀerence equations ˆLMIM = 0. Our argument is
heuristic, but indicates a path toward a more rigorous proof, given further information about
quantization and/or indices.
For simplicity, suppose that a theory 39 TM has a single U(1) symmetry, so that the
indexIM(m,e ;q) depends on a single pair of charges ( m,e ). Correspondingly, the classical
LagrangianLM (or a component of it) can be described by a single equation, which we just
write asLM(x,p ) = 0, with x,p ∈ C∗. Let us also suppose, without loss of generality, that
the amoeba of LM has a tentacle in the negative Re P direction, i.e.LM(x,p ) = 0 has a
solution with|p|→ 0 and x ﬁnite. Otherwise, we can use the Sp(2, Z) action to rotate any
other amoeba tentacle to this position.
Let us write
LM =a0(x) +a1(x)p +... +ad(x)pd. (D.1)
This polynomial is only well-deﬁned up to multiplication by monomials in x andp. The fact
thatLM(x,p ) = 0 has a solution at |p|→ 0 means that the coeﬃcient a0(x), multiplying the
lowest power of p, has a nontrivial root. In particular, a0(x)⁄= 1. If the tentacle is directly
on the negative ReP axis (as we would expect for character varieties of 3-manifolds, cf. [62]),
then the root must actually be on the unit circle; i.e.a0(x) = 0 for some|x| = 1. The simplest
example would be a0(x) = 1−x.
This property of the polynomial (D.1) is also familiar from the relation between amoebas
and Newton polygons. Namely, every tentacle of the amoeba is perpendicular to an edge
of the Newton polygon of LM. A tentacle in the −ReP direction means that the Newton
polygon has a “vertical” (x-direction) edge at the lowest power of p, which is the same thing
as saying that a0(x) is nontrivial.40
Now, the index is annihilated by quantized versions of (D.1),
ˆLM(ˆx+, ˆp+;q)IM = ˆLM(ˆx−, ˆp−;q−1)IM = 0. (D.2)
39This could actually be a general theory in class R; is still has a classical L and quantum operators ˆL.
40Meaning not a monomial. All equations and operators are deﬁned up to (left) multiplication by monomials.
– 72 –
Sometimes the degree of ˆLM in ˆp or ˆx jumps upon quantization, but we will assume here that
it does not (the jumping does not aﬀect the general story). Then we could write
ˆLM(ˆx+, ˆp+;q) =
d∑
n=0
ˆan(ˆx+;q)ˆpn
+, (D.3)
with ˆan(ˆx+;q)→an(x) asq→ 1, and similarly for the (−) operators. In particular, ˆa0(ˆx±;q±)
is a nontrivial (classical!) polynomial in ˆx±, with q-dependent coeﬃcients.
We want to consider the behavior of the index atm = 0 and large positive electric charge
e. For this, the operators ˆx±, ˆp± are not convenient, because they combine shifts in e andm.
Recall from Section 2.5 that (ˆx±, ˆp±) = (e ˆX±,e ˆP±) with
ˆX+ = ℏ
2m−∂e, ˆP+ = ℏ
2e +∂m,
ˆX− = ℏ
2m +∂e, ˆP− = ℏ
2e−∂m.
(D.4)
We can rotate (D.4) to deﬁne a more useful set of operators
ˆη =
√
ˆx−
ˆx+
=e∂e, ˆϵ = ˆp+ˆp− =qe ; ˆ ηm =
√
ˆp+
ˆp−
=e∂m, ˆϵm = ˆx+ˆx− =qm. (D.5)
Quantum-mechanically, it should then be possible to work in the left ideal generated by
LM(ˆx+, ˆp+;q) andLM(ˆx−, ˆp−;q), and eliminate the combination ˆηm, leaving a single operator
ˆEM(ˆη, ˆϵ, ˆϵm;q)IM = 0 (D.6)
that does not shift m. This operator must still annihilate the index.
In the classical limit q→ 1, ˆEM reduces to a classical polynomial EM(η,ϵ,ϵ m). This
polynomial is the result of taking (redundant) complex conjugate equations
LM(x,p ) = 0, LM(¯x, ¯p) = 0, (D.7)
setting η =
√
¯x/x =e−i ImX, ϵ =|p|2, ηm =
√
p/p =ei ImP , ϵm =|x|2, and eliminating the
phase ηm. Thus, EM(η,ϵ,ϵ m) is half-way along to deﬁning the amoeba of LM! Let us write
EM(η,ϵ,ϵ m) =EM
(√
¯x
x,|p|2,|x|2
)
=
d′
∑
n=0
bn(η,ϵm)ϵn. (D.8)
It is not hard to see, by analyzing the limit|p|→ 0, that our ansatz about the amoeba of LM
implies that bn is a nonconstant (non-monomial) polynomial. This is because any solution
toLM = 0 must be a solution to EM = 0. In fact, if we also ﬁx ϵm = 1 (this is the classical
equivalent of setting m = 0 in the index), then η =x−1, and the same root of a0(x) in (D.1)
must be root of b0(x)≡b0(x−1, 1). In particular, if a0(x) has a root on the unit circle, then
b0(x−1, 1) should contain a cyclotomic factor.
– 73 –
What does this ﬁnally imply for the index? The operator ˆEM deﬁnes a recursion relation
forIM that only shifts e. We are therefore free to set m = 0, obtaining
ˆEM(ˆη, ˆϵ, 1;q)IM(0,e ;q) = 0, (D.9)
or
d′
∑
n=0
ˆϵn ˆbn(ˆη, 1;q)IM(0,e ;q) =
d′
∑
n=0
qne ˆbn(e∂e, 1;q)IM(0,e ;q) = 0, (D.10)
for some q-deformed polynomials ˆbn(e∂e, 1;q) that reduce to bn(η, 1) = bn(x−1, 1) as q→ 1.
Now, suppose that the powers of q appearing inIM(m,e ;q) at ﬁnite (m,e ) are bounded from
below, as they are for theories TM; and let us see what happens if the minimum power grows
linearly at m = 0, i.e.
IM(0,e ;q)∼qαe(
1 +O(q)
)
(D.11)
for some α. After plugging (D.11) into (D.10), we can try to take the limit q→ 0. Since the
operator e∂e only modiﬁes the ansatz (D.11) by constant factors of q at leading order, only
the n = 0 term of the sum (D.10) will contribute as q→ 0. This term must vanish by itself.
That is:
ˆb0(e∂e, 1;q)IM(0,e ;q) = ˆb0(e∂e, 1;q)qαe(
1 +O(q)
)
= ˆb0(qα, 1;q)qαe(
1 +O(q)
)
= 0 (D.12)
at leading order in q. One way to satisfy (D.12) is to have
ˆb0(qα, 1;q) = 0 , (D.13)
which is only possible if ˆb0(x−1, 1;q) is a nontrivial polynomial in x. But we know from our
analysis that when the amoeba of LM has a tentacle along the negative Re P axis,b0(x−1, 1)
has a cyclotomic (or nontrivial) factor. The q-deformed version of this factor could then allow
a solution to (D.13). For the moment, this is the closest we can get to the mathematical
claim/conjecture that tentacles of the amoeba allow linear growth.
We note that (D.12) does not universally imply (D.13). For this, a bit more must be
known about the O(q) corrections to the index — for example, that they vanish (involve
higher and higher powers of q) as e→∞ . This is true in every calculated example of an
indexIM, and there is likely a physical argument to justify it. When (D.13) is true, the
leading polynomial ˆb0 determines the growth rate α.
If there is no tentacle of the amoeba lying on the negative Re P axis, then a0(x) and
b0(x, 1) are monomials, which generally implies that ˆb0(x−1, 1;q) is a monomial. Then it is
absolutely impossible to solve (D.13), and (again, with some assumption about O(q) correc-
tions) the linear ansatz (D.11) is excluded. The generic growth of the index is not linear but
quadratic. Having IM(0,e ;q)∼qαe2(
1 +O(q)
)
means that the operator e∂e can produce qe
factors, and then all the terms in the sum (D.10) can mix at leading order. This allows much
more general cancellations to occur.
– 74 –
References
[1] K. Intriligator and B. Wecht, The Exact Superconformal R-Symmetry Maximizes a , Nucl. Phys.
B667 (2003), no. 1-2 183–200, [ hep-th/0304128v3].
[2] D. L. Jaﬀeris, The Exact Superconformal R-Symmetry Extremizes Z , arXiv:1012.3210.
[3] K. Intriligator and N. Seiberg, Mirror Symmetry in Three Dimensional Gauge Theories , Phys.
Lett. B387 (1996) 513–519, [ hep-th/9607207v1].
[4] J. de Boer, K. Hori, H. Ooguri, and Z. Yin, Mirror Symmetry in Three-Dimensional Gauge
Theories, SL(2,Z) and D-Brane Moduli Spaces , Nucl. Phys. B493 (1996) 148–176,
[hep-th/9612131v1].
[5] O. Aharony, A. Hanany, K. Intriligator, N. Seiberg, and M. J. Strassler, Aspects of N=2
Supersymmetric Gauge Theories in Three Dimensions , Nucl. Phys. B499 (1997), no. 1-2 67–99,
[hep-th/9703110v1].
[6] J. de Boer, K. Hori, and Y. Oz, Dynamics of N=2 Supersymmetric Gauge Theories in Three
Dimensions, Nucl. Phys. B500 (1997) 163–191, [ hep-th/9703100v3].
[7] N. A. Nekrasov and S. L. Shatashvili, Supersymmetric vacua and Bethe ansatz , Nucl. Phys. B,
Proc. Suppl. 192-193 (2009) 91–112, [ arXiv:0901.4744].
[8] T. Dimofte, S. Gukov, and L. Hollands, Vortex Counting and Lagrangian 3-manifolds ,
arXiv:1006.0977.
[9] T. Dimofte and S. Gukov, Chern-Simons Theory and S-duality , arXiv:1106.4550.
[10] A. Kapustin, B. Willett, and I. Yaakov, Exact Results for Wilson Loops in Superconformal
Chern-Simons Theories with Matter , JHEP 1003 (2010) 089, [ arXiv:0909.4559]. Published in:
JHEP 1003:089,2010 32 pages.
[11] K. Hosomichi, S. Lee, and J. Park, AGT on the S-duality Wall , JHEP 1012 (2010) 079,
[arXiv:1009.0340].
[12] N. Hama, K. Hosomichi, and S. Lee, SUSY Gauge Theories on Squashed Three-Spheres ,
arXiv:1102.4716.
[13] J. Bhattacharya, S. Bhattacharyya, S. Minwalla, and S. Raju, Indices for Superconformal Field
Theories in 3,5 and 6 Dimensions , JHEP 0802 (2008) 064, [ arXiv:0801.1435].
[14] S. Kim, The complete superconformal index for N=6 Chern-Simons theory , Nucl. Phys. B821
(2009) 241–284, [ arXiv:0903.4172].
[15] Y. Imamura and S. Yokoyama, Index for three dimensional superconformal ﬁeld theories with
general R-charge assignments, arXiv:1101.0557.
[16] C. Krattenthaler, V. P. Spiridonov, and G. S. Vartanov, Superconformal indices of
three-dimensional theories related by mirror symmetry , JHEP 1106 (2011) 008,
[arXiv:1103.4075].
[17] A. Kapustin and B. Willett, Generalized Superconformal Index for Three Dimensional Field
Theories, arXiv:1106.2484.
[18] E. Witten, Phases of N=2 Theories In Two Dimensions , Nucl. Phys. B403 (1993) 159–222,
[hep-th/9301042v3].
– 75 –
[19] T. Dimofte, D. Gaiotto, and S. Gukov, Gauge Theories Labelled by Three-Manifolds ,
arXiv:1108.4389.
[20] D. Gaiotto, G. W. Moore, and A. Neitzke, Framed BPS States, arXiv:1006.0146.
[21] S. Gukov and E. Witten, Gauge Theory, Ramiﬁcation, and the Geometric Langlands Program ,
Curr. Devel. Math. 2006 (Dec, 2008) 35–180, [ hep-th/0612073v2].
[22] E. Witten, SL(2,Z) Action On Three-Dimensional Conformal Field Theories With Abelian
Symmetry, hep-th/0307041v3.
[23] W. D. Neumann and D. Zagier, Volumes of hyperbolic three-manifolds, Topology24 (1985),
no. 3 307–332.
[24] S. J. Bloch, Higher regulators, algebraic K-theory, and zeta functions of elliptic curves , Lecture
notes, UC Irvine 11 (1978).
[25] J. L. Dupont and C. H. Sah, Scissors congruences. II, J. Pure Appl. Algebra 25 (1982), no. 2
159–195.
[26] W. D. Neumann and J. Yang, Bloch invariants of hyperbolic 3-manifolds , Duke Math. J. 96
(Jan, 1999) 29–59, [ math/9712224v1].
[27] Y. Terashima and M. Yamazaki, SL(2,R) Chern-Simons, Liouville, and Gauge Theory on
Duality Walls , arXiv:1103.5748.
[28] S. Gukov, Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial ,
Commun. Math. Phys. 255 (2005), no. 3 577–627, [ hep-th/0306165v1].
[29] T. Dimofte, S. Gukov, J. Lenells, and D. Zagier, Exact Results for Perturbative Chern-Simons
Theory with Complex Gauge Group , Comm. Num. Thy. and Phys. 3 (2009), no. 2 363–443,
[arXiv:0903.2472].
[30] E. Witten, Analytic Continuation of Chern-Simons Theory , arXiv:1001.2933.
[31] T. Dimofte, Quantum Riemann Surfaces in Chern-Simons Theory , arXiv:1102.4847.
[32] D. Gaiotto, G. W. Moore, and A. Neitzke, Four-dimensional wall-crossing via three-dimensional
ﬁeld theory, Comm. Math. Phys. 299 (2010), no. 1 163–224, [ arXiv:0807.4723].
[33] D. Gaiotto, N=2 dualities, arXiv:0904.2715.
[34] S. Cecotti, C. Cordova, and C. Vafa, Braids, Walls, and Mirrors , arXiv:1110.2115.
[35] L. F. Alday, D. Gaiotto, and Y. Tachikawa, Liouville Correlation Functions from
Four-Dimensional Gauge Theories, Lett. Math. Phys. 91 (2010), no. 2 167–197,
[arXiv:0906.3219].
[36] L. F. Alday, D. Gaiotto, S. Gukov, Y. Tachikawa, and H. Verlinde, Loop and Surface Operators
in N=2 Gauge Theory and Liouville Modular Geometry , JHEP 1001 (2010) 113,
[arXiv:0909.0945].
[37] N. Drukker, J. Gomis, T. Okuda, and J. Teschner, Gauge Theory Loop Operators and Liouville
Theory, JHEP 1002 (2010) 057, [ arXiv:0909.1105].
[38] N. Drukker, D. Gaiotto, and J. Gomis, The Virtue of Defects in 4D Gauge Theories and 2D
CFTs, arXiv:1003.1112.
– 76 –
[39] C. K. Zickert, The Extended Bloch Group and Algebraic K-Theory , arXiv:0910.4005.
[40] S. Garoufalidis, D. P. Thurston, and C. K. Zickert, The complex volume of
SL(n,C)-representations of 3-manifolds, arXiv:1111.2828.
[41] V. V. Fock and A. B. Goncharov, Moduli Spaces of Local Systems and Higher Teichmuller
Theory, Publ. Math. Inst. Hautes Etudes Sci. 103 (2006) 1–211, [ math/0311149v4].
[42] E. Witten, Fivebranes and Knots , arXiv:1101.3216.
[43] J. Kinney, J. Maldacena, S. Minwalla, and S. Raju, An Index for 4 dimensional Super
Conformal Theories, Commun. Math. Phys. 275 (2007) 209–254, [ hep-th/0510251v4].
[44] E. Witten, Constraints on supersymmetry breaking, Nucl. Phys. B202 (1982), no. 2 253–316.
[45] G. Festuccia and N. Seiberg, Rigid Supersymmetric Theories in Curved Superspace ,
arXiv:1105.0689.
[46] S. Minwalla, Restrictions Imposed by Superconformal Invariance on Quantum Field Theories ,
Adv. Theor. Math. Phys. 2 (1998) 781–846, [ hep-th/9712074v2].
[47] D. Gaiotto and E. Witten, S-Duality of Boundary Conditions In N=4 Super Yang-Mills Theory ,
Adv. Theor. Math. Phys. 13 (2009), no. 2 721–896, [ arXiv:0807.3720].
[48] B. Feng and A. Hanany, Counting Gauge Invariants: the Plethystic Program , JHEP 0703
(2007) 090, [ hep-th/0701063v2].
[49] V. Borokhov, A. Kapustin, and X. Wu, Monopole Operators and Mirror Symmetry in Three
Dimensions, JHEP 0212 (2002) 044, [ hep-th/0207074v2].
[50] W. Thurston, The Geometry and Topology of Three-Manifolds , Lecture notes at Princeton
University (1980).
[51] S. Garoufalidis and T. T. Le, The Colored Jones Function is q-Holonomic , Geom. Topol. 9
(2005) 1253–1293, [ math/0309214v3].
[52] S. Garoufalidis, On the Characteristic and Deformation Varieties of a Knot , Geom. Topol.
Monogr. 7 (2004) 291–304, [ math/0306230v4].
[53] J. H. Conway, An enumeration of knots and links, and some of their algebraic properties ,
Computational Problems in Abstract Algebra (Ed. J. Leech), Pergamom Press, Oxford (1970)
329–358.
[54] H. R. Morton and P. Traczyk, The Jones polynomial of satellite links around mutants , Braids,
Contemp. Math. (AMS) 78 (1988) 587–592.
[55] D. W. Boyd, F. Rodriguez-Villegas, and N. M. Dunﬁeld, Mahler’s Measure and the Dilogarithm
(II), Canad. J. Math. 54 (2002), no. 3 468–492, [ math/0308041v2].
[56] H. Segerman, A generalisation of the deformation variety , arXiv:0904.1893.
[57] N. M. Dunﬁeld and S. Garoufalidis, Incompressibility criteria for spun-normal surfaces ,
arXiv:1102.4588.
[58] S. Tillmann, Degenerations of ideal hyperbolic triangulations , math/0508295v4.
[59] D. Coulson, O. Goodman, C. Hodgson, and W. Neumann, Computing Arithmetic Invariants of
3-Manifolds, Experiment. Math. 9 (2000), no. 1 127–152.
– 77 –
[60] M. Culler, N. Dunﬁeld, and J. R. Weeks, SnapPy, a computer program for studying the
geometry and topology of 3-manifolds , . http://snappy.computop.org.
[61] T. Dimofte, D. Gaiotto, and R. van der Veen, Seiberg-Witten Duality Walls and Hybrid
Triangulations, in preparation.
[62] D. Cooper, M. Culler, H. Gillet, and D. Long, Plane Curves Associated to Character Varieties
of 3-Manifolds, Invent. Math. 118 (1994), no. 1 47–84.
[63] I. M. Gel’fand, M. M. Kapranov, and A. V. Zelevinsky, Discriminants, resultants, and
multidimensional determinants, Mathematics: Theory and Applications, Birkhauser, Boston
(1994) x+523.
[64] S. Garoufalidis, The Jones slopes of a knot , arXiv:0911.3627.
[65] A. Stoimenow and T. Tanaka, Mutation and the colored Jones polynomial , J. Goekova Geom.
Topol. math.GT (2009), no. 3 44–78, [ math/0607794v3].
[66] D. Green, Z. Komargodski, N. Seiberg, Y. Tachikawa, and B. Wecht, Exactly Marginal
Deformations and Global Symmetries , JHEP 1006 (2010) 106, [ arXiv:1005.3546].
[67] A. Kapustin, Wilson-’t Hooft operators in four-dimensional gauge theories and S-duality , Phys.
Rev. D74 (2006), no. 2 025005, [ hep-th/0501015v3].
[68] A. Gadde, L. Rastelli, S. S. Razamat, and W. Yan, Gauge Theories and Macdonald
Polynomials, arXiv:1110.3740.
[69] J. Gomis, T. Okuda, and V. Pestun, Exact Results for ’t Hooft Loops in Gauge Theories on S4 ,
arXiv:1105.2568.
[70] E. Witten, Quantum Field Theory and the Jones Polynomial , Comm. Math. Phys. 121 (1989),
no. 3 351–399.
[71] E. Witten, Quantization of Chern-Simons Gauge Theory with Complex Gauge Group ,
Commun. Math. Phys 137 (1991) 29–66.
[72] S. Pasquetti, Factorisation of N = 2 theories on the squashed 3-sphere , arXiv:1111.6905.
[73] E. Witten, 2+1 dimensional gravity as an exactly soluble system , Nucl. Phys. B311 (Jan, 1988)
46.
[74] N. Hitchin, The self-duality equations on a Riemann surface , Proc. London Math. Soc (1987).
[75] N. Woodhouse, Geometric quantization, New York: Oxford Univ. Press (Jan, 1992).
[76] S. Gukov and E. Witten, Branes and Quantization , Adv. Theor. Math. Phys. 13 (2009), no. 5
1445–1518, [arXiv:0809.0305].
[77] D. Shale, Linear Symmetries of Free Boson Fields , Trans. Amer. Math. Soc. 103 (1962)
149–167.
[78] A. Weil, Sur Certains Groupes d’Op´ erateurs Unitaires, Acta Math. 111 (1964) 143–211.
– 78 –
