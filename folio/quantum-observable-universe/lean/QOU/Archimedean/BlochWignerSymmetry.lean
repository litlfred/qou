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
nested division becomes a single quotient and `field_simp` has the non-vanishing
facts it needs already in hand. Trying to `field_simp` the nested form directly
asks it to discharge `1 − 1/z ≠ 0` on its own.

**Both** orientations of the non-vanishing fact have to be in context. `field_simp`
matches hypotheses syntactically, so `z − 1 ≠ 0` does not discharge the `(1 − z)⁻¹`
that the right-hand side contributes: with only that one, the goal reduces to
`-1 = z * (1 - z)⁻¹ - (1 - z)⁻¹` and stalls there. -/
theorem one_sub_inv_mobius (z : ℂ) (hz : z ≠ 0) (hz1 : z ≠ 1) :
    1 - 1 / (1 - 1 / z) = 1 / (1 - z) := by
  have hz1' : z - 1 ≠ 0 := sub_ne_zero.mpr hz1
  have h1z : (1 : ℂ) - z ≠ 0 := sub_ne_zero.mpr (Ne.symm hz1)
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

This is one of the facts `FiveTwoOhtsukiBridge.ohtsuki_sum_im_eq_three_blochWigner`
rests on. The others are `BlochWigner_lob_inv` below and an `arg`–`log`
cancellation which, once the cubic is used, is three `arg` evaluations. -/
theorem blochWigner_xOf_eq (y : ℂ) (hy : y ≠ 0) (hy1 : y ≠ 1) :
    BlochWigner_lob (1 - 1 / y) = BlochWigner_lob y :=
  BlochWigner_lob_mobius_cycle y hy hy1

/-! ## The other symmetry: inversion

`z ↦ 1/z` swaps the *orientation* of the ideal tetrahedron. The three angles are
again permuted, but each one is also **negated**, so `D` picks up a sign. Like
the Möbius 3-cycle this is a reordering rather than a computation — the only
analytic input is that `arg` is odd off the branch cut, which is why the
hypothesis is `z.im ≠ 0` rather than anything about `D`. -/

/-- `arg z ≠ π` off the real axis. Mathlib's `Complex.arg_inv` and `arg_conj`
both carry an `if arg z = π` guard for the branch cut; this is the side
condition that discharges it, and it is the *only* thing `z.im ≠ 0` is used for
below. -/
theorem arg_ne_pi_of_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) : z.arg ≠ Real.pi :=
  fun h => hz (Complex.arg_eq_pi_iff.mp h).2

/-- `arg (1/z) = −arg z` off the real axis. -/
theorem arg_one_div_of_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) : (1 / z).arg = -z.arg := by
  rw [one_div, Complex.arg_inv, if_neg (arg_ne_pi_of_im_ne_zero hz)]

/-- `1/z` is off the real axis when `z` is: `Im z⁻¹ = −Im z / |z|²`. Needed three
times below, and again in the `5₂` bridge, because every `hbw`-style hypothesis
about a dilogarithm has to be applied at both `z` and `1/z`. -/
theorem one_div_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) : (1 / z).im ≠ 0 := by
  have hz0 : z ≠ 0 := fun h => hz (by rw [h]; simp)
  rw [one_div, Complex.inv_im, div_ne_zero_iff]
  exact ⟨neg_ne_zero.mpr hz, (Complex.normSq_pos.mpr hz0).ne'⟩

/-- **`D` is odd under inversion**: `D(1/z) = −D(z)` for `z` off the real axis.

Under `z ↦ 1/z` the three shape parameters go to their own reciprocals, but
*shuffled*: `1/z`'s first angle is minus `z`'s first, its second is minus `z`'s
third, and its third is minus `z`'s second. Concretely
`1 − 1/(1/z) = 1 − z` and `1/(1 − 1/z)` is the reciprocal of `z`'s third shape.
So the sum is again a reordering, this time of three negated terms.

