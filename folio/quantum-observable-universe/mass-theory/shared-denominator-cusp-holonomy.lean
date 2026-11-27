import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic


/-!
# Shared-denominator cusp holonomy (conjecture class)

The conjecture: zeros of the q-Pochhammer denominator `(x; q)_n`
enforce the Thurston cusp-completeness conditions
`Hol_μ(z) = Hol_λ(z) = 1` on the corresponding ideal tetrahedron.

Dependency note: this block sits downstream of
`conj:algebraic-geometric-dilog-equivalence` §1 at the **manifest**
level (`uses[]`); the sibling `.lean` files are built self-contained
(no cross-sibling imports), so the dependency is NOT a type-level
`[AlgebraicGeometricEquivalence]` binder here. Conversely, the
alg-geom class's `pole_cusp_matched` hypothesis is exactly what an
instance of THIS class would supply — this conjecture is the
geometric input, not a consequence.

## 2026-08-31 — the class DID have an instance, and the shape is a parameter now

The previous revision of this file, and the `.md`'s Discussion section,
both stated that `SharedDenominatorCuspHolonomy` *"deliberately has **no
instance**: the conjecture's open state is visible in the type system"*, and
explained that strengthening the shape predicate with `im_pos` made *"any
real-constant witness impossible"*.

The first half was false, and the second half is why.  The class's field
concluded `∃ z : ℂ, GeometricShape z` — an existential over **some**
geometric shape, with no link to the root index `k`.  That proposition is
provable outright (`exists_geometricShape` below), so

```lean
example (q x : ℝ) (n : ℕ) : SharedDenominatorCuspHolonomy q x n where
  cusp_complete_of_root := fun _ _ => ⟨Complex.I, …⟩
```

inhabits the class for **every** `q`, `x` and `n`.  Measured 2026-08-31:
`lean`-direct, exit 0.  Excluding real constants excluded the wrong constant;
`z = i` is not real and discharges the whole conjecture in two lines.

The repair is to bind the existential.  The `.md` claims that the root at
`x = q^{-k}` is matched to *the shape parameter `z_k` of cusp `k`*, so the
shape assignment is data the caller supplies: `shape : Fin n → ℂ` is now a
class **parameter** and the field says the **matched** shape `shape k` is
geometric.  An instance can no longer pick the shape, and there is now
genuinely no instance.

Three further changes:

- `shared_denominator_cusp_holonomy` was `:= h.cusp_complete_of_root`, the
  field handed straight back (AGENTS.md §3b-cond item 5).  It now **derives**
  the three consequences of a geometric matched shape, none of which is the
  field.
- `newton_seed_completeness` was **statement-identical** to it — same binders,
  same conclusion, character for character — while its docstring claimed
  something the statement never mentioned: *"the algebraic denominator zeros
  `{q^{-k} : k < n}` are valid Newton–Raphson seed values"*.  There is no
  Newton iteration, no seed and no convergence anywhere in that type.  It is
  removed; the seeding claim is empirical and lives in the `.md` with its two
  witnesses.
