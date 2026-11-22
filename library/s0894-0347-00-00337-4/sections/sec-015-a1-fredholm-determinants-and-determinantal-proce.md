---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-015-a1-fredholm-determinants-and-determinantal-proce
section_title: "A.1. Fredholm determinants and determinantal processes"
section_number: null
pages: 28-30
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
plex Hilbert space, L(H) the algebra of bounded operators in H, and L1(H), L2(H)
the ideals of trace class and Hilbert–Schmidt operators, respectively.
Assume we are given a splitting H = H+ ⊕H−. According to this splitting,
write operators A ∈L(H) in block form, A =
A++
A+−
A−+
A−−

, where
A++ : H+ →H+,
A+−: H−→H+,
A−+ : H+ →H−,
A−−: H−→H−.
The algebra L(H) is equipped with a natural Z2-grading. Speciﬁcally, given A, its
even part Aeven and odd part Aodd are deﬁned as follows:
Aeven =
A++
0
0
A−−

,
Aodd =
 0
A+−
A−+
0

.
Denote by L1|2(H) the set of operators A ∈L(H) such that Aeven is in the trace
class L1(H) while Aodd is in the Hilbert–Schmidt class L2(H). It is readily seen
ASYMPTOTICS OF PLANCHEREL MEASURES
509
that L1|2(H) is an algebra. We endow it with the topology induced by the trace
norm on the even part and the Hilbert–Schmidt norm on the odd part.
It is well known that the determinant det(1 + A) makes sense if A ∈L1(H). It
can be characterized as the only function which is continuous in A with respect to
the trace norm ∥A∥1 = tr
√
AA∗and which coincides with the usual determinant
when A is a ﬁnite–dimensional operator. See, e.g., [33].
Proposition A.1. The function A 7→det(1 + A) admits a unique extension to
L1|2(H), which is continuous in the topology of that algebra.
Proof. For A ∈L1|2(H), set
det(1 + A) = det((1 + A)e−A) · etr Aeven.
(A.1)
As is well known (e.g., [33]),
A 7→(1 + A)e−A −1
is a continuous map from L2(H) to L1(H).
Next, A 7→tr Aeven evidently is a
continuous function on L1|2(H). Consequently, (A.1) is well deﬁned and is a con-
tinuous function on L1|2(H). When A ∈L1(H), (A.1) agrees with the conventional
deﬁnition, because then
det((1 + A)e−A) · etr Aeven = det(1 + A)e−tr A+tr Aeven = det(1 + A).
This concludes the proof.
Corollary A.2. If {Pn} is an ascending sequence of even projection operators in
H such that Pn →1 strongly, then
det(1 + A) = lim
n→∞det(1 + PnAPn).
Proof. Indeed, PnAPn approximates A in the topology of L1|2(H).
Corollary A.3. If A, B ∈L1|2(H), then
det(1 + A) det(1 + B) = det((1 + A)(1 + B)).
Proof. Indeed, this is true for ﬁnite–dimensional A, B, and then we use the conti-
nuity argument.
In our particular case, the splitting of H = ℓ2(X) will come from a splitting of
X = X+ ⊔X−into two complementary subsets as follows:
H± = ℓ2(X±) .
An operator L in H will be viewed as an inﬁnite matrix whose rows and columns
are indexed by elements of X. Given X ⊂X, we denote by LX the corresponding
ﬁnite submatrix in L.
Proposition A.4. If L ∈L1|2(H), then
X
X
det LX = det(1 + L),
(A.2)
where summation is taken over all ﬁnite subsets X ⊂X including the empty set
with the understanding that det L∅= 1.
The exact meaning of the sum in the left-hand side is explained in the proof.
510
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Proof. Given a ﬁnite subset Y ⊂X, we assign to it, in the natural way, a projection
operator PY . Note that PY is even. By elementary linear algebra, we have
X
X⊆Y
det LX = det(1 + PY LPY ).
Assume Y becomes larger and larger, so that in the limit it covers the whole X.
Then the left-hand side tends to the left-hand side of (A.2). More precisely, this is
evident if all the minors det LX are nonnegative. In general, instead of proving that
the sum in the left-hand side of (A.2) is absolutely convergent we simply deﬁne it
as
X
X
det LX = lim
{Y }
X
X⊆Y
det LX .
On the other hand, the right-hand side tends to det(1 + L) by Corollary A.2.
Remark A.5. Suppose that L =
 0
A
−A∗
0

, where A is of Hilbert–Schmidt class.
Then L ∈L1|2(H). It is readily seen that det LX ≥0 for all X, and it is worth
noting that det LX = 0 unless |X+| = |X−|. By Proposition A.4, we can deﬁne a
probability measure on ﬁnite subsets X of X by
Prob(X) =
det LX
det(1 + L) ,
X ∈Conf(X)0 .
