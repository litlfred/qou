---
doc_id: arxiv-2605.15740v1
doc_title: "BAILEY P AIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS"
section_id: sec-004-23-the-key-results
section_title: "The key results"
section_number: 2.3
pages: 10-13
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
doc_brief: "BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´ e homology"
---
(1.16), (1.24) and (1.25) to finite polynomial sums at roots of unity. We have chosen to present
these results following the order in which the Bailey pairs in Section 2.2 were introduced.
Theorem 2.7.Let(α k,βk)denote the Bailey pair in(2.16). Then forp≥1andqany primitive
Nth root of unity we have
H (6)
p (q) =
N−1X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk.(2.31)
Theorem 2.8.Let(α k,βk)denote the Bailey pair in(2.17). Then forp≥1andqany primitive
Nth root of unity we have
H (7)
p (q) =q
N−1X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk.(2.32)
Theorem 2.9.Let(α k,βk)denote the Bailey pair in(2.18). Then forp≥1andqany primitive
Nth root of unity we have
H (3)
p (q) =q−1
N−1X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk.(2.33)
Theorem 2.10.Let(α k,βk)denote the Bailey pair in(2.19). Then forp≥1andqany
primitiveNth root of unity we have
H (4)
p (q) =
N−1X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk.(2.34)
Theorem 2.11.Let(α k,βk)denote the Bailey pair in(2.20). Then forp≥1andqany
primitiveNth root of unity we have
H (8)
p (q) =−q(1−q)
N−1X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk.(2.35)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS 11
Theorem 2.12.Let(α k,βk)denote the Bailey pair in(2.21). Then forp≥1andqany
primitiveNth root of unity we have
H (1)
p (q) =−q−1(1−q)
N−1X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk.(2.36)
Theorem 2.13.Let(α k,βk)denote the Bailey pair in(2.22). Forp≥1andqany primitive
Nth root of unity we have
H (4)
p (q) =q p−1
N−1X
k=0
(−1)kq−(k+1
2 )(qp(k2+2k)αk)∗.(2.37)
Theorem 2.14.Let(α k,βk)denote the Bailey pair in(2.23). Forp≥1andqany primitive
Nth root of unity we have
H (9)
p (q) =q p
N−1X
k=0
(−1)kq−(k+1
2 )(qp(k2+2k)αk)∗.(2.38)
For the last two results we define
bαk = (1−q)
1−q k+1αk.(2.39)
Theorem 2.15.Let(α k,βk)denote the Bailey pair in(2.24). Forp≥1andqany primitive
Nth root of unity we have
−1
2 +H (2)
p (q) =q p
 N−2X
k=0
(−1)kq−(k+1
2 )+p(k2+2k)bαk + 1
2q−pbαN−1
!
. (2.40)
Theorem 2.16.Let(α k,βk)denote the Bailey pair in(2.25). Forp≥1andqany primitive
Nth root of unity we have
−1
2 +H (10)
p (q) =q p
 N−2X
k=0
(−1)kq−(k+1
2 )+p(k2+2k)bαk + 1
2q−pbαN−1
!
. (2.41)
Proof of Theorem 2.7.Let (α k,βk) denote the Bailey pair in (2.16). Using (2.3) we compute
that
βN−1−np = (q1−2N)2npq4Nnp−2n2
p−np
(q2)2N−2
.(2.42)
Inserting this into (2.7) we obtain
X
N−1≥np≥···≥n1≥0
q(N−np−1)(N−np)(q1−2N)2npq4Nnp−2n2
p−np
(q)np
p−1Y
i=1
q(N−ni−1)(N−ni)

ni+1
ni

