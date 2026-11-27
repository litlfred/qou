---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-030-61-weyl-transformation-of-the-stress-tensor
section_title: "Weyl transformation of the stress tensor"
section_number: 6.1
pages: 34-36
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
Thus far we have extracted the stress tensor for a conformal ﬂ uid in ﬂat space R3, 1. We
would like to ensure that the second order stress tensor we ha ve derived transforms homo-
geneously under Weyl rescaling. In order to check this we per form the obvious minimal
covariantization of our stress tensor to generalize it to a ﬂ uid stress tensor about an arbi-
trary boundary metric gµν .22 and study its Weyl transformation properties.
Consider the Weyl transformation of the boundary metric
gµν = e2φ ~gµν ⇒ gµν = e−2φ ~gµν
& uµ = e−φ ~uµ , T = e−φ ~T .
(6.1)
It is well known that the ﬁrst order truncation of the stress t ensor (2.8) transforms as
T µν = e−6 φ ~T µν under this transformation (see for instance Appendix D of [4 4]). We pro-
ceed to show that this transformation rule holds for the two d erivative stress tensor as well.
This transformation property, together with the traceless ness of the stress tensor, ensures
Weyl invariance of the ﬂuid dynamical equations ∇µ T µν , appropriate for a conformal ﬂuid.
It follows from (6.1) that P µν = gµν + uµ uν = e−2φ ~P µν . The Christoﬀel symbols
transform as [44]
Γ ν
λµ = ~Γ ν
λµ + δν
λ ∂µ φ + δν
µ ∂λ φ − ~gλµ ~gνσ ∂σ φ .
The transformation of the covariant derivative of uµ is given by
∇µ uν = ∂µ uν + Γ ν
µλ uλ = e−φ
[
~∇µ ~uν + δν
µ ~uσ ∂σ φ − ~gµλ ~uλ ~gνσ ∂σ φ
]
. (6.2)
This equation can be used to derive the transformation of var ious quantities of interest in
22All metrics in this subsection refer to the metric on the boun dary, i.e.., the background spacetime on
which the ﬂuid is propagating.
ﬂuid dynamics, such as the acceleration aµ , shear σµν , etc..
θ = ∇µ uµ = e−φ
(
~∇µ ~uµ + 3 ~uσ ∂σ φ
)
= e−φ
(
~θ + 3 ~Dφ
)
,
aν = Duν = uµ ∇µ uν = e−2φ
(
~aν + ~P νσ ∂σ φ
)
,
σµν = P λ (µ ∇λ uν ) − 1
3 P µν ∇λ uλ = e−3φ ~σµν ,
ℓµ = uα ǫαβγµ ∇β uγ = e−2φ ~ℓµ
(6.3)
where in the last equation we have accounted for the fact that all epsilon symbols in (2.9)
should be generalized in curved space to their covariant cou nterparts. The objects with
correct tensor transformation properties scale as metric d eterminants i.e., ǫαβγδ ∝ √g,
and ǫαβγδ ∝ 1√g , from which it is easy to infer their scaling behaviour under conformal
transformations; in particular, ǫαβγδ = e4φ ~ǫαβγδ and ǫαβγδ = e−4φ ~ǫ αβγδ .
The Weyl transformation of the two derivative terms that occ ur in the stress tensor
(2.9) is given by
T µν
A = e−4φ ~T µν
A , for A = {2a, 2b}
T µν
B = e−4φ
(
~T µν
B + ~δT
µν
B
)
, for B = {2c, 2d, 2e}
(6.4)
where the inhomogeneous terms arising in the Weyl transform ation are:
δT µν
2c = 3 Dφ
(
∇(µ uν ) + u(µ aν ) − 1
3 θ P µν
)
δT µν
2d = 2 a(µ ∇ν )φ + 2 u(µ aν ) Dφ − 2
3 aα ∇α φ
+ 2 u(µ ∇ν )φ Dφ + uµ uν (Dφ)2 − 1
3 P µν (Dφ)2 + ∇µ φ ∇ν φ − 1
3 P µν ∇α φ ∇α φ
δT µν
2e = −∇(µ uν ) Dφ − 3 u(µ aν ) Dφ + 1
3 P µν θ Dφ − 2 a(µ ∇ν )φ + 2
3 P µν aα ∇α φ
− uµ uν (Dφ)2 + 1
3 P µν (Dφ)2 − 2 u(µ ∇ν )φ Dφ − ∇µ φ ∇ν φ + 1
3 P µν ∇α φ ∇α φ
(6.5)
While the conformal transformation involves the inhomogen eous terms presented in
(6.5) we need to ensure that the full stress tensor is Weyl cov ariant. Satisfyingly, these
inhomogeneous terms cancel among themselves in the precise combination that occurs in
(2.8); consequently the linear combination of terms that oc curs in the stress tensor trans-
forms covariantly. Note that the cancelation of inhomogene ous terms depends sensitively
on the ratio of coeﬃcients of T2c, T2d and T2e; and so provides a check of our results. Note
however that T2a and T2b are separately Weyl covariant. In summary, our result for th e
two derivative stress tensor is a linear combination (with p recisely determined coeﬃcients)
of three independently Weyl covariant forms, with scaling w eight −4 (for upper indices).
Using the transformation of the temperature (6.1) it follow that the full stress tensor
transforms under Weyl transformation as
T µν = e−6φ ~T µν . (6.6)
R. Loganayagam [41] informs us that he has found a compact way of rewriting our stress
tensor T µν (2.8) that makes the Weyl invariance of each of its three piec es manifest.
