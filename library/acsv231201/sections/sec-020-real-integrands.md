---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-020-real-integrands
section_title: "Real integrands"
section_number: null
pages: 109-115
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
91
Exercise 4.1. Explain why the term “stationary phase integral” is usually re-
served for k ≥2.
Exercise 4.2. Although Theorem 4.1 assumes k ≥2, the expansion for I+
given in part (i) by (4.1) holds when k = 1. What is ζ in the case k = 1 and
what expansion for I holds as a consequence?
To those unfamiliar with saddle point methods, this result may seem diﬃcult
to decipher, but both the statement and proof are actually quite intuitive. When
A and φ are real, their orders of vanishing dictate the order of magnitude of
such an integral after direct integration. Changing variables to simplify the ex-
ponent produces a full asymptotic development of the integral. When the phase
is complex, one can use integration by parts in order to cancel oscillations, or
one can reduce to the real case by a contour shift. The latter approach requires
stronger hypotheses (analyticity rather than smoothness) but gives stronger re-
sults (exponentially small remainders rather than rapidly decreasing remain-
ders). In order to give all of the intuition, we take a route to the derivation
that is longer than necessary. We begin with a stripped down special case, in
which direct integration suﬃces, then give the arguments that hold in greater
generality.
4.1 Real integrands
For univariate Fourier–Laplace integrals, Theorem 4.1 states the existence of
an asymptotic expansion
Z ε
0
A(x) exp(−λφ(x)) dx ≈
∞
X
j=ℓ
ajC(k, j)(ckλ)−(1+j)/k
with explicitly computable constants aj. The main result of this section, Theo-
rem 4.6, yields this expansion for real integrands, along with further informa-
tion about the constants.
Complex analytic techniques are not needed when working on the real line,
and consequently we need to assume only diﬀerentiability and not analyticity
of A and φ. We build the argument in three steps: ﬁrst taking A and φ to be
monomials, then taking φ to be a monomial but allowing A to be free, and
ﬁnally handling the general case. The ﬁrst step is accomplished via an exact
computation, the second via a remainder estimate, and the third with a change
of variables.
92
Fourier–Laplace integrals in one variable
A and φ are monomials
On the positive half-line, we can get away with a change of variables involv-
ing a fractional power. This allows us to handle the special case of monomial
phase and amplitude by an exact integral, holding for any positive real α and
nonnegative real β. The change of variables y = λxα gives
Z ∞
0
xβ exp(−λxα) dx =
Z ∞
0
 y
λ
β/α
e−y 1
α
y1/α−1
λ1/α dy
= 1
αλ−(1+β)/α
Z ∞
0
y
1+β
α −1e−y dy ,
so, by the deﬁnition of the Gamma function, we have the exact evaluation
Z ∞
0
xβ exp(−λxα) dx = C(α, β) λ−(1+β)/α
(4.3)
with C(α, β) = 1
αΓ
 1+β
α

as above.
Remark 4.2. All of the contribution to (4.3) comes from a neighborhood of
zero: for any ε > 0 the substitution w = λ(xα −εα) proves that the diﬀerence

Z ε
0
xβ exp(−λxα) dx −C(α, β) λ−(1+β)/α

 =
Z ∞
ε
xβ exp(−λxα) dx
= 1
αλ−(1+β)/αe−λεα Z ∞
0
(w + λεα)
1+β
α −1 e−w dw
= O

λ−(1+β)/αe−λεα
decays exponentially in λ. The fact that a Fourier–Laplace integral decays ex-
ponentially when integrated over a region where its phase does not vanish will
be used multiple times in this chapter.
Exercise 4.3. Suppose x has units of time (or length, or any other physical
unit). Explain the right-hand side of (4.3), except for the constant, via a soft
analysis: what are the free variables on the left, what units must λ have in order
to abide by the principle of unitless exponentiation, what units must the left-
hand side of (4.3) have (remembering to include the units of dx), and what
power must λ therefore be given on the right-hand side?
When β = ℓis an integer and α = 2k is an even integer the corresponding
two-sided integrals make sense as well, giving
Z ∞
−∞
xℓexp

