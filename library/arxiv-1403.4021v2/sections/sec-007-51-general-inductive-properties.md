---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-007-51-general-inductive-properties
section_title: "General inductive properties"
section_number: 5.1
pages: 19-21
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
4.2 (ii).
Proposition 5.1. For all n≥ 2, tn+1 is uniquely determined by tn and tn+1(1).
Proof. In the sequel, we abuse notations by letting ~BMW r denote the image of ~BMW r inside
~BMW n+1. We prove that, for allr≤n+1, tn+1 is uniquely determined bytn and by its value
on ~BMW r. The case r = 1 is the statement of the proposition, since ~BMW 1 =R. We prove
this by descending induction onr, the caser =n+ 1 being trivial. Because of proposition 4.2
(ii) we know that ~BMW r+1 = ~BMW r + ~BMW rsr ~BMW r + ~BMW rs−1
r ~BMW r. If x,y ∈
~BMW r, we have tn+1(xs±1
r y) = tn+1(yxs±1
r ). Conjugating by ( s1s2...s n)n−r maps s±1
r to
sn and x,y to elements x′,y′ of ~BMW n. This yields tn+1(yxs±1
r ) =tn+1(y′x′s±1
n ) =tn(y′x′).
This proves that tn+1 is determined by tn and by its restriction to ~BMW r. The conclusion
follows by induction. □
Proposition 5.2. Lett′
n be the composition of tn with M→M⊗RR[(a2−bc)−1, (b +c)−1].
Then (t′
n) is uniquely determined by t′
1(1) and t′
2(1).
Proof. In view of the previous proposition, it is suﬃcient to prove that, for all n≥ 2,t′
n+1(1)
is determined by t′
n. We have thatRn−1 belongs to
HnsnHn +Hns−1
n Hn− (b +c)b2c2s−2
n + (b +c)s2
n−1 + (bc)2s−1
n sn−1s−1
n .
Sinces−1
n sn−1s−1
n is conjugated tos−1
n−1sns−1
n−1, the Markov property implies that (b+c)tn+1(s2
n−1−
(bc)2s−2
n ) is determined bytn. It is straightforward to check that, because of the cubic relation,
20 Ivan Marin & Emmanuel Wagner
s2
n−1− (bc)2s−2
n is equal to (b+c)
a (a2−bc).1 plus a linear combination of sn−1, s−1
n−1, sn, s−1
n ,
on which the value oftn+1 is clearly determined by tn. It follows that (b +c)2(a2−bc)tn+1(1)
is uniquely determined by tn, and the conclusion follows.
□
We may compare this statement with the stronger assertion one has on BMW +
n .
Proposition 5.3. If (Tn :BMW +
n →S+) is a Markov trace, then it is uniquely determined
by T1(1) and T2(1).
Proof. As before it is suﬃcient to prove that, for all n≥ 2,Tn+1(1) is determined by Tn. We
have that the 12 terms relation can be written as
en−1snen−1−en−1 = x−2sn−1snsn−1−yx−1s−1
n−1sn−yx−1sns−1
n−1 +sn−x−1sn−1sn
−x−1snsn−1 +yx−2sn−1sns−1
n−1 +yx−2s−1
n−1snsn−1
+y2x−2s−1
n−1sns−1
n−1−x−1sn−1−yx−1s−1
n−1 + 1
hence belongs to BMW +
nsnBMW +
n +BMW +
ns−1
n BMW +
n −xsn−1−yx−1s−1
n−1 + 1, hence,
since Tn+1(s±1
n−1) = Tn+1(s±1
n ) = Tn(1), we get that Tn+1(1) is indeed determined by Tn and
the conclusion follows. □
Corollary 5.4. Over BMW +
n , we have t+
n = (−1)n−1η◦t−
n◦E.
Proof. We ﬁrst prove that the RHS deﬁnes a Markov trace on BMW +
n , with values in
S+. We denote Tn this RHS. We clearly have Tn(λβ) = λTn(β), Tn(α +β) = Tn(α) +
Tn(β) and Tn(αβ) = Tn(βα) for all braids α,β ∈ BMW +
n and scalar λ∈ S+, and also
Tn+1(βs±1
n ) = (−1)nt−
n+1(E(βs±1
n )) = (−1)nt−
n+1(E(β)E(s±1
n ))) = (−1)n−1t−
n+1(E(β)s±1
n )) =
(−1)n−1t−
n (E(β))) = Tn(β). By the proposition above we ﬁrst need to prove that T2(1) =
t+
2 (1) and T2(s1) =t+
2 (s1). Recall that t±
2 (1) =δ±
K, t±
2 (s1) = 1 with
δ±
K = y∓x + 1
x .
Since η(δ−
K) =−δ+
K we get T2(1) = δ+
K =t+
2 (1) and T2(s1) = 1 = t+
2 (s1), and the conclusion
follows.
□
This corollary proves that the ‘natural’ diagram below is commutative only up to a sign
depending on n.
BMW n⊗RS
ww ’’
BMW +
n
t+
n

E //BMW−
n
t−
n

S+
’’
S−η
oo
wwS
MARKOV TRACES ON THE BMW-ALGEBRAS 21
