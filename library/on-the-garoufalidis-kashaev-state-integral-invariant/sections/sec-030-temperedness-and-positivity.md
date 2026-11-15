---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT"
section_id: sec-030-temperedness-and-positivity
section_title: "Temperedness and Positivity"
section_number: null
pages: 31-34
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
toc_source: outline
doc_brief: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT — 67 sections: Front matter; ACKNOWLEDGMENTS; ABSTRACT"
---
Temperedness and Positivity
While several known examples in [1, 14, 6] define versions of Ψ within the Schwartz
space, our function is generally a tempered distribution under a positivity constraint
on the angle parameters.
The Schwartz space S(Rn) (see [12] chapter 5, [16] chapter 1, and [17] chapter
5) consists of smooth functions whose derivatives decay faster than any polynomial.
These functions are ideal for Fourier analysis and serve as test functions for tempered
distributions.
The space is stable under differentiation and Fourier transform,
making it fundamental in analysis, quantum theory, and distribution theory.
Lemma 2. Let F be a local field (R or C). Then Ψa,c ∈S′(A), the space of tempered
distributions on the Gaussian group A, provided:
22
0 ≤˙a, ˙b, ˙c ≤1, with ˙a + ˙b + ˙c = 1.
(Here ˙b = 1 −˙a −˙c.) If all inequalities are strict, Ψa,c is locally integrable.
This positivity guarantees convergence of the state-integral and compatibility with
the Fourier analysis over A.
Proof. Check, under the hypotheses
0 ≤˙a, ˙b, ˙c ≤1, ˙a + ˙b + ˙c = 1,
the function in x
Ψa,c(α, x) =
1
α((1 −¨ax)¨c)
∥¨ax∥˙c
∥1 −¨ax∥1−˙a
has at worst polynomial growth at infinity and only mild (integrable or principal-
value) singularities, so defines a tempered distribution (see [11]).
1. Behavior as |x| →∞.
For large |x|, the norms give
∥¨ax∥˙c ∼|x|˙c, ∥1 −¨ax∥1−˙a ∼|x|1−˙a
where ∼denotes asymptotic equivalence up to bounded, smooth factors near the
limit in question. Hence
Ψa,c(α, x) ∼
|x|˙c
|x|1−˙a = |x|˙c+˙a−1 = |x|−˙b,
23
since ˙a + ˙b + ˙c = 1. Thus for 0 ≤˙b ≤1, Ψa,c(x) decays like |x|−˙b (or is bounded
if ˙b = 0). In particular it grows at most polynomially, so any pairing with a
Schwartz test-function at infinity converges.
2. Behavior near x = 0.
As x →0,
Ψa,c(α, x) ∼|x|˙c
1
= |x|˙c,
which is locally integrable for ˙c ≥0.
3. Behavior near the pole x = ¨a−1.
At x0 = ¨a−1 one has 1 −¨ax →0, so
Ψa,c(x) ∼
1
|x −x0|1−˙a.
• If 0 < ˙a < 1, then 1 −˙a < 1 and the singularity is integrable—so Ψ is
locally integrable there.
• If ˙a = 0, it is exactly a |x −x0|−1 singularity, which defines the principal-
value distribution p.v.
1
x−x0 (still tempered).
• If ˙a = 1, the exponent 1 −˙a vanishes and there is no singularity at all.
Putting these together:
• For any 0 ≤˙a, ˙b, ˙c ≤1 summing to 1, Ψa,c(x) has at worst polynomial growth
at infinity and at worst a |x −x0|−1 singularity; both of those are compatible
with being a tempered distribution.
24
• If in addition 0 < ˙a, ˙b, ˙c < 1, all exponents at 0, at infinity, and at the pole
lie strictly between −1 and +1, so Ψa,c is actually a locally integrable function
(hence defines a distribution by honest integration against test functions).
