---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-036-a1-introductory-remarks
section_title: "A.1. Introductory remarks"
section_number: null
pages: 36-37
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
sider here a slightly simpliﬁed situation which should help to make the gen eral picture clearer. Let
(Γ , Z, Ω) be a BPS structure. Given a basis ( γ1,··· , γn)⊂ Γ there is a corresponding cone
Γ ⊕ =
{
γ =
∑
diγi with di∈ Z≥0
}
⊂ Γ ,
whose elements we call positive. We call a class γ∈ Γ negative if −γ is positive.
Let us assume that we can ﬁnd a basis such that every active class is either positive or negative,
and further that all positive classes γ∈ Γ satisfy Im Z(γ) > 0. These assumptions are always
satisﬁed for BPS structures arising from stability conditions on quiv ers. Let us also temporarily
ignore the diﬀerence between the tori T±.
The co-ordinate ring C[T] can be identiﬁed with the algebra of Laurent polynomials
C[T] = C[y±1
1 ,··· , y±n
n ],
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 37
and a regular automorphism of T corresponds to an automorphism of this algebra. The element
DT(ℓ) corresponding to an active ray ℓ⊂ C∗ does not in general deﬁne an element of C[T] however,
since it could an inﬁnite sum of characters. If a ray ℓ⊂ C∗ lies in the upper half-plane, the series
DT(ℓ) deﬁnes an element of the power series ring
C[[T]] = C[[y1,··· , yn]],
which is a Poisson algebra in the same way as C[T]. We can then deﬁne an algebra automorphism
S(ℓ)∗ = exp{DT(ℓ),−}∈ Aut C[[T]],
and interpret the wall-crossing formula ( 15) in the group of automorphisms of C[[T]], at least for
sectors ∆ ⊂ C∗ contained in the upper half-plane.
In what follows we will modify this procedure in two ways. Firstly, to av oid the assumption on
active classes we will work with completions of C[T] deﬁned by more general cones in Γ. Secondly,
note that if the form ⟨−,−⟩ = 0 is trivial, the automorphisms S(ℓ)∗ as deﬁned above will all be
identity maps, and the wall-crossing formula will become vacuous. On e way to avoid this problem
would be to force the form ⟨−,−⟩ to be non-degenerate by passing to the double BPS structure as
in Section 2.8. Instead, we will formulate the wall-crossing formula in a group deﬁn ed abstractly
by using the Baker-Campbell-Hausdorﬀ formula to formally exponen tiate elements of C[[T]].
