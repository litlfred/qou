---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-068-symmetric-functions
section_title: "Symmetric functions"
section_number: null
pages: 451-453
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Theorem 10.38 and Corollary 10.41 in Chapter 10 imply that the asymptotic
contribution of a minimal arrangement point is unchanged when the factors in
the denominator are replaced by their ﬁrst-order terms.
Problem 13.7. Let Q(z) be any polynomial in d variables and letp be a zero
of Q such that the homogeneous part H(z) of Q atp (in the sense of Deﬁni-
tion 6.46) factors into k < d linearly independent factors. Under what condi-
tions is the dominant asymptotic contribution ofp to the series coeﬃcients of
1/Q(z) the same as the dominant asymptotic contribution of p to the series
coeﬃcients of 1/H(z)?
An approach to Problem 13.7 is provided by a series of results in [BP11].
Lemma 2.24 of that paper shows that in the interior of the normal cone at
p, the function 1 /Q(z) can be expanded in negative powers of H(z), while
Lemma 6.3 there shows that the Cauchy integral for the leading negative power
is the inverse Fourier transform. These results are stated for points with speciﬁc
types of local factorizations, but in fact appear to be much more general. As
summarized in Chapter 11 of this text, the construction of a conical contour,
and the error estimates that follow, rely only on the direction ˆ r being non-
obstructed. In fact the types of local divisors allowed are Lorentzian quadratics
and smooth divisors, which as a degenerate case (having no quadratics) include
arrangement points. Thus, solving Problem 13.7 for a large class of functions
should be possible by an application of the results in [BP11].
Some caution is indicated due to the asymptotics for two smooth tangential
divisors, worked out in a special case in Proposition 10.68, and the fact that
asymptotics for the square of a single smooth divisor are a special case but do
not capture the results of Proposition 10.68 in general. The diﬃculty here may
be traced back to the fact that the expansion in [BP11, Lemma 2.24] only holds
in the interior of a cone where the homogeneous part does not vanish; because
two tangential curves cannot be separated by a cone, the expansion does not
hold near where Q vanishes.
13.7 Symmetric functions
Multivariate generating functions often possess some degree of symmetry. For
example, the denominators in the Delannoy generating function, the cube grove
generating function, the Friedrichs–Lewy–Szeg ˝o generating function, and the
Gillis–Reznick–Zeilberger generating functions are all symmetric polynomi-
als. The denominator in the Aztec Diamond generating function is symmetric
in two of its variables.
434 Challenges and extensions
A symmetric function Q always has critical points in the main diagonal
direction, since ∇log Q(z) ‖ 1 wheneverz = (w,..., w) and w is a root of
the univariate polynomial Q(z,..., z). When Q is symmetric and multi-aﬃne,
meaning Q has degree 1 in each variable, then there must be a minimal critical
point.
Theorem 13.8 ([Bar+18, Lemma 15]) . Let Q be a multi-a ﬃne elementary
symmetric function and let δQ denote the univariate diagonalization δQ(z) :=
Q(z,..., z). If w is a root ofδQ of minimal modulus then(w,..., w) is a minimal
point for Q in the main diagonal direction.
Proof Denote the roots ofδQ byα1,...,α k, where|α1| is a root of least mod-
ulus, and let
M(z) =
k∏
j=1
(z j−α j).
For any ε > 0, the polynomial M has no zeros in the polydisk D centered at
the origin whose radii are all|α1|− ε. For any d-variable polynomial P, denote
its symmetrization by
P∗(z) := 1
d!
∑
π∈Sd
P(zπ(1),..., zπ(d)
) .
Then M∗ = Q and the Borcea–Br ¨and´en symmetrization lemma [BB09, The-
orem 2.1] implies that Q has no zeros in the polydisk D. Because ε >0 was
arbitrary, we conclude that (α1,...,α 1) is a minimal point of Q. □
Exercise 13.3. In d variables, the jth elementary symmetric function is the
polynomial
e j(z) =
∑
S∈E j
∏
i∈S
zi,
whereE j consists of all subsets of{1,..., d} with j elements. Use Theorem 13.8
to ﬁnd minimal points for the following denominators without resorting to ge-
ometric arguments.
(a) In 2 variables, Q(x, y) = 1− e1(x, y)− e2(x, y) (the Delannoy generating
function).
(b) In 3 variables, Q(x, y, z) = 3− e1(x, y, z)− e2(x, y, z) + 3e3(x, y, z) (the cube
grove generating function).
(c) In 4 variables, Q(z) = 1− e1(z) + 27e4(z) (the GRZ generating function
with critical parameter).
