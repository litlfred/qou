import Mathlib.Tactic

/-!
# QOU.LiftingDescent.descent_cocycle_deviation — twisted Čech 2-cocycle equation

**Lemma** ([`lem:descent-cocycle-deviation`](../../../quantum-observable-universe/lifting-and-descent/descent-cocycle-deviation.md)).

*Under the central extension `𝔊_{n+1} → 𝔊_n` with local lift data
`a_{ij}^{(n)} ∈ 𝓞_M^×`, the cocycle deviation at level `n+1` is*

```
  g_{ijk}^{(n+1)} = a_{ij}^{(n)} · a_{jk}^{(n)} · (a_{ik}^{(n)})⁻¹ · g_{ijk}^{(n)}
```

*so that the twisted Čech 2-cocycle equation*

```
  d(g_{ijk}^{(n)}) = a_{ij}^{(n)} · g_{ijk}^{(n)} · (a_{jk}^{(n)})⁻¹
```

*holds, with cohomology class in `H²(M, 𝓞_M^×)`.*

-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/descent-cocycle-deviation.md
-/

namespace QOU.LiftingDescent

/-- Abstract context for the descent cocycle deviation. -/
class DescentCocycleContext where
  /-- The unit-group `𝓞_M^×` (multiplicative group). -/
  M : Type
  mul : M → M → M
  inv : M → M
  one : M
  /-- The local lift data `a_{ij}^{(n)} : M` indexed by `(n, i, j)`. -/
  a_local : ℕ → ℕ → ℕ → M
  /-- The Čech 2-cocycle `g_{ijk}^{(n)} : M`. -/
  g_cocycle : ℕ → ℕ → ℕ → ℕ → M
  /-- The Čech coboundary `d g_{ijk}^{(n)} : M`. -/
  d_cocycle : ℕ → ℕ → ℕ → ℕ → M
  /-- Manuscript cocycle-deviation identity. -/
  claim_cocycle_deviation : ∀ n i j k : ℕ,
    g_cocycle (n + 1) i j k =
      mul (mul (a_local n i j) (a_local n j k))
          (mul (inv (a_local n i k)) (g_cocycle n i j k))
  /-- Manuscript twisted Čech 2-cocycle equation. -/
  claim_cech_cocycle : ∀ n i j k : ℕ,
    d_cocycle n i j k =
      mul (a_local n i j)
          (mul (g_cocycle n i j k) (inv (a_local n j k)))

/-- **Cocycle deviation under central extension**
    ([`lem:descent-cocycle-deviation`]).

    `g_{ijk}^{(n+1)} = a_{ij} · a_{jk} · a_{ik}⁻¹ · g_{ijk}^{(n)}`. -/
-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/descent-cocycle-deviation.md
theorem descent_cocycle_deviation
    [ctx : DescentCocycleContext] (n i j k : ℕ) :
    ctx.g_cocycle (n + 1) i j k
      = ctx.mul (ctx.mul (ctx.a_local n i j) (ctx.a_local n j k))
                (ctx.mul (ctx.inv (ctx.a_local n i k))
                         (ctx.g_cocycle n i j k)) :=
  ctx.claim_cocycle_deviation n i j k

/-- **Twisted Čech 2-cocycle equation** (corollary of the deviation
    formula). -/
-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/descent-cocycle-deviation.md
theorem twisted_cech_cocycle_equation
    [ctx : DescentCocycleContext] (n i j k : ℕ) :
    ctx.d_cocycle n i j k
      = ctx.mul (ctx.a_local n i j)
                (ctx.mul (ctx.g_cocycle n i j k)
                         (ctx.inv (ctx.a_local n j k))) :=
  ctx.claim_cech_cocycle n i j k

end QOU.LiftingDescent
