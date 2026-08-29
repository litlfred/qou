---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-006-22-legendre-fenchel-transforms
section_title: "Legendre-Fenchel transforms"
section_number: 2.2
pages: 12-13
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
ties of the Legendre-Fenchel transform, a classical tool in large deviation theory (see
e.g. [DZ98, Section 2.2]) that we shall use a lot in this paper. The Legendre-Fenchel
transform is the following operation on (convex) functions:
Deﬁnition 2.5. The Legendre-Fenchel transform of a function η is deﬁned by:
F(x) = sup
h∈R
(hx− η(h)).
This is an involution on convex lower semi-continuous functions.
Assume that η is the logarithm of the moment generating series of a random vari-
able. In this case, η is a convex function (by Hölder’s inequality). Then F is always
non-negative, and the unique h maximizing hx− η(h), if it exists, is then deﬁned by
the implicit equation η′(h) = x (note that h depends on x, but we have chosen not to
write h(x) to make notation lighter). This implies the following useful identities:
F(x) = xh− η(h) ; F′(x) = h ; F′′(x) = h′(x) = 1
η′′(h).
Example 2.6. If η(z) = mz + σ2z2
2 (Gaussian variable with mean m and variance σ2),
then
h = x− m
σ2 ; FNR(m,σ2)(x) = (x− m)2
2σ2
whereas if η(z) = λ(ez− 1) (Poisson law with parameter λ), then
h = log x
λ ; FP (λ)(x) =
{
x log x
λ− (x− λ) if x > 0,
+∞ otherwise .
FN (m,σ2 )
+∞
FP(λ)
1
FIGURE 3. The Legendre-Fenchel transforms of a Gaussian law and of a
Poisson law.
MOD-φ CONVERGENCE, I 13
