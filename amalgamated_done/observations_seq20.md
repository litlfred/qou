<!-- FILE_START: non-comm-probability-intro.md -->
The algebraic sector forms a non-commutative probability space [`biane1998`]. The inductive-limit Hecke algebra $H_\infty(q)$ under the Markov trace $\mathrm{tr}_M$ yields a type II$_1$ factor. Braid transfer matrices $\sigma_i$ operate as non-commuting random variables. Their joint moments $\mathrm{tr}_M(\sigma_{i_1} \cdots \sigma_{i_k})$ evaluate the Jones polynomial. The hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ defines free entropy.

We develop three framework-internal results:

- A **$q$-deformed Central Limit Theorem**. We explain how continuous $q$-Gaussian distributions emerge macroscopically.
- A **locality / non-locality reconciliation**. We resolve the tension between Markov-property single-generator locality and Gröbner--Shirshov composite non-locality.
- An explicit **brane-tower convergence bound**. We control the $\hbar_q^{2n}$ Yekutieli tower sum via $q$-Laplacian exponential decay.

These proofs combine Hecke-algebra inputs with non-commutative probability literature. We subsequently compare this framework with causal fermion systems.
<!-- FILE_END: non-comm-probability-intro.md -->

<!-- FILE_START: algebraic-gns-embedding.md -->
**Proposition (Markov-trace GNS embedding).**
*Let $q > 0$ satisfy the Wenzl positivity condition $q^{1/2} + q^{-1/2} > 2$. The QOU substrate $q_0 \approx 1.11$ lies here. The infinite Hecke algebra $H_\infty(q) := \varinjlim_n H_n(R, q)$ carries a unique tracial state $\mathrm{tr}_M \colon H_\infty(q) \to R\otimes\mathbb{R}$ satisfying positivity $\mathrm{tr}_M(x^* x) \geq 0$. The GNS construction yields a separable Hilbert space $\mathcal{H}$ and a faithful $*$-representation*
$$
  \pi_{\mathrm{GNS}} \colon H_\infty(q) \;\hookrightarrow\;
    L(\mathcal{H}).
$$
*This embeds the pre-Archimedean Hecke algebra as a concrete operator algebra.*
<!-- FILE_END: algebraic-gns-embedding.md -->

