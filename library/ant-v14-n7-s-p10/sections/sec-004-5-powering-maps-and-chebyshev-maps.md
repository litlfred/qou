---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-004-5-powering-maps-and-chebyshev-maps
section_title: "Powering maps and Chebyshev maps"
section_number: 5
pages: 9-11
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
toc_source: inferred
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Front matter; Introduction; Some algebraic lemmas"
---
In a slightly more general framework than what has been described above, in this section we consider pairs
(φ, α), where φ(x)∈K[x] is a polynomial and where α ∈K. We deﬁne recursively K0 = K0(φ, α)= K(α)
and Kn = Kn(φ, α) = Kn−1(φ−n(α)) for n ≥1, and set K∞(φ, α) = S Kn(φ, α). Since the requirement
that φ and α are deﬁned over K have been relaxed, K0/K may be a proper extension and the Kn/K may
no longer be Galois extensions.
1990
Jesse Andrews and Clayton Petsche
Proposition 11. Let K be a number ﬁeld, let φ(x), ψ(x) ∈K[x] be two polynomials of degree d ≥2,
and let α, β ∈K.
(a) If (φ, α) is K-conjugate to (ψ, β), then K∞(φ, α) is contained in a ﬁnite extension of K ab if and
only if K∞(ψ, β) is contained in a ﬁnite extension of K ab.
(b) If φ(x), ψ(x), α, β are deﬁned over K ab and (φ, α) is K ab-conjugate to (ψ, β), then K∞(φ, α)/K
is an abelian extension if and only if K∞(ψ, β)/K is an abelian extension.
Proof. (a) There exists a ﬁnite extension F/K such that φ(x), ψ(x), α, β are all deﬁned over F,
and extending F if necessary there exists an automorphism γ (x) = ax + b deﬁned over F for which
ψ = γ ◦φ ◦γ −1 and β = γ (α). Note that for each n ≥0, γ restricts to a bijection from φ−n(α) onto
ψ−n(β). In particular, it follows that K∞(ψ, β) ⊆F K∞(φ, α), and thus if K∞(φ, α) is contained in a
ﬁnite extension L of K ab, then K∞(ψ, β) is contained in the ﬁnite extension LF of K ab. The reverse
implication follows from symmetry.
(b) In the preceding argument, we may take F ⊆K ab. Thus if K∞(φ, α) ⊆K ab, then K∞(ψ, β) ⊆K ab
as well, and conversely by symmetry.
□
The following two results verify the Conjecture in the special case that φ(x) is K-conjugate to a
powering map xd or to a Chebyshev map Td(x).
Theorem 12. Let φ(x) ∈K[x] be a polynomial of degree d ≥2, let α ∈K be a nonexceptional point for
φ, and assume that the pair (φ, α) is K-conjugate to the pair (xd, β) for β ∈K. Then K∞(φ, α)/K is an
abelian extension if and only if β is a root of unity and (φ, α) is K ab-conjugate to (xd, β).
Proof. Assume that β is a root of unity and that (φ, α) is K ab-conjugate to (xd, β). Then K∞(xd, β) is a
cyclotomic, and hence abelian, extension of K, and it follows from Proposition 11(b) that K∞(φ, α)/K
is an abelian extension.
Conversely, assume that K∞(φ, α)/K is an abelian extension. Using Proposition 11(a), it follows that
K∞(xd, β) is contained in a ﬁnite extension L of K ab. If β is not a root of unity, then h(β) > 0. (Note
that β̸ = 0 by the assumption that α is not an exceptional point of φ, and hence β is not an exceptional
point of xd.) But β1/dn ∈K∞(xd, β) ⊆L for all n ≥0, and h(β1/dn) = 1
dn h(β) →0+ as n →+∞, a
contradiction of Theorem 9. We conclude that β must be a root of unity.
Finally, we must show that the K-conjugacy between (φ, α) and (xd, β) is actually deﬁned over K ab.
By hypothesis there exists γ (x) = ax + b deﬁned over K for which xd = γ ◦φ ◦γ −1(x) and β = γ (α).
Moreover, γ restricts to a bijection from the backward φ-orbit of α onto the backward xd-orbit of β. These
are inﬁnite sets contained in K ab, since both K∞(φ, α)/K and K∞(xd, β)/K are abelian extensions.
Selecting distinct corresponding pairs γ (s1) = t1 and γ (s2) = t2 with s j, t j ∈K ab, we have that both
a = (t1 −t2)/(s1 −s2) and b = (s1t2 −t1s2)/(s1 −s2) are in K ab.
□
Let d ≥2 be an integer, and let Td(x) ∈Z[x] be the d-th Chebyshev polynomial; that is, Td(x) is the
unique polynomial of degree d satisfying Td(x + 1/x) = xd + 1/xd. In other words, considering the
Abelian extensions in dynamical Galois theory
1991
2-to-1 rational map π : Gm →A1 deﬁned by π(x) = x + 1/x, we have a commutative diagram
Gm
xd
−−−→Gm
π
y
yπ
A1
Td
−−−→A1.
(9)
See [Silverman 2007, Section 6.2].
Theorem 13. Let φ(x) ∈K[x] be a polynomial of degree d ≥2, let α ∈K be a nonexceptional point for
φ, and assume that the pair (φ, α) is K-conjugate to the pair (Td, β) for β ∈K. Then K∞(φ, α)/K is an
abelian extension if and only if β = ζ + 1/ζ for some root of unity ζ ∈K and (φ, α) is K ab-conjugate to
(Td, β).
Proof. Assume that β = ζ +1/ζ for some root of unity ζ ∈K and that (φ, α) is K ab-conjugate to (Td, β).
By the commutative diagram (9), the points ϵ ∈K satisfying T n
d (ϵ) = β are precisely the points of the
form ϵ = ξ + 1/ξ, as ξ ranges over the dn-th roots of ζ. In particular, K∞(Td, β) is contained in a
cyclotomic, and hence abelian, extension of K, and it follows from Proposition 11(b) that K∞(φ, α)/K
is an abelian extension.
Conversely, assume that K∞(φ, α)/K is an abelian extension. Using Proposition 11(a), it follows
that K∞(Td, β) is contained in a ﬁnite extension L of K ab; let D = [L : K ab]. Select ζ ∈π−1(β), thus
β = ζ +1/ζ, and assume that ζ is not a root of unity. In particular h(ζ) > 0. Let n ≥0 and select ϵn ∈K
satisfying T n
d (ϵn) = β; thus ϵn = ξn +1/ξn for some dn-th root ξn = ζ 1/dn of ζ. Since ϵn ∈K∞(Td, β) ⊆L,
it follows that ξn is contained in a quadratic extension of L and hence contained in an extension of K ab
of degree ≤2D. It follows from Theorem 9 that h(ξn) ≥CK,2D. But as n ≥0 is arbitrary, we may let
n →+∞and obtain h(ξn) = 1
dn h(ζ) →0+, a contradiction. We conclude that ζ must be a root of unity.
That the K-conjugacy between (φ, α) and (Td, β) is actually deﬁned over K ab follows from the same
argument used in Theorem 12.
□
