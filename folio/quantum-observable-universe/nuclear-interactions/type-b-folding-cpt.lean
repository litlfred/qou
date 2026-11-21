import Mathlib.Algebra.Algebra.Hom
import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.TypeBFoldingCpt — the D22 conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:type-b-folding-cpt`](type-b-folding-cpt.md): *D22 Type-B folding*.

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## History

* **2026-09-05.** The carrier read `class TypeBFoldingCpt where holds : Prop`, which an
  instance discharges with `⟨True⟩` (bean `qou-tsnp`, census
  `docs/audits/2026-08-23-free-prop-field-census.md`). It was repaired into a crystal-level
  carrier: a caller-supplied crystal, a label fold `i ↦ n - i`, and a vertex involution.
* **2026-11-20.** The crystal carrier gained an intertwining field (bean `qou-dx7g`).
* **2026-11-21 (this version).** The block was restated at the level of Coxeter groups and
  Hecke algebras for every `n` (owner choice *"Restate at Coxeter/Hecke level"*, then
  *"All"* on the follow-up card, which included rewriting this carrier at the Hecke
  level). For odd `n` the fold of the `𝔰𝔩ₙ` Cartan datum puts the adjacent roots `α_m`,
  `α_{m+1}` in one orbit, so the block makes no Cartan-datum or crystal claim, and the
  crystal fields are dropped here. Nothing in the library consumed them.

## What is encoded

The caller supplies an `R`-algebra `A`, elements `T i` for the labels `i ∈ [1, n-1]`, an
`R`-algebra map `θ : A → A`, and two predicates `stable`, `anti` on `A`.

1. **Hecke relations.** `T i * T i = h • T i + 1` (with `h = q - q⁻¹` in the block's
   normalisation), far generators commute, near generators satisfy the braid relation.
2. **The fold.** `θ (T i) = T (n - i)`: the diagram reversal `ι : sᵢ ↔ s_{n-i}`, lifted to
   an algebra map. `θ` is an involution of `A`. The generators are pairwise distinct, so
   the fold genuinely moves the generators it should.
3. **Matter and antimatter.** `stable x ↔ θ x = x` and `anti x ↔ θ x ≠ x`.

All data are supplied by the **caller**, so the class is false for data that does not
behave this way (refutability theorems at the end).

## What is DERIVED rather than axiomatised

* `typeBFold_pair_fixed` — for `i + 2 ≤ n - i`, the product `T i * T (n - i)` is
  `θ`-fixed. Uses the commuting of far generators.
* `typeBFold_middle_fixed` — for odd `n = 2m + 1`, the element `T m * T (m+1) * T m` is
  `θ`-fixed. Uses the braid relation. These two, with the fixed generator `T (n/2)` for
  even `n` (`typeBFold_fixed_root`), are the images of the generators of the folded Coxeter
  group of type `B_{⌊n/2⌋}`: the longest elements of the `ι`-orbits, of lengths 2, 3 and 1.
  That the fixed subalgebra is a Hecke algebra with these weights is **not** derived here.
* `typeBFold_gen_anti_iff` — a generator `T i` is antimatter exactly when `n ≠ 2i`. So for
  odd `n` every generator is antimatter, and the stable elements produced by the fold are
  products such as the two above.
* `typeBFold_no_global_chirality_grading` — if any stable element exists, `A` admits no
  globally `θ`-odd chirality grading. This is the dilemma of
  `QOU.StandardModel.Chirality.stable_matter_and_global_chirality_incompatible`, re-derived
  from this carrier's fields; it agrees with that file's scope-(a) reading.
* The arithmetic of the reversal (`typeBFold_orbit_*`): the `ι`-orbits on `[1, n-1]` are
  indexed by `min i (n - i) ∈ [1, n/2]`, so the folded group has rank `n / 2` (the floor,
  in `ℕ`), the arithmetic behind the block's `B_{⌊n/2⌋}`.

## What is NOT encoded, and why

* **The weight function and type `B`.** The corpus has no Coxeter-group type, so the
  identification of the folded group as type `B_{⌊n/2⌋}` with weights 1, 2, 3 (Lusztig 2003
  §16.2) is stated in the block and checked numerically
  (`computations/probes/bridge_b/h15_*`, `h19_*`), not formalised.
* **Bar-invariance of the GS normal forms.** Carried by
  `QOU.BraidKnot.SymmetricCrystalPairProduction` (block
  `conj:symmetric-crystal-pair-production`); restating it here would duplicate a carrier.
* **The `CPT = C ⊗ P ⊗ T` decomposition.** Needs `C`, `P` and `T` as maps on one common
  type, whose carriers are three separate blocks; that type must grow first. As fixed in
  #6728, the bar involution is `P·C·T` composed and covers `q ↦ q⁻¹`, while the fold here
  is `R`-linear with `q` held fixed.
* **Existence.** No instance on the corpus's Hecke types is provided.

## Base ring

Generic: `R` is any commutative ring and `A` any `R`-algebra. Nothing archimedean is
needed (§7c). The refutation witnesses use `ℚ` only as a concrete commutative example.

-- Ref: [lusztig2003] Lusztig, "Hecke Algebras with Unequal Parameters," CRM Monograph Series 18 (2003), Sec. 16.2
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/type-b-folding-cpt.ts
-/

namespace QOU.BraidsAndKnots

/-! ### Unconditional arithmetic of the diagram reversal -/

/-- The label range `[1, n-1]` is closed under the diagram reversal `i ↦ n - i`. -/
theorem typeBFold_label_mem_range {n i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    1 ≤ n - i ∧ n - i ≤ n - 1 := by omega

/-- **Orbit representatives.** `min i (n - i)` is constant on `ι`-orbits and lands in
`[1, n/2]`, the label set of the folded group. -/
theorem typeBFold_orbit_representative_range {n i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    1 ≤ min i (n - i) ∧ min i (n - i) ≤ n / 2 := by omega

/-- **`min i (n - i)` is a complete invariant of the `ι`-orbits**: two labels share a
representative exactly when they are equal or swapped by the reversal. With the previous
theorem, the orbits are indexed by `[1, n/2]`, so the folded group has rank `n / 2`. -/
theorem typeBFold_orbit_complete_invariant {n i j : ℕ}
    (hi : 1 ≤ i) (hi' : i ≤ n - 1) (hj : 1 ≤ j) (hj' : j ≤ n - 1) :
    min i (n - i) = min j (n - j) ↔ (j = i ∨ j = n - i) := by omega

/-- **A label is `ι`-fixed exactly when `n = 2i`**; so for odd `n` no label is fixed. -/
theorem typeBFold_label_fixed_iff_even {n i : ℕ} (hi : 1 ≤ i) :
    n - i = i ↔ n = 2 * i := by omega

/-! ### The carrier -/

/-- **CONJECTURE (D22).** Type-B Coxeter folding realises CPT via `ℤ/2` fixed points.

The diagram reversal `ι : sᵢ ↔ s_{n-i}` lifts to an algebra involution `θ` of the Hecke
algebra, `θ (T i) = T (n - i)`; stable matter is the `θ`-fixed part, antimatter the part `θ`
moves. `A`, `n`, `h`, `T`, `θ`, `stable` and `anti` are supplied by the caller.

**No instance is provided.** Downstream results consume this as
`[TypeBFoldingCpt R A n h T θ stable anti]` and are conditional on it.

-- Ref: [lusztig2003] Lusztig, "Hecke Algebras with Unequal Parameters," CRM Monograph Series 18 (2003), Sec. 16.2
-- Ref: [leitner2026] conj:type-b-folding-cpt -/
class TypeBFoldingCpt (R A : Type*) [CommRing R] [Ring A] [Algebra R A] (n : ℕ) (h : R)
    (T : ℕ → A) (θ : A →ₐ[R] A) (stable anti : A → Prop) : Prop where
  /-- **Hecke quadratic relation**, `(T i - q)(T i + q⁻¹) = 0` written as
  `T i * T i = (q - q⁻¹) T i + 1` with `h = q - q⁻¹`. -/
  quadratic : ∀ i, 1 ≤ i → i ≤ n - 1 → T i * T i = h • T i + 1
  /-- **Far generators commute.** -/
  braid_far : ∀ i j, 1 ≤ i → j ≤ n - 1 → i + 2 ≤ j → T i * T j = T j * T i
  /-- **Near generators satisfy the braid relation.** -/
  braid_near : ∀ i, 1 ≤ i → i + 1 ≤ n - 1 →
    T i * T (i + 1) * T i = T (i + 1) * T i * T (i + 1)
  /-- **The generators are pairwise distinct**, so `θ` cannot fix a generator it is meant to
  move (this rules out the degenerate data with all `T i` equal). -/
  gens_ne : ∀ i j, 1 ≤ i → i ≤ n - 1 → 1 ≤ j → j ≤ n - 1 → i ≠ j → T i ≠ T j
  /-- **The fold**: `θ` lifts the diagram reversal, `θ (T i) = T (n - i)`. -/
  theta_gen : ∀ i, 1 ≤ i → i ≤ n - 1 → θ (T i) = T (n - i)
  /-- **The fold is a `ℤ/2` on `A`.** On the generators this follows from `theta_gen`; on
  all of `A` it is an assumption, since `A` need not be generated by the `T i`. -/
  theta_involutive : ∀ x, θ (θ x) = x
  /-- **Stable matter = the `θ`-fixed elements.** -/
  stable_iff_fixed : ∀ x, stable x ↔ θ x = x
  /-- **Antimatter = the elements `θ` moves.** -/
  anti_iff_moved : ∀ x, anti x ↔ θ x ≠ x

/-! ### Consequences -/

section Consequences

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A] {n : ℕ} {h : R} {T : ℕ → A}
  {θ : A →ₐ[R] A} {stable anti : A → Prop}

/-- **Swapped pairs give stable matter.** For `i + 2 ≤ n - i`, the product `T i * T (n-i)`
(the image of the folded generator `sᵢ s_{n-i}`, of length 2) is `θ`-fixed. -/
theorem typeBFold_pair_fixed [hc : TypeBFoldingCpt R A n h T θ stable anti]
    {i : ℕ} (hi : 1 ≤ i) (hgap : i + 2 ≤ n - i) :
    stable (T i * T (n - i)) := by
  rw [hc.stable_iff_fixed, map_mul, hc.theta_gen i hi (by omega),
    hc.theta_gen (n - i) (by omega) (by omega)]
  have e : n - (n - i) = i := by omega
  rw [e]
  exact (hc.braid_far i (n - i) hi (by omega) hgap).symm

/-- **The middle orbit gives stable matter at odd `n`.** For `n = 2m + 1` with `m ≥ 1`, the
element `T m * T (m+1) * T m` (the image of `s_m s_{m+1} s_m`, of length 3) is `θ`-fixed.
This is where the braid relation is used. -/
theorem typeBFold_middle_fixed [hc : TypeBFoldingCpt R A n h T θ stable anti]
    {m : ℕ} (hm : 1 ≤ m) (hn : n = 2 * m + 1) :
    stable (T m * T (m + 1) * T m) := by
  rw [hc.stable_iff_fixed, map_mul, map_mul, hc.theta_gen m hm (by omega),
    hc.theta_gen (m + 1) (by omega) (by omega)]
  have e1 : n - m = m + 1 := by omega
  have e2 : n - (m + 1) = m := by omega
  rw [e1, e2]
  exact (hc.braid_near m hm (by omega)).symm

/-- **The fixed root at even `n`.** For `n = 2i`, the generator `T i` is stable. -/
theorem typeBFold_fixed_root [hc : TypeBFoldingCpt R A n h T θ stable anti]
    {i : ℕ} (hi : 1 ≤ i) (hn : n = 2 * i) :
    stable (T i) := by
  rw [hc.stable_iff_fixed, hc.theta_gen i hi (by omega)]
  have e : n - i = i := by omega
  rw [e]

/-- **A generator is antimatter exactly when it is not the middle root of an even `n`.** -/
theorem typeBFold_gen_anti_iff [hc : TypeBFoldingCpt R A n h T θ stable anti]
    {i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    anti (T i) ↔ n ≠ 2 * i := by
  rw [hc.anti_iff_moved, hc.theta_gen i hi hi']
  constructor
  · intro hne heq
    apply hne
    have e : n - i = i := by omega
    rw [e]
  · intro hne
    exact hc.gens_ne (n - i) i (by omega) (by omega) hi hi' (by omega)

/-- **For odd `n` every generator is antimatter.** -/
theorem typeBFold_gen_anti_of_odd [hc : TypeBFoldingCpt R A n h T θ stable anti]
    (hodd : ¬ 2 ∣ n) {i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    anti (T i) :=
  (typeBFold_gen_anti_iff (hc := hc) hi hi').mpr (fun he => hodd ⟨i, he⟩)

/-- **Matter and antimatter partition `A`.** -/
theorem typeBFold_stable_iff_not_anti [hc : TypeBFoldingCpt R A n h T θ stable anti]
    (x : A) : stable x ↔ ¬ anti x := by
  rw [hc.stable_iff_fixed x, hc.anti_iff_moved x]
  simp

/-- **If stable matter exists, `A` carries no globally `θ`-odd chirality grading.** If
`θ x = x` then any `chir` with `chir (θ w) = !chir w` gives `chir x = !chir x`. Compare
`QOU.StandardModel.Chirality.stable_matter_and_global_chirality_incompatible`. -/
theorem typeBFold_no_global_chirality_grading [hc : TypeBFoldingCpt R A n h T θ stable anti]
    {x : A} (hx : stable x) :
    ¬ ∃ chir : A → Bool, ∀ w, chir (θ w) = ! chir w := by
  rintro ⟨chir, hodd⟩
  have hfix : θ x = x := (hc.stable_iff_fixed x).mp hx
  have hx' := hodd x
  rw [hfix] at hx'
  simp at hx'

end Consequences

/-! ### Refutability

Each witness below is commutative (`A = ℚ`) and fails the named field. None of them is
shown to satisfy every other field, so each shows that its field is not vacuous on caller
data; it does not show that the remaining fields are jointly satisfiable. -/

/-- **The quadratic leg is refutable**: zero generators fail `T i * T i = h • T i + 1`. -/
theorem typeBFoldingCpt_refutable_quadratic :
    ¬ TypeBFoldingCpt ℚ ℚ 3 0 (fun _ => 0) (AlgHom.id ℚ ℚ) (fun _ => True) (fun _ => False) := by
  intro hc
  have hq := hc.quadratic 1 (by norm_num) (by norm_num)
  norm_num at hq

/-- **The distinctness leg is refutable**: constant generators `T i = 1` with `h = 0`
satisfy the quadratic relation, both braid relations and `θ = id` lifting the reversal,
and fail because `T 1 = T 2`. -/
theorem typeBFoldingCpt_refutable_distinct :
    ¬ TypeBFoldingCpt ℚ ℚ 3 0 (fun _ => 1) (AlgHom.id ℚ ℚ) (fun _ => True) (fun _ => False) := by
  intro hc
  exact hc.gens_ne 1 2 (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num) rfl

/-- **The fold leg is refutable**: with distinct generators `T i = i` on `ℚ`, the identity
map does not send `T 1` to `T 2`. -/
theorem typeBFoldingCpt_refutable_fold :
    ¬ TypeBFoldingCpt ℚ ℚ 3 0 (fun i => (i : ℚ)) (AlgHom.id ℚ ℚ) (fun _ => True)
      (fun _ => False) := by
  intro hc
  have hf := hc.theta_gen 1 (by norm_num) (by norm_num)
  norm_num at hf

/-- **The matter leg is refutable**: calling every element antimatter fails at `0`, which
every algebra map fixes. -/
theorem typeBFoldingCpt_refutable_matter :
    ¬ TypeBFoldingCpt ℚ ℚ 3 0 (fun _ => 1) (AlgHom.id ℚ ℚ) (fun _ => False) (fun _ => True) := by
  intro hc
  exact ((hc.anti_iff_moved 0).mp trivial) (by simp)

end QOU.BraidsAndKnots
