---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-003-13-the-main-result
section_title: "The main result"
section_number: 1.3
pages: 2-3
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---

|χλ(π)| ≤
a max
where n denotes the number of boxes of λ.
since it provides rather weak estimates in the case when the Young diagram
λ is balanced, i.e. r(λ), c(λ) = O(√n).
Another approach to this problem was initiated by Biane [Bia98, Bia03]
who showed that the value of the normalized character Σλ(π) can be ex-
pressed as a polynomial (called Kerov polynomial) in free cumulants of the
transition measure of a Young diagram λ. The work of Biane was based on
previous contributions of Kerov [Ker93, Ker99] and Vershik. Free cumu-
lants of the transition measure have a nice geometric interpretation therefore
Kerov polynomials are a perfect tool for study of the character χλ(π) in the
limit when the permutation π is ﬁxed and the Young diagram λ tends in
some sense to inﬁnity.
Unfortunately, despite much progress in this ﬁeld ([DF´S10] and refer-
ences therein) our understanding of Kerov polynomials is still not satisfac-
tory; in particular it is not clear how to use Kerov polynomials in order to
obtain non-trivial estimates on the characters χλ(π) when the length |π| of
the permutation π ∈Sn is comparable with n.
In a recent work of one of us with Rattan [R´S08] we took yet another
approach: thanks to the generalized Frobenius formula we showed that the
value of a normalized character of a given Young diagram λ can be bounded
from above by the value of the normalized character of a rectangular Young
diagram p × q for suitably chosen p, q. For such a rectangular Young di-
agram the value of the normalized character can be explicitly calculated
thanks to the formula of Stanley [Sta04]. In this way we proved that for
each C there exists a constant D with a property that if r(λ), c(λ) < C√n
then
!|π|
D max(1, |π|2
n )
√n
,
where |π| denotes the minimal number of factors necessary to write π as
a product of transpositions. Inequality (3) gives a much better estimate
than (2) for balanced Young diagrams and a quite short permutation (|π| =
o(√n)) but a careful analysis of its proof shows that it gives non-trivial
estimates only if max
< O(n3/4).
Theorem 1. There exists a constant a > 0 with a property that for every
Young diagram λ
|π|
r(λ)
n , |π|
n , c(λ)
,
n
ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS
3
It is easy to check that (3) is a consequence of this theorem and that it
gives better estimates than (2) if r(λ)
n , c(λ)
n , |π|
n are smaller than some positive
constant. It is natural to ask what is the optimal value of the constant a.
Asymptotics of characters of symmetric groups related to Thoma characters
shows that a ≥1.
