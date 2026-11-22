---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-012-5-proof-of-theorem-6
section_title: "Proof of Theorem 6"
section_number: 5
pages: 20-22
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
Fix a measure ν on Cn. Consider the process νt constructed in Section 2.2. The 
following lemma provides expressions for H(ν) and ˜H(ν) in terms of the process νt.
Lemma 17. One has,
H(ν) = 1
2E
⎡
⎣
∞

0
Tr (Cov(νt)) dt
⎤
⎦,
(30)
and
˜H(ν) = 1
2E
⎡
⎣
∞

0
Tr

Cov(νt) (diag (Cov(νt)))−1 Cov(νt)

dt
⎤
⎦.
(31)
Proof. Formula (30) is exactly the statement of [7, Lemma 8] (and follows by a direct 
calculation of dH(νt) via Itô’s formula). In order to obtain (31), we deﬁne h : Cn →R
by
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
21
h(x) = −

i∈[n]
1 + xi
2
log 1 + xi
2
+ 1 −xi
2
log 1 −xi
2
.
It is easily veriﬁed that
˜H(ν) = h

xdν(x)
 
= h (a0) .
(32)
Now, recall (equation (11)) that
dat = Cov(νt)dBt.
Thus, by Itô’s formula,
dh(at) = ⟨∇h(at), dat⟩+ 1
2Tr

Cov(νt)∇2h(at)Cov(νt)

dt.
A calculation gives
∇2h(x) = −diag

1
1 −x2
1
, . . . ,
1
1 −x2n
 
.
Observe also that since ν is supported on Cn,
diag (Cov(νt)) = In −diag(at)2.
Combining the last displays gives
dh(at) = −1
2Tr

Cov(νt) (diag (Cov(νt)))−1 Cov(νt)

dt + martingale.
We ﬁnally have, by integrating the last equation,
˜H(ν)
(32)
= h(a0)
= h(a0) −E
	
lim
t→∞h(at)

= 1
2E
⎡
⎣
∞

0
Tr

Cov(νt) (diag (Cov(νt)))−1 Cov(νt)

dt
⎤
⎦.

Using (8), the condition (5) implies that, almost surely for all t, Cov(νt) ⪯
βdiag (Cov(νt)) which yields
Tr

Cov(νt) (diag (Cov(νt)))−1 Cov(νt)

≤βTr(Cov(νt)).
(33)
Combining the above ﬁnally gives
22
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
˜H(ν)
(31)
= 1
2E
⎡
⎣
∞

0
Tr

Cov(νt) (diag (Cov(νt)))−1 Cov(νt)

dt
⎤
⎦
(33)
≤1
2βE
⎡
⎣
∞

0
Tr

Cov(νt)

dt
⎤
⎦
(30)
= βH(ν).
