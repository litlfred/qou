---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-031-54-the-bers-sullivan-thurston-density-conjecture
section_title: "The Bers-Sullivan-Thurston Density Conjecture and other consequences"
section_number: 5.4
pages: 37-38
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
Sulivan [73] proved that CC(M) is the interior of AH(M).
Theorem 5.2. Let M be a compact, oriented, irreducible 3-manifold with non-empty boundary
such that π1(M) is infinite, non-abelian and does not contain a free abelian subgroup of rank 2.
Then CC(M) is the interior of AH(M).
Idea of Proof: Let ρ be an interior point of AH(M). One may use the λ-lemma to show that
there exists a neighborhood U of ρ so that every representation in U is quasiconformally conju-
gate to ρ/ Sullivan proved that the Beltrami differential of every quasiconformal deformation of
a finitely generated Kleinian group is supported on the limit set. Therefore, U is identified with
an open set in T (∂cNρ). Since the dimension of the component of X(M) containing ρ agrees
with the dimension of T (∂M), it follows that T (∂cNρ) has the same dimension as T (∂M), so
χ(∂M) = χ(∂cNρ). Topological considerations then imply that ∂cNρ compactifies Nρ, so ρ is
convex cocompact.
□
Bers, Sullivan and Thurston conjectured that every representation in AH(M), with our
restrictions on M, is a limit of convex cocompact representations. Given Sullivan’s theorem we
38
RICHARD D. CANARY
can rephrase this conjecture by saying that AH(M) is the closure of its interior. This rephrasing
is valid for all manifolds M whose interior admits a hyperbolic structure.
Density Theorem: If M is a compact irreducible 3-manifold and AH(M) is non-empty, then
AH(M) is the closure of its interior int(AH(M)).
The proof of the Density theorem has a rather convoluted history. The first major break-
through was due to Bromberg [20] who established a version of this conjecture for ρ ∈AH(S ×
[0, 1]) where Nρ has no cusp and ∂cNρ has exactly one component. His argument was generalized
by Brock-Bomberg [17] to prove the conjecture for ρ ∈AH(M) where M has incompressible
boundary and Nρ has no cusps. Their approach makes use of the deformation theory of cone-
manifolds developed by Hodgson-Kerckhoff [40, 41] and Bromberg [19]. It only makes use of
the proof of the Ending Lamination Conjecture in the case where there is a lower bound on
injectivity radius, which was established earlier by Minsky [58].
If M has incompressible boundary, one may derive the Density Theorem from the Tameness
Theorem, the Ending Lamination Theorem, and convergence results of Thurston [77, 78] (see
the discussion in [18].) Basically, the idea here is to consider the end invariants of a given
3-manifold, use the convergence results to construct a hyperbolic 3-manifold with the given
end invariants which arises as a limit of geometrically finite hyperbolic 3-manifolds. One then
applies the Ending Lamination Theorem to show that the manifold you constructed agrees with
the original hyperbolic 3-manifold.
If M has compressible boundary, one replaces Thurston’s convergence results with conver-
gence results of Kleineidam-Souto [44], Lecuire [46] and Kim-Lecuire-Ohshika [45]. However,
especially in the case that M is homotopy equivalent to a compression body (e.g. a handle-
body), significant technical difficulties arise in showing that the limits have the correct ending
invariants. Namazi-Souto [63] and Ohshika [64] overcome these obstacles to complete the proof
of the Density Theorem in all cases.
Another consequence of the proof of the Ending Lamination Theorem is the following common
generalization of Mostow [62] and Sullivan’s [71] rigidity theorems.
Corollary 5.3. Let G be a finitely generated, torsion-free group which is not virtually abelian.
If two discrete faithful representations ρ1 : G →PSL(2, C) and ρ2 : G →PSL(2, C) are con-
jugate by an orientation-preserving homeomorphism ϕ of ∂H3, then they are quasiconformally
conjugate. Moreover, if ϕ is conformal on Ω(ρ1(G)), then ϕ is conformal.
