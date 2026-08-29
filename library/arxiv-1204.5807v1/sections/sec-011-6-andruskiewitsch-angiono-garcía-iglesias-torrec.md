---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-011-6-andruskiewitsch-angiono-garcía-iglesias-torrec
section_title: "ANDRUSKIEWITSCH, ANGIONO, GARCÍA IGLESIAS, TORRECILLAS , V AY"
section_number: 6
pages: 6-7
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect exampl es."
---
Condition (2.2) is less apparent. If H is a ﬁnite-dimensional Hopf algebra
andω ∈H a pivot, then (2.2) holds in the following instances:
• ω is an involution.
• There exists a Hopf subalgebra K ofH such that ω ∈K and (K,ω )
is spherical– since EndH(V ) ⊂ EndK (V ).
• H is ribbon, see Subsection 2.7.
• All ﬁnite-dimensional H-modules are naturally self-dual.
Proof. By hypothesis, there exists a natural isomorphism F : id → ∗. Let
V ∈ RepH and ϑ ∈ EndH(V ). Then
tr(ϑω) =
∑
i
⟨αi,ϑωv i⟩ =
∑
i
⟨ϑ∗αi,ωv i⟩ =
∑
i
⟨FVϑF −1
V αi,ωv i⟩
=
∑
i
⟨FVϑω−1F −1
V αi,v i⟩ = tr(FVϑω−1F −1
V ) = tr(ϑω−1).
Here {vi} and {αi} are dual basis of V and V ∗ respectively. □
Proposition 2.1. A pivotal Hopf algebra (H,ω ) is spherical if and only if
(2.2) holds for all S ∈ IrrH.
Proof. The Proposition follows from the following two claims.
Claim 1. If (2.2) holds for M1,M 2 ∈ RepH, then it holds for M1 ⊕M2.
Indeed, let h ∈ EndH(M1 ⊕M2). Let πj :M →Mj, ιi :Mi →M be the
projection and the inclusion, for 1 ≤i,j ≤ 2. Then h = ∑
1≤i,j≤2hij, where
hij = πi ◦h ◦ιj ∈ HomH(Mj,M i). In particular, hijω = (hω)ij as linear
maps. Now, we have that trM (h) = tr M1(h11) + trM2(h22) and thus
trM (hω) = tr M1(hω)11 + trM2(hω)22 = tr M1(h11ω) + trM2(h22ω)
= tr M1(h11ω−1) + trM2(h22ω−1) = tr M1(hω−1)11 + trM2(hω−1)22
= tr M (hω−1).
Claim 2. If (2.2) holds for every semisimple H-module, then H is spherical.
LetM ∈ RepH and letM0 ⊂M1 ⊂ · · · ⊂ Mk =M be the Loewy ﬁltration
of M , that is M0 = Soc M , Mi+1/Mi ≃ Soc(M/Mi), i = 0,...,j − 1. In
particular,Mi+1/Mi is semisimple. We prove the claim by induction on the
Loewy length k of M . The case k = 0 is the hypothesis. Assume k > 0;
set S = SocM and consider the exact sequence 0 →S →M →M/S → 0.
Hence the Loewy length of ~M = M/S is k − 1 and thus (2.2) holds for it.
Also, (2.2) holds for S by hypothesis. Let f ∈ EndH(M ), then f (S) ⊆S and
thus f induces f1 = f|S ∈ EndH(S) by restriction and factorizes through
f2 ∈ EndH( ~M ). Therefore, we can choose a basis of S and complete it
to a basis of M in such a way that f in this new basis is represented by
[f ] =
[
[f1] ∗
0 [ f2]
]
. Also, as ω preserves S and f is an H-morphism, it follows
that [fω ] =
[
[f1ω] ∗
0 [ f2ω]
]
and thus trM (fω ) = tr M (fω −1). □
FROM HOPF ALGEBRAS TO TENSOR CATEGORIES 7
Example 2.2. Let H be a basic Hopf algebra, i. e. all ﬁnite-dimensional
simple modules have dimension 1; when H itself is ﬁnite-dimensional, this
amounts to the dual of H being pointed. If ω ∈G(H) is a pivot, then H is
spherical if and only if χ(ω) ∈ {± 1} for all χ ∈ Alg(H, k). Assume that H
is ﬁnite-dimensional; then H is spherical if and only if ω is involutive. For,
ω −ω−1 ∈ ⋂
χ∈Alg(H,k) Kerχ = RadH, and RadH ∩ k[ω] = 0 .
