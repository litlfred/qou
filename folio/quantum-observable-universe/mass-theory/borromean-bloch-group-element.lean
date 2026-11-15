import QOU.Archimedean.BorromeanVolumeCatalan

/-!
# `conj:borromean-bloch-group-element` — the `8G` is derived, not assumed

Sibling for content block
[`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md).

## What this file used to be

```lean
class BorromeanBlochGroupElement where
  holds : Prop
```

`⟨True⟩` inhabits that, so nothing downstream of it assumed anything (AGENTS.md
§3b-tax; bean `qou-hprp`).

## What is assumed and what is derived

The block's headline is `r₂[𝓑₃] = Vol(𝓑₃) = 8G`. Taking that as a class field
would be assuming the answer. It is not assumed here.

**Assumed** — one field, and it is classical:

* `regulator_bloch_i` — the Beilinson regulator of the Bloch-group symbol `[i]`
  is Catalan's constant, `D(i) = Cl₂(π/2) = G`. Bloch–Suslin plus the
  Bloch–Wigner dilogarithm at the fourth root of unity; cited, not conjectured.

**Structural, in a definition rather than a field** — Thurston's decomposition of
the Borromean complement into **two** regular ideal octahedra, each `4·[i]` in the
Bloch group, so `[𝓑₃] = 8·[i]`. That is what `borromeanClass` *is*.

**Derived** — `r₂[𝓑₃] = 8G`, from additivity of the regulator applied to `8·[i]`
together with the one assumed value. The `8` comes out of the group structure, not
out of a hypothesis, which is the whole point of writing the class as a multiple.
Two further consequences: the class is **non-zero** in `B(ℂ)` (a non-zero regulator
forces a non-zero class — the block's "non-trivial element of `K₃(ℂ)`"), and the
`h⁴` shadow `r₂[𝓑₃]·(−3/4) = −6G`.

## What is NOT formalised here, stated rather than implied

- **No Bloch group.** `B` is an arbitrary `AddCommGroup` and `r₂` an arbitrary
  additive map into `ℝ`. Nothing here constructs `B(ℂ)`, the five-term relation,
  or `K₃`; the block's five-term/pentagon discussion has no counterpart below.
- **`blochI` is a parameter, not `[i]`.** Nothing forces it to be the symbol of the
  fourth root of unity. The `ζ₄`-vs-`ζ₆` distinction the block is careful about —
  `Cl₂(π/2)` for the octahedron against `Cl₂(π/3)` for the figure-eight — is
  carried only by the *value* in `regulator_bloch_i`, not by any structure here.
- **The `h⁴ = −3/4` coefficient is not computed.** It enters `h4Shadow` as a
  hypothesis, sourced to the Markov trace of `𝓑₃`; this file does not re-derive it.
- **The higher-order regulator expansion is absent.** The block's conjectural
  content proper — that `h⁴` *is* the next-order regulator term in the
  `q`-expansion of `log Φ_q` — is not stated. What is below is the arithmetic
  consequence of the coefficient, not the claim that identifies it.

## References
- [neumann-zagier1985] Neumann–Zagier, "Volumes of hyperbolic three-manifolds".
- [adams1985hyperbolic] Adams — the two-octahedron decomposition, `Vol(𝓑₃) = 8G`,
  via `QOU.Archimedean.vol_B3`.
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots

open QOU.Archimedean

/-- **Bloch-group input for the Borromean class.**

`B` stands for `B(ℂ)`, `r2` for the Beilinson regulator, and `blochI` for the
symbol `[i]` of the fourth root of unity.

The single field is classical: `r₂([i]) = D(i) = Cl₂(π/2) = G`. Everything the
block asserts about `𝓑₃` is derived from it below. -/
-- Ref: [neumann-zagier1985] Neumann, Zagier, "Volumes of hyperbolic three-manifolds"
-- Ref: [leitner2026] conj:borromean-bloch-group-element
class BorromeanBlochGroupElement {B : Type*} [AddCommGroup B]
    (r2 : B →+ ℝ) (blochI : B) : Prop where
  /-- `r₂([i]) = G`, Catalan's constant. -/
  regulator_bloch_i : r2 blochI = catalan_G

/-- `[𝓑₃] = 8·[i]`.

Thurston: the Borromean complement is two regular ideal octahedra, and each
octahedron is `4·[i]` in the Bloch group. A **definition**, so the factor `8` is
structural rather than assumed. -/
-- Ref: [adams1985hyperbolic] Adams, "The noncompact hyperbolic 3-manifold of minimum volume"
def borromeanClass {B : Type*} [AddCommGroup B] (blochI : B) : B :=
  (8 : ℕ) • blochI

/-- **`r₂[𝓑₃] = Vol(𝓑₃) = 8G`** — the block's headline, *derived*.

Additivity of the regulator on `8·[i]`, then the one assumed value. This is the
step the previous `holds : Prop` carrier could not take, because it had nothing to
take it from. -/
theorem regulator_borromean {B : Type*} [AddCommGroup B]
    (r2 : B →+ ℝ) (blochI : B) [h : BorromeanBlochGroupElement r2 blochI] :
    r2 (borromeanClass blochI) = vol_B3 := by
  rw [borromeanClass, map_nsmul, h.regulator_bloch_i, vol_B3_eq_8_catalan,
      nsmul_eq_mul]
  norm_num

/-- The Borromean class is **non-trivial** in `B`.

A non-zero regulator forces a non-zero class, since `r₂` is additive and so sends
`0` to `0`. The positivity comes from `vol_B3 > 0`, which is proved. -/
theorem borromeanClass_ne_zero {B : Type*} [AddCommGroup B]
    (r2 : B →+ ℝ) (blochI : B) [BorromeanBlochGroupElement r2 blochI] :
    borromeanClass blochI ≠ 0 := by
  intro hzero
  have hr : r2 (borromeanClass blochI) = vol_B3 := regulator_borromean r2 blochI
  rw [hzero, map_zero] at hr
  exact absurd hr.symm (ne_of_gt vol_B3_pos_via_catalan)

/-- The `h⁴` shadow: `r₂[𝓑₃] · (−3/4) = −6G`.

`h4` is a parameter and its value is a hypothesis — sourced to the Markov trace of
`𝓑₃`, not re-derived here. Given it, the product is arithmetic. -/
theorem h4Shadow {B : Type*} [AddCommGroup B]
    (r2 : B →+ ℝ) (blochI : B) [BorromeanBlochGroupElement r2 blochI]
    (h4 : ℝ) (hh4 : h4 = -3 / 4) :
    r2 (borromeanClass blochI) * h4 = -6 * catalan_G := by
  rw [regulator_borromean r2 blochI, vol_B3_eq_8_catalan, hh4]
  ring

/-- The field is satisfiable: take `B = ℝ`, `r₂ = id`, `[i] = G`.

A consistency witness only — deliberately a `theorem` and **not** an `instance`, so
resolution can never discharge the hypothesis for a caller's own `r₂` and `[i]`. -/
theorem borromeanBlochGroupElement_example :
    BorromeanBlochGroupElement (AddMonoidHom.id ℝ) catalan_G where
  regulator_bloch_i := rfl

/-- The field **discriminates**: a symbol whose regulator vanishes is not one.

Without this, satisfiability would be compatible with the class holding of
everything — the failure mode the `holds : Prop` carrier had. -/
theorem not_borromeanBloch_of_regulator_zero {B : Type*} [AddCommGroup B]
    (r2 : B →+ ℝ) (blochI : B) (hz : r2 blochI = 0) :
    ¬ BorromeanBlochGroupElement r2 blochI := by
  intro h
  have := h.regulator_bloch_i
  rw [hz] at this
  exact absurd this.symm (ne_of_gt catalan_G_pos)

end QOU.BraidsAndKnots
