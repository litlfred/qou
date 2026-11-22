---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-002-3-computer-calculations-of-ohtsuki-series
section_title: "Computer calculations of Ohtsuki series"
section_number: 3
pages: 9-11
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
toc_source: inferred
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
Computer calculations of Ohtsuki series
Using (3), ZK(M±
(( S
T ))) can be computed for all the K −1 diﬀerent Kth
roots of unity, q = qs = exp 2πis
K
(1 ≤s < K) for ﬁxed S, T and prime
K. From these values, the coeﬃcients am,K(M±
(( S
T ))) ∈Z can be found
in (1) where we assume that they vanish past the (K −2)th. Namely,
one solves the following linear system of size K −1,
ZK|q=qs =
K−2

m=0
am,K.(qs −1)m ,
(5)
where the dependence on the manifold has been omitted from the no-
tation. The integrality of the solutions provides a check on the errors in
the computations of the individual WRT invariants at diﬀerent roots
of unity.
There a number of computational challenges here.
3.1. Growth of number of states
As was mentioned in the previous section, the sum obtained from
naively applying, say the Kauﬀman-Lins prescription, to the knot di-
agram Figure 1 leads to a sum over a number of states which grows
exponentially with S, since there would be a summation over S in-
dices ij, and the non-trivial quantum 6j-symbols eﬀectively introduce
a further S −1 summations, where the summand is now a product (or
quotient of products) of quantum numbers and factorials. This problem
is obviated with the used of recombination; thus (3) only involves a sum
over 4 indices (a, x, y and an additional index from the single quantum
6j-symbol) so that there are the order of K3 states to be summed over
(or K4 with a summand which is a quotient of products of quantum
numbers and factorials), and this is independent of S and T.
3.2. Numerical precision and summand size
Since q-factorials can be numerically very large, the individual terms
in (3) can be many orders of magnitude larger than their sum and this
necessitates using very high precision arithmetic.
We give the example of K = 97 for the manifold M+
(( 3
2 )) obtained
by surgery around the knot 52 (obtained from S = 3, T = 2, U = 6).
61
N. Jacoby & R. Lawrence
For s = 1, [90]! ≈10114 and the order of summands in ZK for s = 2
is ∼1026, while their sum (Z97) is ∼106. To obtain an accuracy of d
signiﬁcant ﬁgures in the result then requires 20 + d + e ﬁgures in the
summands, where the number of states is of order 10e. See Figure 4
which shows a plot of the numerical sizes of ZK and the individual
terms in the sum for ZK (more precisely, the sum of absolute values of
the real part of terms in the sum for ZK) on a log scale, against s.
Figure 4. Relative sizes of ZK and its summands against s
Because of the very large numerical values of the quantum factorials,
despite the smaller sizes of terms in the sums (10100 versus 1026 in the
above example), it is necessary to be able to work with numbers with
large exponent (say 300) though maybe only 30 signiﬁcant ﬁgures. It is
very costly in time to use higher precision than absolutely necessary, so
some special routines were written to easily manipulate sum numbers
with large exponents, but (comparitively) not so high precision. For
example, calculating Z97 for all s using 30-digits precision took 596
seconds on a Pentium 600MHz computer but it takes 1740 seconds to
compute it for only one s using 80-digits precision!
62
Some computations of Ohtsuki series
Because of the large discrepancy in orders of magnitude of the in-
dividual terms and the total sum, which as can be see from Figure 4
only occurs for some values of s (near 0 and K), it is necessary for
those values of s to perform the computations with specially higher
precision. Therefore two diﬀerent routines were written, and used on
diﬀerent values of s. For details, see (Ja).
The result of these two factors is to practically limit the size of K
(though not the complexity of the knot, that is S and T, since the
diﬃculty in calculation is practically independent of S and T). For
M+
(( 3
2)) these techniques allow computation for all primes K less then
137 with a total running time less than 1.5 days (using a 586 1GHz
computer).
Knowing am,K for primes K = Ki ≥m + 2 determines λm mod-
ulo  Ki, according to their deﬁnition in (2) (recall that here H =
1). From Ohtsuki’s theorem, it is known that this class, as an in-
teger in [−1
2
 Ki, 1
2
 Ki], stabilizes as the number of primes used
increases. This gives an algorithm for obtaining (the ﬁrst few terms
in) Ohtsuki series. The practical limitation on K above gives a lim-
itation on how many terms can be calculated. The full implemen-
tation of this algorithm for our manifolds M±
(( S
T )) can be found at
http://www.ma.huji.ac.il/~ruthel/nori/index.html.
