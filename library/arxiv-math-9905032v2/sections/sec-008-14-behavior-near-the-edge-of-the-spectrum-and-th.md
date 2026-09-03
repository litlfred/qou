---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-008-14-behavior-near-the-edge-of-the-spectrum-and-th
section_title: "Behavior near the edge of the spectrum and the Airy en-"
section_number: 1.4
pages: 8-10
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
semble. The discrete sine kernel S(k, a) vanishes if a ≥ 2. Therefore,
it follows from Theorem 3 that the limit correlations lim ̺(n, X(n))
vanish if ai ≥ 2 for some i. However, as will be shown below in Propo-
sition 4.1, after a suitable scaling near the edge u = 2, the correlation
functions ̺θ converge to the correlation functions given by the Airy
kernel [11, 32]
A(x, y) = A(x)A′(y) − A′(x)A(y)
x − y .
ASYMPTOTICS OF PLANCHEREL MEASURES 9
Here A(x) is the Airy function:
A(x) = 1
π
∫ ∞
0
cos
(u3
3 + xu
)
du.(1.15)
In fact, the following more precise statement is true about t he behav-
ior of the Plancherel measure near the edge u = 2. By symmetry,
everything we say about the edge u = 2 applies to the opposite edge
u = −2.
Consider the random point process on R whose correlation functions
are given by the determinants
ρAiry
k (x1, . . . , xk) = det
[
A(xi, xj)
]
1≤i,j ≤k
and let
ζ = (ζ1 > ζ 2 > ζ 3 > . . . ) ∈ R∞
be its random conﬁguration. We call the random variables ζi’s the Airy
ensemble. It is known [11, 32] that the Airy ensemble describes the be-
havior of the (properly scaled) 1st, 2nd, and so on largest ei genvalues
of a Gaussian random Hermitian matrix. The distribution of i ndivid-
ual eigenvalues was obtained by Tracy and Widom in [32] in ter ms of
certain Painlev´ e transcendents.
It has been conjectured by Baik, Deift, and Johansson that th e ran-
dom variables
~λ =
(
~λ1 ≥~λ2 ≥ . . .
)
, ~λi = n1/ 3
( λi
n1/ 2 − 2
)
converge, in distribution and together with all moments, to the Airy
ensemble. They veriﬁed this conjecture for individual dist ribution of
λ1 and λ2 in [2] and [3], respectively. In particular, in the case of λ1,
this generalizes the result of [36, 38] that λ 1√n → 2 in probability as
n → ∞. The computation of lim λ 1√n was known as the Ulam problem;
diﬀerent solutions to this problem were given in [1, 14, 29].
Convergence of all expectations of the form
⟨ r∏
k=1
∞∑
i=1
etk~λ i
⟩
, t 1, . . . , tr > 0 , r = 1, 2, . . . ,(1.16)
to the corresponding quantities for the Airy ensembles was e stablished
in [23]. The proof in [23] was based on a combinatorial interp retation of
(1.16) as the asymptotics in a certain enumeration problem f or random
surfaces.
In the present paper we use diﬀerent ideas to prove the follow ing
