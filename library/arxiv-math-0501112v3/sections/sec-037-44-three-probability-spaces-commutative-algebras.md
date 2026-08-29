---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-037-44-three-probability-spaces-commutative-algebras
section_title: "Three probability spaces. Commutative algebras A and A• can be"
section_number: 4.4
pages: 20-21
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
regarded as algebras of random variables on a purely formal l evel (usually
it is not possible to represent them as algebras of functions on some Kol-
mogorov probability space).
Algebras A and A• are trivially isomorphic as vector spaces; we will
denote by Eid : A → A• the identity map between them, in other words
Eid(x) = x.
One can think that Eid is a kind of a conditional expectation.
If ρ is a representation of Sq we consider maps E : A → C and E• :
A• → C given by
E(x) = E•(x) = χ ρ (x).
In this way the following diagram commutes:
(4.3) A Eid
/d47/d47
E
/d40/d40
A•
E•
/d47/d47C .
and we may consider three different probability structures:
• algebra A equipped with the expectation E (which gives rise to the
natural cumulants k),
• algebra A• equipped with the expectation E• (which gives rise to
the disjoint cumulants k•),
• algebra A equipped with the conditional expectation Eid : A →
A• (corresponding conditional cumulants belong to A• and will be
denoted by kid).
The commutativity of the diagram (4.3) implies that the relation between
the corresponding three cumulants is given by the following formula of
Brillinger [Bri69] (see also [Leh04b]).
Proposition 4.1. If x1, . . . , x n belong to the center of A then
(4.4) k(x1, . . . , x n) =
∑
π
k•[
kid(xi : i ∈ π j) : j = 1, 2, . . .
]
,
where the sum runs over all partitions π = {π 1, π 2, . . . } of the set
{1, . . . , n }.
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 21
Example 4.2. Let us consider n = 2: there are two partitions of {1, 2 },
namely
{
{1}, {2}
}
and
{
{1, 2 }
}
therefore
k(x1, x 2) = k•(
kid(x1), k id(x2)
)
+ k•(
kid(x1, x 2)
)
.
Similarly, for n = 3
k(x1, x 2, x 3) = k•(
kid(x1), k id(x2), k id(x2)
)
+ k•(
kid(x1, x 2), k id(x3)
)
+
k•(
kid(x1, x 3), k id(x2)
)
+ k•(
kid(x2, x 3), k id(x1)
)
+
k•(
kid(x1), k id(x2), k id(x3)
)
.
The following result will be of great importance in this article.
Theorem 4.3. For any x1, . . . , x n ∈ A
(4.5) deg kid(x1, . . . , x n) ≤ deg x1 + · · · + deg xn − 2(n − 1).
Furthermore, the highest-order term of the second cumulant is given by
(4.6)
kid(Σ l1 , Σ l2 ) =
∑
r≥1
∑
a1,...,a r≥1
a1+···+ar =l1
∑
b1,...,b r ≥1
b1 +···+br =l2
l1l2
r Σ (a1 +b1 − 1),..., (ar+br − 1)+
terms of degree at most (l1 + l2 − 2).
We postpone its proof to Section 5.
