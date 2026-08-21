---
doc_id: arxiv-q-alg-9608020v2
doc_title: "Shifted Jack polynomials, binomial formula, and applications"
section_id: sec-002-2-shifted-jack-polynomials-s1oook1ksok3-denote-b
section_title: "Shifted Jack polynomials ( [S1,OO,Ok1,KS,Ok3]). Denote by Λ θ (n) the al-"
section_number: 2
pages: 2-3
source_pdf: 9608020v2.pdf
source_sha256: 727268098db7f23d
doc_brief: "Shifted Jack polynomials, binomial formula, and applications — In this note we prove an explicit binomial formula for Jack poly nomials and discuss some applications of it. 1."
---
gebra of polynomials f (x1,...,x n) that are symmetric in variables xi −θi. We
call such polynomials shifted symmetric . By (1.1) one has the Harish-Chandra
isomorphism
(2.1) D(n;θ) → Λ θ (n)
which takes an operator D ∈ D(n;θ) to the polynomial d ∈ Λ θ (n) such that
DP λ (x;θ) = d(λ)Pλ (x;θ).
If D is of order k then degd =k.
Let µ be a partition (also viewed as a diagram). Recall that for a sq uare s =
(i,j ) ∈µ the numbers
a(s) = µ i −j, a ′(s) = j − 1,
l(s) = µ ′
j −i, l ′(s) = i − 1,
are called arm-length, arm-colength, leg-length, and leg- colength respectively. Set
H(µ ) =
∏
s∈µ
(a(s) +θl (s) + 1).
According to a general result of S. Sahi [S1] there exists the unique polynomial
P ∗
µ (x;θ) in Λ θ (n) such that deg P ∗
µ ≤ |µ | and
P ∗
µ (λ;θ) =
{ H(µ ), λ =µ,
0, |µ | ≤ |λ|, µ ⁄=λ
Here we assume µ andλ have length ≤n. It is clear that the uniqueness of P ∗
µ (x,θ )
follows easily from its existence.
The polynomials P ∗
µ (x; 1) were studied in [OO] and [Ok1]. They are closely re-
lated to Schur polynomials and are called shifted Schur functions . In particular,
the Schur function sµ is the highest degree term of P ∗
µ (x; 1). Shifted Schur func-
tions have a very rich combinatorics and numerous applicati ons (such as Capelli-
type identities or asymptotic character theory, see [OO,Ok 1,N,Ok2] and references
therein).
For general θ, F. Knop and S. Sahi proved (see [KS], Theorem 5.2) that
(2.2) P ∗
µ (λ;θ) = 0, unless µ ⊂λ,
and that again ([KS], Corollary 4.7)
(2.3) P ∗
µ (x;θ) = Pµ (x;θ) + lower degree terms .
Their proof was based on diﬀerence equations for the polynom ial P ∗
µ (x;θ). For
θ = 1 these properties follow immediately from explicit formu las for P ∗
µ (x; 1).
Explicit formulas for the polynomials P ∗
µ (x;θ), which generalize explicit formulas
for shifted Schur functions, were found in [Ok3] (see, for ex ample, (2.4) below). In
SHIFTED JACK POLYNOMIALS, BINOMIAL FORMULA, AND APPLICATI ONS 3
particular, they provide an eﬀective proof of the existence ofP ∗
µ (x;θ) and a diﬀerent
proof of (2.2) and (2.3).
We call these polynomials shifted Jack polynomials . They are a degenerate case
of shifted Macdonald polynomials [Kn,S2,Ok3].
It easily follows from the deﬁnition that P ∗
µ (x;θ) are stable, that is
P ∗
µ (x1,...,x n, 0;θ) = P ∗
µ (x1,...,x n;θ)
providedµ has at most n parts. Hence, one can consider shifted Jack polynomials
in inﬁnitely many variables.
The following combinatorial formula for shifted Jack polynomials was proved in
[Ok3]. Let us call a tableau T on µ a reverse tableau if its entries strictly decrease
down the columns and weakly decrease in the rows. By T (s) denote the entry in
the square s ∈µ . We have
(2.4) P ∗
µ (x;θ) =
∑
T
ψ T (θ)
∏
s∈µ
(
xT (s) −a′(s) +θl ′(s)
)
,
where the sum is over all reverse tableaux on µ with entries in {1, 2,... } andψ T (θ)
is the same θ-weight of a tableau that enters the combinatorial formula f or ordinary
Jack polynomials (see [St] or [M],(VI.10.12))
(2.5) Pµ (x;θ) =
∑
T
ψ T (θ)
∏
s∈µ
xT (s).
The coeﬃcients ψ T (θ) are rational functions of θ.
