---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-002-3-a-unitary-matrix-model-for-q-deformed-plancher
section_title: "A unitary matrix model for q-deformed Plancherel growth"
section_number: 3
pages: 7-10
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
The growth of Young diagrams can be compared with the growth of a two-dimensional
crystal as shown in ﬁgure 2. We consider every box as a unit falling from sky under gravity.
There is a boundary given by the two lines passing through the origin with slope ±1.
Since the gravity is working downward it is easy to understand that the boxes will arrange
themselves following the rules of a rotated Young diagrams. One can study a controlled
growth process by assigning a probability to each diagram in this process. Following [1, 2],
we can deﬁne a grand canonical ensemble of Young diagrams
E =
∞⋃
k=0
Yk (3.1)
whereYk is a set of Young diagrams with k boxes. Next, assigning a probability for every
diagram in the ensemble we write a grand canonical partition function for the q-deformed
growth process as
Zq =
∞∑
k=0
∑
λk
tkPq(λk)δ(k−|λk|) (3.2)
where t > 0 is called fugacity. In the above expression, Pq(λk) denotes the q-deformed
Plancherel measure for a Young diagram λk discussed in section 2.
7
In order to study the above partition function in the large k limit, we regularise the
sum by imposing a cut-oﬀ on the Young diagrams in the summation over λk in (3.2). We
introduce a large positive integer N and constrain the Young diagrams in the ensemble to
have no more than N rows. This regularisation gives us a handle on the partition function
to carry out a saddle point analysis of the problem. Later we show that the asymptotic
behaviour of this regularised partition function can be captured by a unitary matrix model
where N plays the role of the rank of the unitary group.
The partition function (3.2) for measure (2.16) is given by
Zq =
∞∑
k=1
∑
λk
tkPq(λk) =
∞∑
k=1
∑
λk
tkk!(1−q)2k q2b(λk)
∏
u∈λk
[h(u)]2 . (3.3)
It was observed in [1] that the ordinary Plancherel growth model is equivalent toU(N) GWW
model after restricting the Young diagrams to have maximumN number of rows. The no-gap
phase of GWW model describes the automodel class of Kerov. The limit shape corresponds
to the GWW transition point. In this section, we ﬁrst study the partition function (3.3)
in the large N limit. The partition function admits two possible phases depending the
value of the parameter t for a given q. The weak coupling phase of this theory captures
the q-deformed growth of Young diagrams. Using the connection between UMM and 2D
droplets we show that there exists an equivalentU(N) UMM for the partition function (3.3)
whose no-gap phase captures the growth of Young diagrams under q-deformed Plancherel
measure. Like GWW, this matrix model also admits a third order phase transition. This is
a q-deformed analogue of GWW phase transition.
Using the deﬁnitions of q deformation (2.9), one can write the partition function as
Zq =
∞∑
k=1
∑
λk
exp
[
k lnt +k lnk−k + 2k ln(1−q) +
∑
i⁄=j
ln|qhj−qhi|
−2
N∑
i=1
hi∑
j=1
ln(1−qj)
] (3.4)
where we have dropped a constant term which makes no contribution to the saddle point
equation.
In order to go to the continuum limit, we ﬁrst re-deﬁne the parameter q,
q =e−gs (3.5)
and take the following double scaling limit
N→∞ , g s→ 0 , such that λ =Ngs is ﬁnite. (3.6)
We also scale the variables and the summation appropriately with a factor of N as follows
x = i
N, h (x) = hi
N and
N∑
i=1
=N
∫ 1
0
dx. (3.7)
8
In the large N limit, the total number of boxes scales as
k =
N∑
i=1
hi− N(N− 1)
2
large N
−−−−→
limit
N 2
∫ 1
0
dx h(x)− N 2
2 ≡N 2k′ (3.8)
where ∫ 1
0
dx h(x) =k′ + 1
2 (3.9)
is an O(1) quantity.
The partition function (3.4) in the double-scaling limit can be written as
Zq =
∫
[Dh]eSeff, (3.10)
where Seff is given by
Seff [h(x)] =N 2
[
k′ ln(N 2t(1−q)2k′)−k′ +
∫ 1
0
dx−
∫ 1
0
dy ln|e−λh(x)−e−λh(y)|
−2
∫ 1
0
dx−
∫ h(x)
0
dy ln(1−e−λy)
] (3.11)
Varying the eﬀective action with respect to h(x), we get the saddle-point equation, which
in terms of Young diagram density
u(h) =−∂x
∂h (3.12)
is given by
−
∫ hU
hL
dh′u(h′) e−λh
e−λh−e−λh′ =− 1
λ log
[1−e−λh
λξ
]
(3.13)
with
ξ2 =t k′. (3.14)
u(h) has support between hL andhU. From the monotonicity of hi (2.4), it follows that the
Young diagram density satisﬁes an upper bound
u(h)≤ 1. (3.15)
Therefore, one has to solve the above saddle-point equation in the presence of this constraint.
To solve the integral equation (3.13), we deﬁne new variables
w = 1−e−λh
λ (3.16)
9
such that u(w) = dh
dwu(h). In terms of these variables, the saddle point equation reduces to
−
∫ wU
wL
dw′ u(w′)
w−w′ = 1
(1−λw) logw
ξ (3.17)
wherewL = 1−e−λhL
λ andwU = 1−e−λhU
λ correspond to the end points of the support of u(w).
Since the Young diagram density, u(h) and hence u(w) have an upper cap, we can
classify solutions of (3.17) in two diﬀerent classes. In the ﬁrst class, the Young diagram
density saturates the upper cap whereas in the second class, it does not. The solution class
1 captures the asymptotic growth of Young diagrams.
