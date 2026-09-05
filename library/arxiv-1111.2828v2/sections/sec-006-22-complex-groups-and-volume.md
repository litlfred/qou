---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-006-22-complex-groups-and-volume
section_title: "Complex groups and volume"
section_number: 2.2
pages: 9-10
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
bundles over M and representations π1(M ) → G up to conjugation. This correspondence takes a
ﬂat bundle to its holonomy representation. If ρ : π1(M ) → G is a representation, we let Eρ denote
the corresponding ﬂat bundle. In the following G denotes a simply connected, simple, complex Lie
group, and M a closed, oriented 3-manifold. The following deﬁnition is motivated by Theorem 2.8
below.
Deﬁnition 2.5. The complex volume VolC(ρ) of a representation ρ : π1(M ) → G is deﬁned by
(2.7) ˆc(Eρ)(M ) = i VolC(ρ) ∈ C/4π2Z.
The volume Vol(ρ) of ρ is the real part of VolC(ρ).
The bundle Eρ is isomorphic to ~M ×ρG, and we thus have a 1-1 correspondence between sections of
Eρ and ρ-equivariant maps~M → G such that f : ~M → G corresponds to the section s(x) = [~x, f(~x)].
Lemma 2.6. For any ρ-equivariant map f : ~M → G, we have i VolC(ρ) =
∫
D f ∗(σ(P )), where D is
a fundamental domain for M in ~M .
Proof. For any invariant form η ∈ Ω 3(G)G, the form θ(η) ∈ Ω 3(Eρ; F) is induced by the pullback of
η under the projection ~M × G → G. Letting η = σ(P ), the result follows from ( 2.5). □
Let H3 = SL(2 , C)/SU(2) be hyperbolic 3-space. We identify the orthonormal frame bundle
F (H3) of H3 with PSL(2, C).
Lemma 2.7. For G = SL(2, C), σ(P ) = −h∗ ∧ e∗ ∧ f ∗, where h =
( 1 0
0 −1
)
, e = ( 0 1
0 0 ) and f = ( 0 0
1 0 )
are the standard generators of sl(2, C) over C.
10 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Proof. As in Example 2.4, P = 1
2 Tr. Using the fact that Tr(AB) = Tr( BA), it follows from ( 2.3)
that σ(P ) ∈ Ω 3(G)G = ∧3(g∗) is given by
(2.8) g × g × g → C, (A, B, C) ↦→ −1
2 Tr(A[B, C]).
A simple computation shows that if A =
( a bc −a
)
, B =
(
e f
g −e
)
and C =
(
i j
k −i
)
(2.9) − 1
2 Tr(A[B, C]) = − det
(
a b c
e f g
i j k
)
= −h∗ ∧ e∗ ∧ f ∗(A, B, C).
This proves the result. □
Theorem 2.8. Let M = H3/Γ be a closed hyperbolic 3-manifold, and let ρ : π1(M ) → SL(2, C) be
a lift of the geometric representation. We have
(2.10) ˆc(Eρ)([M ]) = i(Vol(M ) + iCS(M )) in C/2π2Z,
where CS(M ) = 2 π2 cs(M ), and cs(M ) is the (Riemannian) Chern-Simons invariant [7, (6.2)] .
Proof. The fact that the imaginary part equals volume is well known, and follows from the fact (see
Dupont [ 12]) that the imaginary part of σ(P ) is cohomologous to the pullback of the hyperbolic
volume form. Yoshida [ 28, Lemma 3.1] shows that the real part of the form h∗ ∧e∗ ∧f ∗ equals 2π2 cs,
where cs is the Riemannian Chern-Simons form on F (H3) = PSL(2 , C) (pulled back to SL(2, C).
Note that the Riemannian connection on F (H3) = PSL(2 , C) descends to the Riemannian connection
on F (M ) = PSL(2 , C)/Γ . If f : ~M → SL(2, C) is ρ-equivariant, the composition
(2.11) ~M
f /d47/d47 SL(2, C) /d47/d47 PSL(2, C) /d47/d47 PSL(2, C)/Γ = F (M )
is ρ-invariant, and thus descends to a section of F (M ). The result now follows from Yoshida’s result
together with Lemma 2.7 and Lemma 2.6. □
Remark 2.9. Note that Theorem 2.8 implies that modulo 2π2, the complex volume of a represen-
tation lifting the geometric representation only depends o n M and not on the choice of lift.
Remark 2.10. Since P is real on K, the imaginary part of σ(P ) is cohomologous to an invariant
3-form on G/K. Since H 3(g, k; R) = R, there is a unique such form up to scaling. We may thus
think of Im(σ(P )) as a volume form.
