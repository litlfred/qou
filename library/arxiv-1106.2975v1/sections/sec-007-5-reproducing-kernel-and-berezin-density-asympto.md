---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-007-5-reproducing-kernel-and-berezin-density-asympto
section_title: "Reproducing kernel and Berezin density asymptotics for a"
section_number: 5
pages: 23-25
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
boundary point
Purpose of the section. In this section, we will calculate the limit of the blow-
up berezin transform ˆB⟨z⟩
m,n,q at a boundary point z, that is, |z| = 1. There is no
loss of generality to take z = 1. Our strategy is to investigate the blow-up of the
reproducing kernel of the space of analytic polynomials Polm,n,1 (with q = 1) ﬁrst,
and then use this information together with poly-Bargmann transform to lift the
the asymptotics to the context of the general polyanalytic spaces Polm,n,q.
24
Haimi and Hedenmalm
The central limit theorem revisited. The following improvement of the central
limit theorem will be needed. Let cdfX denote the cumulative distribution function
of a real-valued random variable X and let
erf(z) =
1
√
2π
Z z
−∞
e−1
2 t2dt
be the error function. We shall write i.i.d. as shorthand for independent identically
distributed in the context of random variables. The following result is from [7],
[11].
Theorem 5.1 (Berry-Esséen). Let X1, X2, ... be i.i.d. real-valued random variables with
E(Xj) = 0, E(X2
j) = 1 and E(|Xj|3) = ρ < +∞for all j. Also, let Yn = n−1/2 Pn
j=1 Xj.
Then there exists an absolute constant C such that

cdfYn(x) −erf(x)

 ≤Cρ
√n
,
x ∈R.
The Berry-Esséen theorem gives the following asymptotics for the partial
Taylor sums of the exponential function.
Lemma 5.2. We have
En−1(x)
ex
= erf
n −x
√n

+ O(n−1/2),
as n →+∞, uniformly in x ∈[0, +∞[.
Proof. Let X1, ..., Xn be independent exponentially distributed random variables
on [0, +∞[ with density e−x. It is well known that the sum Pn
j=1 Xj obeys a gamma
distribution with the cumulative distribution function 1−e−xEn−1(x). The random
variables X1−1, ..., Xn−1 all have zero mean and variance 1, and the third moment
is ﬁnite, so by the Berry-Esséen theorem, we have
(5.1)
1 −e−xEn−1(x) = cdfPn
j=1 Xj(x) = cdf Pn
j=1 Xj−n
√n
x −n
√n

= erf
x −n
√n

+ O(n−1/2),
where the “O” term is uniform in x as n →+∞.
□
This allows us to blow up the function En−1(mz ¯w) when z and w are close to
the point 1 and m, n →+∞with n = m + O(1).
Lemma 5.3. Fix a positive real ε. For complex ξ, η ∈C, we then have
En−1

m(1 + m−1/2ξ)(1 + m−1/2 ¯η)

em+ √m(ξ+ ¯η)
= eξ ¯η erf(−ξ −¯η) + O(m−1
2 +ε),
as m, n →+∞while n = m + O(1). Here, the “O” expression on the right-hand side is
uniform on compact subsets of C.
Proof. If we put
ζ := m(1 + m−1/2ξ)(1 + m−1/2 ¯η) = m + m1/2(ξ + ¯η) + ξ ¯η,
then
n −ζ
√n
= n −m −m1/2(ξ + ¯η) −ξ ¯η
√n
= −ξ −¯η + O(m−1/2),
The Polyanalytic Ginibre Ensembles
25
where the “O” term is uniform on compact subsets. If we use that En−1 has only
nonnegative Taylor coeﬃcients, we get from Lemma 5.2 that
(5.2)
|En−1(ζ)|
e|ζ|
≤En−1(|ζ|)
e|ζ|
= erf
n −|ζ|
√n

+ O(n−1/2),
with a uniform “O” term. So, for real ξ, η, we may deduce from (5.2) the assertion
of the lemma with ε = 0. For general complex ξ, η, we note that
|ζ| = m |(1 + m−1/2ξ)(1 + m−1/2 ¯η)|
= m + m1/2 Re[ξ + η] + Re ξ Re η + 1
2(Im ξ)2 + 1
2(Im η)2 + O(m−1/8)
uniformly in the domain where max{|ξ|, |η|} ≤m1/8. As the right-hand side of (5.2)
is ≤3
2 for big n, we see that

En−1

m(1 + m−1/2ξ)(1 + m−1/2η)

em+ √m(ξ+η)+ξ ¯η

 ≤3
2e−(Im ξ)(Im η)+ 1
