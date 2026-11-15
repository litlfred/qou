---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-004-14-behavior-near-the-edge-of-the-spectrum-and-th
section_title: "Behavior near the edge of the spectrum and the Airy ensemble"
section_number: 1.4
pages: 6-7
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
discrete sine kernel S(k, a) vanishes if a ≥2. Therefore, it follows from Theorem 3
that the limit correlations lim ϱ(n, X(n)) vanish if ai ≥2 for some i. However, as
will be shown below in Proposition 4.1, after a suitable scaling near the edge a = 2,
the correlation functions ϱθ converge to the correlation functions given by the Airy
kernel [12, 36]
A(x, y) = A(x)A′(y) −A′(x)A(y)
x −y
.
ASYMPTOTICS OF PLANCHEREL MEASURES
487
Here A(x) is the Airy function:
A(x) = 1
π
Z ∞
0
cos
u3
3 + xu

du.
(1.15)
In fact, the following more precise statement is true about the behavior of the
Plancherel measure near the edge a = 2. By symmetry, everything we say about
the edge a = 2 applies to the opposite edge a = −2.
Consider the random point process on R whose correlation functions are given
by the determinants
ρAiry
k
(x1, . . . , xk) = det
h
A(xi, xj)
i
1≤i,j≤k,
and let
ζ = (ζ1 > ζ2 > ζ3 > . . . ) ∈R∞
be its random conﬁguration. We call the random variables ζi’s the Airy ensemble.
It is known [12, 36] that the Airy ensemble describes the behavior of the (properly
scaled) 1st, 2nd, and so on largest eigenvalues of a Gaussian random Hermitian
matrix.
The distribution of individual eigenvalues was obtained by Tracy and
Widom in [36] in terms of certain Painlev´e transcendents.
It has been conjectured by Baik, Deift, and Johansson that the random variables
eλ =

eλ1 ≥eλ2 ≥. . .

,
eλi = n1/3
 λi
n1/2 −2

,
converge, in distribution and together with all moments, to the Airy ensemble.
They veriﬁed this conjecture for individual distribution of λ1 and λ2 in [3] and [4],
respectively. In particular, in the case of λ1, this generalizes the result of [40, 42]
that
λ1
√n →2 in probability as n →∞. The computation of lim λ1
√n was known as
the Ulam problem; diﬀerent solutions to this problem were given in [1, 16, 32]; see
also the survey [2].
Convergence of all expectations of the form
* r
Y
k=1
∞
X
i=1
etkeλi
+
,
t1, . . . , tr > 0 ,
r = 1, 2, . . . ,
(1.16)
to the corresponding quantities for the Airy ensemble was established in [25]. The
proof in [25] was based on a combinatorial interpretation of (1.16) as the asymp-
totics in a certain enumeration problem for random surfaces.
In the present paper we use diﬀerent ideas to prove the following
Theorem 4. As n →∞, the random variables eλ converge, in joint distribution,
to the Airy ensemble.
This is done in Section 4 using methods described in the next subsection. The
result stated in Theorem 4 was independently obtained by K. Johansson in [17].
See, for example, [13] for an application of Theorem 4.
