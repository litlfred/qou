---
doc_id: arxiv-2605.15740v1
doc_title: "BAILEY P AIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS"
section_id: sec-003-22-an-arsenal-of-bailey-pairs
section_title: "An arsenal of Bailey pairs"
section_number: 2.2
pages: 8-10
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
doc_brief: "BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´ e homology"
---
proof of Theorem 1.2. There are eight Bailey pairs that we cite from the literature – six Bailey
pairs relative toqand two Bailey pairs relative toq 2. First, we have four Bailey pairs relative
toqfrom Slater’s list [33, p.463, A(2), A(4), A(6), A(8)]:
αk =



q6r2−r ifk= 3r−1,
q6r2+r ifk= 3r,
−q6r2+5r+1−q 6r2+7r+2 ifk= 3r+ 1
andβ k = 1
(q2)2k
,(2.16)
αk =



q6r2−4r ifk= 3r−1,
q6r2+4r ifk= 3r,
−q6r2+8r+2−q 6r2+4r ifk= 3r+ 1
andβ k = qk
(q2)2k
,(2.17)
αk =



q3r2+r ifk= 3r−1,
q3r2−r ifk= 3r,
−q3r2+r−q 3r2+5r+2 ifk= 3r+ 1
andβ k = qk2
(q2)2k
(2.18)
and
αk =



q3r2−2r ifk= 3r−1,
q3r2+2r ifk= 3r,
−q3r2+4r+1−q 3r2+2r ifk= 3r+ 1
andβ k = qk2+k
(q2)2k
.(2.19)
Next we have two Bailey pairs relative toqfrom work of Warnaar [34]:
αk = (−1)⌊ 4k+1
3 ⌋q
k(2k−1)
3
(1−q 2k+1)
(1−q) χ(k̸≡1 (mod 3)) andβ k = 1
(q)2k
(2.20)
and
αk = (−1)⌊ 4k+1
3 ⌋q
k(k−2)
3
(1−q 2k+1)
(1−q) χ(k̸≡1 (mod 3)) andβ k = qk2−k
(q)2k
.(2.21)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS 9
Finally, we have two Bailey pairs relative toq 2. These are [32, Eq. (2.34),e→0 ande→∞]:
αk =



0 ifk= 3r−1,
(1−q 6r+2)
1−q 2 q3r2−r ifk= 3r,
−(1−q 6r+4)
1−q 2 q3r2+r ifk= 3r+ 1
andβ k = qk2
(q2)2k
(2.22)
and
αk =



0 ifk= 3r−1,
(1−q 6r+2)
1−q 2 q6r2+r ifk= 3r,
−(1−q 6r+4)
1−q 2 q6r2+5r+1 ifk= 3r+ 1
andβ k = 1
(q2)2k
.(2.23)
To these we add two Bailey pairs relative toq 2 which we were not able to locate in the
literature.
Lemma 2.6.The following two sequences are Bailey pairs relative toq 2:
αk =



(1−q k+1)
1−q

q3r2−2r−q 3r2−r

ifk= 3r−1,
(1−q k+1)
1−q q3r2+r ifk= 3r,
−(1−q k+1)
1−q q3r2+2r ifk= 3r+ 1
andβ k = qk2+k(1 +q)
(q2)2k(1 +qk+1) (2.24)
and
αk =



(1−q k+1)
1−q

q6r2−r−q 6r2−2r

ifk= 3r−1,
(1−q k+1)
1−q q6r2+2r ifk= 3r,
−(1−q k+1)
1−q q6r2+7r+2 ifk= 3r+ 1
andβ k = (1 +q)
(q2)2k(1 +qk+1).(2.25)
Proof.We require [25, Eq. (2.4)], which says that if (α k,βk) is a Bailey pair relative toa, then
(α†
k,β†
k) is a Bailey pair relative toaq, where
α†
k = (1−aq 2k+1)(aq/b)k(−b)kq(k
2)
(1−aq)(bq) k
kX
j=0
(b)j
(aq/b)j
(−b)−jq−(j
2)αj (2.26)
and
β†
k = (b)k
(bq)k
βk.(2.27)
10 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
We apply this withb=−qto the Bailey pair relative toqin (2.19). The resultingβ †
k is clearly
theβ k in (2.24), while
α†
k = (1−q k+1)
1−q q(k+1
2 )
kX
j=0
q−(j+1
2 )αj.(2.28)
An induction argument onkconfirms thatα †
k equalsα k from (2.24).
Next we recall that if (α k,βk) is a Bailey pair relative toq 2, then its dual [4] (α d
k,βd
k) is also
a Bailey pair relative toq 2, where
αd
k =q k2+2kαk(q−1) andβ d
k =q−k2−3kβk(q−1).(2.29)
Using the fact that
(q−2;q−1)2k =q−2k2−3k(q2)2k,(2.30)
a short calculation shows that (2.25) is the dual of (2.24).□
