We verify each $S$-eigenvalue in turn.

**Coefficients.** The action $q \mapsto q^{-1}$ extends to the
underlying field of fractions and acts on each coefficient:

- $D = q^4 + 4q^2 + 1$ is palindromic in $q^2$: under $q \to q^{-1}$,
  $D \to q^{-4} + 4q^{-2} + 1 = q^{-4}(1 + 4q^2 + q^4) = q^{-4} D$.
  Then $W_{\mathrm{sym}} = q^2/D \to q^{-2}/(q^{-4} D) = q^2/D$,
  invariant.  Same for $W_{\mathrm{alt}}$.  For $W_{\mathrm{std}}$:
  $(q^2+1)^2 \to (q^{-2}+1)^2 = q^{-4}(1+q^2)^2$, so
  $W_{\mathrm{std}} \to q^{-4}(1+q^2)^2 / (q^{-4} D) = W_{\mathrm{std}}$.
- $[3]_q = q^2 + 1 + q^{-2}$: invariant under $q \to q^{-1}$.
- $H_A = q - q^{-1} \to q^{-1} - q = -H_A$, so $H_A$ has eigenvalue
  $-1$ and $H_A^2$ has eigenvalue $+1$.
- $z = 1/(q^{1/2} + q^{-1/2})$: the denominator is symmetric under
  $q \to q^{-1}$, so $z$ is invariant.
- Catalan's constant $G$, Borromean volume $8G$, electron mass
  $m_e$, and binding scale $\alpha$ are real numerical constants
  unaffected by the algebraic action.

**Functional $\Phi_2$.** The transfer matrix is
$T(c, d) = \begin{pmatrix} cH_A + d & c \\ c & d \end{pmatrix}$
with $\det T = d(cH_A + d) - c^2$.  The Frobenius antipode
maps the primitive factor $(c, d)$ to $(c, d - cH_A)$ (this swaps
$\sigma \leftrightarrow \sigma^{-1}$).  Direct computation:

See [Table 3](#tbl:frobenius-s-classification-table3-data).

For each primitive the determinant is $S$-invariant.  Since
$\det$ is multiplicative on chain products, $\Phi_2 = \sum_i
\log\lvert\det M_i\rvert$ is $S$-invariant.

**Functional $\Phi_3$.** For each primitive, direct computation
shows
$\chi^{\mathrm{sym}}(S(c, d)) = -\chi^{\mathrm{alt}}(c, d)$ and
$\chi^{\mathrm{alt}}(S(c, d)) = -\chi^{\mathrm{sym}}(c, d)$
(verify: for $(1, 0)$ with $\chi^{\mathrm{sym}} = q$,
$\chi^{\mathrm{alt}} = -1/q$, and $S(1, 0) = (1, -H_A)$ giving
$\chi^{\mathrm{sym}} = q + (-H_A) = q^{-1}$ and
$\chi^{\mathrm{alt}} = -1/q + (-H_A) = -q$, matching the swap with
sign).  For a chain product

$$
  \frac{\chi^{\mathrm{sym}}(S(\beta))}{\chi^{\mathrm{alt}}(S(\beta))}
  = \frac{(-1)^n \chi^{\mathrm{alt}}(\beta)}{(-1)^n \chi^{\mathrm{sym}}(\beta)}
  = \left(\frac{\chi^{\mathrm{sym}}(\beta)}{\chi^{\mathrm{alt}}(\beta)}\right)^{-1}
$$

so $\Phi_3(S(\beta)) = -\Phi_3(\beta)$, eigenvalue $-1$.

**Functional $\Phi_1$.** The unsymmetrised standard character
$\chi^{\mathrm{std}}(\beta)$ is not an $S$-eigenvector in general.
The Frobenius-symmetrised value
$V_{\mathrm{Frob}} = (\chi^{\mathrm{std}}(\beta) + \chi^{\mathrm{std}}(S(\beta)))/2$
is by construction $S$-invariant.  Equivalently, the average
$\Phi_1 := \tfrac12 (\Phi_1(\beta) + \Phi_1(S(\beta)))$ is the
projection onto the $S$-even subspace.
$\qquad\blacksquare$
