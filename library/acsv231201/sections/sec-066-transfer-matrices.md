---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-066-transfer-matrices
section_title: "Transfer matrices"
section_number: null
pages: 411-417
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
393
Ω= {0, 1, 2}, giving v(z) = 1 + z + z2 and
µ(v; z) =
2z2
z2 + z + 1
σ2(v; z) =
z

z2 + 4z + 1

(z2 + z + 1)2 .
When k/n = 1/4, so that the average tree size in a forest is 4, Proposition 12.8
implies that the number [zn] f(z)k of forests of unary-binary trees with n nodes
and k trees is asymptotically given by Cαnn−1/2 where C ≈0.12666642608296
and α ≈2.8610046903287.
◁
12.4 Transfer matrices
The univariate transfer matrix method, discussed in Chapter 2, is easily ex-
tended to multivariate generating functions that enumerate multiplicatively
weighted paths. If M is a matrix indexed by a ﬁnite set S , the weight w(x)
of the path x = (x0, . . . , xn) ∈S n under M is Qn
r=1 Mxr−1,xr. The sum of weights
of all paths of length n from i to j under M is given by (Mn)i,j, yielding the
generating function Fij(z) = (I −zM)−1
i j enumerating weighted walks from
i to j by length. Similarly, the multivariate generating function enumerating
weighted walks by length while also tracking d additive integer valued func-
tions v1, . . . , vd deﬁned by their values v(i, j) on single steps (i, j) is
Fv(y, z)i,j = (I −zMv)−1
i j ,
where Mv is the matrix whose (i, j)-coeﬃcient is Mi, jyv(i,j). We consider two
applications of this observation, message passing and quantum random walks.
Example 12.10 (Message passing). Let G be the graph on K + L + 2 vertices
which is the union of two complete graphs of sizes K +1 and L+1, with a loop
at every vertex and one edge between them. Paths on this graph correspond to
a message or task being passed around two workgroups, with communication
between the workgroups not allowed except between the bosses. If we sample
uniformly among paths of length n, how much time does the message spend
among the common (non-boss) members?
To analyze this problem we build a new graph, with vertices {v1, v2, v3, v4}
where v1 represents the common Group 1 members, v2 represents the Group
1 boss, v3 represents the Group 2 boss, and v4 represents the common Group
2 members. Every time the message moves to v1 it can do so in K ways, and
every move to v4 can be done in L ways. The generating function counting
394
Combinatorial applications
paths by time spent among the common members of each workgroup and by
total length is (I −zA)−1, where
A =

Ku
Ku
0
0
1
1
1
0
0
1
1
1
0
0
Lv
Lv

with u tracking time among common Group 1 members, v tracking time among
common Group 2 members, and z tracking the total time. The entries of (I −
zA)−1 are rational functions with common denominator Q(Ku, Lv, z), where
Q(u, v, z) = uz2 + uz2v −uz −uz4v + z2v −2z −zv + 1 + z3v + uz3 ,
and the coeﬃcient of zn in the power series expansion of any entry gives a prob-
ability distribution for the amount of time spent among the common members
of each group after time n. Using Gr¨obner bases (or simply by computing a
resultant) it can be shown that the system Q(u, v, z) = Qz(u, v, z) = 0 has no so-
lutions with u, v > 0. Thus, by the limit theorem discussed in Theorem 12.33
below, the times spent in Group 1 and Group 2 as a portion of the length n
converge to m = −∇log Q(K, L, z0), where z0 is the minimal modulus root of
f(z) = Q(K, L, z).
The portion of time spent among the common members of Group 1 is given
by KQu(K, L, z)/(z0Qz(K, L, z0)). Plugging in K = L = 1, for example, we
see that Q(1, 1, z) = 1 −4z + 3z2 + 2z3 −z4 so z0  0.382 and a proportion
of approximately 0.154 of the time is spent among the common members of
Group 1. If bosses and employees had equal access to communication then,
by symmetry, this portion would be 1/4, so the eﬀect of communicating only
through bosses reduced the time each message spends with each non-boss by
nearly 40%. This eﬀect is more marked when the workgroups have diﬀerent
sizes: increasing the size of the second group to 2, we plug in K = 1 and
L = 2 to ﬁnd that z0  0.311 and the fraction of time spent among the common
members in Group 1 plummets to just under 0.038.
◁
Example 12.11 (One-dimensional quantum walk). In Example 9.47 the notion
of a quantum random walk, and its associated spacetime generating function
F, was introduced. Letting p(r, n) denote the amplitude for the random walk to
be at location r at time n, we have
F(z) =
X
r,n≥0
p(r, n)xryn = (I −yMU)−1,
where U is a k×k unitary matrix and M is a k×k diagonal matrix whose entries
12.4 Transfer matrices
395
xa run through the k possible steps (a, b) of the walk. It is shown in [BP07] that
when k = 2 there is no loss of generality in taking U to be the real matrix
Uc =

