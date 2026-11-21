---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-007-32-relations-between-incomplete-quadratic-gauss
section_title: "Relations between incomplete quadratic Gauss sums"
section_number: 3.2
pages: 14-21
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
(p1, p2, p3) of pairwise coprime positive integers and ℓ= (ℓ1, ℓ2, ℓ3) ∈Z3 satisfying 0 < ℓj < pj,
we define m(ϵ) ∈{0, . . . , 2P −1} such that
m(ϵ) ≡P

1 +
3
X
j=1
ϵjℓj
pj


(mod 2P).
(3.2)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS 15
Note that m(ϵ)2 (mod 2P) is independent of ϵ ∈{±1}3. We write
T = T(q) = −
X
ϵ∈{±1}3
ϵ1ϵ2ϵ3 Tϵ,
S = S(q) = −
X
ϵ∈{±1}3
ϵ1ϵ2ϵ3 Sϵ
where
Tϵ = Tϵ(q) :=
X
n≡m(ϵ) mod 2P
0≤n≤2p3N
q
n2
4P ,
Sϵ = Sϵ(q) :=
X
n≡m(ϵ) mod 2P
2p3N<n≤4p3N
q
n2
4P .
If we write n = k2P + m(ϵ) for some positive integer k, then
Tϵ =
j 2p3N−m(ϵ)
2P
k
X
k=0
qPk2+m(ϵ)k+ m(ϵ)2
4P ,
Sϵ =
j 4p3N−m(ϵ)
2P
k
X
k=
l 2p3N−m(ϵ)
2P
m qPk2+m(ϵ)k+ m(ϵ)2
4P
(3.3)
and so Tϵ, Sϵ ∈q
m(ϵ)2
4P Z[q]. The sums (3.3) satisfy the following relations when evaluated at a
root of unity.
Proposition 3.4. Let p = (2, 3, p3) with (6, p3) = 1, ℓ= (1, 1, ℓ3) ∈Z3 satisfy 0 < ℓ3 < p3
and ϵ := (ϵ1, ϵ2, ϵ3), ϵ′ := (ϵ′
1, ϵ′
2, ϵ′
3) ∈{±1}3. If M and N are coprime positive integers and
q = e
2πiM
N , then the following are true:
(i) If ϵ1+ϵ′
1
2
≡N (mod 2), ϵ2+ϵ′
2 ≡N (mod 3) and ϵ′
3 = −ϵ3, then m(ϵ)+m(ϵ′)
2P
≡N
6 (mod 1)
and
Tϵ = e
πi(p3N−m(ϵ′))M
3
Tϵ′.
(ii) If ϵ1−ϵ′
1
2
≡N (mod 2), ϵ2 −ϵ′
2 ≡N (mod 3) and ϵ′
3 = ϵ3, then m(ϵ)−m(ϵ′)
2P
≡N
6 (mod 1)
and
Sϵ = e
πi(p3N+m(ϵ′))M
3
Tϵ′.
(iii) If ϵ1+ϵ′
1
2
≡0 (mod 2), ϵ2+ϵ′
2 ≡2N (mod 3) and ϵ3 = −ϵ′
3, then m(ϵ)+m(ϵ′)
2P
≡N
3 (mod 1)
and
Sϵ = e
2πi(2p3N−m(ϵ′))M
3
Tϵ′.
(iv) If ϵ1+ϵ′
1
2
≡N (mod 2), ϵ2 + ϵ′
2 ≡0 (mod 3) and ϵ3 = −ϵ′
3, then m(ϵ)+m(ϵ′)
2P
≡N
2 (mod 1)
and
Sϵ = eπi(p3N−m(ϵ′))MSϵ′.
Proof. We begin with (i). By (3.2) and simplifying, we have
m(ϵ) + m(ϵ′) ≡3p3(ϵ1 + ϵ′
1) + 2p3(ϵ2 + ϵ′
2) + 6ℓ3(ϵ3 + ϵ′
3)
(mod 2P).
(3.4)
The conditions on ϵ and ϵ′ combined with (3.4) now imply that
m(ϵ) + m(ϵ′)
2P
≡N
6
(mod 1).
(3.5)
Since m(ϵ), m(ϵ′) ∈[0, 2P), it follows that m(ϵ)
2P , m(ϵ′)
2P
∈[0, 1). By (3.5), we have
N
6 −m(ϵ)
2P
−
N
6 −m(ϵ)
2P

= m(ϵ′)
2P
(3.6)
16
JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
and so rearranging terms and applying the floor function yields
N
6 −m(ϵ)
2P

