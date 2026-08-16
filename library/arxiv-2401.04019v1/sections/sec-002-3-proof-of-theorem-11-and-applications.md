---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-002-3-proof-of-theorem-11-and-applications
section_title: "Proof of Theorem 1.1 and applications"
section_number: 3
pages: 6-12
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
Proof of Theorem 1.1. Let R ≥ 2 and 0 < S < R. First we consider the case
S ⁄= R/2. Recall that Conjecture 1 states that, for all k ≥ 1, the sequence ak(n)
deﬁned by (8) has non-negative terms. We prove the conjecture for k ∈ { 1, 2, 3}
using combinatorial arguments.
Let a0(n) = ρR(n). From (9), we see that
a0(n) =





1 n =Ri(3i − 1)/2 for i even
−1 n =Ri(3i − 1)/2 for i odd
0 otherwise.
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 7
The sequence Ri(3i − 1)/2 with i even starts: 0 , 5R, 7R, 22R, 26R,....
The sequence Ri(3i − 1)/2 with i odd starts: R, 2R, 12R, 15R,....
Fork ≥ 0,
∞∑
n=0
(
ak(n) +ak+1(n)
)
qn = qk(k+1)R/2−kS
(qS,q R−S;qR)∞
(1 −q(2k+1)S)
= qk(k+1)R/2−kS
(qR+S,q R−S;qR)∞
(1 +qS +q2S + · · · +q2kS ).(13)
The q-series (13) is the generating function for yk(n) := |Yk(n)|, where
Yk(n) := {(λ,δ R−S,R,k) ⊢n |λ ∈ P ±S,R, 0 ≤mλ(S) ≤ 2k}.
Hence, for k ≥ 0, we have ak+1(n) = yk(n) −ak(n).
Case k = 1: Letn ≥ 0. Then a1(n) = y0(n) −a0(n). We see that ∅ ∈ Y 0(0) and if
n =mR with m ≥ 5, then {(m − 1)R +S,R −S} ∈ Y 0(n). Hence, y0(n) ≥a0(n)
for all n ≥ 0 and thus a1(n) ≥ 0 for all n ≥ 0.
Case k = 2 : We have a2(n) = y1(n) −a1(n) = y1(n) −y0(n) +a0(n). If n = 0,
then Y0(0) = {(∅, ∅)}, Y1(0) = ∅ and a0(0) = 1. Thus a2(0) = 0.
If n ≥ 1 we create an injection
ϕ1 : Y0(n) → Y 1(n) = {(λ,δ R−S,1) ⊢n |λ ∈ P ±S,R}, 0 ≤mλ(S) ≤ 2}.
Let (λ, ∅) ∈ Y0(n). Thus, mλ(S) = 0.
Case I: mλ(R −S) ≥ 1. Deﬁne ϕ1(λ, ∅) := (λ \ (R −S),δ R−S,1).
Case II: mλ(R −S) = 0. Since n ≥ 1, we must have λ ⁄= ∅ and
λℓ ≥ min{R +S, 2R −S}.
Deﬁneϕ1(λ, ∅) := (µ,δ R−S,1), whereµ is the partition obtained from λ by replacing
part λℓ by parts λℓ −R,S .
In each of Cases I and II, the transformation ϕ1 is invertible on its image. Con-
sidering mµ(S) for (µ,δ R−S,1) ∈ϕ1(Y0(n)), we see that the image of ϕ1 in Case I
is disjoint from the image of ϕ1 in Case II. Thus, for n ≥ 1, y1(n) −y0(n) ≥ 0.
Finally, to see that a2(n) ≥ 0 for all n ≥ 0, we need to show that for each n =
Ri(3i−1)/2 withi odd, B1(n) := Y1(n)\ϕ1
(
Y0(n)
)
⁄= ∅. Identifying partitions with
their multiset of parts, we have (( S),δ R−S,1) ∈ B 1(R) and ( {R −S,S 2},δ R−S,1) ∈
B1(2R). If n = mR with m ≥ 12, then ( {(m − 3)R +S, (R −S)2,S 2},δ R−S,1) ∈
B1(mR). Hence, a2(n) ≥ 0 for all n ≥ 0.
Case k = 3 : We have a3(n) = y2(n) −a2(n) = y2(n) − (y1(n) −y0(n)) −a0(n).
Suppose S <R/2. First observe that
• if n = 0, then Y0(0) = {(∅, ∅)}, Y1(0) = Y2(0) = ∅ and a0(0) = 1. Thus,
a3(0) = 0.
• if n =R, then Y0(R) = Y2(R) = ∅, Y1(R) = {((S),δ R−S,1)} and a0(R) =
−1. Thus, a3(R) = 0.
• If n = 2 R, then Y0(2R) = {((R + S,R − S), ∅)}, Y1(2R) = {((R +
S),δ R−S,1), ((R −S,S 2),δ R−S,1)}, Y2(2R) = ∅ and a0(2R) = −1. Thus,
a3(2R) = 0.
Let n ⁄∈ {0,R, 2R}. We create an injection
ϕ2 : B1(n) → Y 2(n) = {(λ,δ R−S,2) ⊢n |λ ∈ P ±S,R, 0 ≤mλ(S) ≤ 4}.
8 CRISTINA BALLANTINE AND BROOKE FEIGON
We consider several cases and in each case we describe the image of ϕ2 either
precisely or as a subset of a larger set. This will be suﬃcient to conclu de that ϕ2
is an injection.
Let (λ,δ R−S,1) ∈ B 1(n). From Case k = 2, B1(n) consists of the pairs (µ,δ R−S,1) ∈
Y1(n) with µ satisfying ℓ(µ) ≥ 3, mµ(S) ∈ {1, 2},µℓ−2 −µℓ−1<R .
Case (i)
mλ(R −S) ≥ 2. Thus, ℓ(λ) ≥ 3 and λℓ−2 −λℓ−1 < R. We deﬁne
ϕ2(λ,δ R−S,1) := (λ \ (R −S,R −S,S ),δ R−S,2).
We obtain all pairs ( µ,δ R−S,2) ∈ Y 2(n) with mµ(S) ∈ {0, 1}
Case (ii) mλ(R−S) = 0. The condition λℓ−2−λℓ−1<R implies thatmλ(S) = 1.
Moreover, λℓ−1 ≥ R +S. Deﬁne ϕ2(λ,δ R−S,1) := ( µ,δ R−S,2), where µ is the
partition obtained from λ by replacing parts λℓ−1 andλℓ−2 by parts λℓ−1 −R and
λℓ−2 −R,S .
We obtain all pairs ( µ,δ R−S,2) ∈ Y2(n) satisfying all of the following conditions.
• ℓ(µ) ≥ 4;
• µℓ−4 −µℓ−3 ≥R;
• µℓ−3 −µℓ−2<R ;
• 2 ≤mµ(S) ≤ 4.
Case (iii) mλ(R −S) = 1.
(a) mλ(S) = 2. Since n ⁄= 2R, we must have ℓ(λ) ≥ 4. Deﬁne ϕ2(λ,δ R−S,1) :=
(µ,δ R−S,2), where µ is the partition obtained from λ by replacing parts λℓ−3 and
R −S by part λℓ−3 −R.
We obtain pairs (µ,δ R−S,2) ∈ Y 2(n) satisfying all of the following conditions.
• ℓ(µ) ≥ 3;
• µℓ−3 −µℓ−2 ≥R;
• 2 ≤mµ(S) ≤ 3.
(b) mλ(S) = 1. Then, condition λℓ−2 −λℓ−1 < Rimplies that λℓ−2 = R +S.
First, let ξ be the partition obtained from λ by replacing parts R +S and R −S
by a part equal to S. We have mξ(S) = 2 and ξℓ−2 ≥R +S.
Ifℓ(ξ) = 2 or ℓ(ξ) ≥ 4 andξℓ−i−ξℓ−i+1 <R fori ∈ {3, 4}, deﬁneϕ2(λ,δ R−S,1) :=
(ξ,δ R−S,2).
We obtain pairs (µ,δ R−S,2) ∈ Y 2(n) satisfying all of the following conditions.
• ℓ(µ) ⁄= 3;
• if ℓ(µ) ≥ 4, then µℓ−4 −µℓ−3<R and µℓ−3 −µℓ−2<R ;
• mµ(S) = 2.
Otherwise, if ξℓ−2 ≤ 2R +S, deﬁne ϕ2(λ,δ R−S,1) := (µ,δ R−S,2), where µ is the
partition obtained from ξ by replacing part ξℓ−2 by parts ξℓ−2 −R,R −S,S .
We obtain pairs (µ,δ R−S,2) in Y2(n) with
• ℓ(µ) ≥ 5;
• (mµ(S),m µ(R −S)) ∈ {(3, 1), (3, 2), (4, 1)};
• µℓ−4 −µℓ−3<R ;
• µℓ−5 −µℓ−4 ≥R.
Ifξℓ−2 ≥ 2R+R−S, Deﬁne ϕ2(λ,δ R−S,1) := (µ,δ R−S,2), whereµ is the partition
obtained from ξ by replacing part ξℓ−2 by parts ξℓ−2 − 2R,R −S,R −S,S,S .
We obtain pairs (µ,δ R−S,2) in Y2(n) with
• ℓ(µ) ≥ 7;
• mµ(S) = 4 and 2 ≤mµ(R −S) ≤ 3;
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 9
• µℓ−7 −µℓ−6 ≥ 2R.
The second condition implies µℓ−4 −µℓ−3<R and µℓ−5 −µℓ−4<R .
In each case, the transformation ϕ2 is invertible on its image and the images in
the diﬀerent cases are disjoint. Thus, for n ⁄∈ {0,R, 2R},y2(n)−(y1(n)−y0(n)) ≥ 0.
Letn ⁄∈ {0,R, 2R} and let B2(n) = Y2(n) \ϕ2(B1(n)). We need to show that for
n =Ri(3i − 1)/2 with i even, B2(n) ⁄= ∅.
We have ((( R −S)2,S 4),δ R−S,2) ∈ B 2(5R), (R +S, (R −S)3,S 4),δ R−S,2) ∈
B2(7R), and for m ≥ 22, ((m − 8)R −S, (R +S)2, (R −S)3,S 4),δ R−S,2) ∈ B 2(mR).
The discussion above shows that ϕ2 is an injection and thus a2(n) ≤ y2(n).
Hence, a3(n) = y2(n) −a2(n) ≥ 0 for all n ≥ 0.
Next assume S > R/2. Much of this case is similar to the case S < R/2. We
highlight the diﬀerences below.
First note that if R −S dividesR (which is equivalent to R −S dividesS), then
in addition to the pairs in Yi(n) for 0 ≤ i ≤ 2, n = 0,R, 2R, listed in the case
S <R/2, we have
((R −S)R/(R−S), ∅) ∈ Y0(R),
((R −S)S/(R−S),δ R−S,1) ∈ Y1(R),
((R −S)2R/(R−S), ∅), ((2R −S, (R −S)S/(R−S)), ∅) ∈ Y0(2R),
((R −S)(R+S)/(R−S)δR−S,1), ((S, (R −S)R/(R−S)),δ R−S,1) ∈ Y1(2R),
((R −S)(2S−R)/(R−S),δ R−S,2) ∈ Y2(2R).
Thus, we still have a3(n) ≥ 0 for n ∈ {0,R, 2R}.
Let n ⁄∈ {0,R, 2R}. The set B1(n) consists of the pairs ( µ,δ R−S,1) ∈ Y 1(n)
with µ satisfying ℓ(µ) ≥ 3, mµ(S) ∈ { 1, 2}, (mµ(S),m µ(R −S)) ⁄= (1, 1), and
µℓ−2 −µℓ−1<R .
Let (λ,δ R−S,1) ∈ B 1(n).
Case (I) mλ(R −S) ≥ 2. Proceed as in Case (i) above and obtain the same
image (pairs (µ,δ R−S,2) ∈ Y 2(n) with mµ(S) ∈ {0, 1}).
Case (II) mλ(R −S) = 0 and mλ(S) = 1. Proceed as in Case (ii) above. We
obtain pairs (µ,δ R−S,2) ∈ Y2(n) satisfying all of the following conditions (which are
slightly diﬀerent than in Case (ii) above).
• ℓ(µ) ≥ 4;
• 2 ≤mµ(S) ≤ 4 and (mµ(S),m µ(R −S)) ⁄= (2, 1);
• if mµ(S) = mµ(R −S) = 2, then µℓ−4 −µℓ−3 ≥ 2R − 2S,
else µℓ−4 −µℓ−3 ≥R;
• µℓ−3 −µℓ−2<R .
Case (III) mλ(R −S) = 1 and mλ(S) = 2. Proceed as in Case (iii)(a) above. We
obtain pairs (µ,δ R−S,2) ∈ Y2(n) satisfying all of the following conditions (which are
slightly diﬀerent than in Case (iii)(a) above).
• ℓ(µ) ≥ 3;
• 2 ≤mµ(S) ≤ 3;
• if mµ(R −S) = 1, then µℓ−3 −µℓ−2 ≥ 2R − 2S,
else µℓ−3 −µℓ−2 ≥R.
Case (IV) mλ(R −S) = 0 and mλ(S) = 2. Then, condition λℓ−2 −λℓ−1 < R
implies that λℓ−2 = 2R −S. First, let ζ be the partition obtained from λ by
10 CRISTINA BALLANTINE AND BROOKE FEIGON
removing one part equal to 2 R −S. We have mζ(S) = 2 and ζℓ−2 ≥ 2R −S. In
particular mζ(R −S) = 0. Now we proceed as in Case (iii)(b) with ξ replaced by
ζ. There are again slight modiﬁcations for the conditions on the obtain ed pairs.
They are as follows. If ζℓ−2 ≤ 2R +S and in the obtained pair ( µ,δ R−S,2) we
have (mµ(S),m µ(R − S)) ∈ { (3, 1), (3, 2)}, then µℓ−5 − µℓ−4 ≥ 2R − 2S, else
µℓ−5 −µℓ−4 ≥R. If ζℓ−2 > 2R +S, then ζℓ−2 ≥ 4R −S and in the obtained pair
(µ,δ R−S,2) we have mµ(R −S) = 2.
The rest of the argument is the same as in the case S <R/2.
If R is even and S = R/2 then 1 /(qS,q R−S;qR)∞ = 1/(qR/2;qR)2
∞. The proof
follows in a similar manner as in the case S < R/2 above if instead of partitions
λ ∈ P ±S,R we consider partitions λ ∈ P R/2,R in two colors.
Alternatively, if R is even and S =R/2, then (8) becomes
∞∑
n=0
ak(n)qn := (−1)k−1
(qS;q2S)2
∞
k−1∑
j=0
(−1)jqj2S(1 −q(2j+1)S) − (−1)k−1(q2S;q2S)∞.
Replacing q by q1/S, we see that proving the non-negativity of the coeﬃcients in
the aboveq-series reduces to the case R = 2, S = 1 of Conjecture 1, i.e., the q-series
(−1)k−1
(q;q2)∞

 1
