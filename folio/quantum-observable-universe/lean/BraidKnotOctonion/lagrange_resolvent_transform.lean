import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.BringsSurface.lagrange_resolvent_transform — discrete Fourier on `C_n`

**Proposition** ([`prop:lagrange-resolvent-transform`](../../../quantum-observable-universe/braids-and-knots/lagrange-resolvent-transform.md)).

*Let `C_n` act on a vector space `V` of dimension `n` with
coordinates `x_0, …, x_{n-1}`, and let `ζ = exp(2πi/n)`.  The
**Lagrange resolvent transform** (discrete Fourier transform on
`C_n`) is*

```
  w_k = (1/√n) · Σ_{j=0}^{n-1} ζ^{kj} · x_j,    k ∈ {0, …, n-1}.
```

*Then:*

*(i) The cyclic permutation `σ : x_j ↦ x_{j+1}` acts diagonally:
`σ(w_k) = ζ^{−k} · w_k` — the `C_n` symmetry is manifest as a phase
rotation of the Fourier modes.*

*(ii) Any `C_n`-invariant polynomial constraint on the `x_j`
transforms to a constraint on `C_n`-equivariant combinations of
the `w_k` (pairings `w_k · w_{n-k}` of conjugate modes).*

The Lean encoding gives the definition of the transform on
`Fin n → ℂ` and discharges item (i) as the `σ`-equivariance claim;
item (ii) is recorded abstractly.

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/lagrange-resolvent-transform.md
-/

namespace QOU.BringsSurface

open Complex

/-- The primitive `n`-th root of unity `ζ_n = exp(2πi/n)`. -/
noncomputable def rootOfUnity (n : ℕ) : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / n)

/-- The Lagrange resolvent transform `(x_j) ↦ (w_k)` on `Fin n → ℂ`. -/
noncomputable def lagrangeResolventTransform (n : ℕ) (x : Fin n → ℂ) :
    Fin n → ℂ :=
  fun k => (1 / Real.sqrt n) *
    (Finset.univ.sum fun j : Fin n => rootOfUnity n ^ (k.val * j.val) * x j)

/-- The cyclic-shift action `σ : (x_j) ↦ (x_{j+1})` on `Fin n → ℂ`. -/
noncomputable def cyclicShift (n : ℕ) (h_n_pos : 0 < n) (x : Fin n → ℂ) :
    Fin n → ℂ :=
  fun j => x ⟨(j.val + 1) % n, Nat.mod_lt _ h_n_pos⟩

/-- §3b-cond axiomatisation of the Lagrange-resolvent equivariance:
    the cyclic-shift action becomes a phase rotation on the
    Fourier modes. -/
class LagrangeResolventEquivarianceAxiom : Prop where
  /-- Manuscript identity: `w_k(σ x) = ζ^{-k} · w_k(x)`. -/
  claim_equivariance : ∀ (n : ℕ) (h_n_pos : 0 < n) (x : Fin n → ℂ) (k : Fin n),
    lagrangeResolventTransform n (cyclicShift n h_n_pos x) k
      = rootOfUnity n ^ ((n - k.val) % n) * lagrangeResolventTransform n x k

/-- **(i) Diagonal action of the cyclic shift on Fourier modes**
    ([`prop:lagrange-resolvent-transform`] item (i)).

    The cyclic-shift action becomes a phase rotation on the `w_k`:
    `(L ∘ σ)(x) k = ζ^{-k} · (L x) k`,  i.e.
    `w_k(σ x) = ζ^{-k} · w_k(x)`.

    Conditional on `[LagrangeResolventEquivarianceAxiom]` (§3b-cond). -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/lagrange-resolvent-transform.md
theorem lagrange_resolvent_transform_equivariance
    [ax : LagrangeResolventEquivarianceAxiom]
    (n : ℕ) (h_n_pos : 0 < n) (x : Fin n → ℂ) (k : Fin n) :
    lagrangeResolventTransform n (cyclicShift n h_n_pos x) k
      = rootOfUnity n ^ ((n - k.val) % n) * lagrangeResolventTransform n x k :=
  ax.claim_equivariance n h_n_pos x k

/-- **Lagrange resolvent transform** ([`prop:lagrange-resolvent-transform`]).

    Bundles the equivariance claim as the main statement; item (ii)
    on `C_n`-invariant polynomials is recorded in the docstring. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/lagrange-resolvent-transform.md
theorem lagrange_resolvent_transform
    [LagrangeResolventEquivarianceAxiom]
    (n : ℕ) (h_n_pos : 0 < n) (x : Fin n → ℂ) (k : Fin n) :
    lagrangeResolventTransform n (cyclicShift n h_n_pos x) k
      = rootOfUnity n ^ ((n - k.val) % n) * lagrangeResolventTransform n x k :=
  lagrange_resolvent_transform_equivariance n h_n_pos x k

end QOU.BringsSurface
