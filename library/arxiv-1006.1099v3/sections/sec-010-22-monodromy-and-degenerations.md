---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-010-22-monodromy-and-degenerations
section_title: "Monodromy and degenerations"
section_number: 2.2
pages: 10-12
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
homology computations on Σ 2 and on M(Σ 2) which helped to motivate Theorem 1.1. Let γ⊂ Σ
denote a homologically essential simple closed curve. Taking the subs pace of representations
trivial along γ deﬁnes a co-isotropic submanifold Vγ ⊂ M(Σ) which is an SU (2)-bundle over
M(Σ g−1), where the lower genus surface is essentially the normalisation of t he nodal surface
Σ/{γ}. When g = 2, M(Σ g−1) is a single point, and Vγ∼=SU (2) is a Lagrangian 3-sphere.
Lemma 2.4. Fix g = 2. Let γ and γ′ be homologically independent simple closed curves in Σ 2.
• If γ∩γ′ =∅ then Vγ∩Vγ′ =∅.
• If γ⋔γ′ ={pt} then Vγ⋔Vγ′ ={pt}.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 11
Proof. In the ﬁrst case, a representation in Vγ∩Vγ′ deﬁnes a ﬂat connexion on the sphere given
by cutting Σ 2 open along γ∪γ′, which however has non-trivial holonomy at the puncture. No
such representation can exist. Similarly, if γ⋔γ′ ={pt}, any element of Vγ∩Vγ′ deﬁnes a ﬂat
connexion on the torus given by cutting along γ∪γ′, with non-trivial monodromy at the puncture.
Such a connexion is deﬁned by a pair of matrices ( A,B )∈SU (2)2 with [A,B ] =−I, and it is a
straightforward exercise to see that there is a unique such pair up to simultaneous conjugation.
We must check that the corresponding intersection point of Vγ and Vγ′ is transverse, a result
easily extracted from either of [23, 86]. The map f : (A2,B 2)↦→[A2,B 2] from SU (2)2→SU (2)
has−I as a regular value, and there is an embedding
η :f −1(−I)×BI (δ)֒→SU (2)×SU (2)
for whichf◦η(x,u ) =−u, withBI (δ) a small open neighbourhood of I∈SU (2). We can therefore
embed an open neighbourhood of the zero-section Vγ = SU (2)⊂ T ∗SU (2)∼= su2×SU (2)֒→
M(Σ) by a map
g : (h,B 2) ↦→ (−e−h,B 2,η (A2,B 2, [e−h,B 2]−1).
This shows that locally near Vγ, the ﬁbre direction su2 is parametrised by the holonomy of the
transverse curve γ′, which implies that Vγ and Vγ′ meet transversely. □
Remark 2.5. An essential simple closed curve γ⊂ Σ 2 deﬁnes two Lagrangian 3-spheres, namely
hol−1
γ (±I). Call these Vγ and V¯γ. Since these spheres are disjoint, one obviously has
HF (Vγ,V γ)∼=H ∗(S3)∼=HF (V¯γ,V ¯γ); HF (Vγ,V ¯γ) = 0. (2.5)
The spheres Vγ and V¯γ lie in the same homology class and the same orbit under the action of
H 1(Σ; Z2). This should be compared with Remark 3.22.
The action on M(Σ) of a Dehn twist on Σ has been studied by Callahan and Seidel (both
unpublished, now discussed in detail in [106]). Let σ ⊂ Σ denote a nullhomologous but not
nullhomotopic simple closed curve, dividing Σ into subsurfaces of genu s 1 and g− 1 say (see
Figure 2). There is a unique conjugation-invariant function
SU2−→ [0, 1] for which log
(
eiπt 0
0 e−iπt
)
↦→t, 0≤t≤ 1.
This induces a map f : M(Σ)→ [0, 1], by taking the conjugacy class of the holonomy around σ.
A theorem of Goldman [42] implies that, on the open subset f −1(0, 1) where f is smooth, it is
the Hamiltonian function of a circle action. Explicitly, if σ corresponds to the curve deﬁning the
matrix Ag in the notation above, and if Ag⁄=±I, there is a unique homomorphism
φ :U (1)→SU2 with Ag∈φ({ℑ(z)> 0})
and the circle acts via
λ· (Ai,B i) = ( A1,B 1,...,A g,φ (λ)Bg).
Let Vσ = f −1(ǫ) for a small ǫ >0; V ⊂ M(Σ) is a separating hypersurface which is preserved
and acted upon freely by this S1-action. This manifests it as a ﬁbred co-isotropic submanifold,
with base the moduli space corresponding to the disconnected cur ve given by normalising the
nodal surface in which σ is collapsed to a point.
Proposition 2.6 (Seidel, Callahan) . Lettc denote the positive Dehn twist along a curve c⊂ Σ
and let τc denote the induced action of the twist on M(Σ) .
• τγ is a rank 3 ﬁbred positive Dehn twist in the S3-ﬁbred co-isotropic V¯γ.
• τσ is a rank 1 ﬁbred positive Dehn twist in the S1-ﬁbred co-isotropic Vσ.
12 IV AN SMITH
Both results are proved by considering the monodromy of suitable M orse-Bott degenerations,
cf. related discussions in [80, 86, 106] (the last reference contain s proofs of both cases). If
there is any equivalence of categories DπF(Σ 2)≃ DπF(M(Σ 2); 0) which respects the actions
of the mapping class group, then necessarily [ γ] ↦→[V¯γ], by combining Proposition 2.6 and
Corollary 3.7 (which says that Lagrangian spheres are essentially de termined by their associated
twist functors). Unfortunately, we do not know of any (smooth a nd embedded) Lagrangian
correspondence Γ ⊂ Σ 2× M(Σ 2) which might deﬁne such a functor. The upshot of the following
sections will be to show that a certain generalised Lagrangian corre spondence
Σ 2↝ Z↝ M(Σ 2)
does deﬁne an equivalence on suitable subcategories, where Z denotes the relative quadric
BlM(Σ) (P5). Even here, two subtleties arise: the ﬁrst correspondence (fr om the curve to the
relative quadric) would be singular, and not amenable to quilt theory ( so we will avoid it and
use more algebraic arguments); and the second correspondence will not itself be fully faithful,
but will have an idempotent summand which induces the desired equiva lence.