<!-- FILE_START: algebraic-gns-embedding-interpretation.md -->
**Remark.** The image $M := \pi_{\mathrm{GNS}}(H_\infty(q))''$ forms a finite type II$_1$ von Neumann algebra. This realizes the Jones–Wenzl subfactor planar algebra. The subfactor theory machinery applies directly to the QOU algebraic data. This establishes clause 1 of the [CFS comparison summary](#rem:cfs-comparison-summary).
<!-- FILE_END: algebraic-gns-embedding-interpretation.md -->

<!-- FILE_START: algebraic-gns-embedding-cfs-consequence.md -->
**Consequence for the $\mu_{\mathrm{arch}}$ programme.** The operator-algebra realisation of the QOU pre-Archimedean substrate derives from the Jones–Wenzl theorem ([Markov-trace GNS embedding](#prop:algebraic-gns-embedding)). The [CFS comparison summary](#rem:cfs-comparison-summary) conjectures only the identification of the GNS-image data with causal-fermion-system data $(\mathcal{F}, \rho)$. The exact CFS Lagrangian form remains open.
<!-- FILE_END: algebraic-gns-embedding-cfs-consequence.md -->

<!-- FILE_START: non-commutative-probability-dictionary.md -->
The Hecke-algebra GNS data ([algebraic GNS embedding](#prop:algebraic-gns-embedding)) provides a non-commutative probability space [`biane1998`]. 

**The dictionary.**

See [Table](#tbl:non-commutative-probability-dictionary-table-data).

**Three structural consequences.**

1. **Knot theory evaluates non-commutative moments.** Closed-braid knot invariants evaluate joint transfer matrix moments under $\mathrm{tr}_M$. The Kashaev volume conjecture operates as a free-entropy log-asymptotic.
2. **Wedderburn idempotents define events.** The central projectors $e_\lambda$ partition the unit. The Plancherel measure $\tilde w_\lambda = \mathrm{tr}_M(e_\lambda)$ assigns probability mass.
3. **Jucys--Murphy elements are commuting random variables.** Biane proved large-$n$ $J_k$ elements converge to semicircle distributions at $q = 1$ [`biane1998`]. The $q$-deformed version (Féray--Méliot) yields a $q$-Gaussian [`marsh2006`].

**Formal equivalence.** The Hecke algebra under the Markov trace operates as a $(W^*, \mathrm{tr})$ probability space. 

**Imported tools.** We utilize Voiculescu's R-/S-transforms, Speicher's free cumulants, free entropy, and Biane's asymptotic representation theory.
<!-- FILE_END: non-commutative-probability-dictionary.md -->

<!-- FILE_START: q-plancherel-asymptotic-skeleton.md -->
**Proposition (q-Plancherel asymptotic skeleton).**
*Let $\tilde w_\lambda^{(n)} := \dim_q^2(\lambda) / [n]_q!$ be the q-deformed Wedderburn weight ([Wedderburn weight canonical form](#prop:wedderburn-weight-canonical)). We define a topological space $\Omega_q$ and pushforward maps*

$$
  \iota_n \colon \{\lambda \vdash n\}
    \;\longrightarrow\; \Omega_q,
  \qquad
  n \in \mathbb{N},
$$

*such that $\mu_n^{(q)} := (\iota_n)_*\,\tilde w_\lambda^{(n)}$ satisfy:*

1. *(Existence at $q = 1$.) The sequence $\{\mu_n^{(1)}\}$ converges weakly to $\mu_\infty^{(1)}$* [`kerov1981`, `biane1998`].
2. *(Variance bound at generic $q$.) Character fluctuations have variance $O(1/\sqrt{n - 3})$* [`feray2010`].
3. *(Limit identification, conjectural.) For $q \neq 1$, $\{\mu_n^{(q)}\}$ converges weakly to $\mu_\infty^{(q)}$. We identify $\mu_\infty^{(q)}$ with a measure on $\pi_{\mathrm{GNS}}(H_\infty(q))$.*

**Established results.** Parts (1) and (2) hold. We formalized the Féray–Méliot CLT in `QPlancherel.lean`.
**Conjectural results.** Part (3) isolates two open problems: q-deformed Kerov–Vershik convergence and operator-algebra realisation.
<!-- FILE_END: q-plancherel-asymptotic-skeleton.md -->

<!-- FILE_START: centered-hecke-variance-positive.md -->
**Proposition (positivity of centred Hecke variance).**
*Let $q^{1/2} + q^{-1/2} > 2$. Let $z = 1/(q^{1/2}+q^{-1/2})$ and $\tilde\sigma_i := \sigma_i - z \cdot 1$. The variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
$$
*is strictly positive. At $q_0 \approx 1.110$, $\mathrm{Var}(\sigma_i) \approx 0.855$.*

See [Table: Centred Hecke variance at $q_0$](#tbl:centered-hecke-variance-positive-table-data). The variance is well-separated from zero.
<!-- FILE_END: centered-hecke-variance-positive.md -->

<!-- FILE_START: centered-hecke-variance-positive-interpretation.md -->
**Significance for the q-CLT.** The second free cumulant $\kappa_2^{(q)} = \mathrm{Var}(\sigma_i)$ prevents q-Gaussian degeneration. This guarantees a non-degenerate q-CLT limit across the Wenzl regime.
<!-- FILE_END: centered-hecke-variance-positive-interpretation.md -->

<!-- FILE_START: archimedean-macroscopic-washout.md -->
**Origin of continuous distributions.** Macroscopic observers measure auto-correlated sums $\mathcal{O}_{\mathrm{macro}}(\Phi) = n^{-1} \sum \mathrm{tr}_M(\sigma_{j_i}(\Phi))$. By the q-CLT, the rescaled sum converges to a q-Gaussian $G_{q_0}(t, x)$ peaked at $\mathrm{tr}_M(\Phi)$ with width $\sqrt{\kappa_2^{(q)}/n}$. 

**q-Gaussian rather than Gaussian.** Braid relations impose global correlations. Systems with global correlations possess q-Gaussian attractors [`marsh2006`]. At $q_0 \approx 1.110$, the width deviates from a Gaussian. The probabilistic macroscopic behavior emerges as the CLT attractor.
<!-- FILE_END: archimedean-macroscopic-washout.md -->

<!-- FILE_START: brane-tower-q-laplacian-decay.md -->
**Proposition (brane-tower convergence via q-Laplacian decay).**
*Summing over the brane tower yields the infinite jet prolongation*
$$
  T(\rho) \;=\; \sum_{n \geq 1} \hbar_q^{2n} \, \Delta^{(n)}(\rho).
$$
*The tower sum converges absolutely. It is dominated by the local contribution.*

**Bound.** For $q^{1/2} + q^{-1/2} > 2$ and bounded $L^2$ norm:
$$
  \boxed{\;
  \bigl|\,T(\rho) - \hbar_q^2 \,\Delta^{(1)}(\rho)\,\bigr|
  \;\leq\;
  \hbar_q^4 \, \|\rho\|_{L^2} \cdot
    \frac{q^{-2}}{1 - q^{-2}}
  \;}
$$
The remainder decays geometrically with ratio $q^{-2} < 1$.

**Mechanism.** High-wavenumber Reeb modes suffer exponential damping. For any fixed mode $k$, the $\hbar_q^{2n} \sim (q - q^{-1})^{-2n}$ prefactor dominates. The geometric series converges because $q^{-2}\hbar_q^2 < 1$.
<!-- FILE_END: brane-tower-q-laplacian-decay.md -->

<!-- FILE_START: brane-tower-q-laplacian-decay-interpretation.md -->
**Physical reading.** Non-local integration restricts appreciable contributions to the lowest jet levels. The local single-jet contribution leads. Corrections form a geometric series. 
<!-- FILE_END: brane-tower-q-laplacian-decay-interpretation.md -->

<!-- FILE_START: cfs-comparison-summary.md -->
Finster's causal fermion systems (CFS) [`finster2021`] provide a parallel unification programme. The non-commutative probability lens places CFS and QOU on common ground.

## Structural agreements

1. **Same carrier algebra.** Both embed as finite type II$_1$ factors.
2. **Same universality class.** Both occupy the free-probability universality class.
3. **Common commutative-shadow data type.** The traceful Plancherel projection maps non-commutative algebraic data to a commutative spectrum measure.

## Structural differences

QOU evaluates the Frobenius Gram matrix $G(x, y) := \mathrm{tr}_M(x \cdot y)$. The Finster causal Lagrangian $\mathcal{L}_{\mathrm{CFS}}(x, y)$ evaluates eigenvalue differences.

This yields functional mismatches:
- **Pointwise mismatch.** $G(1, 1) = 1$ but $\mathcal{L}_{\mathrm{CFS}}(1, 1) = 0$.
- **Integral mismatch.** $G$ is odd under $x \mapsto -x$; $\mathcal{L}_{\mathrm{CFS}}$ is even.
- **Algebraic decomposition.** $\mathcal{L}_{\mathrm{CFS}}^{(\mathrm{norm})}(x, y) = G_2(x, y) - \lVert x \cdot y\rVert_1^{\,2}$.

## Open numerical question

Whether the correction moment vanishes at $q_0 \approx 1.110$ remains open. 

## Corollary for QOU

The QOU phenomena (knot topology, braid statistics) are pre-projection algebra data. They lie outside any commutative-shadow framework.
<!-- FILE_END: cfs-comparison-summary.md -->
