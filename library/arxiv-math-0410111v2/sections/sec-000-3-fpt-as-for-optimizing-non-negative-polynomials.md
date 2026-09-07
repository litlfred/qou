---
doc_id: arxiv-math-0410111v2
doc_title: "Integer Polynomial Optimization in Fixed Dimension Jesús A. De Loera University of California, Dept. of Mathematics, Davis CA 95 616, USA email: deloera@math.ucdavis.edu http://www"
section_id: sec-000-3-fpt-as-for-optimizing-non-negative-polynomials
section_title: "FPT AS for Optimizing Non-Negative Polynomials over Inte ger Points of Polytopes"
section_number: 3
pages: 2-6
source_pdf: 0410111v2.pdf
source_sha256: 0ccaeeabd8de6b5f
doc_brief: "Integer Polynomial Optimization in Fixed Dimension Jesús A. De Loera University of California, Dept. of Mathematics, Davis CA 95 616, USA email: deloera@math.ucdavis.edu http://www.math.ucdavis.edu/~d"
---
Consider now a polynomial function f ∈ Z[x1, x2, . . . , xd] of maximum total degree D and a convex
polytope P = {x|Ax ≤ b} where A is an m × d integral matrix and b is an integral m-vector. The purpose
of this section is to present an algorithm to generate lower and uppe r bounds Lk, Uk to the integer global
optimum value of
maximize f (x1, . . . , xd) subject to ( x1, . . . , xd) ∈ P ∩ Zd. (4)
J. A. De Loera, R. Hemmecke, M. K¨ oppe, R. W eismantel: Integer Polynomial Optimization in Fixed Dimension
Mathematics of Operations Research xx(x), pp. xxx–xxx, c© 200x INFORMS 3
We should also remark that in our algorithm the polynomial objective f unction f can be arbitrary (e.g.
non-convex). As we have seen, the optimization problem is NP-hard already for two integer variables and
polynomials of degree four. Nevertheless we will see that, in ﬁxed dim ension and when f (x) ≥ 0 for all
x ∈ P , the algorithm gives a fully polynomial time approximation scheme or FP TAS. This means that, in
polynomial time on the input and (1 /ǫ), one can compute a (1 − ǫ)-approximation to the maximum. The
algorithm we present is based on A. Barvinok’s theory for encoding a ll the lattice points of a polyhedron
in terms of short rational functions. See [1, 2] for all details. Latt ice points are thought of as exponent
vectors of monomials. For example, z2
1z−11
2 encodes the lattice point (2 , −11). The set of lattice points is
represented by a Laurent polynomial: gP (z) =∑
α∈P ∩Zd zα. From Barvinok’s theory this exponentially-
large sum of monomials gP (z) can instead be written as a polynomial-size sum of rational function s
(assuming the dimension d is ﬁxed) of the form:
gP (z) =
∑
i∈I
Ei
zui
d∏
j=1
(1 − zvij )
, (5)
where I is a polynomial-size indexing set, and where Ei ∈ { 1, −1} and ui, vij ∈ Zd for all i and j. For
details see [2, 5, 6].
We need a way to encode via rational functions the values of the poly nomial f over all the lattice points
in a polytope. The key idea, ﬁrst introduced in Lemma 9 of [6] and gene ralized in [8], is that diﬀerential
operators associated to f can be used to compute a rational function representation of ∑
a∈P ∩Zd f (a)za.
The following Lemma recently appeared in [3]:
Lemma 3.1 Let gP (z) be the Barvinok representation of the generating function o f the lattice points of P .
Let f be a polynomial in Z[x1, . . . , xd] of maximum total degree D. We can compute, in time polynomial
on D and the size of the input data, a Barvinok rational function r epresentation gP,f (z) for the generating
function∑
a∈P ∩Zd f (a)za.
Proof. We give here the author’s original proof the lemma for D ﬁxed. The ﬁrst proof without this
assumption was recently given by A. Barvinok in [3].
We begin assuming f (z) = zr, the general case will follow from it: Consider the action of the diﬀer ential
operator zr ∂
∂zr
in the generating function gP (z) and on its Barvinok representation. On one hand, for
the generating function
zr
∂
∂zr
· gP (z) =
∑
α∈P ∩Zd
zr
∂
∂zr
zα =
∑
α∈P ∩Zd
αrzα.
On the other hand, by linearity of the operator, we have that in ter ms of rational functions
zr
∂
∂zr
· gP (z) =
∑
i∈I
Eizr
∂
∂zr
·


