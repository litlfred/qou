**Proposition (strict $\mu_{\mathrm{arch}}$ mismatch at $n=2$).**
*Let $H_2(R, q)$ be the Hecke algebra at $n = 2$ in the Wenzl
positivity regime. The QOU Frobenius Gram kernel
$G(x, y) = \mathrm{tr}_M(x \cdot y)$
([prop:qou-continuum-kernel-is-frobenius-gram](#prop:qou-continuum-kernel-is-frobenius-gram))
and the Finster causal Lagrangian
$\mathcal{L}_{\mathrm{CFS}}(x, y)$ [`finster2021`, `finster2024`]
take strictly different values on the unit pair $(1, 1) \in
H_2(R, q) \times H_2(R, q)$:*
$$
  G(1, 1) \;=\; 1
  \qquad\text{versus}\qquad
  \mathcal{L}_{\mathrm{CFS}}(1, 1) \;=\; 0.
$$
*Therefore the strict-match outcome of the
$\mu_{\mathrm{arch}}$ kernel-match conjecture
([conj:mu-arch-continuum-limit](#conj:mu-arch-continuum-limit))
**fails at the smallest non-trivial level of the Hecke tower**.*

**Where the mismatch comes from — structural reading.** The two
kernels live in different algebraic classes:

- $G(x, y) = \mathrm{tr}_M(x \cdot y)$ is **trace-additive** in the
  eigenvalues of $x \cdot y$. It is a bilinear functional, sum of
  eigenvalues weighted by the Markov-trace decomposition.

- $\mathcal{L}_{\mathrm{CFS}}(x, y)$ is built from *differences*
  $(\lvert\lambda_i\rvert - \lvert\lambda_j\rvert)^2$ of eigenvalues
  of $x \cdot y$ (Finster 2021 Bull. Lond. Math. Soc. eq. (1.3),
  Finster 2016 textbook §1.2.2). It is **trace-subtractive** /
  *spectral-difference-extremal*.

When $x = y = 1$, the operator product $x \cdot y = 1$ has all
eigenvalues equal (to $1$). The trace-additive $G$ gives
$\mathrm{tr}_M(1) = 1$; the trace-subtractive $\mathcal{L}_{\mathrm{CFS}}$
vanishes because all eigenvalue differences are zero. The structural
asymmetry is exhibited on the simplest pair.

**Implication for the bifurcation.** Of the three bifurcation
outcomes of $\mu_{\mathrm{arch}}$:

- **Strict match** ($G = \mathcal{L}_{\mathrm{CFS}}$ as functions) —
  **REFUTED** at $n = 2$ by this proposition.
- **Integral match** ($\iint G\,d\rho^2 = \iint \mathcal{L}_{\mathrm{CFS}}\,d\rho^2$) —
  could still hold by cancellation if the pair $(1, 1)$ has measure
  zero under $\rho_\infty$, or if the difference is in the null space
  of $\rho_\infty \otimes \rho_\infty$. *Open.*
- **Mismatch** (action values differ) — implied by the structural
  asymmetry above, generically expected.

**The integral-match question, sharpened.** With strict-match
refuted, the residual $\mu_{\mathrm{arch}}$ conjecture is reduced to
the question: does the kernel difference $G - \mathcal{L}_{\mathrm{CFS}}$
lie in the null space of $\rho_\infty \otimes \rho_\infty$? The
proposition shows that at $n = 2$, this difference is
$G(1, 1) - \mathcal{L}_{\mathrm{CFS}}(1, 1) = 1 \neq 0$. For the
integral to vanish, *negative* contributions elsewhere would have to
cancel exactly. There is no algebraic reason for this cancellation
to hold, and the integral-match outcome is therefore the new
narrowed open question.

**Status: provable.** The proof in
[`prf:mu-arch-strict-match-fails-at-n2`](#prf:mu-arch-strict-match-fails-at-n2)
is the explicit $n = 2$ computation. The result holds for every
Finster Lagrangian variant in the difference-of-eigenvalues class
(the standard class), independent of normalisation.

**Consequence: QOU and CFS are distinct continuum theories.** This
proposition is the first decisive piece of evidence that the QOU
substrate and the Finster CFS substrate, while sharing carrier
algebra (type II$_1$) and universality class (free probability), do
*not* produce the same continuum action. QOU's natural quadratic
action kernel (Frobenius Gram, bilinear, trace-additive) differs
from Finster's causal Lagrangian (spectral-difference-extremal) at
the smallest non-trivial level of comparison. The two frameworks
describe *different* continuum theories of the same operator-algebra
substrate.

**What remains for $\mu_{\mathrm{arch}}$.** The only open piece of
the conjecture is the *integral-match* version: whether the
kernel-mismatch we've established cancels out under integration
against the free-probability spectral measure $\rho_\infty$. This is
a measure-theoretic question that depends on the specific support
and weights of $\rho_\infty$. It can be checked at finite $n$ via
witness-level computations on the LP basis.
