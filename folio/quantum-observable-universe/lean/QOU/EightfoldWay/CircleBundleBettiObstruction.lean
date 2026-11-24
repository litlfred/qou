import Mathlib.Tactic

/-!
# QOU.Eightfold.CircleBundleBettiObstruction — the QOU contact 3-manifold is not `S³`

## The question this answers

The framework uses an ambient `S³` in two distinct places and calls both "the
arena":

* `def:reeb-bundle` (`mass-theory/reeb-bundle.md`) — the link of the exceptional
  divisor of a blow-up: a circle bundle over `𝒮_p ≅ ℂP¹ ≅ S²`, i.e. the Hopf
  fibration, i.e. the coset projection `SU(2) → SU(2)/U(1)`;
* `rem:brings-qou-4tuple` (`brings-surface/brings-qou-4tuple.md`, item 1) — the
  QOU's own CR manifold `M_S = {(p,η) ∈ T*S : |η| = 1}`, the unit circle bundle
  over Bring's surface, carrying the contact form `Θ = λ|_{M_S}` restricted from
  the Liouville form.  This is the manifold on which `Θ ∧ dΘ` — the natural
  degree-3 volume form the owner's question asks after — actually lives.

Both are circle bundles over a closed orientable surface.  They are **not the
same 3-manifold**, and this file proves it from the framework's own Descartes
axiom `χ(𝒮) = −6` — no extra input.

## The theorem

`descartes_forces_b1_pos` — a circle bundle whose base has Euler characteristic
`−6` has total space with **first Betti number at least 8**, whatever its Euler
number.  Since `b₁(S³) = 0`, `not_sphere_of_descartes` follows: the QOU contact
manifold is not `S³`.

The consequence for the corpus: the Alexander–Markov ambient `S³`, the
Reeb-bundle `S³` over the exceptional divisor, and the QOU contact manifold `M_S`
are **three** objects, not one.  Only the first two can be `S³`; `M_S` provably
cannot.  Any identification of "the arena" with "the manifold carrying `Θ ∧ dΘ`"
is therefore false as stated, and must be read locally (at a blow-up point)
rather than globally.

## The model, and what is cited rather than derived

For an **oriented circle bundle** `S¹ → M → Σ_g` over a closed orientable
surface of genus `g` with Euler number `e`, the Gysin sequence with `ℚ`
coefficients gives

`0 → H¹(Σ_g;ℚ) → H¹(M;ℚ) → H⁰(Σ_g;ℚ) --∪e--> H²(Σ_g;ℚ)`

so `b₁(M) = 2g` when `e ≠ 0` and `b₁(M) = 2g + 1` when `e = 0` (then
`M ≅ Σ_g × S¹`).  That is `totalB1` below: **the count is the model**, cited
standard algebraic topology, exactly as `Sym2GateFSTrichotomy.sym2Singlets`
carries the Frobenius–Schur singlet count.  Mathlib has no circle-bundle Gysin
sequence to derive it from.

What is *not* cited is the conclusion: the case analysis, the recovery of the
genus from the Euler characteristic, and the strict positivity are proved here.
Note in particular that the `e = 0` branch is not a special case to be waved
away — it gives a *larger* `b₁`, so the obstruction holds without any hypothesis
on the Euler number at all.

## Base ring (§7c)

Integer arithmetic only.  No ring parameter, no ordering beyond `ℤ`/`ℕ`, no
archimedean content.

-- Ref: [hatcher2002] §4.D (the Gysin sequence of an oriented sphere bundle;
-- for a circle bundle over a closed orientable surface it yields
-- `b₁(total) = 2g` when the Euler number is nonzero and `2g + 1` when it
-- vanishes).
-- Ref: [leitner2026] `rem:brings-qou-4tuple` item 1 (the CR manifold `M_S` as
-- the unit circle bundle in `T*S`), `def:reeb-bundle` (the Hopf/coset circle
-- bundle over the exceptional divisor), and the Descartes condition
-- `χ(𝒮) = −6` (`prop:archimedean-condition`).
-/

namespace QOU.Eightfold.CircleBundleBettiObstruction

/-! ## 1. The two integer invariants -/

/-- Euler characteristic of a closed orientable surface of genus `g`. -/
def surfaceEuler (g : ℕ) : ℤ := 2 - 2 * (g : ℤ)

/-- First Betti number of the total space of an oriented circle bundle over a
closed orientable surface of genus `g` with Euler number `e`.

**This is the model** — the Gysin count, cited not derived; see the module
docstring. -/
def totalB1 (g : ℕ) (e : ℤ) : ℕ := if e = 0 then 2 * g + 1 else 2 * g

