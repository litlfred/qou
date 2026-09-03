---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-005-13-stable-distributions-and-mod-stable-convergen
section_title: "Stable distributions and mod-stable convergence"
section_number: 1.3
pages: 5-6
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
Let us recall brieﬂy the classiﬁcation of stable distributions (see [Sat99, Chapter 3]). Fixc >0 (the
scale parameter), α∈ (0, 2] (the stability parameter), andβ∈ [−1, 1] (the skewness parameter).
Deﬁnition 2.The stable distribution of parameters (c,α,β ) is the inﬁnitely divisible lawφ =φc,α,β
whose Fourier transform
ˆφ(ξ) =
∫
R
eixξφ(dx) = eη(iξ)
has for Lévy exponentη(iξ) =ηc,α,β(iξ) =−|cξ|α (1− iβh (α,ξ ) sgn(ξ)), where
h(α,ξ ) =
{
tan
(πα
2
)
if α⁄= 1,
− 2
π log|ξ| if α = 1
and sgn(ξ) =±1 is the sign ofξ.
The most usual stable distributions are:
• the standard Gaussian distribution 1√
2π e−x2/2dxfor c = 1√
2, α = 2 and β = 0;
• the standard Cauchy distribution 1
π(1+x2)dxfor c = 1, α = 1 and β = 0;
• the standard Lévy distribution 1√
2π
e−1/2x
x3/2 1 x≥0dxfor c = 1, α = 1
2 and β = 1.
Gaussian
Cauchy
Lévy
Fig. 1 Densities of the standard Gaussian, Cauchy and Lévy distribution.
We recall that mod-φ convergence on an open subsetD of C containing 0 can only occur when the
characteristic function ofφ is analytic around0. Among stable distributions, only Gaussian laws (which
correspond toα = 2) satisfy this property. Mod-φ convergence onD = iR can however be considered for
any stable distributionφ.
Since|eη(iξ)| = e−|cξ|α
is integrable, any stable lawφc,α,β has a densitymc,α,β(x)dx with respect to
the Lebesgue measure. Moreover, the corresponding Lévy exponents have the following scaling property:
for anyt> 0,
