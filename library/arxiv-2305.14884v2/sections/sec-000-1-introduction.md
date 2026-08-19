---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further"
---
2. Preliminaries 5
2.1. The Faddeev quantum dilogarithm 5
2.2. Neumann–Zagier data 6
2.3. Geometric aspects 8
3. Formal Gaussian integration 9
3.1. Basics on formal Gaussian integration 9
3.2. q–holonomic aspects of ψ ℏ 10
3.3. Fourier transform of ψ ℏ 12
3.4. Pentagon identity for ψ ℏ 14
3.5. Inversion formula for ψ ℏ 17
4. Elementary invariance properties 18
5. Invariance under the choice of quad 19
6. Invariance under Pachner moves 23
6.1. The case of B with full rank 25
6.2. The case of B with nullity one 27
6.3. The case of B with nullity two 33
7. The series of the simplest hyperbolic 4 1 knot 39
Acknowledgements 41
Appendix A. Complements on the Fourier transform 41
Appendix B. Complements on the pentagon identity 43
References 46
Date: 11 July 2023.
Key words and phrases : 3-manifolds, knots, Kashaev invariant, Teichm¨ uller TQFT, comple x Chern–
Simons theory, hyperbolic geometry, asymptotic expansions, per turbation theory, Feynman diagrams, Fad-
deev quantum dilogarithm, state-integrals, volume conjecture, id eal triangulations, Neumann-Zagier data,
half-symplectic matrices, 2–3 Pachner moves, Fourier transform , pentagon.
1
2 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WHE ELER
1. Introduction
This paper concerns the topological invariance of a formal power s eries associated to an
ideally triangulated 3-manifold M with a torus boundary component [ 11]. The series is
deﬁned by formal Gaussian integration of a ﬁnite dimensional integr al (a so-called “state-
integral”) and it is expected to coincide to all orders with the asympt otic expansion of three
important topological invariants of 3-manifolds.
The ﬁrst is the Kashaev invariant of a hyperbolic knot [ 25], where Kashaev’s famous
volume conjecture is reﬁned to an asymptotic statement to all ord ers in perturbation theory
using the above formal power series. This was studied in detail in [ 21] based on extensive
numerical computations, but it is only proven for a handful of hype rbolic knots.
The second invariant is the Andersen–Kashaev state integral [ 2], whose asymptotic ex-
pansion for the simplest hyperbolic 4 1 knot was shown to agree with the above series in [ 2,
Sec.12], and also observed numerically for the ﬁrst three simplest hy perbolic knots in [ 20].
The state-integrals of [ 2] are ﬁnite-dimensional integrals whose integrand is a product of
Faddeev quantum dilogarithms times an exponential of a quadratic f orm, assembled from
an ideal triangulation of a 3-manifold with torus boundary componen ts. Andersen–Kashaev
proved that these are topological invariants that are the partitio n function of the Teichm¨ uller
TQFT [2, 1], which is a 3-dimensional version of a quantization of Teichm¨ uller space [26, 17].
A third invariant is the Chern–Simons theory with complex gauge grou p SL 2( /BV ) . This
theory was introduced by Witten [ 38] and studied extensively by Gukov [ 23]. Although
Chern–Simons theory with compact gauge group SU(2) has an exac t nonperturbative deﬁni-
tion given by the so-called Witten–Reshetikhin–Turaev invariant [ 37, 33] and a well–deﬁned
perturbation theory involving Feynman diagrams with uni-trivalent v ertices [ 3, 4], the same
is not known for Chern–Simons theory with complex gauge group SL 2( /BV ). For reasons that
are not entirely understood, the partition function of complex Che rn–Simons theory for
3-manifolds with torus boundary reduces to a ﬁnite-dimensional st ate-integral, as if some
unknown localization principle holds. The corresponding state-integ rals were introduced and
studied by Hikami [ 24], Dimofte [ 10] and others [ 12]. Unfortunately, in those works the in-
tegration contour was not pinned down, and this problem was ﬁnally d ealt with in [ 2] and,
among other things, implied topological invariance of the state-inte grals, which were coined
to be the partition function of Teichm¨ uller TQFT. But ignoring the co ntour of integration,
and focusing on a critical point of the action, which is a solution to a sy stem of polynomial
equations, allowed [ 11] to give a deﬁnition of the formal power series that are the main fo-
cus of our paper. Note, however, that the Feynman diagrams of [ 11] involve stable graphs
of arbitrary valency, a perturbative deﬁnition of Chern–Simons th eory with complex gauge
groups would involve uni-trivalent graphs.
The above discussion points out several aspects of these formal power series and conjectural
relations to perturbation theory of complex Chern–Simons and of T eich¨ uller TQFT. Aside
from conjectures, this paper concerns a theorem, the topologic al invariance of the above
formal power series.
Let us brieﬂy recall the key ingredients that go into the deﬁnition of the series, and
discuss those in detail in later sections. The ﬁrst ingredient is an idea l triangulation T
with N ideal tetrahedra of a 3-manifold M with torus boundary. Each tetrahedron has
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 3
shapes z ∈ /BV \ { 0, 1}, z′ = 1/(1 −z) and z′′ = 1 − 1/z attached to its three pairs of
opposite edges, and the shapes satisfy a system of polynomial equ ations (so-called “gluing
equations” [ 34] or Neumann-Zagier equations [ 29]) determined by the combinatorics of the
triangulation, one for each edge and peripheral curve. After som e choices are made (such
as an ordering of the tetrahedra and their edges, a choice of shap e for each tetrahedron,
a choice of an edge to remove from the gluing equations, and a choice of peripheral curve
to include), one obtains two matrices A and B with integer entries such that ( A |B) is the
upper-half of a symplectic 2 N × 2N matrix, as well as a vector ν ∈ /CI
N . In addition, we
choose a solution z = (z1,...,z N ) of the gluing equations as well as a ﬂattening ( f,f ′′), i.e.,
an integer solution to the equation ν =Af +Bf ′′. The power series Φ Ξ (ℏ) depends on the
tuple Ξ = ( A,B,ν,z,f,f ′′), which we collectively call a NZ-datum.
The next ingredient that goes in the deﬁnition of Φ Ξ (ℏ) is an auxiliary formal power series
ψℏ(x,z ) := exp
(
−
∑
k,ℓ∈/CI
≥0
k+ ℓ
2 >1
Bkxℓ ℏk+ ℓ
2 −1
ℓ!k! Li2−k−ℓ(z)
)
∈ 1 + ℏ
1
2
/C9 [z, (1 −z)−1][x]/llbracketℏ
1
2 /rrbracket. (1)
This series, which diﬀers from the one given in [ 11, Eq. 1.9] by a factor of exp
(1
12ℏ − 1
2xℏ
1
2
)
,
comes from the asymptotics of the inﬁnite Pochhammer symbol (als o known as the quantum
dilogarithm)
(x;q)∞ =
∞∏
k=0
(1 −qkx) = exp
(
−
∞∑
n=1
xn
n(1 −qn)
)
. (2)
Explicitly, for complex numbers x and z with |z| < 1 and Re( ℏ) < 0 we have (see [ 39] and
also [ 22, Lem.2.1])
(zexℏ1/2
;eℏ)−1
∞ ∼ 1√1 −z exp
(
− Li2(z)
ℏ − Li1(z)x
ℏ
1
2
− Li0(z)x2
2
)
ψℏ(x,z ), (ℏ → 0). (3)
Assuming that the matrix B is invertible, (i.e., that det( B) ⁄= 0), we introduce the function
f Ξ
ℏ (x,z ) = exp
(ℏ
1
2
2 xt1 − ℏ
1
2
2 xtB−1ν + ℏ
8ftB−1Af
) N∏
i=1
ψℏ(xi,zi) ∈ /C9 (z)[x]/llbracketℏ
1
2 /rrbracket, (4)
which is the product of one quantum dilogarithm per tetrahedron (e ach with its own integra-
tion variable), with some additional terms coming from the NZ-datum wherex = (x1,...,x N )t
and z = (z1,...,z N ).
The last ingredient is the formal Gaussian integration [ 5]
⟨fℏ(x,z )⟩x,Λ := exp

 1
