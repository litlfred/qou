---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-004-iv-asymptotics
section_title: "ASYMPTOTICS"
section_number: IV
pages: 17-21
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
A. Asymptotics via Painlev´e
Hastings and McLeod [13] (see also [5,6]) have shown that q(s; 1), the unique solution to
equation (1.11) which is asymptotic to Ai(s) as s →+∞, is asymptotically equal to
q
−s/2
as s →−∞. In fact there is a complete asymptotic expansion in decreasing powers of −s,
beginnning with this term [19]. Successive terms are easily computed. This result and later
ones, become a little easier to state if we write s = −t/2:
q(−t/2; 1) = 1
2
√
t

1 −1
t3 −73
2t6 −10657
2t9
−13912277
8t12
+ O( 1
t15)

(t →+∞)
(4.1)
Squaring and integrating and using (1.14) we deduce
R(s) = 1
4s2 + c −1
8 s +
9
64 s4 −
189
128 s7 + 21663
512 s10 + O( 1
s13)
(s →−∞)
where c is a constant. Substituting this into (1.13) shows that c = 0. Thus we obtain (1.16)
and then, after integrating and exponentiating, (1.17).
17
To obtain the asymptotic expansions of qn(s) in (1.18), we diﬀerentiate (1.11) with
respect to λ and set λ = 1. We obtain
q′′
1 −

s + 6q2
0

q1 = 0
(where q0(s) = q(s; 1)). Using (4.1) we ﬁnd two linearly independent solutions of this equa-
tion, one exponentially large at −∞and one exponentially small. Assuming the exponen-
tially large one actually appears with a nonzero factor we obtain the asymptotic expansion
q1(−t/2) = c1
exp( 1
3t3/2)
t1/4

1 +
17
24 t3/2 + 1513
2732 t3 + 850193
21034 t9/2 + 407117521
21535 t6
+ · · ·

(4.2)
where c1 is a constant factor to be determined.
Successive diﬀerentiations of (1.11) with respect to λ, followed by setting λ = 1, yields a
sequence of linear diﬀerential equations for the qn,
q′′
n −

s + 6q2
0

qn = ϕn(q0, · · · , qn−1),
where ϕn is a polynomial in the qm with m < n. For n > 1 a particular solution dominates
all solutions of the homogeneous equation. Therefore, in the asymptotics, no new unknown
constant factors are introduced (unless we want to go “beyond all orders”).
To deduce expansions for the r(n; s) we must diﬀerentiate (1.15) n times with respect to
λ and set λ = 1. We ﬁnd expressions of the form
r(n; s) =
Z ∞
s (x −s)ψ(q0, · · ·, qn) dx
(4.3)
where ψn is a polynomial in q0, · · ·, qn. In particular we obtain (after setting s = −t/2)
r(1; −t/2) = 1
2
Z t
−∞(t −x)q0(−x/2)q1(−x/2) dx .
Substituting (4.1) and (4.2) into this integral gives the asymptotic expansion for r(1; −t/2).
The ﬁrst order result is
r(1; −t/2) ∼c1
exp(t3/2/3)
t3/4
18
and comparing this with (1.22) reveals that
c1 =
1
2
√
2π .
We now state the expansions we have obtained in this way with the help of Mathematica.
For qn with n > 2, as t →+∞
qn(−t/2) =
n!
23n/2 πn/2
exp( n
3t3/2)
t3n/4−1/2
 
1 + 59n −36
24
t−3/2 +
3481n2 + 8244n −8496
1152
t−3 + O(t−9/2)
!
.
(4.4)
For n = 1, 2 the leading order term is as above. For n = 1 the correction terms are given
above in (4.2). For n = 2 the coeﬃcient of t−3/2 is as given above but the coeﬃcient of t−3
is 5461/288. (Similar exceptional values of n occurred in analogous expansions for the sine
kernel [2].) These expansions have been computed for n ≤10 and are undoubtedly correct
for all n. (In [2] the analogous expansions were proved for all n by a backwards induction
argument—such arguments should extend to the present case of qn.)
For r(n; s) we have obtained the following sharpening of (1.22): as t →+∞
r(n; −t/2) = 1!2! · · ·(n −1)!
2n2+n/2πn/2
exp( n
3t3/2)
t3n2/4
 
1 + n(34n2 + 31)
24
t−3/2 +
n2(1156n4 + 6608n2 + 11509)
1152
t−3 + O(t−9/2)
!
.
(4.5)
This was established for n ≤6. As was mentioned in the Introduction, when we substitute
expansions (4.4) into (4.3) a large amount of cancellation takes place, so that r(n; s) is much
smaller than might be anticipated.
This also means that to deduce even the ﬁrst-order
asymptotics in (4.5) for moderate values of n one has to go very far out in the expansions
(4.4). Thus it is important that we have an alternative approach which yields asymptotic
results for all values of n.
B. Asymptotics via the Commuting Diﬀerential Operator
We begin with the integral identity
19
K(x, y) =
Z ∞
0
A(x + z)A(y + z) dz .
(4.6)
This appears in [5] but we give a simple proof here. Think of (2.12) as a diﬀerential equation
for the “unknown” function K(x, y). Since
 ∂
∂x + ∂
∂y
!
A(x + z)A(y + z) = ∂
∂z A(x + z)A(y + z)
one solution is the right side of (4.6) and, of course, another solution is the Airy kernel
K(x, y). The diﬀerence is therefore of the form ϕ(x −y) for some function ϕ. Since both
sides of (4.6) tend to zero as x and y tend to +∞independently, we must have ϕ ≡0.
Rewriting (4.6) as
K(x, y) =
Z ∞
s
A(x + z −s)A(z + y −s) dz
shows that K as an operator on (s, ∞) is the square of the operator with kernel A(x+y−s).
Integration by parts shows that an integral operator with kernel L(x, y) on (s, ∞) com-
mutes with a diﬀerential operator
d
dxα(x) d
dx + β(x)
if α(s) = 0 and if
α(y)∂2L
∂y2 + α′(y)∂L
∂y + β(y)L = α(x)∂2L
∂x2 + α′(x)∂L
∂x + β(x)L .
(Of course we also require, in the end, appropriate vanishing at ∞.) If we set L(x, y) =
A(x + y −s) and use the fact A′′(x) = xA(x) we can easily check that a solution is given by
α(x) = x −s,
β(x) = −x(x −s)
and so we obtain the commuting diﬀerential operator (1.20).
Here is an outline of how (1.21) is found. If we let f1, f2, · · · denote the eigenfunctions
of L then the logarithmic derivative of each λi (thought of as a function of s) is expressible
very simply in terms of the corresponding fi. The asymptotics of these eigenfunctions, and
so of the logarithmic derivative, is established by WKB techniques. Integrating, and using
20
the fact that each λi →1 as s →−∞, gives (1.21). The WKB argument we give is quite
heuristic although it could very likely be made rigorous.
We make a preliminary change of variables, replacing x by x + s (so that L acts on
(0, ∞)) and s by −2t. The eigenvalue problem can then be written as
(xf ′(x))′ +

µ −(x −t)2
f(x) = 0
(4.7)
or in the equivalent form
xg′′(x) +

µ −(x −t)2 + 1
4x

g(x) = 0 ,

g(x) = √xf(x)

(4.8)
The eigenvalues satisfy 0 < µ0 < µ1 < · · · and oscillation considerations applied to (4.8)
show that µi = O(t1/2), for each i as t →∞. So we think of µ in our equations as O(t1/2),
we normalize our eigenfunctions so that f(0) = 1, and proceed to ﬁnd asymptotics for large
t.
