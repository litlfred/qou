---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-006-8-st-ephane-baseilhac1-riccardo-benedetti-2
section_title: "ST ´EPHANE BASEILHAC1, RICCARDO BENEDETTI 2"
section_number: 8
pages: 9-11
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 27 sections: ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE"
---
Recall that π1(Mφ) is a HNN-extension of π1(S). That is, given a generating set γ1,...,γ u of π1(S)
satisfying the relations r1,...,r v, there is an isomorphism between π1(Mφ) and the group generated
by γ1,...,γ u and an element t satisfying the relations r1,...,r v and tαt−1 = φ∗(α) for all α ∈
π1(S), where φ∗ : π1(S)→ π1(S) is the isomorphism induced by φ. Therefore, every representation
r: π1(S)→ PSL (2, C) that may be extended to Mφ is such that r(π1(S)) and r◦φ∗(π1(S)) are
conjugate subgroups of PSL (2, C). Any augmented character of S that may be extended to Mφ is
thus a ﬁxed point of the map Φ ∗ : X(S)→X(S) induced by the map r↦→ r◦φ∗ on representations,
and i∗(X(Mφ)) is a subvariety of Fix(Φ∗).
Again in the setting of Section 2, let ( T, ˜b) be a weakly branched layered triangulation of the
ﬁbred cusped manifold Mφ. Let us recall a few facts about the gluing variety G(T, ˜b), that is, the
set of solutions of the Thurston gluing equations supported by ( T, ˜b). It is a complex aﬃne algebraic
set of dimension greater than or equal to r. The points of G(T, ˜b) are classically called systems of
shape parameters. Their coordinates, the shape parameters, are scalars in C\{ 0, 1} associated to
the abstract edges of T . The shape parameters of opposite edges of a tetrahedron are equal, and the
cyclically ordered triple of shape parameters of a tetrahedron encodes an isometry class of hyperbolic
ideal tetrahedra.
The set G(T, ˜b) is deﬁned by the following two sets of equations. For every branched tetrahedron,
set wj :=w(Ej), j = 0, 1, 2 (see before Figure 1 for the ordering of the edge Ej). For every edge e of
T , deﬁne the total shape parameterW (e) as the product of the shape parameters w(E), whereE→e.
Then we have:
• (Tetrahedral equation) For every tetrahedron and j∈{ 0, 1, 2}, wj+1 = (1−wj)−1 cyclically;
hence w0w1w2 =−1.
• (Edge equation) For every edge e of T , W (e) = 1.
A point w ∈ G(T, ˜b) determines a pseudo-developing map Fw : ˜Mφ → H3, where ˜Mφ is the
universal cover of Mφ, and Fw is well-deﬁned up to post-composition with an orientation-preserving
isometry of H3. The map Fw sends homeomorphically the edges of ˜T to complete geodesics, and
it satisﬁes Fw(g˜x) = rw(g)Fw(˜x) for all ˜x∈ ˜Mφ, g∈ π1(Mφ), where rw : π1(Mφ)→ PSL (2, C) is
a homomorphism. So w encodes the conjugacy class of rw. In fact, Fw determines also some rw-
equivariant set {ξΓ}Γ∈Π as above, so that eventually the map w↦→ rw can be lifted to a regular
“holonomy” map
hol: G(T, ˜b)→X(Mφ).
We have (see Proposition 4.6 of [5] when Mφ has a single cusp, and Remark 1.4 of [6] for the general
case):
Proposition 3.1. There is a subvariety A of G(T, ˜b) of dimension equal to the number of cusps
of M, and a point wh ∈ A, such that hol(wh) is the hyperbolic holonomy of Mφ, and hol|A is a
homeomorphism from a Zariski open subset of A containingwh onto its image.
In particular, every point w∈ A encodes an augmented character of Mφ; the algebraic closure of
hol(A) is the eigenvalue subvarietyE(Mφ) ofX0(Mφ), the irreducible component ofX(Mφ) containing
the discrete faithful holonomyrh (see [12]). If Mφ has a single cusp, thenE(Mφ) =X0(Mφ); in general
E(Mφ) contains rh and has complex dimension equal to the number of cusps of Mφ.
It follows from Proposition 3.1 that a point ofi∗(X0(Mφ))⊂X(S) close enough toi∗(rh) is encoded
by a point w∈A.
From now on, we consider only systems of shape parameters w lying in the subvarietyA ofG(T, ˜b).
Denote by (T, ˜b,w ) the layered triangulation T of Mφ endowed with the weak branching ˜b and the
labelling of the abstract edges of T by a system of shape parameters w. For every j = 0,...,k ,
consider the ideally triangulated surfaces ( S,λj) embedded into (T, ˜b,w ) as in Section 2. For every
edgee ofλj, deﬁne the lateral shape parameterW +
j (e) as the product of the shape parameters of the
abstract edges E→e carried by the tetrahedra lying on the positive side of (S,λj).
ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS 9
Lemma 3.2. For any edgee ofλj, the (exponential) shear-bend coordinate ofe deﬁned by any pleated
surface Fw| ˜S (ie. any lift ( ˜S, ˜λj) of (S,λj) to ˜Mφ, and any pseudo-developing map Fw| ˜S : ˜S→ H3),
coincides with the parameter xj(e) :=−W +
j (e).
The proof follows from the deﬁnitions (see eg. [7]). Note that x0(e) = xk(φ0(e)) for every edge
e of λ = λ0. Also, the shear-bend coordinate of any edge ˜ e of ˜λj is eventually ‘attached’ to the
corresponding edge e of λj, because for diﬀerent choices of ˜S or Fw the images of Fw| ˜S diﬀer only by
an hyperbolic isometry.
Remarks 3.3. The parameter xj(e) is the opposite of W +
j (e) because the (oriented) bending angle
along an edge of λj is traditionally measured by the external dihedral angle π−θ (see eg. [7, 8]),
whereas the shape parameters use the internal dihedral angle θ. So θ = 0 when two adjacent ideal
triangles F (τ) and F (τ′) coincide, for triangles τ, τ′ of ( ˜S, ˜λj).
3.2. Quantum hyperbolic geometry. We keep the setting of the previous section.
Recall that N≥ 3 is an odd integer, and q a primitive N-th root of unity.
We begin with a few qualitative, structural features of the reduced quantum hyperbolic state sum
Hred
N (T, ˜b, w) deﬁned in [5, 6]. It is a regular rational function deﬁned on a covering of the gluing
varietyG(T, ˜b). The points of this covering over a point w∈G(T, ˜b) are certain systems of N-th roots
w(E) of the shape parameters w(E), which label the abstract edges E of T and are called quantum
shape parameters. Alike the “classical” ones, opposite edges of an abstract tetrahedron are given
the same quantum shape parameter. Moreover, the quantum shape parameters verify the following
relations, which are “quantum” counterparts of the deﬁning equations of the gluing variety. For every
branched tetrahedron of (T, ˜b) put wj := w(Ej) (with the usual edge ordering ﬁxed before Figure 1).
For every edge e of (T, ˜b, w), deﬁne the total quantum shape parameter W(e) as the product of the
quantum shape parameters of the abstract edges E→e. Then we have:
• (Tetrahedral relation) For every tetrahedron, w0w1w2 =−q.
• (Edge relation) For every edge e of T , W(e) =q2.
For simplicity we will work with systems of quantum shape parametersw such that the corresponding
systems of “classical” shape parameters w belong to a simply connected open neighborhood A0⊂
A⊂G(T, ˜b) of wh (the general case of systems w with arbitrary w∈A is described in [5]). Note that
A0 is chosen so that w(E) varies continuously with w∈A0.
Remarks 3.4. (1) For everyz∈ C\{ 0}, denote by log(z) the determination of the logarithm which
has the imaginary part in ] −π,π ]. There is a Z-labelling d of the abstract edges of T such that, for
every system w of quantum shape parameters over a point w∈ A0, and every abstract edge E, we
have
(4) w(E) = exp
( 1
N (log(w(E)) +πi(N + 1)d(E))
)
.
The above relations veriﬁed by the quantum shape parameters can be equivalently rephrased in terms
of the Z-labelling d. For any point w∈A0, a Z-labelling d satisfying these relations deﬁnes a system
of quantum shape parameters over w by the formula (4).
(2) In [4, 5, 6] we solved (mainly in terms of the Z-labellings d) the existence problem of triples
(T, ˜b, w) for any cusped hyperbolic 3-manifold in the special case q =− exp(−iπ/N). The same
method works for an arbitrary q, up to minor changes.
The following result summarizes in a qualitative way the invariance properties of Hred
N (T, ˜b, w).
Denote by A0,N the set of systems of quantum shape parameters over A0. Recall from Section 2
that Mφ can be considered as the interior of a compact manifold ¯Mφ bounded by tori. Fix a basis
(l1,m 1),..., (lr,mr) of π1(∂ ¯Mφ), and use it to identify H1(∂ ¯Mφ; C∗) with ( C∗)2r. Any augmented
character [(r,{ξΓ}Γ)]∈ X(Mφ) determines the square of one of the two (reciprocally inverse) eigen-
values of r(γ), for any non trivial simple closed curve γ on∂ ¯Mφ and representative r of the character.
Namely, by taking r in its conjugacy class so that r(π1(∂ ¯Mφ)) ﬁxes the point ∞ on CP 1, r([γ]) acts
