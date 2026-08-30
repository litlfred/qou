import QOU.Archimedean.BlochWignerLobachevsky

/-!
# QOU.Archimedean.BlochWignerSymmetry — the cyclic symmetry of `D`

`BlochWigner_lob` is defined in the sibling module as a sum of Lobachevsky
values at the three dihedral angles of the ideal tetrahedron of shape `z`:

```
D(z) = Λ(arg z) + Λ(arg (1/(1−z))) + Λ(arg (1 − 1/z))
```

The three shape parameters `z`, `1/(1−z)`, `1 − 1/z` describe **the same
tetrahedron** viewed from its three pairs of opposite edges. So `D` is invariant
under the order-3 Möbius rotation `z ↦ 1 − 1/z`.

This file proves that. The point is how cheap it is: the invariance is
**combinatorial, not analytic**. Under `w = 1 − 1/z` the three angle-arguments
are literally permuted, because of three field identities

```
1 − w = 1/z          1/(1 − w) = z          1 − 1/w = 1/(1 − z)
```

so the Lobachevsky sum is reordered and nothing is computed. No dilogarithm, no
polylogarithm, no analysis — which matters, because Mathlib has none of those
(bean `mlgp`, Gaps 1 and 4).

## Why this was worth isolating

Bean `mlgp` recorded that upgrading the literature-cited volume-conjecture
instances would need the method of steepest descent, which Mathlib lacks
entirely. That is true of proving Ohtsuki's asymptotic expansion. It is **not**
true of the identity that carries the *volume* out of that expansion.

`QOU/Archimedean/FiveTwoOhtsukiBridge.lean` reduces the `5₂` volume conjecture,
given Ohtsuki's expansion, to

```
2π · Re ζ = 3 · D(y₀)
```

and that in turn reduces to exactly two facts: a cancellation of `arg`–`log`
correction terms, and `D(x₀) = D(y₀)` where `x₀ = 1 − 1/y₀`. **The second is
this file's `BlochWigner_lob_mobius_cycle`** — an instance of the cyclic
symmetry, needing nothing Mathlib does not already have.

Archimedean (ℂ → ℝ).

-- Ref: [thurston1978] ideal tetrahedra and their three shape parameters
-- Ref: [zagier1986] the Bloch–Wigner dilogarithm
-/

namespace QOU.Archimedean

open Complex

/-! ## The three field identities

Everything below rests on these. They are `field_simp`/`ring` facts about the
order-3 Möbius map `z ↦ 1 − 1/z`, with no complex analysis in sight. -/

/-- Under `w = 1 − 1/z`, the "one minus" slot returns `1/z`. -/
theorem one_sub_mobius (z : ℂ) : 1 - (1 - 1 / z) = 1 / z := by ring

/-- Under `w = 1 − 1/z`, the second shape parameter returns `z` itself.
This is the step that closes the 3-cycle. -/
theorem inv_one_sub_mobius (z : ℂ) (hz : z ≠ 0) :
    1 / (1 - (1 - 1 / z)) = z := by
  rw [one_sub_mobius]
  field_simp

/-- Under `w = 1 − 1/z`, the third shape parameter returns `1/(1−z)`.

Note the shape of the proof: rewrite `1 − 1/z` as `(z−1)/z` **first**, so the
nested division becomes a single quotient and `field_simp` has both non-vanishing
facts it needs (`z ≠ 0` and `z − 1 ≠ 0`) already in hand. Trying to `field_simp`
the nested form directly asks it to discharge `1 − 1/z ≠ 0` on its own. -/
theorem one_sub_inv_mobius (z : ℂ) (hz : z ≠ 0) (hz1 : z ≠ 1) :
    1 - 1 / (1 - 1 / z) = 1 / (1 - z) := by
  have hz1' : z - 1 ≠ 0 := sub_ne_zero.mpr hz1
  have hzm : (1 : ℂ) - 1 / z = (z - 1) / z := by field_simp
  rw [hzm, one_div_div]
  field_simp
  ring

/-! ## The angles are permuted, not recomputed -/

/-- `tetAngle₁` of the rotated shape is `tetAngle₃` of the original —
definitionally, since both are `(1 − 1/z).arg`. -/
theorem tetAngle₁_mobius (z : ℂ) : tetAngle₁ (1 - 1 / z) = tetAngle₃ z := rfl

/-- `tetAngle₂` of the rotated shape is `tetAngle₁` of the original. -/
theorem tetAngle₂_mobius (z : ℂ) (hz : z ≠ 0) :
    tetAngle₂ (1 - 1 / z) = tetAngle₁ z := by
  unfold tetAngle₂ tetAngle₁
  rw [inv_one_sub_mobius z hz]

/-- `tetAngle₃` of the rotated shape is `tetAngle₂` of the original. -/
theorem tetAngle₃_mobius (z : ℂ) (hz : z ≠ 0) (hz1 : z ≠ 1) :
    tetAngle₃ (1 - 1 / z) = tetAngle₂ z := by
  unfold tetAngle₃ tetAngle₂
  rw [one_sub_inv_mobius z hz hz1]

/-! ## The symmetry -/

/-- **`D` is invariant under the order-3 Möbius rotation `z ↦ 1 − 1/z`.**

The proof is a reordering: the three Lobachevsky summands are permuted
cyclically, so the sum is unchanged. Nothing is evaluated. -/
theorem BlochWigner_lob_mobius_cycle (z : ℂ) (hz : z ≠ 0) (hz1 : z ≠ 1) :
    BlochWigner_lob (1 - 1 / z) = BlochWigner_lob z := by
  unfold BlochWigner_lob
  rw [tetAngle₁_mobius, tetAngle₂_mobius z hz, tetAngle₃_mobius z hz hz1]
  ring

/-- **Lemma (i) of the `5₂` bridge.** With `x₀ = 1 − 1/y₀`, the two shapes have
the same Bloch–Wigner value. Verified numerically at 40 digits
(`D(x₀) − D(y₀) = 1.1e-41`) before it was proved; here it is a corollary of the
cyclic symmetry, and needs no `5₂`-specific input at all.

This is one of the two facts `FiveTwoOhtsukiBridge.ohtsuki_sum_im_eq_three_blochWigner`
rests on. The other is the `arg`–`log` cancellation, which is not a `D`
symmetry and is still open. -/
theorem blochWigner_xOf_eq (y : ℂ) (hy : y ≠ 0) (hy1 : y ≠ 1) :
    BlochWigner_lob (1 - 1 / y) = BlochWigner_lob y :=
  BlochWigner_lob_mobius_cycle y hy hy1

end QOU.Archimedean
