---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-011-5-numerical-estimates
section_title: "Numerical estimates"
section_number: 5
pages: 11-12
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
We have not tried to keep track of explicit constants in the proofs above, since
these would obscure the main ideas of the proof, and the calculations become quite
messy.
In this section we sketch what a quantified version of the construction
would give, yielding in particular c ≥0.00000087. We have not made any attempt
to change the structure of the argument, even slightly, to optimize the constants.
Doing so would likely yield a better value, although we expect a c obtained by any
variant of this kind of argument to be very small.
An earlier version of our argument constructed a field with small split primes,
as in the disproof of the unit distance conjecture described in [2], and considered
elements divisible only by these ideals instead of units. To our surprise, the existence
of small split primes turned out to be completely unnecessary, resulting in the
simplified version presented here, but it is likely that an optimized version would
include these primes.
We first state variants of our lemmas with all the different constants appearing
named, and then give explicit values for these constants, before stating a version
of the main result for these constants, and then finally giving an explicit value for
the main result.
(1) In Lemma 3.1 we have
RK ≤c−d
1 ∆K.
(2) In Theorem 3.2 we have ∆K ≤Cd
2.
(3) In Lemma 3.3
Xd∆−1/2
K
≤|B+(X)| ≤(2X + 1)d.
(4) In Lemma 3.4 u ∈{±1} whenever |σi(u)| ∈[
1
1+c3 , 1 + c3].
(5) In Lemma 3.5
(1 −o(1))dY d−1R−1
K ≤|B×(Y )| ≤10(C4Y + 1)d−1.
For example, following the proofs given above we can take
c1 ≥3.819,
C2 ≤857.57,
c3 ≥0.618,
and
C4 ≤4.16.
The values of most of the constants here are immediate from the proofs presented
above. The constant C2 is sometimes called Martinet’s constant (see [19]). Hajir,
Maire, and Ramakrishna [20, §3.3.3] proved that we can take C2 ≤857.57.
12
THOMAS F. BLOOM, WILL SAWIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
For the rest of this sketch we will use the notation ≲and ≳to hide losses of
(1 + o(1))d (which are inconsequential since we can take d arbitrarily large). In
general, our construction leads to
(c1/C2)dY d ≲|G| ≤|GG| ≲(2C4Y + 1)d
and, with ϵ =
c3
2+c3 (which is permissible provided X is an integer),
|P| ≳(ϵC−1/2
2
)dXd.
By discarding elements of P and G if necessary, we can assume that the lower
bounds on |G| and |P| are attained, and
(c1ϵC−3/2
2
)d(XY )d ≲|A| .
Now
|AA| ≲
C2
2(2C4Y + 1)
c2
1Y 2
d
|A|2
and
|A + A| ≲(4(1 + ϵ)XeY + 1)d
≲
(4(1 + ϵ)XeY + 1)C3
2
c2
1ϵ2X2Y 2
d
|A|2 .
For example, with the constant choices above we have
|AA| ≲
419531
Y
+ 50425
Y 2
d
|A|2
and
|A + A| ≲
3836812879
XY 2
eY + 776017933
X2Y 2
d
|A|2 ,
while
|A| ≳(0.000035XY )d.
A rough approximation to the optimal choice is to take X = ⌊e1140402⌋and Y =
1140402, which leads to arbitrarily large A ⊂R with
max(|A + A| , |AA|) ≤|A|2−0.00000087 .
