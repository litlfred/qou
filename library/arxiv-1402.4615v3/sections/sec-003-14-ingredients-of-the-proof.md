---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-003-14-ingredients-of-the-proof
section_title: "Ingredients of the proof"
section_number: 1.4
pages: 7-10
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
results. The proof of Theorem 1.1 is easier than the proof of t he ﬂuctuation result,
so we will focus here on the second and compare it to the work of Ivanov, Kerov
and Olshanski.
8 M. DOŁ ˛ EGA AND V . FÉRAY
Remark. While beautiful and elementary, Hora’s proof of the centrallimit theorem
for characters in the case α = 1 seems very hard to be generalized for a generic
value of α as it relies from the beginning on the representation-theor etical back-
ground.
1.4.1. Polynomial functions. A central idea in the paper [IO02] is to consider char-
acters as functions on all Young diagrams by deﬁning:
Ch(1)
µ (λ) =



|λ|(|λ| − 1) · · · (|λ| − |µ| + 1)
χλ
µ 1|λ|−|µ|
dim(λ) if |λ| ≥ | µ|
0 if |λ| < |µ|.
In Sections 1-4 of paper [IO02], the authors prove that the functions Ch(1)
µ span lin-
early a subalgebra of the algebra of functions on all Young diagrams, give several
equivalent descriptions of this subalgebra and describe co mbinatorially the prod-
uct Ch(1)
µ Ch(1)
ν (Ch(1)
µ is denoted by p#
µ in [IO02]). This subalgebra is called the
algebra of polynomial functions on the set of Young diagrams (see also [KO94])
and denoted here by Λ (1)
⋆ .
In the general α-case, one can deﬁne a deformation of the function above as fol-
lows: for an integer partitionµ, denote |µ| its size, ℓ(µ) its length, mi(µ) its number
of parts of µ equal to i and zµ the standard numerical factor∏
i imi(µ)mi(µ)!. We
deﬁne
Ch(α)
µ (λ) =
{
α− |µ|−ℓ(µ)
2
(|λ|−|µ|+m1(µ)
m1(µ)
)
zµ θ(α)
µ,1|λ|−|µ|(λ) if |λ| ≥ | µ|;
0 if |λ| < |µ|.
While Jack characters have been studied for a long time, the idea, due to Lassalle,
to look at them as a function of λ as above is quite recent [Las08, Las09]. Among
other things, he proved that, as in the caseα = 1, the functions Ch(α)
µ span linearly
a subalgebra of functions on all Young diagrams, which has a nice characterization:
we present these results in Section 2, see in particular Prop osition 2.9. This sub-
algebra is called algebra of α-polynomial functions on the set of Young diagrams
(see also [KO94]) and denoted here by Λ (α)
⋆ .
As a function onall Young diagrams,Ch(α)
µ can be restricted to diagrams of size
n and hence considered as a random variable in our problem. It f ollows directly
from equation (7) that
(8) EP(α)
n
(Ch(α)
µ ) =
{
n(n − 1) · · · (n − k + 1) if µ = 1 k for some k ≤ n,
0 otherwise.
Throughout the paper, we shall use the standard notation(n)k for the falling facto-
rial n(n − 1) · · · (n − k + 1).
1.4.2. Moment method and structure constants. Another idea in paper [IO02] is to
use the method of moments and thus to compute asymptotically (for h ≥ 1)
EP(1)
n
(
Ch(1)
(k)(λ(n))h)
.
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 9
Recall that the algebra Λ (1)
⋆ has a linear basis given by the family of normalized
characters
(
Ch(1)
µ
)
µ
. As the expectation of Ch(1)
µ (λ(n)) is particularly simple –
see equation (8) –, one can compute expectation of
(
Ch(1)
(k)
) h by expanding it on
the basis Ch(1)
µ of Λ (1)
⋆ .
To do this, the authors of [IO02] need to understand how a product Ch(1)
ν Ch(1)
ρ
expands on the Ch(1)
µ basis, that is they need to study the structure constants of
this basis. They provide a combinatorial description of the se structure constants
[IO02, Proposition 4.5]. Unfortunately, this combinatorial description relies on the
representation-theoretical interpretation of θ(1)
ρ (λ) and has a priori no extension to
a general value of α.
To overcome this difﬁculty, we prove that the structure cons tants of the Ch(α)
µ
basis depends polynomially on the auxiliary parameter γ = √
α−1 − √α. This
is a non-trivial result and has other interesting applications than the study of large
Young diagrams under Jack measure. Therefore, we think that it may be on inde-
pendent interest and present it in details in Section 1.5 as our second main result.
Our polynomiality result for structure constants (Theorem 1.4) allows us to
show that some properties proved combinatorially in the cas e α = 1 still holds
in the general α-case (we will also rely on the case α = 2 , which also has some
representation-theoretical background, and use polynomial interpolation). Our re-
sult gives a good estimate of moments of Ch(α)
(k) of order at most 4 (but not of any
order). Therefore, we can not conclude with the moment method. To overcome that
difﬁculty, we have to use another ingredient in our proof: th e multivariate Stein’s
method.
1.4.3. Multivariate Stein’s method and Fulman’s construction.Stein’s method is a
classical method in probability to prove convergence in distrbution towards Gauss-
ian or Poisson distribution, together with bounds on the speed of convergence ; see
the monograph of Stein [Ste86]. To use it, one needs to construct an exchangeable
pair for the relevant random variable. But, when this pair is cons tructed, one can
prove Gaussian ﬂuctuations, using only bounds on (mixed con ditional) moments
of order at most 4 (while the moment method requires control on moments of all
order).
In the framework of Jack characters, an exchangeable pair has already been built
by Fulman to prove a ﬂuctuation result for Ch(α)
(2) . The same construction extends
to Ch(α)
(k), but the analysis of the ﬁrst moments becomes more tricky, re quires new
ideas and heavily relies on our polynomiality result for structure constants.
Let us note that, unlike Fulman’s result, our result is a result of convergence in
distribution of vectors of random variables. Therefore we need to use a multivariate
analog of Stein’s classical theorem. The one recently estab lished by Reinert and
Röllin [RR09] turns out to be suitable for our purpose.
10 M. DOŁ ˛ EGA AND V . FÉRAY
