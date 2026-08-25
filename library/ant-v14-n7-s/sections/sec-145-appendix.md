---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-145-appendix
section_title: "Appendix"
section_number: null
pages: 280-281
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
A.1. The role of the stratiﬁcation. It is useful to remark on the crucial role that the stratiﬁcation plays
in obtaining our main theorem. Suppose that instead of Theorem A we only gained information about X1,
without any further stratiﬁcation into X2,..., Xn. Then for those (x(1),..., x(2r))∈ A2nr
Fq \ X1(Fq), we
would have
|S(x(1),..., x(2r))|≤ Cq n/2,
but for those(x(1),..., x(2r))∈ X1(Fq) we could have an upper bound as bad as the trivial (#Fq)n. We
would then have only the instance j= 1 of Theorem 4.4, namely
#
{
{x}∈ (0, k]2r:
⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐> Cq n/2
}
≤ C′′‖k‖2rk−θ1
1 .
In place of (6-1) and Lemma 6.1 we would now have
∑
m(mod q)
|S(F; m, k)|2r≤
∑
{x}∈(0,k]2r
{x}∈X0\X1
⏐⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐⏐+
∑
{x}∈(0,k]2r
{x}∈X1
⏐⏐⏐⏐
∑
m(mod q)
χ( F{x}(m))
⏐⏐⏐⏐
≪‖ k‖2rCq n/2+ C′′‖k‖2rqnk−θ1
1 .
The second term has the worst growth qn appearing in (6-2) combined with the least savings k−θ1
1 =
Bn,r(1; k)−1. Proceeding with Menshov–Rademacher and the remaining argument, we would obtain
|S(F; N, H)|2r≪(log q)2r(n+1)‖H‖2r−1 P−1qn/2(1+ qn/2~Bn,r(1; H/P)−1).
Burgess bounds for short character sums evaluated at forms 1947
The last factor is 1+ qn/2(H1/P)−θ1, which we balance by choosing P= H1q−n/(2θ1). This is a smaller
choice than (7-4), hence provides smaller savings; ultimately this yields the bound
|S(F; N, H)|≪‖ H‖1−1/2r H−1/2r
1 q(nθ1+n)/4rθ1(log q)n+1. (A-1)
This is worse than our main theorem by a factor of q(n−1)/4rθ1.
