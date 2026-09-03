---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-015-53-characters-of-symmetric-groups-related-to-tho
section_title: "Characters of symmetric groups related to Thoma characters"
section_number: 5.3
pages: 17-19
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
shik and Kerov [VK81] proved that if π is a ﬁxed permutation with the
lengths of non-trivial cycles k1, . . . , kr then for any Young diagram λ with
n boxes
χλ(π) =
r∏
i=1
[∑
j
αki
j −
∑
j
(−βj)ki
]
+ O
( 1
n
)
where αj = λj
n , βj =
λ′
j
n ; we prefer to write this formula in an equivalent
form
(21) χλ(π) = nl
(n)l
r∏
i=1
[∑
j
αki
j −
∑
j
(−βj)ki
]
+ O
( 1
n
)
.
In this section we will prove Theorem 17 which together with T heorem
16 give a uniform estimate for the error term in the formula (21). In partic-
ular, for A = n and ε = D
n we recover the result of Vershik and Kerov.
Theorem 17. There exist constants a, C > 0 with the following property.
Let k1, . . . , kr be positive integers; we denote k1 + . . . + kr = l. If λ is a
Young diagram havingn boxes with less than A rows and columns and such
that ε = (k2
1+···+k2
r )n
A2 < C then
(22)
⏐
⏐
⏐
⏐
⏐
∏ r
i=1 Rki+1(λ)
nl −
r∏
i=1
[∑
j
αki
j −
∑
j
(−βj)ki
]⏐
⏐
⏐
⏐
⏐ ≤ ε
( A
n
) l−r
ar,
where αj = λj
n , βi =
λ′
j
n .
18 V ALENTIN FÉRAY AND PIOTR ´SNIADY
Proof. Firstly, let us consider the case r = 1. Note that
N λ(
e, (1, . . . , k)
)
=
∑
j
(nαj)k, N λ(
(1, . . . , k), e
)
=
∑
j
(nβj)k
therefore Theorem 9 implies that the left-hand side of (22) is equal to
⏐
⏐
⏐
⏐
⏐
1
nk
∑
σ1,σ2∈Sk\{e}
σ1σ2=π
|σ1|+|σ2|=|π|
(−1)|σ1|N λ(σ1, σ2)
⏐
⏐
⏐
⏐
⏐.
For a pair of permutations σ1, σ2 which contributes to the above sum we
consider the bipartite graphG and the graph ˜G given by Lemma 11. Clearly,
in this case graph ˜G has more than one component. With Lemma 15 and
Lemma 11
(23)
( n
A
) k−1
⏐
⏐
⏐
⏐
⏐
Rλ
k+1
nk −
∑
j
(
αk
j − (−βj)k)
⏐
⏐
⏐
⏐
⏐ ≤
∑
s≥2
(C0k)2s−2
(2s − 2)!
( n
A2
) s−1
≤ 2C 2
0 k2n
A2 = 2C 2
0 ε,
where the last inequality holds true if 2C2
0 k2n
A2 = 2 C 2
0 ε is smaller than some
positive constant and the proof is ﬁnished in the case r = 1.
For the general case, we put ǫi = k2
i n
A2 . We denote
Xi = 1
a
( n
A
) ki−1 Rλ
ki+1
nki
,
Yi = 1
a
( n
A
) ki−1∑
j
(
αki
j − (−βj)ki
)
.
Let us ﬁx a > 2. Clearly, |Yi| < 2
a < 1 hence (23) shows that |Xi| < 1 if ε
is smaller than some positive constant. Telescopic summation
X1 · · ·Xr − Y1 · · · Yr = X1 · · · Xr−1(Xr − Yr)+
X1 · · · Xr−2(Xr−1 − Yr−1)Yr + · · · + (X1 − Y1)Y2 · · · Yr
shows that
1
ar
( n
A
) l−r
⏐
⏐
⏐
⏐
⏐
∏ r
i=1 Rλ
ki+1
nl −
r∏
i=1
[∑
j
αki
j −
∑
j
(−βj)ki
]⏐
⏐
⏐
⏐
⏐ ≤
2C0(ǫ1 + · · · + ǫr)
a . □
ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS 19
