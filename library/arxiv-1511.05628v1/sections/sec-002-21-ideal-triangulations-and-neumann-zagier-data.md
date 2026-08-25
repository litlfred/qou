---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-002-21-ideal-triangulations-and-neumann-zagier-data
section_title: "Ideal triangulations and Neumann-Zagier data"
section_number: 2.1
pages: 4-6
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
troduced by Thurston as an eﬃcient way to describe (algebraically, or numerically) 3-
dimensional hyperbolic manifolds. For a leisure introduction, the reader may consult Thurston’s
original notes [Thu77], the exposition of Neumann–Zagier [NZ85] and Weeks [Wee05] and
the documentation of SnapPy [CDW]. The shape of a 3-dimensional hyperbolic tetrahedra
is a complex number z∈ C\{ 0, 1}. Letting z′ = (1−z)−1 and z′′ = 1−z−1, the edges
of an oriented ideal tetrahedron of shape z can be assigned complex numbers according to
Figure 1.
z
z
￿
z
￿￿
z
￿
z
￿￿
z
￿￿
(0)
(1)
(∞ )
(z)
Figure 1. An ideal tetrahedron with a shape assignement.
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 5
Let M be an oriented hyperbolic manifold with one cusp (for instance a hyperbolic knot
complement) andT an ideal triangulation ofM containingN tetrahedra. In [DG13a] the au-
thors introduced a Neumann-Zagier datum ofT . The latter is a tuple γ = (A, B,ν,z,f,f ′′)
that consists of:
(a) Two matrices A, B∈ GL(N, Z) and a vector ν∈ ZN encoding the coeﬃcients of
Thurston’s gluing equations for the triangulation ( N− 1 independent equations im-
posing trivial holonomy around edges, and one equation imposing parabolic holonomy
around the cusp).
(b) An N-tuplez = (z1,...,z N)∈ C\{0, 1} of shape parameters, with each zi parametriz-
ing the shape of the i-th tetrahedron, satisfying the gluing equations in the form
zAz′′B = (−1)ν, i.e.
(5)
∏
i
z
Aji
i (1−z−1
i )Bji = (−1)νj for all j = 1,...,N.
(c) Two N-tuples f,f′′∈ ZN satisfying
(6) Af + Bf′′ =ν.
These provide a combinatorial ﬂattening in the sense of [Neu92]. The integers f,f′′,
and f′ = 1−f−f′′ also label edges of tetrahedra, with the property that the sum
around any edge of the triangulation is 2.
The Neumann-Zagier datum depends not just on the triangulation T but also on which
edges of each tetrahedron are labelled by the distinguished shape parameter zi; this 3N-fold
choice has been called a choice of “quad” or “gauge.”.
Neumann and Zagier [NZ85] proved that (A B) forms the top half of a symplectic matrix,
i.e. that ABT is symmetric and ( A B) has full rank. It follows that if B is invertible, then
B−1A is symmetric. We will call a Neumann-Zagier datum Z-nondegeretate if B is invertible
over the integers.
Fix a positive integer k. If γ is a Neumann-Zagier datum, let
(7) ζ =e
2πi
k , θ i =z1/k
i ,
whereθi are chosen so thatθk
i =zi. This deﬁnes number ﬁelds F = Q(z1,...,z N),Fk =F (ζ),
and FG,k =Fk(θ1,...,θ N), such that
(8) F⊂Fk⊂FG,k.
Observe thatFG,k/Fk is the abelian Galois (Kummer) extension with groupG = (Z/kZ)N =
⟨σ1,...,σ N⟩ where
(9) σj(θi) =ζ−δi,jθi
whereδi,j is Kronecker’s delta function. For the basic properties of Kummer theory, see [Lan02,
Sec.VI.8].
Below, we will construct a series φγ,ζ(ℏ) for the k-th root of unity ζ = exp(2πi/k). Then,
after proving in Theorems 2.2 and 2.6 that the coeﬃcients in this series belong to Fk, the
seriesφγ,ζp(ℏ) for any otherk-th root of unityζp = exp(2πip/k) can be obtained fromφγ,ζ(ℏ)
by a Galois automorphism.
6 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
