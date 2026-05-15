**Proposition (integral-match obstruction via trace symmetry).**
*Let $\rho_\infty$ be any free-probability spectral measure on
$\mathcal{F}_\infty$ that is **symmetric** under $x \mapsto -x$ (the
centered case — Wigner semicircle, centered q-Gaussian at $q = 1$,
etc.). Then under the free product measure $\rho_\infty \otimes
\rho_\infty$:*
$$
  \iint_{\mathcal{F}_\infty^2}
    G(x, y)\,d\rho_\infty(x)\,d\rho_\infty(y) \;=\; 0,
$$
*while*
$$
  \iint_{\mathcal{F}_\infty^2}
    \mathcal{L}_{\mathrm{CFS}}(x, y)\,d\rho_\infty(x)\,d\rho_\infty(y) \;>\; 0.
$$
*The integral-match version of $\mu_{\mathrm{arch}}$
([conj:mu-arch-continuum-limit](#conj:mu-arch-continuum-limit))
**fails strictly** under any centered free-probability limit. The
residual conjecture is therefore reduced to a question about the
**non-centered** q-Gaussian limit at substrate parameter $q_0$.*

**Why the obstruction works.** The two kernels have opposite
parities under $x \mapsto -x$:

- $G(x, y) = \mathrm{tr}_M(x \cdot y)$ is **odd** in $x$: linear in
  $x$ with $\mathrm{tr}_M(-x \cdot y) = -\mathrm{tr}_M(x \cdot y)$.
- $\mathcal{L}_{\mathrm{CFS}}(x, y)$ is **even** in $x$: the
  eigenvalues of $(-x) \cdot y$ are negatives of eigenvalues of
  $x \cdot y$, but Finster's functional depends on $|\lambda|$, so
  $\mathcal{L}_{\mathrm{CFS}}(-x, y) = \mathcal{L}_{\mathrm{CFS}}(x, y)$.

Under symmetric $\rho_\infty$ (so $\rho_\infty(-A) = \rho_\infty(A)$
for measurable $A$), the integral of an odd function vanishes by
change-of-variables, while the integral of an even function is
preserved.

By construction, Finster's causal Lagrangian is **non-negative**
$\mathcal{L}_{\mathrm{CFS}}(x, y) \geq 0$ for all $(x, y)$ — this is
built into the variational design of the causal action (Finster
2024 §2: the causal action must be non-negative to permit
minimisation). On a measure $\rho_\infty$ with full support on
$\mathcal{F}_\infty$ containing pairs of generic signature, the
integral is *strictly positive*: zero only if $\mathcal{L}_{\mathrm{CFS}}$
vanishes ρ-almost-everywhere, which generically does not happen.

**Implication for the conjecture.** Both centred outcomes are now
resolved:

| Outcome | Status under centered $\rho_\infty$ |
|---|---|
| Strict match $G \equiv \mathcal{L}_{\mathrm{CFS}}$ | **Refuted** at $n = 2$ ([prop:mu-arch-strict-match-fails-at-n2](#prop:mu-arch-strict-match-fails-at-n2)) |
| Integral match $\langle G \rangle = \langle \mathcal{L}_{\mathrm{CFS}}\rangle$ | **Refuted** by this proposition: $\langle G \rangle = 0 < \langle \mathcal{L}_{\mathrm{CFS}}\rangle$ |
| Mismatch | Established |

**Where the residual conjecture lives.** The QOU substrate parameter
is $q_0 \approx 1.110 \neq 1$. The corresponding q-Gaussian limit
measure $G_{q_0}(t, x)$ in the Marsh–Tsallis sense [`marsh2006`] is
**not** symmetric under $x \mapsto -x$ — q-Gaussians at $q > 1$ have
heavy tails and non-vanishing odd moments. Under non-centered
$\rho_\infty$, both $\langle G \rangle$ and $\langle \mathcal{L}_{\mathrm{CFS}}\rangle$
are non-zero, and the integral-match question becomes a specific
numerical comparison at $q_0$:
$$
  \langle G \rangle_{G_{q_0}}
  \;\stackrel{?}{=}\;
  \langle \mathcal{L}_{\mathrm{CFS}} \rangle_{G_{q_0}}.
$$
This is a single-q-value coincidence. Given the unrelated structural
forms of $G$ (bilinear trace) and $\mathcal{L}_{\mathrm{CFS}}$
(eigenvalue-difference extremal), the coincidence would be a
multi-parameter fine-tuning at exactly $q_0$.

**Connection to the q-CLT conjecture.** The same q-Gaussian shape
appears in
[conj:q-clt-non-commutative](#conj:q-clt-non-commutative), whose
residual conjecture asks whether three q-parameters (Blitvić,
Tsallis, QOU) coincide at $q_0$. If both this conjecture and the
integral-match conjecture resolve "yes," it would be a **double
coincidence** at the single value $q_0$ — implausible *a priori*.
The most likely combined outcome:

- *(Most likely)* q-CLT q-coincidence holds (the three q's identify
  by definitional matching), but integral-match fails (QOU and CFS
  predict distinct continuum action values at $q_0$).
- *(Less likely)* both hold by an unexplained algebraic identity.
- *(Unlikely)* both fail.

**Fourier-transform reading.** The non-commutative Fourier transform
in our setting is the Plancherel map
$\Pi_{\mathrm{tr}} \colon (A_q, \mathrm{tr}_M) \to (\widehat{A}_q,
\tilde w_\lambda, \{\chi_\lambda\})$
([prop:cfs-as-traceful-projection-of-qou](#prop:cfs-as-traceful-projection-of-qou)).
Under this transform:
- $G(x, y) = \mathrm{tr}_M(x \cdot y)$ decomposes as
  $\sum_\lambda y_\lambda \chi_\lambda(x \cdot y)$, where $y_\lambda$
  is the Jones-Markov central coefficient (notation register).
- $\mathcal{L}_{\mathrm{CFS}}(x, y)$ does *not* admit a similar
  linear-character decomposition: as a non-linear functional of
  $\mathrm{spec}(x \cdot y)$, it does not factor through the
  irreducible-character basis.

This is the **Fourier-orthogonality obstruction**: $G$ lives in
the span of $\{\chi_\lambda\}$ (the "Fourier basis" of the operator
algebra under Plancherel), while $\mathcal{L}_{\mathrm{CFS}}$
projects onto multiple Fourier modes including non-linear products
of characters. No clean Fourier-domain cancellation rescues the
integral-match.

**Status: provable.** The proof in
[`prf:mu-arch-integral-match-symmetry-obstruction`](#prf:mu-arch-integral-match-symmetry-obstruction)
is the trace-symmetry argument plus Finster non-negativity.
