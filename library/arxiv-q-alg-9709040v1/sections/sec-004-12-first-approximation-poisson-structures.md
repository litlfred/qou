---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-004-12-first-approximation-poisson-structures
section_title: "First approximation: Poisson structures"
section_number: 1.2
pages: 3-3
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
It follows from the associativity of ⋆that the bilinear map B1 : A × A−→A satisﬁes the equation
fB1(g, h) −B1(fg, h) + B1(f, gh) −B1(f, g)h = 0,
i.e. the linear map eB1 : A ⊗A−→A associated with B1 as eB1(f ⊗g) := B1(f, g), is a 2-cocycle in the
cohomological Hochschild complex of algebra A (the deﬁnition of this complex is given in 3.4.2).
Let us decompose B1 into the sum of the symmetric part and of the anti-symmetric part:
B1 = B+
1 + B−
1 ,
B+
1 (f, g) = B+
1 (g, f), B−
1 (f, g) = −B−
1 (g, f) .
Gauge transformations
B1 7→B′
1,
B′
1(f, g) = B1(f, g) −fD1(g) + D1(fg) −D1(f)g
where D1 is an arbitrary diﬀerential operator, aﬀect only the symmetric part of B1, i.e. B−
1 = (B′
1)−. One
can show that the symmetric part B+
1 can be killed by a gauge transformation (and it is a coboundary in
the Hochschild complex).
Also one can show that the skew-symmetric part B−
1 is a derivation with respect to both functions f
and g. Thus, B−
1 comes from a bi-vector ﬁeld α on X:
B−
1 (f, g) = ⟨α, df ⊗dg⟩,
α ∈Γ(X, ∧2TX) ⊂Γ(X, TX ⊗TX) .
Analogous fact in algebraic geometry is that the second Hochschild cohomology group of the algebra of
functions on a smooth aﬃne algebraic variety (in characteristic zero) is naturally isomorphic to the space of
bi-vector ﬁelds (see 4.6.1.1).
The second term O(¯h2) in the associativity equation f ⋆(g ⋆h) = (f ⋆g) ⋆h implies that α gives a
Poisson structure on X,
∀f, g, h
{f, {g, h}} + {g, {h, f}} + {h, {f, g}} = 0,
where {f, g} := f ⋆g −g ⋆f
¯h
|¯h=0 = 2 B−
1 (f, g) = 2⟨α, df ⊗dg⟩.
In other words, [α, α] = 0 ∈Γ(X, ∧3TX), where the bracket is the Schouten-Nijenhuis bracket on polyvector
ﬁelds (see 4.6.1 for the deﬁnition of this bracket).
Thus, gauge equivalence classes of star-products modulo O(¯h2) are classiﬁed by Poisson structures on
X. A priori it is not clear whether there exists a star-product with the ﬁrst term equal to a given Poisson
structure, and whether there exists a preferred choice of an equivalence class of star-products. We show in
this paper that there is a canonical construction of an equivalence class of star-products for any Poisson
manifold.
