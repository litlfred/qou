---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-015-5-mallows-random-permutations
section_title: "Mallows Random Permutations"
section_number: 5
pages: 96-104
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
5.1 A q-Stirling’s Formula
Before we say anything about a q-deformed Stirling’s formula, recall that Stirling’s
formula says that
n!∼
√
2πnnn
en
This is an asymptotic formula. We use the ∼ symbol to denote that
lim
n→∞
n!√
2πnnn
en
= 1
It is worthwhile to note that this formula can be proved using the Euler Maclaurin
formula discussed in chapter 2.
For ﬁxed 0<q < 1, we deﬁne
[n]q = 1−qn
1−q
We can then deﬁne a q-deformed factorial as
[n]q! = [n]q[n− 1]q... [1]q =
n∏
k=1
1−qk
1−q
88
For notational convenience, we will denote [n]q by [n] and [n]q! as [n]!, suppressing the
dependence onq. In a work in progress with Shannon Starr, we require a Stirling type
formula (or asymptotic formula) for [n]!. A similar formula was ﬁrst proved by Moak
[Moak, 1984]. At the time this formula was proved, we were unaware of his work.
As our methods and approximation are slightly diﬀerent, we include our verison and
proof of the q-Stirling formula here.
Theorem 5.1.1. For β ∈ R, let q = exp(−β/n). Let [n]! denote [n]q! for this
particularq. Then we have
ln
([n]!
n!
)
=n
∫ 1
0
ln
(1−e−βy
βy
)
dy + β
2 + 1
2 ln
(1−e−β
β
)
+Rn(β)
whereRn(β) is a remainder term and Rn(β)→ 0 as n→∞ .
Proof. First consider
ln
([n]!
n!
)
As mentioned previously, we wantq to be going to 1 as n→∞ , so we are looking at
q =e−β
n for ﬁxed β. Notice that
ln
([n]!
n!
)
=
n∑
k=1
ln
( 1−qk
(1−q)k
)
To approximate this sum, we use the Euler-MacLaurin approach and compare the
sum to
∫ n
1
ln
( 1−qx
(1−q)x
)
dx
For ease of notation, let
f(x) = ln
( 1−qx
(1−q)x
)
89
In order to make this comparison, we will ﬁrst compare 1
2f(k + 1) + 1
2f(k) to
∫ k+1
k
f(x)dx
and then sum over thek’s. Using the fundamental theorem of calculus, we know that
f(k)+f(k+1)
2 is equal to
∫ k+1
k
d
dx
[
(x−k− 1
2)(f(x))
]
dx (5.1)
Evaluating the derivative in the integrand of 5.1 gives
∫ k+1
k
f(x) +
(
x−k− 1
2
)
f′(x)dx (5.2)
This can be broken up into two integrals,
∫ k+1
k
f(x)dx +
∫ k+1
k
(
x−k− 1
2
)
f′(x)dx
where the ﬁrst integral is exactly what we wanted to compare to and the second
integral is an error term. Consider now only this error term
∫ k+1
k
(
x−k− 1
2
)
f′(x)dx (5.3)
Notice that ∫ k+1
k
(
x−k− 1
2
)
dx = 0
so we can add or subtract any constant from f′(x) without changing the value of the
integral. Using this fact, 5.3 can be written as
∫ k+1
k
(
x−k− 1
2
)
[f′(x)−f′(0)]dx
Since this equation is true for any 1 ≤k≤n− 1, we can simplify this and let k = 0
90
and k + 1 = 1, which gives
∫ 1
0
(
x− 1
2
)
[f′(x)−f′(0)]dx (5.4)
This substitution will not cause any problems, because we can always replace f(x)
byf(x +k) later. Since f′(x)−f′(0) can be rewritten as
∫ x
0
f′′(y)dy
we can write 5.4 as the double integral
∫ 1
0
∫ x
0
(
x− 1
2
)
f′′(y)dydx
Switching the order of integration gives
∫ 1
0
∫ 1
y
(
x− 1
2
)
f′′(y)dxdy
After integrating with respect to x we are left with
1
2
∫ 1
0
y(1−y)f′′(y)dy
Using this combined with 5.2, we have shown that
1
2f(0) + 1
2f(1) =
∫ 1
0
f(x)dx +
∫ 1
0
x(1−x)f′′(x)dx
At this point we can return our attention to the original problem, in which we need
to sum up all of these integrals.
n∑
k=1
f(k) = 1
2f(n)− 1
2f(1) +
n−1∑
k=1
1
2(f(k) +f(k + 1)) (5.5)
91
From the previous calculation,
n∑
k=1
1
2(f(k) +f(k + 1)) =
∫ n
1
f(x)dx +
n∑
k=1
∫ 1
0
x(1−x)f′′(k +x)dx
Since we can move the summation inside the integral, we now turn our attention to
f′′(x) to see if this sum will converge. Calculating f′′(x) gives
−(ln(q))2qx
(1−qx)2 + 1
x2
Substituting e−β
n for q gives
−β2e−βx
n
n2(1−e−βx
n )2
+ 1
x2
Multiplying top and bottom of the ﬁrst fraction by e
βx
n
−β2
n2(e
βx
2n−e−βx
2n )2
+ 1
x2
Noticing that the bottom of the ﬁrst fraction is equal to (2 n sinh(βx
2n))2 leaves
−β2
4n2 sinh2(βx
2n) + 1
x2
This term will converge pointwise to 0 by the dominated convergence theorem as
β
n→ 0. Going back to (5.5) gives
ln
([n]!
n!
)
∼ 1
2f(n) +
∫ n
1
f(x)dx + 1
2
n−1∑
k=1
∫ 1
0
x(1−x)f′′(k +x)dx
where this last term will converge in the limit.
92
If we take q = exp(−β/n) for some β∈ R, then we obtain
ln
([n]!
n!
)⏐⏐⏐
q=e−β/n
= 1
2 ln
( 1−e−β
(1−e−β/n)n
)
+
∫ n
1
ln
( 1−e−βx/n
(1−e−β/n)x
)
dx
+ 1
2
∫ 1
0
x(1−x)
n−1∑
k=1
[ 1
(k +x)2− β2
4n2 sinh2(β[k +x]/n)
]
dx.
We can rewrite this as
ln
([n]!
n!
)⏐⏐⏐
q=e−β/n
= nA(β) +B(β) +Rn(β),
where A(β) and B(β) do not depend on n and Rn(β) is a “small” remainder term,
which vanishes for β ﬁxed in the limit n→∞ . More precisely,
A(β) = 1
n
∫ n
0
ln
(1−e−βx/n
βx/n
)
dx,
which can be seen to be independent of n, by making a change of variables, x =ny
so that dx =ndy:
A(β) =
∫ 1
0
ln
(1−e−βy
βy
)
dy.
We can write
B(β) = β
2 + 1
2 ln
(1−e−β
β
)
.
We throw all of the error terms we accumulated into the last term. It is convenient
to break it into three parts:
Rn(β) = R(1)
n (β) +R(2)
n (β) +R(3)
n (β),
93
where
R(1)
n (β) = 1
2
∫ 1
0
x(1−x)
n−1∑
k=1
[ 1
(k +x)2− β2
4n2 sinh2(β[k +x]/n)
]
dx,
R(2)
n (β) =
∫ n
1
ln
( 1−e−βx/n
(1−e−β/n)x
)
dx−nA(β)− β
2 ,
R(3)
n (β) = 1
2 ln
( 1−e−β
(1−e−β/n)n
)
− 1
2 ln
(1−e−β
β
)
.
At this point, the proof of our theorem is complete, provided that we prove the
following lemma.
Lemma 5.1.1. Forβ∈ R ﬁxed, we have
R(1)
n (β), R(2)
n (β), R(3)
n (β)→ 0,
as n→∞ .
Proof. We immediately know that R(1)
n (β) converges to 0, as n→∞ , since
R(1)
n (β) = 1
2
∫ 1
0
x(1−x)
n−1∑
k=1
[ 1
(k +x)2− β2
4n2 sinh2(β[k +x]/n)
]
dx,
and we may use the dominated convergence theorem.
94
For the next term, we notice
R(2)
n (β) =
∫ n
1
ln
( 1−e−βx/n
(1−e−β/n)x
)
dx−nA(β)− β
2
= n ln
( β/n
1−e−β/n
)
− β
2−
∫ 1
0
ln
(1−e−βx/n
βx/n
)
dx
=−n ln
(1−e−β/n
β/n
)
− β
2−
∫ 1
0
ln
(1−e−βx/n
βx/n
)
dx
=−n ln
(1−e−β/n
β/n ·eβ/2n
)
−
∫ 1
0
ln
(1−e−βx/n
βx/n
)
dx
=−n ln
(2n
β sinh
( β
2n
))
−
∫ 1
0
ln
(1−e−βx/n
βx/n
)
dx.
We know that the integrand converges to ln(1) = 0 pointwise, so that the integral
converges to 0 by DCT. For the other term, we know that
2n
β sinh
( β
2n
)
→ 1,
as n→∞ . Moreover, we have the Taylor expansion
sinh(x) = x + x3
3! + x5
5! +··· + x2n+1
(2n + 1)! +... ,
which means that
sinh(x)
x = 1 + x2
6 +... .
This gives
2n
β sinh
( β
2n
)
= 1 + β2
24n2 +... = 1 + O(n−2), as n→∞ ,
whereO(n−2) means that there is a function (which depends on β as well asn) which
may be bounded by a ﬁnite constant C (which is a function C(β) depending on β)
95
times n−2 for suﬃciently large values of n. This means
ln
(2n
β sinh
( β
2n
))
= O(n−2), as n→∞ ,
since ln(1 +x) =x +O(x2), as x→ 0. Then
−n ln
(2n
β sinh
( β
2n
))
= O(n−1), as n→∞ ,
which means in particular that it converges to 0 as n→∞ , (since 1/n does). We
have seen that R(2)
n (β) does indeed converges to 0 as n→∞ .
Finally, we have
R(3)
n (β) = 1
2 ln
( 1−e−β
(1−e−β/n)n
)
− 1
2 ln
(1−e−β
β
)
= 1
2 ln
( β
(1−e−β/n)n
)
=−1
2 ln
(1−e−β/n
β/n
)
.
We know that
1−e−β/n
β/n → 1,
as n→∞ . Therefore, the logarithm converges to 0.
