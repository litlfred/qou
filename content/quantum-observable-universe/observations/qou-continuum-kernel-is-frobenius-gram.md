**Proposition (QOU's natural quadratic continuum kernel).**
*The natural quadratic functional on the QOU pre-Archimedean
algebraic side, in the form $S(\rho) = \iint K(x, y)\,d\rho(x)
\,d\rho(y)$ (the type of functional Finster's CFS uses for the
causal action), has kernel given by the Frobenius Gram matrix*
$$
  G_{\lambda\mu} \;:=\; \mathrm{tr}_M(b_\lambda \cdot b_\mu),
  \qquad \lambda, \mu \in \widehat{A}_q,
$$
*where $\{b_\lambda\}$ is the NF basis of $H_n(R, q)$ used by the
operator-selection LP. The QOU action in quadratic form is*
$$
  S_{\mathrm{QOU}}(\rho) \;=\;
    \sum_{\lambda, \mu \in \widehat{A}_q}
      G_{\lambda\mu} \cdot
      \rho_\lambda \cdot \rho_\mu,
$$
*and its continuum limit on the free-probability spectral measure
extends to $\iint G(x, y)\,d\rho(x)\,d\rho(y)$ with $G(x, y) =
\mathrm{tr}_M(x \cdot y)$ evaluated against the limit measure.*

**Why this is the right comparison object for CFS.** Finster's
causal action has the explicit double-integral form
$$
  S_{\mathrm{CFS}}(\rho) \;=\;
    \iint_{\mathcal{F}\times\mathcal{F}}
      \mathcal{L}_{\mathrm{CFS}}(x, y)\,d\rho(x)\,d\rho(y),
$$
quadratic in $\rho$ with kernel $\mathcal{L}_{\mathrm{CFS}}$. To
compare like with like, the QOU side must also be presented as a
quadratic functional with an explicit kernel. The
[traceful projection](#prop:cfs-as-traceful-projection-of-qou)
established that the QOU trace-side data is structurally CFS-style
$(\Omega, \mu, \mathcal{F})$; the present proposition fills in the
*quadratic kernel* that completes the CFS-style action functional
on QOU's side.

**Operator-algebra reading.** The kernel $G_{\lambda\mu} =
\mathrm{tr}_M(b_\lambda b_\mu)$ is the trace-induced inner product
on $H_\infty(q)$ — the Hilbert–Schmidt / Frobenius inner product
$\langle b_\lambda, b_\mu \rangle_{\mathrm{HS}} =
\mathrm{tr}(b_\lambda^* b_\mu)$ (with $b_\lambda^* = b_\lambda$ for
self-adjoint basis elements). On the GNS Hilbert space
$\mathcal{H}$ ([algebraic GNS embedding](#prop:algebraic-gns-embedding)),
$G$ is the Gram matrix of the embedding $\{b_\lambda\}$ — exactly
the *metric* on the GNS image.

**Where this kernel comes from.** The Frobenius Gram matrix is
*already* central in QOU: it is the constraint matrix in the
operator-selection LP
([`prop:operator-selection-lp`](#prop:operator-selection-lp)),
the metric for the Frobenius positivity constraint $Gx \geq 0$, and
the canonical Hilbert–Schmidt inner product on the Hecke algebra.
Promoting it to "the QOU continuum kernel" is therefore not a new
construction — it is an observation that the kernel already in use
*is* the quadratic kernel that CFS's framework requires.

**Sharpened Lagrangian-match question.** With this proposition, the
residual conjecture of
[μ_arch continuum limit](#conj:mu-arch-continuum-limit) reduces
to a single explicit question:

> ***Does the Finster causal Lagrangian $\mathcal{L}_{\mathrm{CFS}}(x, y)$ equal the QOU Frobenius Gram kernel $G(x, y) = \mathrm{tr}_M(x \cdot y)$ on the free-probability spectral limit?***

Both sides are now quadratic kernels in $(x, y)$; both are
real-valued; both live on the same operator algebra. The bifurcation
into "agree" / "disagree" outcomes is now between two *named*
kernels rather than between abstract Lagrangians of different orders.

**Structural observation: linear vs extremal.** The QOU kernel
$G(x, y) = \mathrm{tr}_M(x \cdot y)$ is **bilinear** in $(x, y)$ —
linear separately in each argument. Finster's
$\mathcal{L}_{\mathrm{CFS}}(x, y)$ is typically of the form
"max-of-pair-products of $|\lambda_i|$" applied to eigenvalues of
$x \cdot y$ — a **non-linear**, extremal functional in
$\mathrm{spec}(x \cdot y)$. Bilinearity is preserved under
free-probability limits (Voiculescu); extremal functionals
generally are not. *Generically*, therefore, $G(x, y)$ and
$\mathcal{L}_{\mathrm{CFS}}(x, y)$ are different functions of
$(x, y)$, and the Lagrangian-match conjecture fails.

The remaining open question is whether there is some *specific*
choice of free-probability spectral measure $\rho_\infty$ on which
the two kernels happen to integrate to the same value:
$\iint G\,d\rho_\infty^2 = \iint \mathcal{L}_{\mathrm{CFS}}\,d\rho_\infty^2$.
This is a measure-equality question, much weaker than the
functional-equality version, and the only remaining piece of
conjecture in the $\mu_{\mathrm{arch}}$ programme.

**Status: provable.** The proof in
[`prf:qou-continuum-kernel-is-frobenius-gram`](#prf:qou-continuum-kernel-is-frobenius-gram)
assembles the LP-duality formulation, the Frobenius positivity
constraint, and the GNS inner-product identification.
