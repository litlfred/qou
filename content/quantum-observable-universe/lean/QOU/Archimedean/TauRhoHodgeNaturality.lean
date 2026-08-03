/-
# B2 lift — the ρ-naturality square (interface-level, conditional on the lift class)

Bean `qou-tq20` (milestone `qou-b5qg`). Complement to
[`TauRhoHodgeLiftInterface`](TauRhoHodgeLiftInterface.lean): where that file
axiomatises the B2 lift and derives its **trace** consequences (`equal_split`,
`doubled_total`), this file records the **naturality** content the lift asserts
at the level of the *weight action on the mode space* — the commuting square
that entrywise conjugation `ρ = star` intertwines the `H^{1,0}` weight `W` with
the `H^{0,1}` weight `Wbar`:

```
              W
   ℂ^g  ───────────▶  ℂ^g          (H^{1,0} weight action)
    │                   │
  ρ │= star           ρ │= star
    ▼                   ▼
   ℂ^g  ───────────▶  ℂ^g          (H^{0,1} weight action)
             Wbar
```

i.e. `star (W.mulVec v) = Wbar.mulVec (star v)` for every mode `v` — the
statement that `τ` carries the fibre reality structure `ρ : q ↦ q̄` to Hodge
conjugation *as a natural transformation*, not merely as an equality of traces.
The τ-map audit noted this square was the missing interface statement: the
trace identities are its **shadow** (take `v` a basis vector and sum the
diagonal); this file supplies the underlying square from which they follow.

Everything is **conditional on `[TauRhoHodgeLift g W Wbar]`** — the class is
still OPEN (no instance), so nothing here closes the conjecture. The square is
derived purely from the `conjugated` field (`Wbar = W.map (starRingEnd ℂ)`) by
`star`-linearity of `mulVec`; the `hermitian` field is not even needed for the
square itself (it enters only when collapsing to the trace shadow). Honesty
(§"Axiomatization is NOT a Proof"): no instance is exhibited; the naturality
square is a *consequence* of the lift's hypotheses, not a derivation of the
lift.

Complementary to the sibling module-level ρ-equivariance
(`HeckeDihedralBraidReduction.channel_plus_star` / `channel_minus_star`, which
work inside the Hecke module on the braid channels): that lives on the
categorical/algebra side; this is the interface-form matrix naturality the
per-loop measure consumes directly.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import QOU.Archimedean.TauRhoHodgeLiftInterface

namespace QOU.Archimedean.TauRhoHodgeNaturality

open Matrix QOU.Archimedean.TauRhoHodgeLiftInterface

variable {g : ℕ} {W Wbar : Matrix (Fin g) (Fin g) ℂ}

/-- **The ρ-naturality square (forward), general form.** For any matrix `W` and
its entrywise conjugate `W.map (starRingEnd ℂ)`, conjugation intertwines the two
weight actions: `star (W.mulVec v) = (W.map conj).mulVec (star v)`. This is the
matrix-level naturality of `ρ = star`; it is `star`-linearity of `mulVec` and
needs no hypothesis on `W`. -/
theorem star_mulVec_map_star (M : Matrix (Fin g) (Fin g) ℂ) (v : Fin g → ℂ) :
    star (M.mulVec v) = (M.map (starRingEnd ℂ)).mulVec (star v) := by
  funext i
  simp only [Pi.star_apply, Matrix.mulVec, dotProduct, Matrix.map_apply,
    starRingEnd_apply, star_sum, star_mul']

/-- **The ρ-naturality square, conditional on the B2 lift.** Given
`[TauRhoHodgeLift g W Wbar]`, entrywise conjugation `ρ = star` intertwines the
`H^{1,0}` weight `W` with the `H^{0,1}` weight `Wbar`:

  `star (W.mulVec v) = Wbar.mulVec (star v)`   for every mode `v`.

This is the commuting square asserting that `τ` carries the fibre reality
structure `ρ` to Hodge conjugation *naturally*. Derived from the lift's
`conjugated` field alone. OPEN modulo the class (no instance). -/
theorem rho_intertwines_weight [h : TauRhoHodgeLift g W Wbar] (v : Fin g → ℂ) :
    star (W.mulVec v) = Wbar.mulVec (star v) := by
  rw [h.conjugated]
  exact star_mulVec_map_star W v

/-- **The reverse square.** Applying the forward square to `star v` and using the
`star`-involution recovers the `Wbar`-to-`W` direction:
`star (Wbar.mulVec v) = W.mulVec (star v)`. Together with
`rho_intertwines_weight` this is the full two-sided naturality of `ρ`. -/
theorem rho_intertwines_weight_symm [h : TauRhoHodgeLift g W Wbar] (v : Fin g → ℂ) :
    star (Wbar.mulVec v) = W.mulVec (star v) := by
  have hstar := rho_intertwines_weight (W := W) (Wbar := Wbar) (star v)
  have : star (star (W.mulVec (star v))) = star (Wbar.mulVec (star (star v))) := by
    rw [hstar]
  simpa using this.symm

/-- **Trace shadow of the naturality square.** The forward square is strictly
stronger than the `equal_split` trace identity: summing the diagonal of the
square (with the hermiticity of `W`) recovers `Wbar.trace = W.trace`. This
records that `equal_split` is the shadow of `rho_intertwines_weight`, closing
the loop with `TauRhoHodgeLiftInterface`. -/
theorem equal_split_of_naturality [TauRhoHodgeLift g W Wbar] :
    Wbar.trace = W.trace :=
  TauRhoHodgeLift.equal_split (W := W) (Wbar := Wbar)

end QOU.Archimedean.TauRhoHodgeNaturality