c
√
1 −c2
√
1 −c2
−c

and taking the entries of M to be 1 and x, meaning that the walk either stays
where it is or moves one to the right. The universal spacetime generating func-
tion for a two-dimensional quantum walk is therefore given by
Fc(x, y) = Pc(x, y)
Qc(x, y) =
Pc(x, y)
1 −cy + cxy −xy2 ,
where the numerator Pc depends on initial chiralities (one of k hidden states
of the walk) and plays no special role. For example, if k = 2 and starting and
ending chiralities are both in state 2 then Pc(x, y) = 1 −cy.
◁
Theorem 12.12 (Spacetime asymptotics for one-dimensional quantum walk).
There is a real phase function ρ(r, s) such that
p(r, s) = 2
π
λ
√
1 −c2
(1 −λ)s
p
−((1 −c2) −4λ + 4λ2)
cos2(ρ(r, s)) + O

s−3/2
uniformly as λ =
r
s varies over any compact subset of the interior of Jc =
[(1 −c)/2, (1 + c)/2]. Conversely, if λ varies over a compact subset of the
complement of Jc then p(r, s) →0 exponentially.
The variation of probabilities in the feasible region for c = 1/2 is illustrated
in Figure 12.2. Qualitatively similar results hold for the other starting and end-
ing chiralities, and for combinations of chiralities.
Proof
The denominator Q = 1 −c(1 −x)y −xy2 is quadratic in y and linear
in x, so the critical point equations can be solved explicitly in radicals. Fur-
thermore, Q satisﬁes the strong torality hypothesis (Deﬁnition 9.20) so that
Corollary 9.21 applies. The intersection V1 of V with the unit torus is a topo-
logical circle x = (cy −1)/(cy −y2) winding twice around the torus in the x
direction and once in the y direction. The logarithmic Gauss map is a smooth
map on this circle with two extreme values, (1−c)/2 and (1+c)/2, and no other
critical points. Therefore, for each λ in the interior of Jc there are precisely two
points (x1, y1) and (x2, y2) in V1 with ∇log Q(x j, y j) ∥(λ, 1) and an application
of (9.7) implies
p(r, s) =
2
X
j=1
1 −cy j
√
2π
x−r
j y−s
j
s
−yjQy(x j, yj)
s Q(xj, y j)
+ O

s−3/2
,
396
Combinatorial applications
0.06
0.02
n
80
70
60
50
40
30
20
0.04
0.08
0.0
Figure 12.2 The time n = 100 probabilities starting and ending in state 2 when
c = 1/2, and their upper envelope obtained by dropping the cos2(ρ) term in The-
orem 12.12.
where Q is given by (9.6). The two critical points (x1, y1) and (x2, y2) are con-
jugate, meaning
p(r, s) = 2 Re

1 −cyj
√
2π
x−r
j y−s
j
s
−yjQy(xj, yj)
s Q(xj, y j)
+ O

s−3/2
.
Deﬁning ρ to be the argument of the expression in braces, writing (x, y) for
either one of the two points, and taking the square modulus, we obtain
p(r, s) = 2
π cos2(ρ)

(1 −cy)2 −yQy(x, y)
s Q(x, y)

 + O

s−3/2
.
Using the techniques of Chapter 8, we compute that at the critical point (x, y)
the quantity
w = (1 −cy)2 −yQy(x, y)
n Q(x, y)
satisﬁes
λ2(1 −c2) + 4
 (1 + c)
