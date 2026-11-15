---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-026-47-a-covering-theorem-for-hyperbolic-3-manifolds
section_title: "A covering theorem for hyperbolic 3-manifolds"
section_number: 4.7
pages: 32-34
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
The restrictive structure of simply degenerate ends places serious restrictions on how it can
cover another manifold. Thurston established the following result when the covering manifold
has freely indecomposable fundamental group and Canary generalized the argument to the
general setting.
Covering Theorem: (Thurston[75], Canary [27]) Let ˆN be a geometrically tame hyperbolic 3-
manifold which covers another hyperbolic 3-manifold N by a local isometry p : ˆN →N. If ˆE is
a simply degenerate end of ˆN then either
a) ˆE has a neighborhood ˆU such that p is finite-to-one on ˆU, or
b) N has finite volume and has a finite cover N′ which fibers over the circle such that if
NS denotes the cover of N′ associated to the fiber subgroup then ˆN is finitely covered by NS.
Moreover, if ˆN̸ = NS, then ˆN is homeomorphic to the interior of a twisted I-bundle which is
doubly covered by NS.
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS
33
Idea of proof: Let ˆU be a neighborhood of ˆE homeomorphic to S × (0, ∞) and let {fn : S × ˆU}
be a sequence of simplicial hyperbolic surfaces exiting E (which are homotopic to the inclusion
map ι within ˆU). There exists L > 0 so that for all n there exists an essential simple closed
curve αn on S so that ℓ(f(αn)) ≤L. (By the usual “blowing a up a balloon” argument, we may
take L to be any number so that
areaBH2(L, i) = 2π cosh L −2π > 2π|ξ(S)| ≥area(S, τf).)
It is then not difficult to show that f(αn) is homotopically non-trivial and f(αn)∗is homotopic
to f(αn) (within U) for all large enough n and {f(αn)∗} exits E. We may then replace fn by
a simplicial hyperbolic surface gn : S →ˆU, for all large n, which realizes αn with one vertex so
that {gn : S × ˆU} is a sequence of simplicial hyperbolic surfaces exiting E (which are homotopic
to the inclusion map ι within ˆU).
Hatcher [38] showed that any two triangulations of S with one vertex can be joined by a path
of triangulations each of which is obtained from the previous one by an “elementary move.”
Using Hatcher’s result, if n̸ = m, we can either
(1) Produce a continuous family {ht : S →ˆN}t∈[0,1] of simplicial hyperbolic surfaces (with at
most two vertices) joining gm to gn (i.e. h0 = gm and h1 = gn), or
(2) Produce continuous families {ht : S →ˆU}t∈[0,1] and {jt : S →ˆN}t∈[0,1] simplicial hyperbolic
surfaces (with at most two vertices) so that h0 = gm and h1(Sn)∩∂ˆU is non-empty and j0 = gn
and j1(Sn) ∩∂ˆU
If S is π1-injective in N, then case (1) always occurs. In either situation, this allows us to find
a smaller neighborhood U of N, so that if x ∈U, there exists a simplicial hyperbolic surface
hx : S →ˆU (which is isotopic to ι within ˆU). One corollary of this observation is:
Corollary 4.8. If N is a hyperbolic 3-manifold with finitely generated fundamental group, then
there exists L so that C(N) does not contain an embedded hyperbolic ball of radius L.
Suppose that p is infinite-to-one on U. So there exists a point x ∈N so that p−1(x) ∩U
is infinite. Index p−1(x) ∩U = {xi}i∈N so that xi exits the end E. For all i, let fi : S →ˆU
be a simplicial hyperbolic surface so that xi ∈fi(S) (homotopic to ι within ˆU). We may pass
to a subsequence so that p(fi(S)) converges. Choose i and j large enough so that there is a
short homotopy in N between p(fi(S)) and p(fj(S)) and fi(S) and fj(S) are far apart in ˆU.
We concatenate the p-image of a homotopy between fi(S) and fj(S) within ˆU and the short
homotopy between fi(S) and fj(S) to construct a map g : M →N of a closed 3-manifold M
which fibers over the circle into N.
If S is π1-injective, then we may show that g is πi-injective. (Notice that the “lift”of the
fibre of M to ˆN is an arc in ˆU joining a point in fi(S) to fj(S), so is not a closed loop.) Let
N′ be the cover of N associated to g∗(π1(M)) and consider the lift ˜g : M →N′. Since ˜g is
a homotopy equivalence, N′ must be closed (for homological reasons). Waldhausen’s Theorem
(see [39, Thm.13.9] then implies that ˜g is homotopic to a homeomorphism. Moreover, since N′
is closed, it must be a finite cover of N.
If S is not π1-injective, let Li be the length (in τfi of the shortest compressible curve on
fi(S) (i.e. an essential curve in S which is mapped to a homotopically trivial curve in ˆN). One
34
RICHARD D. CANARY
may show that Li →∞. This then contradicts the fact that the p(fi(S)) can be chosen to
accumulate in N.
□
A subgroup ˆΓ of Γ is said to be a virtual fiber subgroup if there exist finite index subgroups
Γ0 of Γ and ˆΓ0 of ˆΓ such that N0 = H3/Γ0 fibers over the circle and ˆΓ0 corresponds to the fiber
subgroup. Corollary 4.9 is the key tool in many of the group-theoretic applications of Marden’s
Tameness Conjecture.
Corollary 4.9. If N = H3/Γ is a closed hyperbolic 3-manifold and ˆΓ is a finitely generated
subgroup of Γ, then ˆΓ is either convex cocompact or a virtual fiber subgroup.
Thurston gave a beautiful proof, using that a cover of an infinite-volume convex cocompact
hyperbolic 3-manifold is convex cocompact if it has finitely generated fundamental group. (See
[27] for the general statement and proof.)
Theorem 4.10. If N = H3/Γ is an infinite volume convex cocompact hyperbolic 3-manifold and
Γ0 is a finitely generated (non-abelian) subgroup of Γ, then Γ0 is convex compact.
Proof. Ahlfors’ Finiteness Theorem [3] implies that if ∆is a finitely, generated, torsion-free,
non-abelian Klelnian group which does not contain any parabolic elements, then ∂cN∆is a
finite collection (possibly empty) of closed surfaces. It follows from our earlier discussion that
∂C1(N∆) is also a finite collection of closed surfaces, and hence that ∂C(N∆) is compact.
Since NΓ is convex cocompact and infinite volume, ∂C(NΓ) is non-empty. Since C(NΓ) is
compact, there exists D so that if x ∈C(NΓ), then d(x, ∂C(NΓ)) ≤D. Lifting to the cover we
see that if y ∈CH(Λ(Γ)), then d(y, ∂CH(Λ(Γ)) ≤D.
Since Γ0 ⊂Γ, Λ(Γ0) ⊂Λ(Γ), so CH(Λ(Γ0)) ⊂CH(Λ(Γ)). If y ∈CH(Λ(Γ0), then y ∈
CH(Λ(Γ), so d(y, ∂CH(Λ(Γ)) ≤D. But, again since CH(Λ(Γ0)) ⊂CH(Λ(Γ)), we see that
d(y, ∂CH(Λ(Γ0)) ≤D. So, if x ∈C(NΓ0), then d(x, ∂C(NΓ0) ≤D. Since ∂C(NΓ0) is compact
(by the above discussion), C(NΓ0) is a closed bounded subset of NΓ0, hence compact. Therefore,
Γ0 is convex cocompact.
□
More generally, one may use the covering theorem to completely describe exactly which covers
of a hyperbolic 3-manifold with finitely generated fundamental group are convex cocompact (see
[27]).
Further discussion of the group theoretic consequences of the Covering Theorem are given in
[28].