−λx2k
dx =
( 2C(2k, ℓ) λ−(1+ℓ)/(2k)
if ℓis even
0
if ℓis odd
.
(4.4)
4.1 Real integrands
93
φ is a monomial and A is anything
Generalizing our argument to the case of general amplitude requires the fol-
lowing estimate.
Lemma 4.3 (Big-O Lemma). Let k, ℓ> 0 with k an integer. If A and φ are
real-valued functions such that A(x) = O

xℓ
and φ(x) ∼xk at x = 0, and φ(x)
vanishes in [0, ε] only at 0, then
Z ε
0
A(x) exp(−λφ(x)) dx = O

λ−(1+ℓ)/k
as λ →∞.
Proof
Pick any K > 0 such that |A(x)| ≤K|x|ℓon [0, ε]. Because φ(x) ∼xk
at x = 0, for any δ ∈(0, 1) there is some interval [0, ε′] with ε′ ≤ε such that
φ(x) ≥(1−δ)xk on [0, ε′]. Fixing any such δ and ε′, nonvanishing of φ on (0, ε]
implies that infε′≤x≤ε φ(x) is positive, hence the portion of the integral coming
from [ε′, ε] decays exponentially in λ. On [0, ε′],

Z ε′
0
A(x) exp(−λφ(x)) dx

 ≤K
Z ε′
0
xℓexp(−λ(1 −δ)xk) dx
≤K
Z ∞
0
xℓexp(−λ(1 −δ)xk) dx
= O

(λ(1 −δ))−(1+ℓ)/k
by (4.3)
= O

λ−(1+ℓ)/k
,
as desired.
□
For monomial phase functions and general amplitude functions, we now
have the following result.
Lemma 4.4. Suppose that A is a real function with
A(x) =
M−1
X
j=ℓ
bjx j + O(xM)
as x →0. Then
Z ε
0
A(x) exp(−λxk) dx =
M−1
X
j=ℓ
b jC(k, j)λ−(1+j)/k + O

λ−(1+M)/k
,
where C(k, j) = Γ((1 + j)/k)/k.
Remark. The hypothesis on A in Lemma 4.4 is quite weak. In particular, A
need not even be continuously diﬀerentiable, so it is useful for examples such
94
Fourier–Laplace integrals in one variable
as A(x) = x sin(x−1). If A is represented by an inﬁnite asymptotic series then an
asymptotic expansion for the integral follows by applying the lemma for each
M.
Proof
Multiply the estimate
A(x) −
M−1
X
j=0
b jx j = O(xM)
by exp(−λφ(x)) and integrate. Using Lemma 4.3 to bound the integral of the
right-hand side gives

I −
M−1
X
j=0
Z ε
0
bjx j exp(−λxk) dx

= O

λ−(1+M)/k
,
and applying (4.3) to each integral with monomial amplitude gives the desired
conclusion.
□
Exercise 4.4. Apply Lemma 4.4 with M = 1 to give an asymptotic estimate
with remainder for
Z 1
0
(1 + x sin(x−1))e−λx2/2 dx .
General A and φ
A change of variables reduces the general case to Lemma 4.4, although a bit of
care is required to ensure we understand the asymptotic series for the functions
involved in the change of variables.
Lemma 4.5. Let M ≥2 be an integer and suppose
y(x) = c1x + · · · + cM−1xM−1 + O(xM)
(4.5)
in a neighborhood of zero, where c1 , 0. Then there is a neighborhood of
zero on which y has a compositional inverse. The inverse function x(y) has an
expansion
x(y) = a1y + · · · + aM−1yM−1 + O(yM) ,
where each a j is a polynomial in c1, . . . , cj and c−1
1 .
Proof
Suppose that c1 = 1. From y = x + O(x2) we see that y ∼x at zero,
hence
x = y + O(x2) = y + O(y2).
Now let 2 ≤n < M and suppose inductively that x = y+a2y2 +· · ·+an−1yn−1 +
4.1 Real integrands
95
O(yn), where each coeﬃcient a j is a polynomial in c2, . . . , c j. Let a be an inde-
terminate, and substitute the value of y in (4.5) into the quantity
Φ(x, y) = x −(y + a2y2 + · · · + an−1yn−1 + ayn) .
The result Φ(x, y(x)) is a polynomial in x, whose coeﬃcients in degrees up to
n−1 vanish due to the induction hypothesis, plus a remainder of O(xM) coming
from our starting assumption. The coeﬃcient of the xn term may be written as
a −P(a2, . . . , an−1, c2, . . . , cn), where P is a polynomial. By induction, this is a
polynomial in c2, . . . , cn. Setting an = P(a2, . . . , an−1, c2, . . . , cn), we see that
x −y −
n
X
j=2
a jyj = O(xn+1) ,
completing the induction. When n = M −1, observing that O(xM) = O(yM)
completes the proof of the lemma for c1 = 1. For general c1 , 1 we can
use this argument to represent x as a function of y/c1, which shows that x =
PM−1
j=1 ajyj + O(yM) with each cj
1a j a polynomial in c2, . . . , c j.
□
Exercise 4.5. Write down the quadratic Taylor expansion (with remainder
term O(x3)) near zero for y = 1 −
√
1 −x and ﬁnd its compositional inverse.
Check your work afterward by computing x as a function of y explicitly.
We can now establish Theorem 4.1 for real integrands. Recall that for each
natural number M, a real function f is said to be of class CM or CM-smooth
if all derivatives of f up to and including order M are continuous; if this holds
for all M we say f belongs to C∞and is smooth.
Theorem 4.6. Let M be a positive integer and let k and ℓbe integers with
0 ≤k, ℓ≤M, and k ≥2. Suppose that A is a real function, and φ is a CM-
smooth real function, with series expansions
A(x) =
M−1
X
j=ℓ
bjx j + O

xM
φ(x) =
M+k−1
X
j=k
c jx j + O

xM+k
as x →0, where bℓ, ck , 0. Then I+(λ) =
R ε
0 A(x) exp(−λφ(x)) dx has the
asymptotic expansion
I+(λ) =
M−1
X
j=ℓ
a jC(k, j)(ck λ)−(1+ j)/k + O

λ−(1+M)/k
(4.6)
96
Fourier–Laplace integrals in one variable
as λ →∞, with C(k, j) = k−1Γ
 1+j
k

as above and the coeﬃcient aj given by
a polynomial in bℓ, . . . , bj and c−1
k , ck+1, . . . , ck+ j−ℓ. The ﬁrst two coeﬃcients in
this expansion are
aℓ= bℓ
aℓ+1 = bℓ+1 −bℓ
2 + ℓ
k
ck+1
ck
.
(4.7)
Proof
Applying the change of variables y = φ(x)1/k to
φ(x) = ckxk
 
1 + ck+1
ck
x + · · · + cM+k−1
ck
xM−1 + O

xM!
shows that
y = c1/k
k x
 
1 + ck+1
ck
x + · · · + cM+k−1
ck
xM−1 + O

xM!1/k
,
(4.8)
and the binomial expansion for (1 + u)1/k gives
y = c1/k
k
M
X
j=1
djx j + O

xM+1
,
where each dj is a polynomial in ck+1, . . . , ck+j−1 and c−1
k .
By Lemma 4.5, the inverse function x = x(y) deﬁned by this equation satis-
ﬁes
x =
M
X
j=1
ej

y
c1/k
k

j
+ O

yM+1
,
(4.9)
where ej is a polynomial in ck+1, . . . , ck+j−1. A function of class CM with
nowhere vanishing derivative has an inverse of class CM, which justiﬁes term-
by-term diﬀerentiation and yields
x′(y) = c−1/k
k
M
X
j=1
je j

y
c1/k
k

j−1
+ O

yM
.
The change of variables formula gives
I+(λ) =
Z y(ε)
0
˜A(y) exp(−λyk) dy,
where ˜A(y) = A(x(y))x′(y). Plugging the series for x and x′ into the deﬁnition
of ˜A implies
˜A(y) = c−1/k
k
M−1
X
j=ℓ
˜bj

y
c1/k
k

j
+ O

yM
,
