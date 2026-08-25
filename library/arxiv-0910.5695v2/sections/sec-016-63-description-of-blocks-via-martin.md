---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-016-63-description-of-blocks-via-martin
section_title: "Description of blocks via Martin"
section_number: 6.3
pages: 40-41
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
tion of the nontrivial blocks based on the results of Martin. We start by reviewing
the main result in [Mar96].
Assume d⁄= 0 and let λ(0)⊂ λ(1)⊂··· denote the Young diagrams associated
to a ﬁxed nontrivial block in Re p(Sd;F ). For each m≥| λ(n)|, let E(n)
m denote
the simple FPm(d)-module associated to λ(n) (see Theorem 3.4(1)), and let P (n)
m
denote its projective cover. According to [Mar96, Proposition 9], these modules
have Loewy structure
P (0)
m = E(0)
m
E(1)
m
(m≥|λ(1)|),
P (n)
m =
E(n)
m
E(n−1)
m E(n+1)
m
E(n)
m
(n> 0,m≥|λ(n+1)|).
In other words, for m >0, P (0)
m has a maximal simple submodule B0∼=E(1)
m with
P (0)
m /B0∼=E(0)
m . Moreover, for eachm≥|λ(n+1)| there exists a chain of submodules
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 41
with P (n)
m /An ∼= E(n)
m ,An/B±
n ∼= E(n∓1)
m ,B±
n/Cn ∼= E(n±1)
m , and Cn ∼= E(n)
m for
n> 0. Using the notation above, deﬁne the following maps ‡:
(6.14)
α0 =α0,m :P (0)
m ↠P (0)
m /B0∼=C1 ↪→P (1)
m
β0 =β0,m :P (1)
m ↠P (1)/B+
1 ∼=P (0)
m
αn =αn,m :P (n)
m ↠P (n)
m /B−
n ∼=B−
n+1 ↪→P (n+1)
m (n> 0)
βn =βn,m :P (n+1)
m ↠P (n+1)
m /B+
n+1∼=B+
n ↪→P (n)
m (n> 0)
γn =γn,m :P (n)
m ↠P (n)
m /An∼=Cn ↪→P (n)
m (n> 0)
We are now ready to give a general description of the nontrivial blocks in
Rep(Sd;F ).
Theorem 6.10. Supposed is a nonnegative integer and B is a nontrivial block in
Rep(Sd;F ). Then B is equivalent as an additive category to the nontrivial block
described in Theorem 6.4.
Proof. We may assume d⁄= 0. Notice
HomRep(Sd;F )(L(λ(n)),L (λ(n′))) = HomFPm(d)(P (n)
m ,P (n′)
m )
whenever m≥| λ(n)|,|λ(n′)|. Hence, by Proposition 5.22(2), it suﬃces to prove
the maps deﬁned by (6.14) satisfy equations (1)-(7) in Lemma 6.3. Equations (1)-
(5) are clearly satisﬁed. The fact that equations (6) and (7) are satisﬁed follows
from the observation that the maps B∓
n±1 ↪→P (n±1)
m ↠P (n±1)
m /B±
n±1∼=B±
n factor
through the maps B∓
n±1 ↠B∓
n±1/Cn±1∼=Cn ↪→B±
n . □
Remark 6.11. Our proof of Theorem 6.10 is a bit unsatisfactory since it is based
on rather deep results from [Mar96]. On the other hand Theorem 6.10 follows
from Theorem 6.4, Proposition 6.6, along with Conjecture 6.8. Hence a proof of
Conjecture 6.8 would complete a proof of Theorem 6.10 which is independent from
[Mar96].