The hypothesis `z.im ≠ 0` is exactly what keeps all three reciprocals off the
`arg` branch cut; it cannot be dropped, since at a real `z` the identity reads
`0 = −0` only because both sides vanish for a different reason
(`BlochWigner_lob_real_eq_zero`). -/
theorem BlochWigner_lob_inv {z : ℂ} (hz : z.im ≠ 0) :
    BlochWigner_lob (1 / z) = -BlochWigner_lob z := by
  have hz0 : z ≠ 0 := fun h => hz (by rw [h]; simp)
  have h1z : ((1 : ℂ) - z).im ≠ 0 := by simpa using hz
  have hinv : ((1 : ℂ) - 1 / z).im ≠ 0 := by
    simpa using one_div_im_ne_zero hz
  unfold BlochWigner_lob tetAngle₁ tetAngle₂ tetAngle₃
  rw [arg_one_div_of_im_ne_zero hz,
    show (1 : ℂ) - 1 / (1 / z) = 1 - z by rw [one_div_one_div],
    show (1 : ℂ) / (1 - 1 / z) = 1 / (1 - 1 / z) from rfl,
    arg_one_div_of_im_ne_zero hinv, arg_one_div_of_im_ne_zero h1z,
    Lob_neg, Lob_neg, Lob_neg]
  ring

/-! ## And the third: conjugation

`z ↦ z̄` is the *other* orientation reversal. Unlike inversion it does not
permute the three angles at all — it negates each one where it stands — so the
proof is one line shorter and the sign is the same. Both are needed: the `5₂`
bridge reaches the corpus's triangulation shape `y₊` from Ohtsuki's `y₀` by
composing them, `y₊ = conj (1/y₀)`. -/

/-- `arg z̄ = −arg z` off the real axis, discharging the same branch-cut `if`. -/
theorem arg_conj_of_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) :
    ((starRingEnd ℂ) z).arg = -z.arg := by
  rw [Complex.arg_conj, if_neg (arg_ne_pi_of_im_ne_zero hz)]

/-- **`D` is odd under conjugation**: `D(z̄) = −D(z)` for `z` off the real axis.

Conjugation commutes with all three Möbius maps (`1 − z̄ = conj (1 − z)`,
`1/(1 − z̄) = conj (1/(1 − z))`, `1 − 1/z̄ = conj (1 − 1/z)`), because they have
*real* coefficients. So each angle is negated in place and `Λ` is odd.

This is the formal content of the remark in `FiveTwoOhtsukiBridge` that the
conjugation half of the two-cubic reconciliation is `D(z̄) = −D(z)`. -/
theorem BlochWigner_lob_conj {z : ℂ} (hz : z.im ≠ 0) :
    BlochWigner_lob ((starRingEnd ℂ) z) = -BlochWigner_lob z := by
  have h1z : ((1 : ℂ) - z).im ≠ 0 := by simpa using hz
  have h2 : ((1 : ℂ) / (1 - z)).im ≠ 0 := one_div_im_ne_zero h1z
  have h3 : ((1 : ℂ) - 1 / z).im ≠ 0 := by simpa using one_div_im_ne_zero hz
  have c1 : (1 : ℂ) - (starRingEnd ℂ) z = (starRingEnd ℂ) (1 - z) := by simp
  have c2 : (1 : ℂ) / ((starRingEnd ℂ) (1 - z)) = (starRingEnd ℂ) (1 / (1 - z)) := by simp
  have c3 : (1 : ℂ) - 1 / ((starRingEnd ℂ) z) = (starRingEnd ℂ) (1 - 1 / z) := by simp
  unfold BlochWigner_lob tetAngle₁ tetAngle₂ tetAngle₃
  rw [c1, c2, c3, arg_conj_of_im_ne_zero hz, arg_conj_of_im_ne_zero h2,
    arg_conj_of_im_ne_zero h3, Lob_neg, Lob_neg, Lob_neg]
  ring

/-- **`D(conj (1/z)) = D(z)`** — the two orientation reversals compose back to
the identity on `D`.

This is the step that connects Ohtsuki's shape `y₀` (a root of `y³ − 3y² + 2y −
1` in the *upper* half plane) to the corpus's triangulation shape `y₊` (a root
of the reciprocal cubic `y³ − 2y² + 3y − 1`, also upper): the reciprocal drops
into the lower half plane, and conjugation lifts it back. Measured,
`y₊ = 0.7849201454990266… + 1.3071412786820454…i = conj (1/y₀)`, and both give
`D = 0.9427073627769277…`. -/
theorem BlochWigner_lob_conj_inv {z : ℂ} (hz : z.im ≠ 0) :
    BlochWigner_lob ((starRingEnd ℂ) (1 / z)) = BlochWigner_lob z := by
  rw [BlochWigner_lob_conj (one_div_im_ne_zero hz), BlochWigner_lob_inv hz, neg_neg]

end QOU.Archimedean
