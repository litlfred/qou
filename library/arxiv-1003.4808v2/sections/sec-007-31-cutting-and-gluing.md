---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-007-31-cutting-and-gluing
section_title: "Cutting and gluing"
section_number: 3.1
pages: 15-16
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
In its more mathematical incarnation, a 3-dimensional TQFT can be thought of as a
functor Z that assigns
closed 3-manifold M ↝ numberZ(M)
closed 2-manifold Σ ↝ vector space Z(Σ)
closed 1-manifold S1 ↝ category Z(S1)
point p ↝ 2-category Z(p).
(3.2)
For our applications to Chern-Simons theory, we will really only need the top two levels
Z(M) and Z(Σ). The ﬁner structure of categories and 2-categories has recently been
explored in e.g. [29].
Figure 4: Hilbert space assigned to a surface Σ and partition function assigned to a
three-manifold M in TQFT.
If a 3-manifoldM has a boundary Σ =∂M , the objectZ(M) is no longer a number,
but an element of the vector space Z(Σ) assigned to the boundary, as shown in Figure
4. This vector space is in fact a Hilbert space, so let us denote it as HΣ = Z(Σ). At
the top two levels, the TQFT must then satisfy the following axioms of Atiyah and
Segal (cf. [30]).
1. A change of orientation Σ →− Σ dualizes the Hilbert space, H−Σ =H∗
Σ .
2. For a boundary consisting of multiplet disjoint components,HΣ1⊔Σ2 =HΣ1⊗HΣ2.
3. Using the ﬁrst two axioms, we see that for a manifold M with∂M = (−Σ1)⊔ Σ2
one obtains a map Z(M) : HΣ1→H Σ2. Then, given a 3-manifold N that can
be written as N =M1∪Σ2M2, with ∂M1 = (−Σ1)⊔ Σ2 and ∂M2 = (−Σ2)⊔ Σ3
as illustrated below, the functoriality propertyZ(N) =Z(M2)◦Z(M1) must hold.
14
4. For the empty boundary, HΣ=⊘ = C .
5. For M = Σ×I, the map Z(M) :HΣ
id
→H Σ is just the identity.
Using these axioms, the partition function Z(M) of any three-manifold, with or
without boundary, may be constructed by cutting the manifold into pieces and taking
inner products in boundary Hilbert spaces to glue the pieces back together. For this
purpose, it is often convenient to know how the mapping class group of a surface Σ
acts onHΣ, in order to properly identify the Hilbert spaces on two sides of a gluing.
There are many examples of three-dimensional TQFT, diﬀering essentially in the
deﬁnitions of the boundary Hilbert spaces H(Σ), as well as the action of the mapping
class groups on these spaces. In the case of Chern-Simons theory with gauge group G