zui
d∏
j=1
(1 − zvij )

 .
Thus it is enough to prove that the summands of the expression abo ve can be written in terms of rational
functions computable in polynomial time. The standard quotient rule for derivatives says that
∂
∂zr


zui
d∏
j=1
(1 − zvij )

 =
( ∂z ui
∂zr
)∏ d
j=1(1 − zvij ) − zui( ∂
∂zr
∏ d
j=1(1 − zvij ))
∏ d
j=1(1 − zvij )2
.
We can expand the numerator as a sum of no more than 2 d monomials. This is a constant number
because d, the number of variables, is assumed to be a constant. This argume nt completes the proof of
our lemma when f (z) = zr.
For the case when f (z) is a general monomial, i.e. f (z) = c · zβ1
1 · . . . · zβd
d , then we can compute again
a rational function representation of gP,f (z) by repeated application of basic diﬀerential operators:
c
(
z1
∂
∂z1
) β1
· . . . ·
(
zd
∂
∂zd
) βd
· gP (z) =
∑
α∈P ∩Zd
c · αβzα.
4 J. A. De Loera, R. Hemmecke, M. K¨ oppe, R. W eismantel: Integer Polynomial Optimization in Fixed Dimension
Mathematics of Operations Research xx(x), pp. xxx–xxx, c© 200x INFORMS
Thus we require no more than O(Dd) repetitions of the single-variable case.
Finally, if we deal with a polynomial f of many monomial terms, we compute and add up all such
expressions that we get for each term of f (x) and obtain our desired short rational function representation
for the generating function for ∑
α∈P ∩Zd f (α)zα. Note that only polynomially many steps are needed
because d is ﬁxed and the largest number of possible monomials in f of degree s is
( d+s−1
d−1
)
, thus for
ﬁxed d we will do no more than O(Dd) repetitions of the monomial case. □
Now we are ready to present our algorithm to obtain bounds Uk, Lk that reach the optimum. Step 1 of
preprocessing is necessary because we rely on the elementary fac t that, for a collection S = {s1, . . . , sr}
of non-negative real numbers, maximum {si|si ∈ S} equals lim k→∞
k
√ ∑ r
j=1 sk
j .
Algorithm
Input: A rational convex polytope P ⊂ Rd, a polynomial objective f ∈ Z[x1, . . . , xd] of maximum total
degree D.
Output: An increasing sequence of lower bounds Lk, and a decreasing sequence of upper bounds Uk
reaching the maximal function value f ∗ of f over all lattice points of P .
Step 1. If f is known to be non-negative in all points of P , then go directly to Step 2. Else, solving 2 d
linear programs over P , we ﬁnd lower and upper integer bounds for each of the variables x1, . . . , xd. Let
M be the maximum of the absolute values of these 2 d numbers. Thus |xi| ≤ M for all i. Let C be the
maximum of the absolute values of all coeﬃcients, and r be the number of monomials of f (x). Then
L := −rCM D ≤ f (x) ≤ rCM D =: U,
as we can bound the absolute value of each monomial of f (x) by CM D. Replace f by ¯f (x) = f (x) − L ≤
U − L, a non-negative polynomial over P . Go to Steps 2, 3, etc. and return the optimal value of ¯f .
Trivially, if we ﬁnd the optimal value of ¯f over P we can extract the optimal value for f .
Step 2. Via Barvinok’s algorithm (see [1, 2, 3]), compute a short rational fun ction expression for the
generating function gP (z) = ∑
α∈P ∩Zd zα. From gP (z) compute the number |P ∩ Zd| = gP (1) of lattice
points in P in polynomial time.
Step 3. From the rational function representation gP (z) of the generating function ∑
α∈P ∩Zd
zα compute
the rational function representation of gP,f k(z) of ∑
α∈P ∩Zd f k(α)zα in polynomial time by application
of Lemma 3.1. We deﬁne
Lk := k
√
gP,f k (1)/gP,f 0(1) and Uk := k
√
gP,f k (1).
When ⌊Uk⌋ − ⌈Lk⌉ < 1 stop and return ⌈Lk⌉ = ⌊Uk⌋ as the optimal value.
End of Algorithm .
Lemma 3.2 The algorithm is correct.
Proof. Using the fact that the arithmetic mean of a ﬁnite set of nonnegativ e values is at most as big
as the maximum value, which in turn is at most as big as the sum of all valu es, we obtain the sequences
of lower and upper bounds, Lk and Uk, for the maximum:
Lk =
k
/radicaltp/radicalvertex/radicalvertex√
∑
α∈P ∩Zd
f (α)k
|P ∩ Zd| ≤ max{f (α) : α ∈ P ∩ Zd} ≤ k
√ ∑
α∈P ∩Zd
f (α)k = Uk.
Note that as s → ∞ , Lk and Uk approach this maximum value monotonously (from below and above,
respectively). Trivially, if the diﬀerence between (rounded) upper and lower bounds becomes strictly less
than 1, we have determined the value max {f (x) : x ∈ P ∩ Zd} = ⌈Lk⌉. Thus the algorithm terminates
with the correct answer. □
Theorem 1.1 will follow from the next lemma:
J. A. De Loera, R. Hemmecke, M. K¨ oppe, R. W eismantel: Integer Polynomial Optimization in Fixed Dimension
Mathematics of Operations Research xx(x), pp. xxx–xxx, c© 200x INFORMS 5
Lemma 3.3 Let f be a polynomial with integer coeﬃcients and maximum total de gree D. When the
dimension d is ﬁxed,
(i) the bounds Lk, Uk can be computed in time polynomial in k, the input size of P and f , and the
total degree D. The bounds satisfy the following inequality:
Uk − Lk ≤ f ∗ ·
(
k
√
|P ∩ Zd| − 1
)
.
(ii) In addition, when f is non-negative over P (i.e. f (x) ≥ 0 for all x ∈ P ), for k = (1 +
1/ǫ) log(|P ∩ Zd|), Lk is a (1 − ǫ)-approximation to the optimal value f ∗ and it can be computed
in time polynomial in the input size, the total degree D, and 1/ǫ. Similarly, Uk gives a (1 + ǫ)-
approximation to f ∗. Moreover, with the same complexity, one can also ﬁnd a feasi ble lattice
point that approximates an optimal solution with similar qu ality.
Proof. Part (i). From Lemma 3.1 on ﬁxed dimension d, we can compute gP,f =∑
α∈P ∩Zd f (α)zα as
a rational function in time polynomial in D, the total degree of f , and the input size of P . Thus, because
f k has total degree of Dk and the encoding length for the coeﬃcients of f k is bounded by k log(kC )
(with C the largest coeﬃcient in f ), we can also compute gP,f k =∑
α∈P ∩Zd f k(α)zα in time polynomial
in k, the total degree D, and the input size of P . Note that using residue techniques [3], we can evaluate
gP,f k (1) in polynomial time. Finally observe
Uk − Lk = k
√ ∑
α∈P ∩Zd
f k(α) −
k
√ ∑
α∈P ∩Zd f k(α)
|P ∩ Zd| =
k
√ ∑
α∈P ∩Zd f k(α)
|P ∩ Zd|
(
k
√
|P ∩ Zd| − 1
)
= Lk
(
k
√
|P ∩ Zd| − 1
)
≤ f ∗
(
k
√
|P ∩ Zd| − 1
)
.
Part (ii). Note that if
(
k
√
|P ∩ Zd| − 1
)
≤ ǫ then Lk is indeed a (1 − ǫ)-approximation because
f ∗ ≤ Uk = Lk + (Uk − Lk) ≤ Lk + f ∗
(
k
√
|P ∩ Zd| − 1
)
≤ Lk + f ∗ǫ.
Observe that φ(ǫ) := (1 + 1 /ǫ)/(1/ log(1 + ǫ)) is an increasing function for ǫ < 1 and lim ǫ→0 φ(ǫ) = 1,
thus φ(ǫ) ≥ 1 for 0 < ǫ ≤ 1. Hence, for all k ≥ log(|P ∩ Zd|) + log(|P ∩ Zd|)/ǫ ≥ log(|P ∩ Zd|)/ log(1 +
ǫ), we have indeed
(
k
√
|P ∩ Zd| − 1
)
≤ ǫ. Finally, from Lemma 3.1, the calculation of Lk for k =
log(|P ∩ Zd|) + log(|P ∩ Zd|)/ǫ would require a number of steps polynomial in the input size and 1 /ǫ. A
very similar argument can be written for Uk but we omit it here.
To complete the proof of part (ii) it remains to show that not only we a pproximate the optimal value
f ∗ but we can also eﬃciently ﬁnd a lattice point α with f (α) giving that quality approximation of f ∗.
Let k = (1 + 1 /ǫ) log(|P ∩ Zd|), thus, by the above discussion, Lk is an (1 − ǫ)-approximation to f ∗. Let
Q0 := [ −M, M ]d denote the box computed in Step 1 of the algorithm such that P ⊆ Q0. By bisecting
Q0, we obtain two boxes Q′
1 and Q′′
1 . By applying the algorithm separately to the polyhedra P ∩ Q′
1 and
P ∩ Q′′
1 , we compute lower bounds L′
k and L′′
k for the optimization problems restricted to Q′
1 and Q′′
1 ,
respectively. Because Lk
k is the arithmetic mean of f k(α) for α ∈ P ∩ Zd, clearly
min{L′
k, L′′
k} ≤ Lk ≤ max{L′
k, L′′
k}.
Without loss of generality, let L′
k ≥ L′′
k. We now apply the bisection procedure iteratively on Q′
k. After
d log M bisection steps, we obtain a box Q′
k that contains a single lattice point α ∈ P ∩ Q′
k ∩ Z d, which
has an objective value f (α) = L′
k ≥ Lk ≥ (1 − ǫ)f ∗. □
We remark that if we need to apply the construction of Step 1 of the algorithm because f takes negative
values on P , then we can only obtain an (1 − ǫ)-approximation (and (1 + ǫ)-approximation, respectively)
for the modiﬁed function ¯f in polynomial time, but not the original function f . We also emphasize that,
although our algorithm requires the computation of ∑
α∈P f q(α) for diﬀerent powers of f , these numbers
are obtained without explicitly listing all lattice points (a hard task), n or we assume any knowledge of
the individual values f (α). We can access the power means ∑
α∈P f q(α) indirectly via rational functions.
Here are two small examples:
6 J. A. De Loera, R. Hemmecke, M. K¨ oppe, R. W eismantel: Integer Polynomial Optimization in Fixed Dimension
Mathematics of Operations Research xx(x), pp. xxx–xxx, c© 200x INFORMS
Example 1, monomial optimization over a quadrilateral: The problem we consider is that of
maximizing the value of the monomial x3y over the lattice points of the quadrilateral
{(x, y)|3991 ≤ 3996 x − 4 y ≤ 3993, 1/2 ≤ x ≤ 5/2}.
It contains only 2 lattice points. The sum of rational functions enco ding the lattice points is
x2y1000
(1 − (xy999)−1) (1 − y−1) + xy
(1 − xy999) (1 − y−1) + xy
(1 − xy999) (1 − y) + x2y1000
(1 − (xy999)−1) (1 − y) .
In the ﬁrst iteration L1 = 4000 .50 while U1 = 8001. After thirty iterations, we see L30 = 7817 .279750
while U30 = 8000, the true optimal value.
Example 2, nvs04 from MINLPLIB: A somewhat more complicated example, from a well-known
library of test examples (see http://www.gamsworld.org/minlp/), is the problem given by
min 100
(
1
2 + i2 −
( 3
5 + i1
) 2) 2
+
( 2
5 − i1
) 2
s. t. i1, i2 ∈ [0, 200] ∩ Z.
(6)
Its optimal solution as given in MINLPLIB is i1 = 1, i2 = 2 with an objective value of 0 .72. Clearly, to
apply our algorithm from page 4 literally, the objective function need s to be multiplied by a factor of 100
to obtain an integer valued polynomial.
Using the bounds on i1 and i2 we obtain an upper bound of 165 · 109 for the objective function, which
allows us to convert the problem into an equivalent maximization proble m, where all feasible points have
a non-negative objective value. The new optimal objective value is 1 64999999999.28. Expanding the new
objective function and translating it into a diﬀerential operator yie lds
4124999999947