/-- First Betti number of `S³`.  Recorded as a definition so the statements
below read as comparisons of invariants rather than as arithmetic on `0`. -/
def sphereB1 : ℕ := 0

/-! ## 2. Genus is recoverable from the Euler characteristic -/

/-- The Euler characteristic determines the genus. -/
theorem genus_injective_of_surfaceEuler {g h : ℕ}
    (hgh : surfaceEuler g = surfaceEuler h) : g = h := by
  unfold surfaceEuler at hgh
  omega

/-- `χ = 2` characterises the sphere. -/
theorem surfaceEuler_eq_two_iff {g : ℕ} : surfaceEuler g = 2 ↔ g = 0 := by
  unfold surfaceEuler
  omega

/-- The Descartes condition `χ = −6` pins the genus to `4`. -/
theorem genus_eq_four_of_descartes {g : ℕ} (h : surfaceEuler g = -6) : g = 4 := by
  unfold surfaceEuler at h
  omega

/-- The Descartes base is not a sphere. -/
theorem descartes_not_sphere_base : surfaceEuler 4 ≠ 2 := by decide

/-! ## 3. What a vanishing first Betti number costs -/

/-- A circle bundle whose total space has `b₁ = 0` must sit over a sphere, and
its Euler number must be nonzero.  Both branches of the Gysin count are used:
`e ≠ 0` forces `2g = 0`, and `e = 0` forces the impossible `2g + 1 = 0`. -/
theorem base_sphere_of_totalB1_eq_zero {g : ℕ} {e : ℤ}
    (h : totalB1 g e = 0) : g = 0 ∧ e ≠ 0 := by
  unfold totalB1 at h
  by_cases he : e = 0
  · rw [if_pos he] at h; omega
  · rw [if_neg he] at h; exact ⟨by omega, he⟩

/-- Restated through the Euler characteristic: a `b₁ = 0` total space forces
`χ(base) = 2`. -/
theorem base_euler_eq_two_of_totalB1_eq_zero {g : ℕ} {e : ℤ}
    (h : totalB1 g e = 0) : surfaceEuler g = 2 :=
  surfaceEuler_eq_two_iff.mpr (base_sphere_of_totalB1_eq_zero h).1

/-! ## 4. The theorem -/

/-- **The theorem.**  A circle bundle over a base of Euler characteristic `−6`
has total space with first Betti number at least `8`, *whatever* its Euler
number.  No hypothesis on `e` is needed: the `e = 0` branch only makes `b₁`
larger. -/
theorem descartes_forces_b1_pos {g : ℕ} {e : ℤ} (hg : surfaceEuler g = -6) :
    8 ≤ totalB1 g e := by
  have hg4 : g = 4 := genus_eq_four_of_descartes hg
  subst hg4
  unfold totalB1
  by_cases he : e = 0
  · rw [if_pos he]; omega
  · rw [if_neg he]

/-- **The exclusion.**  The QOU contact manifold — the unit circle bundle over
Bring's surface, whose Euler characteristic the Descartes condition fixes at
`−6` — is not `S³`.

The invariant is the **first Betti number**: `8` against `0`.  This is a
structural exclusion, not a scope-limited negative; it holds for every Euler
number and so for every circle bundle over that base. -/
theorem not_sphere_of_descartes {g : ℕ} {e : ℤ} (hg : surfaceEuler g = -6) :
    totalB1 g e ≠ sphereB1 := by
  have := descartes_forces_b1_pos (e := e) hg
  unfold sphereB1
  omega

/-! ## 5. The two bundles are different — one can be `S³`, the other cannot

`def:reeb-bundle` sits over the exceptional divisor `𝒮_p ≅ ℂP¹`, genus `0`; the
link of a `(−1)`-curve has Euler number `−1`.  `rem:brings-qou-4tuple` sits over
Bring's surface, genus `4`.  The first is Betti-compatible with `S³`; the second
is not.  So the corpus's two "arenas" are provably distinct 3-manifolds, and the
recorded contradiction between `rem:markov-trace-ambient-s3` and
`docs/audits/2026-06-28-ed-ambient-s3-gauge-embedding-wlambda-scope.md` §(i) is
a conflation of two objects under one glyph, not a disagreement about one. -/

theorem reeb_bundle_b1 : totalB1 0 (-1) = sphereB1 := by decide

theorem descartes_bundle_b1 : totalB1 4 (-6) = 8 := by decide

/-- The two arenas are distinguished by an invariant of the total space. -/
theorem arenas_are_distinct : totalB1 0 (-1) ≠ totalB1 4 (-6) := by decide

end QOU.Eightfold.CircleBundleBettiObstruction
