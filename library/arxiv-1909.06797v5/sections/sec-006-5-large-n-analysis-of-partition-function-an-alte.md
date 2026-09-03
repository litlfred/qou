---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-006-5-large-n-analysis-of-partition-function-an-alte
section_title: "Large N analysis of partition function : an alternate proof of the limit shape theorem"
section_number: 5
pages: 15-16
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
The large N analysis of partition function (4.1) was explicitly done in [7]. We brieﬂy review the
procedure for the readers not familiar with matrix model techniques (for a more comprehensive
treatment of matrix models, see [42–44]). To analyse the partition function (4.3) we denote a valid
Young diagram of symmetric group S k by a set of numbers{ni}N
i=1 where ni denotes the number of
boxes in ith row. N is an arbitrary positive integer greater than or equal to the height of the ﬁrst
Figure 4: A generic Young diagram in English notation. HereN is an arbitrary positive integer. The number
of boxes in the ﬁrst column is less than or equal to N. In general,∃ a number 0 < M≤ N such that ni = 0
for i = M + 1,··· , N.
column. See ﬁgure 4. The dimension of a representation λk of S k is given by [24]
dimλk = k!
h1!h2!··· hN!
N∏
i=1
i< j
(hi− h j) (5.1)
where,
hi = ni + N− i (5.2)
is the hook length of the ﬁrst box in ith row.
We consider the large N limit of the partition function (4.3). In this limit the hook numbers hi∼ N
(5.2). Therefore we deﬁne the following continuous functions to describe Young diagrams at large
N
n(x) = ni
N, h(x) = hi
N, where x = i
N, x∈ [0, 1]. (5.3)
The function n(x) or h(x) captures the distribution of boxes in a large k Young diagram. The
relation between n(x) and h(x) follows from equation (5.2) and is given by
h(x) = n(x) + 1− x. (5.4)
15
The number of boxes in a Young diagram in the large N limit is given by
k =
N∑
i=1
ni−→ N2
[∫ 1
0
dx (h(x) + 1− x)
]
= N2
[∫ 1
0
dxh(x)− 1
2
]
= N2k′ (5.5)
where
k′ =
∫ 1
0
dxh(x)− 1
2 (5.6)
is the renormalised box number and is anO(1) quantity. Thus we see that the number of boxes in a
Young diagram in the largeN limit goes as∼O (N2) and hence N∼O (
√
k). The partition function
(4.3) in N→∞ limit is given by,
QY =
∫
[Dh(x)]e−N2S eﬀ[h(x)] (5.7)
where
−S eﬀ[h(x)] =
∫ 1
0
dx−
∫ 1
0
dy ln|h(x)− h(y)|− 2
∫ 1
0
dxh(x) lnh(x) + k′ ln(zk′) + k′ + 1. (5.8)
Therefore, the dominant contribution to the partition function comes from the extrema ofS eﬀ[h(x)].
Varying S eﬀ[h(x)] with respect to h(x) we get the saddle point equation
−
∫ u(h′)dh′
h− h′ = ln
( h
ξ
)
, where ξ2 = zk′ (5.9)
where the Young diagram density u(h) is given by
u(h) =−∂x
∂h. (5.10)
Monotonicity of h(x) implies 0≤ u(h)≤ 1. u(h) also satisﬁes two conditions
∫
dh u(h) = 1, and
∫
h u(h) dh = k′ + 1
2. (5.11)
We solve the saddle point equation (5.9) to ﬁnd Young diagram density that satisﬁes the constraints
(5.11).
