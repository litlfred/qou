import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin

/-!
# QOU.Archimedean.skein_finiteness_bound

**Placeholder canonical** for content block at
[`quantum-observable-universe/archimedean-universe/skein-finiteness-bound.ts`](quantum-observable-universe/archimedean-universe/skein-finiteness-bound.ts).

The full Lean statement is pending; this stub exists so the
`lean.ref` URI `qou:QOU.Archimedean.skein_finiteness_bound` resolves to a real declaration in the `qou`
Lake package.
-/

namespace QOU.Archimedean


/-- Abstract context for the `skein_finiteness_bound` claim — manuscript-themed
    typed fields below; sub-claims encode (i) the Skein-polynomial
    factorisation, (ii) the per-generator positivity equivalence, and
    (iii) the finiteness of the stable-configuration count. -/
class SkeinFinitenessBoundContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The Skein polynomial `P_{N(p,n)}(q) ∈ ℝ` at fixed `q`. -/
  P : ℝ
  /-- The per-generator traced volume `V̂_i` as a function `Fin (Z + N - 1) → ℝ`. -/
  V : Fin (Z + N - 1) → ℝ
  /-- Manuscript sub-claim (i): the Skein polynomial factorises as
      `P = ∏_{i=0}^{A-2} V̂_i(q)`. -/
  claim_i_skein_factorisation :
    P = (Finset.univ.prod (fun i : Fin (Z + N - 1) => V i))
  /-- Stability predicate: configuration `N(Z, N)` is stable. -/
  is_stable : Prop
  /-- Manuscript sub-claim (ii): stability iff every per-generator
      volume is positive. -/
  claim_ii_per_generator_positivity :
    is_stable ↔ ∀ i : Fin (Z + N - 1), 0 < V i
  /-- Type of stable nuclear configurations at fixed `q`. -/
  StableConfig : Type
  /-- Manuscript sub-claim (iii): the type of stable configurations
      is finite. -/
  claim_iii_stable_configurations_finite : Finite StableConfig

/-- **Manuscript statement** (full body):

The number of stable nuclear configurations at a given substrate
parameter $q$ is **finite**.  The stability boundary is the zero
locus of the Skein polynomial $P_{\mathcal{N}(p,n)}(q)$.

## The transfer matrix eigenvalue inequality

Each generator $\sigma_i$ of the nuclear braid contributes a
traced volume
$\hat{V}_i = z \cdot M_{11}^{(i)} + M_{21}^{(i)}$
([transfer matrix](#prop:skein-polynomial-transfer-matrix)),
and the Skein polynomial is the product:

$$
  P_{\mathcal{N}(p,n)}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q).
$$

The transfer matrix $T(c, d)$ at each crossing has eigenvalues

$$
  \lambda_{\pm} = 
  \frac{\mathrm{tr}T \pm \sqrt{(\mathrm{tr}T)^2 - 4\det T}}{2}
$$

which are **real and opposite in sign** (since $\det T < 0$ for
all three crossing types):

| Crossing type | $\lambda_+$ | $\lambda_-$ | $\lvert\lambda_+/\lambda_-\rvert$ |
|:---:|:---:|:---:|:---:|
| pp | $q$ | $-q^{-1}$ | $q^2$ |
| nn | $q^3$ | $-q^{-1}$ | $q^4$ |
| mix | $\approx q^{3/2}$ | $\approx -q^{-1/2}$ | $\approx q^2$ |

The chain of $k$ crossings at generator $\sigma_i$ gives

$$
  \hat{V}_i =  c_+\lambda_+^k +  c_-\lambda_-^k
$$

where $c_{\pm}$ depend on $z$ and the crossing coefficients.
Since $\lambda_- < 0$, the term $c_- \lambda_-^k$ **alternates
in sign** with $k$.

## The finiteness inequality

**Proposition.**
*A nuclear configuration $\mathcal{N}(p, n)$ is stable only if
the Skein polynomial is positive:*

$$
  P_{\mathcal{N}(p,n)}(q)  >  0.
$$

*This is equivalent to the **lattice inequality**: for each
generator $i = 0, \ldots, A-2$, the traced volume must be
positive:*

$$
  \hat{V}_i(q) = 
  c_+^{(i)}\lambda_+^{k_i}
  + 
  c_-^{(i)}\lambda_-^{k_i}
   >  0
  \qquad (i = 0, \ldots, A-2)
$$

*where $k_i$ is the number of crossings at generator $i$
(nucleon $i$ with all nucleons $j > i$).*

**The bound.** Since $|\lambda_+| > |\lambda_-|$ (the ratio
is $q^2$ or $q^4$), the $c_+ \lambda_+^k$ term dominates for
large $k$.  The sign of $\hat{V}_i$ depends on:

1. The **sign of

[…truncated; see manuscript for remainder…]

    The Lean encoding below splits the manuscript claim into named
    sub-claim fields; concretisation requires per-block manuscript
    translation. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/skein-finiteness-bound.ts
theorem skein_finiteness_bound [ctx : SkeinFinitenessBoundContext] :
    ctx.P
      = (Finset.univ.prod (fun i : Fin (ctx.Z + ctx.N - 1) => ctx.V i)) ∧
    (ctx.is_stable ↔ ∀ i : Fin (ctx.Z + ctx.N - 1), 0 < ctx.V i) ∧
    Finite ctx.StableConfig :=
  ⟨ctx.claim_i_skein_factorisation, ctx.claim_ii_per_generator_positivity, ctx.claim_iii_stable_configurations_finite⟩

end QOU.Archimedean
