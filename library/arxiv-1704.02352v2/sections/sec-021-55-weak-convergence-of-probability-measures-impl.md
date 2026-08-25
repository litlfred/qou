---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-021-55-weak-convergence-of-probability-measures-impl
section_title: "Weak convergence of probability measures implies uniform convergence of densities"
section_number: 5.5
pages: 38-39
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
vergence of densities. For ǫ > 0 and u0 ∈ R let φǫ : R → R+ be a function
on the real line such that φǫ is supported on an ǫ-neighborhood of u0 and∫
φǫ(u) du = 1. Since EfΛ n is Lipschitz with constant 1, it follows that
(5.6)
⏐
⏐
⏐
⏐EfΛ n(u0) −
∫
φǫ(u) d EPΛ n(u)
⏐
⏐
⏐
⏐ =
⏐
⏐
⏐
⏐
∫
φǫ(u)
(
EfΛ n(u0) − EfΛ n(u)
)
du
⏐
⏐
⏐
⏐ ≤
∫
φǫ(u)
⏐
⏐EfΛ n(u0) − EfΛ n(u)
⏐
⏐ du ≤ ǫ.
By weak convergence of probability measures, the integral o n the left-hand
side converges, as n → ∞ , to
∫
φǫ(u) d PΛ ∞(u). By passing to the limit,
the above inequality implies therefore that
lim sup
n→∞
⏐
⏐
⏐
⏐EfΛ n(u0) −
∫
φǫ(u) d PΛ ∞(u)
⏐
⏐
⏐
⏐ ≤ ǫ.
Since this inequality holds true for arbitrary ǫ > 0, it follows that the se-
quence EfΛ n(u0) is a Cauchy sequence, hence it converges to a ﬁnite limit
which will be denoted by fΛ ∞(u0). In other words, we have proved that the
functions EfΛ n converge pointwise to the function fΛ ∞; since all functions
EfΛ n are Lipschitz with the same constant, the convergence is uniform on a
compact set K = [−R, R] for arbitrary value of R.
On the other hand, inequalities (5.2) show that the distance between EfΛ n
and fΛ ∞ with respect to the supremum norm on the set K c = R \ K is
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 39
bounded by
(5.7) ‖EfΛ n − fΛ ∞‖L∞[K c] ≤ 2
√
R2 + 4 + |R|
.
Since the right-hand side converges to zero as R → ∞ , it follows that the
sequence of functions EfΛ n converges to fΛ ∞ uniformly on the whole real
line R.
To conclude, we proved the following theorem which might be o f inde-
pendent interest.
Theorem 5.1. Let (Λ n) be a sequence of random anisotropic Young dia-
grams, each with the unit area. Let (PΛ n) be the corresponding sequence
of random probability measures on R with densities (fΛ n) as in Section 5.1.
Assume that the sequence of probability measures (EPΛ n) converges to
some limit in the weak topology.
Then there exists a function fΛ ∞ such that EfΛ n → fΛ ∞ uniformly on R.
