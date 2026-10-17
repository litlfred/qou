---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-013-24-faithfulness
section_title: "Faithfulness"
section_number: 2.4
pages: 13-15
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
entropy of a mapping class φ ∈Symp(X)/ Ham(X)
hF loer(φ) = lim sup 1
n log rkK HF(φn).
As mentioned in the Introduction, for area-preserving diﬀeomorphisms of a surface Σ the Floer-
theoretic entropy (of the action on Σ itself) co-incides with the topological entropy which in
turn co-incides with the periodic entropy, or rather their minimal values on the isotopy class
[21, 31, 33]. Thus
hF loer(φ) > 0 ⇔φ has a pseudo-Anosov component.
(2.7)
This follows from the classical fact that pseudo-Anosov maps have exponentially growing numbers
of periodic points realising exponentially many diﬀerent Nielsen classes; Floer-theoretically one
can actually make much more precise statements [21]. Recall also there is a natural representation
ˆρ : bΓ(Σ) −→π0 Symp(M(Σ))
where Γ(Σ) →Γg is a Z2g
2 -extension of the mapping class group π0 Diﬀ+(Σg). Mildly abusing
notation, we will say ˆφ ∈bΓ(Σ) has a pseudo-Anosov component if that is true of its image φ ∈Γg.
Our faithfulness criterion Lemma 2.9 relies on a classical observation of Thurston:
Lemma 2.8 (Thurston). Let Σg be a closed surface and σ ⊂Σg a separating simple closed
curve. There is another separating simple closed curve σ′ ⊂Σg for which the products τk
στ −k
σ′
are
pseudo-Anosov mapping classes for all k ≥1.
In fact, one chooses σ′ so that σ ∪σ′ ﬁll Σg in the sense that their complement is a union of
disks. Then any word in positive twists along σ and negative twists along σ′ (with both twists
appearing) yields a pseudo-Anosov diﬀeomorphism; a proof is given in [31, Expos´e 13, Th´eor`eme
III.3].
Lemma 2.9. Let g(Σ) ≥2. Suppose that for any ˆφ ∈bΓ(Σ) with a pseudo-Anosov component,
ˆρ(ˆφ) has strictly positive Floer-theoretic entropy. Then ˆρ is faithful.
Proof. Suppose a mapping class ˆφ̸ = id lies in the kernel of ˆρ. We ﬁrst claim that ˆφ cannot
be in the ﬁnite subgroup H1(Σ; Z2) which is the kernel of bΓ(Σ) →Γg. Indeed, a theorem of
Narasimhan and Ramanan [71] implies that for ι ∈H1(Σ; Z2)\{id},
Fix(ι) = Prym(ι) ∼= T 2g−2
is an abelian variety of dimension g −1, isomorphic to the Prym variety of the double cover
of Σ deﬁned by ι. These ﬁxed points form a smooth Morse-Bott manifold, which arises as a
clean intersection between the graph of ι and the diagonal. Pozniak’s “local-to-global” spectral
sequence for Floer cohomology [82] then implies that
dimK(HF(ι)) ≤dimK(H∗(T 2g−2))
which is strictly smaller than dimK(QH∗(M(Σ)), cf.
Section 2.1.
It follows that HF(ι)̸ ∼=
HF(id), so ι̸ ∈ker(ˆρ). Accordingly, if ˆφ does lie in this kernel, it has non-trivial image φ in
the classical mapping class group Γg.
The hypothesis implies that φ has no pseudo-Anosov
component; Thurston’s classiﬁcation of surface diﬀeomorphisms [31] implies φ is reducible with
14
IVAN SMITH
all components periodic. If any periodic component is non-trivial, the mapping class ˆρ(ˆφ) acts
non-trivially on cohomology, via the µ-map of Equation 2.4 and the non-trivial action on H∗(Σ).
We therefore reduce to φ being a product of powers of Dehn twists on disjoint separating simple
closed curves.
If σ ⊂Σ is a separating curve, by Lemma 2.8 we can ﬁnd another separating curve σ′ for which
the elements τ k
σ τ −k
σ′
are pseudo-Anosov when k > 0. By the hypothesis, these therefore map to
elements of positive Floer-theoretic entropy under ˆρ. If a lift to bΓ(Σ) of some power of the twist
τσ was in the kernel of ˆρ, then the Floer cohomology of iterates of τ −1
σ′ would grow exponentially
in rank, hence so would the Floer cohomologies of iterates of τσ′ recalling HF(ψ−1) ∼= HF(ψ)∗.
However, it is straightforward using Proposition 2.6 to write down an explicit representative for
the action of τσ′ on M(Σ) for which the Floer chain groups grow only linearly in rank under
iteration. It follows that the Dehn twist in the separating curve σ actually maps to an element
of inﬁnite order. The same trick shows a product of separating twists in disjoint curves is also
inﬁnite order. The result follows.
□
Remark 2.10. It may be worth emphasising that the hypotheses of the faithfulness criterion
Lemma 2.9 could be derived from something much weaker than Conjecture 1.9; for instance
it would follow (over K = ΛC) from the existence of a formal deformation of categories from
F(M(Σg); 4(g −2)) to F(Σg).
Such (bulk) deformations seem likely to arise in the obvious
strategies to attack Conjecture 1.9 as coming from ﬂip diagrams, cf. Section 1.8.
Lemma 2.11. If g(Σ) = 2, the hypothesis of Lemma 2.9 is satisﬁed.
Proof. Again take ˆφ ∈bΓ(Σ) with image φ, and pick a representative diﬀeomorphism of the surface
Σ for that mapping class. This can be written as a product of Dehn twists in simple closed
curves associated to matching paths in C, which means that the action of the diﬀeomorphism
on DπF(Σ) ≃DπF(M(Σ); 0) is determined by the twist functors in the spheres Vγ.
These
act compatibly with the equivalence of categories, by Addendum 1.2, cf. Corollaries 4.45 and
5.29. For any k ∈Z, the Floer group HF(φk) ∼= HH(Gφk) is given by the group of natural
transformations between the identity functor and that induced by φk, by Corollary 3.12.
In
particular this Floer group is completely determined by the action of φ on the Fukaya category.
It follows that the Floer cohomology of the mapping class on the underlying surface is a summand
of the Floer cohomology on the moduli space. Equation (2.7) now proves the Lemma.
□
When g = 2, the Floer-theoretic entropy of ˆρ(ˆφ) is positive if and only if φ has a pseudo-
Anosov component; the converse implication holds by the proof of Lemma 2.9. Combining the
two previous results, we obtain a proof of Theorem 1.5 from the Introduction, using an argument
due to Wehrheim and Woodward.
Corollary 2.12. For g ≥2, the representation bΓ(Σg) →π0 Symp(M(Σg)) is non-trivial on the
Torelli group I(Γ).
Proof. For g = 2, we have actually seen that the Dehn twist on the separating waist curve σ ⊂Σ2
induces a non-identity functor of Donaldson’s quantum category H(FM(Σ2)). For higher genus,
following Wehrheim and Woodward, we use induction on g with g = 2 the base case. Suppose for
contradiction that τσ induces the identity functor of the Donaldson category H(F(M(Σg))) but
the separating twist is non-trivial at genus g −1. Viewing the co-isotropic vanishing cycles Vγ
as Lagrangian correspondences, there are natural isomorphisms of functors Vγ ◦τ g
σ ◦V op
γ
∼= τ g−1
σ
(this is the cohomology level version of Theorem 3.14). But if τ g
σ ≃idHFM(Σg) then the left hand
side gives the identity functor, contradicting the inductive hypothesis.
□
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
