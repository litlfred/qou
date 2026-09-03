---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-011-62-properties-of-principal-2-bundles
section_title: "Properties of Principal 2-Bundles"
section_number: 6.2
pages: 36-38
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
Principal Γ-2-bundles over M form a bicategory denoted 2- BunΓ (M ). There is an evident pullback
2-functor
f ∗ : 2-BunΓ (N ) /d47/d47 2-BunΓ (M )
associated to smooth maps f : M /d47/d47 N , and these make 2- BunΓ a pre-2-stack over smooth
manifolds. We deduce the following important two theorems about th is pre-2-stack. The ﬁrst
asserts that it actually is a 2-stack:
Theorem 6.2.1. Principal Γ -2-bundles form a 2-stack 2-BunΓ over smooth manifolds.
Proof. This follows from Theorem 5.1.5 (Γ-bundle gerbes form a 2-st ack) and Theorem 7.1 (the
equivalence GrbΓ ∼= 2-BunΓ ) we prove in Section 7. □
Remark 6.2.2. Similar to Remark 5.1.6, we obtain automatically bicategories 2- BunΓ (X ) of prin-
cipal Γ-2-bundles over Lie groupoids X , including bicategories of equivariant principal Γ -2-bundles .
The second concerns a homomorphism Λ : Γ /d47/d47 Ω of Lie 2-groups, which induces the extension
Λ : GrbΓ /d47/d47 GrbΩ between 2-stacks of bundle gerbes (Proposition 5.2.1). Combined w ith the
equivalence GrbΓ ∼= 2-BunΓ of Theorem 7.1, it deﬁnes a 1-morphism
Λ : 2- BunΓ /d47/d47 2-BunΩ
– 36 –
between 2-stacks of principal 2-bundles. Now we get as a direct co nsequence of Theorem 5.2.2:
Theorem 6.2.3. If Λ : Γ /d47/d47 Ω is a weak equivalence between Lie 2-groups, then the 1-morph ism
Λ : 2 -BunΓ /d47/d47 2-BunΩ is an equivalence of 2-stacks.
A third consequence of the equivalence of Theorem 7.1 in combination with Lemma 5.2.7 is
Corollary 6.2.4. Every 1-morphism F : P1 /d47/d47 P2 between principal Γ -2-bundles over M is
invertible.
The following discussion centers around local trivializability that is implicitly contained in Def-
inition 6.1.5. A principal Γ-2-bundle that is isomorphic to the trivial Γ-2 -bundle I introduced in
Example 6.1.7 is called trivializable. A section of a principal Γ-2-bundle P overM is an anafunctor
S :Mdis /d47/d47 P such that π ◦S = idMdis (recall that an anafunctor π ◦S :M /d47/d47 M is the same as
a smooth map). One can show that every point x ∈ M has an open neighborhood U together with
a section s : Udis /d47/d47 P|U . Such sections can even be chosen to be smooth functors, rathe r than
anafunctors, namely simply as ordinary sections of the surjective submersion π : (P|U )0 /d47/d47 Udis.
Lemma 6.2.5. A principal Γ -2-bundle over M is trivializable if and only if it has a smooth section.
Proof. The trivial Γ-2-bundle I has the section S(m) := (m, 1), where 1 denotes the unit of Γ 0. If
P is trivializable, and F : I /d47/d47 P is an isomorphism, then, F ◦S is a section of P. Conversely,
suppose P has a section S :Mdis /d47/d47 P. Then, we get the anafunctor
I =Mdis × Γ
S ×id /d47/d47 P × Γ R /d47/d47 P. (6.2.1)
It has an evident Γ-equivariant structure and respects the proj ections toM . According to Corollary
6.2.4, this is suﬃcient to have a 1-isomorphism. □
Corollary 6.2.6. Every principal Γ -2-bundle is locally trivializable, i.e. every point x ∈ M has an
open neighborhoodU and a 1-morphism T : I /d47/d47 P|U .
Remark 6.2.7. In Wockel’s version [Woc11] of principal 2-bundles, local trivializations are required
to be smooth functors and to be invertible as smooth functors, ra ther than allowing anafunctors.
This version turns out to be too restrictive in the sense that the re sulting bicategory receives no
2-functor from the bicategory GrbΓ (M ) of Γ-bundle gerbes that would establish an equivalence.
It is also possible to reformulate our deﬁnition of principal 2-bundles in terms of local trivializa-
tions. This reformulation gives us criteria which might be easier to che ck than the actual deﬁnition,
similar to the case of ordinary principal bundles.
Proposition 6.2.8. Let P be a Lie groupoid, π : P /d47/d47 Mdis be a surjective submersion functor,
and R be a smooth right action of Γ on P that preserves π. Suppose every point x ∈ M has
– 37 –
an open neighborhood U together with a Γ -equivariant anafunctor T : I /d47/d47 P|U that respects the
projections. Then, π : P /d47/d47 Mdis is a principal Γ -2-bundle over M .
Proof. We only have to prove that the functor τ is a weak equivalence, and we use Theorem 2.3.13.
Since all morphisms of P have source and target in the same ﬁbre of π : P0 /d47/d47 Mdis, we may
check the two conditions of Theorem 2.3.13 locally, i.e. for P|Ui where Ui is an open cover of M .
Using local trivializations Ti : I /d47/d47 P|Ui, the smooth functor τ translates into the smooth functor
(id, pr1,m ) : Mdis × Γ × Γ /d47/d47 (Mdis × Γ) ×M (Mdis × Γ). This functor is an isomorphism of Lie
groupoids, and hence essentially surjective and fully faithful. □
