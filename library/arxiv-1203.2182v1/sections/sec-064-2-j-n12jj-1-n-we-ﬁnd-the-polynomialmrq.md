---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-064-2-j-n12jj-1-n-we-ﬁnd-the-polynomialmrq
section_title: "(̺j := (N+1)/2−j,j = 1, · · ·,N ), we ﬁnd the polynomialMR(q̺"
section_number: 2
pages: 69-70
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
2;q1,q 2) :=
PR(x = q̺
2;q1,q 2) as (3.35). Up to r ≤ 3, the Macdonald functions MSr+ℓ,r−ℓ(q̺
2;q1,q 2) and
MΛ r+ℓ,r−ℓ(q̺
2;q1,q 2) are listed as:
MS1(q̺
2;q1,q 2) = A
1
2 −A− 1
2
q
1
2
2 −q
− 1
2
2
,
MS2(q̺
2;q1,q 2) =
(
A
1
2 −A− 1
2
) (
A
1
2q
1
2
1 −A− 1
2q
− 1
2
1
)
(
q
1
2
2 −q
− 1
2
2
)(
q
1
2
1q
1
2
2 −q
− 1
2
1 q
− 1
2
2
) ,
MS1,1(q̺
2;q1,q 2) =
(
A
1
2 −A− 1
2
) (
A
1
2q
1
2
2 −A− 1
2q
− 1
2
2
)
(
q
1
2
2 −q
− 1
2
2
) (
q2 −q−1
2
) ,
MS3(q̺
2;q1,q 2) =
(
A
1
2 −A− 1
2
) (
A
1
2q
1
2
1 −A− 1
2q
− 1
2
1
) (
A
1
2q1 −A− 1
2q−1
1
)
(
q
1
2
2 −q
− 1
2
2
)(
q
1
2
1q
1
2
2 −q
− 1
2
1 q
− 1
2
2
)(
q1q
1
2
2 −q−1
1 q
− 1
2
2
) ,
MS2,1(q̺
2;q1,q 2) =
(
A
1
2 −A− 1
2
) (
A
1
2q
1
2
1 −A− 1
2q
− 1
2
1
)(
A
1
2q
− 1
2
2 −A− 1
2q
1
2
2
)
(
q
1
2
2 −q
− 1
2
2
) 2(
q
1
2
1q2 −q
− 1
2
1 q2
) ,
MΛ 1(q̺
2;q1,q 2) = MS1(q̺
2;q1,q 2),
MΛ 2(q̺
2;q1,q 2) = MS1,1(q̺
2;q1,q 2), M Λ 1,1(q̺
2;q1,q 2) =MS2(q̺
2;q1,q 2),
MΛ 3(q̺
2;q1,q 2) =
(
A
1
2 −A− 1
2
) (
A
1
2q
−1
2
2 −A− 1
2q
1
2
2
) (
A
1
2q−1
2 −A− 1
2q2
)
(
q
1
2
2 −q
− 1
2
2
) (
q2 −q−1
2
) (
q
3
2
2 −q
− 3
2
2
) ,
MΛ 2,1(q̺
2;q1,q 2) = MS2,1(q̺
2;q1,q 2), (A8)
16SF is package of Maple program created by J. Stembridge, whic h is available from
http://www.math.lsa.umich.edu/~jrs/maple.html#SF/ .
– 68 –
where A :=qN
2 , and the power sum symmetric function pn is
pn = A
n
2 −A− n
2
q
n
2
2 −q
− n
2
2
. (A9)
A2 Consistency check of the gamma factor (3.47) and (3.48)
Here we check the consistency of the gamma factors (3.47) and(3.48) by applying the identity
of the q-hypergeometric function. Plugging γSr+ℓ,r−ℓ
SrSr of (3.47) into the consistency condition
for Z ref
SU (N )(S3,T 2,1
Sr ;q1,q 2) = Z ref
SU (N )(S3,
Sr;q1,q 2) in (3.43), we expect the following rela-
tion:
PSr(q̺
2;q1,q 2) = (A;q1)r
(q2;q1)r
A− r
2q
r
2
2
=
r∑
ℓ=0
(q2;q1)ℓ(q1;q1)r(A;q1)r+ℓ(q−1
2 A;q1)r−ℓ
(q1;q1)ℓ(q2;q1)r(q1q2;q1)r+ℓ(q1;q1)r−ℓ
(1 −q2q2ℓ
1 )
(1 −q2) (−1)r−ℓA− r
2q
(r−ℓ)(r+ℓ+1)
2
1 q
3r
2 −ℓ
2 .
(A10)
Here we quote an identity eq.(2.8.1) of [93]:
(a;q)r(b;q)r(c;q)r
(q;q)r(aq/b;q)r(aq/c;q)r
= (λbc/a;q)r
(qa2/λbc;q)r
r∑
ℓ=0
(λ;q)ℓ(1 −λq2ℓ)(λb/a;q)ℓ(λc/a;q)ℓ(aq/bc;q)ℓ
(q;q)ℓ(1 −λ)(aq/b;q)ℓ(aq/c;q)ℓ(λbc/a;q)ℓ
(a;q)r+ℓ(a/λ;q)r−ℓ
(λq;q)r+ℓ(q;q)r−ℓ
(a
λ
) ℓ
.
(A11)
Choosing q =q1, λ =q2 and a =A in the above identity and taking b,c → 0 limit, we ﬁnd
(A;q1)r
(q1;q1)r
(−1)rA−2rq−r(r+1)
