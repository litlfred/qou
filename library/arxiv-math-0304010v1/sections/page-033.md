---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-033
section_title: "Page 33"
section_number: null
pages: 33-33
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
where a(n) = {a(n)
1 , a(n)
2 , . . .} are families of random variables depending on n
and a = {a1, a2, . . .} is one more family of random variables. Next, assume that
f1(x) = f1(x1, x2, . . .), f2(x) = f2(x1, x2, . . .), . . . are continuous functions in real
variables x = (x1, x2, . . .), where each function actually depends on ﬁnitely many
variables only. Then
{f1(a(n)), f2(a(n)), . . .}
d
−→{f1(a), f2(a), . . .} ,
n →∞.
Using this general fact we conclude from Theorem 6.1 that any polynomial in
η(n)
2
, η(n)
3 , . . . converges in distribution to the same polynomial in ξ2, ξ3, . . .. More-
over, this also holds for any ﬁnite system of polynomials. By virtue of (6.9), each
ηρ is a polynomial in η(n)
2
, η(n)
3
, . . ., within a “remainder term”. So we only need to
check that the “remainder term” does not aﬀect the convergence in distribution.
Remark that the “remainder term” is of the form r(n), where r is an element of
Aext of strictly negative degree. It follows that any moment of r(n) tends to 0 as
n →∞, which implies that r(n)
d
−→0. This shows that the “remainder term” is
negligible.
□
For a diﬀerent proof of Theorems 6.1 and 6.5, see [Ho].
§7. The central limit theorem for Young diagrams
Given λ ∈Yn , we set
∆λ(x) =
√n
2 (¯λ(x) −Ω(x)),
x ∈R.
(7.1)
This is a continuous function on R with compact support. Dropping λ, which we
consider as the random element from the probability space (Yn, Mn), we interpret
(7.1) as a random function ∆(n)(x).
For any polynomial v ∈R[x], the integral
v(n) =
Z
R
v(x)∆(n)(x)dx
(7.2)
makes sense (because ∆(n) is compactly supported) and is a random variable. We
aim to show that the random variables (7.2), where v ranges over R[x], are asymp-
totically Gaussian.
The result will be stated in terms of the Chebyshev polynomials of the second
kind. Instead of the conventional polynomials Uk(x) (see [Sz], [Er]) we prefer to
deal with slightly modiﬁed polynomials
uk(x) = Uk(x/2) =
[k/2]
X
j=0
(−1)j
k −j
j

xk−2j ,
k = 0, 1, 2, . . . .
(7.3)
Note that
uk(2 cos θ) = sin((k + 1)θ)
sin θ
(7.4)
and
Z 2
−2
uk(x)ul(x)
√
4 −x2
2π
= δk,l ,
k, l = 0, 1, 2, . . . .
(7.5)
33
