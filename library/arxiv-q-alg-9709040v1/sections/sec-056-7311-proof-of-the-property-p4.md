---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-056-7311-proof-of-the-property-p4
section_title: "Proof of the property P4"
section_number: 7.3.1.1
pages: 32-34
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
7.3.1.1. Proof of the property P4
Graphs appearing in the calculation of Uk(ξ1, . . . , ξk) have k edges, k vertices of the ﬁrst type, and m
vertices of the second type, where
2k + m −2 = k .
Thus, there are no such graphs for k ≥3 as m is non-negative. The only intersting case is k = 2, m = 0.
The graph is looking as
32
p
p
1
2
.
.
By our construction, U2 restricted to vector ﬁelds is equal to the non-trivial quadratic map
ξ 7−→
d
X
i,j=1
∂i(ξj)∂j(ξi) ∈Γ(Rd, O),
ξ =
X
i
ξi∂i ∈Γ(Rd, T )
with the weight
Z
C2,0
dφ(12)dφ(21) =
Z
H\{z0}
dφ(z, z0) ∧dφ(z0, z)
where z0 is an arbitrary point of H.
Lemma. For arbitrary angle map the integral
R
H\{z0}
dφ(z, z0) ∧dφ(z0, z) is equal to zero.
Proof: We have a map C2,0−→S1 × S1, [(x, y)] 7→(φ(x, y), φ(y, x)). We calculate the integral of the
pullback of the standard volume element on two-dimensional torus. It is easy to see that the integral does not
depend on the choice of map φ : C2,0−→S1. The reason is that the image of the boundary of the integration
domain ∂C2,0 in S1 × S1 cancels with the reﬂected copy of itself under the involution (φ1, φ2) 7→(φ2, φ1) of
the torus S1 ×S1. Let us assume that φ = φh and z0 = 0+1·i. The integral vanishes because the involution
z 7→−z reverses the orientation of H and preserves the form dφ(z, z0) ∧dφ(z0, z).
Q.E.D.
7.3.2. Flat families over ΠT (Xcoor)
If X is a d-dimensional manifold, then there is a natural map of Q-manifolds (the Maurer-Cartan form)
ΠT (Xcoor)−→W .
It follows from following general reasons. If G is a Lie group, then it acts freely by left translations on itself,
and also on ΠT G. The quotient Q-manifold ΠT G/G is equal to Πg where g = Lie(G). Thus, we have a
Q-equivariant map
ΠT G−→Πg .
Analogous construction works for any principal homogeneous space over G. We apply it to Xcoor considered
as a principal homogeneous space for a non-existent group with the Lie algebra Wd.
The pullbacks of ﬂat families of formal manifolds over W constructed in 7.3.1, are two ﬂat families over
ΠT (Xcoor). As Q-equivariant bundles these families are trivial bundles
T × ΠT (Xcoor)−→ΠT (Xcoor),
D × ΠT (Xcoor)−→ΠT (Xcoor) .
Pullbacks of sections σT and σD gives sections in the bundles above. These sections we denote again by σT
and σD. The pullback of the morphism U × idW is also a morphism of ﬂat families.
7.3.3. Flat families over ΠT (Xaff)
33
Recall that Xaff is the quotient space of Xcoor by the action of GL(d, R). Thus, from functorial prop-
erties of operation ΠT (= Maps(R0|1, ·)) follows that ΠT (Xaff) is the quotient of Q-manifold ΠT (Xcoor)
by the action of Q-group ΠT (GL(d, R)).
We will construct an action of ΠT (GL(d, R)) on ﬂat families
T × ΠT (Xcoor) and D × ΠT (Xcoor) over ΠT (Xcoor). We claim that the morphism between these families
is invariant under the action of ΠT (GL(d, R)). Flat families over ΠT (Xaff) will be deﬁned as quotient
families. The morphism between them will be the quotient morphism.
The action of ΠT (GL(d, R)) on T and on W is deﬁned as follows. First of all, if G is a Lie group with
the Lie algebra g, then ΠT G acts Q-equivariantly on Q-manifold Πg, via the identiﬁcation Πg = ΠT G/G.
Analogously, if g is a subalgebra of a larger Lie algebra g1, and an action of G on g1 is given in a way
compatible with the inclusion g֒→g1, then ΠT G acts on Πg1.
We apply this construction to the case
G = GL(n, R) and g1 = Tpoly(Rd
formal) or g1 = Dpoly(Rd
formal).
One can check easily that sections σT and σD over ΠT (Xcoor) are ΠT (GL(d, R))-equivariant. Thus, we
get two ﬂat families over ΠT (Xaff).
The last thing we have to check is that the morphism U × idΠT (Xcoor) of ﬂat families
T × ΠT (Xcoor)−→D × ΠT (Xcoor)
is ΠT (GL(d, R))-equivariant. After the translation of the problem to the language of Lie algebras, we see
that we should check that U is GL(d, R)-invariant (property P3, that is clear by our construction), and that
