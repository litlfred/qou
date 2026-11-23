## Connection to the wider framework

The two ingredients each acquired a categorical home elsewhere in the
framework after the initial derivation:

- **Step 1 (the polynomial form `χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶`)**
  shares its Wedderburn partition-indexed framework with the
  [q-heat-kernel Peter–Weyl
  decomposition](../information-theory/q-heat-kernel-peter-weyl.md)
  and the [Habiro residue-sum equivalence](habiro-residue-sum-equivalence.md).
  Note the q-heat-kernel proposition supplies the
  $q$-Laplacian eigenvalues $\mu_\lambda(q)$ — heat-flow decay rates,
  *not* the braid-character values $\chi^\lambda(\beta)$; the
  polynomial form itself comes from the projector route below or
  from direct substitution on the closed-form trace.
  The categorical projector onto the (2,1) channel is the
  $\mathbf{e}_-$ minus-eigenspace idempotent of the Hecke quadratic
  relation $q\sigma^2 = (q^2 − 1)\sigma + q$: $\mathbf{e}_\pm$ are
  orthogonal idempotents with $\mathbf{e}_+ + \mathbf{e}_- = 1$.
  Closed-form trace computation on $V^{\otimes 3}$ can be done via
  the Cayley–Hamilton block reduction of polynomials in a Hecke
  generator.

- **Step 2 (the Markov normalisation `y_{(2,1)}(q=1) = 1/4`)**
  is the $q = 1$ evaluation of the exact closed-form Wenzl weight
  $y_{(2,1)}(q) = 1/[2]_q^2$ established in
  [Closed-form Jones/Temperley–Lieb weights on $H_3(q)$ (Borromean Jones polynomial)](h3-markov-wenzl-weights.md).
  The full $\mathrm{H}_3$ weight vector is
  $\bigl([4]_q/[2]_q^3,\ 1/[2]_q^2,\ 0\bigr)$, evaluating at $q = 1$
  to the non-uniform $(\tfrac12, \tfrac14, 0)$ — the sign channel
  carries zero weight identically (Temperley–Lieb quotient), and the
  Jones-normalised trace is chiral, so no bar-involution uniformity
  applies.

Concretely, the R-matrix derivation in **Step 1** of this proof can
be reformulated equivalently as: extract the $\mathbf{e}_-$ component
of $\sigma_1^{-1}\sigma_2$ on $V_{1/2}^{\otimes 3}$, take the $h^4$
coefficient of its trace.  The $\mathbf{e}_-$ idempotent is the
categorical replacement for the explicit $8 \times 8$ R-matrix
computation; both lead to the same
`χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶` identity.

## Significance

The Borromean $h^4 = -3/4$ — the *first topological invariant* of the
Borromean linking, the part of the Jones polynomial that distinguishes
$\mathcal{B}_3$ from the trivial 3-component unlink — is now derived
*from first principles* within $\mathrm{H}_3(q)$. The chain is:

| Step | Source | Result |
|---|---|---|
| 1 | $U_q(\mathfrak{sl}_2)$ R-matrix on $V_{1/2}^{\otimes 3}$ | $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$ |
| 2 | Markov normalisation for $c = 3$ link closure | $y_{(2,1)}(q=1) = 1/4 = 1/[2]_q^2|_{q=1}$ |
| 3 | Combined Frobenius expansion | $h^4(\mathrm{tr}_M) = (-3) \cdot (1/4) = -3/4$ |

The derivation is purely categorical — no empirical fitting, no
free parameters. Each ingredient ($\check{R}$, the Hecke relation, the
Schur–Weyl decomposition, the Markov normalisation $[2]_q^{c-1}$) is a
standard categorical / topological object whose form is determined by
the framework's existing structure.

> **Scope note.** This closes the *within-$\mathrm{H}_3$* categorical
> chain (the 3-strand side of the Borromean story). It does **not**
> resolve the *cross-algebra* obstruction linking 5-strand $A_5$ fiber
> action to 3-strand $\mathrm{H}_3$ — that is the question posed by
> the $S_5 \leftrightarrow \mathrm{SO}(3)$ fibre-action conjecture, and it remains open: eight candidate
> cross-algebra functors have been refuted.

