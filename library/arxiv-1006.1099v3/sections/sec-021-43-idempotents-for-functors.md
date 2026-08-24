---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-021-43-idempotents-for-functors
section_title: "Idempotents for functors"
section_number: 4.3
pages: 36-37
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
categories. We begin by recalling the construction of a split-closure . An idempotent up to
homotopy for an object Y ∈ A is an A∞-functor from K to A taking the unit of the ﬁeld to Y .
Explicitly, this amounts to giving a collection of elements
℘d∈hom1−d
A (Y,Y ); d≥ 1
satisfying the equations
∑
r
∑
s1,...,sr
µr
A(℘s1,...,℘ sr ) =
{
℘d−1 if d is even,
0 if d is odd (4.4)
summing over partitions s1 +··· +sr =d. If p∈Hom H(A)(Y,Y ) is an idempotent endomorphism
in the cohomological category 3, there is always an idempotent up to homotopy ℘ for which
[℘1] = p [92, Lemma 4.2]. Any A∞-category has a split-closure Π A, meaning a fully faithful
functor A→ Π A with the property that in the larger category all asbtract images of idempotents
up to homotopy are quasi-represented. The abstract image of ℘ (an idempotent with target
Y ∈ A) is a certain A∞-module Z in mod-A, with underlying vector spaces
X↦→homA(X,Y )[q] where q is a formal variable of degree −1
and with operations beginning with
µ1
Z(b(q)) =
∑
r
∑
s2,...,sr
δs2+···+sr
q µr
A(℘sr,...,℘ s2,b (q)) + ∆ b(q).
Here δq is normalised formal diﬀerentiation, qk↦→qk−1 and q0↦→0, whilst ∆ denotes antisym-
metrization followed by δq (we will not write out the higher order operations). By [92, Lemma
4.5], one has the critical property that:
Hom H(mod−A)(Z, Z′) ∼= e·Hom H(A)(Y,Y ′)·e′ (4.5)
whenever Z and Z′ are the abstract images of idempotents up to homotopy with targe ts Y,Y ′
corresponding to cohomological idempotents e∈Hom H(A)(Y,Y ) and e′∈Hom H(A)(Y ′,Y ′).
3Since our categories are Z2-graded, such idempotents are necessarily of even degree.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 37
Lemma 4.17. Let A, B and C be non-unital A∞-categories and suppose there is an A∞-functor
Φ : A→ nu-fun (B, C). To each idempotent up to homotopy ℘ for Y ∈ A one can canonically
associate an element of nu-fun (B, Π C).
Proof. ℘ is deﬁned by a functor K→ A so there is a composite functor K→nu-fun (B, C) with
target Φ Y . This is deﬁned by a sequence of elements
℘d
Φ Y ∈hom1−d
nuf un(B,C)(Φ Y, Φ Y ).
The degree zero term in this morphism of functors yields elements
℘Φ Y (B)∈hom1−d
C (Φ Y (B), Φ Y (B))
which satisfy the conditions of Equation 4.4. Thus ℘Φ Y (B) is an idempotent up to homotopy for
Φ Y (B)∈ C, for each B∈ B. The functor Φ Y is deﬁned by a collection of natural maps
homB(Bd−1,B d)⊗···⊗ homB(B1,B 2)→homC(Φ Y (B1), Φ Y (Bd))[1−d]
We claim these induce maps
homB(Bd−1,B d)⊗···⊗ homB(B1,B 2)→homΠ C(℘Φ Y (B1),℘ Φ Y (B2))[1−d]
where ℘• denotes the abstract image of the given idempotent. To see this, s ince Π C is by
deﬁnition a certain category of modules, thus of functors from C to chain complexes, an element
of homΠ C(F, G) is explicitly deﬁned by the collection of maps
homC(Cd−1,C d)⊗···⊗ homC(C1,C 2)→homCh (F(C1), G(Cd)).
Taking the functors F = Φ Y (B1) and G = Φ Y (Bd), we require maps
homC(Cd−1,C d)⊗···⊗ homC(C1,C 2)−→
homCh (homC(C1, Φ Y (B))[q],hom C(Cd, Φ Y (B))[q])
These are canonically obtained by using composition µd
C in the category C. It is a straightforward
check to see that the construction is compatible with varying B, hence yields a functor from B
to Π C as required. □
Corollary 4.18. There is a natural functor Π A→nu-fun (B, Π C).
We will not need this stronger result and omit the proof.
