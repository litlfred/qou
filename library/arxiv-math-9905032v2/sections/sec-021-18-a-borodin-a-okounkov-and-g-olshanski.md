---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-021-18-a-borodin-a-okounkov-and-g-olshanski
section_title: "A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI"
section_number: 18
pages: 18-18
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
computation shows that
(2.18)
[
Df
]
(k) = ( −α(k + 1) − α(k) + β(k))f (k) +
α(k)f (k − 1) + α(k + 1)f (k + 1) .
It follows that if α(s) = 0 for a certain s ∈ Z then the space of functions
f (k) vanishing for k < s is invariant under D.
Proposition 2.12. Let [J]s denote the operator in ℓ2({s, s + 1, . . .})
obtained by restricting the kernel J to {s, s+1, . . .}. Then the diﬀerence
Sturm–Liouville operator (2.17) commutes with [J]s provided
α(k) = k − s, β (k) = − k(k + 1 − s − 2
√
θ)√
θ
+ const .
Proof. Since [J]s is the square of the operator with the kernel Jk+l+1−s,
it suﬃces to check that the latter operator commutes with D, with the
above choice of α and β. But this is readily checked using (2.18).
This proposition is a counterpart of a known fact about the Ai ry
kernel, see [32]. Moreover, in the scaling limit when θ → ∞ and
k = 2
√
θ + x θ1/ 6, s = 2
√
θ + ς θ 1/ 6,
the diﬀerence operator D becomes, for a suitable choice of the constant,
the diﬀerential operator
d
dx ◦ (x − ς) ◦ d
dx − x(x − ς),
which commutes to the Airy operator restricted to ( ς, +∞). The above
diﬀerential operator is exactly that of Tracy and Widom [32] .
Remark 2.13. Presumably, this commuting diﬀerence operator can
be used to obtain, as was done in [32] for the Airy kernel, asym ptotic
formulas for the eigenvalues of [ J]s, where s = 2
√
θ + ς θ1/ 6 and ς ≪ 0.
Such asymptotic formulas may be very useful if one wishes to r eﬁne
Theorem 4 and to establish convergence of moments in additio n to
convergence of distribution functions. For individual dis tributions of
λ1 and λ2 the convergence of moments was obtained, by other methods,
in [2, 3].
