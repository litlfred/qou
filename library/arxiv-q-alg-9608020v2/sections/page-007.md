---
doc_id: arxiv-q-alg-9608020v2
doc_title: "Shifted Jack polynomials, binomial formula, and applications"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 9608020v2.pdf
source_sha256: 727268098db7f23d
toc_source: undetermined
doc_brief: "Shifted Jack polynomials, binomial formula, and applications — In this note we prove an explicit binomial formula for Jack polynomials and discuss some applications of it. 1."
---
SHIFTED JACK POLYNOMIALS, BINOMIAL FORMULA, AND APPLICATIONS
7
Lemma.
(5.3)
(
X
xi −|µ|)P ∗
µ(x; θ) =
X
|λ|=|µ|+1
θ-dim λ/µ P ∗
λ(x; θ) .
Proof. Let f be the diﬀerence of the LHS and RHS in (5.3). By (2.3) and (5.1) we
have deg f ≤|µ|. One easily checks that f(ν) = 0 for all |ν| ≤|µ|. It follows that
f = 0.
□
Applying this lemma k times, where k = |λ| −|µ|, we obtain
(5.4) (
X
xi −|µ|) · · · (
X
xi −|µ|−k +1)P ∗
µ(x; θ) =
X
|ν|=|µ|+k
θ-dim ν/µ P ∗
ν (x; θ) .
Evaluation of (5.4) at x = λ gives
(5.5)
(|λ| −|µ|)! P ∗
µ(λ) = θ-dim λ/µ P ∗
λ(λ) .
In particular, for µ = ∅one has
(5.6)
|λ|! = θ-dim λ P ∗
λ(λ) .
Dividing (5.5) by (5.6) we obtain (5.2).
□
6. Integral representation of Jack polynomials. Write ν ≺λ if
λ1 ≥ν1 ≥λ2 ≥ν2 ≥· · · ≥νn−1 ≥λn .
For any number r set (t)r = Γ(t + r)/Γ(t). We have (see [M], VI.7.13′)
(6.1)
Pλ(x1, . . ., xn; θ) =
X
ν≺λ
ψλ/νPν(x1, . . ., xn−1)x|λ/ν|
n
,
where
(6.2)
ψλ/ν =
Y
i≤j≤n−1
(νi −λj+1 + θ(j −i) + 1)θ−1(λi −νj + θ(j −i) + 1)θ−1
(λi −λj+1 + θ(j −i) + 1)θ−1(νi −νj + θ(j −i) + 1)θ−1
.
Suppose µ has less than n parts. The formulas (3.2) and (6.1) together imply
(6.3)
P ∗
µ(λ) =
(nθ)µ
((n −1)θ)µ
X
ν≺λ
ψλ/ν
Pν(1, . . ., 1)
Pλ(1, . . ., 1) P ∗
µ(ν)
where 1 is repeated n times in the denominator and (n−1) times in the numerator.
Note that after substitution of (6.2) and of (3.1) rewritten as
(6.4)
Pλ(1, . . ., 1) =
Y
i<j≤n
(λi −λj + θ(j −i))θ
Y
i≤n
Γ(θ)/Γ(θi)
the formula (6.3) becomes the formula (7.16) from [Ok3]. We replace λ and µ in
(6.3) by their multiples κλ and κµ and let κ →∞. By (2.3)
P ∗
µ(κλ)/κ|µ| →Pµ(λ) ,
κ →∞.
Introduce the following product of beta-functions
C(µ, n) =
Y
i≤n−1
B(µi + (n −i)θ, θ) .
Set
Π(λ, ν; θ) =
Y
i≤j
(λi −νj)θ−1 Y
i>j
(νj −λi)θ−1 .
Using the well known relation (t)θ/tθ →1, t →∞, one obtains from (6.3) the
following
