---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR INFINITE/INFINITESIMAL COUNTERPARTS
5
3. The algebra K(η, r) and the stabilization property
For a matrix A = (aij) ∈Mη(N) (resp. j = (ji) ∈Nη), let |A| = P
i,j aij (resp., |j| = P
i ji).
Let Ξ(η) = Mη(N), Ξ(η, r) = {A ∈Ξ(η) | r = |A|} and eΞ(η) = {(aij) ∈Mη(Z) : aij ⩾0 ∀i̸ =
j}.
Let V be a vector space of dimension r over a ﬁeld k. An η-step ﬂag is a collection f =
(Vi)i∈η of subspaces of V such that V = ∪i∈ηVi, Vi ⊆Vi+1 for all i ∈η⊣and Vi = 0 for i ≪0 if
η has no lower bound. Let F be the set of η-step ﬂags. The group G = G(k) := GL(V ) acts
naturally on F with orbits being the ﬁbres of the map F →Λ(η, r) := {λ ∈Nη | r = |λ|}
given by
(Vi)i∈η 7→(dim Vi/Vi−1)i∈η,
where V min (η)−1 = 0 if η is bounded below. If Fλ denotes the inverse image of λ ∈Λ(η, r),
then F = ∪λ∈Λ(η,r)Fλ, a disjoint union of G-orbits. If f ∈Fλ and Pλ is the stabilizer of f in
G, then Fλ ∼= G/Pλ.
Let V = V(k) = F × F and let G act on V diagonally. For (f, f′) ∈V where f = (Vi)i∈η
and f′ = (V ′
i )i∈η, the subspaces
Xi,j = Xi,j(f, f′) = Vi−1 + (Vi ∩V ′
j )
(where i, j ∈η) form an (η × η)-ﬂag:
· · · ⊆Xi,j ⊆Xi,j+1 · · · ⊆Xi+1,j ⊆Xi+1,j+1 · · · ⊆V.
Let ai,j = dim Xi,j/Xi,j−1. Setting Ψ(f, f′) = (ai,j) deﬁnes a map Ψ : V →Ξ(η). Then
Ξ(η, r) = imΨ. The G-orbits OA, A ∈Ξ(η, r), in V are the ﬁbres of Ψ.
When k = Fq is a ﬁnite ﬁeld of q elements, then the action of G(q) := G(k) on V(q) := V(k)
induces a permutation module ZV(q). Let Eη,r(q) be the Z-algebra with basis {eA}A∈Ξ(η,r)
and multiplication: for A, A′ ∈Ξ(η, r),
eA · eA′ =
X
A′′∈Ξ(η,r)
cA,A′,A′′eA′′
where, for ﬁxed (f1, f2) ∈OA′′,
cA,A′,A′′ = {f ∈V(q) | (f1, f) ∈OA, (f, f2) ∈OA′}.
Note that, if η is ﬁnite, then
Eη,r(q) = EndZG(q)(ZV(q)) op.
Thus, Eη,r(q) has an identity. This is not the case if η is inﬁnite.
It is well known that there are polynomials fA,A′,A′′ such that fA,A′,A′′(q) = cA,A′,A′′ for
all A, A′, A′′ ∈Ξ(η, r). Thus, we deﬁne a Z-algebra K(η, r) with basis {φB}B∈Ξ(η,r) and
multiplication
φA · φA′ =
X
A′′
fA,A′,A′′(v2)φA′′.
For any n ⩾1, we may embed Ξ([−n, n], r) into Ξ([−n −1, n + 1], r) by adding zeros
in rows and columns labelled with −n −1 or n + 1. This induces an algebra embedding
K([−n, n], r) into K([−n −1, n + 1], r) as a centralizer subalgebra eK([−n −1, n + 1], r)e for
an idempotent e. Thus, we obtain a direct system {K([−n, n], r)}n⩾1.
