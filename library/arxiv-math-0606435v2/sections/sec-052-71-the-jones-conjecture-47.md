---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-052-71-the-jones-conjecture-47
section_title: "The Jones conjecture 47"
section_number: 7.1
pages: 47-48
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Table 2:This table shows the valuesc(i,Y)of (50) for Young tableauxYof 6 boxes and the 7 possible eigenvaluesδiofπY(α).
Y
11−
(
q4
1+q2
)
q7
(1+q2)(1+q+q2)00000000
q400000000q
(1+q2)(1+q+q2)−
(
q2
1+q2
)
q4
q01
2
−((−1+q)q)
2q+q3
2
q2+2q4
−2−2q2
q(1−4q+q2)
2−c(6,)0q6
2+2q2
q6
1+q+q200
−q01
2
−((−1+q)q)
2
q3
2
q2+2q4
−2−2q2
(1−q)2q
2−q2
1+q−c(6,)0q6
2+2q2000
−q201
1+q2
q(1+(−1+q)q)
1+q2−q2−q2q(1+ (−1+q)q)−q2−q2q3(1−q+q2)
1+q2
q6
1+q20
q3001
1+q+q201
2+2q2c(6,)q
2+q3−(q2(2+q2))
2(1+q2)
(−1+q)q2
2
q4
20
−q300001
2+2q2
q2
1+q+c(6,)q
2
−(q2(2+q2))
2(1+q2)
(−1+q)q2
2
q4
20
48 7 Applications of the representation theory
This is, however, not really a problem, because in the braids γa = β6a−1,−2a of (46) we need for our proof, k = 6a − 1
is always odd, so we need only c(i,Y ) − c(i′,Y ) to evaluate the polynomial in (48).
We used the special evaluations to select equations that give the full matrix rank, and to guess the formula for general
q for some of the c(i,Y ). (The ones we already found suggest that these formulas shou ld not be so complicated.)
Substituting these (yet potential) solutions too, gives aneven simpler linear system for the still unknownc(i,Y ), which
then could be solved in q.
Since we know that our matrix has rank 14, it is enough to check our solution (up to the 1-dimentional ambiguity,
which will disappear in (48)) with the 111 equations we have. The result was conﬁrmed, and is shown in table 2.
With all c(i,Y ) determined, the main work is done. So far we can evaluate X(ˆβk,l) for odd k. Multiplying (53) by
Z = (1 + q)(1 + q2)(1 + q + q2) to clear all denominators in the c(i,Y ), normalizing and taking coefﬁcients in λm for
m = 0, . . . ,5, we have (with eY being the exponents of q in (52) and e = [βk,l])
[
− 1
√
λ
e−5 · Z · (1 − q) · . . .· (1 − q6)Xˆβk,l
(q,λ)
]
λm
= ∑
Y ⊢6
7
∑
i=1
(Z · c(i,Y )) δk
i ql·eY
[ ˆWY (q,λ)
]
λm .(54)
Recall that for our proof it is enough to show that this term be comes non-zero for m = 0 or m = 1, when k = 6a − 1
and l = −2a for an integer a > 1 (and βk,l = γa in (46)). Now, for odd k (and ﬁxed Y), we can group the sum over 7
terms Z · c(i,Y ) into 5 terms ˜c(i,Y ) accounting for δ3 = −δ4 and δ6 = −δ7, and thus excluding i = 4,7. So the above
sum in (54) becomes
∑
Y ⊢6
6
∑
i = 1
i ⁄= 4
˜c(i,Y )δk
i ql·eY
[ ˆWY (q,λ)
]
λm .(55)
(Now in the ˜c(i,Y ), the 1-degree ambiguity of c(i,Y ) for Y = , as explained above, cancels out.)
Among the 55 possible (i,Y ) (with i ⁄= 4,7), only 21 of the ˜c(i,Y ) are non-zero. It turns out that for m = 0, when
k = 6a − 1, l = −2a and a > 1, there is a unique term among the 21 summands in (55) whose mi nimal degree in q is
the smallest (it is 14 − 36a). Thus [P(ˆβk,l)]ve−5 ⁄= 0. We calculated the polynomial with Morton-Short’s program for
a = 2 (where the calculation was still feasible), and it conﬁrme d that all 6 v-terms appear. We also calulated that for
m = 0 and a = 0,1 there are two terms of smallest minimal degree. This better ought to be so, because in that case ˆγa
are just a 2-cable of the unknot and !5 1, resp., and the coefﬁcients for m = 0,1 in (55) must be 0, which we checked
once more separately. (Also we found that for m = 1 there are two terms of smallest minimal degree in (55) for al l
a ≥ 0.) With this the proof of theorem 7.1 is complete.
Let us ﬁnally say that the computer part of the calculation ow ed a lot to the use of MATHEMATICA. While, if done
properly, it could be carried out in a few minutes, it required a week of work to ﬁnd the way of skillfully programming
MATHEMATICA to do all the separate steps in an efﬁcient way. ✷
Remark 7.1 Note that one could handle the cases µ = σ6a+1
1 σ−1
2 from the beginning of the proof also using the
representation theoretic argument, by looking at m = 4,5 for a < 0. We waived on this investigation, though, since the
proof for a > 0 was laborious enough.
