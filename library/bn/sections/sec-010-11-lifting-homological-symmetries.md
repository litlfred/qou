---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-010-11-lifting-homological-symmetries
section_title: "Lifting homological symmetries"
section_number: 11
pages: 50-52
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
toc_source: inferred
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cover- ings of P1, highlighting their"
---
Lifting homological symmetries
For brevity of notation, let Sp(X) = Sp(H1(X, Z)) ∼= Sp2g(Z), let Sp(X)T
denote the centralizer of T ∗, and let
Sp(X)T
d = Sp(X)T | Ker Φd(T ∗),
where Φd(x) is the dth cyclotomic polynomial. As in §7, we have natural
maps
Bn →Mod(X)T →Sp(X)T →Sp(X)T
d .
We say a group homomorphism φ : G1 →G2 almost onto if [G2 : φ(G1)] is
ﬁnite.
In this section we study the following purely topological question:
Question 11.1 When is the natural map Bn →Sp(X)T
d almost onto?
For example, by [A’C] we have:
Theorem 11.2 When d = 2, the natural map Bn →Sp(X)T
d ∼= Sp(X) is
almost onto for all n ≥3.
We will show that additional cases of Question 11.1 can be resolved using
arithmeticity of lattices.
Proposition 11.3 The following are equivalent:
1. The map Bn →Sp(X)T
d is almost onto.
2. The map Mod(X)T →Sp(X)T
d is almost onto.
3. There is a primitive dth root of unity q such that ρq(Bn) has ﬁnite
index in U(Λn,q).
Proof.
Up to isotopy, any mapping-class [φ] commuting with T can be
represented by a homeomorphism commuting with T (e.g. we may assume
T is conformal and take φ to be a Teichm¨uller mapping). This easily implies
that Bn →Mod(X)T is almost onto and hence (1) and (2) are equivalent.
We have also seen, in §7, that the projection of Sp(X)T
d to U(Λn,q) is almost
onto, so (1) is equivalent to (3).
49
Theorem 11.4 Suppose q is a primitive dth root of unity, and Γ = ρq(Bn) ⊂
U(1, s) is a lattice. Then Bn →Sp(X)T
d is almost onto if and only if Γ is
arithmetic.
Proof. If Γ′ = U(Λn,q) is discrete then the hypotheses imply both it and Γ
are arithmetic lattices, by Theorem 10.3, and hence [Γ′ : Γ] < ∞. Otherwise
Γ′ is indiscrete and [Γ′ : Γ] = ∞.
Corollary 11.5 The map B3 →Sp(X)T
d is almost onto if and only if the
Fuchsian (2, 3, p) triangle group is ﬁnite or arithmetic, where p is the order
of (d −2) in Z/2d.
(Explicitly, using Table 9, we ﬁnd B3 →Sp(X)T
d is almost onto iﬀd =
2, 3, 4, 5, 6, 7, 9, 10, 14, 15, 16, 18, 22 or 24.)
Proof. We may assume d = 2 or d ≥7, since otherwise Sp(X)T
d is ﬁnite.
Let q be the primitive dth root of unity closest to −1 with Im q ≤0. Then
ρq(B3) ⊂U(1, 1) is a lattice, namely the discrete (2, 3, p) triangle group
(with p = ∞when d = 2), and we may apply the Theorem above.
Corollary 11.6 The map Bn →Sp(X)T
d is almost onto whenever d and n
appear in Table 9 with associated signature (r, s) = (0, s) or (1, s).
Proof. In these cases either Sp(X)T
d is ﬁnite or ρq(Bn) ⊂U(1, s) is arith-
metic by Corollary 10.4.
Corollary 11.7 The map Bn →Sp(X)T is almost onto for d = 3 and
n = 3, 4, 5, 6; d = 5 and n = 3, 4, 5; and d = 7, n = 3.
Proof.
These cases appear in Table 9 as required, and d is prime, so
Sp(X)T
d = Sp(X)T .
On the other hand, since ρq(B4) ⊂U(1, 2) is a non-arithmetic lattice for
q = ζ−7
18 (see §10), we ﬁnd:
Corollary 11.8 The image of B4 has inﬁnite index in Sp(X)T
18.
50
Notes and references.
It is well-known that for any closed orientable
surface Σg of genus g, the natural map
Mod(Σg) →Sp(Σg)
is surjective [MKS, Thm. N13] (see also [Bu, §7], [FM, Thm. 7.3]). One
can then ask, which subgroups H ⊂Sp(Σg) lift to Mod(Σg)?
This is a
homological form of the Nielsen realization problem; cf. [Ker]. Question
11.1 is related to certain special cases of this question, where H is an abelian
group of the form ⟨S, T⟩.
A version of question 11.1 for ﬁnite abelian coverings of closed surfaces
is addressed in [Lo1].
