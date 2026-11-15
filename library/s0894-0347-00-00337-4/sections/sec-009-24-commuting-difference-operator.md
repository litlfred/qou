---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-009-24-commuting-difference-operator
section_title: "Commuting difference operator"
section_number: 2.4
pages: 14-14
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
∇on the lattice Z,
(∆f)(k) = f(k + 1) −f(k) ,
(∇f)(k) = f(k) −f(k −1) .
Note that ∇= −∆∗as operators on ℓ2(Z). Consider the following second order
diﬀerence Sturm–Liouville operator:
D = ∆◦α ◦∇+ β ,
(2.17)
where α and β are operators of multiplication by certain functions α(k), β(k). The
operator (2.17) is self–adjoint in ℓ2(Z). A straightforward computation shows that
(2.18)

Df

(k) = (−α(k + 1) −α(k) + β(k))f(k)
+ α(k)f(k −1) + α(k + 1)f(k + 1) .
It follows that if α(s) = 0 for a certain s ∈Z, then the space of functions f(k)
vanishing for k < s is invariant under D.
Proposition 2.12. Let [J]s denote the operator in ℓ2({s, s+1, . . .}) obtained by re-
stricting the kernel J to {s, s+1, . . .}. Then the diﬀerence Sturm–Liouville operator
(2.17) commutes with [J]s provided
α(k) = k −s,
β(k) = −k(k + 1 −s −2
√
θ)
√
θ
+ const .
Proof. Since [J]s is the square of the operator with the kernel Jk+l+1−s, it suﬃces
to check that the latter operator commutes with D, with the above choice of α and
β. But this is readily checked using (2.18).
This proposition is a counterpart of a known fact about the Airy kernel; see [36].
Moreover, in the scaling limit when θ →∞and
k = 2
√
θ + x θ1/6,
s = 2
√
θ + ς θ1/6,
the diﬀerence operator D becomes, for a suitable choice of the constant, the diﬀer-
ential operator
d
dx ◦(x −ς) ◦d
dx −x(x −ς),
which commutes with the Airy operator restricted to (ς, +∞). The above diﬀeren-
tial operator is exactly that of Tracy and Widom [36].
Remark 2.13. Presumably, this commuting diﬀerence operator can be used to ob-
tain, as was done in [36] for the Airy kernel, asymptotic formulas for the eigenvalues
of [J]s, where s = 2
√
θ + ς θ1/6 and ς ≪0. Such asymptotic formulas may be very
useful if one wishes to reﬁne Theorem 4 and to establish convergence of moments
in addition to convergence of distribution functions. For individual distributions of
λ1 and λ2 the convergence of moments was obtained, by other methods, in [3, 4].
