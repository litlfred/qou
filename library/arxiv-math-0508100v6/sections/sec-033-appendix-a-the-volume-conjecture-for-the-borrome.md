---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-033-appendix-a-the-volume-conjecture-for-the-borrome
section_title: "Appendix A. The volume conjecture for the Borromean rings"
section_number: null
pages: 25-27
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
It is well-known that the complement of the Borromean rings B can be geometrically identiﬁed by gluing
two regular ideal octahedra, see [ Thu77]. As a result, the volume vol( S3 − B) of S3 − B is equal to 2 v8.
Suppose L is a k-component framed link, and n1, . . . , nk are positive integers. The colored Jones poly-
nomial ˜JL(n1, . . . , nk) ∈ Z[q±1/ 4] is the sl2-quantum invariant of the link whose components are colored by
sl2-modules of dimensions n1, . . . , nk, see [ RT90, Tur94]. The normalization is chosen so that for the unknot,
˜JL(n) = [ n]. Deﬁne
JL,n (q) := JL(n, n, . . . , n)
[n] .
The next theorem conﬁrms the volume conjecture for the Borrom ean rings.
26 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
Theorem A.1. Let B be the Borromean rings, then
lim
n→∞
log |JB,n (e2πi/n )|
n = 1
2π vol(S3 − B).
Proof. For an integer j and a positive integer k let xj = 2 sin(jπ/n) and zk =∏ k
j=1 xj.
Then, see (
38),
xj = xn−j = −xn+j,(46)
zk = n/zn−1−k for 1 ≤ k ≤ n − 1.(47)
Using Habiro’s formula for ˜JL of the Borromean ring [ Hab00, Hab08], one has
JB,n (q) =
n−1∑
l=0
(−1)l
{n}2
(∏ l
j=1{n + j}{n − j}
) 3
(∏ 2l+1
j=l+1{j}
) 2 .
When q1/ 2 = eiπ/n , one has {j} = 2i sin jπ
n , which is 0 exactly when j is divisible by n. Hence if 2 l+1 < n,
then the denominator of the term in the above sum is never 0, while th e numerator is 0, since it has 2 factors
{n}. On the other hand, if 2 l + 1 > n, then the denominator has 2 factors {n}, which would cancel with the
2 same factors of the numerator. Hence at q1/ 2 = eiπ/n one can assume that 2 l + 1 ≥ n, or l > n/ 2 − 1:
JB,n (e2πi/n ) =
∑
n>l>n/ 2−1
(−1)l evn
(∏ l
j=1{n + j}{n − j}
) 3
(∏ n−1
j=l+1{j}∏ 2l+1
j=n+1{j}
) 2
=
∑
n>l>n/ 2−1
(zl)6
(zn−l−1)2 (z2l+1−n)2 by ( 46)
Using ( 47), which says zl = n/zn−1−l, we have
(48) JB,n (e2πi/n ) =
∑
n>l>n/ 2−1
n2 (γl)2, where γl = (zl)2
(zn−1−l)2 z2l+1−n
.
By ( 51) below, with al = l, bl = n − 1 − l and kl = 2l + 1 − n, we have:
γl = |evn(R+(n; al, bl, kl))|.
By Proposition 8.9, |evn(R+(n; al, bl, kl))| achieves maximum at
amax = ⌊3n/4⌋, b max = ⌊(n − 1)/4⌋, and kmax = amax − bmax .
When l = ⌊3n/4⌋ we have al = amax , while |bl − bmax | ≤ 1 and |kl − kmax | ≤ 1. It is easy to see that
(49) lim
n→∞
log γ⌊(n−1)/ 4⌋ − log |evn(R(n; amax , bmax , kmax ))|
n = 0.
There are less than n summands in the right hand side of ( 48), and each summand is positive. Hence
n2(
γ⌊3n/ 4⌋
) 2
< J B,n (e2πi/n ) < n 3|evn(R(n; amax , bmax , kmax ))|2
From (49) it follows that
2π lim
n→∞
log |JB,n (e2πi/n )|
n = 2π lim
n→∞
log |evn(R(n; amax , bmax , kmax ))|2
n ,
which is equal to 2 v8, according to Corollary 8.10. □
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 27
