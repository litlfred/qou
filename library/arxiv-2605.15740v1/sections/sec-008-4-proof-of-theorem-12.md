---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-008-4-proof-of-theorem-12
section_title: "Proof of Theorem 1.2"
section_number: 4
pages: 21-25
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
We are now in a position to prove Theorem 1.2. Again, we follow the order in which the
Bailey pairs were introduced in Section 2.2.
Proof. We begin with the proof of (1.32). By Proposition 3.3, (1.32) is equivalent to
−1
2
6(6p+1)N
X
n=0
χ(n)

1 −
n
6(6p + 1)N

ζ
M n2−(6p−1)2
24(6p+1)
N
= H(6)
p (ζM
N )
(4.1)
where χ = χ(1,1,2p)
(2,3,6p+1) is the odd periodic function given by
χ(n) =





1
if n ≡42p + 5, 54p + 7, 54p + 11, 66p + 13
(mod 72p + 12),
−1
if n ≡6p −1, 18p + 1, 18p + 5, 30p + 7
(mod 72p + 12),
0
otherwise.
(4.2)
By Theorem 2.7,
H(6)
p (q) =
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk
(4.3)
where q = ζM
N and (αk, βk) is the Bailey pair in (2.16). Next, we claim that
4
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk = −
6(6p+1)N
X
n=0
χ(n)q
n2−(6p−1)2
24(6p+1)
(4.4)
when q = ζM
N . To deduce (4.4), we first demonstrate that (as polynomials in q)
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk = −
2(6p+1)N
X
n=0
χ(n)q
n2−(6p−1)2
24(6p+1) .
(4.5)
We proceed by induction on N. The induction step consists of verifying the identity
(−1)Nq(N+1
2 )+(p−1)(N2+N)αN = −
12p+1
X
n=0
χ((12p + 2)(N + 1) −n)q
((12p+2)(N+1)−n)2−(6p−1)2
24(6p+1)
. (4.6)
We consider three cases. First suppose that N = 3r. If r is even, then
χ((12p + 2)(N + 1) −n) = χ(12p + 2 −n)
and so the right-hand side of (4.6) is
−
12p+1
X
n=0
χ(12p + 2 −n)q
((12p+2)(N+1)−n)2−(6p−1)2
24(6p+1)
= −χ(6p −1)q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
= q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
(4.7)
by (4.2). Similarly, if r is odd, then we have
χ((12p + 2)(N + 1) −n) = χ((12p + 2)(N + 3) −24p −4 −n) = −χ(n + 24p + 4),
22
JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
and so the right-hand side of (4.6) is
12p+1
X
n=0
χ(n + 24p + 4)q
((12p+2)(N+1)−n)2−(6p−1)2
24(6p+1)
= χ(30p + 7)q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
= −q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
(4.8)
by (4.2). In both (4.7) and (4.8), one can check using (2.16) that the signs and powers of q on
both sides of (4.6) match. Next suppose that N = 3r + 1. If r is even, then
χ((12p + 2)(N + 1) −n) = χ(24p + 4 −n)
and so the right-hand side of (4.6) is
−
12p+1
X
n=0
χ(24p + 4 −n)q
((12p+2)(N+1)−n)2−(6p−1)2
24(6p+1)
= −χ(18p + 1)q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
−χ(18p + 5)q
((12p+2)(N+1)−(6p−1))2−(6p−1)2
24(6p+1)
= q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
+ q
((12p+2)(N+1)−(6p−1))2−(6p−1)2
24(6p+1)
(4.9)
by (4.2). Similarly, if r is odd, then we have
χ((12p + 2)(N + 1) −n) = χ((12p + 2)(N + 2) −12p −2 −n) = −χ(n + 12p + 2),
and so the right-hand side of (4.6) is
12p+1
X
n=0
χ(n + 12p + 2)q
((12p+2)(N+1)−n)2−(6p−1)2
24(6p+1)
= χ(18p + 5)q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
+ χ(18p + 1)q
((12p+2)(N+1)−(6p−1))2−(6p−1)2
24(6p+1)
= −q
((12p+2)(N+1)−(6p+3))2−(6p−1)2
24(6p+1)
−q
((12p+2)(N+1)−(6p−1))2−(6p−1)2
24(6p+1)
(4.10)
by (4.2). In both (4.9) and (4.10), one can check using (2.16) that the signs and powers of q on
both sides of (4.6) match. As the argument is similar for N = 3r −1, we omit the details.
Now, by (4.5), it suffices to prove
6(6p+1)N
X
n=0
χ(n)q
n2−(6p−1)2
24(6p+1)
= 4
2(6p+1)N
X
n=0
χ(n)q
n2−(6p−1)2
24(6p+1)
(4.11)
when q = ζM
N . This follows by taking p3 = 6p + 1 and multiplying both sides of (3.26) by
q−(6p−1)2
24(6p+1) in Corollary 3.6. Thus, (4.5) with q = ζM
N and (4.11) imply (4.4). By Lemma 3.1, we
have
6(6p+1)N
X
n=0
χ(n)q
n2−(6p−1)2
24(6p+1)
= 2q−(6p−1)2
24(6p+1)
6(6p+1)N
X
n=0
χ(n)

1 −
n
6(6p + 1)N

q
n2
24(6p+1)
(4.12)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS 23
where q = ζM
N . Combining (4.3), (4.4) and (4.12), we arrive at
2
6(6p+1)N
X
n=0
χ(n)

1 −
n
6(6p + 1)N

