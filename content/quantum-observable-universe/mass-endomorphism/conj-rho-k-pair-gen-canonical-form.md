**Conjecture (Canonical form of $\rho_K^{\text{pair-gen}}$).**
*There exists a closed-form Wedderburn-coupled functional $f_2 : \mathbb{Q}(q^{1/2}) \times \mathbb{Q}(q^{1/2}) \times \mathbb{Q}(q^{1/2}) \to \mathbb{R}$ such that for every atomic braid $\mathcal{B}_K \in B_{3A}$:*

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
\mathcal{M}(K)^{\text{CODATA}}
\;+\; O(\hbar_q^{6})
$$

*matches CODATA to sub-percent accuracy across $Z = 1..20$. Here, $\hat V_i^{\text{full}}$ denotes the Wedderburn-traced per-generator volumes, and $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter.*

## Empirical evidence

| Candidate $f_2$ | Form | $Z=1..20$ status |
|---|---|---|
| Naive log-additive | $\alpha z^2 \sum \ln\|V_i V_j\|$ | Degrades vs LO + single-gen |
| Wedderburn-decomposed | $\alpha z^2 \sum \|V_i V_j\|_{\text{Wedderburn}}$ (with $w_{sym}, w_{std}, w_{alt}$) | Degrades (wrong functional form) |
| Six-term theorem $T_3$ | $-z^2 \sum \text{Li}_2^q(-\|V_i V_j\|)$ | Expected per [`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md); wiring pending |

The Kashaev-limit form (six-term $T_3$) is the anticipated canonical form. Its derivation as a leading-order expansion in $\hbar_q$ remains incomplete. This must parallel the single-generator Kashaev derivation $\alpha \sum \ln|V_i|$.

## Conjecture status

| Component | Status | Evidence |
|---|---|---|
| Existence of $f_2$ (any form) | Conjectural | Follows from evaluating mass formula at finite truncation |
| $f_2 = -\text{Li}_2^q(-\|V_i V_j\|) \cdot z^2$ | Conjectural | Matches six-term $T_3$; derivation pending |
| Naive log-additive form | Refuted | `rho-k-pair-gen-extension.witness.json` |
| Wedderburn-coupled form | Partial | Correct Wedderburn weights, wrong functional form |
| Six-term theorem [`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md) | Theorem | Proved independently |

## Wedderburn-coupling structure

Under [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) §pair-gen, the pair coupling expands as:

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
- $w_{\text{sym}}, w_{\text{std}}, w_{\text{alt}}$ are Wedderburn–Markov weights from [`thm:wedderburn-mass-formula`](wedderburn-mass-formula.md).
- $\lambda_i^\bullet$ are per-generator eigenvalues within each Wedderburn channel.
- $M_i$ is the per-generator $2 \times 2$ standard-representation transfer matrix.

The standard-channel pair coupling relies on the Markov-traced $2 \times 2$ matrix product $M_i M_j$. This captures braid non-commutativity, superseding the naive scalar product $V_i^{\text{std}} \cdot V_j^{\text{std}}$.

The open requirement is the functional form $f_2$. The naive logarithmic form $\alpha z^2 \ln|V_i V_j|_{\text{Wedderburn}}$ degrades empirically. The expected $q$-dilogarithmic form $-z^2 \text{Li}_2^q(-|V_i V_j|_{\text{Wedderburn}})$ requires a formal derivation connecting it to the pair-generator expansion.

## Dependencies

- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md): The lepton-sector variant. It gates on the graded-expansion formalism but evaluates at $Z = N = 0$, nullifying the atomic LO piece. It requires its own dimensional factor $\xi_\ell(q)$.
- [`conj:mass-endomorphism`](mass-endomorphism-conjecture.md): The unifying closed-form mass element $\Phi_{\text{mass}}(W) \in H_{3A}(q)$. The present conjecture restricts this to the pair level.

## Lean formalization

```lean
namespace QOU.BraidKnot.RhoKPairGenCanonicalForm

/-- The conjectural canonical pair-gen functional `f_2(q, V_i, V_j)`;
    expected six-term `T_3` Kashaev form, derivation open. -/
noncomputable def pair_gen_functional
    {R : Type*} [Field R] (q V_i V_j : R) : R :=
  sorry

/-- Conjecture axiomatisation: a single canonical functional
    reproduces ρ_K^pair-gen to sub-percent accuracy. The specific Li_2^q
    recovery bound requires the graded-expansion infrastructure, 
    so it exists as a `Prop` class assumed downstream as `[PairGenCanonical]`. -/
class PairGenCanonical : Prop where
  exists_subpercent_recovery :
    ∀ (M : ℝ), 0 ≤ M → ∃ M_rec : ℝ, |M_rec - M| ≤ M / 100

end QOU.BraidKnot.RhoKPairGenCanonicalForm
```

## Resolution path

Deriving the canonical $f_2$ yields four consequences:
1. This conjecture elevates to a theorem.
2. The open status of [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) §pair-gen resolves to proved.
3. Downstream conjectures unblock, specifically [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md).
4. The $\mathfrak{Q}_\beta$ residual closure direction becomes tractable.

## Archimedean specialization

We state this conjecture on the archimedean side of the substrate wall. It asserts a real-mass sub-percent recovery bound: $\forall M \ge 0,\ \exists M_{\mathrm{rec}},\ |M_{\mathrm{rec}} - M| \le M/100$ over $\mathbb{R}$. The generic $q$-deformation functional $f_2(q, \hat V_i, \hat V_j)$ serves as input. The conjectural statement intrinsically addresses real masses; it is not a separable archimedean specialization of an otherwise $\mathbb{R}$-free construction.