= (q2)2N−2
(q)N−1(q2)N−1
N−1X
k=0
(q1−N)k
(q1+N)k
(−1)kqNk−(k+1
2 )+p(k2+k)αk.
(2.43)
Now we letqbe a primitiveNth root of unity. The terms (q2)2N−2
(q)N−1 (q2)N−1
and (q1−N )k
(q1+N )k
become 1,
as do all other instances ofq N. The result is (2.31).□
12 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
Proofs of Theorems 2.8–2.12.The proofs of Theorems 2.8–2.12 closely resemble the proof of
Theorem 2.7. The only difference is the initial Bailey pair (α k,βk). Therefore we limit ourselves
to noting the expression forβ N−1−np in each case. For the Bailey pairs in (2.17)–(2.21), we
have, respectively,
βN−1−np = (q1−2N)2npq4Nnp−2n2
p−2np+N−1
(q2)2N−2
,(2.44)
βN−1−np = (q1−2N)2npq4Nnp−2n2
p−np+(N−np−1)2
(q2)2N−2
,(2.45)
βN−1−np = (q1−2N)2npq4Nnp−2n2
p−np+(N−np−1)2+(N−np−1)
(q2)2N−2
,(2.46)
βN−1−np = (q2−2N)2npq4Nnp−2n2
p−3np
(q)2N−2
(2.47)
and
βN−1−np = (q2−2N)2npq4Nnp−2n2
p−3np+(N−1−np)2−(N−1−np)
(q)2N−2
.(2.48)
Using these in (2.3) and calculating as in the proof of Theorem 2.7 we obtain (2.32)–(2.36).□
The proofs of Theorems 2.13 and 2.14 are similar, the only difference being the use of Propo-
sition 2.4 instead of Proposition 2.3.
Proofs of Theorems 2.13–2.14.Let (α k,βk) denote the Bailey pair in (2.22). Note that theβ k
is the same as in (2.18), and soβ N−1−np is given by (2.45). Using this in (2.12) we have
X
N−1≥np≥···≥n1≥0
q(N−np)2−1(q1−2N)2npq4Nnp−2n2
p−np+(N−np−1)2
(q)np
p−1Y
i=1
q(N−ni−1)(N−ni+1)

ni+1
ni

= (q2)2N−2
(q)N−1(q2)N−1
N−1X
k=0
(q1−N)k
(q1+N)k
(−1)kqNk−(k+1
2 )(qp(k2+2k)αk)∗.
(2.49)
Lettingqbe a primitiveNth root of unity gives (2.37). Theorem 2.14 follows in the same way
using the Bailey pair in (2.23).□
Proofs of Theorems 2.15–2.16.For Theorem 2.15 we use (2.24) in Proposition 2.5 to obtain
X
N−1≥np≥···≥n1≥0
q(N−np−1)(N−np+1)q2Nnp−n2
p+N 2−N(q1−2N)2np
(1 +qN−np)(q)np
p−1Y
i=1
q(N−ni−1)(N−ni+1)

ni+1
ni

= (q)2N−1
(q)N−1(q)N
N−1X
k=0
(q1−N)k
(q2+N)k
(−1)kqNk−(k+1
2 )+p(k2+2k)αk.
(2.50)
Lettingqbe a primitiveNth root of unity the left-hand side of (2.50) becomes
q−p X
np≥···≥n1≥0
qnp(qnp+1)np
(1 +qnp)
p−1Y
i=1
qn2
i

ni+1
ni

.(2.51)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS 13
Note that
(qnp+1)np
(1 +qnp) =



(qnp)np ifn p>0
1
2 ifn p = 0
(2.52)
and so (2.51) whenqis a primitiveNth root of unity is
q−p

−1
2 +
X
np≥···≥n1≥0
qnp(qnp)np
p−1Y
i=1
qn2
i

ni+1
ni

.(2.53)
Now lettingqbe a primitiveNth root of unity on the right-hand side of (2.50), the prefactor
becomes 1 as usual. As for the term (q1−N )k
(q2+N )k
, it does not become 1 as before. But when multiplied
by (1−q k+1)/(1−q), it becomes 1 fork <N−1 while fork=N−1 it is (1−qN )
(1−q2N )→ 1
2. This
observation accounts for the use ofbα k and the splitting of the sum on the right-hand side of
(2.40). Here, we also use thatq −(N
2)+pN 2
= (−1)N+1. This gives Theorem 2.15. Theorem 2.16
follows in the same way using (2.25) in Proposition 2.5.□