2
N∑
i,j=1
(Λ −1)i,j
∂
∂xi
∂
∂xj

fℏ(x,z )
⏐
⏐
⏐
x=0
=
∫
e− 1
2xtΛ xfℏ,z(x)dx
∫
e− 1
2xtΛ xdx
∈ /C9 (z)/llbracketℏ/rrbracket(5)
of a power series fℏ(x,z ) ∈ /C9 (z)[x]/llbracketℏ
1
2 /rrbracket, with respect to an invertible matrix Λ. Assuming
further that the symmetric matrix
Λ = −B−1A + diag(1/(1 −zj)) (6)
is invertible, we deﬁne
4 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WHE ELER
Φ Ξ (ℏ) = ⟨f Ξ
ℏ (x,z )⟩x,Λ ∈ /C9 (z)/llbracketℏ/rrbracket. (7)
Using a solution z of the Neumann–Zagier equations that corresponds to the discre te
faithful representation ρgeom :π1(M) → PSL2( /BV ) of a cusped hyperbolic 3-manifold M, one
obtains a series Φ Ξ (ℏ) with coeﬃcients in the invariant trace ﬁeld of M. Our main theorem
is the following.
Theorem 1.1. Φ Ξ (ℏ) is a topological invariant of a cusped hyperbolic 3-manifol d.
A corollary of the above theorem is that every coeﬃcient of the abo ve series is a topological
invariant of a cusped hyperbolic 3-manifold. These topological invar iants have a geometric
origin, since they take values in the invariant trace ﬁeld of the manifo ld, and hence they are
algebraic, but not (in general) rational, numbers. This series seems to come from hyperbolic
geometry (though a deﬁnition of these invariants in terms of the hy perbolic geometry of the
3-manifold is not known), and perhaps not from enumerative quant um ﬁeld theory (such
as the Gromov–Witten or any of the 4-dimensional known theories) . The behavior of these
series under ﬁnite cyclic coverings of cusped hyperbolic 3-manifolds is given in [
19], and the
formulas presented there (e.g., for the coeﬃcient of ℏ2) point to unknown connections with
the spectral theory of hyperbolic 3-manifolds.
The proof of our theorem combines the ideas of the topological inva riance of the Andersen–
Kashaev state-integrals [ 2] with those of the Aarhus integral [ 4]. We brieﬂy recall that the
building block for the state-integral is the Faddeev quantum dilogar ithm, the state-integral
is a ﬁnite-dimensional integral of a product of Faddeev quantum dilo garithm [ 15], one for
each tetrahedron of an (ordered) ideal triangulation. Aside from elementary choices, two
important parts in the proof of topological invariance of the state -integral is invariance
under (a) the choice of a nondegenerate quad, and (b) 2–3 order ed Pachner moves, the latter
connecting one ideal triangulation with another. In [ 2], (a) and (b) are dealt with a Fourier
transform and a pentagon identity for the Faddeev quantum diloga rithm.
The power series Φ Ξ (ℏ) is given instead by a formal Gaussian integral (as opposed to
an integral over Euclidean space), where the building block is the for mal power series ψℏ
