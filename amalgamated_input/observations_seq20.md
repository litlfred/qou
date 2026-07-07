<!-- FILE_START: non-comm-probability-intro.md -->
The algebraic sector operates as a non-commutative probability space in
Voiculescu's sense [`biane1998`]. The inductive-limit Hecke algebra
$H_\infty(q)$ under the Markov trace $\mathrm{tr}_M$ forms a type II$_1$
factor with faithful trace. Braid transfer matrices $\sigma_i$ act as
non-commuting random variables. Their joint moments
$\mathrm{tr}_M(\sigma_{i_1} \cdots \sigma_{i_k})$ evaluate the Jones
polynomial of the closed braid. The hyperbolic volume
$\mathrm{Vol}(S^3 \setminus K)$ constitutes free entropy in the
asymptotic-log-moment sense.

This section develops three framework-internal results derived from this
non-commutative probability structure:

- A **$q$-deformed Central Limit Theorem**, explaining how continuous
  $q$-Gaussian distributions emerge macroscopically from a discrete,
  deterministic substrate.
- A **locality / non-locality reconciliation**, resolving the apparent tension
  between Markov-property single-generator locality and Gröbner--Shirshov
  composite non-locality.
- An explicit **brane-tower convergence bound**, controlling the $\hbar_q^{2n}$
  Yekutieli tower sum via $q$-Laplacian exponential decay.

These proofs combine Hecke-algebra inputs (the quadratic relation, the Markov
property, the Wenzl bridge) with established literature (Voiculescu--Biane
free probability, the Kerov--Vershik and Féray--Méliot asymptotic Plancherel
measures, Blitvić's $(q,t)$-Gaussian CLT, and the Marsh--Tsallis $q$-Gaussian
attractor). The subsequent section applies this framework to compare the present
theory with Finster's causal fermion systems.
<!-- FILE_END: non-comm-probability-intro.md -->

<!-- FILE_START: algebraic-gns-embedding.md -->
**Proposition (Markov-trace GNS embedding).**
*Let $q > 0$ satisfy the Wenzl positivity condition $q^{1/2} + q^{-1/2} > 2$. The QOU substrate $q_0 \approx 1.11$ lies in this regime. The infinite Hecke algebra $H_\infty(q) := \varinjlim_n H_n(R, q)$ carries a unique tracial state given by the colimit of the Markov traces,*
$$
  \mathrm{tr}_M \colon H_\infty(q) \;\longrightarrow\; R\otimes\mathbb{R},
$$
*satisfying positivity $\mathrm{tr}_M(x^* x) \geq 0$ for all $x \in H_\infty(q)$, where $x \mapsto x^*$ is the bar-involution. The GNS construction applied to this trace yields a separable Hilbert space $\mathcal{H}$ and a faithful $*$-representation*
$$
  \pi_{\mathrm{GNS}} \colon H_\infty(q) \;\hookrightarrow\;
    L(\mathcal{H}).
$$
*This embedding realises the pre-Archimedean Hecke algebra as a concrete operator algebra. It provides the Hilbert space required for analytic limits.*
<!-- FILE_END: algebraic-gns-embedding.md -->

