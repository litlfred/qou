---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-033-62-torsion-sheaf-bps-invariants
section_title: "Torsion sheaf BPS invariants"
section_number: 6.2
pages: 30-33
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
sheaves on X supported in dimension ≤ 1. Any sheaf E ∈ A has a Chern character ch( E)∈
H ∗(X, Z), which via Poincar´ e duality we can view as an element
ch(E) = ( β, n)∈ Γ = H2(X, Z)⊕ Z.
We note that for any objects E1, E2 of A, the Riemann-Roch theorem tells us that
χ(E1, E2) =
∑
i∈Z
(−1)i dimC Exti
X (E1, E2) =
∫
X
ch(E1)∨ ch(F ) td(X) = 0 ,
because the intersection number of any two curves on a threefold is zero. We therefore take ⟨−,−⟩
to be the zero form on Γ. We deﬁne a central charge Z : Γ → C via the formula
Z(β, n) = 2 π(β· ωC− n),
where ωC = B + iω∈ H 2(X, C) is a complexiﬁed K¨ ahler class. The assumption that ω is K¨ ahler
ensures that for any nonzero object E∈ A the complex number Z(E)∈ C lies in the semi-closed
upper half-plane
¯H ={z = r exp(iπφ) : r∈ R>0 and 0 < φ≤ 1}⊂ C∗.
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 31
It follows that Z deﬁnes a stability condition on the abelian category A.
For each class γ∈ Γ there is an associated BPS invariant Ω( γ)∈ Q ﬁrst constructed by Joyce and
Song ([ 21], see particularly Sections 6.3–6.4). They are deﬁned using moduli st acks of semistable
objects in A, and should not be confused with the ideal sheaf curve-counting in variants appearing in
the famous MNOP conjectures [ 25]. Joyce and Song prove that the numbers Ω( γ) are independent
of the complexiﬁed K¨ ahler class ωC. This is to be expected, since wall-crossing is trivial when the
form⟨−,−⟩ vanishes: see Remark A.4 below.
A direct calculation [ 21, Section 6.3] shows that
Ω(0 , n) =−χ(X), n ∈ Z\{ 0}. (38)
It is expected [ 21, Conjecture 6.20] that when β > 0 is a positive curve class
Ω(±β, n) = GV(0 , β), (39)
and, in particular, is independent of n. We shall assume this in what follows. We emphasise that
the higher genus Gopakumar-Vafa invariants are invisible from the p oint-of-view of the torsion
sheaf invariants Ω( γ).
6.3. Formal computation of the τ -function. The discussion of the last subsection gives rise
to a framed variation of BPS structures over the complexiﬁed K¨ ah ler cone of X, in which the BPS
invariants Ω( γ) are constant. Let us consider the family of double structures as deﬁned in Section
2.8. We can identify
Γ⊕ Γ ∨ = H∗(X, Z)
equipped with the standard intersection form, and the resulting BP S structures are all uncoupled.
Remarks 6.1. (i) We can easily extend this to a miniversal variation if required, by ﬁr st
introducing an extra factor q ∈ C∗ rescaling the central charge Z, and also adding a
component Z ∨ : Γ ∨→ C as in Section 2.8. The resulting central charge is
Z((β, n), λ) = 2 πq(β· ωC− n) + Z ∨(λ).
Nothing interesting is gained by doing this however.
(ii) We view the doubled structures deﬁned here as an approximation to the correct BPS
structures, which should also incorporate BPS invariants corresp onding to objects of the full
derived category Db Coh(X) supported in all dimensions. To deﬁne these rigorously would
32 TOM BRIDGELAND
involve constructing stability conditions on Db Coh(X), which for X a general compact
Calabi-Yau threefold is a well-known unsolved problem (see [ 3] and [ 28] for more on this).
Although our BPS structures are not ﬁnite, we can nonetheless tr y to solve the associated
Riemann-Hilbert problem by superposing inﬁnitely many gamma functio ns. Let us formally apply
(33) to compute for g≥ 2 the coeﬃcient
∑
γ∈Γ
Ω( γ)· B2g
4g(2g− 2)· 1
Z(γ)2g−2
of (2πit)2g−2 in the asymptotic expansion of the τ -function.1 The contribution from zero-dimensional
sheaves is
− χ(X)B2g
2g(2g− 2)(2π)2g−2·
∑
k≥1
1
k2g−2 = χ(X)(−1)g−1B2g B2g−2
4g(2g− 2)(2g− 2)! ,
which agrees with ( 35). The contribution from one-dimensional sheaves is
B2g
2g(2g− 2)(2π)2g−2
∑
β>0
∑
k∈Z
GV(0, β)
(vβ− k)2g−2 , (40)
where vβ = ωC· β. Using the identity
∑
k∈Z
1
(z− k)2g−2 = (2πi)2g−2
(2g− 3)! Li3−2g(e2πiz),
valid for Im( z) > 0 and g≥ 2, we can rewrite ( 40) as
(−1)g−1B2g
2g(2g− 2)!
∑
β>0
GV(0, β)· Li3−2g(e2πivβ ), (41)
which then agrees with ( 37). We conclude that under the variable change
λ = 2πit, x β = exp(2πivβ),
the log of the τ -function reproduces the genus 0 degenerate contributions to t he Gromov-Witten
generating function ( 34), at least for positive powers of λ.
Remark 6.2. In the paper [ 7] we give a rigorous solution to the Riemann-Hilbert problem in
the case when X is the resolved conifold. This involves writing down a non-perturbativ e function
which has the above asymptotic expansion.
1This calculation was worked out jointly with K. Iwaki.
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 33
