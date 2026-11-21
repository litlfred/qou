---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-023-estimate-of-a-solution-of-36
section_title: "Estimate of a solution of (36)"
section_number: null
pages: 56-58
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Estimate of a solution of (36)
In this section, we explain how to estimate a solution in 2-variable case. We explain it
for a solution of (36); we can estimate solutions in other 2-variable cases in similar ways.
As mentioned in Section 3.2, there are exactly two solutions of (36). We put wmax to
be w of the solution whose w is the larger one. As we mentioned in Remark 3.2, we give
a rigorous proof of an estimate of wmax in the following lemma.
Lemma A.2. wmax ≤0.94.
Proof. The system of equations (36) is rewritten
{
Λ(w −2s) + Λ(s) −1
2ςR = 0,
2 Λ′(w −2s) = Λ′(s).
Since Λ′(t) = −log 2 sin πt, the second equation is rewritten
2 sin2 π(w −2s) = sin πs.
56
We put t = w −s −u = w −2s.
Since 0.03 ≤t ≤0.4 as shown in Section 3.2,
sin π(w −2s) > 0. Therefore,
sin π(w −2s) =
√
1
2 sin πs ,
and
w = 2s + 1
π arcsin
√
1
2 sin πs .
We put the right-hand side of this formula to be f(s), that is, w = f(s).
In order to transform a range of s to a range of w later, we show that f(s) is mono-
tonically increasing in an area where we consider a solution, as follows. We put
F(w, s) = 2 sin2 π(w −2s) −sin πs.
Since F(w, s) = 0,
d
dsF
(
f(s), s
)
= ∂F
∂w · f ′(s) + ∂F
∂s
= 0.
Hence, since
∂F
∂w = 4π sin π(w−2s) cos π(w−2s) = 2π sin 2π(w−2s),
∂F
∂s
= −4π sin 2π(w−2s) −π sin πs,
we have that
f ′(s) = −
∂F
∂w
∂F
∂s
= 2 +
cos πs
2 sin 2π(w−2s) = 2 + cos πs
2 sin 2πt > 0,
where we obtain the last inequality since 0.001 ≤s ≤0.5 and 0.03 ≤t ≤0.4 as shown in
Section 3.2. Therefore, f(s) is monotonically increasing in the area of such s and t.
We estimate a solution of (36) by rewriting it as a 1-variable equation, as follows. We
put
P(s) = Λ
(
f(s) −2s
)
+ Λ(s) −1
2ςR .
Then, (36) is rewritten as P(s) = 0. Since
P(0.346) = 0.0003872... > 0,
P(0.347) = −0.0002516... < 0,
a solution of P(s) = 0 is in the following range,
0.346 < s < 0.347.
Further, since f(s) is monotonically increasing, w of a solution of (36) is in the following
range
f(0.346) < wmax < f(0.347).
Therefore,
wmax < f(0.347) = 0.925927... < 0.94,
as required.
57
