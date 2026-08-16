---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-004-5-tilting-modules-in-the-modular-case
section_title: "Tilting modules in the modular case"
section_number: 5
pages: 13-16
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick id eals."
---
We recall some statements about tilting modules over a ﬁeld k and a
complete discrete valuation ring R.
5.1. W eights. Let k be a ﬁeld of characteristic p> 0 and G a semisimple,
simply connected algebraic group over k. We denote by Rep(G) the category
of ﬁnite dimensional representations. We ﬁx a maximal torus T and a Borel
subgroupB. We denote by R the set of roots and by R+ the set of positive
roots. The dominant integral weights are
X(T )+ = {λ ∈X(T ) | <λ,α ∨ >≥ 0 ∀α ∈R+}.
14 THORSTEN HEIDERSDORF AND HANS WENZL
5.2. Induced modules and W eyl modules. The induction functor from
B to G is not exact. For any B-module M we put
H i(M ) = RiInd G
BM, i ∈ N
and also abbreviate
H i(λ) = H i(kλ)
where kλ stands for k regarded as a B-module via λ ∈ X(T ). All these
H i(λ) are ﬁnite dimensional over k [
J03, I.5.12.c]. The following properties
are well-known:
(1) For λ ∈X(T )+ we have H 0(λ) ⁄= 0.
(2) If λ ∈ X(T )+, then soc(H 0(λ)) =: L(λ) is simple, and any ﬁnite
dimensional simple G-module is isomorphic to exactly one L(λ).
(3) L(λ)∗ ∼
=L(−w0λ) where w0 is the longest element of the Weyl group
W .
(4) EndG(H 0(λ)) ∼
= k ∼
=EndGL(λ).
(5) H i(λ) = 0 for i> 0 and λ ∈X(T )+ (Kempf vanishing).
We deﬁne V (λ) := H 0(−w0λ)∗. We call H 0(λ) the induced module and
V (λ) the Weyl module. A G-module V has a good ﬁltration if there is an
ascending chain
0 = V0 ⊂V1 ⊂...
such that V = ⋃
iVi and Vi/Vi−1 ∼
=H 0(λi) for some λi ∈X(T )+. Likewise
we say it has a Weyl ﬁltration if Vi/Vi−1 ∼
= V (λi) for some λi ∈ X(T )+.
Then
(1) V admits a good ﬁltration iﬀ Ext1
G(V (λ),V ) = 0 ∀λ ∈X(T )+.
(2) V admits a Weyl ﬁltration iﬀ Ext1
G(V,H 0(λ)) = 0 ∀λ ∈X(T )+.
(3) V has a Weyl ﬁltration iﬀ V ∗ has a good ﬁltration.
(4) The tensor product of two modules with a good ﬁltration ha s again
a good ﬁltration.
5.3. Tilting modules over k. A ﬁnite dimensional G-module is called a
tilting module if it has a Weyl ﬁltration and a good ﬁltration . We denote
by Tilt (G,k ) the full subcategory of tilting modules where k is a ﬁeld of
characteristic p >0. The direct sum and the tensor product of two tilting
modules is tilting. If V1,V 2 are tilting modules, then Ext1
G(V1,V 2) = 0 ∀i>
0.
Proposition 5.1. [
J03, Lemma E.6] For each λ ∈ X + there exists a
unique indecomposable tilting module T (λ) such that the weight space T (λ)λ
is free of rank 1 over k and such that T (λ)µ ⁄= 0 impliesµ ≤λ. Every tilting
module can be written in a unique way as a direct sum of these T (λ).
5.4. Tilting modules over discrete valuation rings. The entire theory
of tilting modules can be developed over more general rings. We assume
now that R is a complete discrete valuation ring.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 1 5
For a split reductive group G over Z we denote by GR the group over
R obtained by extension of scalars to R (but we may omit the subscript if
there is no risk of confusion). As for R =k, one deﬁnes
H i
R(M ) = RiInd GR
BR (M ), Hi
R(λ) = H i
R(Rλ).
We denote by V (λ)Z the Z-form of the irreducible GQ-module V (λ), λ ∈
X(T )+ as in [ J03, II.8.3] and put
V (λ)R =V (λ)Z ⊗ZR.
By [ J03, II.8.8, II.8.9] H 0
R(λ) ∼
= H 0
Z(λ) ⊗ZR, H i(λ) = 0 for all i > 0 and
V (λ)R ∼
=H 0
R(−w0λ)∨. The analogue of Kempf’s vanishing theorem permits
to develop the theory of good ﬁltrations and Weyl ﬁltrations also over R.
Lemma 5.2. [
J03, Lemma B.9, B.10] Suppose R is a complete discrete
valuation ring. Let M be a G-module that is free of ﬁnite rank over R. Then
GF1.1 - GF1.3 are equivalent and GF1.4 - GF1.6 are equivalent.
GF1.1 M has a good ﬁltration.
GF1.2 Ext1
G(V (λ)R,M ) = 0 ∀λ ∈X(T )+.
GF1.3 For each maximal m in R the GR/m-module M ⊗R/m has a good
ﬁltration.
GF1.4 M has a Weyl ﬁltration.
GF1.5 Ext1
G(M,H 0
R(λ)) = 0 ∀λ ∈X(T )+.
GF1.6 For each maximal m in R the GR/m-module M ⊗R/m has a Weyl
ﬁltration.
Note that if a G-module M has a good ﬁltration, then M is free over R
(since all H 0(µ) are so) and for each R-algebra R′ the GR′-module M ⊗R′
has a good ﬁltration since H 0(µ) ⊗R′ ∼
=H 0
R′(µ) [
J03, 8.8(1)]. Furthermore
V (λ) ⊗R/m ∼
=V (λ)R/m [
J03, 8.3].
In particular we can deﬁne tilting modules for GR. Any tilting module
for GR is free of ﬁnite rank over R.
Lemma 5.3. [J03, Lemma E.19, Proposition E.22] Suppose that R is
a complete discrete valuation ring. For each λ ∈ X + there exists a unique
indecomposable tilting moduleTR(λ) such that the weight space TR(λ)λ is free
of rank 1 over R and such that TR(µ)(µ) ⁄= 0 implies µ ≤ λ. Every tilting
module can be written in a unique way as a direct sum of these TR(λ).
Remark 5.4. The existence of the T (λ) with the correct properties works
in greater generality (for instance if R is a Dedekind ring which is a principal
ideal domain, see [ J03, Section E]). While any tilting module for such R can
be decomposed into a direct sum of indecomposable tilting mo dules, their
decomposition will in general not be unique.
5.5. Extension of scalars for tilting modules. By [
J03, E.20] M is an
indecomposable GR-module if and only if EndGR(M ) is a local ring. We
have
EndGR(T (λ)) = RidTR(λ) +rad EndTR(λ)(TR(λ)),
16 THORSTEN HEIDERSDORF AND HANS WENZL
where
rad EndGR(TR(λ)) = {ϕ ∈EndGR(TR(λ)) | ϕ((TR(λ)λ) ⊂ m(TR(λ))λ}.
Furthermore
EndGR/ m(TR(λ)) ⊗RR/m) ∼
=EndGR(TR(λ)) ⊗RR/m.
From this one concludes that EndGR/ m(TR(λ)) ⊗RR/m) is a local ring and
that therefore TR(λ) ⊗R/m is indecomposable.
Corollary 5.5. [
J03, E.20] We have
TR(λ) ⊗R/m ∼
=TR/m(λ).
