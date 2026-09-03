---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
We consider the space of even rational functions of degree 2p
E2p
:=
(
R(z) = P(z)
Q(z)

 P(z) :=
p−1
X
k=0
bkz2(p−1−k) and Q(z) :=
p
X
k=0
akz2(p−k)
)
with positive real coeﬃcients ak, bk ∈R+ normalized by the condition a0 = ap = 1,
the space
E∞
:=
∞
[
p=1
E2p
of normalized even rational functions, and the set of 2p −1 parameters
P2p := {a1, · · · , ap−1; b0, · · · , bp−1}.
We describe an algorithm to determine, as a function of the parameter set P2p, a
closed-form expression of the integral
I
:=
Z ∞
0
R(z) dz
(1.1)
for a large class of functions R ∈E∞. The function R is called symmetric if its
denominator Q satisﬁes Q(1/z) = z−2pQ(z). This is equivalent to its coeﬃcients
being palindromic, i.e. aj = ap−j for 1 ≤j ≤p.
The class of symmetric functions plays a crucial role in this algorithm. Deﬁne
Es
2p
:=
{R ∈E2p

 den(R) is symmetric}
(where den(R) denotes the denominator of R), the class of rational functions with
symmetric denominators of degree 2p, and
Es
∞
:=
∞
[
p=1
Es
2p.
Date: August 11, 2021.
1991 Mathematics Subject Classiﬁcation. Primary 33.
Key words and phrases. Rational functions, Landen transformation, Integrals.
The second author was supported in part by NSF Grant DMS-0070567.
1
2
GEORGE BOROS AND VICTOR H. MOLL
For m ∈N deﬁne
Em
2p
:=
{R ∈E∞

 (den(R))1/(m+1) is even, symmetric of degree 2p}
and Em,s
2p
:= Em
2p ∩Es
2p, so a function R ∈Em,s
2p
can be written in the form
R(z)
=
P(z)
Qm+1(z),
where P(z) is an even polynomial and Q(z) is an even symmetric polynomial of
degree 2p.
The method of partial fractions gives (in principle) the value of I in terms of
the roots of Q. Symbolic computations yield either a closed-form answer, an ex-
pression in terms of the roots of an associated polynomial, or the integral returned
unevaluated.
The algorithm described here allows only algebraic operations on elementary
functions and changes of variables of the same type. In particular, we exclude the
solution of algebraic equations of degree higher than 2. We say that a rational
function R ∈E∞is computable if its integral can be evaluated by our algorithm.
The ﬁrst step in the algorithm is to consider symmetric rational functions. In
Section 2 we prove a reduction formula, i.e. a map Fp : Es
2p →Rp that reduces the
computability of the integral of the symmetric function R to that of one of degree
1
2deg(R). Here Rp is the space of rational functions with denominator of degree p.
These new functions are not necessarily symmetric, and this is the main limitation
of our algorithm. The details of Fp require the evaluation of some binomial sums
which are presented in Appendix A. The classical Wallis’ formula
Z ∞
0
dz
(z2 + 1)m+1
=
π
22m+1
2m
m

shows that every R ∈Em
2 is computable. The reduction formula now implies that
every R ∈Em
4 is computable. This is described in Section 3. The computability of
R ∈E4 is also a consequence of the classical theory of hypergeometric functions;
the details are given in [2]. In Section 4 we compute the integral of every function
in Em,s
8
, where the reduction method expresses these integrals in terms of functions
in Em
4 . The algorithm does not, in general, provide a value for the integral of a
nonsymmetric function of degree 8.
The ﬁnal piece of the algorithm is described in Section 5: for R ∈E2p, the
symmetrization of its denominator produces a (symmetric) rational function in E4p
with the same integral as R. The reduction formula now yields a new function in
E2p with the same integral as R. We thus obtain a map T2p : E2p →E2p such that
Z ∞
0
R(z) dz
=
Z ∞
0
T2p(R(z)) dz.
(1.2)
In particular, the class of computable rational functions of degree 2p is invariant
under forward and backward iteration of T2p. This map is the rational analog of
the original Landen transformation for elliptic integrals described in [4, 13]. The
map T2p can also be interpreted as a map on the coeﬃcients Φ2p : O+
2p →O+
2p
where O+
2p = R+
p−1 × R+
p.
LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS
3
The case of Φ6 is described in detail in Section 6 and is given explicitly by
a1
→
9 + 5a1 + 5a2 + a1a2
(a1 + a2 + 2)4/3
(1.3)
a2
→
a1 + a2 + 6
(a1 + a2 + 2)2/3
b0
→
b0 + b1 + b2
(a1 + a2 + 2)2/3
b1
→
b0(a2 + 2) + 2b1 + b2(a1 + 3)
a1 + a2 + 2
b2
→
b0 + b2
(a1 + a2 + 2)1/3 .
Let x0 := (a1, a2; b0, b1, b2). Then Φ6 : O+
6 →O+
6 is iterated to produce a sequence
xn+1 := Φ6(xn) of points in O+
6 that yield a sequence of rational functions with
constant integral. We have proved in [3] the existence of L ∈R+, depending upon
the initial point x0 = (a1, a2; b0, b1, b2), such that xn →(3, 3; L, 2L, L). Thus
Z ∞
0
b0z4 + b1z2 + b2
z6 + a1z4 + a2z2 + 1 dz
=
L(x0) × π
2 .
(1.4)
This establishes a numerical method to compute the integral in (1.4).
Numerical studies on integrals of even degree 2p suggest the existence of a lim-
iting value L = L(x0) such that the sequence xn := Φ2p(xn) satisﬁes
xn
→
p
1

,
p
2

, · · · ,

p
p −1

;
p −1
0

L,
p −1
1

L, · · · ,
p −1
p −1

L

.
The integral of the original rational function is thus
π
2 × L(x0).
The proof of
convergence remains open for p ≥4. Examples are given in Section 7.
The most important issues left unresolved in this paper are the convergence of
the iteration of the map Φ2p discussed above and the geometric interpretation of the
Landen transformation T2p. Finally, the question of integration of odd functions
has not been addressed at all.
Some history. The problem of integration of rational functions R(z) = P(z)/Q(z)
was considered by J. Bernoulli in the 18th century.
He completed the original
attempt by Leibniz of a general partial fraction decomposition of R(z). The main
diﬃculty associated with this procedure is to obtain a complete factorization of
Q(z) over R. Once this is known the partial fraction decomposition of R(z) can be
computed. The fact is that the primitive of a rational function is always elementary:
it consists of a new rational function (its rational part) and the logarithm of a second
rational function (its transcendental part). In his classic monograph [9] G. H. Hardy
states: The solution of the problem (of deﬁnite integration) in the case of rational
functions may therefore be said to be complete; for the diﬃculty with regard to the
explicit solution of algebraical equations is one not of inadequate knowledge but of
proved impossibility. He goes on to add: It appears from the preceding paragraphs
that we can always ﬁnd the rational part of the integral, and can ﬁnd the complete
integral if we can ﬁnd the roots of Q(z) = 0.
4
GEORGE BOROS AND VICTOR H. MOLL
In the middle of the last century Hermite [10] and Ostrogradsky [15] developed
algorithms to compute the rational part of the primitive of R(z) without factor-
ing Q(z). More recently Horowitz [11] rediscovered this method and discussed its
complexity. The problem of computing the transcendental part of the primitive
was ﬁnally solved by Lazard and Rioboo [12], Rothstein [17] and Trager [18]. For
detailed descriptions and proofs of these algorithms the reader is referred to [5] and
[6].
