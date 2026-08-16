---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-031-25-super-tannakian-categories-35
section_title: "Super Tannakian categories 35"
section_number: 2.5
pages: 43-44
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
henceEndP(P) is a skew ﬁeld or zero, andP is simple or zero inP. Over
an algebraically closed ﬁeldΛ there exist no skew ﬁelds other thanΛ itself,
hence in this case we haveEndP(P) = Λ, and it follows thatidP∈ ND(P,P)
ifftr(idP) =0, which is the case iffχ(P) =0. □
COROLLARY2.9. LetN⊆Dbe the full subcategory of all objects which
become isomorphic to zero in the quotient categoryD. If Λ is algebraically
closed, thenN satisﬁes the stability axiom (N1), the acyclicity axiom (N3)
and the Euler axiom (N4), and an object K∈ D lies in the subcategoryN iff
all simple constituents of allpHn(K) have Euler characteristic zero.
Proof.Property (N1) is obvious, property (N3) follows from (N4), and
the latter is immediate from corollary 2.8 by the perverse decomposition
axiom (D3) and the semisimplicity axiom (D4). □
2.5. Super Tannakian categories
Using a criterion of Deligne, we now show that the semisimple abelian
rigid symmetric monoidal categoryD from the previous section is almost
Tannakian: It is an inductive limit of super Tannakian categories, a notion
that we will recall below and in appendix A. In the casek = C we will
see later (in corollary 2.14, using that in this case the Euler characteristic
of perverse sheaves is non-negative) thatD is in fact an inductive limit of
ordinary Tannakian categories, and this is closely related to our proof of
theorem 1.1. One may conjecture the same also forchar(k) > 0.
Throughout this section we will always assume thatΛ is algebraically
closed and that axioms (D1) – (D4) of section 2.3 hold. By semisimplicity
the convolution functor
∗ : D×D−→D
is exact in each variable, andEndD(1) = Λ (this latter property is inherited
fromD where it can be checked by applying the faithful functorrat). So D
is acat´egorieΛ-tensoriellein the sense of [30, sect. 0.1].
Recall that a full subcategory ofD is said to be ﬁnitely tensor generated
if it is the category⟨K⟩ consisting of all subquotients of convolution powers
of K⊕K∨ for some ﬁxed objectK∈ D. Our next goal is to show that any
such subcategory is super Tannakian in the following sense.
The framework of algebraic geometry is generalized to super algebraic
geometry by replacing the category of commutative rings with the category
of Z/2Z-graded super commutative rings. In particular one has the notion
of an algebraic resp. reductive super group and its super representations, see
appendix A. For an algebraic super groupG overΛ and a pointε∈ G(Λ)
with ε2 = 1 such that int(ε) is the parity automorphism ofG, let us denote
36 Chapter 2 – Proof of the vanishing theorem(s)
by RepΛ(G,ε) the category of all super representationsV = V0⊕V1 of G
overΛ such thatε acts by(−1)a onVa for a = 0,1. Categories of this form
will be called super Tannakian, with Tannaka super groupG.
THEOREM 2.10. Any ﬁnitely generated full tensor subcategory⟨K⟩⊂ D
is super Tannakian, and its Tannaka super group G= G(K) is reductive.
Proof.SinceD is a cat´egorieΛ-tensorielle, for the ﬁrst claim it sufﬁces
by [30, th. 0.6] to see that for any objectK∈ D and alln∈ N the number of
simple constituents of(K⊕K∨)∗n in the semisimple abelian categoryD is
at mostNn for some constantN = N(K) depending only onK. In the case
at hand one can take
N(K) = ∑
i∈Z
dimΛ(Hi(X,M))
for any objectM∈ D that becomes isomorphic toK⊕K∨ in D, using the
argument given in [110, top of p. 5]. Concerning reductivity, note that a
categoryRepΛ(G,ε) is semisimple iffG is reductive [108]. □
