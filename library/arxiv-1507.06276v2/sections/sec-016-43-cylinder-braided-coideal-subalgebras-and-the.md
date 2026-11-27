---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-016-43-cylinder-braided-coideal-subalgebras-and-the
section_title: "Cylinder-braided coideal subalgebras and the universal K-matrix"
section_number: 4.3
pages: 19-21
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
Examples 4.1, 4.3, and 4.7 can be formalized in the setting of bialgebras and their
coideal subalgebras. For the convenience of the reader we recall the relevant notions
in the setting of the present paper.
Deﬁnition 4.8. ([Kas95, Deﬁnition VIII.2.2]) A bialgebra H with coproduct ∆H :
H → H ⊗ H is called braided (or quasitriangular) if there exists an in vertible
element RH ∈H ⊗H such that the following two properties hold:
(1) For all x ∈H one has
∆op
H (x) = (RH )−1∆H (x)RH(4.9)
where∆op
H = ﬂip ◦∆H :H →H ⊗H denotes the opposite coproduct.
(2) The element R satisﬁes the relations
(∆H ⊗ idH )(RH ) = RH
23RH
13, (idH ⊗∆H )(RH ) = RH
12RH
13(4.10)
where we use the usual leg-notation.
In this case the element RH is called a universal R-matrix for H.
20 MARTINA BALAGOVI ´C AND STEF AN KOLB
LetH be a braided bialgebra with universal R-matrix RH = ∑
isi ⊗ti ∈H ⊗H.
In this situation the category A =H-mod ofH-modules is a braided tensor category
with braiding
cH
M,N :M ⊗N →N ⊗M, m ⊗n ↦→
∑
i
sin ⊗tim(4.11)
for all M,N ∈Ob(A), see [Kas95, VIII.3].
Remark 4.9. The conventions in Deﬁnition 4.8 slightly diﬀer from the con ventions
in [Kas95]. The reason for this is that following [Lus94] we use the braiding R ·κ−1 ·
ﬂip for Oint and hence the braiding RH ◦ ﬂip for H-mod. To match conventions
observe that RH in Deﬁnition 4.8 coincides with R21 in [Kas95, Deﬁnition VIII.2.2] .
Let B be a right coideal subalgebra of H. As in Example 4.3 deﬁne B to be the
category with Ob(B) = Ob(A) and Hom B(M,N ) = Hom B(M,N ) for all M,N ∈
Ob(A). Then ( B, A) is a tensor pair. For any bialgebra automorphism ϕ :H →H
deﬁne
RH,ϕ = (id ⊗ϕ)(RH )
In analogy to the notion of a universal R-matrix the following deﬁnitio n is natural.
Deﬁnition 4.10. LetH be a braided bialgebra with universal R-matrix RH ∈H⊗H
and let ϕ :H →H be an automorphism of braided bialgebras. We say that a right
coideal subalgebraB of H is ϕ-cylinder-braided if there exists an invertible element
K ∈ H such that
Kb =ϕ(b)K for all b ∈B,(4.12)
∆(K) = ( K ⊗ 1)RH,ϕ(1 ⊗ K)RH
21.(4.13)
In this case we call K a ϕ-universal K-matrix for the coideal subalgebra B. If
ϕ = idH then we simply say that B is cylinder-braided and that K is a universal
K-matrix for B.
The bialgebra automorphism ϕ deﬁnes a braided tensor equivalence tw : A → A
given by M ↦→Mϕ, where as before Mϕ denotes the H-module which coincides
with M as a vector space and has the left action h ⊗m ↦→ϕ(h)m. In the above
setting aϕ-universal K-matrix for the coideal subalgebra B deﬁnes a family of maps
tM :M →M, m ↦→ Km, for all M ∈Ob(A).(4.14)
By construction the natural transformation t = (tM )M∈Ob(A) is a tw-cylinder twist
for the tensor pair ( B, A).
Remark 4.11. Observe the parallel between Deﬁnition 4.8 and Deﬁnition 4. 10 in
the case ϕ = idH . Indeed, condition (4.9) means that the maps cH
M,N deﬁned by
(4.11) are H-module homomorphisms while condition (4.12) means that the maps
tM deﬁned by (4.14) areB-module homomorphisms if ϕ = idH . Similarly, condition
(4.10) and (4.13) both express compatibility with the tensor product.
Deﬁnition 4.10 can be extended to include the quantized universal en veloping
algebraUq(g) which is braided only in the completion. In this case we also need to
allow for K to lie in the completion U . We repeat Deﬁnition 4.10 in this setting
for later reference. Recall the notation from Section 3 and from E xample 4.7. For
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 21
any Hopf algebra automorphisms ϕ :Uq(g) →Uq(g) deﬁne an element ˆRϕ ∈ U (2)
by
( ˆRϕ)M,N = ˆRM ϕ ,N for all M,N ∈Ob(Oint).
In the following deﬁnition we reformulate condition (4.13) in terms of ˆR and ˆRϕ.
Deﬁnition 4.12. Letϕ :Uq(g) →Uq(g) be a Hopf algebra automorphism. A right
coideal subalgebraB ⊆Uq(g) is called ϕ-cylinder-braided if there exists an invertible
element K ∈ U such that the relation
Kb =ϕ(b)K for all b ∈B(4.15)
holds in U and the relation
∆(K) = ( K ⊗ 1) · ˆRϕ · (K ⊗ 1) · ˆR(4.16)
holds in U (2). In this case we call K a ϕ-universal K-matrix for the coideal subal-
gebra B. If ϕ = idUq(g) then we simply say that B is cylinder-braided and that K
is a universal K-matrix for B.
Similarly to the discussion for the bialgebra H above, a cylinder-braided coideal
subalgebra of Uq(g) naturally gives rise to a cylinder twist. For later reference we
summarize the situation in the following remark.
Remark 4.13. Let B ⊆ Uq(g) be a right coideal subalgebra and let (B, Oint) be
the tensor pair from Example 4.1. Moreover, let ϕ : Uq(g) → Uq(g) be a Hopf-
algebra automorphism and let tw : Oint → Oint be the corresponding braided tensor
equivalence as in Example 4.7. An element K ∈ U is a ϕ-universal K-matrix for B
if and only if K is a tw-cylinder twist of (B, Oint). In this case, in particular, the
element t = K ∈ U satisﬁes the fusion procedure (4.7) and the reﬂection equation
(4.8) for all M,N ∈ Oint.