- `seed_is_not_the_cusp_shape` is new and is **derived**: at a root index the
  matched shape is not a real number, so the bare algebraic seed `q^{-k}`
  cannot be the cusp shape.  That is the `.md`'s own bounding finding from
  `snappy-cusp-seeding.witness.json` (bare seeds sit `0.4`–`0.9` from
  SnapPy's `z_k`), and it now follows from the conjecture rather than only
  from the measurement.

Bean `qou-z9ws`.

-- Ref: [leitner2026] conj:shared-denominator-cusp-holonomy
-- Ref: [thurston1978] manuscript: The geometry and topology of 3-manifolds
-- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds — see folio/schema/references.ts
-/

namespace QOU.QPochhammer

/-- The geometric-shape predicate over `ℂ` at the shape parameter `z` —
    the *necessary* conditions for cusp completeness (the name says what
    it asserts; the full holonomy content remains open, see below):
    the shape is a **geometric** ideal-tetrahedron shape — non-degenerate
    (`z ≠ 0`, `z ≠ 1`) and of positive imaginary part (upper half-plane,
    positively oriented). A genuine formalisation would additionally carry
    the ideal triangulation and the Neumann-Zagier potential with
    `Hol_μ(z) = Hol_λ(z) = 1`; those gluing equations remain open here,
    but `im_pos` already excludes every real (flattened) shape, so the
    predicate is not dischargeable by a *real* constant witness — see
    `exists_geometricShape` for why that is much weaker than it sounds. -/
-- Ref: [thurston1978] §4.5 (gluing equations)
-- Ref: [futer-gueritaud-angled] Def 2.4 (edge and completeness equations), Prop 2.5 (they glue to a hyperbolic metric; complete iff completeness eqns hold) — held copy, library/angled-survey
structure GeometricShape (z : ℂ) : Prop where
  /-- Shape nondegeneracy: `z ≠ 0` (the degenerate collapsed vertex; the
      meridian holonomy equation `Hol_μ(z) = 1` itself remains open). -/
  shape_ne_zero : z ≠ 0
  /-- Shape nondegeneracy: `z ≠ 1` (the degenerate flat vertex; the
      longitude holonomy equation `Hol_λ(z) = 1` itself remains open). -/
  shape_ne_one : z ≠ 1
  /-- Geometric (positively oriented) shape: `Im z > 0`. -/
  im_pos : 0 < z.im

/-- **A geometric shape exists**, witnessed by `z = i`.

Recorded as a theorem because it is the reason the previous encoding of this
conjecture was empty.  The old class field concluded `∃ z : ℂ,
GeometricShape z` with no link to the root index, and that is exactly this
statement — so the class was inhabited for every `q`, `x`, `n` by a constant
witness, despite the file and the `.md` both asserting it had no instance.

`im_pos` does rule out real constants.  It does not rule out constants. -/
theorem exists_geometricShape : ∃ z : ℂ, GeometricShape z :=
  ⟨Complex.I,
   { shape_ne_zero := Complex.I_ne_zero
     shape_ne_one := by
       intro h
       have := congrArg Complex.im h
       simp at this
     im_pos := by simp }⟩

/-- The shared-denominator conjecture, packaged as a typeclass over a
    state variable `x`, substrate parameter `q`, depth `n`, and the
    **cusp shape assignment** `shape : Fin n → ℂ`.

    An instance asserts that whenever the algebraic denominator `(x; q)_n`
    vanishes at a root of the form `x = q^{-k}`, the *matched* cusp shape
    parameter `shape k` satisfies the Thurston cusp-completeness predicate.

    `shape` is a **parameter**, not a field.  That is what makes the class a
    hypothesis about the caller's cusp data rather than about an assignment
    the instance chose — see `exists_geometricShape` and the module docstring
    for what happened when the shape was existentially quantified instead. -/
-- Ref: [leitner2026] conj:shared-denominator-cusp-holonomy
class SharedDenominatorCuspHolonomy
    (q x : ℝ) (n : ℕ) (shape : Fin n → ℂ) : Prop where
  /-- For each algebraic denominator zero `x = q^{-k}` (i.e. each
      `k < n` with `1 - x q^k = 0`), the matched complex cusp shape
      parameter `shape k` is `GeometricShape`. -/
  -- Ref: [leitner2026] conj:shared-denominator-cusp-holonomy §proof sketch
  cusp_complete_of_root :
    ∀ (k : Fin n), 1 - x * q ^ (k : ℕ) = 0 → GeometricShape (shape k)

/-- **Shared-denominator cusp holonomy**
([`conj:shared-denominator-cusp-holonomy`]), in consequence form.

At an algebraic denominator zero, the matched cusp shape has non-zero
imaginary part and is neither of the two degenerate shapes.

Derived: the conclusion is a conjunction of three consequences of
`GeometricShape (shape k)`, not that proposition, so this is not the class
field restated.  The previous version *was* — it read
`:= h.cusp_complete_of_root`. -/
-- Ref: [leitner2026] conj:shared-denominator-cusp-holonomy
theorem shared_denominator_cusp_holonomy
    (q x : ℝ) (n : ℕ) (shape : Fin n → ℂ)
    [h : SharedDenominatorCuspHolonomy q x n shape] (k : Fin n)
    (hroot : 1 - x * q ^ (k : ℕ) = 0) :
    (shape k).im ≠ 0 ∧ shape k ≠ 0 ∧ shape k ≠ 1 := by
  have hg := h.cusp_complete_of_root k hroot
  exact ⟨hg.im_pos.ne', hg.shape_ne_zero, hg.shape_ne_one⟩

/-- **The bare algebraic seed is not the cusp shape.**

At a root index the matched shape is not a real number, so no real seed —
`q^{-k}` included — equals `shape k`.  The pole-to-cusp correspondence is a
bijection of *labels*, and the shape parameter is a non-trivial function of
the seed.

The `.md` reaches this empirically: `snappy-cusp-seeding.witness.json`
measures the bare seeds at distance `0.4`–`0.9` from SnapPy's `z_k` for
`m004`, `m003` and `L6a4`, and concludes the identity `q₀^{-k} = z_k` cannot
hold.  Here it follows from the conjecture itself, since `im_pos` excludes
every real shape.

This replaces `newton_seed_completeness`, which had the same type as
`shared_denominator_cusp_holonomy` above and a docstring claiming a
Newton–Raphson seeding property its statement did not contain. -/
-- Ref: [leitner2026] conj:shared-denominator-cusp-holonomy §implication
theorem seed_is_not_the_cusp_shape
    (q x : ℝ) (n : ℕ) (shape : Fin n → ℂ)
    [h : SharedDenominatorCuspHolonomy q x n shape] (k : Fin n)
    (hroot : 1 - x * q ^ (k : ℕ) = 0) (r : ℝ) :
    shape k ≠ (r : ℂ) := by
  intro hEq
  have hg := h.cusp_complete_of_root k hroot
  have him : (shape k).im = 0 := by rw [hEq, Complex.ofReal_im]
  have hpos := hg.im_pos
  rw [him] at hpos
  exact lt_irrefl 0 hpos

/-! ## No instance — this is an open primary conjecture

A revision before 2026-08-31 carried a "skeleton" `instance canonical`
witnessing cusp-completeness with the constant real shape `z = 2`. That
instance encoded none of the Thurston gluing-equation content yet
*discharged* the §3b-cond hypothesis for every downstream consumer —
precisely the "fabricated trivial instance" pattern forbidden by AGENTS.md
§3b-tax ("an unproved primary is honestly represented by a content-bearing
class with no instance"). It was removed and `im_pos` was added to block a
real-constant witness.

**That was not enough, and the file said it was.** With the shape
existentially quantified, `z = i` discharged the class for every `q`, `x`,
`n` — see `exists_geometricShape`. The shape assignment is now a class
parameter, so no constant witness of any kind is available, and the class has
genuinely had no instance since. The actual `z_k` for the `k`-th cusp must
come from the Newton–Raphson gluing pipeline
(`computations/q-pochhammer-seed.witness.json` records the trefoil case) —
and by `seed_is_not_the_cusp_shape` it is not the seed itself. -/

/-! ## Index-blindness of `τ_arch` under tetrahedron isometry (`qou-v57s`)

In `snappy-cusp-seeding.witness.json`, `m004` (`n = 2`), `m003` (`n = 2`) and
`L6a4` (`n = 8`) have `n` pairwise-distinct algebraic denominator roots `q₀^{-k}`
while all ideal tetrahedra in each triangulation lie in a **single** edge-relabelling
isometry class (`m = 1`; on `L6a4` the two recorded shapes `1 + i` and `(1 + i)/2`
are related by two applications of `z ↦ 1/(1 − z)`).

By pigeonhole (`Fintype.card_le_of_injective`), no map `τ_arch : Fin n → Fin m`
from `n` roots to `m < n` shape/isometry classes can be injective, and for
`m = 1` every root index maps to the exact same class. -/

/-- **First step of the `L6a4` edge-relabelling orbit (`qou-v57s`).**
In cleared-denominator form for `z ↦ 1/(1 − z)`, rotating `z₀ = 1 + i` gives
`z₁ = i` since `(1 − (1 + i)) · i = −i² = 1`. -/
theorem l6a4_orbit_step_one :
    (1 - (1 + Complex.I)) * Complex.I = (1 : ℂ) := by
  calc (1 - (1 + Complex.I)) * Complex.I
      = -(Complex.I ^ 2) := by ring
    _ = 1 := by rw [Complex.I_sq]; ring

/-- **Second step of the `L6a4` edge-relabelling orbit (`qou-v57s`).**
Rotating `z₁ = i` under `z ↦ 1/(1 − z)` gives SnapPy's second recorded `L6a4`
shape `z₂ = (1 + i)/2` since `(1 − i) · (1 + i)/2 = (1 − i²)/2 = 1`. -/
theorem l6a4_orbit_step_two :
    (1 - Complex.I) * ((1 + Complex.I) / 2) = (1 : ℂ) := by
  calc (1 - Complex.I) * ((1 + Complex.I) / 2)
      = (1 - Complex.I ^ 2) / 2 := by ring
    _ = 1 := by rw [Complex.I_sq]; ring

/-- **Third step closing the `L6a4` 3-cycle (`qou-v57s`).**
Rotating `z₂ = (1 + i)/2` returns to `z₀ = 1 + i` since
`(1 − (1 + i)/2) · (1 + i) = (1 − i²)/2 = 1`. -/
theorem l6a4_orbit_step_three :
    (1 - (1 + Complex.I) / 2) * (1 + Complex.I) = (1 : ℂ) := by
  calc (1 - (1 + Complex.I) / 2) * (1 + Complex.I)
      = (1 - Complex.I ^ 2) / 2 := by ring
    _ = 1 := by rw [Complex.I_sq]; ring

/-- **Pigeonhole non-injectivity of `τ_arch` (`qou-v57s`).**
Whenever a triangulation has `m` distinct shape or tetrahedron-isometry classes
and `n > m` distinct algebraic denominator roots, no map
`tau_arch : Fin n → Fin m` can be injective. -/
theorem tau_arch_not_injective_of_lt_roots {n m : ℕ} (hmn : m < n)
    (tau_arch : Fin n → Fin m) : ¬ Function.Injective tau_arch := by
  intro hinj
  have hcard := Fintype.card_le_of_injective tau_arch hinj
  simp only [Fintype.card_fin] at hcard
  omega

/-- **Complete index-blindness on a single-isometry-class triangulation (`qou-v57s`).**
When all tetrahedra belong to one isometry class (`m = 1`, as for `m004`, `m003`
and `L6a4` up to edge relabelling), `tau_arch : Fin n → Fin 1` assigns the exact
same class to every root index `j, k : Fin n`. -/
theorem tau_arch_constant_of_single_isometry_class {n : ℕ}
    (tau_arch : Fin n → Fin 1) (j k : Fin n) :
    tau_arch j = tau_arch k :=
  Subsingleton.elim (tau_arch j) (tau_arch k)

/-- **Instantiation on the three `snappy-cusp-seeding` manifolds (`qou-v57s`).**
Neither the `n = 2 → m = 1` assignments (`m004`, `m003`) nor the `n = 8 → m = 2`
raw-shape and `n = 8 → m = 1` isometry-class assignments (`L6a4`) can be injective. -/
theorem snappy_cusp_seeding_non_injective
    (tau_m004 : Fin 2 → Fin 1)
    (tau_l6a4_raw : Fin 8 → Fin 2)
    (tau_l6a4_iso : Fin 8 → Fin 1) :
    ¬ Function.Injective tau_m004
      ∧ ¬ Function.Injective tau_l6a4_raw
      ∧ ¬ Function.Injective tau_l6a4_iso :=
  ⟨tau_arch_not_injective_of_lt_roots (by decide) tau_m004,
   tau_arch_not_injective_of_lt_roots (by decide) tau_l6a4_raw,
   tau_arch_not_injective_of_lt_roots (by decide) tau_l6a4_iso⟩

end QOU.QPochhammer
