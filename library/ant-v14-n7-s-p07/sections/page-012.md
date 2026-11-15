---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-012
section_title: "Page 12"
section_number: null
pages: 12-12
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
1906
Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
the general “minimalist conjecture” philosophy, which holds that positive ranks should be a density 0
phenomenon except when forced by parity considerations from the functional equation (in this setting the
functional equation never forces positive rank, and the rank is always even.)
Corollary 3.3. Let A be an abelian variety deﬁned over a ﬁnite ﬁeld Fq of odd characteristic. For each
f ∈Qn,qm, denote by A f the quadratic twist of A ×Fq Fqm(x) by f . Let Rn,m be the set { f ∈Qn,qm :
A f has positive rank}. Then
lim
m→∞lim sup
n→∞
|Rn,m|
|Qn,qm| = 0.
Proof. Let P(x) be the characteristic polynomial of Frobenius acting on the Tate module of A and let q−s
be one of its roots. Then rank A f > 0 is equivalent to L(s, χ f ) = 0. (See [Li 2018, Proposition 4.6] for a
similar statement with the same proof.) Thus, the statement is a direct application of Theorem 3.2.
□
We now prove Theorem 1.5, which makes use of the mod 2 Galois representations on J(C) rather
than the representations modulo odd primes.
Proof of Theorem 1.5. Let x1, . . . , x2g+2 be the set of Weierstrass points of C. The 2-torsion subgroup
J(C)[2] is spanned by the degree-0 2-torsion divisors xi −x j. That is, the group of divisors of the form
P aixi with P ai = 0 surjects onto J(C)[2]. Note also that x1 + · · · + x2g+2 −(2g + 2)x1 is a principal
divisor and thus x1 + · · · + x2g+2 is 0 in J(C)[2]. See [Gross 2012, Section 4] for detailed discussion.
This identiﬁes J(C)[2] with an explicit subquotient of F2g+2
2
; namely, J(C)[2] is the quotient of the
subspace (a1, . . . , a2g+2) : P ai = 0 by the 1-dimensional subspace spanned by (1, . . . , 1).
This identiﬁcation is equivariant for the Frobenius action on both sides, so it allows us to describe the
mod 2 Galois representation afforded by J(C) in terms of the permutation π which Frobenius induces on
x1, . . . , x2g+2. To be precise, the action of S2g+2 on J(C)[2] is a representation ρ : S2g+2 →Sp2g(Z/2Z),
and the action of Frobenius on J(C)[2] is given by ρ(π).
The conditions on π given in Theorem 1.5 are equivalent to the condition that π2 is a product of
two disjoint odd cycles. Thus, the action of π2 in its permutation representation F2g+2
2
has eigenvalues
given by µk and µ2g+2−k for some odd 1 ≤k ≤2g + 1; passing to the subquotient J(C)[2] removes two
eigenspaces of ρ(π2) with the eigenvalue 1. So the eigenvalues of Frob2 on J(C)[2] are the multiset
µ′
k ∪µ′
2g+2−k, where µ′
n denotes the nontrivial n-th roots of unity. We see in particular that ρ(π2) does
not have 1 as an eigenvalue. But if the zeta function ZC had a zero at 1
2, then √q would be a Frobenius
eigenvalue on C, which would mean that q was an eigenvalue of Frob2; we have shown that Frob2 has no
eigenvalue congruent to 1 mod 2, which rules this out. This proves (1).
What’s more, the multiset µ′
k∪µ′
2g+2−k contains any eigenvalue at most twice, and if (k, 2g+2−k)=1,
no eigenvalue appears more than once. This proves (2) (or rather, it proves (2) for the zeta function of
C/Fq2, from which (2) is immediate.)
□
Proof of Corollary 1.6. By assumption, f is an irreducible polynomial over Fq. So when deg f = n is
even, Frobenius acts on the set of Weierstrass points of C f : y2 = f (x) as a n-cycle. If deg f = n is odd,
then Frobenius acts on the set of Weierstrass points of C f as a disjoint union of a (n−1)-cycle and a
