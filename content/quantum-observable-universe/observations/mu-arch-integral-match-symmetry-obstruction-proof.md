*Proof.* We establish the two claims separately.

**(1) $\langle G \rangle = 0$ under symmetric $\rho_\infty$.**

By the assumption that $\rho_\infty$ is symmetric under $x \mapsto
-x$: for every measurable $A \subset \mathcal{F}_\infty$,
$\rho_\infty(-A) = \rho_\infty(A)$, where $-A = \{-x : x \in A\}$.

Change variables $x \to -x$ in the inner integral:
$$
  \iint G(x, y)\,d\rho(x)\,d\rho(y)
  \;=\;
  \iint G(-x, y)\,d\rho(-x)\,d\rho(y)
  \;=\;
  \iint G(-x, y)\,d\rho(x)\,d\rho(y).
$$
Using $G(-x, y) = -\mathrm{tr}_M(x \cdot y) = -G(x, y)$ (linearity of
trace in the first argument and sign-flip):
$$
  \iint G(x, y)\,d\rho(x)\,d\rho(y)
  \;=\;
  -\iint G(x, y)\,d\rho(x)\,d\rho(y).
$$
Therefore $\iint G\,d\rho^2 = 0$. $\square$ for (1).

**(2) $\langle \mathcal{L}_{\mathrm{CFS}} \rangle > 0$ under
non-trivial $\rho_\infty$.**

The Finster causal Lagrangian is non-negative pointwise by
construction:
$\mathcal{L}_{\mathrm{CFS}}(x, y) \geq 0$ for all $(x, y) \in
\mathcal{F}_\infty^2$ (Finster 2024 §2: non-negativity is built into
the variational design so the causal action admits minima).

It remains to show $\mathcal{L}_{\mathrm{CFS}}(x, y) > 0$ on a set
of positive $\rho_\infty \otimes \rho_\infty$ measure. The set where
$\mathcal{L}_{\mathrm{CFS}}(x, y) = 0$ is the set of pairs where
*all eigenvalues of $x \cdot y$ are equal in absolute value* (by the
difference-of-eigenvalues structure of $\mathcal{L}_{\mathrm{CFS}}$).
For a generic free-probability spectral measure with continuous
support, this constraint defines a positive-codimension subset of
$\mathcal{F}_\infty^2$ — i.e., a set of $\rho_\infty \otimes
\rho_\infty$ measure zero.

Therefore on a full-measure subset, $\mathcal{L}_{\mathrm{CFS}}(x, y) >
0$, and integration gives a strictly positive value:
$$
  \iint \mathcal{L}_{\mathrm{CFS}}(x, y)\,d\rho(x)\,d\rho(y) \;>\; 0.
$$
$\square$ for (2).

**Combining (1) and (2).** $\langle G \rangle = 0$ while
$\langle \mathcal{L}_{\mathrm{CFS}} \rangle > 0$, so $\langle G
\rangle \neq \langle \mathcal{L}_{\mathrm{CFS}} \rangle$.
Integral-match version of $\mu_{\mathrm{arch}}$ fails under any
centered free-probability limit. $\square$

**Independence of Finster variant.** The argument uses only two
properties of $\mathcal{L}_{\mathrm{CFS}}$:
- Evenness in $x$ (since eigenvalues of $(-x)y$ are negatives of those
  of $xy$, and the functional depends on $|\lambda|$).
- Non-negativity (built into the variational principle).
Both properties hold for every Finster variant in the literature; the
conclusion is therefore robust against normalisation or definitional
choice.

**Robustness against $\rho_\infty$ choice.** The argument also
applies to any symmetric (under $x \mapsto -x$) free-probability
spectral measure: Wigner semicircle, centered q-Gaussian, free-Poisson
with vanishing mean shift, etc. The obstruction is the *parity
mismatch* between $G$ (odd) and $\mathcal{L}_{\mathrm{CFS}}$ (even),
which forces $\langle G \rangle = 0$ while $\langle \mathcal{L}_{\mathrm{CFS}}
\rangle$ remains positive.