(q;q2)∞
k−1∑
j=0
(−1)jqj2
(1 −q2j+1) − (q;q)∞


has non-negative coeﬃcients. When k = 1, 2, 3, one can deﬁne simpler injections to
prove the stronger Conjecture 2 below. We leave this as an exercis e for the reader.
This concludes the proof of Theorem 1.1. □
Conjecture 2. Letk be a positive integer. Then, the series
(−1)k−1
(q;q2)∞
k−1∑
j=0
(−1)jqj2
(1 −q2j+1) − (−1)k−1(q;q)∞
has non-negative coeﬃcients.
Next, we derive some applications of Theorem 1.1. We note that, whe n (R,S ) =
(3, 1),
1
(qS,q R−S;qR)∞
= 1
(q,q 2;q3)∞
=
∞∑
n=0
b3(n)qn
and when (R,S ) = (4, 1),
1
(qS,q R−S;qR)∞
= 1
(q,q 2;q4)∞
=
∞∑
n=0
Q(n)qn.
Then, Theorem 1.1 leads to the following linear inequalities for b3(n) and also for
Q(n).
Corollary 3.1. For all n ≥ 0,
b3(n) −b3(n − 1) −ρ3(n) ≥ 0
b3(n) −b3(n − 1) −b3(n − 2) +b3(n − 5) −ρ3(n) ≤ 0
b3(n) −b3(n − 1) −b3(n − 2) +b3(n − 5) +b3(n − 7) −b3(n − 12) −ρ3(n) ≥ 0
Q(n) −Q(n − 1) −ρ4(n) ≥ 0
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 11
Q(n) −Q(n − 1) −Q(n − 3) +Q(n − 6) −ρ4(n) ≤ 0
Q(n) −Q(n − 1) −Q(n − 3) +Q(n − 6) +Q(n − 10) −Q(n − 15) −ρ4(n) ≥ 0.
We continue with another application of Theorem 1.1 when ( R,S ) = (4, 1).
Given a partition λ, the minimal excludant of λ, denoted by mex( λ), is the
smallest positive integer that does not occur as a part of λ. For example,
mex(7, 7, 5, 3, 2, 2, 1) = 4.
In [6], Andrews and Newman deﬁne mex A,a(π) to be the smallest integer con-
gruent to a moduloA that is not a part of the partition π. They also deﬁne pA,a(n)
to be the number of partitions of π of n with
mexA,a(π) ≡a (mod 2A)
and pA,a(n) to be the number of partitions π of n with
mexA,a(π) ≡A +a (mod 2A).
As stated in the introduction, when R = 4,S = 1, Conjecture 1 is equivalent to
the non-negativity of the coeﬃcients of the q-series
1
(q;q2)∞
∞∑
n=0
(−1)TnqTn+2k.
From case k = 1 of Theorem 1.1, we have that for all n ≥ 0,
∑
j≥0
(
Q(n −T4j+2) −Q(n −T4j+4)
)
+
∑
j≥0
(
Q(n −T4j+1)−Q(n −T4j+3)
)
(14)
≥Q(n − 1).
Since T2j = |δ3,4,j| the transformation λ ↦→λ ∪δ3,4,j shows that
Q(n −T2j) = |{λ ⊢n |λ has odd parts, mex 4,3(λ) ≥ 4j + 3}|
Similarly, the transformation λ ↦→λ ∪δ1,4,j+1 shows that
Q(n −T2j+1) = |{λ ⊢n |λ has odd parts, mex 4,1(λ) ≥ 4j + 5}|.
Hence, Q(n −T4j+2) −Q(n −T4j+4) is the number of partitions π of n into odd
parts with mex 4,3(π) = 8j + 7 and Q(n −T4j+1) −Q(n −T4j+3) is the number of
partitions π of n into odd parts with mex 4,1(π) = 8j + 5.
In analogy to [6], we denote by QA,a(n) the number of partitions π ofn into odd
parts with
mexA,a(π) ≡A +a (mod 2A).
Then, the discussion above leads to the following result.
Proposition 1. Forn ≥ 0, we have
Q4,3(n) +Q4,1(n) ≥Q(n − 1).
12 CRISTINA BALLANTINE AND BROOKE FEIGON
