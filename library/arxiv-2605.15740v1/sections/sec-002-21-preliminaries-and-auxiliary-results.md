---
doc_id: arxiv-2605.15740v1
doc_title: "BAILEY P AIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS"
section_id: sec-002-21-preliminaries-and-auxiliary-results
section_title: "Preliminaries and auxiliary results"
section_number: 2.1
pages: 6-8
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
doc_brief: "BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´ e homology"
---
sequences (αn,βn)n≥0 satisfying
βn =
nX
k=0
αk
(q)n−k(aq)n+k
(2.1)
= 1
(q)n(aq)n
nX
k=0
(q−n)k
(aqn+1)k
(−1)kqnk−(k
2)αk.(2.2)
The first equation is the original definition [4], while the second follows from an application of
the identity [13, Appendix I, Eq. (I.10)]
(x)n−k = (x)n
(q1−n/x)k
(−q/x)kq(k
2)−nk.(2.3)
We begin by reviewing two important facts about Bailey pairs. First, we require a special
case of the Bailey lemma [4].
Lemma 2.1.If(α n,βn)is a Bailey pair relative toa, then so is(α ′
n,β′
n), where
α′
n =a nqn2
αn (2.4)
and
β′
n =
nX
j=0
ajqj2
(q)n−j
βj.(2.5)
Second, we have a special case of the Bailey lattice [1].
Lemma 2.2.If(α n,βn)is a Bailey pair relative toq 2, then(α ∗
n,βn)is a Bailey pair relative to
q, where
α∗
n = (1−q 2)
 αn
1−q 2n+2− q2nαn−1
1−q 2n

.(2.6)
By convention we takeα −1 = 0.
Using Lemmas 2.1 and 2.2, we establish three auxiliary results which will allow us to relate
theq-multisums in Theorem 1.2 to polynomial sums at roots of unity. The first result is for
Bailey pairs relative toq.
Proposition 2.3.If(α k,βk)is a Bailey pair relative toq, then for anyp≥1we have
X
n−1≥np≥···≥n1≥0
q(n−np−1)(n−np)βn−np−1
(q)np
p−1Y
i=1
q(n−ni−1)(n−ni)

ni+1
ni

= 1
(q)n−1(q2)n−1
n−1X
k=0
(q1−n)k
(q1+n)k
(−1)kqnk−(k+1
2 )+p(k2+k)αk.
(2.7)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS 7
Proof.Suppose that (α k,βk) is a Bailey pair relative toq. Iterating (2.4) and (2.5)ptimes we
obtain another Bailey pair relative toq,
α(p)
k =q p(k2+k)αk (2.8)
and
β(p)
k =
X
k≥np≥···≥n1≥0
qnp(np+1)+···+n1(n1+1)
(q)k−np···(q) n2−n1
βn1.(2.9)
Now inβ (p)
k we replacekbyn−1 and then make the change of indicesn i→n−1−n p−i+1 for
1≤i≤p. The result is
β(p)
n−1 =
X
n−1≥np≥···≥n1≥0
q(n−n1−1)(n−n1)+···+(n−np−1)(n−np)
(q)n1(q)n2−n1···(q) np−np−1
βn−np−1.(2.10)
Multiplying numerator and denominator by (q)np and then converting toq-binomial coefficients
(1.8) gives the left-hand side of (2.7). The right-hand side follows from inserting (2.8) into (2.2).
This completes the proof.□
Our second auxiliary result is analogous to Proposition 2.3, but for Bailey pairs relative to
q2. In what follows, we definea ∗
n for any sequencea n by
a∗
n = (1−q 2)
 an
1−q 2n+2− q2nan−1
1−q 2n

(2.11)
in analogy with (2.6).
Proposition 2.4.If(α k,βk)is a Bailey pair relative toq 2, then for anyp≥1we have
X
n−1≥np≥···≥n1≥0
q(n−np−1)(n−np+1)βn−np−1
(q)np
p−1Y
i=1
q(n−ni−1)(n−ni+1)

ni+1
ni

= 1
(q)n−1(q2)n−1
n−1X
k=0
(q1−n)k
(q1+n)k
(−1)kqnk−(k+1
2 )(qp(k2+2k)αk)∗.
(2.12)
Proof.Suppose that (α k,βk) is a Bailey pair relative toq 2. We argue as in Proposition 2.3 with
the same iterations of (2.4) and (2.5) (but witha=q 2) and the same changes of indices. The
result is a Bailey pair relative toq 2,
α(p)
k =q p(k2+2k)αk (2.13)
and
β(p)
n−1 =
X
n−1≥np≥···≥n1≥0
q(n−n1−1)(n−n1+1)+···+(n−np−1)(n−np+1)
(q)n1(q)n2−n1···(q) np−np−1
βn−np+1.(2.14)
Now we change this to a Bailey pair relative toqusing Lemma 2.2 and then insert it into (2.2)
to complete the proof.□
The third auxiliary result also applies to Bailey pairs relative toq 2, but in a different way.
8 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
Proposition 2.5.If(α k,βk)is a Bailey pair relative toq 2, then for anyp≥1we have
X
n−1≥np≥···≥n1≥0
q(n−np−1)(n−np+1)βn−np−1
(q)np
p−1Y
i=1
q(n−ni−1)(n−ni+1)

ni+1
ni

= (1−q 2)
(q)n−1(q)n
n−1X
k=0
(q1−n)k
(q2+n)k
(−1)kqnk−(k+1
2 )+p(k2+2k)αk.
(2.15)
Proof.This follows from substituting (2.13) and (2.14) into the definition of a Bailey pair in
(2.2) witha=q 2. □
