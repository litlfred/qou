---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-047-2-for-a-ribbon-algebra-h-it-is-trivial-that-t-ma
section_title: "For a ribbon algebra H it is trivial that T maps Z(H) into itself, since θ ∈ Z(H). ✷"
section_number: 2
pages: 57-59
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
57
The modularity condition requires invertibility of the mat rix
Si,j = (T rq
πi ⊗ T rq
πj )(R21R12), (A.7)
where i, j range over the equivalence classes of irreducible represen tations of H. Now, in
the semisimple case the representations are in one-to-one c orrespondence with the minimal
projections in Z(H), which leads to the following result.
Theorem A.11 Let H be a factorizable quasitriangular semisimple and cosemisi mple
Hopf algebra. Then the category Rep H is modular.
Proof. We have already proven that Rep H is a spherical ribbon category. Thus by Propo-
sition A.9 the center of H is stable under the Fourier transform S+. By factorizability
S+ is invertible, and the same holds for the restriction S+ ↾ Z(H). By the remark after
Lemma A.4 the quantum traces on H-modules V , in terms of which the S-matrix is de-
ﬁned, coincide with the usual traces on End V . In terms of the basis for Z(H) given by
the minimal idempotents Pi we obtain
S+(Pj ) =
∑
i
Sij Pi,
where the matrix S = (Sij) is invertible. But S is nothing but the modular matrix (A.7)
as we have
Sij = di µ(Pi S+(Pj )) = di (µ ⊗ µ)(R21R12 (Pi ⊗ Pj))
= 1
dj
(Trq
i ⊗ Trq
j )(R21R12)
We have used µ(Pi) = 1 /di and µ(x Pi) = 1 /di Tri(x) [55]. ■
Note that the proof is conceptually quite similar to our proo f of modularity for general
semisimple spherical categories. In view of Lemma A.1 the fo llowing is now immediate:
Corollary A.12 Let H be semisimple and cosemisimple. Then Rep D(H) is modular.
We close the appendix with a remark which is meant to aid the re ader in appreciating
the ‘self-duality’ of a quantum double D(H), in particular since in general it is not self-
dual in the sense of Hopf algebras: D(H)∗ ⁄≃D(H). (For a ﬁnite abelian group G we in
fact have D(G) ≃ D(G)∗ ≃ CG ⊗ C(G).) For any ﬁnite dimensional Hopf algebra one
can use the integrals to deﬁne ‘Fourier transforms’ H → ˆH. In [42] Fourier transforms
Fσ,σ′ , σ, σ′ = ±, deﬁned as linear maps H → ˆH which intertwine certain actions of H on
H and ˆH by multiplication and translation, respectively, were stu died systematically and
used to give a new proof of the invertibility of the antipode. There is a beautiful relation
between these more conventional Fourier transforms, relat ing H and ˆH, and the selfdual
Fourier transforms [34], which map D(H) onto itself. For simplicity we restrict ourselves
to FDKA’s, where things are easier since the Haar measures ar e two-sided invariant traces
and since there are unique Fourier transforms F : H → ˆH and ˆF : ˆH → H:
⟨F(x), y⟩ = ⟨µ, xS(y)⟩, ∀x, y ∈ H, (A.8)
⟨α, ˆF (β)⟩ = ⟨ˆS(α)β, Λ ⟩, ∀α, β ∈ ˆH, (A.9)
58
where Λ , µ are the integrals in H, ˆH, respectively. If ι : H → D(H), ˆι : ˆH → D(H) are
the canonical embedding maps then the following diagram com mutes:
ˆH ⊗ H ˆι ⊗ ι✲ D(H) ⊗ D(H) m✲ D(H)
H ⊗ ˆH
ˆF ⊗ F
❄
ι ⊗ ˆι
✲ D(H) ⊗ D(H) m
✲ D(H)
S−
❄
This nice observation is due to Kerler [26, Proposition 9] (w ith diﬀerent conventions), who,
however, did not emphasize the interpretation of F, ˆF as conventional Fourier transforms.
