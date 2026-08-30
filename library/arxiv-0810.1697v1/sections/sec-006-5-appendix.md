---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA QIHOU LIU"
section_id: sec-006-5-appendix
section_title: "Appendix"
section_number: 5
pages: 12-14
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
doc_brief: "ON THE CABLE EXPANSION FORMULA QIHOU LIU — In this paper, a generalized version of Morton’s formula [8] is proved."
---
Now we will present a proof of lemma 3 and lemma 4.
Proof of lemma 3. By change of variables, we have
∑
k≥0
f (k + 1)g(k + 1)δ(k − t − pk′) =
∑
k′′ ≥1
f (k
′′
)g(k
′′
)δ(k
′′
− t − 1 − pk′)
and∑
k≥0
f (k + 1)g(k + 1)δ(k + t + 2 + pk′) =
∑
k′′ ≥1
f (k
′′
)g(k
′′
)δ(k
′′
+ t + 1 + pk′)
=
∑
k′′ ≤−1
f (−k
′′
)g(−k
′′
)δ(−k
′′
+ t + 1 + pk′)
= −
∑
k′′ ≤−1
f (k
′′
)g(k
′′
)δ(k
′′
− t − 1 − pk′)
CABLE EXPANSION 13
So
∑
k≥0
f (k + 1)g(k + 1){δ(k − t − pk′) − δ(k + t + 2 + pk′)}
=
∑
k′′ ⁄=0
f (k
′′
)g(k
′′
)δ(k
′′
− t − 1 − pk′)
=
∑
k′′ ∈Z
f (k
′′
)g(k
′′
)δ(k
′′
− t − 1 − pk′)
since f (0) = 0
= f (pk′ + t + 1)g(pk′ + t + 1)
□
Proof of lemma 4.
N∑
k′=−N
k′+N even
exp(α1k′2 + α2k′) sinh(α3k′ + ζ)
=
N∑
k′=−N
k′+N even
exp(α1k′2
+ α2k′)(sinh(α3k′) cosh(ζ) + cosh(α3k′) sinh(ζ))
And
N∑
k′=−N
k′+N even
exp(α1k′2 + α2k′) sinh(α3k′)
=
N∑
k′=−N
k′+N even
exp(α1(−k′)2 − α2k′) sinh(−α3k′)
=
N∑
k′=−N
k′+N even
− exp(α1k′2 − α2k′) sinh(α3k′)
= 1/2
N∑
k′=−N
k′+N even
exp(α1k′2) sinh(α3k′)(exp(α2k′) − exp(−α2k′))
=
N∑
k′=−N
k′+N even
exp(α1k′2) sinh(α3k′) sinh(α2k′)
Apply this trick to
N∑
k′=−N
k′+N even
exp(α1k′2 + α2k′) cosh(α3k′)
14 QIHOU LIU
we have
N∑
k′=−N
k′+N even
exp(α1k′2+α2k′) cosh(α3k′) =
N∑
k′=−N
k′+N even
exp(α1k′2) cosh(α3k′) cosh(α2k′)
So
N∑
k′=−N
k′+N even
exp(α1k′2 + α2k′) sinh(α3k′ + ζ)
=
N∑
k′=−N
k′+N even
exp(α1k′2)(sinh(α2k′) sinh(α3k′) cosh(ζ) + cosh(α2k′) cosh(α3k′) sinh(ζ))
In this expression, α2 and α3 are symmetric, and our formula follows. □