=
N
6 −m(ϵ′)
2P

.
(3.7)
From (3.3), we compute
Tϵ =
j
N
6 −m(ϵ)
2P
k
X
k=0
qPk2+m(ϵ)k+ m(ϵ)2
4P
=
j
N
6 −m(ϵ)
2P
k
X
k=0
qP
j
N
6 −m(ϵ)
2P
k
−k
2
+m(ϵ)
j
N
6 −m(ϵ)
2P
k
−k

+ m(ϵ)2
4P
= qP
j
N
6 −m(ϵ)
2P
k2
+m(ϵ)
j
N
6 −m(ϵ)
2P
k
+ m(ϵ)2−m(ϵ′)2
4P
×
j
N
6 −m(ϵ)
2P
k
X
k=0
qk2−

2P
j
N
6 −m(ϵ)
2P
k
+m(ϵ)

k+ m(ϵ′)2
4P
= q
N(p3N−m(ϵ′))
6
j
N
6 −m(ϵ′)
2P
k
X
k=0
qk2+m(ϵ′)k+ P Nk
3
+ m(ϵ′)2
4P
(3.8)
where we have applied the substitution k 7→
j
N
6 −m(ϵ)
2P
k
−k and used (3.6) and (3.7). Letting
q = e
2πiM
N
in (3.8) and simplifying yields the result.
For (ii), a computation similar to that of (3.4) and the conditions on ϵ and ϵ′ imply
m(ϵ) −m(ϵ′)
2P
≡N
6
(mod 1).
(3.9)
By (3.9), we have
N
6 −m(ϵ)
2P
−
N
6 −m(ϵ)
2P

= −m(ϵ′)
2P
+ 1
(3.10)
and so again rearranging terms and applying the floor function leads to
N
3 −m(ϵ)
2P

−
N
6 −m(ϵ)
2P

=
N
6 −m(ϵ′)
2P

+ 1.
(3.11)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS 17
From (3.3), we compute
Sϵ =
j
N
3 −m(ϵ)
2P
k
X
k=
j
N
6 −m(ϵ)
2P
k
+1
qPk2+m(ϵ)k+ m(ϵ)2
4P
=
j
N
3 −m(ϵ)
2P
k
−
j
N
6 −m(ϵ)
2P
k
−1
X
k=0
qP
j
N
6 −m(ϵ)
2P
k
+1+k
2
+m(ϵ)
j
N
6 −m(ϵ)
2P
k
+1+k

+ m(ϵ)2
4P
= qP
j
N
6 −m(ϵ)
2P
k
+1
2
+m(ϵ)
j
N
6 −m(ϵ)
2P
k
+1

+ m(ϵ)2
4P
×
j
N
3 −m(ϵ)
2P
k
−
j
N
6 −m(ϵ)
2P
k
−1
X
k=0
qPk2+

m(ϵ)+2P
j
N
6 −m(ϵ)
2P
k
+2P

k+ m(ϵ′)2
4P
= q
N(p3N+m(ϵ′))
6
j
N
6 −m(ϵ′)
2P
k
X
k=0
qPk2+m(ϵ′)k+ P Nk
3
+ m(ϵ′)2
4P
(3.12)
where we have applied the substitution k 7→
j
N
6 −m(ϵ)
2P
k
+ 1 + k and used (3.10) and (3.11).
Letting q = e
2πiM
N
in (3.12) and simplifying yields the result.
For (iii), a computation similar to that of (3.4) and the conditions on ϵ and ϵ′ imply
m(ϵ) + m(ϵ′)
2P
≡N
3
(mod 1).
(3.13)
By (3.13), we have
N
3 −m(ϵ)
2P
−
N
3 −m(ϵ)
2P

= m(ϵ′)
2P
(3.14)
and so again rearranging terms and applying the floor function leads to
N
3 −m(ϵ)
2P

−
N
6 −m(ϵ)
2P

−1 =
N
6 −m(ϵ′)
2P

.
(3.15)
18
JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
Here, we have used ⌊−x⌋= −⌊x⌋−1 for x ∈R \ Z. From (3.3), we compute
Sϵ =
j
N
3 −m(ϵ)
2P
k
X
k=
j
N
6 −m(ϵ)
2P
k
+1
qPk2+m(ϵ)k+ m(ϵ)2
4P
=
j
N
3 −m(ϵ)
2P
k
−
j
N
6 −m(ϵ)
2P
k
−1
X
k=0
qP
j
N
3 −m(ϵ)
2P
k
−k
2
+m(ϵ)
j
N
3 −m(ϵ)
2P
k
−k

