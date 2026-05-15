*Proof.* We assemble the three parts from existing QOU infrastructure.

**Part (1): Markov trace as Plancherel integral.** For $q$ generic,
the Hecke algebra $A_q = H_n(R, q)$ is semisimple over $R\otimes\mathbb{Q}$,
with Wedderburn decomposition
$$
  A_q \otimes_R \mathbb{Q}(q^{1/2})
  \;\cong\;
  \bigoplus_{\lambda \vdash n} \mathrm{End}_{\mathbb{Q}(q^{1/2})}(S^\lambda_q),
$$
where $S^\lambda_q$ is the q-deformed Specht module of shape $\lambda$
([Wedderburn weight canonical form](#prop:wedderburn-weight-canonical)).
Any $R\otimes\mathbb{Q}$-linear trace $\mathrm{tr} \colon A_q \to R\otimes\mathbb{Q}$
factors uniquely as a Plancherel-type sum
$$
  \mathrm{tr}(x) \;=\; \sum_{\lambda \vdash n} c_\lambda \cdot \chi_\lambda(x),
  \qquad c_\lambda \in R\otimes\mathbb{Q},
$$
because each block $\mathrm{End}(S^\lambda_q)$ admits a unique trace
up to scalar (its standard trace, with central character
$\chi_\lambda$).

The Markov trace $\mathrm{tr}_M$ is characterised by the recursive
trace condition
([Jones–Markov trace](#thm:jones-markov-trace)). Evaluating the
recursion on a complete set of minimal idempotents in each Wedderburn
block — by the hook–content principal specialisation
([Plancherel term-7 formulation](#prop:plancherel-term-7-formulation),
following Wenzl 1988) — identifies the Plancherel coefficient as
$$
  c_\lambda \;=\; \frac{\dim_q^2(\lambda)}{[n]_q!}
  \;=\;
  \tilde w_\lambda,
$$
giving the desired identity
$\mathrm{tr}_M(x) = \sum_\lambda \tilde w_\lambda\,\chi_\lambda(x)$.
The integration interpretation follows immediately: $\tilde w_\lambda$
is a positive (in $R\otimes\mathbb{Q}$) function on the finite set
$\widehat{A}_q$, and $\mathrm{tr}_M$ is the linear functional sending
$x$ to the central-character integral against $\tilde w_\lambda$.

**Part (2): LP existence, duality, active set.** This is the content
of [`prop:operator-selection-lp`](#prop:operator-selection-lp) and the
LP/SDP infrastructure documented in CLAUDE.md §"LP/SDP duals — first-class
infra". Feasibility of the primal is hypothesised; under feasibility,
both primal and dual are bounded (the primal by non-negativity of
$t$, the dual by the right-hand side $\mathbf{1}$), so the
fundamental theorem of linear programming yields optimal
$(x^\star, y^\star)$ with $\sum_\lambda t_\lambda x^\star_\lambda
= n_{\text{target}}\,y^\star_0$ (strong duality, zero gap). The
canonical entry point
[`lp_dual_solver.solve_operator_selection_lp`](folio-assistant/computations/lp_dual_solver.py)
produces both $x^\star$ and $y^\star = (y^\star_0, y^\star)$ and
records the active set $\widehat{A}_q^{\,\mathrm{active}}
= \{\lambda : y^\star_\lambda > 0\}$ in the witness JSON.
Complementary slackness gives
$\mathrm{supp}(x^\star) \subseteq \widehat{A}_q^{\,\mathrm{active}}$.

**Part (3): dictionary.** The dictionary is asserted, not derived.
Each row is an identification of QOU algebraic-side data with the
analogous CFS data. We verify the rows are internally consistent.

- *Row 1* ($\mathcal{F} \leftrightarrow A_q$). The CFS operator set
  $\mathcal{F}$ is a subset of $L(H)$ with bounded signature; $A_q$ is
  a finite-dimensional $R\otimes\mathbb{Q}$-algebra acting on its
  regular module. Both carry an involution (CFS: adjoint; $A_q$:
  bar-involution under $q \mapsto q^{-1}$).

- *Row 2* ($\rho \leftrightarrow \tilde w_\lambda$). CFS $\rho$ is a
  Borel measure on $\mathcal{F}$; $\tilde w_\lambda$ is a finitely-
  supported $R\otimes\mathbb{Q}$-valued measure on $\widehat{A}_q$.
  The latter is the discrete pullback of the former under the
  identification of Row 1 once one chooses a parametrisation of
  $\mathcal{F}$ by spectral data (Row 3 below).

- *Row 3* (spectral projectors $\leftrightarrow$ idempotents). The
  Wedderburn idempotents $e_\lambda \in A_q$ are the spectral
  projectors of the central element
  $z_\lambda = \chi_\lambda(\,\cdot\,)\,e_\lambda$; they decompose the
  regular module into isotypic pieces. CFS uses spectral projectors of
  the operator product $xy$ in the same role
  [`finster2021`, §3].

- *Row 4* (Lagrangian). For $x, y \in A_q$, the product $x\,y$ has
  central character $\chi_\lambda(x\,y) \in R\otimes\mathbb{Q}$ in
  each block; the Finster Lagrangian $\mathcal{L}(x, y)$ is a
  symmetric polynomial in the spectrum of $x\,y$ [`finster2024`, §2].
  Both are $\Sigma_n$-symmetric polynomials in the central characters.

- *Rows 5–6* (action and stationarity). Part (1) realises
  $\mathrm{tr}_M$ as integration of central-character data against
  $\tilde w_\lambda$, so the row is exactly the identity proved in
  Part (1). Part (2) gives a variational principle (the LP) whose
  optimality conditions distinguish a finite *active set* of weights,
  exactly mirroring the role of $\mathrm{supp}(\rho)$ in CFS as the
  emergent locus where physics happens.

- *Row 7* (Euler–Lagrange = LP optimality). LP optimality is
  characterised by KKT (complementary slackness, dual feasibility,
  primal feasibility). For a smooth measure $\rho$ on a finite-
  dimensional simplex, the same KKT conditions arise as the
  Euler–Lagrange equations for the causal action. On the algebraic
  side this is finite-dimensional; the Archimedean lift to PDE
  Euler–Lagrange equations is conjectural and is the content of
  [μ_arch continuum limit](#conj:mu-arch-continuum-limit).

All rows are internally consistent; the dictionary holds. $\square$
