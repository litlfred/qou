---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-010-22-spaces-of-test-functions
section_title: "Spaces of test functions"
section_number: 2.2
pages: 8-9
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
Until the end of Section 2, all the spaces of functions considered will be spaces of complex valued
functions on the real line. Iff∈ L1(R), we denote its Fourier transform
ˆf(ξ) =
∫
R
eixξf(x)dx.
Recall that the Schwartz spaceS (R) is by deﬁnition the space of inﬁnitely diﬀerentiable functions whose
derivatives tend to0 at inﬁnity faster than any power ofx. Restricted toS (R), the Fourier transform is
an automorphism, and it satisﬁes the Parseval formula
∀f,g ∈ S (R),
∫
R
f(x)g(x)dx = 1
2π
∫
R
ˆf(ξ)ˆg(ξ)dξ.
We refer to [Lan93, Chapter VIII] and [Rud91, Part II] for a proof of this formula, and for the theory of
Fouriertransforms.TheParsevalformulaallowstoextendbydualityand/ordensitytheFouriertransform
to other spaces of functions or distributions. In particular, iff ∈ L2(R), then its Fourier transformˆf
is well deﬁned inL2(R), although in general the integral
∫
R eixξf(x)dx does not converge; and we have
again the Parseval formula
∀f,g ∈ L2(R),
∫
R
f(x)g(x)dx = 1
2π
∫
R
ˆf(ξ)ˆg(ξ)dξ,
which amounts to the fact thatf↦→ 1√
2π
ˆf is an isometry ofL2(R) (see [Rud91, §7.9]).
We denote M 1(R) the set of probability measures on Borel subsets ofR. In the sequel, we will need
to apply a variant of Parseval’s formula, whereg(x)dx is replaced byµ(dx), withµ in M 1(R). This is
given in the following lemma (see [Str11, Lemma 2.3.3], or [Mal95, p. 134]).
Lemma 10.For any functionf∈ L1(R) with ˆf∈ L1(R), and any Borel probability measureµ∈ M 1(R),
the pairing⟨µ|f⟩ =
∫
Rf(x)µ(dx) is well deﬁned, and the Parseval formula holds:
∫
R
f(x)µ(dx) = 1
2π
∫
R
ˆf(ξ)ˆµ(−ξ)dξ,
whereˆµ(ξ) =
∫
R eiξxµ(dx). The formula also holds for ﬁnite signed measures.
Let us now introduce two adequate spaces of test functions, for which we shall be able to prove
speed of convergence estimates. We ﬁrst consider functionsf∈ L1(R) with compactly supported Fourier
transforms:
Deﬁnition 11.We call smooth test function of order 0, or simply smooth test function an element
f ∈ L1(R) whose Fourier transform is compactly supported. We denoteT0(R) the subspace of L1(R)
that consists in smooth test functions; it is an ideal for the convolution product.
Example 12.If
sinc(x) := sinx
x = 1
2
∫ 1
−1
eixξdξ,
then by Fourier inversion ˆsinc(ξ) = π 1|ξ|≤1 is compactly supported on [−1, 1]. Therefore, f(x) =
(sinc(x))2 is an element ofL1(R) whose Fourier transform is compactly supported on[−1, 1] + [−1, 1] =
[−2, 2], andf∈ T0(R).
Mod-φ convergence, II: Estimates on the speed of convergence 9