+ m(ϵ)2
4P
= qP
j
N
3 −m(ϵ)
2P
k2
+m(ϵ)
j
N
3 −m(ϵ)
2P
k
+ m(ϵ)2
4P
×
j
N
3 −m(ϵ)
2P
k
−
j
N
6 −m(ϵ)
2P
k
−1
X
k=0
qPk2−

m(ϵ)+2P
j
N
3 −m(ϵ)
2P
k
k+ m(ϵ′)2
4P
= q
N(P N/3−m(ϵ′))
3
j
N
6 −m(ϵ′)
2P
k
X
k=0
qPk2+m(ϵ′)k+ 2P Nk
3
+ m(ϵ′)2
4P
(3.16)
where we have applied the substitution k 7→
j
N
3 −m(ϵ)
2P
k
−k and used (3.14) and (3.15). Letting
q = e
2πiM
N
in (3.16) and simplifying yields the result.
In order to prove (iv), we will use (ii) and (iii). A computation similar to that of (3.4) and
the conditions on ϵ and ϵ′ imply
m(ϵ) + m(ϵ′)
2P
≡N
2
(mod 1).
(3.17)
We now distinguish between two different cases.
First, if 2N −ϵ2̸ ≡0 (mod 3), we define
ϵ′′ = (ϵ′′
1, ϵ′′
2, ϵ′′
3) ∈{±1}3 by
ϵ1 + ϵ′′
1
2
≡0
(mod 2),
ϵ2 + ϵ′′
2 ≡2N
(mod 3),
ϵ3 = −ϵ′′
3.
(3.18)
Then (iii) with conditions (3.18) and (3.17) imply
Sϵ = e
2πi(2p3N−m(ϵ′′))M
3
Tϵ′′ = e
2πi(−2p3N−m(ϵ′))M
3
Tϵ′′.
(3.19)
Subtracting the equations in (3.18) from the initial assumptions on ϵ and ϵ′ yields
ϵ′
1 −ϵ′′
1
2
≡N
(mod 2),
ϵ′
2 −ϵ′′
2 ≡N
(mod 3),
ϵ′
3 = ϵ′′
3.
(3.20)
Thus (ii) with conditions (3.20) imply
Tϵ′′ = e
−πi(p3N+m(ϵ′′))M
3
Sϵ′ = e
−πi(−p3N+m(ϵ′))M
3
Sϵ′.
(3.21)
We now combine (3.19) and (3.21) and simplify to obtain the result. Second, if 2N −ϵ2 ≡
0 mod 3, then N −ϵ2̸ ≡0 mod 3 and we define ϵ′′′ = (ϵ′′′
1 , ϵ′′′
2 , ϵ′′′
3 ) ∈{±1}3 by
ϵ1 −ϵ′′′
1
2
≡N
(mod 2),
ϵ2 −ϵ′′′
2 ≡N
(mod 3),
ϵ3 = ϵ′′′
3 .
(3.22)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS 19
Thus (ii) with conditions (3.22) imply
Sϵ = e
πi(p3N+m(ϵ′′′))M
3
Tϵ′′′ = e
πi(−p3N−m(ϵ′))M
3
Tϵ′′′.
(3.23)
Subtracting the equations in (3.22) from the initial assumptions on ϵ and ϵ′, we obtain
ϵ′
1 + ϵ′′′
1
2
≡0
(mod 2),
ϵ′
2 + ϵ′′′
2 ≡2N
(mod 3),
ϵ′
3 = −ϵ′′′
3 .
(3.24)
Thus (iii) with conditions (3.24) imply
Tϵ′′′ = e
−2πi(2p3N−m(ϵ′′′))M
3
Sϵ′ = e
−2πi(4p3N+m(ϵ′))M
3
Sϵ′.
(3.25)
We now combine (3.23) and (3.25) and simplify to obtain the result.
□
Applying the identities from Proposition 3.4 immediately yields the following result. Hence-
forth, we use the convention + for +1 and −for −1 in the indices of Tϵ and Sϵ.
Corollary 3.5. Let p = (2, 3, p3) with (6, p3) = 1 and ℓ= (1, 1, ℓ3) ∈Z3 satisfy 0 < ℓ3 < p3. If
M and N are coprime positive integers and q = e
2πiM
N , then the following are true:
(1) If N ≡0 mod 6, then
T+++ = e−πip3M
3
T−−−= e
πip3M
3
S+++ = e−2πip3M
3
S−−−,
T++−= e−πip3M
3
T−−+ = e−2πip3M
3
S++−= e
πip3M
3
S−−+,
T+−+ = e
πip3M
3
T−+−= e−πip3M
3
S+−+ = e
2πip3M
3
S−+−,
T+−−= e
πip3M
3
T−++ = e−πip3M
3
S+−−= e
2πip3M
3
S−++.
(2) If N ≡1 mod 6, then
T+−+ = T+−−,
T−−+ = T−−−,
T−++ = S+−+ = S++−,
T−+−= S+−−= S+++,
T+++ = S−−+ = S−+−,
T++−= S−−−= S−++.
(3) If N ≡2 mod 6, then
T+++ = −T−+−,
T++−= −T−++,
T+−+ = −S+++ = S−−−,
T+−−= −S++−= S−−+,
T−−+ = −S−++ = S+−−,
T−−−= −S−+−= S+−+.
(4) If N ≡3 mod 6, then
T+++ = e
2πM
3 T+−−= e−2πiM
3
S−++ = e−2πiM
3
S−−−,
T++−= e
2πiM
3
T+−+ = e−2πiM
3
S−+−= e−2πiM
3
S−−+,
T−++ = e
2πiM
3
T−−−= e−2πiM
3
S+++ = e−2πiM
3
S+−−,
T−+−= e
2πiM
3
T−−+ = e−2πiM
3
−S++−= e−2πiM
3
−S+−+.
20
JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
(5) If N ≡4 mod 6, then
T+−+ = −T−−−,
T+−−= −T−−+,
T+++ = −S+−+ = S−+−,
T++−= −S+−−= S−++,
T−++ = −S−−+ = S++−,
T−+−= −S−−−= S+++.
(6) If N ≡5 mod 6, then
T+++ = T++−,
T−++ = T−+−,
T−−+ = S+++ = S+−−,
T−−−= S++−= S+−+,
T+−+ = S−++ = S−−−,
T+−−= S−+−= S−−+.
We now illustrate the previous result.
Corollary 3.6. Let p = (2, 3, p3) with (6, p3) = 1 and ℓ= (1, 1, ℓ3) ∈Z3 satisfy 0 < ℓ3 < p3
and write χ = χ(1,1,ℓ3)
(2,3,p3). If M and N are coprime positive integers and q = e
2πiM
N , then
6p3N
X
n=0
χ(n)q
n2
24p3 = 4
2p3N
X
n=0
χ(n)q
n2
24p3 .
(3.26)
Proof. By Remark 3.2, we obtain
6p3N
X
n=0
χ(n)q
n2
24p3 = −2
X
ϵ∈{±1}3
ϵ1ϵ2ϵ3Tϵ −
X
ϵ∈{±1}3
ϵ1ϵ2ϵ3Sϵ
= 2 (−T+++ + T++−+ T+−+ −T+−−+ T−++ −T−+−−T−−+ + T−−−)
−S+++ + S++−+ S+−+ −S+−−+ S−++ −S−+−−S−−+ + S−−−
and
2p3N
X
n=0
χ(n)q
n2
24p3 = −
X
ϵ∈{±1}3
ϵ1ϵ2ϵ3Tϵ
= −T+++ + T++−+ T+−+ −T+−−+ T−++ −T−+−−T−−+ + T−−−.
Hence, to verify (3.26) it suffices to prove that
0 = −2 (−T+++ + T++−+ T+−+ −T+−−+ T−++ −T−+−−T−−+ + T−−−)
−S+++ + S++−+ S+−+ −S+−−+ S−++ −S−+−−S−−+ + S−−−.
(3.27)
If N̸ ≡0 (mod 3), this follows directly from Corollary 3.5 (2), (3), (5) and (6). Otherwise, the
terms on the right-hand side of (3.27) have to be rearranged. For example, if N ≡0 (mod 6),
by Corollary 3.5 (1), the right-hand side of (3.27) is given by
T+++

2 −2e
πip3M
3
−e−πip3M
3
+ e
2πip3M
3

+ T++−

−2 + 2e
πip3M
3
+ e−πip3M
3
−e
2πip3M
3

+ T+−+

−2 + 2e−πip3M
3
+ e
πip3M
3
−e−2πip3M
3

+ T+−−

2 −2e−πip3M
3
−e
πip3M
3
+ e−2πip3M
3

(3.28)
where M̸ ≡0 (mod 3). We then use the identity 2 −2e
πip3M
3
−e−πip3M
3
+ e
2πip3M
3
= 0 to deduce
(3.27) from (3.28). The proof for N ≡3 (mod 6) is similar.
□
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS 21