ζ
M n2−(6p−1)2
24(6p+1)
N
= −4H(6)
p (ζM
N ).
(4.13)
Multiplying both sides of (4.13) by −1
4 yields (4.1). Thus, (1.32) follows.
As the proofs for (1.26)–(1.31) and (1.33)–(1.36) are similar to that of (1.32), we sketch the
details.
One first uses Proposition 3.3 to express the limiting value of the relevant Eichler
integral as a finite sum (as in the left-hand side of (4.1)). Next, by Theorems 2.8–2.16, we can
express each of the left-hand sides of (1.26)–(1.31) and (1.33)–(1.36) as a finite sum involving
αk, (qp(k2+2k)αk)∗or bαk (analogous to (4.3)). One then proves an underlying identity between
polynomials in q akin to (4.5). Here we list these identities as significant care is required in some
cases. As for (4.5), the proofs proceed by induction on N. For (1.33), the identity is
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk = −
2(6p+1)N
X
n=0
χ(n)q
n2−(6p+5)2
24(6p+1)
(4.14)
where (αk, βk) is the Bailey pair (2.17) and χ = χ(1,1,2p+1)
(2,3,6p+1). For (1.29), it is
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk = −
2(6p−1)N
X
n=0
χ(n)q
n2−(6p−5)2
24(6p−1)
(4.15)
where (αk, βk) is the Bailey pair (2.18) and χ = χ(1,1,2p−1)
(2,3,6p−1). For (1.30), it is
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk = −
2(6p−1)N
X
n=0
χ(n)q
n2−(6p+1)2
24(6p−1)
(4.16)
where (αk, βk) is the Bailey pair (2.19) and χ = χ(1,1,2p)
(2,3,6p−1). For (1.34), it is
(1 −q)
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk =
2(6p+1)N
X
n=0
χ(n)q
n2−(6p−5)2
24(6p+1)
(4.17)
where (αk, βk) is the Bailey pair (2.20) and χ = χ(1,1,1)
(2,3,6p+1). For (1.26), it is
q−1(1 −q)
N−1
X
k=0
(−1)kq(k+1
2 )+(p−1)(k2+k)αk =
2(6p−1)N
X
n=0
χ(n)q
n2−(6p+5)2
24(6p−1)
(4.18)
for p ≥2 and
q−1(1 −q)
N−1
X
k=0
(−1)kq(k+1
2 )αk =
10N
X
n=0
χ(n)q
n2−112
120
−q−1λN
(4.19)
where
λN = λN(q) := −2 +







(−1)rq
15r2+r
2
+ (−1)rq
15r2−r
2
if N = 3r,
(−1)rq
15r2+11r+2
2
if N = 3r + 1,
(−1)r+1q
15r2+19r+6
2
if N = 3r + 2
24
JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
for p = 1. Here, (αk, βk) is the Bailey pair (2.21) and χ = χ(1,1,1)
(2,3,6p−1). One can check that if
q = ζM
N , then λN = λN(ζM
N ) = −1. For (1.31), it is
N−1
X
k=0
(−1)kq−(k+1
2 )(qp(k2+2k)αk)∗= −
2(6p−1)N
X
n=0
χ(n)q
n2−(12p−5)2
24(6p−1)
(4.20)
where (αk, βk) is the Bailey pair (2.22) and χ = χ(1,1,3p−1)
(2,3,6p−1). For (1.35), it is
N−1
X
k=0
(−1)kq−(k+1
2 )(qp(k2+2k)αk)∗= −
2(6p+1)N
X
n=0
χ(n)q
n2−(12p−1)2
24(6p+1)
(4.21)
where (αk, βk) is the Bailey pair (2.23) and χ = χ(1,1,3p)
(2,3,6p+1). For (1.28), it is
N−1
X
k=0
(−1)kq−(k+1
2 )+p(k+1)2 bαk + 1 + 1
2(−1)Nq−(N
2)+pN2(bαN−1 −γN−1)
= −
2(6p−1)N
X
n=0
χ(n)q
n2−1
24(6p−1)
(4.22)
where (αk, βk) is the Bailey pair (2.24),
γk = γk(q) :=





q3r2−2r + q3r2−r
if k = 3r −1,
−q3r2+r
if k = 3r,
−q3r2+2r
if k = 3r + 1
and χ = χ(1,1,p)
(2,3,6p−1). Again, one can confirm that if q = ζM
N , then γN−1 = γN−1(ζM
N ) = −1 and
(−1)Nq−(N
2)+pN2 = −1. Finally, for (1.36), it is
N−2
X
k=0
(−1)kq−(k+1
2 )+p(k+1)2 bαk −1
2(−1)Nq−(N
2)+pN2 bαN−1 −1 −1
2(−1)NqpN2κN
= −
2(6p+1)N
X
n=0
χ(n)q
n2−1
24(6p+1)
(4.23)
where (αk, βk) is the Bailey pair (2.25),
κN = κN(q) :=







−q
r(3r−1)
2
−q
r(3r+1)
2
if N = 3r,
q
r(3r+1)
2
if N = 3r + 1,
q
(r+1)(3r+2)
2
if N = 3r + 2
and χ = χ(1,1,p)
(2,3,6p+1). In this case, if q = ζM
N , then κN = κN(ζM
N ) = (−1)N+1. We now take q = ζM
N
in each of (4.14)–(4.23), simplify and then combine with statements similar to (4.11) (resulting
from Corollary 3.5) to establish versions of (4.4). After applying Lemma 3.1 (to obtain variants
of (4.12)), the results follow by combining steps and multiplying by an appropriate factor. In
total, this yields (1.26)–(1.31) and (1.33)–(1.36).
□
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS 25
