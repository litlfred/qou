---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-027-51-critical-points
section_title: "Critical points"
section_number: 5.1
pages: 30-32
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
solutions to the gluing equations
(5.3) critical points ←→ zA(1−z−1)B = (−1)ν,
with z = exp(Z). In particular, the critical points are isolated. Then, choosing th e discrete
faithful solution to (
5.3), we formally expand the state integral to ﬁnd that
• ST , 0, the evaluation of leading-order part of the integrand at the critic al point, is the
complex volume of M;
• exp(−2ST , 1) is expressed as the determinant of a Hessian matrix
H =−B−1A + ∆ −1
1−z,
with a suitable monomial correction, and reproduces the torsion ( 1.8); and
• the higherST ,n are obtained via a ﬁnite-dimensional Feynman calculus, and explicitly
appear as rational functions of shape parameters.
It follows from the formalism of [ Dim], reviewed in Appendix C, that the state integral
(5.2) is only well deﬁned up to multiplicative prefactors of the form
(5.4) exp
(π2
6ℏa + iπ
4b + ℏ
24c
)
, a, b, c ∈ Z.
This means that we only obtain
(
ST , 0,τ T = 4π3e−2ST , 1,S T , 2
)
modulo
(π 2
6 Z, i, 1
24 Z
)
, respec-
tively; however, all the higher invariantsST ,n ≥3 should be unambiguous. Moreover, in Section
3 we saw that the ambiguity in τT could be lifted 6 to a sign ±1. Although the construction
of the asymptotic series ( 5.1) appears to depend on T , we certainly expect that
Conjecture 5.1. The invariants
{
ST ,n
} ∞
n=0 are independent of the choice of regular trian-
gulation and Neumann-Zagier datum (including the choice of quad typ e with det B⁄= 0,
etc.), up to the ambiguity (
5.4), and thus constitute topological invariants of M.
We now proceed to analyze the critical points and asymptotics of ( 5.2) in greater detail.
In Section 5.5, we will also generalize the state integral to arbitrary representa tions, with
non-unit meridian eigenvalue m = eu ⁄= 1, and give an example of ST , 2(m), ST , 3(m) as
functions on the character variety Y geom
M for the ﬁgure-eight knot.
5.1. Critical points. We begin by showing that the critical points of ( 5.2) are indeed
solutions to the gluing equations. For this purpose, we need to know the quantum dilogarithm
ψℏ(Z). The latter is given by [ DGLZ09, Eqn.3.22]
(5.5) ψℏ(Z) =
∞∏
r=1
1−qre−Z
1− (Lq)−r+1e−LZ ,
6It may also be possible to lift the ambiguities in ST ,0 and ST ,2 by using ordered triangulations, as in
[Neu04] or [ Zic09].
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 31
for|q|< 1, where
(5.6) q := exp ℏ, Lq := exp−4π2
ℏ , LZ := 2πi
ℏ Z.
The quantum dilogarithm ψℏ(Z) coincides with the restriction to |q|< 1 of Faddeev’s quan-
tum dilogarithm [ Fad95], as follows from [ DGLZ09, Eqn.3.23]. ψℏ(Z) is the Chern-Simons
wavefunction of a single tetrahedron [ Dim]. The quantum dilogarithm has an asymptotic
expansion as ℏ→ 0, given by ( cf. [DGLZ09, Eqn.3.26])
ψℏ(Z)
ℏ→0
∼ exp
∞∑
n=0
Bn ℏn−1
n!
~Li2−n(e−Z)(5.7)
= exp
[ 1
ℏ
~Li2(e−Z) + 1
2
~Li1(e−Z)− ℏ
12z′ + ℏ3
720z(1 +z)z′3 +...
]
,
where Bn is the nth Bernoulli number, with B1 = 1/2.
The coeﬃcients of strictly positive powers of ℏ (i.e. n≥ 2) in the expansion are rational
functions ofz =eZ, but the two leading asymptotics — the logarithm and dilogarithm — are
multivalued and have branch cuts. In contrast, the function ψℏ(Z) itself is a meromorphic
function on C for any ﬁxed ℏ⁄= 0. Branch cuts in its asymptotics arise when families of
poles collide in the ℏ→ 0 limit. In the case of purely imaginary ℏ with Im ℏ> 0 (a natural
choice in the analytic continuation of SU(2) Chern-Simons theory), a careful analysis of this
pole-collision process leads to branch cuts for ~Li2 and ~Li1 that are diﬀerent from the standard
ones (Figure 9). We indicate the modiﬁed analytic structure of these two function s (really
functions of Z rather than e−Z) with an extra tilde.
2πi 
πi 
4πi 
− 2πi 
− 4πi 
0
Re( Z )
Im( Z )
~Li 1,2(e− Z )Li 1,2(e− Z )
2πi 
πi 
4πi 
− 2πi 
− 4πi 
0
Re( Z )
Im( Z )
Figure 9. Rotating the standard branch cuts of Li 2(e−Z) and Li 1(e−Z) to
produce ~Li2(e−Z) and ~Li1(e−Z), as functions of Z. The shaded region indicates
where the standard logarithms of shape parameters for the discr ete faithful
representation lie.
32 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
Now, the critical points of the integrand, at leading order 7 in the ℏ expansion, are solutions
to
0 = ∂
∂Zi
(
− π2
2 f· B−1ν−iπZ· B−1ν + 1
2Z· B−1AZ +
∑
i
~Li2(e−Zi)
)
=−iπ
(
B−1ν)i +
(
B−1AZ)i−~Li1(e−Zi),
in other words,
(5.8) AZ + B(−~Li1(e−Z)) = iπν.
Since exp[−~Li1(e−Zi)] = 1−z−1
i , we see that every solution to (
5.8) is a particular logarithmic
lift of a solution to the actual gluing equations zA(1−z−1)B = (−1)ν . It is a lift that precisely
satisﬁes the logarithmic constraints ( 2.6) of Section 2, with Z ′′
i =−~Li1(e−Zi).
When 0≤ ImZi≤π, the branches of the standard logarithms and dilogarithms agree w ith
those of the modiﬁed ones. In particular, given the discrete faithf ul solution tozA(1−z−1)B =
(−1)n, taking standard logarithms immediately produces a solution to ( 5.8). Therefore, the
discrete faithful representation always corresponds to a critica l point of the state integral.
