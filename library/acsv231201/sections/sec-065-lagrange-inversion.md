---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-065-lagrange-inversion
section_title: "Lagrange inversion"
section_number: null
pages: 408-411
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
On many families of recursively deﬁned combinatorial classes, such as tree
enumeration problems, the combinatorial constructions discussed in Chapter 2
yield generating functions satisfying functional equations of the form f(z) =
zv( f(z)) for some function v that is analytic at the origin and does not vanish
there. Although this equation can be solved exactly for f in some simple cases,
the method of Lagrange inversion gives an invaluable tool for computing the
coeﬃcients of f, and their asymptotic behavior, directly from this functional
equation.
Proposition 12.7 (Lagrange inversion formula). If f(z) = zv( f(z)) with v an-
alytic and v(0) , 0 then
[zn] f(z) = 1
n
h
yn−1i
v(y)n.
(12.9)
Proof
Change variables to y = f(z) so that the implicit equation for f implies
z = y/v(y) and dz = dy[1/v(y) −yv′(y)/v(y)2]. The Cauchy integral representa-
tion
[zn] f(z) = 1
2πi
Z
z−n−1 f(z) dz
over a circle suﬃciently close to the origin becomes the integral
1
2πi
Z 
 v(y)
y
!n
−
 v(y)
y
!n−1
v′(y)
dy
12.3 Lagrange inversion
391
around the origin in the y-plane. The diﬀerence between this integral and
1
n
h
yn−1i
v(y)n = 1
2πi
Z 1
n
 v(y)
y
!n
dy
equals
1
2πi
Z 
 v(y)
y
!n−1
−n −1
n
 v(y)
y
!ndy = 1
2πi
Z
d
"y
n
 v(y)
y
!n#
dy = 0 ,
as claimed.
□
To estimate the right-hand side of (12.9) via multivariate asymptotic analy-
sis, we consider the generating function
1
1 −xv(y) =
∞
X
n=0
xnv(y)n
which generates the powers of v, so that
[zn] f(z) = 1
n
xnyn
y
1 −xv(y) .
(12.10)
This formula holds at the level of formal power series and, if v has a non-zero
radius of convergence, at the level of analytic functions.
Asymptotics for [zn] f(z) can be derived in terms of the power series coeﬃ-
cients of v using (12.10). For example, it follows from Theorem VI.6 of [FS09]
that
[zn]f(z) ∼
1
p
2πv′′(y0)/v(y0)
n−3/2v′(y0)n,
(12.11)
where y0 is the least y > 0 such that the tangent line to v at (y, v(y)) passes
through the origin. In our notation y0 is the smallest positive solution to µ(v; y) =
1.
For a ﬁxed power k, the generalization
[zn] f(z)k ∼k
n
yk−1
0
p
2πnv′′(y0)/v(y0)
v′(y0)n
can also be obtained with univariate methods. Using multivariate methods,
however, we may go further and derive bivariate asymptotics for [zn] f(z)k as
k, n →∞, holding uniformly as λ = k/n varies over compact subsets of (0, 1).
Proposition 12.8. Let v be analytic and nonvanishing at the origin, where its
power series expansion is aperiodic with nonnegative coeﬃcients, and of order
at least 2 at inﬁnity. Let f be the nonnegative series satisfying f(z) = zv( f(z))
and deﬁne µ and σ2 by equations (12.5) and (12.6) above, respectively. Let
392
Combinatorial applications
λ = λ(k, n) = k/n and let xλ be the positive real solution of the equation
µ(v; x) = 1 −λ. Then
[zn] f(z)k ∼v(xλ)nxk−n
λ
λ
p
2πnσ2(v; xλ)
= (1 −λ)−nv′(xλ)n
λxk
λ
p
2πnσ2(v; xλ)
,
(12.12)
uniformly as λ varies over any compact subset of (0, 1).
Proof
Exercise 12.5 below asks the reader to prove that if ψ is analytic at the
origin then
[zn]ψ( f(z)) = 1
n
h
yn−1i
ψ′(y)v(y)n ,
(12.13)
a classic extension of Proposition 12.7. Assuming this result and taking ψ(y) =
yk, we see that
[zn] f(z)k = k
n
h
yn−ki
v(y)n
= k
n [xnyn−k]
1
1 −xv(y) ,
(12.14)
representing coeﬃcients in the powers of f as a Riordan array determined
by the (known) function v. We thus apply Theorem 12.2 with φ ≡1, after
reversing the roles of x and y to obtain the Riordan array {ars} with generating
function 1/(1 −yv(x)), yielding
[zn] f(z)k = k
nan−k,k
∼λv(xλ)nxk−n
λ n−1/2
1
p
2πσ2(v; xλ)
.
The ﬁnal equality in (12.12) follows from the deﬁning equation µ(v; xλ) =
1 −λ.
□
Examples seen in previous chapters, including binomial coeﬃcients and De-
lannoy numbers, ﬁt into this framework, but we present a more interesting ex-
ample here.
Example 12.9 (Forests of trees with restricted oﬀspring sizes). Consider the
class of unlabeled plane trees with the restriction that the number of children of
each node must lie in a prescribed ﬁnite subset Ω⊆N. The generating function
f(z) counting such trees by their number of vertices satisﬁes f(z) = zv( f(z))
where v(z) = P
j∈Ωyj (see [FS09, Section VII.3]) and asymptotic behavior
follows from Proposition 12.8. For instance, unary-binary trees are deﬁned by
