---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-012-0-r-of
section_title: "(R) of"
section_number: 0
pages: 9-10
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
smooth functions whose derivatives all vanish at inﬁnity.
Actually, we will need to work with more general test functions, deﬁned by using the theory of tempered
distributions. We endow the Schwartz spaceS (R) of smooth rapidly decreasing functions with its usual
topology of metrizable locally convex topological vector space, deﬁned by the family of semi-norms
‖f‖k,l =
∑
a≤k
∑
b≤l
sup
x∈R
|xa (∂bf)(x)|.
We recall that a tempered distributionψ is a continuous linear formψ : S (R)→ C. The value of a
tempered distributionψ on a smooth functionf will be denotedψ(f) or⟨ψ|f⟩. The space of all tempered
distributions is classically denoted S′(R), and it is endowed with the∗-weak topology. The spaces of
integrable functions, of square integrable functions and of probability measures can all be embedded in
the space S′(R) as follows: iff is a function inL1(R)∪ L2(R), or ifµ is in M 1(R), then we associate to
them the distributions
⟨f|g⟩ =
∫
R
f(x)g(x)dx ; ⟨µ|g⟩ =
∫
R
g(x)µ(dx).
We then say that these distributions are represented by the functionf and by the measureµ.
The Fourier transform of a tempered distributionψ is deﬁned by duality: it is the unique tempered
distribution ˆψ such that ⟨
ˆψ
⏐⏐⏐f
⟩
=
⟨
ψ
⏐⏐⏐ ˆf
⟩
for anyf∈ S (R). This deﬁnition agrees with the previous deﬁnitions of Fourier transforms for integrable
functions, square integrable functions, or probability measures (all these elements can be paired with
Schwartz functions). Similarly, ifψ is a tempered distribution, then one can also deﬁne by duality its
derivative: thus,∂ψ is the unique tempered distribution such that
⟨∂ψ|f⟩ =−⟨ψ|∂f⟩
for anyf∈ S (R). The deﬁnition agrees with the usual one whenψ comes from a derivable function,
by the integration by parts formula. On the other hand, Fourier transform and derivation deﬁne linear
endomorphisms of S′(R); also note that the Fourier transform is bijective.
Deﬁnition 13.A smooth test function of order 1, or smooth test distribution is a distribution f ∈
S′(R), such that ∂f is in T0(R), that is to say that the distribution∂f can be represented by an
integrable function with compactly supported Fourier transform. We denoteT1(R) the space of smooth
test distributions.
We now discuss Parseval’s formula for functions inT1(R).
Proposition 14.Any smooth test distributionf∈ T1(R) can be represented by a bounded function in
C∞(R). Moreover, for any smooth test distribution inT1(R):
(TD1) Ifµ is a Borel probability measure, then the pairing⟨µ|f⟩ =
∫
Rf(x)µ(dx) is well deﬁned.
