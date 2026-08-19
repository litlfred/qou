---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-010-5-blocks
section_title: "Blocks"
section_number: 5
pages: 26-27
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
of Re p(St,F ) in section 5.5. First we state Frobenius’ result on the symmetric
group:
Theorem 4.8 (Frobenius’ formula‡‡). Fix integers d≥ r≥ 1. Given a Young
diagram λ = (λ0,λ 1,... ) of size d, set µi = λi−i for each i≥ 0. Then Ωr,d,
††The polynomial a(x) (resp. a′(x)) exists since FPn(t) (resp. ¯FPn(t)) is ﬁnite dimensional
overF (resp. ¯F ).
‡‡We take formula (4.7) to be the deﬁnition of ξλ
r,k even if λ = (λ0,λ 1,... ) is not a Young
diagram.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 27
(Deﬁnition 4.1), acts on the simple Sd-module corresponding to λ by the scalar
(4.7) ξλ
r,k := 1
r
k∑
i=0
(µi +k− 1)(µi +k− 2)··· (µi +k−r)
∏
0≤j≤k
j⁄=i
µi−µj−r
µi−µj
wherek is any positive integer such that λk+1 = 0.
The result of Theorem 4.8 ﬁrst appeared in [Fro68]. A modern proof of Theorem
4.8 is outlined in [FH91, exercise 4.17], (see also [Mac95, Example 7 in section I.7]).
We close this section by showing the scalar ξ in Proposition 4.7 is given by
Frobenius’ formula.
Proposition 4.9. Fixt∈F , a positive integerr, and a Young diagram λ. Suppose
that L(λ) = ([n],e ) in Rep(St,F ). If k is a positive integer such that λk+1 = 0,
then (ωr
n(t)−ξλ(t)
r,k )me = 0 for some positive integer m.
Proof. By Theorem 3.7 we may assume n =|λ|. Let ξ and m be as in Proposition
4.7, so that ( ωr
n(t)−ξ)me = 0. Applying the quotient map ψ : FPn(t) ↠ FSn
(Lemma 3.1(2)) to this equation yields (ψ(ωr
n(t))−ξ)mcλ = 0 inFSn wherecλ is a
primitive idempotent in FSn corresponding to λ. Since ψ(ωr
n(t)) is central in FSn,
this implies ψ(ωr
n(t))cλ = ξcλ. Hence, by Deﬁnition 4.5, ξ depends polynomially
on t.
Now, assume d is a positive integer such that d≥λ1 +|λ|. By Proposition 3.25,
applying the functorF to the equation (ωr
n(d)−ξ)me = 0 yields (Ωr,d−ξ)mcλ(d) = 0.
Thus, by Theorem 4.8,ξ =ξλ(t)
r,k whenevert =d is a suﬃciently large integer. Since
ξ depends polynomially on t, ξλ(t)
r,k is a rational function in t, and ξ = ξλ(t)
r,k for
inﬁnitely many values of t, we conclude that ξ =ξλ(t)
r,k for all t∈F . □
5. Blocks
