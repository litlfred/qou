---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-011-5-numerical-estimates
section_title: "Numerical estimates"
section_number: 5
pages: 11-12
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
We have not tried to keep track of explicit constants in the proofs above, since
these would obscure the main ideas of the proof, and the calculations become quite
messy. In this section we sketch what a quantified version of the construction
would give, yielding in particularc≥0.00000087. We have not made any attempt
to change the structure of the argument, even slightly, to optimize the constants.
Doing so would likely yield a better value, although we expect acobtained by any
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
RK≤c−d
1 ∆K.
(2) In Theorem 3.2 we have ∆ K≤C d
2 .
(3) In Lemma 3.3
Xd∆−1/2
K ≤|B +(X)|≤(2X+ 1) d.
(4) In Lemma 3.4u∈{±1}whenever|σ i(u)|∈[ 1
1+c3
,1 +c 3].
(5) In Lemma 3.5
(1−o(1)) dYd−1R−1
K ≤|B×(Y)|≤10(C 4Y+ 1) d−1.
For example, following the proofs given above we can take
c1≥3.819, C 2≤857.57, c 3≥0.618,andC 4≤4.16.
The values of most of the constants here are immediate from the proofs presented
above. The constantC 2 is sometimes called Martinet’s constant (see [19]). Hajir,
Maire, and Ramakrishna [20,§3.3.3] proved that we can takeC 2≤857.57.
12 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
For the rest of this sketch we will use the notation≲and≳to hide losses of
(1 +o(1)) d (which are inconsequential since we can takedarbitrarily large). In
general, our construction leads to
(c1/C2)dYd≲|G|≤|GG|≲(2C 4Y+ 1) d
and, withϵ= c3
2+c3
(which is permissible providedXis an integer),
|P|≳(ϵC −1/2
2 )dXd.
By discarding elements ofPandGif necessary, we can assume that the lower
bounds on|G|and|P|are attained, and
(c1ϵC−3/2
2 )d(XY) d≲|A|.
Now
|AA|≲
C 2
2(2C4Y+ 1)
c2
1Y 2
d
|A|2
and
|A+A|≲(4(1 +ϵ)Xe Y + 1)d
≲
(4(1 +ϵ)XeY + 1)C3
2
c2
1ϵ2X 2Y 2
d
|A|2.
For example, with the constant choices above we have
|AA|≲
419531
Y + 50425
Y 2
d
|A|2
and
|A+A|≲
3836812879
XY 2 eY + 776017933
X 2Y 2
d
|A|2,
while
|A|≳(0.000035XY) d.
A rough approximation to the optimal choice is to takeX=⌊e 1140402⌋andY=
1140402, which leads to arbitrarily largeA⊂Rwith
max(|A+A|,|AA|)≤|A| 2−0.00000087.
