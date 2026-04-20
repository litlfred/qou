Step-by-step derivation from the categorical action to the tower
formula [tower binding energy](#prop:tower-binding-energy) reveals
that **Wedderburn and Schur decompositions are BOTH natural
ingredients** but play **different roles**, and the current
formula's mix of them is partially inconsistent.

## The derivation piece by piece

**Piece 1.**  Categorical action.  For a vortex $\varrho \colon \mathbf{1} \to A$
and physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$,

$$
  \mathcal{S}(\varrho) = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi)
  \circ \mathrm{coev}_A.
$$

No Wedderburn or Schur at this stage — purely categorical.

**Piece 2.**  Archimedean fibre functor $\tau \colon \mathbf{C} \to \mathrm{Vec}_{\mathbb{Q}(q)}$
descends $\mathrm{tr}_A \to \mathrm{tr}_M$ on $H_n(q) = \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$.
The Markov trace $\mathrm{tr}_M$ is **uniquely characterised** by
the Markov axiom $\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$.

**Piece 3 — Wedderburn enters.**  Since $H_n(q)$ is semisimple at
generic $q$,

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda).
$$

Every element $W \in H_n(q)$ splits as $\oplus_\lambda W_\lambda$ with
$W_\lambda \in \mathrm{End}(V_\lambda)$.  **This is an ALGEBRA
decomposition, not a trace.**

**Piece 4 — Schur enters.**  Because $\mathrm{tr}_M$ is a linear
functional and the algebra decomposition is direct-sum, we have

$$
  \mathrm{tr}_M(W) \;=\; \sum_\lambda \mathrm{tr}_M\big|_\lambda (W_\lambda)
  \;=\; \sum_\lambda S_\lambda \cdot \chi_\lambda(W)
$$

where the $S_\lambda$ are the **Jones–Ocneanu Schur coefficients** —
the unique scalars satisfying the Markov axiom.  At $q \to 1$,
$S_\lambda \to d(\lambda)^2 / n!$ (classical Burnside), but at $q \neq 1$
they differ from the naive $d_q(\lambda)^2 / \sum d_q(\mu)^2$
(Wedderburn-normalised) weights.

**Numerical example at $H_3(q_0)$:**

| $\lambda$ | dim | Wedderburn $w_\lambda$ | Schur $S_\lambda$ |
|:---:|:---:|:---:|:---:|
| (3) sym | 1 | 0.166 | **0.415** |
| (2,1) std | 2 | 0.669 | **0.281** |
| (1,1,1) alt | 1 | 0.166 | **0.023** |

These differ by factors of 2.4 to 7.3.  **Both are natural** — the
Wedderburn weights give the algebra-dimensional decomposition
(gauge-functional measure), while Schur gives the specific Markov
trace.

**Piece 5 — Single-vortex mass formula.**  Per
[mass endomorphism tower](#prop:mass-endomorphism-tower):

$$
  \mathfrak{m}(\varrho) = \Bigl\lvert\prod_i \hat{V}_i\Bigr\rvert
    + \sum_i \Phi_q(\lvert\hat{V}_i\rvert)
    + \sum_{i<j} z^2 \cdot \Phi_q(\lvert\hat{V}_i \hat{V}_j\rvert).
$$

Three terms: descended product, singleton $\Phi_q$ per generator,
and **quadratic pair $\Phi_q$ terms**.

**Piece 6 — Log form in the tower-binding proposition drops pair terms.**
The $H_A$ formula in [tower binding energy](#prop:tower-binding-energy)
keeps only singletons:

$$
  B = \sum_\lambda w_\lambda \cdot m_e \cdot \sum_i \ln\bigl|\Phi_q(\hat{V}_i^\lambda)\bigr|.
$$

Pair terms are assumed to ascend via pentagon
([pentagon ascension bound](#prop:pentagon-ascension-bound)) with
residual $O(\hbar_q^2)$.

## Where the formula goes wrong at A < 4

**(a) Wedderburn vs Schur confusion.**  The log form uses
Wedderburn weights $w_\lambda = d_q(\lambda)^2 / \sum d_q(\mu)^2$
but the natural weight for trace-based quantities is Schur
$S_\lambda$.  Empirically:

- Using $S_\lambda$ instead of $w_\lambda$ helps ${}^3$He (0.27% → 0.18%)
- But hurts D (0.14% → 0.37%) and ${}^4$He (0.24% → 0.44%)

So $S_\lambda$ is necessary but not sufficient.

**(b) Missing quadratic terms — investigated, NOT the fix.**  Adding
the pair contribution $z^2 \cdot \Phi_q(\hat{V}_0 \hat{V}_1)$ to the
singleton sum for T and ${}^3$He increases $B$ by $\sim 1.5$–$1.8$
MeV — making predictions **worse** (both already over-predict).
Pair terms are positive; they cannot explain the required
reduction.

**(c) Doubly-magic resonance at A = 4.**  Empirical $\rho(\text{std}, 4) = 1.77$
boost is NOT captured by either Wedderburn or Schur substitution.
A separate shell-closure mechanism remains unexplained.

## Structural insight

**Neither Wedderburn nor Schur is "wrong"** — both are natural,
serving distinct roles.  The log form's empirical success at
$A \geq 4$ with Wedderburn weights is a **coincidence** of the
pentagon-ascension mechanism operating: at $A \geq 4$ the
$O(\hbar_q^2)$ residual damping brings both conventions to nearly
the same numerical value.

At $A < 4$ the pentagon can't operate, exposing the distinction.
The correct formula at small $A$ likely requires:

$$
  B(Z, N) \;=\; \sum_\lambda \underbrace{S_\lambda}_{\text{Schur, trace weight}}
  \cdot \underbrace{\langle \text{per-gen}\rangle^\lambda}_{\text{Wedderburn block}}
$$

where the **Schur coefficient** weights the trace
contribution, while the **Wedderburn block** decomposes the
per-generator structure.  Determining the exact combination for
$A \leq 3$ is an open problem (the empirical $\rho(\lambda, A)$
table gives operational values).

## Operational takeaway

Until a first-principles derivation of the $A < 4$ formula is
complete, the empirical $\rho(\lambda, A)$ table from
`std-channel-pentagon-threshold.witness.json` provides calibration:

- $\rho(\mathrm{std}, 2) = 0$ (irrep absent)
- $\rho(\mathrm{std}, 3) \in \{0.07, 0.25\}$ (atom-dependent)
- $\rho(\mathrm{std}, 4) = 1.77$ (doubly-magic resonance)
- $\rho(\mathrm{std}, A \geq 5) \approx 1$ (pentagon operational)

Applied in the binding formula:

$$
  B(Z, N) = \sum_\lambda w_\lambda \cdot \rho(\lambda, A) \cdot m_e \cdot
  \sum_i \ln\bigl|\Phi_q(\hat{V}_i^\lambda)\bigr|
$$

reproduces AME within 0.02–0.27% across $A = 2$ to $A = 12$.
