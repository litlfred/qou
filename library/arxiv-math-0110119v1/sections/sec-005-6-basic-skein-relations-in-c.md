---
doc_id: arxiv-math-0110119v1
doc_title: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus"
section_id: sec-005-6-basic-skein-relations-in-c
section_title: "Basic skein relations in C′"
section_number: 6
pages: 8-11
source_pdf: 0110119v1.pdf
source_sha256: 4904a86e8a340f59
toc_source: inferred
doc_brief: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus — The Hecke algebra Hn contains well known idempotents Eλ which are indexed by Young diagrams with n cells."
---
Basic skein relations in C′
We recall that the quasi-idempotent ai ∈Ri
i satisﬁes aiai = αiai for a non-zero
scalar αi. We deﬁne hi =
1
αi∆(ai) ∈Ci and h′
i =
1
αi∆′(ai) ∈C′i for any integer
i ≥0. We deﬁne hi = 0 and h′
i = 0 for any integer i < 0.
8
[i+1]
αi+1
ai+1
=
1
αi
ai
+ s−1[i]
αi
ai
Figure 10: Depiction of lemma 6.1.
The following lemma is a direct consequence of the decomposition
ai+1 = (ai ⊗11)(1i+1 + sσi + s2σiσi−1 + · · · + siσiσi−1 · · · σ1)
of the quasi-idempotent ai+1 ∈Ri+1
i+1 (see [10], [7] for a proof). The lemma is
depicted in ﬁgure 10.
Lemma 6.1 We have
[i + 1]h′
i+1 = ehi + s−1[i]h′
ia
in C′+ for any integer i ≥0.
We deﬁne
ti = hie −ehi ∈C′
+
for any integer i. We remark that ti = 0 for i ≤0.
Lemma 6.2 We have
ti = (s−i −si)h′
ia
for any integer i ≥0.
Proof We have
[i + 1]h′
i+1 = ehi + s−1[i]h′
ia
by lemma 6.1 for any integer i. By applying the map ρ from section 1 we get
[i + 1]h′
i+1 = hie + s[i]h′
ia
because hi, h′
i and h′
i+1 are invariant under ρ by lemma 3.2. These two equations
imply that ti = hie −ehi = (s−i −si)h′
ia.
⋄
9
ai
= v ·
ai
=
vs1−i·
ai
Figure 11: The closure of ∆′(ai)a.
Corollary 6.3 We have
ˆti = (s1−2i −s)vhi
for any integer i.
Proof From lemma 6.2 and the skein relation in ﬁgure 11 we deduce that
ˆti
=
(s−i −si)vs1−ihi
=
(s1−2i −s)vhi
for any integer i ≥0. This equation holds for negative integers i as well because
hi and ti are equal to zero for negative i.
⋄
Lemma 6.4 We have

ti
ti+1
tj
tj+1

 = (s2 −1)

ehi
ti+1
ehj
tj+1

in C′ for any integers i and j.
Proof If either i or j is negative then the lemma is obviously true because tk = 0
for k ≤0. Let i ≥0 and j ≥0 from now on. The combination of lemmas 6.1 and
6.2 implies that
[i + 1]h′
i+1 = ehi +
1
1 −s2ti.
We have (s−1 −s)[j + 1]h′
j+1a = tj+1 by lemma 6.2. Multiplication of the above
equation by these terms gives
(s−1 −s)[i + 1][j + 1]h′
i+1h′
j+1a = (ehi)tj+1 +
1
1 −s2titj+1.
10
The left hand side of the above equation is invariant under the interchange of i
and j because C′ is commutative, and thus the right hand side is invariant under
this interchange. Hence,
(ehi)tj+1 +
1
1 −s2titj+1 = (ehj)ti+1 +
1
1 −s2tjti+1
which is equivalent to our claim.
⋄
Lemma 6.4 is the stepping stone from skein calculations to the following algebraic
calculations.
