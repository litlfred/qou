Under the surreal lift $q = 1 + \varepsilon$
(Hahn-series aether), every spectral operator
$O_q$ of this paper (Hecke generators, transfer matrices, $q$-
Hamiltonians, Feynman integrals, vortex operators) has eigenvalues
$\lambda_i(q)$ that are rational in $\varepsilon$, hence elements
of the valuation ring $\mathcal{O}$.

This conjecture asserts that **spectral gaps and singularities as
$q \to 1$ are read directly off the leading exponent $\ordw(\cdot)$**
of the eigenvalues, without analytic limits.

## Conjecture

Let $O_q : V \to V$ be a linear operator on a finite-dimensional
$\mathbf{No}$-vector space, whose matrix entries are rational
functions of $q$. At $q = 1 + \varepsilon$, let

$$
  \lambda_1(\varepsilon) \leq \lambda_2(\varepsilon) \leq \cdots
   \leq \lambda_N(\varepsilon)
$$

be the eigenvalues ordered by $\mathbf{No}$-magnitude. Define the
**spectral gap** $\Delta := \lambda_2(\varepsilon) -
\lambda_1(\varepsilon)$.

1. **Algebraic closure at $q = 1$**: the gap $\Delta$ closes in
   the classical limit iff $\ordw(\Delta) < 0$ (i.e., $\Delta$ is
   infinitesimal).

2. **Closure rate from leading exponent**: the rate of closure is
   $\ordw(\Delta) \in \mathbf{No}$. Specifically:
   - $\ordw(\Delta) = 0$: gap stays open in the classical limit
     (no closure).
   - $\ordw(\Delta) = -1$: gap closes linearly, $\Delta \sim
     c\,\varepsilon$ — generic first-order closure.
   - $\ordw(\Delta) = -n$ for $n \in \mathbb{N}$: gap closes
     polynomially of order $n$.
   - $\ordw(\Delta) \in (-\omega\cdot 2,\, -\omega)$: gap closes
     *faster than any polynomial but slower than any exponential*
     — signals transcendental quantum-dilogarithm behaviour.

3. **Singularity formation**: a divergence (eigenvalue blowing up)
   has $\ordw(\lambda_i) > 0$ in the surreal lift. The exponent
   $\ordw(\lambda_i)$ classifies the divergence type:
   - $\ordw(\lambda_i) = 1$: simple pole, $\lambda_i \sim
     C/\varepsilon = C\omega$.
   - $\ordw(\lambda_i) = n$: $n$-th order pole, $\lambda_i \sim
     C\omega^n$.
   - $\ordw(\lambda_i) \in (1, 2)$: fractional-order divergence,
     signalling root-of-unity or Weierstrass behaviour.

4. **Algebraic vs transcendental singularities**: if
   $\ordw(\lambda_i)$ is a **rational** surreal (in the
   Hahn-series rationals $\mathbb{Q} \subset \mathbf{No}$), the
   singularity is algebraic. If $\ordw(\lambda_i)$ is transfinite
   (involves $\omega$ or logarithms), the singularity is
   transcendental.

## Application to QOU

Specialise to two main-paper operators:

**Categorical transfer matrix $T(c, d)$** (braiding eigenvalues):
- Eigenvalues are $q$ and $-q^{-1}$ at every Hecke-level step.
- At $q = 1 + \varepsilon$: leading terms $1 + \varepsilon$ and
  $-(1 - \varepsilon + \varepsilon^2 - \cdots) = -1 + \varepsilon -
  \varepsilon^2 + \cdots$.
- Gap $\Delta = q - (-q^{-1}) = q + q^{-1}$, which equals $2 + O(\varepsilon^2)$
  at $q = 1 + \varepsilon$. $\ordw(\Delta - 2) = -2$, so no
  closure; the classical limit preserves the binary splitting.

**$q$-Hamiltonian $\hat{H}_q$** (from this paper):
- At $q = 1 + \varepsilon$, each eigenvalue is rational in
  $\varepsilon$.
- Classical-limit $q \to 1$ eigenvalues are the
  standard-parts.
- Quantum corrections are the subleading coefficients —
  accessible by inverting the $\ordw$ filtration.

**Möbius energy $E_q$**:
- $E_q = \frac{1}{4} E_{\mathrm{classical}} + \mathrm{const}$ at
  $q \to 1$.
- Surreal-lifted: $\ordw(E_q - \frac{1}{4}E_{\mathrm{classical}}) \geq 0$,
  with the leading surreal constant fixed.

## Contrast with classical spectral theory

Classical spectral analysis of $q$-deformed operators requires:
- $\varepsilon$--$\delta$ bounds on eigenvalues as $q \to 1$;
- careful treatment of multiplicity crossings;
- perturbation theory with analytic convergence radii.

Under the surreal lift, all of this is replaced by:
- *algebraic* evaluation of eigenvalues at $q = 1 + \varepsilon$
  (a rational arithmetic in $\varepsilon$);
- *ordinal-valued* leading exponents of spectral differences
  classifying gap closure;
- *no convergence requirement* — everything is formal power series
  with infinite-birthday exponents.

This is a substantive conceptual simplification; whether it
corresponds to a practical *proof* technique (replacing current
spectral-gap proofs in the paper with surreal evaluations)
depends on computability of the normal forms.

## Proof strategy

**Algebraic case (provable conditionally on the Hahn-series aether embedding)**:

1. Assume $O_q$ has matrix entries in $\mathbb{Q}(q)$ or, more
   generally, in the Hahn-series aether.

2. Eigenvalues are rational functions of $q$ by standard
   linear algebra; hence rational in $\varepsilon$ at
   $q = 1 + \varepsilon$.

3. Compute $\ordw(\Delta)$ directly from the rational-function
   expression.

4. Verify against this paper's spectral-gap statements
   (e.g., for the Hecke generators where the gap is known
   classically).

**Transcendental case (speculative)**:

5. For operators whose entries involve the quantum dilogarithm
   or other transcendentals, appeal to
   Berarducci–Mantova exponential/log on $\mathbf{No}$
   \cite{berarducci-mantova2018}.

6. Compute the normal-form expansion of each eigenvalue, reading
   off the leading transfinite exponent.

7. Match against known asymptotic-volume formulas (Kashaev,
   etc.).

**Required mathematical ingredients**:
- Evaluation of rational functions in $q$ at $q = 1 + \varepsilon$ in the valuation ring $\mathcal{O}$.
- The Hahn-series aether embedding.
- Conway normal-form extraction for characteristic-polynomial roots.

**Falsification path**: find an operator $O_q$ with classically
well-defined spectral gap closure *not* matching the leading
exponent $\ordw(\Delta)$. Such a mismatch would refute the
surreal-normal-form interpretation, likely indicating a subtle
multi-scale behaviour that the surreal lift does not capture.

**Assessment**: the algebraic case reduces to rational-function valuation arithmetic over $\mathbb{R}(\varepsilon)$, whereas the transcendental case requires the Berarducci–Mantova exponential and logarithm on $\mathbf{No}$. The overall conjecture is a *dictionary*, more testable than deep-research-open.

## Open problem

The conjecture is open. Its importance depends on whether the
QOU paper's spectral-gap and singularity-formation claims can be
rewritten as leading-exponent computations. If so, the
classical-limit discussions simplify substantially; if not, the
surreal lift is a curiosity.
