---
doc_id: arxiv-1611.09182v1
doc_title: ""
section_id: sec-029-47-the-dirac-algebra
section_title: "The Dirac algebra"
section_number: 4.7
pages: 34-36
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? C. Furey A thesis presented to the University of Waterloo in fulfillment of the thesis requirement for the degree of Doctor of Philosophy Physics — 57 sections"
---
It is not enough for us here to consider minimal left ideals for just Ψ L or for just Ψ R,
separately. We would like also to combine these two objects together into a single four-
complex-dimensional Dirac spinor, as shown in Section 3.5.2.
It had been mentioned earlier that chirality, L and R, is the analogue of spin, ↑ and
↓, in this formalism. One can conﬁrm that left multiplying Ψ L and Ψ R by C⊗ H causes
rotation between their spin states,↑ and↓, whereas right multiplying ΨL and ΨR by C⊗ H
causes rotation between L and R.
The left action and right action of C⊗ H on itself each give a representation of Cl(2).
Furthermore, taking 𝓁, a, r∈ C⊗ H, one can easily show that 𝓁a = ar∀a⇒ 𝓁,r ∈ C⊂
C⊗ H. That is, the left action of C⊗ H on itself cannot be re-expressed as the right
action of C⊗ H on itself, and vice versa. It is a property of C⊗ H that these two actions
are distinct, a feature which does not appear in the case of C⊗ O. Furthermore, the
associativity of C⊗ H ensures that the left and right action commute with each other.
26
Hence, the underlying Cliﬀord algebraic structure when considering both left and right
multiplication of C⊗ H on itself is Cl(2)⊗C Cl(2), where the tensor product is over C.
As Cl(n)⊗C Cl(2)≃ Cl(n+2) for n∈ Z≥ 0, we then ﬁnd that Cl(2)⊗C Cl(2)≃ Cl(4).
Furthermore, as the complexiﬁcation of a real Cliﬀord algebra, Cl(p,q ) acts to erase its
signature, C⊗Cl(p,q )≃ Cl(p +q), we then ﬁnd that Cl(4)≃ C⊗Cl(1, 3).
In other words, the left and right action of C⊗ H on itself gives a representation of the
Dirac algebra.
It is straightforward for readers to conﬁrm this fact. Explicitly, the gamma matrices
γ0,γ1,γ2, and γ3, written in the Weyl basis, have the following correspondences in C⊗ H:
γ0 =
( 0 I
I 0
)
↦→ 1|iϵx γ1 =
( 0 σx
−σx 0
)
↦→ iϵx|ϵy
γ2 =
( 0 σy
−σy 0
)
↦→ iϵy|ϵy γ3 =
( 0 σz
−σz 0
)
↦→ iϵz|ϵy.
(4.9)
These ﬁndings are likely to appear in future joint work with G. Fiore from INFN.
Here, we make use of the bar notation from earlier authors, [50]. By deﬁnition, the
operator a|b acting on some element c, for a,b,c ∈ C⊗ H, is given simply by acb. As an
example, consider the object corresponding to γ0 acting on Ψ D∈ C⊗ H,
1 ΨDiϵx = 1 (Ψ L + ΨR) iϵx
=
(
ψ↑
Lϵ↑↑ +ψ↓
Lϵ↓↑ +ψ↑
Rϵ↑↓ +ψ↓
Rϵ↓↓
)
iϵx
=
(
ψ↑
Rϵ↑↑ +ψ↓
Rϵ↓↑ +ψ↑
Lϵ↑↓ +ψ↓
Lϵ↓↓
)
.
(4.10)
This ﬂips chirality, as one would expect.
From these operators, an object corresponding to γ5≡iγ0γ1γ2γ3 can be found to be
γ5 =
(−I 0
0 I
)
↦→ −1|iϵz. (4.11)
This thereby conﬁrms the role of P and P∗ as 1
2 (1∓γ5), introduced early on in equa-
tion (3.5).
27
More generally, it can now be seen that Ψ D = ΨL + ΨR introduced previously, does in
fact behave as a Dirac spinor, acted upon by a complex quaternionic representation of the
Dirac algebra, C⊗Cl(1, 3).
