---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-013-25-super-tannakian-categories
section_title: "Super Tannakian categories"
section_number: 2.5
pages: 43-44
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
35
hence EndP(P) is a skew ﬁeld or zero, and P is simple or zero in P. Over
an algebraically closed ﬁeld Λ there exist no skew ﬁelds other than Λ itself,
hence in this case we have EndP(P) = Λ, and it follows that idP ∈ND(P,P)
iff tr(idP) = 0, which is the case iff χ(P) = 0.
□
COROLLARY 2.9. Let N ⊆D be the full subcategory of all objects which
become isomorphic to zero in the quotient category D. If Λ is algebraically
closed, then N satisﬁes the stability axiom (N1), the acyclicity axiom (N3)
and the Euler axiom (N4), and an object K ∈D lies in the subcategory N iff
all simple constituents of all pHn(K) have Euler characteristic zero.
Proof. Property (N1) is obvious, property (N3) follows from (N4), and
the latter is immediate from corollary 2.8 by the perverse decomposition
axiom (D3) and the semisimplicity axiom (D4).
□
2.5. Super Tannakian categories
Using a criterion of Deligne, we now show that the semisimple abelian
rigid symmetric monoidal category D from the previous section is almost
Tannakian: It is an inductive limit of super Tannakian categories, a notion
that we will recall below and in appendix A. In the case k = C we will
see later (in corollary 2.14, using that in this case the Euler characteristic
of perverse sheaves is non-negative) that D is in fact an inductive limit of
ordinary Tannakian categories, and this is closely related to our proof of
theorem 1.1. One may conjecture the same also for char(k) > 0.
Throughout this section we will always assume that Λ is algebraically
closed and that axioms (D1) – (D4) of section 2.3 hold. By semisimplicity
the convolution functor
∗: D×D −→D
is exact in each variable, and EndD(1) = Λ (this latter property is inherited
from D where it can be checked by applying the faithful functor rat). So D
is a cat´egorie Λ-tensorielle in the sense of [30, sect. 0.1].
Recall that a full subcategory of D is said to be ﬁnitely tensor generated
if it is the category ⟨K⟩consisting of all subquotients of convolution powers
of K ⊕K∨for some ﬁxed object K ∈D. Our next goal is to show that any
such subcategory is super Tannakian in the following sense.
The framework of algebraic geometry is generalized to super algebraic
geometry by replacing the category of commutative rings with the category
of Z/2Z-graded super commutative rings. In particular one has the notion
of an algebraic resp. reductive super group and its super representations, see
appendix A. For an algebraic super group G over Λ and a point ε ∈G(Λ)
with ε2 = 1 such that int(ε) is the parity automorphism of G, let us denote
36
Chapter 2 – Proof of the vanishing theorem(s)
by RepΛ(G,ε) the category of all super representations V = V0 ⊕V1 of G
over Λ such that ε acts by (−1)a on Va for a = 0,1. Categories of this form
will be called super Tannakian, with Tannaka super group G.
THEOREM 2.10. Any ﬁnitely generated full tensor subcategory ⟨K⟩⊂D
is super Tannakian, and its Tannaka super group G = G(K) is reductive.
Proof. Since D is a cat´egorie Λ-tensorielle, for the ﬁrst claim it sufﬁces
by [30, th. 0.6] to see that for any object K ∈D and all n ∈N the number of
simple constituents of (K ⊕K∨)∗n in the semisimple abelian category D is
at most Nn for some constant N = N(K) depending only on K. In the case
at hand one can take
N(K) = ∑
i∈Z
dimΛ(Hi(X,M))
for any object M ∈D that becomes isomorphic to K ⊕K∨in D, using the
argument given in [110, top of p. 5]. Concerning reductivity, note that a
category RepΛ(G,ε) is semisimple iff G is reductive [108].
□
