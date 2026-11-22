---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-013-7-variants
section_title: "Variants"
section_number: 7
pages: 14-15
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
A related question is to bound the number of solutions to (6.1) in the group of
units O×
K. Evertse [14] proved that the number of solutions to x1 + x2 = 1 with
x1, x2 ∈O×
K is at most 3 · 73d, where d is the degree of K. (Such xi are often
called ‘exceptional units’.) Niklasch [34] considered this question further and in
particular, generalising a conjecture of Stewart (see [15, p.120]), conjectured [34,
Conjecture 4.2] the sub-exponential upper bound of
exp(d2/3+o(1)).
We are able to prove that if we consider the analogous question with 2 variables
replaced by a sufficiently large (but still a constant) number of variables, the anal-
ogous conjecture is false, and in fact there are exponentially in d many solutions.
Theorem 6.3. There exists an integer k ≥2 and an absolute constant C > 1 such
that, for infinitely many d, there exists a number field K of degree d such that there
are at least Cd non-degenerate solutions to (6.1) with xi ∈O×
K.
This is, in hindsight, a simple consequence of the fact that units of bounded
height still have small height after O(1) many sums, and so the size of their k-fold
sumset is small. To highlight the simplicity of the example we will present the
construction from first principles, at the cost of some slight repetition of earlier
arguments.
Proof. Let C > 0 be the constant provided by Theorem 3.2, and let K be a number
field of degree d and discriminant ∆K ≤Cd. Let Y ≥1 be some constant to be
chosen later, and let A = B×(Y ) ⊂O×
K, so that by Lemma 3.1 and Lemma 3.5
|A| ≥Y d−1d−1/2C−d.
|kA| ≤(2keY + 1)d ≤(3keY )d,
|kA| ≥|A|3k/2 ,
say, provided we first choose Y to be some large constant depending on C, and then
k some larger constant depending on Y . By H¨older’s inequality (see, for example,
the proof of [1, Lemma 5]) the left-hand side is at most
for some constant C > 1, where X counts the number of solutions to x1+· · ·−yk = 0
in which no subsum on the left-hand side vanishes. Hence X ≥|A|k/4, say, provided
d is sufficiently large, which concludes the proof (using that −1 ∈O×
K and dilating
by some fixed yk ∈A).
□
In this section, we discuss three variants of our argument.
The first, which
requires only minor modifications, disproves the sum-product conjecture in the p-
adic numbers for each prime p. The bounds obtained are uniform in p, though we
do not make them explicit.
THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS 15

The second, which again requires only minor modifications, produce counterex-
amples to the strongest form of the sum-product conjecture in all sufficiently large
finite fields F, of prime order.

The third, which requires a complete rewrite of the argument, disproves the
sum-product conjecture in certain fields of formal Laurent series in characteristic p.
The bounds on |A + A| and |AA| obtained this way get worse as the characteristic
p grows, but for small characteristics, the bounds are much stronger than those
obtained from the real version of the argument.
