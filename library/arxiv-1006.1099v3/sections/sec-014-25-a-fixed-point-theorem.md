---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-014-25-a-fixed-point-theorem
section_title: "A fixed point theorem"
section_number: 2.5
pages: 15-17
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
2.5. A ﬁxed point theorem. Since there are periodic, ﬁxed-point free surface diﬀeomorphisms,
even when g = 2 Theorem 1.1 does not imply that HF(ˆρ(φ))̸ = 0 for an arbitrary mapping class
φ. In fact, such a non-vanishing result does hold in any genus; the proof relies on concentrating
not on the summand of the Fukaya category corresponding to the underlying curve but on a
“semi-simple” summand. The moduli space M(Σg) is monotone with minimal Chern number 2,
hence its quantum cohomology is mod 4 graded. We recall a result of Munoz [70]:
Theorem 2.13 (Munoz). The eigenvalues of quantum cap-product ∗h by the generator h ∈
H2(M(Σg); Z) ∼= Z on the quantum cohomology QH∗(M(Σg)) are {0, ±4, ±8, . . ., ±4(g −1)}.
Moreover, with ﬁeld co-eﬃcients, the generalised eigenspaces associated to the eigenvalues ±4(g−
1) have rank 1.
For V ⊂M an Sk-ﬁbred coisotropic submanifold with base B, denote by τV the ﬁbred
positive Dehn twist along V . We will not distinguish notationally between V and the associated
Lagrangian correspondence V ⊂B×M. Fix a homologically essential simple closed curve γ ⊂Σg,
hence a Lagrangian correspondence Vγ ⊂M(Σg−1) × M(Σg), cf. Section 2.2.
Corollary 2.14 (Perutz). There is an isomorphism
HF(Vγ, Vγ) ∼= QH∗(M(Σg−1)) ⊗H∗(S3; ΛR)
as QH∗(M(Σg−1))-modules.
This is [80, Theorem 7.5] (and is a direct application of Perutz’ Theorem 3.3 in a case where
the Euler class of the sphere bundle vanishes).
Lemma 2.15. Let φ ∈Symp(M(Σg)). The eigenvalues of quantum cup-product by the generator
h ∈H2(M(Σg)) on HF(Vγ, (φ × id)Vγ) are contained in {0, ±4, . . ., ±4(g −2)}.
Proof. Let R be a unital ring, A a ﬁnitely generated R-algebra and r ∈R. The spectrum of
multiplication by r on A is a subset of that of multiplication by r on R. Indeed, there is a
surjective quotient π : Rk →A, and ker(π) is stable under multiplication by elements of R. The
result then follows from the well-known fact that if a transformation T on a vector space V has
invariant subspace W, the minimal polynomial of the induced map on V/W is a factor of the
minimal polynomial of T . Therefore, it suﬃces to compute the spectrum of quantum cup-product
by h on HF(Vγ, Vγ).
Since Vγ ⊂M(Σg−1) × M(Σg) is simply-connected, it has minimal Maslov number 4. Lemma
3.1 implies that under the natural map
QH∗(M(Σg−1)) ⊗QH∗(M(Σg)) ∼= QH∗(M(Σg−1) × M(Σg)) −→HF(Vγ, Vγ)
the ﬁrst Chern class maps to zero. (In the language of Section 3.1, m0(Vγ) = 0.) Therefore,
1 ⊗c1(M(Σg)) and c1(M(Σg−1)) ⊗1 have the same image up to sign, so it is enough to know the
spectrum of the latter class. The action of this is determined by Corollary 2.14, and the result
follows on combining that with Theorem 2.13.
□
Theorem 2.16 (Wehrheim-Woodward). Let k > 1. Suppose that V ⊂M is an Sk-ﬁbred co-
isotropic, whose graph deﬁnes an orientable monotone Lagrangian submanifold of B × M of
minimal Maslov number ≥4. Let φ ∈Symp(M). There is an exact triangle
· · · →HF ∗(φ) →HF ∗(τV ◦φ) →HF ∗(V, (φ × idB)V )
[1]
−→HF ∗(φ) →· · ·
of (relatively graded) modules for the ring QH∗(M; K).
This is taken from [106]. We point out that when g = 2, the case relevant for determining
instanton Floer homology of genus 2 ﬁbred 3-manifolds in Equation 1.1, the generalised Dehn
twist of Proposition 2.6 is just a classical Dehn twist in a Lagrangian 3-sphere, and the proof of
the following Corollary simpliﬁes accordingly.
16
IVAN SMITH
Corollary 2.17. Let ˆφ ∈Symp(M(Σg)) represent a mapping class in the image of the natural
homomorphism ˆρ : bΓ(Σg) →π0 Symp(M(Σg)). Then HF(ˆφ)̸ = 0.
Proof. Write the given mapping class ˆφ = ˆρ(φ◦) and write φ◦= Q
i t±εi
γi
as a product of (positive
and negative) Dehn twists along non-separating simple closed curves; this is always possible. We
consider the long exact sequences in Floer cohomology associated to the induced rank 3 ﬁbred
Dehn twists on M(Σg) of Proposition 2.6:
HF(ψ) →HF(τV ◦ψ) →HF(V, (ψ × id)V )
[1]
−→· · ·
where ψ is a sub-composite of Dehn twists. We claim by induction on the number of twists in
the expression of φ, equivalently φ◦, that HF(ˆφ) is non-trivial. Indeed, we make the following
somewhat stronger inductive hypothesis: the generalized eigenspace for ∗h on HF(ψ) for the
eigenvalue 4(g −1) is rank 1 whenever ψ is a product of ≤k (positive or negative) Dehn twists.
If k is zero, then ˆφ = id and we have a ring isomorphism HF(id) ∼= QH∗(M(Σg)), in which case
this result is exactly Munoz’ theorem.
Taking generalized eigenspaces is an exact functor over any ﬁeld; consider the associated
exact sequence of generalised eigenspaces, for eigenvalue 4(g −1), for the operation given by
quantum cup-product ∗h in the exact sequence above.
If g = 2 the third term in the se-
quence is HF(Lγ, ψ(Lγ)). Quantum cohomology acts via the module structure of this group
over HF(Lγ, Lγ) ∼= H∗(S3), which is trivial in relative (mod 4) degree 2, from which it immedi-
ately follows that ∗h is nilpotent. More generally, Lemma 2.15 implies that the spectrum of ∗h
on HF(Vγ, (ψ × id)Vγ) is contained in {0, . . . , ±4(g −2)}, so the generalized eigenspace for the
eigenvalue 4(g −1) is trivial. By exactness, if that eigenspace has rank 1 for ψ, it also has rank 1
for τV ◦ψ. The argument for inserting a negative Dehn twist is the same, but working with the
exact triangle
HF(τ −1
V ψ) →HF(τV ◦(τ −1
V ψ)) →HF(V, (τ −1
V ψ × id)V )
In either case, the induction implies that for any mapping class, there is a distinguished rank one
summand in HF(φ), so in particular HF(φ)̸ = 0.
□
Corollary 2.17, via the circle of ideas of Section 2.3, yields:
Corollary 2.18. Every ﬁbred 3-manifold admits a non-abelian SO(3)-representation.
A stronger statement was proved by Kronheimer-Mrowka [55], who used Feehan and Leness’
deep work on the relation between Seiberg-Witten and Donaldson invariants of closed 4-manifolds
(note the proof given above uses the Dehn twist exact triangle, but not the existence of the Fukaya
category).
Any element of the mapping class group Γ2,1 can be written as a product of Dehn twists in
simple closed curves lifted from arcs in C. Addendum 1.2 and Corollary 2.17 imply that over
K = C, there is an isomorphism
HF(ˆρ(φ)) ∼= C ⊕HF(φ) ⊕C
(2.8)
determining HF(ˆρ(φ)) for any φ ∈Γ2,1, and not just for φ = id (the special case of Lemma
2.3, which we knew previously). The central term on the RHS can be computed, via results of
[21], from knowledge of the Thurston decomposition of φ or from the train-track obtained from
a description of φ as a product of positive and negative Dehn twists in simple closed curves.
Equation 2.7 and the general discussion of Section 2.3 now implies Corollary 1.7. Viewed in
terms of Corollary 3.12, Equation 2.8 describes the Hochschild cohomology of general functors
of the Fukaya category obtained from mapping classes on the surface, rather than just of the
identity functor. Modulo Remark 5.30, the instanton Floer homologies of other SO(3)-bundles
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
17
on the mapping torus are computed by the Hochschild cohomologies of the other lifts of the
monodromy to the split extension of Γg by H1(Σ; Z2) which acts on F(Σg).
Remark 2.19. Corollary 2.17 implies that the summand F(Σg; 4(g −1))̸ = ∅. One can exhibit
explicit Lagrangian submanifolds in this summand using toric degeneration methods. For in-
stance, when g = 2, Nishinou et. al. [74] show by degenerating M(Σ2) to the toric intersection
{x2 = yz, p2 = qr} ⊂P5 that there is a Lagrangian torus with m0(T 3) = 4 and with Floer
cohomology a Cliﬀord algebra.
In general, take an idempotent summand of a Lagrangian L+ ∈T wπF(M(Σg−1)) lying
in the top summand of its Fukaya category, corresponding to eigenvalue 4(g −2), and with
HF(L+, L+) ∼= K.
Given any homologically essential simple closed curve γ ⊂Σg with as-
sociated Lagrangian correspondence Vγ ⊂M(Σg−1) × M(Σg), one gets an object Φ(Vγ)(L+) ∈
T wπF(M(Σg)). This seems a good candidate for the image of γ under the conjectural equivalence
DπF(Σg)
?≃DπF(M(Σg); 4(g −2)).
