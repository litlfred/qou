---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-015-42-stability-implies-negative-association
section_title: "Stability implies negative association"
section_number: 4.2
pages: 24-25
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
of the following theorem goes back to Feder-Mihail [29], although the proof of the
full theorem is scattered over the literature [24, 57, 58, 72].
Theorem 4.8. Let S be a class of probability measures satisfying:
(1) Each µ ∈S is a measure on 2E, where E is a ﬁnite subset of {1, 2, . . .}
depending on µ.
(2) S is closed under conditioning.
(3) For each µ ∈S the variables Xe, e ∈E, are pairwise negatively correlated.
(4) Each µ ∈S has a homogeneous generating polynomial.
Then all measures in S are CNA (conditionally negatively associated).
The homogeneity condition in (4) above is essential and ensures the existence of
a variable of so-called “positive inﬂuence” [24] (various notions of “inﬂuence” have
been studied by Bourgain et al. in [14]).
A sketch of the proof of Theorem 4.8 is as follows. Recall from §2.1 the deﬁni-
tion of an increasing event. Since any increasing function depending on a set E0
can be written as a positive linear combination of characteristic functions, χA, of
increasing events A depending on E0, it is enough to prove the theorem for such
characteristic functions. The proof of negative association in the case when F = χA
and G = Xe in Deﬁnition 2.7 are such that A does not depend on e is recovered
from Feder-Mihail’s proof [29, 58]. The general case – when F = χA1 and G = χA2
in Deﬁnition 2.7 are such that A1 and A2 depend on disjoint sets of variables –
then follows from the proof of [57, Theorem 6.5].
Using Theorem 4.8 we can establish the following result.
Theorem 4.9. If µ ∈Pn is strongly Rayleigh, then it is CNA+.
Proof. Let S be the class of all probability measures µ such that
• each µ ∈S is a measure on 2E, where E is a ﬁnite subset of {1, 2, . . .}
depending on µ, and
• µ has a stable homogeneous generating polynomial.
Since stable homogeneous polynomials are pairwise negatively correlated and are
also closed under conditioning (cf. §2.1), the class S satisﬁes all the hypotheses
required in Theorem 4.8. Therefore, all the measures in S are negatively associated.
Further, let %S be the class of all probability measures µ such that
• each µ ∈%S is a measure on 2E, where E is a ﬁnite subset of {1, 2, . . .}
depending on µ, and
• µ has a stable generating polynomial.
Now by Theorem 4.2 every measure in %S is the projection of a measure in S. Since
negative association is closed under projections and the strongly Rayleigh property
is closed under conditioning and external ﬁelds, the theorem follows.
□
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
545
Note that since the Rayleigh/h-NLC+ property is also closed under conditioning,
projections, and external ﬁelds, Theorem 4.8 and slight modiﬁcations of the above
arguments actually yield the following stronger version of Theorem 4.9.
Theorem 4.10. If µ ∈Pn is PHR, then it is CNA+.
Since homogeneous Rayleigh polynomials need not be stable, strongly Rayleigh
⇒PHR strictly. As we will see in §7, one also has PHR ⇒CNA+ strictly.
