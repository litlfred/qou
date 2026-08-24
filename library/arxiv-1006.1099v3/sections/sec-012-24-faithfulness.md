---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-012-24-faithfulness
section_title: "Faithfulness"
section_number: 2.4
pages: 13-16
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
Lemma 2.8 (Thurston). Let Σ g be a closed surface and σ ⊂ Σ g a separating simple closed
curve. There is another separating simple closed curve σ′⊂ Σ g for which the products τ k
στ −k
σ′ are
pseudo-Anosov mapping classes for all k≥ 1.
In fact, one chooses σ′ so that σ∪σ′ ﬁll Σ g in the sense that their complement is a union of
disks. Then any word in positive twists along σ and negative twists along σ′ (with both twists
appearing) yields a pseudo-Anosov diﬀeomorphism; a proof is given in [31, Expos´ e 13, Th´ eor` eme
III.3].
Lemma 2.9. Let g(Σ) ≥ 2. Suppose that for any ˆφ∈ ˆΓ(Σ) with a pseudo-Anosov component,
ˆρ( ˆφ) has strictly positive Floer-theoretic entropy. Then ˆρ is faithful.
Proof. Suppose a mapping class ˆφ⁄= id lies in the kernel of ˆ ρ. We ﬁrst claim that ˆφ cannot
be in the ﬁnite subgroup H 1(Σ; Z2) which is the kernel of ˆΓ(Σ) → Γ g. Indeed, a theorem of
Narasimhan and Ramanan [71] implies that for ι∈H 1(Σ; Z2)\{id},
Fix(ι) = Prym( ι) ∼= T 2g−2
is an abelian variety of dimension g− 1, isomorphic to the Prym variety of the double cover
of Σ deﬁned by ι. These ﬁxed points form a smooth Morse-Bott manifold, which arise s as a
clean intersection between the graph of ι and the diagonal. Pozniak’s “local-to-global” spectral
sequence for Floer cohomology [82] then implies that
dimK(HF (ι)) ≤ dimK(H ∗(T 2g−2))
which is strictly smaller than dimK(QH ∗(M(Σ)), cf. Section 2.1. It follows that HF (ι) ⁄∼=
HF (id), so ι⁄∈ker(ˆρ). Accordingly, if ˆφ does lie in this kernel, it has non-trivial image φ in
the classical mapping class group Γ g. The hypothesis implies that φ has no pseudo-Anosov
component; Thurston’s classiﬁcation of surface diﬀeomorphisms [ 31] implies φ is reducible with
14 IV AN SMITH
all components periodic. If any periodic component is non-trivial, th e mapping class ˆρ( ˆφ) acts
non-trivially on cohomology, via the µ-map of Equation 2.4 and the non-trivial action on H ∗(Σ).
We therefore reduce to φ being a product of powers of Dehn twists on disjoint separating simp le
closed curves.
Ifσ⊂ Σ is a separating curve, by Lemma 2.8 we can ﬁnd another separating curveσ′ for which
the elements τ k
στ −k
σ′ are pseudo-Anosov when k >0. By the hypothesis, these therefore map to
elements of positive Floer-theoretic entropy under ˆρ. If a lift to ˆΓ(Σ) of some power of the twist
τσ was in the kernel of ˆρ, then the Floer cohomology of iterates of τ −1
σ′ would grow exponentially
in rank, hence so would the Floer cohomologies of iterates of τσ′ recalling HF (ψ−1)∼=HF (ψ)∗.
However, it is straightforward using Proposition 2.6 to write down an explicit representative for
the action of τσ′ on M(Σ) for which the Floer chain groups grow only linearly in rank under
iteration. It follows that the Dehn twist in the separating curve σ actually maps to an element
of inﬁnite order. The same trick shows a product of separating twis ts in disjoint curves is also
inﬁnite order. The result follows. □
Remark 2.10. It may be worth emphasising that the hypotheses of the faithfulne ss criterion
Lemma 2.9 could be derived from something much weaker than Conjec ture 1.9; for instance
it would follow (over K = Λ C) from the existence of a formal deformation of categories from
F(M(Σ g); 4(g− 2)) to F(Σ g). Such (bulk) deformations seem likely to arise in the obvious
strategies to attack Conjecture 1.9 as coming from ﬂip diagrams, c f. Section 1.8.
Lemma 2.11. If g(Σ) = 2 , the hypothesis of Lemma 2.9 is satisﬁed.
Proof. Again take ˆφ∈ ˆΓ(Σ) with image φ, and pick a representative diﬀeomorphism of the surface
Σ for that mapping class. This can be written as a product of Dehn tw ists in simple closed
curves associated to matching paths in C, which means that the action of the diﬀeomorphism
on DπF(Σ) ≃ DπF(M(Σ); 0) is determined by the twist functors in the spheres Vγ. These
act compatibly with the equivalence of categories, by Addendum 1.2, cf. Corollaries 4.45 and
5.29. For any k∈ Z, the Floer group HF (φk)∼= HH (Gφk ) is given by the group of natural
transformations between the identity functor and that induced b y φk, by Corollary 3.12. In
particular this Floer group is completely determined by the action of φ on the Fukaya category.
It follows that the Floer cohomology of the mapping class on the unde rlying surface is a summand
of the Floer cohomology on the moduli space. Equation (2.7) now pro ves the Lemma. □
When g = 2, the Floer-theoretic entropy of ˆ ρ( ˆφ) is positive if and only if φ has a pseudo-
Anosov component; the converse implication holds by the proof of L emma 2.9. Combining the
two previous results, we obtain a proof of Theorem 1.5 from the Int roduction, using an argument
due to Wehrheim and Woodward.
Corollary 2.12. Forg≥ 2, the representation ˆΓ(Σ g)→π0 Symp(M(Σ g)) is non-trivial on the
Torelli groupI(Γ) .
Proof. Forg = 2, we have actually seen that the Dehn twist on the separating wais t curveσ⊂ Σ 2
induces a non-identity functor of Donaldson’s quantum category H(FM(Σ 2)). For higher genus,
following Wehrheim and Woodward, we use induction on g withg = 2 the base case. Suppose for
contradiction that τσ induces the identity functor of the Donaldson category H(F(M(Σ g))) but
the separating twist is non-trivial at genus g− 1. Viewing the co-isotropic vanishing cycles Vγ
as Lagrangian correspondences, there are natural isomorphism s of functors Vγ◦τ g
σ◦V op
γ ∼=τ g−1
σ
(this is the cohomology level version of Theorem 3.14). But if τ g
σ≃idHFM(Σ g ) then the left hand
side gives the identity functor, contradicting the inductive hypoth esis. □
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 15
2.5. A ﬁxed point theorem. Since there are periodic, ﬁxed-point free surface diﬀeomorphisms ,
even when g = 2 Theorem 1.1 does not imply that HF (ˆρ(φ))⁄= 0 for an arbitrary mapping class
φ. In fact, such a non-vanishing result does hold in any genus; the pr oof relies on concentrating
not on the summand of the Fukaya category corresponding to the underlying curve but on a
“semi-simple” summand. The moduli space M(Σ g) is monotone with minimal Chern number 2,
hence its quantum cohomology is mod 4 graded. We recall a result of M unoz [70]:
Theorem 2.13 (Munoz). The eigenvalues of quantum cap-product ∗h by the generator h ∈
H 2(M(Σ g); Z)∼= Z on the quantum cohomology QH ∗(M(Σ g)) are{0,±4,±8,..., ±4(g− 1)}.
Moreover, with ﬁeld co-eﬃcients, the generalised eigenspa ces associated to the eigenvalues ±4(g−
1) have rank 1.
For V ⊂ M an Sk-ﬁbred coisotropic submanifold with base B, denote by τV the ﬁbred
positive Dehn twist along V . We will not distinguish notationally between V and the associated
Lagrangian correspondenceV⊂B×M . Fix a homologically essential simple closed curve γ⊂ Σ g,
hence a Lagrangian correspondence Vγ⊂ M(Σ g−1)× M(Σ g), cf. Section 2.2.
Corollary 2.14 (Perutz). There is an isomorphism
HF (Vγ,V γ) ∼= QH ∗(M(Σ g−1))⊗H ∗(S3; Λ R)
as QH ∗(M(Σ g−1))-modules.
This is [80, Theorem 7.5] (and is a direct application of Perutz’ Theore m 3.3 in a case where
the Euler class of the sphere bundle vanishes).
Lemma 2.15. Letφ∈ Symp(M(Σ g)). The eigenvalues of quantum cup-product by the generator
h∈H 2(M(Σ g)) on HF (Vγ, (φ× id)Vγ ) are contained in {0,±4,..., ±4(g− 2)}.
Proof. Let R be a unital ring, A a ﬁnitely generated R-algebra and r∈ R. The spectrum of
multiplication by r on A is a subset of that of multiplication by r on R. Indeed, there is a
surjective quotient π :Rk→A, and ker(π) is stable under multiplication by elements of R. The
result then follows from the well-known fact that if a transformatio nT on a vector space V has
invariant subspace W , the minimal polynomial of the induced map on V/W is a factor of the
minimal polynomial of T . Therefore, it suﬃces to compute the spectrum of quantum cup- product
byh on HF (Vγ,V γ).
Since Vγ⊂ M(Σ g−1)× M(Σ g) is simply-connected, it has minimal Maslov number 4. Lemma
3.1 implies that under the natural map
QH ∗(M(Σ g−1))⊗QH ∗(M(Σ g))∼= QH ∗(M(Σ g−1)× M(Σ g))−→HF (Vγ,V γ)
the ﬁrst Chern class maps to zero. (In the language of Section 3.1, m0(Vγ) = 0.) Therefore,
1⊗c1(M(Σ g)) and c1(M(Σ g−1))⊗ 1 have the same image up to sign, so it is enough to know the
spectrum of the latter class. The action of this is determined by Cor ollary 2.14, and the result
follows on combining that with Theorem 2.13. □
Theorem 2.16 (Wehrheim-Woodward). Let k > 1. Suppose that V ⊂ M is an Sk-ﬁbred co-
isotropic, whose graph deﬁnes an orientable monotone Lagra ngian submanifold of B×M of
minimal Maslov number ≥ 4. Let φ∈ Symp(M ). There is an exact triangle
···→ HF ∗(φ)→HF ∗(τV◦φ)→HF ∗(V, (φ× idB)V )
[1]
−→HF ∗(φ)→···
of (relatively graded) modules for the ring QH ∗(M ; K).
This is taken from [106]. We point out that when g = 2, the case relevant for determining
instanton Floer homology of genus 2 ﬁbred 3-manifolds in Equation 1.1 , the generalised Dehn
twist of Proposition 2.6 is just a classical Dehn twist in a Lagrangian 3- sphere, and the proof of
the following Corollary simpliﬁes accordingly.
16 IV AN SMITH
Corollary 2.17. Let ˆφ∈ Symp(M(Σ g)) represent a mapping class in the image of the natural
homomorphism ˆρ : ˆΓ(Σ g)→π0 Symp(M(Σ g)). Then HF ( ˆφ)⁄= 0.
Proof. Write the given mapping class ˆφ = ˆρ(φ◦) and write φ◦ = ∏
it±εi
γi as a product of (positive
and negative) Dehn twists along non-separating simple closed curve s; this is always possible. We
consider the long exact sequences in Floer cohomology associated t o the induced rank 3 ﬁbred
Dehn twists on M(Σ g) of Proposition 2.6:
HF (ψ)→HF (τV◦ψ)→HF (V, (ψ× id)V )
[1]
−→···
where ψ is a sub-composite of Dehn twists. We claim by induction on the number of twists in
the expression of φ, equivalently φ◦, that HF ( ˆφ) is non-trivial. Indeed, we make the following
somewhat stronger inductive hypothesis: the generalized eigensp ace for ∗h on HF (ψ) for the
eigenvalue 4(g− 1) is rank 1 whenever ψ is a product of ≤k (positive or negative) Dehn twists.
Ifk is zero, then ˆφ = id and we have a ring isomorphism HF (id)∼=QH ∗(M(Σ g)), in which case
this result is exactly Munoz’ theorem.
Taking generalized eigenspaces is an exact functor over any ﬁeld; c onsider the associated
exact sequence of generalised eigenspaces, for eigenvalue 4( g− 1), for the operation given by
quantum cup-product ∗h in the exact sequence above. If g = 2 the third term in the se-
quence is HF (Lγ,ψ (Lγ)). Quantum cohomology acts via the module structure of this grou p
overHF (Lγ,L γ)∼=H ∗(S3), which is trivial in relative (mod 4) degree 2, from which it immedi-
ately follows that ∗h is nilpotent. More generally, Lemma 2.15 implies that the spectrum of ∗h
on HF (Vγ, (ψ× id)Vγ ) is contained in {0,..., ±4(g− 2)}, so the generalized eigenspace for the
eigenvalue 4(g− 1) is trivial. By exactness, if that eigenspace has rank 1 for ψ, it also has rank 1
for τV◦ψ. The argument for inserting a negative Dehn twist is the same, but w orking with the
exact triangle
HF (τ −1
V ψ)→HF (τV◦ (τ −1
V ψ))→HF (V, (τ −1
V ψ× id)V )
In either case, the induction implies that for any mapping class, ther e is a distinguished rank one
summand in HF (φ), so in particular HF (φ)⁄= 0. □
Corollary 2.17, via the circle of ideas of Section 2.3, yields:
Corollary 2.18. Every ﬁbred 3-manifold admits a non-abelian SO(3)-representation.
A stronger statement was proved by Kronheimer-Mrowka [55], who used Feehan and Leness’
deep work on the relation between Seiberg-Witten and Donaldson inv ariants of closed 4-manifolds
(note the proof given above uses the Dehn twist exact triangle, bu t not the existence of the Fukaya
category).
Any element of the mapping class group Γ 2,1 can be written as a product of Dehn twists in
simple closed curves lifted from arcs in C. Addendum 1.2 and Corollary 2.17 imply that over
K = C, there is an isomorphism
HF (ˆρ(φ))∼= C⊕HF (φ)⊕ C (2.8)
determining HF (ˆρ(φ)) for any φ∈ Γ 2,1, and not just for φ = id (the special case of Lemma
2.3, which we knew previously). The central term on the RHS can be c omputed, via results of
[21], from knowledge of the Thurston decomposition of φ or from the train-track obtained from
a description of φ as a product of positive and negative Dehn twists in simple closed curv es.
Equation 2.7 and the general discussion of Section 2.3 now implies Coro llary 1.7. Viewed in
terms of Corollary 3.12, Equation 2.8 describes the Hochschild cohom ology of general functors