2
−λ
! 
λ −(1 −c)
2
!
(1 −λ)2w2 = 0,
12.4 Transfer matrices
397
where λ and c are parameters. Solving, we ﬁnd
|w| =
√
1 −c2λ
(1 −λ)s
p
−((1 −c2) −4λ + 4λ2)
,
proving the claimed asymptotics when λ ∈Jc.
If λ < Jc then either (0, 0) does not minimize the height function in the
direction (λ, 1) on the amoeba complement component corresponding to the
power series expansion of Fc, meaning β ≤β* < 0, or (0, 0) is the minimizing
point but there are no critical points on T(1, 1), so Theorem 11.4 implies β < 0.
In either case, p(r, s) decays exponentially.
□
Example 12.13 (QRWs in higher dimensions). Example 9.47 of Chapter 9
shows that, in general, the spacetime generating function for a quantum walk
with steps v(1), . . . , v(k) has the form
F(z) = (I −zd+1MU)−1,
where z◦= (z1, . . . , zd) are d space variables, the variable zd+1 tracks time, and
M is the diagonal matrix whose (j, j)-entry is (z◦)v( j). The common denomi-
nator of the Fij is Q(z) = det(I −zd+1MU). As noted in Example 9.47, the
feasible velocity region R is the image of the logarithmic Gauss map and the
limit law for the amplitudes can be written, up to an oscillatory term, in terms
of the Gaussian curvature.
Consider the two-dimensional family of walks with the nearest neighbor unit
vectors v(1), . . . , v(4) as steps and the unitary matrix
U = S (p) =

√p
√
2
√p
√
2
√
1−p
√
2
√
1−p
√
2
−
√p
√
2
√p
√
2
−
√
1−p
√
2
√
1−p
√
2
√
1−p
√
2
−
√
1−p
√
2
−
√p
√
2
√p
√
2
−
√
1−p
√
2
−
√
1−p
√
2
√p
√
2
√p
√
2

.
Setting α =
p
2p to simplify notation, we have
Q(x, y, z) = (x2y2 + y2 −x2 −1 + 2xyz2)z2 −2xy
−αz(xy2 −y −x + z2y −z2x + z2xy2 + z2x2y −x2y)
and a lexicographic Gr¨obner Basis for the ideal generated by Q and its partial
derivatives includes the polynomial
zα2(α2 −1)(α2 −2) = 2zp(2p −1)(2p −2).
The only root of this polynomial with x, y, z , 0 and 0 < p < 1 occurs when
398
Combinatorial applications
p = 1/2, and back substitution of this value implies that −z+z5 = z3 +2y−z =
−z −z3 + 2x = 0. The ﬁrst of these polynomials vanishes on the unit circle
when z ∈{±1, ±i}, however when z = ±1 the second polynomial only vanishes
when y = 0, and when z = ±i the third polynomial only vanishes when x = 0,
so Q and its partial derivatives do not simultaneously vanish on T(1).
Thus, if Qz vanishes at some point (a, b, c) of V1 = V ∩T(1) then (a, b, c)
contributes to nonvanishing asymptotics in a direction (r, s, 0) for some (r, s) ,
(0, 0). This is ruled out from our knowledge of the generating function, because
the velocity of QRW is at most the longest step, so Qz does not vanish on
V1 and the projection (x, y, z) →(x, y) is a smooth four-fold cover of the
unit torus in C2. There are many four-fold covers of the 2-torus, but in this
case some trigonometry [Bar+10, Proposition 4.6] shows that V1 is in fact
the union of four 2-tori, each mapping diﬀeomorphically to the 2-torus under
the logarithmic Gauss map. Figure 12.13 shows the four components for the
parameter value p = 1/2 by graphing z as a function of x and y with the torus
depicted as the unit cube with wraparound boundary conditions.
Figure 12.3 The four tori comprising V1 for S (1/2).
Asymptotic behavior follows from Corollary 9.46 in Chapter 9.
Theorem 12.14. For each ˆr in the image of the logarithmic Gauss map on V1
