---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-007-32-numerical-precision-and-summand-size
section_title: "Numerical precision and summand size"
section_number: 3.2
pages: 9-11
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
Since q-factorials can be numerically very large, the individual terms
in (3) can be many orders of magnitude larger than their sum and this
necessitates using very high precision arithmetic.
We give the example of K = 97 for the manifold M
+
((3
2 )) obtained
by surgery around the knot 52 (obtained from S =3 , T =2 , U =6 ) .
61
N. Jacoby & R. Lawrence
For s = 1, [90]! ≈ 10114 and the order of summands in ZK for s =2
is ∼ 1026, while their sum (Z97)i s∼ 106. To obtain an accuracy of d
signiﬁcant ﬁgures in the result then requires 20 + d + e ﬁgures in the
summands, where the number of states is of order 10 e. See Figure 4
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
example, calculating Z
97 for all s using 30-digits precision took 596
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
M
+
((3
2 )) these techniques allow computation for all primes K less then
137 with a total running time less than 1 .5 days (using a 586 1GHz
computer).
Knowing am,K for primes K = Ki ≥ m + 2 determines λm mod-
ulo ∏ Ki, according to their deﬁnition in (2) (recall that here H =
1). From Ohtsuki’s theorem, it is known that this class, as an in-
teger in [− 1
2
∏ Ki, 1
2
∏ Ki], stabilizes as the number of primes used
increases. This gives an algorithm for obtaining (the ﬁrst few terms
in) Ohtsuki series. The practical limitation on K above gives a lim-
itation on how many terms can be calculated. The full implemen-
tation of this algorithm for our manifolds M
±
(( S
T )) can be found at
http://www.ma.huji.ac.il/~ruthel/nori/index.html.
