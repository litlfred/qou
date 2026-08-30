---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-001-12-short-history-of-the-problem
section_title: "Short history of the problem"
section_number: 1.2
pages: 1-2
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
calculating characters, the Murnaghan–Nakayama rule, qui ckly becomes
cumbersome and hence intractable for computing characters corresponding
to large Young diagrams. Nevertheless Roichman [Roi96] showed that it is
possible to use it to ﬁnd an upper bound for characters, namel y he proved
that there exist constants 0 < q < 1 and b > 0 such that
(2) |χλ(π)| ≤
[
max
( r(λ)
n , c(λ)
n , q
)] b | supp π|
,
where r(λ), c(λ) denote the numbers of rows and columns of λ and supp π
denotes the support of a permutation π (the set of its non-ﬁxed points). In-
equality (2) is not satisfactory for many practical purposes (such as [MR´S07])
1
2 V ALENTIN FÉRAY AND PIOTR ´SNIADY
since it provides rather weak estimates in the case when the Young diagram
λ is balanced, i.e. r(λ), c(λ) = O(√n).
Another approach to this problem was initiated by Biane [Bia 98, Bia03]
who showed that the value of the normalized character Σ λ(π) can be ex-
pressed as a polynomial (called Kerov polynomial) infree cumulants of the
transition measure of a Young diagramλ. The work of Biane was based on
previous contributions of Kerov [Ker93, Ker99] and Vershik . Free cumu-
lants of the transition measure have a nice geometric interpretation therefore
Kerov polynomials are a perfect tool for study of the character χλ(π) in the
limit when the permutation π is ﬁxed and the Young diagram λ tends in
some sense to inﬁnity.
Unfortunately, despite much progress in this ﬁeld ([DF ´S10] and refer-
ences therein) our understanding of Kerov polynomials is still not satisfac-
tory; in particular it is not clear how to use Kerov polynomia ls in order to
obtain non-trivial estimates on the characters χλ(π) when the length |π| of
the permutation π ∈ Sn is comparable with n.
In a recent work of one of us with Rattan [R ´S08] we took yet another
approach: thanks to the generalized Frobenius formula we sh owed that the
value of a normalized character of a given Young diagramλ can be bounded
from above by the value of the normalized character of a rectangular Young
diagram p × q for suitably chosen p, q. For such a rectangular Young di-
agram the value of the normalized character can be explicitl y calculated
thanks to the formula of Stanley [Sta04]. In this way we prove d that for
each C there exists a constant D with a property that if r(λ), c(λ) < C √n
then
(3) |χλ(π)| <
(
D max(1, |π|2
n )√n
) |π|
,
where |π| denotes the minimal number of factors necessary to write π as
a product of transpositions. Inequality (3) gives a much bet ter estimate
