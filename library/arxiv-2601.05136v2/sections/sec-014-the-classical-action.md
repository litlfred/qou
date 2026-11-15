---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-014-the-classical-action
section_title: "The classical action"
section_number: null
pages: 13-14
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
Here we deﬁne an action S(D) corresponding to the N →∞limit of SN(D). Set
(4.2)
Ω+(t1, t2, t3, t4) := L(t4 −t1) + L(t2 −t3)
−L(t2 −t1 + 1) −L(t4 −t3)
−2πi(t2 −t1)
Ω−(t1, t2, t3, t4) := −L(t1 −t4 + 1) −L(t3 −t2 + 1)
+ L(t1 −t2) + L(t3 −t4 + 1)
+ 2πi(t2 −t1)
Assign complex variables ti to the segments as before and construct a function S(D|t) by taking a
sum over crossing functions
t2
t4
t1
t3
→Ω+(t1, t2, t3, t4)
(4.3)
t1
t3
t2
t4
→Ω−(t1, t2, t3, t4)
(4.4)
and assigning critical points shifts in the variables (which we could also think of as δ functions)
t
t
t
t
t −1
t
t + 1
t
(4.5)
Deﬁnition 4.2. The construction above deﬁnes the classical action as a holomorphic function
S(D) : ΩD →C
where
ΩD =

t ∈CE 

 ti −tj̸ ∈X whenever i, j meet at a corner of D
	
The classical action is a variant of Yokota’s potential function introduced in [Yok00] and used
throughout the Volume Conjecture literature. We prefer to call it an action to match the language
used in physics, since it is essentially the Chern-Simons action if we view ΩD as parametrizing ﬂat
sl2 connections on the knot complement. Our action includes parameter shifts that appear to be
related to the normalization terms Ω1, Ω2 studied by Ohtsuki and Takata [OT15].
Deﬁnition 4.3. A generalized critical point γ ∈CE of the classical action is one where
exp ∂S(D)
∂ti

γ
= 1 for all i ∈E.
or equivalently, a point for which there is a ﬂattening vector k ∈ZE with
∂S(D)
∂ti

γ
= 2πiki for all i ∈E.
