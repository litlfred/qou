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
| Six-term theorem $T_3$ | $-z^2 \sum \text{Li}_2^q(-\|V_i V_j\|)$ | Expected per [Unified mass formula: tower + Frobenius co-Casimir correction](../mass-theory/knot-mass-formula-unified.md); wiring pending |

The Kashaev-limit form (six-term $T_3$) provides the anticipated canonical form. Its derivation as a leading-order expansion in $\hbar_q$ remains incomplete. This must parallel the single-generator Kashaev derivation $\alpha \sum \ln|V_i|$.

## Component decomposition and epistemic tiers

| Component | Epistemic tier | Evidence |
|---|---|---|
| Existence of $f_2$ (any form) | Conjectural | Follows from evaluating mass formula at finite truncation |
| $f_2 = -\text{Li}_2^q(-\|V_i V_j\|) \cdot z^2$ | Conjectural | Matches six-term $T_3$; derivation pending |
| Naive log-additive form | Refuted | `rho-k-pair-gen-extension.witness.json` |
| Wedderburn-coupled form | Partial | Correct Wedderburn weights, wrong functional form |
| Six-term theorem [Unified mass formula: tower + Frobenius co-Casimir correction](../mass-theory/knot-mass-formula-unified.md) | Theorem | Proved independently |

## Wedderburn-coupling structure

Under [Graded expansion of the categorical density $\rho_K = \rho_K^{\mathrm{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}} + \dots$](rho-k-graded-expansion.md) §pair-gen, the pair coupling expands as:

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
- $w_{\text{sym}}, w_{\text{std}}, w_{\text{alt}}$ denote Wedderburn–Markov weights from [Three-invariant atomic mass formula](../mass-theory/wedderburn-mass-formula.md).
- $\lambda_i^\bullet$ denote per-generator eigenvalues within each Wedderburn channel.
- $M_i$ denotes the per-generator $2 \times 2$ standard-representation transfer matrix.

The standard-channel pair coupling relies on the Markov-traced $2 \times 2$ matrix product $M_i M_j$. This captures braid non-commutativity, superseding the naive scalar product $V_i^{\text{std}} \cdot V_j^{\text{std}}$.

The open requirement is the functional form $f_2$. The naive logarithmic form $\alpha z^2 \ln|V_i V_j|_{\text{Wedderburn}}$ degrades empirically. The expected $q$-dilogarithmic form $-z^2 \text{Li}_2^q(-|V_i V_j|_{\text{Wedderburn}})$ requires a formal derivation connecting it to the pair-generator expansion.

## Dependencies

- [Canonical operator-level lepton-mass-tower formula](../mass-theory/lepton-mass-tower-canonical.md): The lepton-sector variant. It depends on the graded-expansion formalism but evaluates at $Z = N = 0$, nullifying the atomic LO piece. It requires its own dimensional factor $\xi_\ell(q)$.
- [Mass endomorphism conjecture](mass-endomorphism-conjecture.md): The unifying closed-form mass element $\Phi_{\text{mass}}(W) \in H_{3A}(q)$. The present conjecture restricts this to the pair level.

## Lean formalization

```lean
namespace QOU.BraidKnot.RhoKPairGenCanonicalForm

/-- The quantum dilogarithm `Li₂^q` as a concrete real function — the
    Faddeev–Kashaev series, evaluated over `ℝ`. -/
noncomputable def qDilog (q x : ℝ) : ℝ :=
  ∑' n : ℕ, x ^ (n + 1) / ((n + 1 : ℝ) * (1 - q ^ (n + 1)))

/-- Markov datum for one atomic braid: the Wedderburn-traced
    per-generator volumes `|V̂_i|`. -/
structure AtomicBraid where
  vols : List ℝ

/-- The measured (CODATA) pair-gen contribution — an external empirical
    datum, hence an opaque *function* of the braid's Markov data. -/
axiom physMass : AtomicBraid → ℝ

/-- Pairwise sum `Σ_{i<j} f (vᵢ) (vⱼ)`. -/
def pairSum (f : ℝ → ℝ → ℝ) : List ℝ → ℝ
  | [] => 0
  | v :: vs => (vs.map (f v)).sum + pairSum f vs

/-- The six-term theorem's `T₃` Kashaev-limit functional
    `f(x, y) = -z² · Li₂^q(-|x·y|)`. -/
def kashaevT3 (Li2q : ℝ → ℝ) (z x y : ℝ) : ℝ :=
  -z ^ 2 * Li2q (-(|x * y|))

/-- Conjecture axiomatisation (§3b class, content-bearing). One concrete
    `T₃` functional recovers every atomic braid's measured pair-gen mass
    to sub-percent accuracy, uniformly in the braid. **No instance is
    provided** — that is the open Kashaev-limit derivation. -/
class PairGenCanonical : Prop where
  content :
    ∃ (q z : ℝ), 1 < q ∧
      ∀ K : AtomicBraid, 0 < physMass K →
        |pairSum (kashaevT3 (qDilog q) z) K.vols - physMass K| ≤ physMass K / 100

end QOU.BraidKnot.RhoKPairGenCanonicalForm
```


## Resolution path

Deriving the canonical $f_2$ yields four consequences:
1. This conjecture elevates to a theorem.
2. The open status of [Graded expansion of the categorical density $\rho_K = \rho_K^{\mathrm{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}} + \dots$](rho-k-graded-expansion.md) §pair-gen resolves to proved.
3. Downstream conjectures become reachable, specifically [Canonical operator-level lepton-mass-tower formula](../mass-theory/lepton-mass-tower-canonical.md).
4. The $\mathfrak{Q}_\beta$ residual closure direction becomes tractable.

## Archimedean specialization

We state this conjecture on the archimedean side of the substrate wall. It asserts a real-mass sub-percent recovery bound: $\forall M \ge 0,\ \exists M_{\mathrm{rec}},\ |M_{\mathrm{rec}} - M| \le M/100$ over $\mathbb{R}$. The generic $q$-deformation functional $f_2(q, \hat V_i, \hat V_j)$ serves as input. The conjectural statement intrinsically addresses real masses; it does not constitute a separable archimedean specialization of an otherwise $\mathbb{R}$-free construction.