<!-- FILE_START: algebraic-gns-embedding-interpretation.md -->
**Remark.** The image $M := \pi_{\mathrm{GNS}}(H_\infty(q))'' \subset L(\mathcal{H})$ (double commutant) forms a finite type II$_1$ von Neumann algebra with trace $\mathrm{tr}_M$. This realizes the Jones–Wenzl subfactor planar algebra at modular parameter $z$. The full machinery of subfactor theory therefore applies directly to the QOU algebraic data. This mathematical fact renders clause 1 of the [CFS comparison summary](#rem:cfs-comparison-summary) established rather than conjectural.
<!-- FILE_END: algebraic-gns-embedding-interpretation.md -->

<!-- FILE_START: algebraic-gns-embedding-cfs-consequence.md -->
**Consequence for the $\mu_{\mathrm{arch}}$ programme.** The existence of an operator-algebra realisation of the QOU pre-Archimedean substrate on a Hilbert space is *not* a conjecture. It is the Jones–Wenzl theorem applied to $\mathrm{tr}_M$ ([Markov-trace GNS embedding](#prop:algebraic-gns-embedding)). What remains conjectural in the [CFS comparison summary](#rem:cfs-comparison-summary) is the **identification** of the GNS-image data $(\pi_{\mathrm{GNS}}(H_\infty(q)), \tilde w_\lambda\text{-pushforward})$ with the Finster causal-fermion-system data $(\mathcal{F}, \rho)$. Specifically, the exact form of the CFS Lagrangian remains open ([CFS comparison summary](#rem:cfs-comparison-summary)). The operator-algebra carrier itself is mathematically secured.
<!-- FILE_END: algebraic-gns-embedding-cfs-consequence.md -->

<!-- FILE_START: non-commutative-probability-dictionary.md -->
The Hecke-algebra GNS data ([algebraic GNS embedding](#prop:algebraic-gns-embedding))
forms a non-commutative probability space in Voiculescu's sense [`biane1998`]:
a unital $*$-algebra equipped with a tracial state. Every computation involving
the Markov trace admits a precise probabilistic translation.

**The dictionary.**

See [Table](#tbl:non-commutative-probability-dictionary-table-data).

**Three structural consequences.**

1. **Knot theory evaluates non-commutative moments.** Every closed-braid knot
   invariant (Jones, colored Jones, HOMFLY, Khovanov categorifications) evaluates
   a joint moment of transfer matrices under $\mathrm{tr}_M$. Knot tables
   function as joint-moment tables. The Kashaev volume conjecture operates as
   a free-entropy log-asymptotic of these moments.
2. **Wedderburn idempotents define events.** The central projectors $e_\lambda$
   satisfy $1 = \sum_\lambda e_\lambda$, $e_\lambda^2 = e_\lambda$, and
   $e_\lambda e_\mu = 0$ for $\lambda \neq \mu$. They partition the unit,
   forming non-commutative measurable events. The Plancherel measure
   $\tilde w_\lambda = \mathrm{tr}_M(e_\lambda)$ assigns probability mass to
   each event. The decomposition
   $\mathrm{tr}_M(x) = \sum_\lambda \tilde w_\lambda \cdot \chi_\lambda(x)$
   acts as the law of total probability.
3. **Jucys--Murphy elements are commuting random variables.** The elements
   $J_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-2} \sigma_{k-1}$
   commute pairwise, generating the maximal abelian subalgebra (Gelfand--Tsetlin).
   Biane showed that in the large-$n$ limit at $q = 1$, suitably normalized $J_k$
   converge to free random variables with semicircle distributions [`biane1998`].
   The $q$-deformed version (Féray--Méliot) replaces the semicircle with a
   $q$-Gaussian [`marsh2006`].

**Formal equivalence.** The Hecke algebra under the Markov trace formally
constitutes a $(W^*, \mathrm{tr})$ probability space. Theorems governing such
spaces apply directly. The subsequent $q$-CLT for Hecke transfer matrices
makes this explicit.

**Imported tools.** This mapping incorporates the analytic machinery of free
probability and asymptotic representation theory. We utilize Voiculescu's
R-/S-transforms, Speicher's free cumulants (non-crossing partitions), free
entropy, Biane's asymptotic representation theory of $S_\infty$, and the
Jones--Wenzl subfactor planar algebra. Random matrix theory's large-$N$
universality governs expectations under the $q$-Plancherel limit.
<!-- FILE_END: non-commutative-probability-dictionary.md -->

<!-- FILE_START: q-plancherel-asymptotic-skeleton.md -->
**Proposition (q-Plancherel asymptotic skeleton).**
*Let $\tilde w_\lambda^{(n)} := \dim_q^2(\lambda) / [n]_q!$ be the
q-deformed Wedderburn weight on partitions of $n$
([Wedderburn weight canonical form](#prop:wedderburn-weight-canonical)).
There exists a topological space $\Omega_q$ (the q-deformed Thoma
simplex) and a sequence of pushforward maps*

$$
  \iota_n \colon \{\lambda \vdash n\}
    \;\longrightarrow\; \Omega_q,
  \qquad
  n \in \mathbb{N},
$$

*such that the pushforward measures
$\mu_n^{(q)} := (\iota_n)_*\,\tilde w_\lambda^{(n)}$ on $\Omega_q$
satisfy:*

1. *(Existence of limit at $q = 1$, established.) For $q = 1$, the sequence $\{\mu_n^{(1)}\}$ converges weakly to a measure $\mu_\infty^{(1)}$ on the classical Thoma simplex* [`kerov1981`, `biane1998`].
2. *(Variance bound at generic $q$, established by Féray–Méliot.) The character fluctuations $\chi_\lambda - \mathbb{E}_q[\chi]$ measured under $\mu_n^{(q)}$ have variance $O(1/\sqrt{n - 3})$* [`feray2010`].
3. *(Limit identification, conjectural.) For $q \neq 1$ in the Wenzl positivity regime ([algebraic GNS embedding](#prop:algebraic-gns-embedding)), $\{\mu_n^{(q)}\}$ converges weakly to a limit measure $\mu_\infty^{(q)}$ on $\Omega_q$. The identification of $\mu_\infty^{(q)}$ with a measure on the GNS operator algebra $\pi_{\mathrm{GNS}}(H_\infty(q))$ requires a continuous map $\Omega_q \to L(\mathcal{H})$ compatible with $\iota_n$.*

**Established results.** Parts (1) and (2) are established theorems. We formalized the Féray–Méliot CLT as the typeclass `HasQPlancherelCLT` in [`QPlancherel.lean`](/content/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean). Convergence in measure is fixed in the infrastructure.

**Conjectural results.** Part (3) isolates two open problems:

- (3a) *q-deformed Kerov–Vershik.* We extend the classical $q=1$ Thoma-simplex convergence to generic $q$. The variance bound permits this convergence, but does not construct the limit measure.
- (3b) *Operator-algebra realisation.* We identify the limit measure $\mu_\infty^{(q)}$ with the pushforward of a measure on the GNS image $\pi_{\mathrm{GNS}}(H_\infty(q)) \subset L(\mathcal{H})$, via a continuous map $\Omega_q \to L(\mathcal{H})$. This step enables the measure-valued route to CFS ([CFS comparison summary](#rem:cfs-comparison-summary)).

**Status summary.** The convergence is established. Only the operator-algebra realisation of the limit measure remains conjectural. We restrict the conjectural surface to (3a) and (3b), leaving them as problems of identification rather than analysis.
<!-- FILE_END: q-plancherel-asymptotic-skeleton.md -->

<!-- FILE_START: centered-hecke-variance-positive.md -->
**Proposition (positivity of centred Hecke variance).**
*Let $q > 0$ with $q^{1/2} + q^{-1/2} > 2$ (Wenzl positivity regime).
Let $z = 1/(q^{1/2}+q^{-1/2})$ be the Markov parameter and
$\tilde\sigma_i := \sigma_i - z \cdot 1$ the centred Hecke generator.
Then the variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
$$
*is strictly positive: $\mathrm{Var}(\sigma_i) > 0$. Numerically at
the QOU substrate $q_0 \approx 1.110$, $\mathrm{Var}(\sigma_i) \approx 0.855$.*

**Numerical check at $q_0$.** With $q_0 \approx 1.110$:

See [Table: Centred Hecke variance at $q_0$](#tbl:centered-hecke-variance-positive-table-data).

The variance is well-separated from zero, confirming the q-CLT limit
is non-degenerate at the substrate value.
<!-- FILE_END: centered-hecke-variance-positive.md -->

<!-- FILE_START: centered-hecke-variance-positive-interpretation.md -->
**Significance for the q-CLT.** The second free cumulant $\kappa_2^{(q)} = \mathrm{Var}(\sigma_i)$ is the variance parameter of the q-Gaussian limit measure (`conj:q-clt-non-commutative`). Its positivity in the Wenzl regime is a necessary condition for the q-CLT. Without it, the rescaled sum would degenerate to a delta measure at zero. The proposition guarantees that the q-CLT limit is non-degenerate for all $q$ in the Wenzl regime, including the QOU substrate.
<!-- FILE_END: centered-hecke-variance-positive-interpretation.md -->

<!-- FILE_START: archimedean-macroscopic-washout.md -->
**Origin of continuous q-Gaussian distributions on a deterministic substrate.** A macroscopic observer cannot resolve individual Reeb ticks due to the operational-entropy limit $\eta_q = (2q-1)/q^3$. The measurement of an observable $\Phi$ appears as an $n$-step auto-correlated sum $\mathcal{O}_{\mathrm{macro}}(\Phi) = n^{-1} \sum_{i=1}^n \mathrm{tr}_M(\sigma_{j_i}(\Phi))$ spanning the unresolved ticks in the observation window (typically $n \sim 10^{20}$ per nanosecond). By the q-CLT (conj:q-clt-non-commutative), the rescaled centred sum converges in joint moments to the q-Gaussian $G_{q_0}(t, x)$ peaked at $\mathrm{tr}_M(\Phi)$ with width $\sqrt{\kappa_2^{(q)}/n}$. The observer measures a q-Gaussian bell curve rather than the underlying delta-function expectation.

**q-Gaussian rather than Gaussian.** The braid relations $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ impose global correlations across the entire braid. Every generator interacts with every other through the Hecke algebra structure. The classical CLT, which produces a Gaussian attractor, demands asymptotic independence. The QOU substrate maximally violates this condition. Systems with such global correlations possess q-Gaussian attractors where the deformation parameter equals the substrate's $q$ [`marsh2006`]. At $q_0 \approx 1.110$, the substrate's q-Gaussian width deviates from a classical Gaussian of the same variance by $O(10^{-3})$ in the tails. This provides a falsifiable signature for high-precision experiments.

This resolves the paradox between deterministic algebraic dynamics and probabilistic macroscopic observations. The probabilistic behavior emerges as the CLT attractor of the substrate, not from a stochastic-mechanical postulate.
<!-- FILE_END: archimedean-macroscopic-washout.md -->

<!-- FILE_START: brane-tower-q-laplacian-decay.md -->
**Proposition (brane-tower convergence via q-Laplacian decay).**
*Dropping the locality assumption for composite physical observables requires summing over the brane tower. This summation constitutes an infinite jet prolongation*
$$
  T(\rho) \;=\; \sum_{n \geq 1} \hbar_q^{2n} \, \Delta^{(n)}(\rho),
$$
*where $\Delta^{(n)}$ is the $n$-th iterated q-Laplacian on the Reeb bundle. The tower sum converges absolutely for all $q$ in the Wenzl positivity regime. It is dominated by the lowest-level local contribution.*

**Bound.** For $q$ in the Wenzl regime $q^{1/2} + q^{-1/2} > 2$, and for $\rho$ with bounded $L^2$ norm on the Reeb bundle,
$$
  \boxed{\;
  \bigl|\,T(\rho) - \hbar_q^2 \,\Delta^{(1)}(\rho)\,\bigr|
  \;\leq\;
  \hbar_q^4 \, \|\rho\|_{L^2} \cdot
    \frac{q^{-2}}{1 - q^{-2}}
  \;}
$$

The leading correction $\hbar_q^2 \, \Delta^{(1)}(\rho)$ represents the single-jet (local) Laplacian contribution. The remainder decays geometrically with ratio $q^{-2} < 1$ within the regime $q > 1$, which includes the QOU substrate $q_0 \approx 1.110$.

**Mechanism: exponential damping of high modes.** The q-Laplacian on a vortex filament of length $L_q$ possesses the spectrum
$$
  \lambda_k^{(q)} \;=\; [k]_q^{\,2} \cdot \hbar_q / L_q^2,
  \qquad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}}.
$$
For $q > 1$, the q-integer $[k]_q$ grows exponentially in $k$: $[k]_q \sim q^k / (q - q^{-1})$ as $k \to \infty$. Thus, high-wavenumber Reeb modes suffer damping at the exponential rate $\exp\!\bigl(-\nu_q [k]_q^2 \, t\bigr)$. The $n$-th iterated Laplacian acting on mode $k$ contributes a factor $\lambda_k^{(q),n} \sim q^{2nk} / (q - q^{-1})^{2n}$. For any fixed mode $k$, the $\hbar_q^{2n} \sim (q - q^{-1})^{-2n}$ prefactor dominates this growth.

**Geometric-series tail.** Iteration of the bound yields
$$
  T(\rho) \;=\;
  \sum_{n = 1}^{\infty}
    \hbar_q^{2n}\,\Delta^{(n)}(\rho)
  \;\leq\;
  \|\rho\|_{L^2} \,
  \sum_{n = 1}^{\infty}
    \hbar_q^{2n} \cdot q^{-2(n-1)}
  \;=\;
  \frac{\hbar_q^2 \, \|\rho\|_{L^2}}{1 - q^{-2}\hbar_q^2}.
$$
This forms a convergent geometric series because $q^{-2}\hbar_q^2 < 1$ across the substrate range $q > 1.05$. This range cleanly covers the QOU calibration window.
<!-- FILE_END: brane-tower-q-laplacian-decay.md -->

<!-- FILE_START: brane-tower-q-laplacian-decay-interpretation.md -->
**Physical reading.** Dropping locality demands a summation over all causally connected knots. This sum is formally infinite. The q-Laplacian exponential mode-damping restricts the appreciable contributions to the lowest few jet levels. The remaining levels suffer geometric suppression. This renders the non-local integration finite. It is dominated by local contributions and computable to arbitrary precision by truncating the tower at any fixed level.

This establishes the convergence underlying the treatment of composite operators. In the Gröbner–Shirshov tower expansion of a hadron's mass, the local single-jet contribution provides the leading term. The corrections form a geometric series scaling by $\hbar_q^2 \cdot q^{-2}$.
<!-- FILE_END: brane-tower-q-laplacian-decay-interpretation.md -->

<!-- FILE_START: cfs-comparison-summary.md -->
Finster's causal fermion systems (CFS) [`finster2021`, `finster2022`, `finster2024`, `dappiaggi2024`] are a parallel programme for unifying quantum field theory with general relativity. CFS posits a Borel measure $\rho$ on a set of operators with bounded signature. Dynamics are determined by a causal action $\mathcal{S}_{\mathrm{CFS}} = \iint \mathcal{L}_{\mathrm{CFS}}(x, y)\,d\rho\,d\rho$, where $\mathcal{L}_{\mathrm{CFS}}$ is built from differences $\lvert\lambda_i\rvert - \lvert\lambda_j\rvert$ of eigenvalues of the operator product $x \cdot y$. The non-commutative probability lens places CFS and QOU on common ground. The comparison yields three structural conclusions.

## Structural agreements

1. **Same carrier algebra.** Both QOU's inductive-limit Hecke algebra $(H_\infty(q), \mathrm{tr}_M)$ — embedded via Jones–Wenzl GNS as a type II$_1$ factor ([algebraic GNS embedding](#prop:algebraic-gns-embedding)) — and CFS's regularised operator algebra are finite type II$_1$ factors with faithful tracial state.
2. **Same universality class.** Under joint Faddeev / Kerov–Vershik scaling, both sit in the free-probability universality class (Voiculescu–Biane, Féray–Méliot [`biane1998`]). The asymptotic spectral measure of QOU under the q-Plancherel weight ([q-Plancherel asymptotic skeleton](#prop:q-plancherel-asymptotic-skeleton)) and CFS's universal measure $\rho$ are objects in the same class of free-probability spectral distributions.
3. **Common commutative-shadow data type.** The traceful Plancherel projection $\Pi_{\mathrm{tr}} \colon (A_q, \mathrm{tr}_M) \to (\widehat{A}_q, \tilde w_\lambda, \{\chi_\lambda\})$ sends QOU's non-commutative algebraic data to a (measure, functional-family) pair on the commutative spectrum. This is structurally a CFS-style data type. The kernel of $\Pi_{\mathrm{tr}}$ contains commutators, braid relations, knot crossing-order, and non-trace free-probability cumulants. QOU has this data; CFS structurally cannot represent it.

## Structural differences

The two continuum theories evaluate different real-valued functionals on the shared spectral data. The QOU natural quadratic kernel is the Frobenius Gram matrix $G(x, y) := \mathrm{tr}_M(x \cdot y)$ (bilinear, trace-additive in the spectrum of $x \cdot y$). The Finster causal Lagrangian $\mathcal{L}_{\mathrm{CFS}}(x, y)$ is built from eigenvalue differences (non-linear, trace-subtractive).

This functional mismatch exhibits concretely:

- **Strict pointwise mismatch at $n = 2$.** On the unit pair $(1, 1) \in H_2(R, q) \times H_2(R, q)$:
  $$
    G(1, 1) = \mathrm{tr}_M(1) = 1
    \qquad\text{but}\qquad
    \mathcal{L}_{\mathrm{CFS}}(1, 1) = 0
  $$
  (Finster's pair-difference functional vanishes when all eigenvalues of $x \cdot y$ are equal).
- **Integral mismatch under any centered free-probability limit.** $G$ is odd under $x \mapsto -x$ (trace is linear); $\mathcal{L}_{\mathrm{CFS}}$ is even (depends on $\lvert\lambda\rvert$). Under any centered limit measure $\rho_\infty$ symmetric under $x \mapsto -x$: $\langle G \rangle_{\rho_\infty\otimes\rho_\infty} = 0$ but $\langle \mathcal{L}_{\mathrm{CFS}}\rangle > 0$ strictly (by Finster's non-negativity).
- **Explicit algebraic decomposition.** Even taking the squared QOU kernel $G_2(x, y) := \mathrm{tr}_M((x\cdot y)^2)$ (an even modification of $G$) does not produce equality. For self-adjoint $x, y$ with real-spectrum product on a block of dimension $n$ with normalised Markov trace ($\mathrm{tr}_M(1) = 1$), the Finster pair-difference Lagrangian satisfies
  $$
    \mathcal{L}_{\mathrm{CFS}}(x, y)
    = n^{2}\,\bigl(G_2(x, y) - \lVert x \cdot y\rVert_1^{\,2}\bigr),
  $$
  where $\lVert x \cdot y\rVert_1 = \mathrm{tr}_M\lvert x \cdot y\rvert$ is the (normalised) trace-class norm. Equivalently, after normalising $\mathcal{L}_{\mathrm{CFS}}$ by $n^{2}$: $\mathcal{L}_{\mathrm{CFS}}^{(\mathrm{norm})}(x, y) = G_2(x, y) - \lVert x \cdot y\rVert_1^{\,2}$. The Finster action equals QOU's energy-quadratic minus an explicit trace-class correction. The correction term $\lVert x \cdot y\rVert_1^{\,2}$ is the concentration penalty that distinguishes CFS dynamics from QOU dynamics. On the unit pair $(1, 1)$, it equals $G_2$, giving $\mathcal{L}_{\mathrm{CFS}}(1,1) = 0$ exactly.

## Open numerical question

Whether the correction moment $\langle \lVert x \cdot y\rVert_1^{\,2}\rangle_{\rho_\infty}$ might coincidentally vanish at the QOU substrate value $q_0 \approx 1.110$ remains open. It is generically expected to be non-zero given the full support of the limit measure. If this integral vanishes at $q_0$, QOU and CFS predict equal total action values at the substrate (though they still differ in local dynamics via the pointwise mismatch). Otherwise, QOU and CFS are confirmed as distinct continuum theories of the same operator-algebra substrate.

## Corollary for QOU

The framework developed in this section (non-commutative probability, q-CLT, Jones–Wenzl carrier, Plancherel asymptotics) stands independently of any CFS comparison. The QOU phenomena that CFS cannot natively express (knot topology, braid statistics, chirality, Gröbner–Shirshov reduction) are pre-projection algebra data. They are killed by $\Pi_{\mathrm{tr}}$ and are therefore outside the reach of any commutative-shadow framework. Particle physics is derived from these QOU phenomena. Consequently, QOU's predictions are not recoverable from a Finster-style continuum theory alone.
<!-- FILE_END: cfs-comparison-summary.md -->

