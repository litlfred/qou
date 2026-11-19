**Conjecture (Canonical form of $\rho_K^{\text{pair-gen}}$).**
*There exists a closed-form Wedderburn-coupled functional $f_2 : \mathbb{Q}(q) \times \mathbb{Q}(q) \times \mathbb{Q}(q) \to \mathbb{R}$ such that for every atomic Hecke word $\mathcal{B}_K \in H_{3A}(q)$:*

$$
\rho_K^{\text{pair-gen}}
\;=\;
\sum_{0 \leq i < j \leq 3A-2}
  f_2\!\left(q, \hat V_i^{\text{full}}, \hat V_j^{\text{full}}\right)
$$

*and the resulting graded-expansion truncation*

$$
m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)| \cdot \left(\rho_K^{\text{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}}\right)
\;=\;
\mathfrak{m}(K)^{\text{CODATA}}
\;+\; O(\hbar_q^{6})
$$

*matches CODATA to sub-percent accuracy across $Z = 1..20$. Here, $\hat V_i^{\text{full}}$ denotes the Wedderburn-traced per-generator volumes, and $z = q^{3}/(q^{2}+1)$ forms the Markov parameter (**convention D**).*

## Empirical evidence

| Candidate $f_2$ | Form | $Z=1..20$ status |
|---|---|---|
| Naive log-additive | $\alpha z^2 \sum \ln\|V_i V_j\|$ | Degrades vs LO + single-gen |
| Wedderburn-decomposed | $\alpha z^2 \sum \|V_i V_j\|_{\text{Wedderburn}}$ (with $w_{sym}, w_{std}, w_{alt}$) | Degrades (wrong functional form) |
| Six-term theorem $T_3$ | $-z^2 \sum \text{Li}_2^q(-\|V_i V_j\|)$ | Expected per [the unified knot mass formula](../mass-theory/knot-mass-formula-unified.md); wiring pending |

The Kashaev-limit form (six-term $T_3$) provides the anticipated canonical form. Its derivation as a leading-order expansion in $\hbar_q$ remains incomplete. This must parallel the single-generator Kashaev derivation $\alpha \sum \ln|V_i|$.

## Component decomposition and epistemic tiers

| Component | Epistemic tier | Evidence |
|---|---|---|
| Existence of $f_2$ (any form) | Conjectural | Follows from evaluating mass formula at finite truncation |
| $f_2 = -\text{Li}_2^q(-\|V_i V_j\|) \cdot z^2$ | Conjectural | Matches six-term $T_3$; derivation pending |
| Naive log-additive form | Refuted | Degrades residual accuracy across $Z = 1..20$ |
| Wedderburn-coupled form | Partial | Correct Wedderburn weights, wrong functional form |
| Six-term theorem ([unified knot mass formula](../mass-theory/knot-mass-formula-unified.md)) | Theorem | Proved independently |

## Wedderburn-coupling structure

Under [the graded $\rho_K$ expansion](rho-k-graded-expansion.md) §pair-gen, the pair coupling expands as:

$$
|\hat V_i \hat V_j|_{\text{Wedderburn}}
\;=\;
w_{\text{sym}}\, \lambda_i^{\text{sym}} \lambda_j^{\text{sym}}
\;+\;
w_{\text{std}}\, \bigl[z\,(M_i M_j)_{1,2} + (M_i M_j)_{2,2}\bigr]
\;+\;
w_{\text{alt}}\, \lambda_i^{\text{alt}} \lambda_j^{\text{alt}},
$$

where:
- $w_{\text{sym}}, w_{\text{std}}, w_{\text{alt}}$ denote Wedderburn–Markov weights from [the Wedderburn mass formula](../mass-theory/wedderburn-mass-formula.md).
- $\lambda_i^\bullet$ denote per-generator eigenvalues within each Wedderburn channel.
- $M_i$ denotes the per-generator $2 \times 2$ standard-representation transfer matrix.

The standard-channel pair coupling relies on the Markov-traced $2 \times 2$ matrix product $M_i M_j$. This captures braid non-commutativity, superseding the naive scalar product $V_i^{\text{std}} \cdot V_j^{\text{std}}$.

The open requirement is the functional form $f_2$. The naive logarithmic form $\alpha z^2 \ln|V_i V_j|_{\text{Wedderburn}}$ degrades empirically. The expected $q$-dilogarithmic form $-z^2 \text{Li}_2^q(-|V_i V_j|_{\text{Wedderburn}})$ requires a formal derivation connecting it to the pair-generator expansion.

## Dependencies

- [Canonical lepton mass tower](../mass-theory/lepton-mass-tower-canonical.md): The lepton-sector variant. It depends on the graded-expansion formalism but evaluates at $Z = N = 0$, nullifying the atomic LO piece. It requires its own dimensional factor $\xi_\ell(q)$.
- [Mass endomorphism conjecture](mass-endomorphism-conjecture.md): The unifying closed-form mass element $\Phi_{\text{mass}}(W) \in H_{3A}(q)$. The present conjecture restricts this to the pair level.

## Precise formulation of the $T_3$ Kashaev-limit functional

With the quantum dilogarithm

$$
\mathrm{Li}_2^q(x) \;=\; \sum_{n \geq 0} \frac{x^{n+1}}{(n+1)(1 - q^{n+1})}
$$

and the six-term theorem's $T_3$ Kashaev-limit functional $f(x, y) = -z^2\,\mathrm{Li}_2^q(-|xy|)$, the pair-generator hypothesis states that there exist $q > 1$ and Markov parameter $z$ such that for every atomic braid $K$ with Wedderburn-traced per-generator volumes $\{v_i\}$ and positive measured pair-generator mass $M_{\mathrm{phys}}(K) > 0$,

$$
\Biggl|\sum_{i < j} \bigl(-z^2\,\mathrm{Li}_2^q(-|v_i v_j|)\bigr) - M_{\mathrm{phys}}(K)\Biggr| \;\leq\; \frac{M_{\mathrm{phys}}(K)}{100}.
$$


## Resolution path

Deriving the canonical $f_2$ yields four consequences:
1. This conjecture elevates to a theorem.
2. The open status of [the graded $\rho_K$ expansion](rho-k-graded-expansion.md) §pair-gen resolves to proved.
3. Downstream conjectures become reachable, specifically [the canonical lepton mass tower](../mass-theory/lepton-mass-tower-canonical.md).
4. The $\mathfrak{Q}_\beta$ residual closure direction becomes tractable.
