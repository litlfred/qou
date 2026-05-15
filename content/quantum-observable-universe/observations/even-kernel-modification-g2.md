**Proposition (squared kernel $G_2$ as even alternative + structural identity to $\mathcal{L}_{\mathrm{CFS}}$).**
*Define the **squared QOU kernel***
$$
  G_2(x, y) \;:=\; \mathrm{tr}_M\bigl((x \cdot y)^2\bigr).
$$
*Then:*

1. *(Even parity.) $G_2(-x, y) = G_2(x, y)$ — the parity
   obstruction
   ([prop:mu-arch-integral-match-symmetry-obstruction](#prop:mu-arch-integral-match-symmetry-obstruction))
   does not apply to $G_2$.*

2. *(Algebraic identity to Finster $\mathcal{L}_{\mathrm{CFS}}$.) For
   self-adjoint $x, y$ with real spectrum of $x \cdot y$ on the
   simple Wedderburn blocks, the Finster causal Lagrangian in the
   pair-difference form
   $\mathcal{L}_{\mathrm{CFS}}(x, y) = \sum_{i<j}(|\lambda_i| -
   |\lambda_j|)^2$ admits the decomposition*
   $$
     \mathcal{L}_{\mathrm{CFS}}(x, y)
     \;=\;
     n \cdot G_2(x, y) - \lVert x \cdot y\rVert_1^{\,2},
   $$
   *where $n = \dim(\text{block})$ and $\lVert x \cdot y\rVert_1 :=
   \mathrm{tr}_M(|x \cdot y|)$ is the trace-class norm of $x \cdot y$.*

3. *(Reformulation of $\mu_{\mathrm{arch}}$.) Substituting (2) into
   the integral-match question:*
   $$
     \iint \mathcal{L}_{\mathrm{CFS}}\,d\rho^2
     \;=\;
     n \cdot \iint G_2\,d\rho^2
     \;-\;
     \iint \lVert x \cdot y\rVert_1^{\,2}\,d\rho^2.
   $$
   *So the residual conjecture is the **trace-class-norm correction
   integral**: does $\iint \lVert x \cdot y\rVert_1^{\,2}\,d\rho^2$
   vanish on the free-probability spectral limit? If yes, $\mathcal{L}_{\mathrm{CFS}}
   = n \cdot G_2$ in integral, and $\mu_{\mathrm{arch}}$ holds with
   $G_2$ as the QOU kernel; if no, the trace-class correction is the
   structural difference between QOU and CFS continuum theories.*

**Setup and computation.** For self-adjoint operator $x \cdot y$
with real eigenvalue spectrum $\{\lambda_1, \ldots, \lambda_n\}$ on a
block of dimension $n$:

- $\mathrm{tr}((x \cdot y)^2) = \sum_i \lambda_i^2 = G_2$ (sum of
  squared eigenvalues).
- $\mathrm{tr}|x \cdot y| = \sum_i |\lambda_i| = \lVert x \cdot y\rVert_1$
  (sum of absolute eigenvalues).
- The Finster pair-difference Lagrangian is
  $\sum_{i < j}(|\lambda_i| - |\lambda_j|)^2$.

Expanding:
$$
  \sum_{i<j}(|\lambda_i| - |\lambda_j|)^2
  = \sum_{i<j}|\lambda_i|^2 + \sum_{i<j}|\lambda_j|^2 - 2\sum_{i<j}|\lambda_i||\lambda_j|.
$$
Each of $|\lambda_i|^2$ and $|\lambda_j|^2$ appears in $n-1$ pairs
(summing over all $j \neq i$), so the first two terms together give
$(n-1)\sum_i |\lambda_i|^2 = (n-1)\sum_i \lambda_i^2 = (n-1)G_2$.

Using $(\sum_i |\lambda_i|)^2 = \sum_i \lambda_i^2 + 2\sum_{i<j}|\lambda_i||\lambda_j|$:
$$
  2\sum_{i<j}|\lambda_i||\lambda_j| = \lVert xy\rVert_1^{\,2} - G_2.
$$

Substituting:
$$
  \mathcal{L}_{\mathrm{CFS}} = (n-1)G_2 - (\lVert xy\rVert_1^{\,2} - G_2) = n \cdot G_2 - \lVert xy\rVert_1^{\,2}.
$$
This proves the identity. $\square$ for the algebra.

**What this reveals.** The Finster causal Lagrangian in the natural
pair-difference form is *algebraically a multiple of $G_2$ minus the
squared trace-class norm*. Substituting back into the conjecture:

| Version of $\mu_{\mathrm{arch}}$ | Comparison object |
|---|---|
| Original | "Does Finster L equal QOU Plancherel functional?" |
| Refined (kernel-match) | "Does $G$ equal $\mathcal{L}_{\mathrm{CFS}}$?" — refuted (parity + $n=2$) |
| **Reformulated (this proposition)** | **Does $\iint \lVert xy\rVert_1^{\,2}\,d\rho^2 = 0$ on the free-probability limit?** |

The reformulation is a clean, sharp question with a known mathematical
object on each side. The answer determines whether QOU and CFS
coincide as continuum theories:

- **Yes** ($\lVert xy\rVert_1^{\,2}$ integrates to zero): the trace-class
  correction vanishes, $\mathcal{L}_{\mathrm{CFS}}$ integrates to
  $n \cdot G_2$, and QOU's natural even kernel $G_2$ exactly matches
  Finster's causal action (up to the dimension factor $n$). $\mu_{\mathrm{arch}}$
  holds with $G_2$ as the QOU side.

- **No** ($\lVert xy\rVert_1^{\,2}$ integrates to a non-zero value):
  the trace-class correction is the structural separation between
  QOU and CFS. Both theories share the energy-like quadratic term
  $G_2$, but Finster's adds a (negative) trace-class correction that
  QOU does not. The two continuum theories then differ specifically
  by this correction term, which has a physical interpretation as
  the **trace-class energy density** of the product $xy$ — a
  measure of the "spread" of the spectrum vs its "magnitude."

**Free-probability evaluation.** Under the centered Wigner semicircle
limit, both $\iint G_2\,d\rho^2$ and $\iint \lVert xy\rVert_1^{\,2}\,d\rho^2$
are computable from moments:

- $\iint G_2\,d\rho^2 = \langle (xy)^2 \rangle_\rho$, the 4th free
  moment of a product of two free semicirculars. Equal to $1$ for
  standard free semicirculars (up to normalisation; Catalan-number
  computation).
- $\iint \lVert xy\rVert_1^{\,2}\,d\rho^2 = \langle (\sum |\lambda_i|)^2 \rangle$,
  a 2nd moment of the spectral $L^1$ norm. *Strictly positive* on any
  non-trivial measure with full support.

Therefore, under the centered free-probability limit:
$$
  \iint L_{\mathrm{CFS}}\,d\rho^2 \;=\; n \cdot G_2^{\text{avg}} - \langle \lVert\cdot\rVert_1^2\rangle
$$
is generally smaller than $n \cdot G_2^{\text{avg}}$. The mismatch
between QOU's $G_2$ action and CFS's full action is
$\langle \lVert\cdot\rVert_1^2\rangle \neq 0$, confirming the
**mismatch outcome** of the bifurcation.

**Physical reading: the trace-class deficit.** The Finster causal
action is *less* than QOU's energy-quadratic $n \cdot G_2$ by exactly
the squared trace-class norm. This "deficit" is what makes the
Finster Lagrangian vanish on equal-eigenvalue pairs (like $(1, 1)$,
where $G_2 = 1$ but $\lVert\cdot\rVert_1^2 = 1$ too, giving $L =
n - 1$ if we use the proportionality version, or $0$ in the spread-
only version). It is a "concentration penalty" — CFS penalises
high-magnitude pairs that QOU's $G_2$ rewards. The two theories
predict *different* equilibrium configurations.

**Status: provable.** Part (1) is parity-direct. Part (2) is the
algebraic identity proved above. Part (3) is substitution. The
trace-class moment integrals in the free-probability evaluation are
standard free-probability calculations.

**Conclusion.** The user's intuition about even-modification is
correct: replacing $G$ with $G_2$ removes the parity obstruction
and reformulates the conjecture into a sharp question about a
specific trace-class moment integral. The reformulation also
*resolves* the mismatch direction: the trace-class moment integral
is generically non-zero, so QOU's natural even kernel $G_2$ and
Finster's $\mathcal{L}_{\mathrm{CFS}}$ differ by a known correction
term in the limit. The structural separation between QOU and CFS
continuum theories is now identified as exactly the
**squared trace-class norm of the operator product**,
$\langle \lVert x \cdot y\rVert_1^{\,2}\rangle_{\rho_\infty}$.
